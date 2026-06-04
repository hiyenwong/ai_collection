---
name: skill-rm-unifying-reward-modeling
description: "Skill Reward Model (Skill-RM) framework for unified reward modeling in RL pipelines. Treats reward computation as structured agentic task orchestrating heterogeneous evaluation criteria."
---

# Skill-RM: Unified Reward Modeling via Agent Skill

## Core Concept
Reformulate reward modeling as execution of reusable **Reward-Evaluation Skill**. Instead of static evaluation, treat reward computation as structured agentic task that dynamically selects and aggregates evidence.

## Key Innovation
- **Unified interface**: rule-based verifiers, ground-truth references, procedural checklists, complex rubrics
- **Dynamic orchestration**: Select evidence tailored to each input's requirements
- **Transparency & consistency**: Beyond static evaluation, structured task execution

## Implementation
1. **Reward-Evaluation Skill**: Reusable skill module for reward computation
2. **Evidence aggregation**: Dynamic selection based on input requirements
3. **Integration**: RL pipelines, RFT, best-of-N selection

## Applications
- RLHF pipelines
- Reinforced fine-tuning (RFT)
- Best-of-N selection
- Reward benchmarks

## Results
Consistently outperforms traditional judge baselines on reward benchmarks and downstream RL applications.

## Source
- arXiv: 2606.03980
- Title: Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill
- Authors: Tao Chen, Gangwei Jiang, et al. (Qwen team)
- Code: https://github.com/Qwen-Applications/Skill-RM

## Activation Keywords
skill-rm, reward modeling, heterogeneous evaluation, RLHF reward, reward orchestration, agentic reward