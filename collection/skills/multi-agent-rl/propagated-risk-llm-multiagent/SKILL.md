---
name: propagated-risk-llm-multiagent
description: "Estimation of propagated risk in LLM-based multi-agent systems. Use when modeling error propagation and reliability in multi-agent LLM pipelines."
version: 1.0.0
author: Hermes Agent
date: 2026-10-27
source: arXiv:2610.33282
tags: [multi-agent-systems, llm-reliability, error-propagation, risk-estimation, uncertainty, sender-receiver]
category: multi-agent-rl
---

# Estimation of Propagated Risk in LLM-based Multi-Agent Systems

## Core Contribution

Introduces a framework for explicitly modeling how realized sender-receiver interactions affect error propagation in LLM-based multi-agent systems. Unlike prior uncertainty estimation methods, this approach captures the actual risk transmitted between agents.

## Key Insights

- **Problem**: Actions by upstream agents affect correctness of downstream agents, but existing approaches don't explicitly model realized sender-receiver interactions
- **Challenge**: Multi-agent LLM systems introduce distinctive reliability challenges through cascading errors
- **Gap**: Prior work investigates error propagation but doesn't model how specific agent interactions transmit risk

## Technical Approach

1. **Sender-Receiver Modeling**: Explicitly model how information flows between agents
2. **Risk Propagation Framework**: Track how errors propagate through agent chains
3. **Realized Interaction Analysis**: Focus on actual interactions rather than theoretical uncertainty
4. **Downstream Impact Estimation**: Quantify how upstream agent actions affect downstream correctness

## Applications

- Reliability engineering for multi-agent LLM systems
- Error analysis in agent pipelines
- Designing robust multi-agent architectures
- Uncertainty quantification in agentic workflows

## Activation Triggers

Use this skill when:
- Building multi-agent LLM systems and need reliability analysis
- Debugging error propagation in agent pipelines
- Designing fault-tolerant multi-agent architectures
- Estimating risk in cascaded LLM agent systems

## Related Concepts

- Multi-agent systems
- LLM reliability
- Error propagation
- Uncertainty quantification
- Agent orchestration

## References

- arXiv:2610.33282
- Categories: cs.AI, cs.MA
