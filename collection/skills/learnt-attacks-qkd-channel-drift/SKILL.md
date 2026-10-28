---
name: learnt-attacks-qkd-channel-drift
description: "Methodology from 'Learnt Attacks on Quantum Key Distribution under Channel Noise and Device Drift' (arXiv:2610.01792). Use when modeling adaptive eavesdropping on QKD links under drifting channel noise, constrained-MDP attacker formulations, RL-trained compact quantum attack circuits, security analysis of QKD under non-stationary devices, or Holevo-information optimization attacks on E91/BB84 with noise budgets."
---

# Learnt Attacks on QKD under Channel Noise and Device Drift

Source: arXiv:2610.01792 — Mordarski, Gras, Shehata, Budina, Bondesan (Oct 2026).

## Core insight

QKD links are provisioned with security analyses of **stationary channels**, but the devices that define the channel **drift between recalibrations**. Question answered: does an eavesdropper — who cannot alter the channel's own noise — gain by **following that drift**? Yes, substantially: a reinforcement-learning attacker raises Holevo information from 0.135 (best fixed circuit) to **0.348 at zero detection** (98% of the dynamic-programming upper bound) on device-independent E91 under bilateral depolarising noise.

## Methodology

### 1. Constrained-MDP attacker formulation

Model adaptive eavesdropping as a **constrained Markov decision process**:

- **State**: channel noise level n_t — evolves as an **Ornstein–Uhlenbeck process** (mean-reverting drift; models device drift between recalibrations)
- **Action**: attacker selects one attack circuit per round from a discrete set
- **Constraint**: the abort condition is a **budget over each block of rounds** (detection threshold on observed QBER/statistics); attacker must keep block-statistics inside budget
- **Reward**: Holevo information extracted per round (or fidelity gain on BB84)

Bounds sandwich the value of adaptation:
```
V(fixed best circuit)  ≤  V(adaptive attacker)  ≤  V(DP upper bound)
```
The DP upper bound solves the MDP exactly when the action set and state space are discrete.

### 2. Joint gate-structure + angle search → compact discrete action set

Improvement over Decker et al. (fixed gate template against fixed channel): search **gate structure and rotation angles jointly**. Result: attack circuits compact enough to enumerate as a **discrete action set** — which (a) makes RL well-posed, (b) extends to noise models **lacking a known template**, e.g. amplitude damping.

### 3. Results (paper)

| Setting | Metric | Fixed best | RL attacker | Upper bound |
|---|---|---|---|---|
| DI-E91, bilateral depolarising | Holevo info | 0.135 | **0.348** @ zero detection | 0.355 (98%) |
| BB84, drifting bit-flip channel | fidelity gain | conservative rule | exceeds by 0.024 | 99% of UB |

- Under **stationary** noise, the attacker's gain from basis asymmetry **changes sign** — adaptation is specifically about tracking the drift, not about static asymmetry exploitation.
- Attacks transfer to channels without known templates (amplitude damping) — evidence the approach generalizes beyond hand-designed noise models.

## Reusable attack-analysis pipeline

1. **Threat model first**: write down what the eavesdropper can and cannot touch (here: channel noise untouched — only attacker circuit choice adapts). This determines the MDP state.
2. **Model device drift**: OU process fitted to recalibration intervals; discretize noise levels for the MDP.
3. **Budget constraint**: derive the block abort rule from the protocol's parameter-estimation stage; encode as per-block budget in the MDP.
4. **Action space**: joint structure+angle circuit search → cluster/prune to a compact discrete set (essential for both RL and DP bounds).
5. **Solve three ways**: (a) best fixed circuit (baseline), (b) RL attacker (learned policy), (c) DP over discretized MDP (upper bound). Report the sandwich.
6. **Metrics**: Holevo information at zero detection; fidelity excess over conservative noise-indexed rules; % of DP upper bound achieved.
7. **Sanity checks**: stationary-noise control (gain should vanish or flip), template-free noise transfer (amplitude damping).

## Security-engineering takeaways

- Security analyses that assume a stationary channel **underestimate adaptive adversaries** when devices drift — recalibration cadence is a security parameter, not just an ops one.
- Conservative noise-indexed abort rules (BB84 practice) leave measurable fidelity on the table for adaptive attackers.
- Compactness of the attack-circuit set matters more than circuit expressivity — a small discrete set is enough for near-DP-optimal attacks, hence also enough for tight security bounds.
- Countermeasure direction: budget accounting that adapts with measured drift rate (time-dependent thresholds), or recalibration triggered by drift statistics rather than calendar.

## Pitfalls

1. **Don't compare against a single fixed circuit only** — report the DP upper bound or the claim "98% of optimal" is unanchored.
2. **OU parameters matter** — mean-reversion time vs block length determines how much drift an attacker can exploit; calibrate from real device logs.
3. **Zero-detection ≠ undetectable forever** — the budget is per-block; multi-block statistics can still expose persistent attackers (paper's scope is per-block).
4. **Gate-structure search can overfit small noise models** — validate transfer on a held-out noise family (the amplitude-damping transfer is the paper's own validation).

## Related skills

- `ml-qem-variational-algorithms` — noise modeling on NISQ
- `post-quantum-crypto-analysis` — classical PQC side; this is the quantum-physical-layer side
