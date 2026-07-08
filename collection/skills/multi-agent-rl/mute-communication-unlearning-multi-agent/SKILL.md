---
name: mute-communication-unlearning-multi-agent
description: "Return-preserving communication unlearning for efficient multi-agent coordination under bandwidth constraints. Enables MARL agents to selectively forget inter-agent communications while preserving coordination returns, addressing the trade-off between communication sparsity and cooperative performance. Activation: MUTE, communication unlearning, MARL, bandwidth constraints, cooperative games, inter-agent communication, partial observability."
metadata:
  arxiv_id: "2607.03473"
  published: "2026-07-03"
  authors: "Rui Zuo, Qinwei Huang, Mingyang Li, Zhenhang Zhang, Simon Khan, Qinru Qiu"
  tags: [mute, communication-unlearning, marl, bandwidth-constraints, cooperative-games, inter-agent-communication, partial-observability]
---

# MUTE: Return-Preserving Communication Unlearning for Efficient Multi-Agent Coordination

## Overview

Inter-agent communication is critical for coordinating Multi-Agent Reinforcement Learning (MARL) agents under partial observability to perform effectively in cooperative games; however, real-world bandwidth constraints demand sparse interactions. Prior approaches primarily address this trade-off by designing communication protocols. MUTE introduces a complementary approach: selectively unlearning (forgetting) communications while preserving coordination returns.

## Key Problem

### Communication Efficiency in MARL
- Agents in cooperative games need to communicate to coordinate under partial observability
- Real-world bandwidth constraints require sparse communication
- Traditional approach: design more efficient communication protocols
- MUTE's approach: selectively forget communications that don't contribute to returns

## Key Innovations

### Communication Unlearning
- Selectively removes learned communication behaviors that are redundant or low-impact
- Preserves the cooperative return (team reward) despite reduced communication
- Complementary to existing communication-efficient MARL methods

### Return-Preserving Guarantee
- Unlearning process explicitly targets communications that don't affect coordination returns
- Ensures that removing communication doesn't degrade team performance
- Distinguishes between communications that are critical vs. those that are noise

## Methodology

1. **Communication Analysis**: Identify which inter-agent messages contribute to returns
2. **Unlearning Process**: Selectively remove non-critical communication behaviors from trained policies
3. **Return Preservation**: Validate that team performance is maintained after unlearning
4. **Bandwidth Reduction**: Measure communication sparsity achieved while preserving returns

## Implications

- Communication unlearning as a new paradigm for MARL efficiency
- Complements existing bandwidth-efficient communication protocols
- Demonstrates that trained MARL policies often have redundant communication
- Practical for deploying MARL in bandwidth-constrained real-world environments

## Pitfalls

- Unlearning may remove communications that are marginally useful in edge cases
- Return preservation is validated empirically, not with formal guarantees
- Unlearning process itself has computational cost
- May not generalize across different cooperative game structures
- Interaction with existing communication-efficient methods needs further study

## Activation Keywords

MUTE, communication unlearning, MARL, bandwidth constraints, cooperative games, inter-agent communication, partial observability, communication sparsity, return preservation, multi-agent coordination

## Paper Reference

arXiv:2607.03473 - "MUTE: Return-Preserving Communication Unlearning for Efficient Multi-Agent Coordination" (Jul 2026)
