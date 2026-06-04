"""Transport-based mean field simulation for integrate-and-fire neural populations.

Based on arXiv:2605.14319 - approximate macroscopic dynamics via transport solution.
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def gaussian_initial(v, v_mean=0.5, v_std=0.1):
    """Gaussian initial voltage distribution."""
    return np.exp(-0.5 * ((v - v_mean) / v_std) ** 2) / (v_std * np.sqrt(2 * np.pi))


def transport_meanfield(v0_dist, mu_func, v_reset=-1.0, v_thresh=1.0,
                        n_grid=2000, dt=0.01, T=50.0, coupling=0.0):
    """Transport-based mean field for IF population.

    Args:
        v0_dist: callable, initial voltage distribution
        mu_func: callable(t), time-varying input current
        v_reset: reset potential
        v_thresh: threshold potential
        n_grid: number of voltage grid points
        dt: time step
        T: total simulation time
        coupling: recurrent coupling strength (J times synaptic weight)

    Returns:
        times: array of time points
        flux: array of instantaneous firing rates
        rho_history: voltage density history (optional, shape=(n_steps, n_grid))
    """
    v_grid = np.linspace(v_reset, v_thresh, n_grid)
    dv = v_grid[1] - v_grid[0]
    rho = v0_dist(v_grid)
    rho = rho / np.trapz(rho, v_grid)  # normalize

    n_steps = int(T / dt)
    times = np.zeros(n_steps)
    flux = np.zeros(n_steps)

    for i in range(n_steps):
        t = i * dt
        mu = mu_func(t) + coupling * flux[i - 1] if i > 0 else mu_func(t)

        # Upwind transport scheme
        if mu > 0:
            rho_new = np.zeros_like(rho)
            rho_new[1:] = rho[:-1]
            rho_new[0] = 0.0
        else:
            rho_new = np.zeros_like(rho)
            rho_new[:-1] = rho[1:]
            rho_new[-1] = 0.0

        # Compute flux at threshold
        J = max(mu, 0) * rho[-1]
        flux[i] = J
        times[i] = t

        # Reset: spiking neurons return to reset
        if J > 0:
            idx = int((v_reset - v_reset) / dv)
            rho_new[idx] += J * dt / dv

        # Update density
        rho = rho_new

        # Normalize to prevent drift
        total = np.trapz(rho, v_grid)
        if total > 0:
            rho /= total

    return times, flux


def plot_results(times, flux, title="Transport Mean Field", save_path=None):
    """Plot firing rate dynamics."""
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(times, flux, 'b-', linewidth=1.5)
    ax.set_xlabel('Time (ms)')
    ax.set_ylabel('Firing Rate (Hz)')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"Saved figure to {save_path}")
    plt.close()


if __name__ == "__main__":
    # Example: constant input
    mu0 = 0.5
    mu_func = lambda t: mu0

    times, flux = transport_meanfield(
        v0_dist=gaussian_initial,
        mu_func=mu_func,
        coupling=0.0,
        T=100.0,
        dt=0.005
    )

    plot_results(times, flux,
                 title="Transport Mean Field - Constant Input",
                 save_path="/tmp/transport_meanfield_demo.png")
    print(f"Mean firing rate: {np.mean(flux[1000:]):.4f}")
    print(f"Peak firing rate: {np.max(flux):.4f}")
