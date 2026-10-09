---
name: multi-agent-egocentric-world
description: 'Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction. Predicting first-person observations conditioned on multiple agents actions in shared environments.'
metadata:
  arxiv_id: "2610.12299"
  utility: 0.87
  authors: ["Dahyun Chung", "Siyoon Jin", "Hyunwook Choi", "Honggyu An", "Junyoung Seo"]
  published: "2026-10-08"
  categories: ["cs.CV", "cs.AI"]
  tags: ["world-model", "egocentric", "multi-agent", "embodied-interaction", "first-person-prediction"]
---

# Multi-Agent Egocentric World Model with Fine-Grained Embodied Interaction

**arXiv:** [2610.12299](https://arxiv.org/abs/2610.12299)
**Utility:** 0.87

## Key Innovation

Egocentric world models predicting first-person observations conditioned on **multiple agents' actions** in shared environments, with fine-grained embodied interactions.

## Problem

Most egocentric world models focus on single agents. Real embodied settings involve multiple agents acting and interacting. Existing multi-agent world models rely on coarse actions (locomotion, camera control, discrete commands), leaving fine-grained embodied interactions underexplored.

## Approach

- Model first-person observation prediction for multi-agent settings
- Support fine-grained action conditioning (not just locomotion)
- Capture inter-agent interaction dynamics

## Practical Use

- Build better multi-agent embodied AI systems
- Enable agents to predict and reason about other agents' actions
- Improve planning in shared physical environments
