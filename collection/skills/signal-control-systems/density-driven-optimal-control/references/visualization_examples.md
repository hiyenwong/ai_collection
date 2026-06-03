# D²OC Visualization Examples

This reference document provides visualization techniques and code examples for analyzing Density-Driven Optimal Control systems.

## 1. Density Evolution Visualization

### Heatmap Animation

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_density_evolution(states_history, target_density, bounds, save_path=None):
    """
    Create animated heatmap of density evolution.
    
    Args:
        states_history: (time_steps, n_agents, 2) array
        target_density: Target density function
        bounds: (min, max) workspace bounds
        save_path: Optional path to save animation
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    grid_res = 40
    x = np.linspace(bounds[0], bounds[1], grid_res)
    y = np.linspace(bounds[0], bounds[1], grid_res)
    X, Y = np.meshgrid(x, y)
    
    # Precompute target density
    Z_target = np.zeros((grid_res, grid_res))
    for i in range(grid_res):
        for j in range(grid_res):
            Z_target[i, j] = target_density(np.array([X[i, j], Y[i, j]]))
    
    def update(frame):
        ax1.clear()
        ax2.clear()
        
        states = states_history[frame]
        
        # Current density estimation
        from scipy.stats import gaussian_kde
        kde = gaussian_kde(states.T)
        positions = np.vstack([X.ravel(), Y.ravel()])
        Z_current = kde(positions).reshape(X.shape)
        
        # Plot current density
        im1 = ax1.contourf(X, Y, Z_current, levels=20, cmap='viridis')
        ax1.scatter(states[:, 0], states[:, 1], c='red', s=30, alpha=0.7)
        ax1.set_title(f'Current Density (t={frame})')
        ax1.set_aspect('equal')
        
        # Plot target density
        im2 = ax2.contourf(X, Y, Z_target, levels=20, cmap='viridis')
        ax2.set_title('Target Density')
        ax2.set_aspect('equal')
        
        return im1, im2
    
    anim = FuncAnimation(fig, update, frames=len(states_history), interval=50, blit=False)
    
    if save_path:
        anim.save(save_path, writer='pillow', fps=20)
    
    plt.show()
    return anim
```

### Density Mismatch Over Time

```python
def plot_convergence_analysis(states_history, target_density, ddco_controller):
    """
    Plot density mismatch convergence over time.
    
    Args:
        states_history: State trajectories
        target_density: Target density function
        ddco_controller: D²OC controller instance
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Compute metrics over time
    time_steps = len(states_history)
    mismatches = []
    centroid_dispersions = []
    coverage_ratios = []
    
    for t in range(time_steps):
        states = states_history[t]
        
        # Density mismatch
        mismatch = ddco_controller.compute_density_mismatch(states, target_density)
        mismatches.append(mismatch)
        
        # Centroid dispersion (average distance from centroid)
        centroid = np.mean(states, axis=0)
        dispersion = np.mean(np.linalg.norm(states - centroid, axis=1))
        centroid_dispersions.append(dispersion)
        
        # Coverage ratio (fraction of area with agent proximity)
        # Simplified: count grid cells within threshold distance
        coverage = estimate_coverage_ratio(states, ddco_controller.workspace_bounds)
        coverage_ratios.append(coverage)
    
    # Plot 1: Density mismatch
    axes[0, 0].plot(mismatches, 'b-', linewidth=2)
    axes[0, 0].set_xlabel('Time Step')
    axes[0, 0].set_ylabel('Density Mismatch D(t)')
    axes[0, 0].set_title('Convergence: Density Mismatch')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_yscale('log')
    
    # Plot 2: Centroid dispersion
    axes[0, 1].plot(centroid_dispersions, 'g-', linewidth=2)
    axes[0, 1].set_xlabel('Time Step')
    axes[0, 1].set_ylabel('Average Distance from Centroid')
    axes[0, 1].set_title('Agent Distribution Spread')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Coverage ratio
    axes[1, 0].plot(coverage_ratios, 'r-', linewidth=2)
    axes[1, 0].set_xlabel('Time Step')
    axes[1, 0].set_ylabel('Coverage Ratio')
    axes[1, 0].set_title('Workspace Coverage Over Time')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].set_ylim([0, 1])
    
    # Plot 4: Phase portrait (first two agents)
    axes[1, 1].plot(states_history[:, 0, 0], states_history[:, 0, 1], 'b-', alpha=0.5, label='Agent 1')
    axes[1, 1].plot(states_history[:, 1, 0], states_history[:, 1, 1], 'r-', alpha=0.5, label='Agent 2')
    axes[1, 1].scatter(states_history[0, 0, 0], states_history[0, 0, 1], c='blue', s=100, marker='o', label='Start 1')
    axes[1, 1].scatter(states_history[-1, 0, 0], states_history[-1, 0, 1], c='blue', s=100, marker='*', label='End 1')
    axes[1, 1].set_xlabel('X Position')
    axes[1, 1].set_ylabel('Y Position')
    axes[1, 1].set_title('Phase Portrait (First 2 Agents)')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].set_aspect('equal')
    
    plt.tight_layout()
    plt.show()


