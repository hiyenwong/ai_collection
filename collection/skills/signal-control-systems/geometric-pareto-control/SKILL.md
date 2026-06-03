---
name: geometric-pareto-control
description: >
  Geometric Pareto Control (GPC) methodology for cyber-physical systems with known physics.
  Core idea: embed the family of Pareto-optimal solutions as a submanifold within a Lie group
  offline, then use closed-form proximal navigation via Riemannian gradient flow online.
  Resolves RL barriers in safety-critical CPS: sample complexity, retraining needs,
  brittle switching logic, and unsafe exploration. Applicable to multi-objective optimal
  control, power systems, autonomous systems, real-time economic dispatch.
  Activation: geometric pareto control, riemannian gradient flow control, lie group control,
  multi-objective optimal control, pareto submanifold, safety-critical CPS control.
---

# Geometric Pareto Control: Riemannian Gradient Flow of Energy Function via Lie Group Homotopy

Based on: Tong Wu (2026) - arXiv:2605.09824

## Core Problem

Reinforcement learning in safety-critical cyber-physical systems faces four barriers:
1. **Sample complexity** grows with action-space dimension
2. **Retraining required** when objectives or conditions shift
3. **Brittle switching logic** needed for goals like safety recovery vs economic dispatch
4. **Unsafe exploration** persists even under constrained RL formulations

## Key Innovation: Geometric Two-Stage Approach

### Stage 1: Offline — Pareto Submanifold Construction

The supported family of Pareto-optimal solutions is embedded as a **submanifold within a Lie group**:

```
Pareto-optimal solutions → Submanifold M ⊂ G (Lie group)
```

Key properties:
- **Exponential map closure**: Preserves membership in the ambient Lie group
- **Drift/reset assumptions**: Keep online latent states within bounded neighborhood of Pareto submanifold
- **Training-time feasibility margin**: Guarantees decoded actions remain feasible without post-hoc projection
- **"Map" construction**: Creates a complete map of the solution landscape

### Stage 2: Online — Riemannian Gradient Flow Navigation

A **closed-form proximal navigator** traverses the submanifold:

```
Unified Riemannian gradient flow ← Singular perturbation potential field
```

Key properties:
- **Dual-timescale dynamics**: Prioritizes constraint restoration over performance optimization
- **Homeomorphic structure**: Varying system parameters and objective weights produce continuous control actions
- **No retraining needed**: Deployment under unseen conditions without retraining

## Methodology

### Mathematical Framework

```python
# Lie group G containing Pareto submanifold M
# Exponential map: exp: g → G (Lie algebra to Lie group)
# Logarithm map: log: G → g (inverse of exp)

# Pareto submanifold M is defined as:
# M = {x ∈ G : x is Pareto-optimal for some weight vector w}

# Offline construction:
def construct_pareto_submanifold(objectives, constraints):
    """
    Embed Pareto-optimal solutions as submanifold in Lie group.
    Returns parameterized submanifold with feasibility margin.
    """
    # 1. Generate Pareto front via weighted scalarization
    pareto_points = []
    for w in weight_grid:
        x_opt = solve_weighted_problem(objectives, constraints, w)
        pareto_points.append(x_opt)
    
    # 2. Embed into Lie group via exponential map
    submanifold = embed_in_lie_group(pareto_points)
    
    # 3. Compute feasibility margin
    margin = compute_feasibility_margin(submanifold, constraints)
    
    return submanifold, margin

# Online navigation:
def riemannian_navigation(current_state, target_weights, submanifold):
    """
    Navigate Pareto submanifold via Riemannian gradient flow.
    """
    # Dual-timescale dynamics:
    # Fast timescale: constraint restoration
    # Slow timescale: performance optimization
    
    potential = singular_perturbation_potential(current_state, target_weights)
    gradient = riemannian_gradient(submanifold, potential)
    
    # Proximal step with feasibility guarantee
    new_state = proximal_step(current_state, gradient, step_size)
    
    return new_state
```

### Singular Perturbation Potential Field

The potential field uses singular perturbation to create dual-timescale behavior:

```python
def singular_perturbation_potential(state, weights, epsilon=0.01):
    """
    Potential field with fast constraint restoration and slow optimization.
    
    epsilon << 1 creates timescale separation:
    - O(1/epsilon) dynamics for constraint satisfaction
    - O(1) dynamics for objective optimization
    """
    constraint_potential = sum(c(state)**2 for c in constraints) / epsilon
    objective_potential = sum(w * f(state) for w, f in zip(weights, objectives))
    
    return constraint_potential + objective_potential
```

### Feasibility Margin Guarantee

