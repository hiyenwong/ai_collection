---
name: rshd-grounding-hindsight-distillation
description: Use when GRPO all-fail groups waste rollouts.
---

# RSHD: Replay-Selected Hindsight Distillation

Source: arXiv:2610.21018 (Yu, Yu, Kuang, Chu, Tang, Kim, Yao, McAuley, Wu — "Failure Is the Mother of Success: Recovering Supervision with Grounding Hindsight", 14 Oct 2026, v2)

## Activation
- all-fail GRPO group, zero advantage, failure-conditioned exploration, hindsight note, self-distillation from failures, note admission test, repair basin, GRPO signal starvation, distill failure lessons

## Problem
Two failure modes of GRPO-style group training:
1. **All-fail group**: Pr(E_fail|x) = (1−p0)^n — every group-relative advantage is zero, the task-reward part of the clipped GRPO surrogate has ZERO gradient (Lemma 2). The model learns nothing from exactly the problems it most needs to learn.
2. **Local repair ceiling**: a failed trajectory may sit in a "repair basin" B(y−) — a strategy that cannot succeed within the remaining budget. Repair kernels with escape bound ε succeed within m retries with probability ≤ 1−(1−ε)^m ≤ mε; strategy-preserving repair has ε=0 and can NEVER succeed (Prop. 4). Restarting with failure-derived context is the only way to reach a different strategy.

## Method: RSHD (Replay-Selected Hindsight Distillation)

**Stage 1 — explore and select (per failed rollout y):**
1. Model writes a note s = write_note(x, y) — a structured lesson diagnosing the failure. Writer sees NEITHER the reference answer nor any solution.
2. Screen (no sampling cost): ok(s) = 1 iff s parses AND does not state the reference answer (string match of normalized g against note text = leak check).
3. **Admission test by replay**: sample k replays from π(·|x⊕s) (prompt + note); admit iff r̂(s) = mean R over replays > p̂ (original group's success rate). A note helps exactly when p_s > p_0; both unobservable, so estimated by replay.
4. One revision round: if not admitted, writer sees its note, the replay tally, and excerpts of ≤3 failed replays (still no reference), revises; re-screen + re-test; second failure ends the search.
5. For admitted note i: target ỹ_i ~ Unif{admitted replays} — whether or not it succeeded.

**Stage 2 — policy update:**
- loss = grpo_loss(ys) — UNCHANGED original GRPO loss, plus auxiliary term:
- For each kept (s, y_t): same model scored twice — l_t = logπ(y_t | x+s).detach(), l_s = logπ(y_t | x); per-token lift w = clip(l_t − l_s, 0, c).detach() (c = weight cap);
- num += Σ(w · l_s); ntok counts all tokens (w=0 included). Aux loss = λ · num/ntok (λ=0.2, c=2, k=2 replays, 2 note rounds, no KL penalty).
- Intuition: imitate the note-conditioned continuation **in proportion to the note's measured lift** — tokens where the note helped most get the strongest distillation signal.

**Admission guarantees enrichment, not purity**: for an all-fail group, admission needs ≥1 of k replays to succeed; a uniformly-drawn admitted replay is correct with probability p_s/(1−(1−p_s)^k) ≥ p_s — more likely correct than a fresh sample, never guaranteed. Leak screen runs BEFORE admission because an answer-revealing note would pass the test trivially.

## Results (Qwen3-1.7B/4B/8B; MATH + MMLU-Pro/GPQA/TheoremQA science; 150 steps × 14 problems × 8 rollouts)
- Qwen3-4B MATH-500: **RSHD 84.5 vs GRPO 76.9** (+7.6); OPSD 73.6, SEED 75.2 — both alternative distillation baselines UNDERPERFORM plain GRPO here.
- Qwen3-4B science: MMLU-Pro 61.2 vs 48.7 (GRPO); GPQA-Diamond 9.1/27.0 vs 3.0/9.6; TheoremQA 56.5 vs 40.1.
- Gain concentrates exactly where the method is built to work: on MATH difficulty Levels the margin rises monotonically to +10.8 pts on 134 Level-5 problems (indistinguishable at Level 1, 94.5 both).
- **Gemma-4-E4B never-solves split (0/8 samples)**: RSHD +8.5 pts (6.4→15.0) on 66 never-solved problems; −0.4 on 172 sometimes-solved — ALL of the gain sits on problems the policy cannot solve at all. Cleanest evidence that manufactured failure-signal drives the gain.
- In the math run, one note in NINE states the answer — the leak screen is not optional.
- Controlled 2-strategy task: unguided retry ≈ no learning; repair-biased restart (ε=0.1) slow; strategy-switch note reaches success — matches Prop. 4's escape-bound analysis.

## When to Use
- Frontier/hard-problem training where all-fail groups are common (the +8.5 on never-solved problems).
- Any GRPO pipeline where difficulty-adjusted sampling leaves many zero-gradient groups.
- NOT needed if p̂ is high across the curriculum — the aux term adds k replays per failed rollout.

## Implementation Notes
- Cost accounting: k=2 replays per failed rollout × 2 note rounds — bounded overhead, only paid on failures; skip groups the policy solves every time.
- Note admission threshold compares against the ORIGINAL group mean p̂, not zero — a note must beat the group, not merely succeed once.
- Treat mixed-fail and all-fail groups alike (failures processed the same way).
- Baselines OPSD (re-score rollouts under reference solution) and SEED (untested self-note) both underperform plain GRPO on these benchmarks — untested notes can actively hurt; the replay test is the load-bearing component.

## Related skills
- Contrasts with [[rc-opd-root-cause-repaired-distillation]] (repairs the student's own reasoning, no note mechanism). Complements [[hindsight-privileged-rlvr]] (same all-same-reward problem, different fix: JSD weights vs distillation). See also [[search-e1-self-distillation]], [[self-policy-distillation-spd]].