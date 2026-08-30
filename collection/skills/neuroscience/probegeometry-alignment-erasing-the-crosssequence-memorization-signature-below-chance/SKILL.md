# Probe-Geometry Alignment: Erasing the Cross-Sequence Memorization Signature Below Chance

**arXiv ID:** 2605.01699
**Authors:** Anamika Paul Rupa, Anietie Andy
**Published:** 2026-05-03T03:44:15Z
**Abstract:**
Recent attacks show that behavioural unlearning of large language models leaves internal traces recoverable by adversarial probes. We characterise where this retention lives and show it can be surgically removed without measurable capability cost. Our central protocol is a leave-one-out cross-sequence probe that tests whether a memorisation signature generalises across held-out sequences. The signature is real and consistent across scale: memorisation-specific gaps of +0.32, +0.19, +0.30 on Pythia-70M, GPT-2 medium, and Mistral-7B; on Pythia-70M, the random-initialisation control collapses to -0.04 at the deepest layer where the pretrained signature peaks. The probe direction is causally separable from recall -- projecting it out collapses the signature locally (+0.44 -> -0.19) while behavioural recall barely changes -- and a probe trained on naturally memorised content does not classify fine-tuning-injected secrets, marking two representationally distinct regimes. We then introduce probe-geometry alignment (PGA), a surgical erasure that aligns activations along the probe's live readout direction at each depth. PGA drives the cross-sequence probe below random chance at all four scales tested (toy depth-4: 0.17; Pythia-70M: 0.07; Mistral-7B: 0.45; GPT-2 medium: 0.06 via MD-PGA k=2) and remains robust to six adversarial probe variants. Against a re-fitting attacker who trains a fresh probe on PGA-treated activations, we extend PGA adversarially, defeating the re-fit probe at every memorisation-relevant depth while preserving five zero-shot capability benchmarks within 2.8 percentage points per task (mean Δacc = +0.2pp). The cross-sequence signature is a real, causally separable, regime-specific property of pretrained representations -- removable below chance with a single rank-one intervention per depth at no measurable capability cost.

## Skill Description

This skill is generated from the arXiv paper: Probe-Geometry Alignment: Erasing the Cross-Sequence Memorization Signature Below Chance (2605.01699).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2605.01699](http://arxiv.org/abs/2605.01699v3)
