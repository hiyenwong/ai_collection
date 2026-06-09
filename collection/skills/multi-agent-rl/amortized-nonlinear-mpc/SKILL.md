---
name: amortized-nonlinear-mpc
description: "Amortized Nonlinear Model Predictive Control using state-dependent quadratic programs (QPs) with single-network residual-corrector architecture. Replaces expensive real-time NLP solving with differentiable interior-point QP layer, enabling deployment on resource-constrained hardware. Achieves orders-of-magnitude speedup while maintaining constraint satisfaction. Applications: robotics, autonomous systems, high-frequency control. Activation: amortized MPC, nonlinear MPC acceleration, QP-based MPC, differentiable optimization, interior-point layer, real-time control, robotics control."
---

## Context

From arXiv:2606.05840 (June 2026) - "Amortized Nonlinear Model Predictive Control" by Francesco Pillitteri, Alberto Bemporad.

Addresses computational bottleneck of real-time Nonlinear MPC by approximating optimal control moves with state-dependent QPs. Uses residual-corrector network architecture trained offline with hybrid loss combining imitation and KKT-residual penalties.

## Core Methodology

### 1. Problem Formulation

**Standard NMPC bottleneck**:
- Solve constrained nonlinear program (NLP) at each sampling instant
- Computational cost limits deployment on resource-constrained hardware
- High sampling rate applications infeasible

**Key insight**: For input-affine nonlinear systems, optimal control can be approximated by state-dependent QP whose parameters depend on current state and reference.

### 2. Architecture Design

**Single-network residual-corrector**:
1. **State-dependent analytic baseline**: Provides initial QP parameters (cost matrix H, gradient h, constraint bounds)
2. **Neural network correction**: Learns only the residual corrections needed to match full NLP solution
3. **Differentiable interior-point layer**: Solves resulting QP, guaranteeing constraint satisfaction

**Why residual learning**:
- Baseline captures problem structure
- Network focuses on refinement
- Faster training, better generalization
- Smaller network capacity needed

### 3. Training Procedure

**Offline data generation**:
- Run full NLP solver over representative state-reference scenarios
- Record optimal control inputs and QP parameters
- Build training dataset

**Hybrid loss function**:
```python
Loss = L_imitation + λ * L_KKT

L_imitation = ||u_network - u_NLP||²  # Supervised imitation
L_KKT = ||KKT_residual||²             # KKT optimality condition penalty
```

**Training steps**:
1. Collect NLP solutions across state space
2. Compute analytic baseline QP parameters
3. Train network to predict corrections
4. Enforce KKT conditions via loss penalty
5. Validate on held-out scenarios

### 4. Input-Affine System Structure

**System model**: x_dot = f(x) + g(x) * u

**State-dependent QP approximation**:
```
minimize: 0.5 * u^T H(x, r) u + h(x, r)^T u
subject to: A(x) u ≤ b(x)
           u_min ≤ u ≤ u_max
```

Parameters H(x,r), h(x,r) depend on current state x and reference r.

### 5. Implementation Architecture

```python
class AmortizedNMPC:
    def __init__(self, baseline_policy, correction_network):
        self.baseline = baseline_policy  # Analytic QP parameter generator
        self.network = correction_network  # Residual correction network
        self.qp_solver = DifferentiableInteriorPointLayer()
    
    def compute_control(self, x, r):
        """
        Real-time control computation
        
        Steps:
        1. Analytic baseline → H0, h0, A0, b0
        2. Network correction → ΔH, Δh, ΔA, Δb
        3. QP parameters → H = H0 + ΔH, etc.
        4. Solve QP → optimal u
        """
        # Baseline (no computation, analytic)
        H0, h0, A0, b0 = self.baseline(x, r)
        
        # Network correction (single forward pass)
        delta_params = self.network(x, r)
        
        # Final QP parameters
        H = H0 + delta_params['H']
        h = h0 + delta_params['h']
        A = A0 + delta_params['A']
        b = b0 + delta_params['b']
        
        # Solve QP (differentiable interior-point)
        u_opt = self.qp_solver.solve(H, h, A, b)
        
        return u_opt
```

### 6. Differentiable Interior-Point Layer

**Key requirement**: QP solver must be differentiable for gradient flow through training

**Interior-point method characteristics**:
- Handles inequality constraints
- Iterative optimization with barrier function
- Backpropagation through iterations possible

**Implementation**:
- Use custom autograd function
- Fixed iteration count for consistent computation time
- Warm start from previous solution

