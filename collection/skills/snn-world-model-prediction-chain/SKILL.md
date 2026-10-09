---
name: snn-world-model-prediction-chain
description: Fully-spiking world-model rollout for model-based RL.
trigger: spiking world model, model-based RL SNN, world state prediction chain, gating synapses, CoLaNET, imagination loop SNN, purely spiking inference, LIF temporal coding
license: MIT
metadata:
  arxiv_id: "2609.27459"
  published: "2026-09-23"
  authors: "Mikhail Kiselev (Chuvash State University)"
  tags: [spiking-neural-network, model-based-rl, world-model, gating-synapses, LIF, CoLaNET]
---

# Fully-Spiking World-Model Prediction Chain (SNN Imagination Loop)

Methodology from arXiv:2609.27459 — "Spiking Neural Network Predicting Sequence of the External Worlds States in Model-Based Reinforcement Learning" (Kiselev, Sep 2026). Follow-up to NEUROINFORMATICA-2026 work on purely-spiking model-based RL.

## Core Contribution

First demonstrated SNN that **rolls out a chain of predicted future world states** — starting from the current state — with **all supporting mechanisms implemented as spiking neuron ensembles** ("only-spikes, only-SNN" principle). The world dynamics model (learned elsewhere by a CoLaNET ensemble) is imported into a new inference SNN; prediction, memory, state updating, and loop termination are entirely spiking circuits, no external digital processing.

## 1. World State Formalization (Time-Augmented Markov)

World state = Cartesian product of S elementary state sets. Each dimension a carries **both a value AND an age**:

```
current world state = {a | <s_a^i, t_a^i>}
- s_a^i ∈ [1..S_a]: elementary state value of dimension a (e.g., ball X-coordinate bin)
- t_a^i ∈ [1..T]: which time interval since dimension a LAST CHANGED to its current value
```

This is a step beyond classic Markov: the **temporal coordinate is discretized** (T intervals) and part of the state. Example (ATARI ping-pong, 5 dimensions): ball (X,Y) coordinates, ball (Vx,Vy) velocity components, racket Y. For a ball moving right, next elementary state after <x,t> is <x+1,t> OR <x,t+1> — the network must learn WHICH.

## 2. Neuron Model Extensions (the enabling mechanisms)

Base: current-based LIF with delta synapses (instant weight jump per spike), membrane reset by threshold h. Implemented on Loihi/TrueNorth-class neuroprocessors.

### Gating synapses (do NOT change membrane potential — change activity state)
Each neuron has an activity variable a; active iff a>0. Per simulation step: a decreases by 1 if a>0, increases toward 0 if negative, jumps to +∞ when passing -1.

```
Spike at gating synapse (weight ω):
  ω < 0 → a ← min(a, ω)   [BLOCKING: neuron silenced for |ω| steps — a refractory period]
  ω > 0 → a ← max(a, ω)   [ACTIVATING: enables repeat of input spike train while ISI ≤ ω]
```

### Spike-train emission (short-term memory)
A neuron parameter > 1 sets the **length of a spike train** emitted after firing — sustained output until terminated by a negative gating spike. This is the state-holding primitive.

### Forced firing synapses
Very strong excitatory synapses fire the neuron unconditionally on input spike; membrane reset to 0. Used for hard-wired routing of control flow.

## 3. The Inference Architecture ("Imagination" loop)

```
Input node block (initial {<s,t>} pairs, 1 spike each)
        │
        ▼
Imagination block — neurons with spike-train memory: once triggered,
  keep firing until blocked. Holds CURRENT hypothetical state.
        │  feeds as input
        ▼
CoLaNET ensemble (imported world-dynamics model, green box):
  one classifier per <s_a^i, t_a^i> pair; learns states from which the
  world can immediately pass INTO the given state
        │
        ▼ OUT neuron fires → predicts NEXT world state
CoLaNET_Output_Gate — repeats spike; can terminate the chain
        │
        ├──► triggers corresponding Imagination neuron (new state active)
        └──► inhibits ALL OTHER Imagination neurons of the same dimension
              (winner-take-all per dimension → excludes ambiguity)
        └─ loop closed → next prediction step
```

**Loop closure trick**: the predicted-next-state spike both (1) activates the new state's memory neuron and (2) laterally inhibits competing states in the same dimension. The world model consumes its own predictions as new inputs — autonomous multi-step rollout.

## 4. Learning (done in a separate SNN, then imported)

- Time representation module: per elementary state, a small SNN with 1 input → T output neurons; output neuron t fires a train once the input has been active for interval t (built from forced connections with delays D, blocking connections, and spike-train generators).
- CoLaNET classifiers (columnar SNN, local learning): modified variants for zero vs nonzero t_a^i.
- Plasticity: 1-factor (weight decay on pre-spike), 2-factor anti-Hebbian (depress recently-active inputs at post-fire), 3-factor dopamine (reward-modulated), plus weight redistribution keeping per-neuron total weight constant.

## 5. Results (ATARI Ping-Pong)

| Metric | SNN inference | Algorithmic (C++) inference |
|---|---|---|
| Mean standard error (hit-point Y) | 8.93 | 8.3 |
| No-prediction rate (endless loop) | 0.45% | — |
| Std between series | 1.2 / 0.4 | 1.3 |

SNN inference ≈ algorithmic baseline (<2σ difference); accuracy-vs-starting-X curves and heatmap patterns (error and no-prediction vs X-bin × Vx-bin) nearly identical. Validates that the spiking control logic preserves the learned model's predictive quality.

## Why It Matters

1. **Neuromorphic path to model-based RL**: prior SNN world models (PNAS 2025 spiking world model) treat dynamics as discrete state sequences without temporal structure or use extra-network digital components; this work keeps the temporal dimension and achieves full on-chip deployability.
2. **Design pattern for spiking control flow**: gating synapses + spike-train memory + forced firing + winner-take-all inhibition = a reusable toolkit for building loops, latches, and conditional routing **in spikes** — the spiking analog of program counters and registers.
3. **Separation of learning and inference**: model trained in one SNN context, exported, embedded in another — portability of learned spiking models.

## Limitations (stated by author)

- Learned-model transfer is currently physical (export/import); unified learn+infer SNN is future work.
- Validated on one simple 5-dimension benchmark.

## Related Skills
- [[spiking-mode-neural-networks]] — Hopfield-decomposition mode/pattern training
- [[spiking-tolman-eichenbaum-machine]] — spiking world models for navigation
- [[dt4x-plus-diagnosis-decision-tree]] — decision-tree rule extraction (analogous interpretable model)

## Sources
- arXiv:2609.27459 — Kiselev, "SNN Predicting Sequence of the External Worlds States in Model-Based RL"
- Kiselev, "Toward a Purely Spiking Implementation of Model-Based Reinforcement Learning", NEUROINFORMATICA-2026
- CoLaNET lineage: Larionov/Bazenkov/Kiselev (columnar SNN continual learning), Goryunov et al. 2025 (training dynamics)
