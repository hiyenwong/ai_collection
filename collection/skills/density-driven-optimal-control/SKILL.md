---
name: density-driven-optimal-control
description: "Density-Driven Optimal Control (D²OC) for multi-agent systems. Analytical framework for decentralized non-uniform area coverage with convergence guarantees for stochastic LTI systems. Use when: (1) Designing density-based multi-agent control systems, (2) Solving optimal coverage problems with formal guarantees, (3) Implementing decentralized control for robotic swarms, (4) Developing resource-constrained area coverage missions, (5) Analyzing convergence of stochastic multi-agent dynamics. Activation: density-driven control, D2OC, multi-agent coverage, optimal control, density tracking, LTI systems."
---

# Density-Driven Optimal Control (D²OC)

## Overview

This skill provides methodology for **Density-Driven Optimal Control** - a framework that synthesizes density-based control with optimal control theory for multi-agent systems. The approach enables decentralized non-uniform area coverage with formal convergence guarantees, avoiding expensive spatial discretization while scaling linearly with the number of agents.

**Key Innovation**: Instead of computationally heavy Eulerian PDE solvers or heuristic planning, this framework derives closed-form analytical solutions for the optimal control problem with provable convergence properties.

## When to Use This Skill

### Primary Use Cases

1. **Decentralized Area Coverage**: Designing multi-agent systems for non-uniform coverage missions with spatial priority maps
2. **Resource-Constrained Missions**: When computational resources are limited and real-time control synthesis is required
3. **Formal Guarantee Requirements**: When convergence guarantees and error bounds are critical (e.g., safety-critical applications)
4. **Scalable Swarm Control**: Systems where the number of agents varies or grows
5. **Stochastic Environment Control**: Operating under uncertainty with known statistical properties

### Domain Applications

| Domain | Application |
|--------|-------------|
| **Robotics** | Search and rescue, environmental monitoring, precision agriculture |
| **Autonomous Systems** | Drone swarms, underwater vehicles, ground robot teams |
| **Cyber-Physical Systems** | Sensor networks, distributed actuation, surveillance |
| **Logistics** | Warehouse automation, delivery coordination |

## Theoretical Foundation

### Problem Formulation

Given:
- **N** agents with LTI dynamics: `ẋᵢ(t) = Axᵢ(t) + Buᵢ(t) + wᵢ(t)`
- **Target density** ρ*(x): desired spatial distribution
- **Current density** ρ(x,t): agent distribution

Objective:
Minimize density mismatch: `J = ∫∫ (ρ(x,t) - ρ*(x))² dx dt`

### Key Components

#### 1. Density Mismatch Metric
```
D(t) = ∫ (ρ(x,t) - ρ*(x))² dx
```
Measures the difference between current agent distribution and target distribution.

#### 2. Optimal Control Law
For LTI systems, the analytical solution yields:
```
uᵢ*(t) = -R⁻¹BᵀP(xᵢ(t) - x̄ᵢ(t))
```
where:
- `P` solves the algebraic Riccati equation
- `x̄ᵢ(t)` is the target position derived from density gradient

#### 3. Convergence Guarantees
Under stochastic LTI dynamics with bounded noise, the framework provides:
- **Mean-square convergence**: E[‖ρ(t) - ρ*‖²] → 0 as t → ∞
- **Exponential rate**: Convergence with known decay rate λ
- **Robustness bounds**: Maximum steady-state error under disturbances

## Workflow

### Step 1: Define the Coverage Problem

**Input Requirements**:
- Target spatial density ρ*(x) (continuous or discrete representation)
- Agent dynamics model (LTI parameters A, B)
- Environment boundaries and constraints
- Agent count N and initial positions

**Key Questions**:
- What spatial distribution needs to be achieved?
- What are the agent movement constraints?
- Is the environment static or dynamic?

### Step 2: Formulate the Optimal Control Problem

**Mathematical Setup**:
```python
# Define system matrices
A = ...  # State transition matrix
B = ...  # Control input matrix
Q = ...  # State cost (density mismatch weight)
R = ...  # Control effort weight

# Solve Riccati equation for optimal gain
P = solve_algebraic_riccati(A, B, Q, R)
K = np.linalg.inv(R) @ B.T @ P
```

