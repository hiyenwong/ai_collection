---
name: discounted-mpc-robust-control
description: "Discounted Model Predictive Control (MPC) robustness analysis under plant-model mismatch - stability and suboptimality guarantees. Use for: analyzing MPC stability with surrogate models, designing robust control systems, plant-model mismatch compensation. Activation: discounted MPC, MPC robustness, plant-model mismatch, control stability, suboptimality bound."
---

# Discounted MPC Robust Control

## Description
Discounted Model Predictive Control (MPC) robustness analysis framework for systems with plant-model mismatch. Provides unified analysis of closed-loop stability and suboptimality when using surrogate models that differ from the real plant.

## Activation Keywords
- discounted MPC
- MPC robustness
- plant-model mismatch
- control stability
- suboptimality bound
- infinite-horizon optimal control
- surrogate model control
- robust MPC design
- model predictive control analysis

## Tools Used
- **exec**: Run Python/MATLAB simulations for MPC analysis
- **write**: Create control system design documents
- **read**: Load existing control parameters and models

## Core Concepts

### Plant-Model Mismatch Framework
The paper establishes a unified framework based on quadratic costs to analyze:
- Finite-horizon MPC problems
- Infinite-horizon optimal control
- Discounted and undiscounted scenarios

### Key Assumptions
1. **Mismatch Bounds**: Plant-model mismatch proportional to states and controls
2. **Equilibrium Preservation**: Origin remains an equilibrium under mismatch
3. **Continuity**: Model and cost-controllability are continuous

### Main Results

#### Stability Guarantee
Under the framework assumptions:
- **Exponential stability** of the closed loop can be guaranteed
- Robustness guarantees are **uniform over horizon length**
- Larger horizons do not require successively smaller plant-model mismatch

#### Suboptimality Bound
The closed-loop cost recovers the optimal cost of the surrogate model with bounded error.

#### Tradeoff Analysis
Results reveal tradeoffs between:
- Horizon length
- Discounting factor
- Plant-model mismatch magnitude

## Implementation Patterns

### Pattern 1: Stability Analysis
```python
def analyze_mpc_stability(plant_model, surrogate_model, horizon, discount):
    """
    Analyze MPC stability under plant-model mismatch.
    
    Args:
        plant_model: True system dynamics
        surrogate_model: Approximate model used for MPC
        horizon: Prediction horizon length
        discount: Discount factor (0 < discount <= 1)
    
    Returns:
        stability_cert: Boolean stability certificate
        suboptimality_bound: Upper bound on performance loss
    """
    # Check continuity assumptions
    # Verify cost-controllability
    # Compute mismatch bounds
    # Return stability guarantees
```

### Pattern 2: Robust Controller Design
```python
def design_robust_mpc(plant, uncertainty_bounds, performance_specs):
    """
    Design MPC with robustness guarantees.
    
    Steps:
    1. Characterize plant-model mismatch
    2. Select appropriate horizon length
    3. Tune discount factor
    4. Verify stability conditions
    5. Compute suboptimality bounds
    """
```

### Pattern 3: Horizon-Discount Tradeoff
```python
def optimize_horizon_discount(mismatch_level, stability_requirement):
    """
    Optimize MPC parameters for given mismatch level.
    
    The key insight: robustness guarantees are uniform over horizon,
    so larger horizons don't require smaller mismatch bounds.
    """
```

## Mathematical Framework

### Quadratic Cost Formulation
```
J = Σ γ^k (x_k^T Q x_k + u_k^T R u_k)
```
where γ is the discount factor, Q and R are cost matrices.

### Plant-Model Mismatch
```
‖f_plant(x,u) - f_model(x,u)‖ ≤ L_f ‖x‖ + L_g ‖u‖
```
where L_f and L_g are Lipschitz constants for state and control mismatch.

### Stability Condition
Exponential stability requires:
1. Continuity of dynamics
2. Cost-controllability
3. Bounded mismatch

## Workflow

### Step 1: Characterize Mismatch
Identify bounds on plant-model mismatch:
- State-dependent mismatch: L_f
- Control-dependent mismatch: L_g

### Step 2: Verify Assumptions
Check:
- [ ] Model continuity
- [ ] Cost-controllability
- [ ] Equilibrium preservation

### Step 3: Design MPC Parameters
Select:
- Horizon length N
- Discount factor γ
- Cost matrices Q, R

### Step 4: Stability Verification
Apply theorems to certify stability:
- Compute stability region
- Verify exponential convergence

### Step 5: Suboptimality Analysis
Compute performance bounds:
- Closed-loop cost vs. optimal cost
- Worst-case performance degradation

## Examples

### Example 1: Simple Mass-Spring-Damper
```python
# Plant: true dynamics with unmodeled friction
# Model: nominal linear dynamics
# Task: Design robust MPC with stability guarantees

plant = MassSpringDamper(friction=0.1)  # True system
model = MassSpringDamper(friction=0.0)  # Surrogate

# Analyze mismatch
mismatch_bounds = compute_mismatch_bounds(plant, model)

# Design MPC
mpc = RobustMPC(model, horizon=20, discount=0.95)

# Verify stability
stability_cert = verify_stability(plant, mpc, mismatch_bounds)
```

### Example 2: Multi-Agent Consensus
```python
# Plant: nonlinear agent dynamics
# Model: linearized approximation
# Task: Achieve consensus with robustness guarantees

# Design distributed MPC
mpc = DistributedMPC(
    model=linearized_dynamics,
    horizon=10,
    discount=0.9,
    communication_graph=graph
)

# Each agent uses surrogate model
# Stability guaranteed despite mismatch
```

## Error Handling

### Common Issues
1. **Assumption Violation**: Check continuity and controllability
2. **Conservative Bounds**: Mismatch bounds may be too restrictive
3. **Computational Complexity**: Large horizons increase solve time

### Debugging Tips
- Verify model linearization accuracy
- Check cost matrix positive definiteness
- Validate horizon-discount tradeoff

## References

- **Paper**: "Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality"
- **Authors**: Moldenhauer, Worthmann, Postoyan, Nešić, Granzotto
- **arXiv**: 2604.08521v1
- **Category**: math.OC (Optimization and Control)

## Related Skills
- `mpc-stability-suboptimality`: General MPC stability analysis
- `plant-model-mismatch-mpc`: Mismatch compensation techniques
- `distributed-multi-agent-control`: Multi-agent MPC

## Notes
- This skill is based on recent research (April 2026)
- Framework applies to both discounted and undiscounted MPC
- Uniform robustness guarantees are a key advantage
- Suitable for safety-critical control applications


## Instructions for Agents

When this skill is activated:

1. Identify the user's specific need
2. Apply the specialized knowledge
3. Provide clear guidance