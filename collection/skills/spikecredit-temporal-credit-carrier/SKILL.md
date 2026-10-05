---
name: spikecredit-temporal-credit-carrier
description: SNN temporal credit carriers for sparse-reward RL.
category: ai_collection
---

# SpikeCredit: Temporal Credit Carriers for Sparse-Reward RL

**Source**: arXiv:2609.35268 (Yu, Sun, Pan, Chen, Hong, Hao, Jin — Donghua/Westlake/Imperial, 28 Sep 2026)

Use when: reinforcement learning with terminal-only (sparse/ delayed) rewards; credit assignment in spiking neural network (SNN) actors; reward redistribution; making internal policy dynamics credit-readable.

## Core Insight

Prior sparse-reward RL asks "how to redistribute delayed outcomes". SpikeCredit asks the prior question: **where is credit-relevant temporal information preserved in the first place?** Answer: policy internal dynamics. Formalized as **Temporal Credit Carriers (TCCs)** — neural states whose temporal evolution preserves information that later supports transition-level credit inference. SNN actors naturally instantiate TCCs via two complementary dynamics:

- **Membrane potentials** = graded temporal integration → preserve slowly-evolving behavioral dependencies
- **Spike events** = sparse localized markers → expose event-specific temporal evidence

Biological grounding: fast sensorimotor feedback constrains ongoing movement; delayed reward signals reshape future control (Wolpert/Scott/Schultz fast-slow motor learning).

## Framework: Closed Read-Write Loop

### Stage 1: Task-Adaptive TCC Selection (training-free)
Collect random rollouts; per transition compute:
- D_t = ‖Δs_t‖² (state displacement), A_t = ‖a_t‖² (action energy)
- **Task event score**: E_task = e_rhythm + e_burst where
  - e_rhythm = max(0, Lag1(A) − Lag1(D)) — periodic action structure
  - e_burst = BurstFrac(A) · max(0, Lag1(D)) — localized action bursts under coherent transitions
- Select: c* = spike carrier if E_task > δ, else membrane carrier
- Empirical: Ant/Hopper → membrane (smooth dynamics); Swimmer/Walker2d → spikes (rhythmic/burst structure). Selected carrier beats the alternative on every task — no single carrier is universally optimal.

### Stage 2: Fast Pathway — SMF (Self-Motion Feedback Constraint) reads credit
Per episode, record TCC dynamics h_t^(c*). Lightweight scorer f_φ: S_t^TCC = f_φ(h_t). Terminal R alone under-determines credit, so add a **behavior-grounded temporal anchor** — linear proxy p_ψ on self-motion z_t = [s_t, Δs_t, ‖a_t‖²]:

L_SMF = L_return + λ_align·L_align + λ_sparse·L_sparse
- L_return = (Σ S_t^proxy − R)²/T — proxy scores aggregate to episodic outcome
- L_align = KL(Ŝ^proxy ‖ Ŝ^TCC) — softmax-normalized (temperature τ_f), transfers behavior-grounded temporal structure INTO the TCC scorer
- L_sparse = ‖W_proxy‖₁ — compact interpretable proxy

Recompute with updated scorer: Ŝ^TCC,+ = Softmax(sgn(R)·Norm(S^TCC,+)/τ_s) — direction-aware (for R<0, ordering reverses). Redistribute: r̂_t = R·Ŝ_t^TCC,+; credit target y_t = log(T·Ŝ_t^TCC,+) (y>0 above-uniform, y=0 uniform, y<0 below). Store both in replay buffer.

### Stage 3: Slow Pathway — CTT (Credit-Targeted Trace Alignment) writes credit
During actor updates: replayed states → current actor → new TCC dynamics h_θ^(c*)(s_i); **frozen scorer** f_φ+ maps them to scores; align with stored targets via Huber loss:
- L_CTT = (1/B)Σ Huber(f_φ+(h_θ^(c*)(s_i)), y_i)
- Actor loss: L_actor = −(1/B)Σ Q(s_i, π(s_i)) + λ_CTT·L_CTT
- Freezing the scorer makes recovered credit a fixed shaping target — gradients reshape the ACTOR's internal dynamics to become more credit-readable, not the estimator

### Stage 4: Closed loop
Episode end → SMF reads → (r̂_t, y_t) stored → critics update on r̂_t (TD3 twin critics) → delayed actor updates align future TCCs to y_t → next episode's dynamics are more readable. Credit inference and representation shaping mutually reinforce.

Backbone: CaRe-BN (recent spiking RL); TD3-style updates; SMF once per episode; CTT only on delayed actor updates after warm-up.

## Results (sparse-reward MuJoCo, 5 seeds)

| Task | Last10 gain vs sparse SNN | vs dense-reward SNN |
|------|---------------------------|---------------------|
| Ant | +1169% | approaches |
| Hopper | +953% | approaches |
| Swimmer | +723% | **exceeds dense +113%** |
| Walker2d | +1781% | approaches |

Mechanistic validation: recovered credit vs true dense rewards (Ant): transition-wise **Pearson 0.63 / Spearman 0.64**; temporal profile 0.62/0.67. Sparse SNN baseline: ≈0 correlation.

Controls (Fig 4c): uniform mean redistribution / rate-coded TCCs (discard fine temporal structure) / time-shuffled TCCs (break trajectory alignment) all fail consistently → gains require transition-specific credit + fine-grained dynamics + correct temporal alignment jointly.

## Ablations (Ant)
- Full: 1669.9±402.8 (peaks ~995K steps)
- w/o s_t: 544.4 (peaks at 20K — no sustained learning)
- w/o SMF: 192.7 — collapse; credit reading is the load-bearing component
- w/o CTT: 1403.8 — writing further boosts but reading is primary
- SMF attribution: dominated by state/state-change features (forward velocity, joint/foot velocities); action energy contributes least

## Implementation Notes

- TCC selection is training-free — compute Lag1 autocorrelations + burst fraction from random rollouts
- Direction-aware redistribution (sgn(R)) is critical for negative outcomes
- Proxy is LINEAR + L1-regularized — deliberately interpretable, not a learned reward model
- Applicable beyond SNNs conceptually: any recurrent policy exposes candidate TCCs (hidden states); SNNs make the two timescales explicit (membrane vs spike)
- Related classical lineage: eligibility traces / R-STDP (Izhikevich, Florian, Frémaux-Gerstner) modulated local plasticity; SpikeCredit instead reads/writes credit at the trajectory level

## Related Skills
- `score-broadcast-decorrelation-credit-assignment` — broadcast credit assignment
- `shunting-inhibition-dendritic-credit` — dendritic credit pathways
- `diffusing-blame-dale-principle-credit-assignment` — Dale-principle credit propagation
- `snn-world-model-prediction-chain` — spiking world models for RL
