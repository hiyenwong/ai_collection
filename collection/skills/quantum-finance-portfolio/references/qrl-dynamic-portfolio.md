# QRL for Dynamic Portfolio Optimization — Detailed Patterns

Source: arXiv:2601.18811 (Gurgul, Chen, Lessmann, 2026-01-20)

## QDDPG Architecture

State → VQC Actor (angle encoding) → Portfolio weights (continuous)
State, Action → VQC Critic (amplitude encoding) → Q-value

### Training Loop

1. Sample action from VQC policy π(s; θ_actor)
2. Execute action, observe reward r and next state s'
3. Critic TD target: y = r + γ·Q(s', π(s'; θ_actor'); θ_critic')
4. Update critic: minimize MSE(Q(s,a; θ_critic), y)
5. Update actor: maximize Q(s, π(s; θ_actor); θ_critic) via policy gradient
6. Soft update target networks: θ' ← τθ + (1-τ)θ'

### Parameter Efficiency

- QDDPG achieves similar Sharpe ratio to classical DDPG with ~50% fewer parameters
- VQC exploits tensor product structure for compact representations
- Critical for NISQ where circuit depth is coherence-limited

## NISQ Implementation Tips

1. Circuit depth: start with p ≤ 2 layers on real hardware
2. Shots: ≥ 1000 per expectation value for stable gradients
3. Barren plateaus: initialize near identity, use layerwise training
4. Error mitigation: apply ZNE for improved VQC gradient estimates