**Parameter Selection Guidelines**:
- **Q matrix**: Larger values prioritize density tracking accuracy
- **R matrix**: Larger values penalize aggressive control inputs
- Trade-off between coverage quality and energy efficiency

### Step 3: Derive Target Positions from Density

**Density-to-Position Mapping**:
```python
def density_to_target_positions(rho_star, N):
    """
    Convert target density to agent target positions.
    
    Args:
        rho_star: Target density function or grid
        N: Number of agents
    
    Returns:
        target_positions: Array of shape (N, dim)
    """
    # Method 1: Lloyd's algorithm (centroidal Voronoi tessellation)
    # Method 2: Gradient descent on density potential
    # Method 3: Sampling from probability distribution
    ...
```

**Implementation Options**:
1. **Lloyd's Algorithm**: Iterative centroid computation
2. **Gradient Flow**: Follow density gradient ascent
3. **Importance Sampling**: Sample proportional to density

### Step 4: Implement Decentralized Control

**Control Synthesis**:
```python
def compute_optimal_control(x_i, x_target_i, K):
    """
    Compute optimal control input for agent i.
    
    Args:
        x_i: Current position
        x_target_i: Target position from density
        K: Optimal gain matrix
    
    Returns:
        u_i: Control input
    """
    error = x_i - x_target_i
    u_i = -K @ error
    return u_i
```

**Decentralization Strategy**:
- Each agent computes its own target based on local density information
- No global coordination required after initialization
- Communication only needed for density map updates (if dynamic)

### Step 5: Verify Convergence Properties

**Theoretical Verification**:
1. Check LTI dynamics assumption holds
2. Verify noise bounds match stochastic analysis assumptions
3. Validate density representation accuracy

**Empirical Verification**:
```python
def verify_convergence(trajectories, rho_star, threshold=0.01):
    """
    Verify empirical convergence of the system.
    
    Args:
        trajectories: Agent position history
        rho_star: Target density
        threshold: Convergence threshold
    
    Returns:
        converged: Boolean
        final_error: Steady-state density mismatch
    """
    final_positions = trajectories[-1]
    rho_final = estimate_density(final_positions)
    error = np.mean((rho_final - rho_star)**2)
    return error < threshold, error
```

## Advanced Topics

### Non-Uniform Density Tracking

For time-varying target densities:
```python
def time_varying_target(t):
    """Define time-varying density target."""
    # Example: Moving coverage window
    center = initial_center + velocity * t
    return gaussian_density(center, sigma)

# Update control law with time derivative
u_i = -K @ (x_i - x_target_i(t)) + feedforward_term
```

### Handling Obstacles and Constraints

**Barrier Function Approach**:
```python
def obstacle_barrier(x, obstacle_center, radius):
    """Compute barrier function for obstacle avoidance."""
    distance = np.linalg.norm(x - obstacle_center)
    if distance < radius:
        return float('inf')
    return -np.log(distance - radius)

# Modified control with barrier constraints
u_safe = project_to_safe_set(u_optimal, barriers)
```

### Multi-Scale Coverage

For hierarchical coverage (macro + micro):
```python
# Macro-level: Cluster assignment
cluster_assignments = cluster_agents_by_density(N_clusters)

# Micro-level: Intra-cluster density control
for cluster in clusters:
    u_cluster = density_driven_control(cluster.agents, cluster.local_density)
```

## Implementation Examples

### Example 1: 2D Area Coverage with Drone Swarm

```python
import numpy as np
from scipy.linalg import solve_continuous_are

# System parameters
n_agents = 20
A = np.zeros((2, 2))  # Double integrator
B = np.eye(2)
Q = np.eye(2) * 10    # High priority on position accuracy
R = np.eye(2) * 0.1   # Moderate control cost

# Solve Riccati equation
P = solve_continuous_are(A, B, Q, R)
K = np.linalg.inv(R) @ B.T @ P

# Define target density (e.g., Gaussian centered at origin)
def target_density(x):
    return np.exp(-np.sum(x**2) / (2 * 5**2))

# Initialize agents
agent_positions = np.random.uniform(-10, 10, (n_agents, 2))

# Simulation loop
dt = 0.01
for t in range(1000):
    # Compute target positions from density
    target_positions = sample_from_density(target_density, n_agents)
    
    # Compute control for each agent
    for i in range(n_agents):
        error = agent_positions[i] - target_positions[i]
        control = -K @ error
        agent_positions[i] += control * dt
```

