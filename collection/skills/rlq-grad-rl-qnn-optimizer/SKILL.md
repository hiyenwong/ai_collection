---
name: rlq-grad-rl-qnn-optimizer
description: RL agent emits QNN gradients to bypass barren plateau variance decay.
category: ai_collection
trigger_words: QNN training, barren plateau, reinforcement learning optimizer, surrogate gradient, quantum neural network gradient
---

# RLQ-Grad: Reinforcement Learning Surrogate Gradients for QNN Training

Methodology from "Modeling quantum neural network gradient with reinforcement learning" (arXiv:2609.31066, Sep 2026).

## When to Use
- Training quantum neural networks (variational circuits) where parameter-shift/adjoint/backprop gradients suffer exponential variance decay (barren plateaus)
- When the O(L·2^n) cost of differentiating through an n-qubit L-layer circuit is prohibitive
- Hybrid quantum-classical classification where quantum-layer gradients block upstream classical layers

## Core Idea
A classical RL policy π_φ (spectrally-normalized PPO agent) learns to **propose parameter updates directly**, replacing the gradient computed by differentiating through the unitary U(θ):

- **State**: s_t = [θ_t, E[loss over batch], E[accuracy over batch], g_{t-1}] — current QNN params, batch-mean loss/accuracy, previous proposed update
- **Action**: a_t = g_t ∈ R^P interpreted as the gradient estimate for P trainable parameters
- **Reward**: r_t = acc_t + 1/(loss_t + ε) — accuracy plus inverse loss (drives loss down)
- **Update**: θ_{t+1} = θ_t − η·g_t, then classical head weights (W, b) updated by ordinary backprop + Adam (lr 1e-3, weight decay 1e-4, β=(0.9,0.999)) with cosine annealing

## Why It Bypasses Barren Plateaus (Theorem 1)
The barren plateau bound (Jordan-algebraic form): Var_θ[ℓ] = Σ_α Tr(O_α)²·Tr(ρ_α)²/dim_R(Aut(A_α)) ∈ O(poly(log N)^-1) constrains only gradients computed by differentiating through U(θ). Since g_t is emitted by a classical network, the variance decay places **no constraint** on it — the decay is structurally bypassed. Cost scales with P (trainable parameters), not Hilbert-space dimension 2^n. Theorem 2: the agent's own training uses classical backprop, so it does not inherit the pathology.

## Implementation Pattern
```python
# 1. Build hybrid model: classical FC_in → Rx encoding → HEA(ansatz) → measurement → FC_out
# 2. RL agent: MLP policy with spectral normalization, PPO updates
# 3. Per training step:
state = concat(theta, batch_mean_loss, batch_mean_acc, prev_update)
g_t = agent.policy(state)              # surrogate gradient, NOT differentiating U(theta)
theta_next = theta - lr * g_t          # quantum params updated by surrogate
loss.backward()                        # only classical head W, b get true gradients
optimizer.step()                       # Adam over [theta_next treated as constant, W, b]
# 4. Reward for PPO: r = mean_acc + 1.0/(mean_loss + eps)
```

## Honest Limitations (from the paper itself)
1. **Reward concentration in deep barren plateaus**: reward is a function of loss; when the landscape is truly exponentially flat, reward differences vanish at the same rate as cost-function differences — no gradient-free optimizer escapes the exponential shot-budget scaling there. RLQ-Grad gives a *landscape advantage* only when the Jordan algebra leaves the cost non-flat; otherwise only a *computational* advantage.
2. **Poor local minima are NOT bypassed**: when overparameterization p ≥ max_α β_α r_α fails, good local minima are exponentially suppressed for every method, including this one.
3. **Input-gradient decay still propagates**: if U(θ) forms a 2-design, E_θ[‖∇_x ℓ‖²] ≤ Cn/2^n — classical layers upstream of the quantum encoding receive vanishing gradients regardless.
4. Empirical scope: statevector simulators, 2–20 qubits, classification only (no VQE/QAOA/generative), early-onset rather than fully saturated plateau regime.

## Selection Guidance
- Prefer RLQ-Grad over parameter-shift when n ≥ 10 and circuit depth L makes shot-based gradient estimation dominate runtime
- Prefer it over evolutionary search when parameter dimension P is large (RL action space scales with P; evolutionary methods degrade)
- Do NOT expect it to rescue a fundamentally flat landscape (see limitation 1)
