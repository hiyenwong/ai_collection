---
name: nonlinear-mas-optimal-control
description: "Nonlinear Multi-Agent Systems Optimal Control - distributed optimal consensus for general nonlinear dynamics using optimal control principle (OCP) and MPC framework. Use for: nonlinear multi-agent consensus, leaderless/leader-follower coordination, distributed optimal control. Activation: nonlinear multi-agent, optimal consensus, distributed optimal control, OCP method, leader-follower consensus."
---

# Nonlinear Multi-Agent Systems Optimal Control

## Description
Distributed optimal consensus framework for general nonlinear multi-agent systems. Converts consensus problems into optimal control problems using the Optimal Control Principle (OCP) method, with MPC-based enhancements for broader applicability.

## Activation Keywords
- nonlinear multi-agent
- optimal consensus
- distributed optimal control
- OCP method
- leader-follower consensus
- leaderless consensus
- nonlinear consensus
- multi-agent coordination
- superlinear convergence
- general nonlinear dynamics

## Tools Used
- **exec**: Run Python/MATLAB for nonlinear control simulations
- **write**: Create consensus algorithms
- **read**: Load multi-agent system configurations
- **numpy/scipy**: Numerical optimization

## Core Concepts

### Problem Statement
**Optimal Consensus Problem**: Design control inputs for multi-agent systems with nonlinear dynamics to achieve consensus while minimizing a global cost function.

**Two Cases**:
1. **Leaderless Consensus**: All agents converge to common value
2. **Leader-Follower Consensus**: Followers converge to leader state

### Unified Framework
Both cases addressed in a single optimal control formulation:
```
min_u J = Σ ∫(consensus_error_i + control_effort_i) dt
subject to: ẋ_i = f_i(x_i, u_i)  # Nonlinear dynamics
```

### Key Innovations

#### 1. OCP-Based Approach
**Optimal Control Principle Method**:
- Converts consensus to optimal control problem
- Each agent minimizes global consensus cost
- Handles general nonlinear dynamics

#### 2. MPC Enhancements
Two algorithms under MPC framework:
- **MPC-OCP**: Receding horizon implementation
- **Enhanced MPC-OCP**: Broader applicability for complex nonlinearities

#### 3. Convergence Analysis
- **Convergence**: Guaranteed under mild assumptions
- **Superlinear Rate**: Faster than linear convergence
- **Rigorous Proof**: Formal mathematical analysis

## Implementation Patterns

### Pattern 1: OCP Consensus Design
```python
def design_ocp_consensus(agents, graph, consensus_type='leaderless'):
    """
    Design OCP-based consensus for nonlinear multi-agent systems.
    
    Args:
        agents: List of nonlinear agent dynamics
        graph: Communication topology
        consensus_type: 'leaderless' or 'leader-follower'
    
    Returns:
        controller: OCP consensus controller
        convergence_rate: Superlinear convergence guarantee
    """
    # Formulate global consensus cost
    # Set up optimal control problem
    # Design distributed solution
    # Return controller with guarantees
```

### Pattern 2: MPC Enhancement
```python
def design_mpc_consensus(agents, graph, horizon, consensus_type):
    """
    Design MPC-enhanced consensus algorithm.
    
    Args:
        horizon: Prediction horizon for MPC
        Other args same as OCP version
    
    Returns:
        mpc_controller: MPC-based controller
        enhanced: Whether enhanced algorithm is used
    """
    # Formulate finite-horizon optimal control
    # Handle nonlinear constraints
    # Implement receding horizon
```

### Pattern 3: Convergence Verification
```python
def verify_consensus_convergence(agents, controller, simulation_time):
    """
    Verify consensus convergence with superlinear rate.
    
    Returns:
        converged: Whether consensus achieved
        rate: Empirical convergence rate
        theoretical_bound: Guaranteed rate
    """
```

## Mathematical Framework

### Nonlinear Agent Dynamics
```
ẋ_i = f_i(x_i, u_i),  i = 1, ..., N
```
where f_i is nonlinear dynamics of agent i.

### Consensus Error
**Leaderless**:
```
e_i = x_i - (1/N) Σ x_j
```

**Leader-Follower**:
```
e_i = x_i - x_0  (for followers)
```
where x_0 is leader state.

### Global Cost Function
```
J = Σ_{i=1}^N ∫_0^T (e_i^T Q e_i + u_i^T R u_i) dt
```

### OCP Formulation
```
min_u J
subject to: ẋ_i = f_i(x_i, u_i)
            x_i(0) = x_i0
```

### MPC Formulation
```
min_u Σ_{k=0}^{N-1} (e_i(k)^T Q e_i(k) + u_i(k)^T R u_i(k))
subject to: x_i(k+1) = f_i(x_i(k), u_i(k))
```

## Workflow

### Step 1: Define Multi-Agent System
```python
# Define nonlinear dynamics for each agent
agents = [
    NonlinearAgent(
        dynamics=f_i,
        state_dim=n_i,
        control_dim=m_i
    )
    for i in range(N)
]

# Define communication graph
graph = CommunicationGraph(
    adjacency=adj_matrix,
    laplacian=lap_matrix
)
```

### Step 2: Select Consensus Type
```python
if consensus_type == 'leaderless':
    # All agents converge to average
    reference = None
elif consensus_type == 'leader-follower':
    # Followers track leader
    reference = LeaderAgent(dynamics=f_0, state=x_0)
```

