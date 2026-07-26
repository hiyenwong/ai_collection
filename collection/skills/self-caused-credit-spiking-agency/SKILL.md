---
title: "Self-Caused Credit Builds Durable Behavioral Self"
arxiv_id: "2606.30191"
authors: ["Haoliang Han"]
date: "2026-06-29"
categories: ["cs.AI", "cs.LG", "cs.NE"]
trigger_words: ["agency detection", "behavioral self", "self-caused credit", "spiking agent", "slow credit", "persistent behavior", "agency-gated learning"]
activation: ["agency", "self", "credit", "durable", "spiking", "behavioral residue", "Nengo", "LIF", "PES"]
---

# Self-Caused Credit Builds Durable Behavioral Self in Minimal Spiking Agent

## Core Contribution

Proposes that **agency-gated slow credit** (conjunctive term `Own*Agency*Salience` driving slow parameter updates) produces **post-unload behavioral residue**: a learned self-preserving choice survives episodic buffer removal.

## Key Mechanisms

1. **Agency Comparator**: Detects self vs world distinction
2. **Slow Credit Channel**: Conjunctive gating `Own*Agency*Salience` performs slow parameter work
3. **Behavioral Residue**: Post-unload self-preservation retained (fraction 0.96, N=50)
4. **Clean Dissociation**: At matched agency gain, durable behavior develops only when self-credit performs slow work (1.00 vs 0.00)

## Experimental Validation

- **Nengo LIF/PES substrate**: Demonstrates on spiking networks
- **Episodic buffer removal**: Learned choice survives (0.96 retention)
- **24D partially-observed control**: Dissociation holds (0.74 vs 0.00)
- **Sequential task learning**: 8 tasks with exogenous interference
  - Old task retention: 0.88 final accuracy, forgetting 0.13
  - Additive pooling collapses to chance
  - No-agency ablation falls below chance
  - No replay buffer needed

## Theoretical Implications

- **Operational behavioral self**: Self-caused credit doing slow work is necessary for agents that develop a self
- **Basin deformation**: Equals net self-credit work
- **No consciousness claim**: Explicitly avoids consciousness claims

## Implementation Pattern

```python
# Pseudo-code for agency-gated slow credit
update_rule = Own_signal * Agency_signal * Salience_signal
slow_param_update = learning_rate * update_rule  # slow timescale
# Only active when agent detects its own agency
```

## Relevance

- Bridging agency detection and durable behavioral change
- Biologically plausible credit assignment without replay buffers
- Potential for continual learning in embodied agents
