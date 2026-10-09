---
name: cot-prefix-scoring-pitfall
version: v1.0.0
last_updated: 2026-09-26
description: "CoT-prefix scoring pitfall methodology — diagnosing how appended reasoning cues break logit-based answer readout in VLM multiple-choice evaluation, plus linear-probe/generation recovery diagnostics. Use when: (1) multiple-choice eval scores collapse after adding reasoning instructions, (2) designing logit-readout evaluation for reasoning models, (3) distinguishing model-knowledge failure from evaluation-interface mismatch. Keywords: CoT evaluation, answer decoding, logit readout, VLM evaluation, position bias, linear probe."
arxiv_id: "2609.29278"
authors: "Zeyan Li, Siyuan Qiu, Jianfeng Xu"
tags: [evaluation, chain-of-thought, vlm, logit-readout, position-bias, benchmark-design]
---

# CoT-Prefix Scoring Breaks Answer Decoding in VLMs

From arXiv:2609.29278 (2026-09-24).

## Problem

A widespread evaluation pattern is broken: appending a CoT cue (e.g., "Let's think step by step") but **reading answer-label logits before the model generates any rationale** — "CoT-prefix scoring."

**Magnitude**: Qwen2.5-VL-7B on ScienceQA drops **80.76% → 45.48%**; across 5 option-content permutations, **93.54% of predictions collapse onto the first slot** — a massive position artifact, not knowledge loss.

## Diagnosis Workflow

1. **Check it's interface, not knowledge**: condition-matched **linear probes** on the same hidden states recover 78.94%; **free generation** restores 75.24%. If probes recover the answer, the information is present — the readout failed.
2. **Vocabulary/layer diagnostics**: probability mass shifts toward continuation tokens (e.g., "step", "1.") while answer information remains linearly accessible in late layers. The mismatch is between what the scorer samples and what the prompt primes.
3. **Permutation test for position bias**: shuffle option contents across slots. A readout that follows the first slot (not content) is decoding the cue's continuation, not the answer.

## Prescriptions

- Never score answer-label logits immediately after a reasoning cue unless the **requested and scored output events are aligned** (i.e., score where the model is actually expected to emit the answer)
- Prefer: free generation + parse, or forced-answer tokens *after* generated rationale
- When a CoT-prompted model scores near chance, run the linear-probe recovery test before concluding it lacks the knowledge

## Reusable Pattern

**Align scored event with requested event.** Any logit-based readout is only valid at the token position where the model was actually asked to commit to an answer. Reasoning instructions move the model's distribution toward rationale-continuation tokens; early-slot logit readouts then measure continuation statistics (with first-slot artifacts), not knowledge. Applies to LLM-as-judge setups, MCQ harnesses, and any scorer that peeks at logits mid-prompt.

## Resources

- Paper: https://arxiv.org/abs/2609.29278
