---
name: rat-randomized-advantage-transformation
description: "Randomized Advantage Transformation (RAT) methodology for computing Tikhonov-regularized natural policy gradients via direct backpropagation. Uses Woodbury formula and randomized block Kaczmarz iterations to avoid explicit Fisher matrix construction, CG solvers, or architecture-specific approximations. ICML 2026 accepted. Matches or exceeds established natural-gradient methods across continuous and visual control benchmarks. Use when: scalable natural policy gradients, Fisher-free natural gradient, efficient second-order RL, continuous/visual control RL. Activation: RAT, randomized advantage transformation, natural policy gradient, Woodbury natural gradient, block Kaczmarz RL, Fisher-free policy gradient, Tikhonov-regularized policy gradient."
---

# Randomized Advantage Transformation (RAT): Computing Natural Policy Gradients via Direct Backpropagation

**Paper**: arXiv:2605.18591 | Submitted: 18 May 2026 | **ICML 2026**
**Authors**: Mingfei Sun

## Core Problem

Natural policy gradients (NPG) improve optimization by accounting for the geometry of the distribution space (using the Fisher information matrix), but their practical use is limited by:

1. **High cost** of estimating and inverting the Fisher matrix
2. **Architecture-specific** approximations required
3. **Complex solvers** like conjugate-gradient (CG) needed

## Key Innovation: RAT

RAT computes **Tikhonov-regularized natural policy gradients** via direct backpropagation, making natural gradients as easy to implement as vanilla policy gradients.

### Mathematical Reformulation

Using the **Woodbury formula**, RAT shows that the regularized natural policy gradient is equivalent to a **vanilla policy gradient with a transformed advantage function**:

```
g_natural = VPG(reformulated_advantage)
```

Where the transformation is computed efficiently via:

### Randomized Block Kaczmarz Iterations

RAT computes the advantage transformation using **randomized block Kaczmarz** on on-policy mini-batches:

- **No explicit Fisher construction** needed
- **No conjugate-gradient solvers**
- **No architecture-specific approximations**
- Works with any differentiable policy architecture

## Algorithm Summary

1. Compute vanilla policy gradient on a mini-batch
2. Apply randomized block Kaczmarz iterations to compute the transformed advantage
3. Use the transformed advantage to compute a natural policy gradient estimate
4. Update policy parameters with the natural gradient direction

## Key Properties

- **Convergence guarantees**: RAT provides theoretical convergence proofs
- **Architecture agnostic**: Compatible with any differentiable policy (MLP, CNN, etc.)
- **Practical simplicity**: Easy to implement - just one additional transformation step
- **Efficiency**: Block Kaczmarz iterations are much cheaper than Fisher inversion

## Experimental Results (ICML 2026)

| Benchmark Type | RAT | Natural AC | TRPO | PPO |
|---------------|:---:|:----------:|:----:|:---:|
| Continuous control (MuJoCo) | **Matches/exceeds** | ✓ | ✓ | ✓ |
| Visual control (DMControl) | **Matches/exceeds** | ✓ | ✓ | ✓ |

- Matches or exceeds established natural-gradient methods (NAC, TRPO)
- Consistent improvements over vanilla PPO
- Simple implementation without architecture-specific code

## Relationship to Existing Skills

- [[pg-dpo-non-exponential-discounting]] - Another policy gradient advancement (non-exponential discounting)
- [[gcpo-cooperative-policy-optimization]] - GRPO variant for LLMs (different domain: continuous control)
- [[efficient-tdmpc]] - Model-based RL for continuous control (complementary approach)
- [[advanced-control-systems-2026]] - Control theory overlap

## Implementation Notes

- Drop-in replacement for vanilla policy gradient in AC frameworks
- One additional forward-backward pass equivalent in cost
- No need for Fisher-vector products
- Works with both discrete and continuous action spaces
- Compatible with PPO/TRPO-style clipping (can be combined)

## Use Cases

1. **Continuous Control**: MuJoCo, robotic control tasks
2. **Visual Control**: DMControl, pixel-based RL
3. **Any Differentiable Policy**: Plug into existing AC implementations
4. **Scalable NPG**: First practical method that scales natural gradients to large policies

## Activation Keywords

RAT, randomized advantage transformation, natural policy gradient, Woodbury natural gradient, block Kaczmarz RL, Fisher-free policy gradient, Tikhonov-regularized policy gradient, second-order RL, ICML 2026, Fisher matrix approximation, randomized Kaczmarz iteration, direct backpropagation natural gradient
