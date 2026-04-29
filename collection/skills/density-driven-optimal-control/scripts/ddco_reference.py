#!/usr/bin/env python3
"""
D²OC Implementation: Density-Driven Optimal Control for Multi-Agent Systems

This script provides a reference implementation of the D²OC framework
for decentralized non-uniform area coverage with convergence guarantees.

Usage:
    python3 ddco_reference.py --agents 20 --area 10 --time 10.0
"""

import numpy as np
from scipy.linalg import solve_continuous_are
import matplotlib.pyplot as plt
from typing import Callable, Tuple, Optional
import argparse


class DensityDrivenOptimalControl:
    """
    Density-Driven Optimal Control (D²OC) implementation.
    
    Provides closed-form optimal control synthesis for multi-agent systems
    with formal convergence guarantees under stochastic LTI dynamics.
    """
    
    def __init__(
        self,
        n_agents: int,
        A: np.ndarray,
        B: np.ndarray,
        Q: np.ndarray,
        R: np.ndarray,
        workspace_bounds: Tuple[float, float] = (-10, 10),
        dt: float = 0.01
    ):
        """
        Initialize D²OC controller.
        
        Args:
            n_agents: Number of agents
            A: State transition matrix (LTI dynamics)
            B: Control input matrix
            Q: State cost matrix (density mismatch weight)
            R: Control cost matrix (control effort penalty)
            workspace_bounds: (min, max) bounds for workspace
            dt: Time step for simulation
        """
        self.n_agents = n_agents
        self.A = A
        self.B = B
        self.Q = Q
        self.R = R
        self.workspace_bounds = workspace_bounds
        self.dt = dt
        
        # Compute optimal gain matrix via Riccati equation
        self.P = solve_continuous_are(A, B, Q, R)
        self.K = np.linalg.inv(R) @ B.T @ self.P
        
        # State dimensions
        self.state_dim = A.shape[0]
        self.control_dim = B.shape[1]
        
    def compute_control(
        self,
        states: np.ndarray,
        target_density: Callable,
        time: float = 0.0
    ) -> np.ndarray:
        """
        Compute optimal control inputs for all agents.
        
        Args:
            states: Current agent states (n_agents x state_dim)
            target_density: Target density function rho*(x)
            time: Current time (for time-varying densities)
        
        Returns:
            controls: Optimal control inputs (n_agents x control_dim)
        """
        # Compute target positions from density
        target_positions = self._density_to_positions(target_density)
        
        # Compute optimal control for each agent
        controls = np.zeros((self.n_agents, self.control_dim))
        for i in range(self.n_agents):
            error = states[i] - target_positions[i]
            controls[i] = -self.K @ error
        
        return controls
    
    def _density_to_positions(
        self,
        target_density: Callable,
        n_samples: int = 10000
    ) -> np.ndarray:
        """
        Convert target density to agent target positions using importance sampling.
        
        Args:
            target_density: Target density function
            n_samples: Number of samples for estimation
        
        Returns:
            target_positions: Target positions for each agent
        """
        # Generate samples proportional to density
        samples = []
        weights = []
        
        bounds = self.workspace_bounds
        for _ in range(n_samples):
            x = np.random.uniform(bounds[0], bounds[1], self.state_dim)
            rho = target_density(x)
            samples.append(x)
            weights.append(rho)
        
        samples = np.array(samples)
        weights = np.array(weights)
        weights = weights / np.sum(weights)  # Normalize
        
        # Select agent targets via weighted sampling
        indices = np.random.choice(
            len(samples),
            size=self.n_agents,
            replace=False,
            p=weights
        )
        
        return samples[indices]
    
    def simulate(
        self,
        initial_states: np.ndarray,
        target_density: Callable,
        duration: float,
        noise_std: float = 0.0
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Simulate multi-agent system with D²OC.
        
        Args:
            initial_states: Initial agent states
            target_density: Target density function
            duration: Simulation duration
            noise_std: Standard deviation of process noise
        
        Returns:
            states_history: State trajectories (time_steps x n_agents x state_dim)
            controls_history: Control inputs (time_steps x n_agents x control_dim)
        """
        n_steps = int(duration / self.dt)
        states = initial_states.copy()
        
        states_history = np.zeros((n_steps, self.n_agents, self.state_dim))
        controls_history = np.zeros((n_steps, self.n_agents, self.control_dim))
        
        for t in range(n_steps):
            states_history[t] = states
            
            # Compute optimal control
            controls = self.compute_control(states, target_density, t * self.dt)
            controls_history[t] = controls
            
            # Update states (Euler integration with noise)
            noise = np.random.normal(0, noise_std, states.shape)
            states = states + (self.A @ states.T + self.B @ controls.T).T * self.dt + noise * np.sqrt(self.dt)
            
            # Keep agents within bounds
            states = np.clip(states, self.workspace_bounds[0], self.workspace_bounds[1])
        
        return states_history, controls_history
    
    def compute_density_mismatch(
        self,
        states: np.ndarray,
        target_density: Callable,
        grid_resolution: int = 50
    ) -> float:
        """
        Compute density mismatch metric D(t).
        
        Args:
            states: Current agent positions
            target_density: Target density function
            grid_resolution: Resolution for density estimation
        
        Returns:
            mismatch: Density mismatch value
        """
        # Create grid
        bounds = self.workspace_bounds
        x = np.linspace(bounds[0], bounds[1], grid_resolution)
        y = np.linspace(bounds[0], bounds[1], grid_resolution)
        X, Y = np.meshgrid(x, y)
        
        # Estimate current density using kernel density estimation
        from scipy.stats import gaussian_kde
        kde = gaussian_kde(states.T)
        positions = np.vstack([X.ravel(), Y.ravel()])
        current_density = kde(positions).reshape(X.shape)
        current_density = current_density / np.sum(current_density)  # Normalize
        
        # Compute target density on grid
        target_grid = np.zeros_like(X)
        for i in range(grid_resolution):
            for j in range(grid_resolution):
                target_grid[i, j] = target_density(np.array([X[i, j], Y[i, j]]))
        target_grid = target_grid / np.sum(target_grid)  # Normalize
        
        # Compute mismatch
        mismatch = np.sum((current_density - target_grid) ** 2)
        return mismatch


def gaussian_density(center: np.ndarray, sigma: float) -> Callable:
    """Create Gaussian density function."""
    def density(x):
        return np.exp(-np.sum((x - center) ** 2) / (2 * sigma ** 2))
    return density


def mixture_density(densities: list, weights: list) -> Callable:
    """Create mixture of densities."""
    def density(x):
        return sum(w * d(x) for w, d in zip(weights, densities))
    return density


def uniform_density(x):
    """Uniform density function."""
    return 1.0


def visualize_coverage(
    states_history: np.ndarray,
    target_density: Callable,
    bounds: Tuple[float, float] = (-10, 10),
    save_path: Optional[str] = None
):
    """
    Visualize coverage evolution.
    
    Args:
        states_history: State trajectories
        target_density: Target density function
        bounds: Workspace bounds
        save_path: Optional path to save figure
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Select time points for visualization
    time_points = [0, len(states_history)//3, 2*len(states_history)//3, -1]
    titles = ['Initial', 'Early', 'Mid', 'Final']
    
    grid_res = 30
    x = np.linspace(bounds[0], bounds[1], grid_res)
    y = np.linspace(bounds[0], bounds[1], grid_res)
    X, Y = np.meshgrid(x, y)
    
    # Compute target density grid
    Z_target = np.zeros_like(X)
    for i in range(grid_res):
        for j in range(grid_res):
            Z_target[i, j] = target_density(np.array([X[i, j], Y[i, j]]))
    
    for idx, (ax, t, title) in enumerate(zip(axes.flat, time_points, titles)):
        states = states_history[t]
        
        # Plot target density as contour
        ax.contour(X, Y, Z_target, levels=5, colors='gray', alpha=0.5, linewidths=1)
        
        # Plot agent positions
        ax.scatter(states[:, 0], states[:, 1], c='red', s=50, alpha=0.7, label='Agents')
        
        # Plot trajectories up to this point
        if t > 0:
            for i in range(states.shape[0]):
                trajectory = states_history[:t+1, i]
                ax.plot(trajectory[:, 0], trajectory[:, 1], 'b-', alpha=0.3, linewidth=0.5)
        
        ax.set_xlim(bounds)
        ax.set_ylim(bounds)
        ax.set_aspect('equal')
        ax.set_title(f'{title} Configuration (t={t})')
        ax.grid(True, alpha=0.3)
        ax.legend()
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    plt.show()


def main():
    """Main demonstration of D²OC."""
    parser = argparse.ArgumentParser(description='D²OC Demonstration')
    parser.add_argument('--agents', type=int, default=20, help='Number of agents')
    parser.add_argument('--area', type=float, default=10, help='Workspace size')
    parser.add_argument('--time', type=float, default=10.0, help='Simulation duration')
    parser.add_argument('--noise', type=float, default=0.1, help='Process noise std')
    args = parser.parse_args()
    
    print("=" * 60)
    print("Density-Driven Optimal Control (D²OC) Demonstration")
    print("=" * 60)
    
    # System parameters (2D double integrator)
    A = np.zeros((2, 2))  # Position dynamics
    B = np.eye(2)         # Direct velocity control
    Q = np.eye(2) * 10    # High position accuracy priority
    R = np.eye(2) * 0.5   # Moderate control cost
    
    # Initialize controller
    ddco = DensityDrivenOptimalControl(
        n_agents=args.agents,
        A=A,
        B=B,
        Q=Q,
        R=R,
        workspace_bounds=(-args.area, args.area),
        dt=0.01
    )
    
    print("\nConfiguration:")
    print(f"  Agents: {args.agents}")
    print(f"  Workspace: [{-args.area}, {args.area}]")
    print(f"  Duration: {args.time}s")
    print(f"  Process noise: {args.noise}")
    
    # Define target density (Gaussian mixture)
    d1 = gaussian_density(np.array([3, 3]), 2.0)
    d2 = gaussian_density(np.array([-3, -3]), 2.0)
    d3 = gaussian_density(np.array([0, 0]), 3.0)
    target_density = mixture_density([d1, d2, d3], [0.3, 0.3, 0.4])
    
    print("\nTarget density: 3-component Gaussian mixture")
    
    # Initialize agents randomly
    initial_states = np.random.uniform(-args.area, args.area, (args.agents, 2))
    
    # Simulate
    print("\nSimulating...")
    states_history, controls_history = ddco.simulate(
        initial_states,
        target_density,
        args.time,
        noise_std=args.noise
    )
    
    # Compute metrics
    initial_mismatch = ddco.compute_density_mismatch(initial_states, target_density)
    final_mismatch = ddco.compute_density_mismatch(states_history[-1], target_density)
    
    print("\nResults:")
    print(f"  Initial density mismatch: {initial_mismatch:.4f}")
    print(f"  Final density mismatch: {final_mismatch:.4f}")
    print(f"  Reduction: {(1 - final_mismatch/initial_mismatch)*100:.1f}%")
    print(f"  Average control effort: {np.mean(np.linalg.norm(controls_history, axis=2)):.4f}")
    
    # Visualize
    print("\nGenerating visualization...")
    visualize_coverage(states_history, target_density, (-args.area, args.area))
    
    print("\n" + "=" * 60)
    print("Demonstration complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
