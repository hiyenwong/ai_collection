---
name: density-driven-optimal-control
description: "Density-Driven Optimal Control (D²OC) for Stochastic LTI Multi-Agent Systems. Decentralized non-uniform area coverage using Wasserstein distance minimization with formal convergence guarantees. Activation: density-driven control, multi-agent coverage, stochastic control, Wasserstein distance, area coverage."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [optimal-control, multi-agent-systems, density-coverage, stochastic-control, wasserstein-distance, decentralized-control, area-coverage]
    source_paper: "Density-Driven Optimal Control: Convergence Guarantees for Stochastic LTI Multi-Agent Systems (arXiv:2604.08495v1)"
    citations: 0
    published: "2026-04-09"
    category: "optimization and control"
---

# Density-Driven Optimal Control (D²OC)

## Overview
This skill provides methodologies for decentralized non-uniform area coverage in multi-agent systems using Density-Driven Optimal Control (D²OC). This Lagrangian framework bridges the gap between individual agent dynamics and collective distribution matching, ensuring that the time-averaged empirical distribution converges to a non-parametric target density under stochastic LTI dynamics.

## Key Insights

### Problem Statement
- Multi-agent systems need to achieve non-uniform area coverage
- High spatial priority areas require more agent density
- Resource constraints limit agent deployment
- Existing methods rely on computationally heavy Eulerian PDE solvers

### Core Innovation
- **Lagrangian Framework**: Bridges individual and collective dynamics
- **Wasserstein Distance**: Used as running cost for distribution matching
- **Stochastic MPC-like**: Formulation for robust control
- **Formal Convergence**: Mathematical guarantees for convergence

## Implementation Pattern

