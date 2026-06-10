---
name: l2ru-ssm-controller-stability
description: "L2-bounded structured state-space controller methodology with free parametrization for nonlinear control with stability guarantees. L2-Recurrent Unit (L2RU) enforces prescribed L2 gain by design, enabling unconstrained optimization via small-gain theorem or performance-boosting framework. Parallel scan enables efficient long-sequence processing. Use for nonlinear control, stability-guaranteed neural controllers, structured state-space models, robot formation control. Activation: L2-bounded controller, SSM controller, state-space model, nonlinear control, stability guarantee, small-gain theorem, L2RU, L2-recurrent-unit"
metadata:
  arxiv_id: "2606.11049"
  published: "2026-06-09"
  authors: "Muhammad Zakwan, Leonardo Massai, Efe C. Balta, Giancarlo Ferrari-Trecate"
  tags: [control-theory, state-space-model, nonlinear-control, stability, neural-controller, L2-gain]
---

## L2-Bounded SSM Controller with Free Parametrization

Guarantee closed-loop stability for nonlinear control policies using structured state-space models with prescribed L2 gain, enabling fully unconstrained optimization.

### Core Methodology

1. **L2 Gain Parametrization**: Construct a free parametrization of LTI systems with prescribed L2 gain bound γ. The parametrization ensures ||G||₂ ≤ γ by construction, eliminating the need for explicit stability constraints during optimization.

2. **L2-Recurrent Unit (L2RU)**: Build SSM layer enforcing the L2 bound by design:
   - State update: xₜ₊₁ = Axₜ + Buₜ
   - Output: yₜ = Cxₜ + Duₜ
   - Parameter matrices (A, B, C, D) constrained via orthogonal/Lyapunov-based parametrization
   - Result: any parameter values in the free space guarantee ||G||₂ ≤ γ

3. **Stability via Small-Gain Theorem**: If the linear part has L2 gain < 1/γ and the nonlinear part has Lipschitz constant < γ, the closed-loop is stable. The L2RU guarantees the linear part's gain.

4. **Performance-Boosting Framework**: Alternative to small-gain — use the L2RU as a stabilizing "skeleton" and optimize arbitrary nonlinear objectives unconstrained on top.

5. **Parallel Scan**: The SSM structure enables parallel processing via associative scan (parallel prefix), making it efficient for long input sequences compared to sequential RNN processing.

### Implementation Steps

1. **Define L2 Bound**: Choose γ based on system requirements (disturbance rejection, noise tolerance).

2. **Construct L2RU**: Implement the free parametrization — typically via Cayley transform or Lyapunov-based reparametrization of (A, B, C, D).

3. **Stack Layers**: Build multi-layer architecture by stacking L2RUs with nonlinear activation functions.

4. **Optimize**: Train with any loss function — no stability constraints needed. Standard optimizers (Adam, SGD) work directly.

5. **Deploy**: The resulting controller guarantees closed-loop stability independently of the learned parameters.

### Pitfalls

- **L2 vs. practical stability**: L2 stability guarantees bounded-input bounded-output (BIBO) stability, but does not guarantee fast convergence or transient performance.
- **Conservativeness**: The small-gain theorem is conservative — actual stability region may be larger than guaranteed.
- **Nonlinear part bound**: The small-gain approach requires the nonlinear part's Lipschitz constant to be bounded. This must be verified separately.
- **Discrete-time**: The paper addresses discrete-time systems. Continuous-time requires different parametrization.

### Verification

- Formation control task: verify collision and obstacle avoidance while maintaining stability
- Compare L2RU-based controller against constrained optimization baseline (should match performance with less computational overhead)
- Check L2 gain numerically: compute ||G||₂ from frequency response

### Activation Keywords

- `l2ru-ssm-controller-stability`
- L2-bounded control
- SSM controller
- nonlinear control stability
- small-gain theorem
- L2 recurrent unit