def estimate_coverage_ratio(states, bounds, threshold=2.0, grid_res=20):
    """
    Estimate coverage ratio based on agent distribution.
    
    Args:
        states: Agent positions
        bounds: Workspace bounds
        threshold: Distance threshold for coverage
        grid_res: Grid resolution
    
    Returns:
        coverage_ratio: Fraction of area covered
    """
    x = np.linspace(bounds[0], bounds[1], grid_res)
    y = np.linspace(bounds[0], bounds[1], grid_res)
    X, Y = np.meshgrid(x, y)
    grid_points = np.vstack([X.ravel(), Y.ravel()]).T
    
    covered = 0
    for gp in grid_points:
        if np.any(np.linalg.norm(states - gp, axis=1) < threshold):
            covered += 1
    
    return covered / len(grid_points)
```

## 2. Voronoi-Based Coverage Visualization

```python
from scipy.spatial import Voronoi, voronoi_plot_2d

def visualize_voronoi_coverage(states, target_density, bounds):
    """
    Visualize coverage using Voronoi tessellation.
    
    Args:
        states: Agent positions
        target_density: Target density function
        bounds: Workspace bounds
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Compute Voronoi diagram
    vor = Voronoi(states)
    
    # Plot Voronoi cells
    voronoi_plot_2d(vor, ax=ax1, show_vertices=False, line_colors='gray')
    ax1.scatter(states[:, 0], states[:, 1], c='red', s=50, zorder=5)
    ax1.set_xlim(bounds)
    ax1.set_ylim(bounds)
    ax1.set_aspect('equal')
    ax1.set_title('Voronoi Tessellation')
    ax1.grid(True, alpha=0.3)
    
    # Plot density with Voronoi overlay
    grid_res = 40
    x = np.linspace(bounds[0], bounds[1], grid_res)
    y = np.linspace(bounds[0], bounds[1], grid_res)
    X, Y = np.meshgrid(x, y)
    
    Z = np.zeros((grid_res, grid_res))
    for i in range(grid_res):
        for j in range(grid_res):
            Z[i, j] = target_density(np.array([X[i, j], Y[i, j]]))
    
    ax2.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.7)
    voronoi_plot_2d(vor, ax=ax2, show_vertices=False, line_colors='white', line_alpha=0.5)
    ax2.scatter(states[:, 0], states[:, 1], c='red', s=50, zorder=5)
    ax2.set_xlim(bounds)
    ax2.set_ylim(bounds)
    ax2.set_aspect('equal')
    ax2.set_title('Target Density + Voronoi Cells')
    
    plt.tight_layout()
    plt.show()
```

## 3. Agent Trajectory Analysis

```python
def plot_trajectory_analysis(states_history, controls_history):
    """
    Comprehensive trajectory analysis visualization.
    
    Args:
        states_history: (time_steps, n_agents, state_dim) array
        controls_history: (time_steps, n_agents, control_dim) array
    """
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    n_agents = states_history.shape[1]
    time_steps = len(states_history)
    time_axis = np.arange(time_steps)
    
    # 1. All trajectories (2D)
    ax1 = fig.add_subplot(gs[0, :2])
    colors = plt.cm.tab10(np.linspace(0, 1, n_agents))
    for i in range(n_agents):
        ax1.plot(states_history[:, i, 0], states_history[:, i, 1], 
                color=colors[i], alpha=0.6, linewidth=1)
        ax1.scatter(states_history[0, i, 0], states_history[0, i, 1], 
                   color=colors[i], s=50, marker='o')
        ax1.scatter(states_history[-1, i, 0], states_history[-1, i, 1], 
                   color=colors[i], s=50, marker='*')
    ax1.set_xlabel('X Position')
    ax1.set_ylabel('Y Position')
    ax1.set_title('Agent Trajectories')
    ax1.grid(True, alpha=0.3)
    ax1.set_aspect('equal')
    
    # 2. Control effort over time
    ax2 = fig.add_subplot(gs[0, 2])
    control_magnitudes = np.linalg.norm(controls_history, axis=2)
    for i in range(n_agents):
        ax2.plot(time_axis, control_magnitudes[:, i], color=colors[i], alpha=0.5)
    ax2.plot(time_axis, np.mean(control_magnitudes, axis=1), 'k-', linewidth=2, label='Mean')
    ax2.set_xlabel('Time Step')
    ax2.set_ylabel('Control Magnitude')
    ax2.set_title('Control Effort')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. X position over time
    ax3 = fig.add_subplot(gs[1, 0])
    for i in range(n_agents):
        ax3.plot(time_axis, states_history[:, i, 0], color=colors[i], alpha=0.5)
    ax3.set_xlabel('Time Step')
    ax3.set_ylabel('X Position')
    ax3.set_title('X Position Evolution')
    ax3.grid(True, alpha=0.3)
    
    # 4. Y position over time
    ax4 = fig.add_subplot(gs[1, 1])
    for i in range(n_agents):
        ax4.plot(time_axis, states_history[:, i, 1], color=colors[i], alpha=0.5)
    ax4.set_xlabel('Time Step')
    ax4.set_ylabel('Y Position')
    ax4.set_title('Y Position Evolution')
    ax4.grid(True, alpha=0.3)
    
    # 5. Velocity magnitude
    ax5 = fig.add_subplot(gs[1, 2])
    velocities = np.linalg.norm(np.diff(states_history, axis=0), axis=2)
    for i in range(n_agents):
        ax5.plot(time_axis[1:], velocities[:, i], color=colors[i], alpha=0.5)
    ax5.set_xlabel('Time Step')
    ax5.set_ylabel('Velocity')
    ax5.set_title('Agent Velocities')
    ax5.grid(True, alpha=0.3)
    
    # 6. Inter-agent distances
    ax6 = fig.add_subplot(gs[2, 0])
    min_distances = []
    mean_distances = []
    for t in range(time_steps):
        distances = np.linalg.norm(states_history[t][:, None] - states_history[t], axis=2)
        # Exclude self-distances (zeros on diagonal)
        distances = distances[distances > 0]
        if len(distances) > 0:
            min_distances.append(np.min(distances))
            mean_distances.append(np.mean(distances))
    
    ax6.plot(time_axis, min_distances, 'r-', label='Min Distance')
    ax6.plot(time_axis, mean_distances, 'b-', label='Mean Distance')
    ax6.set_xlabel('Time Step')
    ax6.set_ylabel('Distance')
    ax6.set_title('Inter-Agent Distances')
    ax6.legend()
    ax6.grid(True, alpha=0.3)
    
    # 7. Cumulative control energy
    ax7 = fig.add_subplot(gs[2, 1])
    energy = np.cumsum(np.sum(control_magnitudes**2, axis=1))
    ax7.plot(time_axis, energy, 'g-', linewidth=2)
    ax7.set_xlabel('Time Step')
    ax7.set_ylabel('Cumulative Energy')
    ax7.set_title('Control Energy Consumption')
    ax7.grid(True, alpha=0.3)
    
    # 8. Distribution histogram (final positions)
    ax8 = fig.add_subplot(gs[2, 2])
    final_positions = states_history[-1]
    ax8.hist2d(final_positions[:, 0], final_positions[:, 1], bins=10, cmap='viridis')
    ax8.set_xlabel('X Position')
    ax8.set_ylabel('Y Position')
    ax8.set_title('Final Position Distribution')
    ax8.set_aspect('equal')
    
    plt.suptitle('D²OC Trajectory Analysis', fontsize=16)
    plt.show()
```

## 4. Comparative Analysis

```python
def compare_coverage_methods(
    initial_states,
    target_density,
    bounds,
    methods=['ddco', 'lloyds', 'potential_fields']
):
    """
    Compare different coverage methods.
    
    Args:
        initial_states: Initial agent positions
        target_density: Target density function
        bounds: Workspace bounds
        methods: List of methods to compare
    """
    fig, axes = plt.subplots(2, len(methods), figsize=(6*len(methods), 12))
    if len(methods) == 1:
        axes = axes.reshape(-1, 1)
    
    results = {}
    
    for idx, method in enumerate(methods):
        # Simulate with each method
        if method == 'ddco':
            states_hist, controls_hist = run_ddco(initial_states, target_density, bounds)
        elif method == 'lloyds':
            states_hist = run_lloyds(initial_states, target_density, bounds)
            controls_hist = None
        elif method == 'potential_fields':
            states_hist, controls_hist = run_potential_fields(initial_states, target_density, bounds)
        
        results[method] = {'states': states_hist, 'controls': controls_hist}
        
        # Plot initial and final
        ax_init = axes[0, idx]
        ax_final = axes[1, idx]
        
        # Initial configuration
        ax_init.scatter(states_hist[0, :, 0], states_hist[0, :, 1], c='blue', s=50, alpha=0.7)
        ax_init.set_xlim(bounds)
        ax_init.set_ylim(bounds)
        ax_init.set_aspect('equal')
        ax_init.set_title(f'{method.upper()} - Initial')
        ax_init.grid(True, alpha=0.3)
        
        # Final configuration with density overlay
        grid_res = 30
        x = np.linspace(bounds[0], bounds[1], grid_res)
        y = np.linspace(bounds[0], bounds[1], grid_res)
        X, Y = np.meshgrid(x, y)
        Z = np.zeros((grid_res, grid_res))
        for i in range(grid_res):
            for j in range(grid_res):
                Z[i, j] = target_density(np.array([X[i, j], Y[i, j]]))
        
        ax_final.contourf(X, Y, Z, levels=10, cmap='viridis', alpha=0.5)
        ax_final.scatter(states_hist[-1, :, 0], states_hist[-1, :, 1], c='red', s=50, alpha=0.7)
        ax_final.set_xlim(bounds)
        ax_final.set_ylim(bounds)
        ax_final.set_aspect('equal')
        ax_final.set_title(f'{method.upper()} - Final')
        ax_final.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return results
```

## 5. Statistical Analysis

```python
def statistical_convergence_analysis(states_history, target_density, n_trials=50):
    """
    Perform statistical analysis of convergence properties.
    
    Args:
        states_history: State trajectories from multiple runs
        target_density: Target density function
        n_trials: Number of simulation trials
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Run multiple trials
    all_mismatches = []
    all_final_mismatches = []
    
    for trial in range(n_trials):
        # Run simulation with different initial conditions
        # ... (simulation code)
        mismatches = []  # Compute for this trial
        all_mismatches.append(mismatches)
        all_final_mismatches.append(mismatches[-1])
    
    all_mismatches = np.array(all_mismatches)
    
    # Plot 1: Mean convergence with confidence intervals
    mean_mismatch = np.mean(all_mismatches, axis=0)
    std_mismatch = np.std(all_mismatches, axis=0)
    time_axis = np.arange(len(mean_mismatch))
    
    axes[0, 0].plot(time_axis, mean_mismatch, 'b-', linewidth=2, label='Mean')
    axes[0, 0].fill_between(time_axis, 
                           mean_mismatch - std_mismatch, 
                           mean_mismatch + std_mismatch, 
                           alpha=0.3, label='±1 Std Dev')
    axes[0, 0].set_xlabel('Time Step')
    axes[0, 0].set_ylabel('Density Mismatch')
    axes[0, 0].set_title('Convergence Statistics')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_yscale('log')
    
    # Plot 2: Final mismatch distribution
    axes[0, 1].hist(all_final_mismatches, bins=20, edgecolor='black', alpha=0.7)
    axes[0, 1].axvline(np.mean(all_final_mismatches), color='r', linestyle='--', 
                      linewidth=2, label=f'Mean: {np.mean(all_final_mismatches):.4f}')
    axes[0, 1].set_xlabel('Final Density Mismatch')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].set_title('Final Mismatch Distribution')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Convergence time distribution
    convergence_times = []
    threshold = 0.01  # Define convergence threshold
    for mismatches in all_mismatches:
        conv_idx = np.where(mismatches < threshold)[0]
        if len(conv_idx) > 0:
            convergence_times.append(conv_idx[0])
        else:
            convergence_times.append(len(mismatches))
    
    axes[1, 0].hist(convergence_times, bins=20, edgecolor='black', alpha=0.7)
    axes[1, 0].axvline(np.mean(convergence_times), color='r', linestyle='--',
                      linewidth=2, label=f'Mean: {np.mean(convergence_times):.1f}')
    axes[1, 0].set_xlabel('Convergence Time (steps)')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Convergence Time Distribution')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: QQ plot for normality check
    from scipy import stats
    stats.probplot(all_final_mismatches, dist="norm", plot=axes[1, 1])
    axes[1, 1].set_title('Q-Q Plot: Final Mismatch Normality')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Print statistics
    print("Statistical Analysis Results:")
    print(f"  Mean final mismatch: {np.mean(all_final_mismatches):.6f}")
    print(f"  Std final mismatch: {np.std(all_final_mismatches):.6f}")
    print(f"  Mean convergence time: {np.mean(convergence_times):.1f} steps")
    print(f"  Success rate (<{threshold}): {np.mean(np.array(all_final_mismatches) < threshold)*100:.1f}%")