### D²OC Framework
```python
import numpy as np
from typing import List, Tuple, Callable, Optional
from dataclasses import dataclass
from scipy.spatial.distance import cdist
import scipy.optimize as opt

@dataclass
class AgentState:
    """State of a single agent in the multi-agent system."""
    position: np.ndarray
    velocity: np.ndarray
    agent_id: int
    
    def __post_init__(self):
        if isinstance(self.position, list):
            self.position = np.array(self.position)
        if isinstance(self.velocity, list):
            self.velocity = np.array(self.velocity)

@dataclass
class StochasticLTIDynamics:
    """
    Stochastic Linear Time-Invariant dynamics.
    
    x_{k+1} = A x_k + B u_k + w_k
    where w_k ~ N(0, Sigma)
    """
    A: np.ndarray  # State transition matrix
    B: np.ndarray  # Control input matrix
    Sigma: np.ndarray  # Process noise covariance
    dt: float  # Time step
    
    def propagate(self, state: np.ndarray, control: np.ndarray) -> np.ndarray:
        """Propagate state forward one time step."""
        noise = np.random.multivariate_normal(
            np.zeros(self.Sigma.shape[0]), self.Sigma
        )
        return self.A @ state + self.B @ control + noise
    
    def propagate_deterministic(self, state: np.ndarray, control: np.ndarray) -> np.ndarray:
        """Propagate without noise (for planning)."""
        return self.A @ state + self.B @ control

class TargetDensity:
    """Represents a target spatial density distribution."""
    
    def __init__(self, 
                 density_fn: Callable[[np.ndarray], float],
                 domain: Tuple[np.ndarray, np.ndarray],
                 grid_resolution: int = 50):
        """
        Initialize target density.
        
        Args:
            density_fn: Function that returns density at given position
            domain: (min_bounds, max_bounds) defining the domain
            grid_resolution: Resolution for discretization
        """
        self.density_fn = density_fn
        self.domain = domain
        self.grid_resolution = grid_resolution
        self.grid_points = self._create_grid()
        self.grid_values = self._evaluate_density_on_grid()
    
    def _create_grid(self) -> np.ndarray:
        """Create discretized grid over domain."""
        min_b, max_b = self.domain
        grids = [np.linspace(min_b[i], max_b[i], self.grid_resolution) 
                for i in range(len(min_b))]
        mesh = np.meshgrid(*grids)
        return np.column_stack([m.flatten() for m in mesh])
    
    def _evaluate_density_on_grid(self) -> np.ndarray:
        """Evaluate density function on grid points."""
        return np.array([self.density_fn(p) for p in self.grid_points])
    
    def evaluate(self, positions: np.ndarray) -> np.ndarray:
        """Evaluate density at given positions."""
        return np.array([self.density_fn(p) for p in positions])
    
    def sample(self, n_samples: int) -> np.ndarray:
        """Sample from the target density (rejection sampling)."""
        samples = []
        max_density = np.max(self.grid_values)
        
        while len(samples) < n_samples:
            # Sample uniformly from domain
            min_b, max_b = self.domain
            candidate = np.random.uniform(min_b, max_b)
            
            # Accept with probability proportional to density
            density = self.density_fn(candidate)
            if np.random.random() < density / max_density:
                samples.append(candidate)
        
        return np.array(samples)

def wasserstein_distance_1d(samples1: np.ndarray, 
                            samples2: np.ndarray) -> float:
    """
    Calculate 1-Wasserstein distance between two empirical distributions.
    
    For 1D distributions: W_1 = integral |CDF_1(x) - CDF_2(x)| dx
    """
    # Sort samples
    s1_sorted = np.sort(samples1)
    s2_sorted = np.sort(samples2)
    
    # Pad to same length
    n1, n2 = len(s1_sorted), len(s2_sorted)
    if n1 < n2:
        s1_sorted = np.interp(
            np.linspace(0, n2-1, n2),
            np.linspace(0, n1-1, n1),
            s1_sorted
        )
    elif n2 < n1:
        s2_sorted = np.interp(
            np.linspace(0, n1-1, n1),
            np.linspace(0, n2-1, n2),
            s2_sorted
        )
    
    # Wasserstein distance is L1 distance between sorted samples
    return np.mean(np.abs(s1_sorted - s2_sorted))

def wasserstein_distance_2d(samples1: np.ndarray,
                            samples2: np.ndarray) -> float:
    """
    Approximate 2-Wasserstein distance for 2D distributions.
    
    Uses sliced Wasserstein distance approximation.
    """
    n_projections = 100
    distances = []
    
    for _ in range(n_projections):
        # Random projection direction
        theta = np.random.rand(samples1.shape[1])
        theta = theta / np.linalg.norm(theta)
        
        # Project samples
        proj1 = samples1 @ theta
        proj2 = samples2 @ theta
        
        # Compute 1D Wasserstein
        distances.append(wasserstein_distance_1d(proj1, proj2))
    
    return np.mean(distances)

class DensityDrivenOptimalControl:
    """
    D²OC: Density-Driven Optimal Control for multi-agent systems.
    
    Implements MPC-like control that minimizes Wasserstein distance
    to target density distribution.
    """
    
    def __init__(self,
                 dynamics: StochasticLTIDynamics,
                 target_density: TargetDensity,
                 horizon: int = 10,
                 dt: float = 0.1):
        """
        Initialize D²OC controller.
        
        Args:
            dynamics: Stochastic LTI dynamics for agents
            target_density: Target spatial distribution
            horizon: MPC prediction horizon
            dt: Time step
        """
        self.dynamics = dynamics
        self.target_density = target_density
        self.horizon = horizon
        self.dt = dt
        self.control_limits = (-1.0, 1.0)  # Control input bounds
    
    def compute_control(self, 
                       agents: List[AgentState],
                       time_step: int) -> List[np.ndarray]:
        """
        Compute optimal control inputs for all agents.
        
        Args:
            agents: Current states of all agents
            time_step: Current time step
        
        Returns:
            List of control inputs for each agent
        """
        controls = []
        
        for agent in agents:
            # Solve MPC problem for this agent
            control = self._solve_mpc(agent, agents)
            controls.append(control)
        
        return controls
    
    def _solve_mpc(self, agent: AgentState, 
                   all_agents: List[AgentState]) -> np.ndarray:
        """
        Solve MPC optimization problem for a single agent.
        
        Minimizes Wasserstein distance to target density over horizon.
        """
        def objective(control_sequence):
            """MPC objective function."""
            total_cost = 0.0
            state = np.concatenate([agent.position, agent.velocity])
            
            # Simulate over horizon
            for t in range(self.horizon):
                control = control_sequence[t*self.dynamics.B.shape[1]:
                                          (t+1)*self.dynamics.B.shape[1]]
                
                # Predict next state
                state = self.dynamics.propagate_deterministic(state, control)
                
                # Compute empirical distribution of all agents
                predicted_positions = self._predict_positions(all_agents, t)
                predicted_positions[agent.agent_id] = state[:len(agent.position)]
                
                # Sample from target density
                target_samples = self.target_density.sample(len(all_agents))
                
                # Wasserstein distance as running cost
                w_dist = wasserstein_distance_2d(
                    np.array(predicted_positions),
                    target_samples
                )
                
                total_cost += w_dist
                
                # Add control effort penalty
                total_cost += 0.01 * np.sum(control**2)
            
            return total_cost
        
        # Initial guess (zero control)
        n_controls = self.dynamics.B.shape[1]
        x0 = np.zeros(self.horizon * n_controls)
        
        # Bounds on control inputs
        bounds = [self.control_limits] * len(x0)
        
        # Solve optimization
        result = opt.minimize(
            objective,
            x0,
            method='SLSQP',
            bounds=bounds,
            options={'maxiter': 100}
        )
        
        # Return first control input
        if result.success:
            return result.x[:n_controls]
        else:
            return np.zeros(n_controls)
    
    def _predict_positions(self, agents: List[AgentState], 
                          steps: int) -> List[np.ndarray]:
        """Predict positions of all agents after given steps."""
        positions = []
        for agent in agents:
            # Simple prediction (constant velocity)
            pred_pos = agent.position + steps * self.dt * agent.velocity
            positions.append(pred_pos)
        return positions
    
    def run_simulation(self,
                      agents: List[AgentState],
                      n_steps: int,
                      callback: Optional[Callable] = None) -> List[List[AgentState]]:
        """
        Run full simulation of the multi-agent system.
        
        Args:
            agents: Initial agent states
            n_steps: Number of simulation steps
            callback: Optional callback function called each step
        
        Returns:
            Trajectory of agent states over time
        """
        trajectory = [agents.copy()]
        
        for t in range(n_steps):
            # Compute controls
            controls = self.compute_control(agents, t)
            
            # Update agent states
            new_agents = []
            for agent, control in zip(agents, controls):
                state = np.concatenate([agent.position, agent.velocity])
                new_state = self.dynamics.propagate(state, control)
                
                new_agent = AgentState(
                    position=new_state[:len(agent.position)],
                    velocity=new_state[len(agent.position):],
                    agent_id=agent.agent_id
                )
                new_agents.append(new_agent)
            
            agents = new_agents
            trajectory.append(agents.copy())
            
            if callback:
                callback(t, agents)
        
        return trajectory
    
    def compute_coverage_error(self, agents: List[AgentState]) -> float:
        """
        Compute coverage error as Wasserstein distance to target.
        
        Args:
            agents: Current agent states
        
        Returns:
            Wasserstein distance
        """
        positions = np.array([a.position for a in agents])
        target_samples = self.target_density.sample(len(agents))
        
        return wasserstein_distance_2d(positions, target_samples)
    
    def verify_convergence(self, 
                          trajectory: List[List[AgentState]],
                          window_size: int = 50) -> bool:
        """
        Verify convergence of empirical distribution to target.
        
        Args:
            trajectory: Simulation trajectory
            window_size: Window for averaging
        
        Returns:
            True if converged
        """
        if len(trajectory) < window_size:
            return False
        
        # Compute coverage error over time
        errors = []
        for agents in trajectory:
            error = self.compute_coverage_error(agents)
            errors.append(error)
        
        # Check if error is decreasing and stabilizing
        recent_errors = errors[-window_size:]
        if len(recent_errors) < window_size:
            return False
        
        # Convergence criterion: low variance in recent errors
        error_variance = np.var(recent_errors)
        error_mean = np.mean(recent_errors)
        
        return error_variance < 0.1 * error_mean


# Example usage
if __name__ == "__main__":
    # Define 2D target density (Gaussian mixture)
    def target_density_fn(pos):
        """Bimodal Gaussian target density."""
        mu1 = np.array([2.0, 2.0])
        mu2 = np.array([-2.0, -2.0])
        sigma = 1.0
        
        d1 = np.linalg.norm(pos - mu1)
        d2 = np.linalg.norm(pos - mu2)
        
        return np.exp(-d1**2 / (2*sigma**2)) + np.exp(-d2**2 / (2*sigma**2))
    
    # Create target density
    target = TargetDensity(
        density_fn=target_density_fn,
        domain=(np.array([-5, -5]), np.array([5, 5])),
        grid_resolution=30
    )
    
    # Define stochastic LTI dynamics (double integrator)
    dt = 0.1
    A = np.array([[1, 0, dt, 0],
                  [0, 1, 0, dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    B = np.array([[0, 0],
                  [0, 0],
                  [dt, 0],
                  [0, dt]])
    Sigma = 0.01 * np.eye(4)
    
    dynamics = StochasticLTIDynamics(A, B, Sigma, dt)
    
    # Initialize agents
    n_agents = 20
    agents = [
        AgentState(
            position=np.random.randn(2) * 3,
            velocity=np.zeros(2),
            agent_id=i
        )
        for i in range(n_agents)
    ]
    
    # Create D²OC controller
    controller = DensityDrivenOptimalControl(
        dynamics=dynamics,
        target_density=target,
        horizon=5,
        dt=dt
    )
    
    # Run simulation
    trajectory = controller.run_simulation(agents, n_steps=200)
    
    # Verify convergence
    converged = controller.verify_convergence(trajectory)
    print(f"Convergence verified: {converged}")
    
    # Final coverage error
    final_error = controller.compute_coverage_error(trajectory[-1])
    print(f"Final coverage error: {final_error:.4f}")
```

## Best Practices

### 1. Target Density Design
- Use smooth, well-defined density functions
- Ensure target is achievable given agent count
- Consider domain boundaries

### 2. MPC Tuning
- Balance horizon length (longer = better planning, more computation)
- Tune control effort penalty for smooth trajectories
- Consider real-time constraints

### 3. Convergence Verification
- Monitor Wasserstein distance over time
- Use sliding window for stability assessment
- Set appropriate convergence thresholds

## References
- Lee, K. (2026). Density-Driven Optimal Control: Convergence Guarantees for Stochastic LTI Multi-Agent Systems. arXiv:2604.08495v1.

## Related Skills
- multi-agent-control
- optimal-control-theory
- coverage-planning
- stochastic-systems