### Example 2: Environmental Monitoring with Sensor Network

```python
# Time-varying target density based on pollution measurements
def pollution_density(x, t, sensor_readings):
    """Dynamic density based on real-time sensor data."""
    base_density = uniform_density(x)
    for reading in sensor_readings:
        if reading.timestamp > t - dt:
            # Increase density near high pollution areas
            distance = np.linalg.norm(x - reading.location)
            base_density += gaussian(distance, reading.value)
    return base_density

# Adaptive control loop
while monitoring:
    current_readings = get_sensor_data()
    rho_star = lambda x: pollution_density(x, current_time, current_readings)
    
    # Recompute targets and controls
    targets = density_to_positions(rho_star, n_agents)
    controls = [compute_optimal_control(pos, tgt, K) 
                for pos, tgt in zip(agent_positions, targets)]
```

## Comparison with Alternative Approaches

| Approach | Computation | Scalability | Guarantees | Flexibility |
|----------|-------------|-------------|------------|-------------|
| **D²OC (This Skill)** | Closed-form | O(N) linear | ✓ Formal | High |
| Eulerian PDE Solvers | Heavy grid-based | O(M²) grid | ✓ Formal | Medium |
| Voronoi-based | Lloyd iteration | O(N log N) | ~ Empirical | Medium |
| Potential Fields | Gradient descent | O(N) | ✗ None | Low |
| Heuristic Planning | Sampling-based | O(N²) | ✗ None | High |

## References

### Core Paper
- **Lee, K. (2026)**. "Density-Driven Optimal Control: Convergence Guarantees for Stochastic LTI Multi-Agent Systems." arXiv:2604.08495v1.

### Related Work
- Cortés, J., et al. (2004). Coverage control for mobile sensing networks.
- Schwager, M., et al. (2009). Decentralized, adaptive coverage control.
- Liu, Y., et al. (2018). Density-aware robotic systems.

### Mathematical Background
- Linear Quadratic Regulator (LQR) theory
- Voronoi tessellations and coverage
- Stochastic stability analysis
- Optimal transport theory

## Tools and Resources

### Required Libraries
```python
# Core numerical computing
numpy >= 1.20.0
scipy >= 1.7.0

# Optional for visualization
matplotlib >= 3.4.0
plotly >= 5.0.0

# Optional for ROS integration
rospy >= 1.15.0
```

### Visualization Tools
See `references/visualization_examples.md` for plotting density evolution, agent trajectories, and convergence metrics.

## Troubleshooting

### Common Issues

**Issue**: Slow convergence
- **Check**: Are Q and R matrices appropriately tuned?
- **Solution**: Increase Q for faster response, decrease R to allow larger controls

**Issue**: Oscillations around target
- **Check**: Is the system properly damped?
- **Solution**: Add velocity feedback or reduce proportional gain

**Issue**: Density estimation errors
- **Check**: Is the kernel density estimator bandwidth appropriate?
- **Solution**: Use adaptive bandwidth or increase agent count

**Issue**: Agents cluster in local optima
- **Check**: Is the density landscape multi-modal?
- **Solution**: Use simulated annealing or multi-start initialization

## Extensions and Future Work

### Potential Enhancements
- Nonlinear system extensions via feedback linearization
- Learning-based density estimation from data
- Game-theoretic formulations for competitive scenarios
- Hybrid discrete-continuous coverage problems

### Research Opportunities
- Tightening convergence rate bounds
- Asynchronous and event-triggered control
- Communication-constrained implementations
- Real-world deployment case studies

---

_Last updated: 2026-04-14_
_Source: arXiv:2604.08495v1 (April 2026)_