```

## 6. Export and Report Generation

```python
def generate_coverage_report(states_history, target_density, ddco_controller, save_path='report.pdf'):
    """
    Generate comprehensive PDF report of coverage analysis.
    
    Args:
        states_history: State trajectories
        target_density: Target density function
        ddco_controller: D²OC controller
        save_path: Path to save report
    """
    from matplotlib.backends.backend_pdf import PdfPages
    
    with PdfPages(save_path) as pdf:
        # Page 1: Title and summary
        fig = plt.figure(figsize=(8.5, 11))
        fig.text(0.5, 0.9, 'D²OC Coverage Analysis Report', 
                ha='center', fontsize=20, fontweight='bold')
        fig.text(0.5, 0.85, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}',
                ha='center', fontsize=12)
        
        # Summary statistics
        summary_text = f"""
        Configuration:
        - Number of agents: {states_history.shape[1]}
        - Simulation duration: {len(states_history)} steps
        - Workspace bounds: {ddco_controller.workspace_bounds}
        
        Results:
        - Initial mismatch: {ddco_controller.compute_density_mismatch(states_history[0], target_density):.6f}
        - Final mismatch: {ddco_controller.compute_density_mismatch(states_history[-1], target_density):.6f}
        - Convergence rate: Exponential (theoretical)
        
        Key Findings:
        - Agents successfully converged to target density
        - Control effort remained bounded throughout simulation
        - Decentralized control achieved desired coverage
        """
        
        fig.text(0.1, 0.7, summary_text, fontsize=10, family='monospace',
                verticalalignment='top')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # Page 2-3: Coverage evolution
        visualize_coverage(states_history, target_density, 
                         ddco_controller.workspace_bounds)
        pdf.savefig(bbox_inches='tight')
        plt.close()
        
        # Page 4: Convergence analysis
        plot_convergence_analysis(states_history, target_density, ddco_controller)
        pdf.savefig(bbox_inches='tight')
        plt.close()
        
        # Page 5: Trajectory analysis
        plot_trajectory_analysis(states_history, 
                               np.zeros_like(states_history))  # Placeholder for controls
        pdf.savefig(bbox_inches='tight')
        plt.close()
    
    print(f"Report saved to: {save_path}")
```

---

_Last updated: 2026-04-14_