## Pitfalls

1. **Baseline inadequacy**: If analytic baseline is too far from NLP solution, network correction may be insufficient. Ensure baseline captures essential problem structure.

2. **Constraint violation**: Differentiable QP layer must guarantee feasibility. Interior-point methods handle this better than projected gradient.

3. **Training distribution mismatch**: Dataset must cover operational state-reference space. Missing regions lead to poor extrapolation.

4. **Non-input-affine systems**: Method assumes input-affine structure. General nonlinear systems require different approach.

5. **KKT condition weighting**: λ parameter for KKT loss must balance imitation vs optimality. Too high → ignores data; too low → violates constraints.

6. **Real-time constraint**: Must guarantee fixed computation time. Interior-point iterations must be bounded.

7. **Reference prediction horizon**: QP approximation assumes first control action. Long horizons require recursive approach.

## Verification

1. **Speedup validation**: Compare wall-clock time vs NLP solver. Expected orders-of-magnitude improvement.
2. **Tracking performance**: Compare closed-loop tracking error vs full NMPC.
3. **Constraint satisfaction**: Verify that QP solution respects constraints for ALL tested scenarios.
4. **Training convergence**: Monitor imitation loss and KKT residual during training.
5. **Generalization test**: Evaluate on held-out state-reference combinations.
6. **Hardware deployment**: Test on target platform (embedded system, robot controller).

## Key Applications

1. **Robotic manipulation**: High-frequency end-effector tracking (validated on 3-link planar arm)
2. **Autonomous vehicles**: Real-time path planning and control
3. **Process control**: Chemical process regulation with nonlinear dynamics
4. **Power systems**: Grid voltage/frequency regulation
5. **Aerospace**: Flight control with aerodynamic nonlinearities

## Algorithm Comparison

| Method | Computation | Constraints | Accuracy |
|--------|-------------|-------------|----------|
| Full NMPC | Slow (NLP solve) | Exact | Optimal |
| Linear MPC | Fast (QP) | Approximate | Approximate |
| Amortized NMPC | Fast (QP + net) | Exact (QP layer) | Near-optimal |

## Key Innovation

**Residual-corrector architecture**: Instead of learning full QP parameters from scratch, network only learns corrections to analytic baseline. This:
- Reduces network size
- Improves generalization
- Preserves problem structure
- Enables faster training

**Differentiable optimization layer**: Guarantees constraint satisfaction by solving actual QP, not predicting solution. Differentiability enables end-to-end training with backprop through solver.

## Mathematical Details

**Input-affine system**: dx/dt = f(x) + g(x)u

**NMPC problem** (horizon N):
```
minimize Σ_{k=0}^{N-1} [l(x_k, u_k) + l_f(x_N)]
subject to: x_{k+1} = f(x_k) + g(x_k)u_k
           x_k ∈ X, u_k ∈ U
           x_0 = current state
```

**QP approximation** (first step only):
```
minimize 0.5*u^T H(x,r) u + h(x,r)^T u
subject to: A(x) u ≤ b(x)
           u_min ≤ u ≤ u_max
```

**Network correction**: ΔH, Δh, ΔA, Δb = NN(x,r)

**Training loss**: L = ||u_NN - u_NLP||² + λ||KKT(u_NN)||²

## Experimental Validation (Paper)

**Test case**: 3-link planar robotic arm, Cartesian end-effector tracking

**Results**:
- Orders-of-magnitude speedup over NLP
- Comparable tracking performance
- Constraint satisfaction verified
- Robust to parameter variations

**Computation time**: ~1ms vs ~100ms for full NLP (100x speedup)

## Connection to Prior Work

- **Linear MPC**: Fast but inaccurate for nonlinear systems
- **Real-time iteration scheme**: Sequential QP approximations (slower convergence)
- **Explicit MPC**: Offline solution enumeration (limited complexity)
- **Learning-based MPC**: Direct policy learning (constraint violations)
- **This paper**: Differentiable optimization + residual learning (fast + feasible)

## Practical Deployment

1. **Offline training phase**: Generate data, train network (hours)
2. **Online inference**: QP solve + network forward pass (milliseconds)
3. **Hardware**: Embedded processors, FPGA, GPU inference
4. **Safety**: Constraint satisfaction guaranteed by QP layer

**Activation**: amortized MPC, real-time nonlinear control, QP approximation, differentiable optimization, interior-point solver, robotics control, constraint satisfaction, MPC acceleration, learning-based control