---
name: self-caused-credit-spiking-agency
description: "Self-caused credit framework for building durable behavioral self in spiking agents — agency-gated slow credit produces post-unload behavioral residue and prevents catastrophic forgetting without replay buffers (arXiv: 2606.30191)"
tags: [spiking neural networks, agency detection, continual learning, behavioral self, credit assignment, Nengo, catastrophic forgetting]
arxiv_id: "2606.30191v1"
authors: ["Haoliang Han"]
date_added: "2026-06-30"
activation: self-caused credit, agency detection, behavioral self, spiking agent, catastrophic forgetting, slow credit, agency gate, Nengo LIF, post-unload residue, basin deformation
---

## Core Contribution

Demonstrates that **agency-gated slow credit** — a conjunctive term `Own * Agency * Salience` driving slow parameter updates — produces durable behavioral residue in spiking agents. This is the first computational demonstration that detecting agency is insufficient; agency must **do slow work** to build a persistent behavioral self.

## Key Innovation

### The Agency-Credit Dissociation
- **Detecting agency** ≠ **durable self-shaped behavior**
- At matched agency gain, durable behavior develops ONLY when self-credit performs slow work
- Post-unload self-preservation: **1.00** (with slow credit) vs **0.00** (without)
- This dissociation holds across task dimensions (simple choice + 24D partially-observed control)

### Mechanism: Multiplicative Veto
The `Own * Agency * Salience` conjunction acts as a **multiplicative gate** on slow parameter updates:
- **Own**: Signal originates from self-generated actions
- **Agency**: Comparator detects self-causation (prediction matches outcome)
- **Salience**: Behaviorally relevant outcomes trigger learning

This multiplicative structure prevents:
1. Forgetting (old tasks retained: final accuracy 0.88, forgetting 0.13)
2. Catastrophic interference (additive pooling collapses to chance)
3. Requires NO replay buffer and NO task-boundary detection

## Technical Details

### Architecture (Nengo Implementation)
- **Substrate**: Nengo LIF (Leaky Integrate-and-Fire) spiking neurons
- **Learning Rule**: PES (Prescribed Error Sensitivity) on slow decoders
- **Agency Comparator**: Predictive model comparing self-generated vs external outcomes
- **Slow Credit Channel**: Conjunctive gate driving parameter updates at slow timescale

### Experimental Results (N=50 for all)
| Condition | Post-unload self-preservation | Forgetting rate |
|-----------|-------------------------------|-----------------|
| Full model (slow credit + agency gate) | 0.96 | 0.13 |
| Slow decoders reset | 0.00 | — |
| Agency gate removed | 0.00 | — |
| Additive pooling (vs multiplicative) | ~chance | high |
| Episodic/replay baselines | ~chance | high |
| 24D partially-observed control | 0.74 | — |

### Plastic Work Analysis
- **Key result**: Basin deformation = net self-credit work
- Formalizes how slow credit physically reshapes the attractor landscape
- Self-caused learning carves stable attractors that persist after episodic memory is removed

## Theoretical Framework

### Operational Behavioral Self
Defined as durable behavioral residue that:
1. Survives episodic buffer removal
2. Requires slow parameter changes (not fast episodic memory)
3. Depends on agency-gated credit (not just prediction error)
4. Is formally measurable via post-unload behavioral assays

### Necessary Building Block Argument
Self-caused credit doing slow work is argued to be a **necessary** (not sufficient) building block for agents that develop a self:
- Without it: no durable behavioral patterns persist
- With it: behavioral self emerges as attractor landscape deformation
- No consciousness claim is made — purely operational/behavioral

## Connections to Related Work

### Predictive Processing / Active Inference
- Builds on Ye (2026) agency detection in predictive systems
- Extends from detecting agency to **using** agency for durable learning

### Catastrophic Forgetting Solutions
- Contrasts with replay-based methods (no buffer needed)
- Contrasts with regularization methods (no task-boundary detection)
- Provides biologically-motivated alternative to EWC, A-GEM, etc.

### Enactivism / 4E Cognition
- Computational implementation of enactive self-construction
- Agent actively shapes its own behavioral dispositions through self-caused experience

### Spiking Neural Networks
- Demonstrates SNNs can implement sophisticated credit assignment
- Uses biological timescale separation (fast spiking + slow plasticity)
- Nengo framework enables large-scale simulation

## Implementation Guide

### Core Algorithm
```
For each timestep t:
    1. Compute action from current policy (fast spiking dynamics)
    2. Observe outcome
    3. Agency comparator: predict outcome from action → compute agency signal
    4. Salience computation: outcome relevance/modulation
    5. Self-credit = Own(t) * Agency(t) * Salience(t)
    6. IF self-credit > threshold:
         Update slow decoders: Δw = η * self-credit * error_signal
    7. Fast dynamics continue with updated slow context
```

### Key Parameters
- **η (slow learning rate)**: Much smaller than fast learning rate
- **Agency threshold**: Minimum prediction match for agency attribution
- **Timescale separation**: Slow updates (τ_slow >> τ_fast)
- **Salience modulation**: Task-dependent relevance weighting

### Nengo Implementation Notes
- Use `nengo.Ensemble` with LIF neurons for spiking substrate
- `nengo.PES` learning rule on connection decoders for slow credit
- Agency comparator as separate predictive ensemble
- Multiplicative gating via `nengo.networks.EnsembleArray` product network

## Applications

### For Continual Learning
- Alternative to replay-based anti-forgetting
- Biologically plausible mechanism for lifelong learning
- Applicable to robotics and embodied AI

### For AI Safety/Alignment
- Operational framework for understanding self-model in AI agents
- Connection between agency detection and durable value alignment
- Testable predictions about self-model development

### For Neuroscience
- Predictions about basal ganglia/slow plasticity interactions
- Hypothesis: agency-gated slow credit in cortico-basal circuits
- Links to sense of agency literature in cognitive neuroscience

## Falsification Predictions

1. **Removing slow credit channel** → immediate loss of durable behavior (confirmed)
2. **Replacing multiplicative with additive** → catastrophic forgetting (confirmed)
3. **Matching agency gain without slow work** → no behavioral residue (confirmed)
4. **Predicted**: Lesioning analogous circuits in biological agents should impair durable habit formation while sparing fast learning

## Activation Triggers

self-caused credit, agency detection, behavioral self, spiking agent, catastrophic forgetting, slow credit, agency gate, Nengo LIF, post-unload residue, basin deformation, multiplicative veto, continual learning, enactive self
