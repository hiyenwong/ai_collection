---
name: repulsive-self-attention-nonequilibrium
description: Use when analyzing attention dynamics or recurrent transformer collective behavior. Minimal repulsive self-attention model (V=-I) exhibiting chaos, attention condensation, and emergent locality across d=2 and d=N scaling regimes.
trigger: repulsive self-attention, attention condensation, nonequilibrium attention phases, recurrent transformer dynamics, flip bifurcation attention, butterfly cone routing, attention chaos, softmax sharpness scaling, emergent locality
category: ai_collection
---

# Nonequilibrium Phases of Repulsive Self-Attention

**Source**: arXiv:2609.28448v1 (2026-09-23) — Gao, Yang, Chen (cond-mat.dis-nn).

## The Minimal Model

Recurrent transformer with N normalized tokens, **Q = K = I** (similarity-based attention selects nearby representations) and **V = −I** (negative value map drives tokens *away* from the selected field). This feedback continually reorganizes representation geometry AND the attention network.

Two control parameters: attention feedback strength **γ**, softmax sharpness **β**.

## Phase Structure (two scaling regimes)

### d = 2 (tokens on a circle)
- Regular polygon = exact fixed point.
- Increasing γ: polygon loses stability via **flip bifurcation** → period-two motion → **chaos** → cluster-exchange / cluster-flip states.
- **Attention stays diffuse** as N→∞ at finite fixed β — temporal complexity ≠ attention concentration.
- **Attention condensation** only emerges in the scaling regime **β ~ N²**.
- Hard-routing limit: repulsive updates amplify local perturbations; routing-partner switches transmit them **ballistically** → emergent **butterfly cone** in representation space.

### d = N → ∞ (high-dimensional geometry)
- Evidence for a **condensation transition at β = O(1)** (vs N² in low-d), driven by **dynamically generated finite overlap gaps**.
- Phases vs γ: diffuse simplex-like states → consensus flips → condensed active routing with chaos signatures → fragmented cluster flips.

## Key Conceptual Results

1. **Temporal activity, attention condensation, and geometric clustering are distinct collective phenomena** — a model can be chaotic while attention stays diffuse.
2. **Sparse attention can sustain persistent dynamics rather than freeze it** — against the intuition that attention concentration freezes token geometry.
3. Dimensionality provides a distinct route to localization (d=N condenses at constant β; d=2 needs β~N²).

## Usage

- Analytical prototype for studying attention dynamics: bifurcation analysis, chaos measures, condensation order parameters — all tractable in this minimal setting.
- Interpretability lens: when training dynamics show token geometry reorganization, check whether the feedback (V sign structure) drives repulsion vs attraction; the phase taxonomy (diffuse/condensed/clustered × chaotic/periodic) classifies observed regimes.
- Design heuristic: **β scaling relative to N** determines whether attention concentration can occur — connects softmax temperature schedules to phase behavior.

## Implementation Sketch (simulation)

```
tokens x_i ∈ R^d, ||x_i|| = 1
A_ij = softmax_j(β·x_i·x_j)          # Q=K=I
x_i ← normalize(x_i + γ·Σ_j A_ij·(−x_j))   # V=−I, feedback γ
# d=2: track polygon flip; d=N: track overlap gaps g_ij = x_i·x_j
```

## Related Skills

- `attention-sink-structural` — attention concentration phenomenology
- `chaos-programming-neural-circuits` — chaos in neural circuits
- `attention-frustrated-synchronization-fsn` — frustrated attention dynamics
