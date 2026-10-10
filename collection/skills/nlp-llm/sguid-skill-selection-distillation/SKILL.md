---
name: sguid-skill-selection-distillation
description: Use when selecting compact skill banks for model-skill co-evolution via on-policy distillation. Individual skill utility drives selection.
tags: [skill-distillation, model-skill-co-evolution, on-policy, skill-selection, compact-skill-bank]
---

# SGUID: Selecting Skills for Distillation

## Paper Metadata

- **arXiv ID**: 2610.12367
- **Authors**: arXiv authors
- **Categories**: cs.CL, cs.LG
- **Utility Score**: 0.88
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12367

## Key Contributions

- Formalizes skill selection as a pre-distillation step: choosing a compact, high-utility skill bank before on-policy distillation
- Demonstrates that individual skill utility (not just aggregate coverage) matters for distillation efficiency
- Shows skill selection improves distillation efficiency — fewer skills yield better or comparable performance
- Provides a framework for model-skill co-evolution where skill bank composition adapts to model capabilities

## Core Methodology

SGUID addresses the problem of distilling a large skill set into a smaller model. Rather than distilling all skills uniformly, it first selects a compact subset based on individual skill utility scores. The selection process considers how much each skill contributes to the student model's capabilities given its current capacity.

The core insight is that on-policy distillation (where the student generates its own trajectories) interacts with skill selection differently than off-policy approaches. Skills that are individually useful may not all be simultaneously distillable — the method identifies which skills the student can actually learn given its architecture and capacity constraints.

This creates a model-skill co-evolution loop: the skill bank is pruned based on what the model can effectively learn, and the model is trained on the selected subset. The result is a more efficient distillation pipeline that avoids wasting capacity on skills the student cannot internalize.

## Relevance to nlp-llm

Directly relevant to LLM efficiency: shows how to compress skill capabilities into smaller models through principled selection rather than brute-force distillation of all available skills.

## Activation

skill-distillation, model-skill-co-evolution, on-policy, skill-selection, compact-skill-bank
