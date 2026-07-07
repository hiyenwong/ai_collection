---
name: reasonmaxxer-entropy-gated-selection
description: RL-free reasoning improvement via entropy-gated contrastive selection. Based on arXiv 2605.06241 showing RL's benefit is sparse policy selection at high-entropy decision points, not capability learning.
category: llm-reasoning
---

# ReasonMaxxer: Entropy-Gated Sparse Policy Selection

## Overview
RL for LLM reasoning doesn't teach new capabilities — it performs **sparse policy selection** at high-entropy decision points. Only 1-3% of token positions are affected, promoted tokens are always within base model's top-5, and targeted corrections at these positions recover most of RL's accuracy gain.

## Core Methodology: ReasonMaxxer
1. **Rollout base model** on a few hundred problems (no online generation needed)
2. **Compute token-level entropy** at each decision point
3. **Identify high-entropy decision points** (where model is uncertain about next branch)
4. **Apply contrastive loss** only at these entropy-gated positions
5. **Train with minimal data** — tens of problems, minutes of single-GPU training

## Key Findings
- RL's beneficial footprint is sparse: only 1-3% of token positions affected
- Promoted tokens always in base model's top-5 alternatives
- Base model's own entropy identifies critical positions without RL-trained model
- Correction is low-dimensional, representable in tiny fraction of parameters
- ReasonMaxxer matches/exceeds full RL across 3 model families, 6 scales, 6 benchmarks
- Training cost reduced ~3 orders of magnitude vs full RL

## Implementation Steps
1. Generate base model rollouts on training problems
2. Compute per-token entropy distributions
3. Select top entropy-gated positions (high uncertainty decision points)
4. Apply contrastive loss at selected positions only
5. Fine-tune with minimal compute (tens of problems)

## Applicable Use Cases
- Improving math/reasoning capabilities without full RL pipeline
- Single-GPU reasoning improvement for small-to-medium models
- When RL compute budget is prohibitive
- When you have limited training problems (tens to hundreds)
- Complement to existing SFT before RL stage

## Triggers / Keywords
reasoning improvement, RL-free, entropy-gated, sparse policy selection, math reasoning, contrastive loss, token-level analysis
