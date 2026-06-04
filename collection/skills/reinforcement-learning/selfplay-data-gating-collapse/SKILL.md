---
name: selfplay-data-gating-collapse
description: Analysis of data gating vs reward grounding in self-play RL for LLMs, revealing the Grounded Proposer Paradox and two-stage phase transitions
---

# Survive or Collapse: The Asymmetric Roles of Data Gating and Reward Grounding in Self-Play RL

**arXiv: 2605.22217** | Submitted 21 May 2026

## Core Concept

Self-play RL trains language models on their own generated tasks, co-evolving a proposer and solver without human labels. While recent systems report strong reasoning gains, **collapse and instability are widely observed**. This paper argues collapse is governed by **data-level gating**, not reward design — and reveals a surprising *Grounded Proposer Paradox*.

## Key Findings

### Two Distinct Levers
1. **Data-level gate**: Decides which proposer-generated tasks enter the training pool
2. **Reward signal**: Updates the policy on tasks already admitted

### Asymmetry (Key Result)
- A **strict gate is sufficient for stability** under every reward variant tested
- **No reward variant is sufficient once the gate is removed**

### Grounded Proposer Paradox
A proposer with **ground-truth access accelerates collapse** faster than an ungrounded one when paired with a self-consistency solver. Reason: ground-truth access concentrates training on clean tasks that form the fastest path to a **spurious self-consistent attractor**.

### Phase Transition
Replacing the binary gate with a continuous strictness parameter ε reveals:
- **Training-side metrics decouple at low ε** (training metrics improve but validation doesn't)
- **Validation accuracy holds until ε is much higher**
- A genuine **two-stage phase transition** exists in self-play dynamics

## Implementation Points
- Data filtering (gating) is more critical than reward calibration for self-play stability
- Ground-truth access for proposers is not always beneficial — can accelerate collapse
- Binary gating should be replaced with continuous gating (ε parameter) for finer control
- Monitor both training and validation metrics — they decouple at moderate gating strictness

## Application Scenarios
- Self-play RL for LLM reasoning improvement
- Multi-agent co-evolution training systems
- Any system where a proposer and solver co-evolve without human labels

## Activation Keywords
- self-play RL collapse
- data gating vs reward grounding
- Grounded Proposer Paradox
- self-play phase transition
- proposer-solver co-evolution