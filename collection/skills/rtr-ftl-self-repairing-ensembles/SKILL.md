---
name: rtr-ftl-self-repairing-ensembles
description: Online sensor-failure recovery via masked RNN ensembles.
category: ai_collection
trigger: recurrent policy self-repair, Kalman fusion ensemble policy, RFLO online gradient, distribution shift recovery without expert, follow-the-leader consensus loss, random observation masking diversity, real-time recurrent learning deployment, RTR-IIL online imitation
---

# Self-Repairing Recurrent Ensembles (RTR-FTL) for Real-Time Distribution-Shift Recovery

**Paper**: Lemmel, Wendel Garcia, Kobayashi, Grosu — "Self-Repairing Recurrent Ensembles for Real-Time Recovery from Distribution Shift" (arXiv:2610.03249, TU Wien / MedUni Wien / NII Tokyo, IJCAI-style 2026)

## Core Insight

A sufficiently diverse ensemble contains its own supervision. If each member sees a *different randomly masked subset* of the observation, a shift corrupting one dimension confuses only the members that depend on it; the rest keep predicting sensible actions. Kalman-gain fusion then (a) makes confident members dominate the consensus and (b) provides a self-supervised label that confused members can be pulled back toward — online, at every control step, with no expert and no replay buffer.

## Architecture

- **Ensemble**: N recurrent networks (CT-RNN or LRU), each predicting Gaussian action distribution N(μ_n, σ²_n), each initialized differently.
- **Random observation masking**: each member receives a binary-masked subset of observation dims (visibility prob. 0.5–0.7 optimal). Masking is the *diversity manufacturing mechanism*, not the robustness mechanism itself — recovery comes from online fine-tuning; masking alone restores nothing (verified: LR=0 curves stay collapsed at all mask rates).
- **Member dynamics options**:
  - CT-RNN: `x_{t+1} = x_t + (1/τ)[−x_t + φ(Wξ_t)]`, ξ_t = [x_t; u_t; 1]
  - LRU: complex-diagonal SSM `ḣ = Ah + Bx`, y = Re[Ch] + Dx — efficient online updates.

## Kalman-Gain Fusion (sequential)

Combine member Gaussians in fixed order, n = 1..N:

```
k_n        = σ̄²_{n-1} / (σ̄²_{n-1} + σ²_n)          # Kalman gain vs running fusion
σ̄²_n       = (1−k_n) σ̄²_{n-1} + k_n σ²_n
μ̄_n        = μ̄_{n-1} + k_n (μ_n − μ̄_{n-1})
```

Final fused action distribution N(μ̄_N, σ̄²_N). Confused members report high variance → low gain → they don't corrupt the consensus. (Order matters; paper keeps it fixed.)

## Self-Supervised Follow-The-Leader Loss (RTR-FTL)

Consensus mean μ̄_N is the label; each member is trained toward it, weighted by the **complement of its own squared Kalman gain** k̄_n² (recomputed post-fusion):

```
L_SR = −Σ_n (1 − k̄_n²) · log p(μ̄_N | μ_n, σ²_n),
       k̄_n² = σ̄²_N / (σ̄²_N + σ²_n)
```

Low-contribution (confused) members get the strongest correction toward the consensus; high-contribution (confident) members get almost none. This is TTRL-style test-time self-improvement (Zuo et al. 2025) transposed from discrete majority votes to continuous action distributions — behavioral cloning toward the consensus admits a single-step gradient, compatible with control-loop rates, unlike an RL objective.

## RFLO: Real-Time Gradients for Recurrent Members

BPTT requires buffering + replay — incompatible with live control. RFLO (Murray 2019) approximates RTRL by dropping the non-local Jacobian coupling term:

```
Ĵ_{t+1} ≈ (1 − 1/τ) Ĵ_t + (1/τ) φ′(Wξ_t)^T ξ_t      # local, O(1) per step
Δθ(t)   = η · B ε_t ⊙ Ĵ_t                             # fixed random feedback B
```

- No weight transport, no backward phase → biologically plausible.
- B aligns with readout weights over time (feedback-alignment effect), so error keeps decreasing.
- Parameter update follows *every environment step* → the policy adapts as the shift unfolds, not after the episode.

## Dual Regime (one machinery)

- **RTR-FTL** (no expert): consensus label μ̄_N from fusion, L_SR as above.
- **RTR-IIL** (expert present, teleoperation): replace consensus label with expert action a*, identical RFLO update → fully online EnsembleDAgger. Expert handover gated by thresholds: ‖π̄(s) − π*(s)‖ > τ_m or Var(π̄(s)) > τ_v.

## Verified Results (brax/Mujoco, 10 seeds)

| Shift type | Setup | Outcome |
|---|---|---|
| Sensor offset (ant, idx 5, +0.1) | mask 0.5/0.7 | recovers ≈ full pre-shift reward over 100 ep; mask 1.0 (full visibility) **fails to recover** |
| Sensor failure (ant, idx 10 pinned 0) | 5 modules, mask 0.5 | significant recovery; 5-module ensemble best |
| Gradual noise (halfcheetah, linear σ→0.1) | 10 modules, mask 0.5 | RTR-FTL ≫ LR=0 in cumulative distance, never resets |
| RTR-IIL from scratch (ant/halfcheetah/humanoid) | LRU/CT-RNN | on par with batch-replay EnsembleDAgger (MLP/BPTT/LRU) while fully streaming |

**Central claim**: robustness comes from the *diversity masking induces*, not the ensemble or fusion rule alone — full-visibility ensembles collapse under the same shifts and never recover.

## Implementation Checklist

1. Pretrain ensemble from offline expert (PPO) trajectories with per-member random binary observation masks.
2. Run members forward each step; fuse sequentially with Kalman gains; execute a ~ N(μ̄_N, σ̄²_N).
3. Recompute k̄_n² against final fusion; compute L_SR; RFLO gradient; apply per-step update.
4. Monitor fused variance σ̄²_N as a built-in anomaly signal (rises when members disagree = shift detected).
5. If expert available: swap label source, keep everything else identical.

## Limitations (stated by authors)

- Untested on simultaneous/multi-sensor mixed corruption; shifts correlated with agent actions untested.
- Sim-only; physical-platform transfer pending.

## Relation Map

- TTRL (Zuo et al. 2025): majority-vote proxy reward → here continuous Kalman consensus + BC (single-step gradient).
- EnsembleDAgger (Menda et al. 2019): ensemble as doubt estimator → here ensemble as *self-supervision source*.
- Tent/TTA entropy minimization (Wang et al. 2020): perception-level self-consistency → here action-level, recurrent, per-control-cycle.
- RFLO/e-prop lineage: Murray 2019 (RFLO), Bellec et al. 2020 (e-prop), Zucchet et al. 2023 (diagonal+online).
- Domain randomization (Tobin et al. 2017): robustness without adaptation → masking is diversity manufacture, adaptation does the recovery.
