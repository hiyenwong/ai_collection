---
name: linear-probe-transfer-distilled-models
description: Use when auditing LLM successors with reused safety probes.
category: ai_collection
version: 1.0
author: hermes-dl-cron
license: MIT
trigger: linear probe reuse, safety auditing across releases, distilled model probing, safety direction rotation, XSTest, OR-Bench, activation classifier transfer
arxiv: "2610.35586"
---

# Linear Probes Transfer from Base to Distilled Language Models despite Rotation

arXiv 2610.35586.

## When to Use
Use when a safety/behavior auditor wants to reuse activation probes across model releases (distilled reasoning successors, instruction-tuned variants) instead of retraining per release — and when interpreting how fine-tuning moves internal safety representations.

## Protocol (reusable auditing recipe)
1. **Activations**: residual stream after one layer, averaged over the LAST 8 tokens of the prompt. Raw text, no chat template, no BOS — so base and successor see identical tokens.
2. **Probe**: logistic regression (C=1) on per-coordinate standardized activations; carry the base model's standardization stats over unchanged on transfer.
3. **Layer selection**: cross-validated mean-difference reader (project onto the safe-minus-unsafe mean-difference direction); chosen layers vary per family (Qwen2.5-Math-7B: 17–19; Llama-3.1-8B: 12–23; Qwen-14B: 27–45; Qwen-32B: ~43).
4. **Safety direction + rotation**: direction = mean unsafe activation − mean safe activation; rotation = angle between base and successor directions in the base's standardized coordinates.
5. **Text-only control**: TF-IDF / character-ngram logistic regression on prompt text (the no-activation baseline).
6. **Held-out evaluation**: 8 folds over prompt-type groups (each safe type grouped with its contrast — they share alarming words); independent OR-Bench set with bootstrap CIs.

## Findings
- **Transfer works**: four families (Qwen2.5-Math-7B, Llama-3.1-8B, Qwen2.5-14B, Qwen2.5-32B), successors = DeepSeek-R1-distilled reasoning + developer instruct models. Safety direction rotates 17°–35°, yet transferred-probe XSTest AUC changes only −0.011..+0.027 (base AUCs 0.878–0.931); independent OR-Bench: −0.015..+0.053.
- **Beats text-only by +0.15–0.20 AUC on XSTest** (safe prompts deliberately contain alarming words); margin shrinks to 0.03–0.20 on OR-Bench.
- **Caveat — probes read appearance of harm**: 29–42% of benign-but-alarming prompts get flagged; part of what probes encode is harmful-LOOKING content, not harm itself.
- **Geometric intuition**: probe score = projection along w; movement perpendicular to w is invisible. Successor tuning moves activations largely in probe-invisible ways despite rotating the safety direction.

## Reusable patterns
1. Probe reuse across fine-tuned successors within a family — train once on the base, deploy unchanged on distilled/instruct successors (validated to 32B, R1-distillation).
2. Last-8-token mean pooling of the residual stream — cheap, template-free activation summary that matches across variants.
3. Report rotation AND transferred AUC together — rotation alone overstates degradation; decision boundaries survive direction rotation.
4. Contrastive prompt groups sharing alarming words (XSTest style) separate activation-read signal from surface lexical signal.

## Related
Refusal-direction literature, activation steering, model-diff auditing, linear-representation hypothesis
