---
name: lastopd-latent-onpolicy-distillation
version: v1.0.0
last_updated: 2026-09-26
description: "LastOPD methodology — fixing latent-alignment collapse in on-policy distillation by applying latent supervision only at the last-layer state with a short crossfade into token-level OPD. Use when: (1) student-teacher latent alignment in OPD degrades after early gains, (2) alignment metric improves but downstream performance collapses, (3) combining latent + token distillation signals. Keywords: on-policy distillation, latent collapse, reverse KL, LLM distillation, layer-mismatch."
arxiv_id: "2609.28845"
authors: "Jie Yang, Zhengyu Fang, Zelin Xu, Jiarui Sun, Xiran Fan et al."
tags: [distillation, on-policy, latent-alignment, llm-training, collapse-diagnosis]
---

# LastOPD: Taming Collapse in Latent On-Policy Distillation

From arXiv:2609.28845 (2026-09-23). Code: https://github.com/Muyiiiii/LastOPD

## Problem: Two Failure Modes of Latent OPD

On-policy distillation (OPD) supervises student-generated responses with the teacher's next-token distribution. Latent supervision (e.g., OPRD-style) additionally aligns student hidden states to teacher hidden states. Distilling Qwen3-4B/8B → Qwen3-1.7B-Base reveals:

1. **Early gain, late collapse**: latent supervision lifts MATH-500 from 25→46 in 10 steps, then degrades to 11 with no recovery.
2. **Better alignment, worse behavior**: the alignment metric keeps improving *throughout* the collapse — the most aligned model performs worst.

**Root cause**: layers paired by depth play different roles in teacher vs student. Same-depth alignment drags the student toward teacher states it *cannot represent*, and the alignment metric cannot see this incompatibility.

## Method: LastOPD

1. **Apply the latent signal only at the last-layer state** — the one interface both LM heads actually read. This sidesteps the same-depth layer-role mismatch entirely.
2. **Crossfade schedule**: run latent supervision only during a short ~10-step window, then hand over to token-level OPD. This harvests the early gains (where latent signal helps) and exits before collapse sets in.

## Results

- +5.55 / +4.02 MATH-500 points over token-only OPD (4B / 8B teachers)
- Leads on most held-out datasets; reaches token-only OPD's final score in ~half the steps

## Reusable Patterns

1. **Metric-behavior divergence as an alarm**: when your auxiliary alignment metric monotonically improves while end-task performance degrades, suspect the metric rewards an unrepresentable target. Do not trust proxy metrics through collapse regions.
2. **Align at shared interfaces, not structural mirrors**: when aligning two heterogeneous systems (student/teacher, model/model, brain/model), align at the *functional common interface* (here: the pre-LM-head state both models consume) rather than same-index internal layers whose roles diverge.
3. **Crossfade over hard mixing**: for two supervision signals where one helps early then harms, use an explicit short-window schedule that transfers from the fragile signal to the robust one, instead of fixed-weight combination.

## Resources

- Paper: https://arxiv.org/abs/2609.28845
- Code: https://github.com/Muyiiiii/LastOPD