### Step 3: Design OCP Controller
```python
ocp_controller = OCPConsensusController(
    agents=agents,
    graph=graph,
    consensus_type=consensus_type,
    cost_matrices=(Q, R)
)
```

### Step 4: Enhance with MPC (Optional)
```python
mpc_controller = MPCConsensusController(
    base_controller=ocp_controller,
    horizon=20,
    dt=0.01
)
```

### Step 5: Execute Consensus
```python
for t in simulation_time:
    for i, agent in enumerate(agents):
        # Compute optimal control
        if use_mpc:
            u_i = mpc_controller.compute_control(i, agent, neighbors)
        else:
            u_i = ocp_controller.compute_control(i, agent, neighbors)
        
        # Apply control
        agent.update(u_i)
    
    # Check consensus
    if check_consensus(agents, tolerance):
        print(f"Consensus achieved at t={t}")
        break
```

### Step 6: Verify Convergence Rate
```python
# Verify superlinear convergence
rate = compute_convergence_rate(consensus_error_history)
assert rate > 1.0, "Superlinear convergence verified"
```

## Examples

### Example 1: Robot Formation Control
```python
# Mission: Achieve formation with nonlinear unicycle robots
# Dynamics: Nonholonomic unicycle model
# Consensus: Leader-follower (follow leader trajectory)

# Define unicycle dynamics
def unicycle_dynamics(state, control):
    x, y, theta = state
    v, omega = control
    dx = v * cos(theta)
    dy = v * sin(theta)
    dtheta = omega
    return [dx, dy, dtheta]

# Create robot agents
robots = [
    NonlinearAgent(dynamics=unicycle_dynamics)
    for _ in range(5)
]

# Define leader
leader = NonlinearAgent(dynamics=unicycle_dynamics)
leader.set_trajectory(trajectory)

# Design leader-follower consensus
controller = OCPConsensusController(
    agents=robots,
    leader=leader,
    consensus_type='leader-follower'
)

# Execute formation control
run_formation_control(robots, leader, controller)
```

### Example 2: UAV Coordination
```python
# Mission: Synchronize UAV attitudes
# Dynamics: Nonlinear attitude dynamics
# Consensus: Leaderless (common attitude)

# Define UAV attitude dynamics (nonlinear)
def attitude_dynamics(state, control):
    # Quaternion or Euler angle dynamics
    # Nonlinear coupling terms
    pass

# Create UAV swarm
uavs = [NonlinearAgent(dynamics=attitude_dynamics) for _ in range(8)]

# Design leaderless consensus
controller = MPCConsensusController(
    agents=uavs,
    consensus_type='leaderless',
    horizon=15
)

# Execute attitude synchronization
run_attitude_sync(uavs, controller)
```

### Example 3: Vehicle Platooning
```python
# Mission: Vehicle platoon with nonlinear dynamics
# Dynamics: Nonlinear vehicle model with tire slip
# Consensus: Leader-follower (follow lead vehicle)

# Define nonlinear vehicle model
def vehicle_dynamics(state, control):
    # Position, velocity, acceleration
    # Nonlinear tire force model
    pass

# Create vehicle platoon
vehicles = [NonlinearAgent(dynamics=vehicle_dynamics) for _ in range(10)]
lead_vehicle = vehicles[0]
followers = vehicles[1:]

# Design platooning controller
controller = OCPConsensusController(
    agents=followers,
    leader=lead_vehicle,
    consensus_type='leader-follower'
)

# Execute platooning
run_platooning(vehicles, controller, safety_distance=2.0)
```

## Error Handling

### Common Issues
1. **Nonlinear Instability**: Check dynamics Lipschitz continuity
2. **Slow Convergence**: Verify superlinear rate conditions
3. **Communication Delays**: Account for delayed information
4. **Input Constraints**: Handle actuator saturation

### Debugging Tips
- Verify nonlinear dynamics are smooth
- Check communication graph connectivity
- Validate cost function convexity
- Monitor consensus error decay rate

## Comparison with Existing Methods

### vs. Linear Consensus
- **This Method**: Handles general nonlinear dynamics
- **Linear Methods**: Limited to linear or near-linear systems

### vs. Gradient-Based Methods
- **This Method**: Optimal control formulation, superlinear rate
- **Gradient Methods**: Local optimization, linear rate

### vs. Passivity-Based Methods
- **This Method**: Broader applicability, MPC enhancement
- **Passivity Methods**: Require specific system structure

## References

- **Paper**: "Distributed Optimal Consensus of Nonlinear Multi-Agent Systems"
- **Authors**: Ziyuan Guo, Chuanzhi lv, Liping Zhang, et al.
- **arXiv**: 2604.03958v1
- **Category**: math.OC (Optimization and Control)

## Related Skills
- `distributed-optimal-control`: General distributed optimal control
- `multi-agent-consensus`: Consensus algorithms overview
- `mpc-multi-agent`: MPC for multi-agent systems
- `nonlinear-control`: Nonlinear control theory

## Notes
- Based on April 2026 research
- Handles general nonlinear multi-agent systems
- Provides superlinear convergence rate
- Broader applicability than existing methods
- Both leaderless and leader-follower cases supported
- MPC enhancement for complex nonlinearities