The training-time feasibility margin ensures:

```python
def decode_with_margin(latent_state, submanifold, margin):
    """
    Decode latent state to action with feasibility guarantee.
    No post-hoc projection needed.
    """
    # Project to tangent space of submanifold
    tangent_projection = project_to_tangent(latent_state, submanifold)
    
    # Ensure within feasibility margin
    if distance(tangent_projection, submanifold) < margin:
        return decode(tangent_projection)
    else:
        # Fallback: retract to submanifold via exponential map
        return retract_via_expmap(tangent_projection, submanifold)
```

## Implementation Patterns

### Pattern 1: Multi-Objective Power Dispatch

```python
class GeometricParetoDispatch:
    def __init__(self, network_model, cost_functions, constraints):
        # Offline: construct Pareto submanifold
        self.submanifold = construct_pareto_submanifold(
            cost_functions, constraints
        )
        self.margin = compute_feasibility_margin(self.submanifold, constraints)
    
    def dispatch(self, current_state, objective_weights, network_conditions):
        # Online: navigate to optimal dispatch
        potential = self._build_potential(objective_weights)
        gradient = self._riemannian_gradient(potential)
        new_dispatch = self._proximal_step(current_state, gradient)
        return new_dispatch
```

### Pattern 2: Safety-Critical Mode Transition

```python
class SafeModeTransition:
    def __init__(self, safety_submanifold, performance_submanifold):
        # Unified submanifold covering both safety and performance regimes
        self.unified_manifold = merge_submanifolds(
            safety_submanifold, performance_submanifold
        )
    
    def transition(self, current_state, mode):
        """
        Continuous transition between safety recovery and economic dispatch.
        No brittle switching logic needed.
        """
        if mode == "safety":
            weights = {"safety": 0.9, "economics": 0.1}
        else:
            weights = {"safety": 0.3, "economics": 0.7}
        
        return self._navigate(current_state, weights)
```

### Pattern 3: Adaptive Control Under Uncertainty

```python
def adaptive_geometric_control(state, uncertain_parameters, submanifold):
    """
    Maintain feasibility under parameter uncertainty without retraining.
    """
    # Homeomorphic structure ensures continuous response to parameter changes
    for param in uncertain_parameters:
        perturbed_manifold = deform_submanifold(submanifold, param)
        control = riemannian_navigation(state, perturbed_manifold)
    
    return control
```

## Performance Results (from paper)

| Metric | GPC | Model-Free Baselines |
|--------|-----|---------------------|
| Feasibility | 100% | 0% (under uncertainty) |
| Oracle Suboptimality | 0.30% | N/A |
| Decision Time | 12.3 ms | Variable |
| Retraining Needed | No | Yes |

## Key Advantages

1. **Zero retraining**: Deploy under unseen conditions without retraining
2. **Guaranteed feasibility**: Training-time margin ensures no infeasible actions
3. **Continuous adaptation**: Homeomorphic structure provides smooth response to parameter changes
4. **Dual-timescale control**: Natural prioritization of safety over performance
5. **Closed-form navigation**: No iterative optimization needed online

## Applications

1. **Optimal Power Flow**: Real-time multi-objective economic dispatch
2. **Autonomous Vehicles**: Safety-performance tradeoff navigation
3. **Robotics**: Constrained motion planning with feasibility guarantees
4. **Process Control**: Multi-objective optimization in chemical plants
5. **Aerospace**: Trajectory optimization with safety constraints
6. **Financial Systems**: Risk-return optimization with regulatory constraints

## Pitfalls

1. **Offline construction cost**: Building Pareto submanifold requires significant computation
   - Mitigation: Use adaptive sampling of weight space
2. **Dimensionality**: High-dimensional action spaces make submanifold construction expensive
   - Mitigation: Use low-rank approximations or manifold learning
3. **Non-convex objectives**: Pareto front may have disconnected components
   - Mitigation: Use multiple local submanifolds with transition regions
4. **Lie group selection**: Choice of Lie group affects computational efficiency
   - Mitigation: Select minimal Lie group containing the Pareto set

## Verification Steps

1. Verify feasibility margin is positive for all Pareto points
2. Check dual-timescale separation (epsilon parameter)
3. Test continuous response to parameter variations
4. Compare against oracle solution for suboptimality gap
5. Verify no retraining needed under distribution shift

## Related Concepts

- Differential geometry (Riemannian manifolds, exponential maps)
- Multi-objective optimization (Pareto fronts, weighted scalarization)
- Lie group theory (matrix groups, homogeneous spaces)
- Singular perturbation theory (timescale separation)
- Geometric control theory (control on manifolds)
