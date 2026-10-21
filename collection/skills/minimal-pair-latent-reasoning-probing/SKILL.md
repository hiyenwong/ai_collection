---
name: minimal-pair-latent-reasoning-probing
description: "Use when auditing claims that a model 'reasons latently' (values present but unwritten). Minimal-pair probing protocol: shared-code readout across prompts, synthetic mixing nulls, and causal patching to separate present vs readable vs used."
category: ai_collection
metadata:
  arxiv_id: "2610.28498"
---

# Minimal-Pair Probing of Latent Reasoning: Present vs Readable vs Used

Source: arXiv:2610.28498 (Shalev Merin, Oct 2026). Probing studies of latent reasoning often read a model's state where the answer begins and take a **failed probe as evidence that a value is absent**. This paper shows that inference is invalid, using a digit copied from the question in the looped model Ouro-1.4B and the standard transformer Qwen2.5-1.5B.

## Core findings

1. **Present, shared code**: comparing prompts that differ only in one digit (minimal pairs), the value is present at the last prompt token in a code shared across questions — cross-question readout ≈ 0.9.
2. **Unreadable per-prompt**: a probe seeing one prompt at a time (the usual setting) barely reads it — 0.36 in Ouro, 0.19 in Qwen even after 5,249 training questions.
3. **Small, not crowded**: the digit's change is small along a specific direction rather than drowned in noise — random noise lands on equally busy directions, while a random word in its place moves the state far more and *is* readable.
4. **Successful probes are ambiguous too**: every varied token leaves a trace, so finding *some* readable signal does not show the value is computed or used.
5. **Pre-registered two-step study**: small signal for the unwritten intermediate a+b just before Ouro writes the answer's last digit; its sign follows the operation — but **mixing alone produces much of the sign-following part** (the synthetic null matters).
6. **Readable but not used**: patching the a+b value to another problem's from the first loop on does **not** move the written digit toward the other problem; patching the answer's own representation does.

## Protocol (reusable)

1. Build **minimal pairs** — prompts differing in exactly one input value; train readout **across prompts on shared code** vs per-prompt.
2. Run a **synthetic null for generic mixing** (e.g., linear/attention mixing of input traces) before attributing signal to computation.
3. Distinguish three claims explicitly: **present** (in state), **readable** (linearly decodable in the usual probing setting), **used** (causally affects output).
4. Test *used* by **activation patching** the candidate value to a different problem's value; if output doesn't follow, the value is not consumed by the computation.

## Use when

- Auditing latent/CoT-free reasoning claims (looped models, recurrent transformers, diffusion LMs).
- Reviewing interpretability papers that infer absence from probe failure (the paper shows why that fails).
- Designing probing studies that need pre-registration and nulls to be credible.

Related: CoT-prefix scoring pitfalls, probe-trajectory monitoring of reasoning models, activation patching methodology, LLM readout interference bottlenecks.
