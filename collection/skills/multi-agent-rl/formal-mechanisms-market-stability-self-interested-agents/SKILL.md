---
name: formal-mechanisms-market-stability-self-interested-agents
description: "Multi-agent marketplace simulation studying formal mechanisms for market stability with self-interested LLM agents. 18 DeepSeek-V3 agents with complementary specialties trade in constrained network. Mediation identified as top mechanism, robust under adversarial attack. Activation: market stability, self-interested agents, multi-agent economics, cooperation mechanisms, social dilemmas."
metadata:
  arxiv_id: "2607.08652"
  published: "2026-07-09"
  authors: "Eugene Ng Yi Sheng, Bingquan Shen"
  tags: [market-stability, self-interested-agents, multi-agent-economics, cooperation-mechanisms, social-dilemmas]
---

# Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study

## Overview

Self-interested agents, left unconstrained, tend toward defection in repeated social dilemmas, causing cooperative gains from trade to collapse. This paper investigates what formal mechanisms are sufficient for a society of self-interested LLM agents to maintain market stability, and how resilient those mechanisms are to adversarial attack, using a multi-agent marketplace simulation with 18 LLM agents.

## Key Innovations

### Multi-Agent Marketplace Simulation
- 18 LLM agents (DeepSeek-V3) with complementary production specialties
- Trade within constrained social network for utility
- Realistic simulation of self-interested agent economies

### Mechanism Comparison
- Eight conditions tested under progressive troll injection over 200 rounds
- Mediation identified as top-performing mechanism for market stability
- Systematic comparison of formal mechanisms layered on unrestricted communication

### Adversarial Robustness
- Red-teaming of Mediation using iteratively prompt-optimised LLM-driven trolls
- Best attack (v6) reduces honest-agent utility by 13.3% but cannot collapse market
- Mediation enables recovery even under sustained adversarial pressure
- Adversarial robustness defined as sustained positive honest-agent utility under attack

### Mediation: Bend but Not Break
- Mediation is robust: can be bent but not broken
- Maintains market stability under optimized adversarial attack
- Enables recovery after adversarial pressure

## Methodology

1. **Simulation Setup**: 18 LLM agents with complementary specialties in constrained network
2. **Mechanism Comparison**: Test 8 conditions under progressive troll injection (200 rounds)
3. **Adversarial Red-Teaming**: Iteratively prompt-optimise LLM trolls against Mediation
4. **Robustness Analysis**: Measure honest-agent utility under optimized attack
5. **Recovery Assessment**: Test Mediation's ability to recover after attacks

## Implications

- Formal mechanisms are essential for LLM agent societies to maintain cooperation
- Mediation is a practical and robust mechanism for market stability
- Adversarial robustness should be a core evaluation criterion for multi-agent mechanisms
- LLM-based multi-agent economics is a viable testbed for mechanism design

## Pitfalls

- DeepSeek-V3 specific results may not generalize to other LLMs
- 18 agents may not capture dynamics of larger economies
- Social network constraint affects trade dynamics
- Prompt-optimised trolls may not represent worst-case adversarial behavior

## Activation Keywords

market stability, self-interested agents, multi-agent economics, cooperation mechanisms, social dilemmas, Mediation, adversarial robustness, LLM agents, marketplace simulation, DeepSeek-V3

## Paper Reference

arXiv:2607.08652 - "Formal Mechanisms for Market Stability in Self-Interested Agent Societies" (Jul 2026)
