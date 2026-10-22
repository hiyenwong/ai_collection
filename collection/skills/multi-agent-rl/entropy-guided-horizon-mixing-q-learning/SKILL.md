---
name: entropy-guided-horizon-mixing-q-learning
description: "Entropy-guided multi-discount horizon mixing for Q-learning."
category: reinforcement-learning
---

# Q(γ_H): Entropy-Guided Horizon Mixing in Multi-Discount Q-Learning

Source: arXiv:2610.21764 (Arwa Albelaihi, Abdulrahman Altahhan — University of Leeds, Oct 2026). Multi-horizon Q-learning that keeps K discount-specific heads and mixes them at control time with an entropy-derived confidence signal; Bellman updates stay untouched. Strongest gains on delayed-credit tasks; best AUC in deep RL across CartPole/Acrobot/MountainCar.

Use when: a single discount factor is hard to choose or the needed planning horizon shifts during training (short horizon stabilizes early bootstrapping; long horizon needed later for credit assignment), in value-based RL (tabular, linear/tile-coding, or deep DQN/DDQN), especially delayed-reward or navigation tasks.

## Mechanism

A fixed γ imposes one horizon for the whole run. Q(γ_H) maintains K heads with discounts γ₁<…<γ_K, each trained by its own STANDARD fixed-γₖ Q-learning update (targets never modified), sharing one experience stream and feature basis. Only action selection mixes them — horizon adaptation is fully decoupled from learning updates. Neuro motivation: dopaminergic neurons encode RPEs at multiple discount time constants.

## Algorithm (per step)

1. **Heads**: Q⁽ᵏ⁾(s,a) = Wₖ(a,:)⊤φ(s); fixed positions uₖ = (k−1)/(K−1) ∈ [0,1] (u₁=0 shortest horizon, u_K=1 longest).
2. **Reference vector** (max–min aggregation across heads): q_ref(a) = η·maxₖ Q⁽ᵏ⁾(s,a) + (1−η)·minₖ Q⁽ᵏ⁾(s,a); default η = 0.5.
3. **Boltzmann reference policy**: π_ref(a|s) ∝ exp(q_ref(a)/τ); normalized Shannon entropy H_n(s) = −(1/log|A|) Σₐ π_ref(a|s) log π_ref(a|s).
4. **Confidence**: c(s) = 1 − H_n(s) ∈ [0,1] (low entropy = decisive = high confidence).
5. **Mixing weights**: softmax over negative distances, wₖ(s) ∝ exp(−β|uₖ − c(s)|) — LOW confidence lands on SHORT-horizon heads; HIGH confidence shifts weight to LONG horizons.
6. **Act** ε-greedily on Q_agg(s,a) = Σₖ wₖ(s)Q⁽ᵏ⁾(s,a).
7. **Update every head independently**: δₖ = r + 1{s′∉T}·γₖ·maxₐ′ Q⁽ᵏ⁾(s′,a′) − Q⁽ᵏ⁾(s,a); Wₖ(a,:) ← Wₖ(a,:) + α·δₖ·φ(s).

The mixture-weighted discount summary γ̄(s) = Σₖ wₖ(s)γₖ is DESCRIPTIVE ONLY — it is not the discount of any equivalent Bellman operator.

## Results (N=10 seeds)

- Tabular/linear (tile coding), 8 benchmarks: best mean AUC on delayed-credit tasks — MountainCar −6.0%, Acrobot −2.1% vs the next-best fixed-γ baseline that was handed the ORACLE γ per task.
- Deep (shared-trunk multi-head DDQN): best AUC on all of CartPole-v1 / Acrobot-v1 / MountainCar-v0; +8.5% (Acrobot) and +7.0% (MountainCar) over DDQN; +48.0% over Scheduled-γ on Acrobot (p<0.0001), +21.4% over Ogawa-Adapt.
- Gains concentrate where credit is delayed; competitive elsewhere; fixed-γ can still win when one horizon suffices or risk-sensitivity dominates.

## Complexity and practice

- Overhead linear in K: O(K|A|d) memory and per-step compute; reference/entropy/weighting add only O(K|A|). Tabular/linear needs no replay buffer or target network.
- Hyperparameters: the γ set (e.g., spread 0.80→0.99), τ (Boltzmann temperature), β (mixing sharpness), η (optimism of the reference), ε-schedule (ε₀=0.10, decay 0.985 in the paper).
- Ablations: max–min reference (η=0.5) beats a single-head reference; confidence gating is the load-bearing part (removing it collapses to fixed uniform mixing ≈ Hyperbolic DQN).
- Mixing changes only the behavior policy of an off-policy learner — keep exploration sufficient; heads stay standard Q-learning so any Q-learning improvement (double Q, target nets) composes.

## Relation

- Generalizes Hyperbolic DQN (K heads, fixed uniform mix) by adding a learned state-dependent gate; unlike adaptive-γ methods (Ogawa: critic-loss PID controller; Scheduled-γ: linear ramp) it never modifies Bellman targets or learns γ(s).
- Related skills: [[ema-momentum-coefficient-rlvr]] (RLVR optimizer dynamics), [[gppo-f-divergence-trust-region-policy-optimization]], [[policy-gradient-baselines-score-centering]], [[multi-timescale-conductance-snn]] (multi-timescale aggregation in SNNs).

## Activation keywords

discount factor selection, multi-horizon Q-learning, adaptive discount, planning horizon, delayed credit assignment, entropy confidence, multi-discount heads, horizon mixing, Q(γ_H)
