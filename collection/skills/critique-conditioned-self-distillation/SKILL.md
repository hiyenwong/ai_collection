---
name: critique-conditioned-self-distillation
description: Critique-first localization for self-distillation signals.
category: ai_collection
---

# Critique-Conditioned Self-Distillation

Source: "A Privileged Teacher That Only Scores Cannot Search: Critique-Conditioned On-Policy Self-Distillation for Reasoning" (arXiv: 2610.13744, Maniparambil et al., 2026)

## Core Diagnosis (the reusable insight)

A privileged teacher conditioned on the reference solution, scoring the student's own rollout, produces signals (full-distribution KL, token log-ratio) that **neither localize errors nor push probability away from erroneous tokens**. The failure is structural: locating an error in a reasoning trace is itself a *search problem*, and a scoring pass is never asked to perform that search. The same model with the same privileged information localizes errors well **when allowed to generate a critique first** — generation performs the search, scoring converts the critique into a dense token-level signal.

## Method

1. **Critique generation**: critic reads (problem, reference, student rollout, rollout presented sentence-numbered) and writes critiques as pairs `{(q_j, ρ_j)}` — `q_j` is a **verbatim quote of an erroneous sentence**, `ρ_j` explains the error. Favor recall over precision.
2. **Critique-conditioned scoring**: replace the reference in the teacher's context with the critique; teacher scores the rollout with critique in context.
3. **Targeted application**: apply the corrective log-ratio with weight 3 **only on the quoted sentence and the 50 tokens after it** — not the whole rollout.
4. **Cost control**: critique only wrong rollouts in groups that contain ≥1 correct rollout (16–18 of 128 rollouts/step). Critique tokens ≈ 0.4% of rollout tokens, whole pass ≈ 6% of step time.

## Evaluation Protocol (error-span Z readout)

To test whether *any* privileged-context signal carries corrective credit:
- Get gold error spans from a grader model (verbatim quote + reason), double-judged by two independent models; only flags both accept count as gold.
- For each rollout, measure signal in a short window after the first gold error span vs length-matched windows after clean spans in the prefix: `Z = (s̄_err − mean(s̄_clean)) / std(s̄_clean)`. Log-transform window-mean KL before Z (heavy tail). Calibrate by subtracting Z from a random clean sentence treated as error.
- Control for "solution-shaped preamble" shifts with matched **placebo contexts** (reference from another problem / critique of another rollout) and report content signal = signal(b) − signal(b̃).

## Results

- Self-critique (student critiques its own rollouts) recovers most of the oracle-critic gain: 0.593 vs 0.606 OOD with RLCSD at 0.567 base; self-critique quote-match rate 82% vs 96% oracle.
- Critique term on top of GRPO: +5.5 OOD pts; on top of RLCSD: +3.9 more. Gains add.
- Test-time: resuming a wrong rollout with the critique in context converts math problems the model cannot solve by sampling. Cold-start GRPO: critique provides an advantage signal on prompts where verifiable rewards give none.

## Lessons

- Verify a distillation signal *at gold error spans* before building an objective on it — distributional shift at the error position, not aggregate KL, is the property that matters.
- A scoring pass cannot substitute for a search: any signal that requires locating a problem within a sequence needs a generation pass that performs the search.
- Restrict the corrective term to the critique-quoted span + short window, not the full trace; whole-rollout application dilutes the signal.
- The student can be its own critic — a weaker but sufficient critic keeps the loop closed-loop without external APIs.

## Activation

self-distillation error localization, privileged teacher scoring, on-policy distillation critique, GRPO cold-start advantage, reasoning rollout credit assignment
