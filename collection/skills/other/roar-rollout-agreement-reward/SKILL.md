---
name: roar-rollout-agreement-reward
description: "Use when correct GRPO traces hide spurious reasoning."
category: reinforcement-learning
---

# RoAR: Rollout-Agreement Reward for Group-Based Policy Optimization

Source: arXiv:2610.34951 (Sohyun Son, Yerim Hong, Jaeyun Park, Mujeen Sung — Kyung Hee University, Oct 2026). Blind paired analysis shows low-agreement verified-correct traces carry 35% spurious reasoning vs 22% for high-agreement; RoAR adds an agreement bonus gated to verified-correct rollouts. 1.5B avg pass@1 49.5 -> 55.5 on 7K training examples (+6.0 over GRPO, +5.5 over GRPO-CARE); blind audit spurious rate 32% -> 18%; same wall-clock as outcome-only GRPO (LLM-judge baseline: 2x time + $42.97 judge cost). Code: github.com/ldi-kyunghee/RoAR.

Use when: GRPO groups contain multiple correct-but-flawed traces, you want process-style rewards without a trained PRM or extra sampling, or you are auditing reasoning validity beyond final-answer correctness.

## Diagnostic: what differences among correct rollouts mean
Final-answer verification leaves reasoning validity open — a correct answer can follow from unsound intermediate steps. Blind paired analysis on a GRPO-trained DeepSeek-R1-Distill-Qwen-1.5B (K=32 rollouts/problem, MinervaBench, 126 highest- vs lowest-agreement verified-correct pairs, agreement labels hidden): low-agreement traces have higher spurious rate (35% vs 22%) and lower valid rate (31% vs 47%). Largest error-rate gaps (lowest minus highest agreement): internal inconsistency +21.4pp, wrong operation/formula +9.5, wrong evidence/condition +7.1. Divergence from peer traces is therefore associated with unresolved errors even when the final answer is correct.

## Method
1. Agreement score (Eq. 1-2): pairwise trace similarity s(i,j) = alpha*s_sem(i,j) + (1-alpha)*s_lex(i,j) — cosine similarity between reasoning-trace embeddings + token-level F1 (alpha = 0.5); per-rollout agreement a_i_all = (1/(K-1)) * sum_j s(i,j) over the FULL on-policy rollout group (not just correct ones).
2. Correctness gating (Eq. 3): r_ROAR(y_i) = I_correct(y_i) * a_i_all — the bonus goes ONLY to verified-correct rollouts; an incorrect-but-similar trace receives nothing (similarity can be high among wrong answers too).
3. GRPO integration (Eq. 4): r_i = w_fmt*r_fmt + w_acc*r_acc + w_ROAR*r_ROAR (w_ROAR = 1.0), then the standard group-relative advantage and GRPO update. No human rationales, no additional sampling, no separately trained process evaluator; computed entirely from existing rollout groups.

## Evidence
- 1.5B (Open-RS 7K training set, zero-shot pass@1): mean 55.5 across AIME26 / MATH-500 / AMC23 / Minerva / OlympiadBench vs GRPO 49.5, GRPO-CARE 50.1, GRPO w/ LLM-judge 51.8, DRA-GRPO 54.0, OpenRS 52.3, base 47.1 (+8.4 over base); best on AMC23 80.0 and OlympiadBench 55.3. Paired bootstrap 95% CIs for gains over GRPO/CARE: [1.6, 10.6] / [0.9, 10.0] points.
- Pass@4 macro-average: ROAR 68.3 vs GRPO 66.2 (+2.1) while diversity-reward methods drop consensus: GRPO-CARE 65.1 (-1.1), DRA-GRPO 63.7 (-2.5).
- 3 training seeds (0/7/2025) x {1.5B, 4B Qwen3-4B}: +1.7 and +1.4 avg pass@1; 4B AIME26 61.1 -> 66.7 (+5.6).
- Blind audit of 100 problems answered correctly by ALL four 1.5B models: spurious 18% (GRPO-ROAR) vs 32% (GRPO), 27% (GRPO-CARE), 37% (DRA-GRPO). 4B audit agrees.
- Ablations: full-group references + correctness-gated reward is the winning combination — correct-only references drop to 52.2 (sparse/absent correct rollouts make the score ill-defined); rewarding all rollouts drops to 51.9 (reinforces majority errors).
- Cost: ~same wall-clock as outcome-only GRPO (11h16m vs LLM-judge 21h58m + $42.97).

## Reuse pattern
Zero-infrastructure process reward for any GRPO-style RLVR: reuse the already-sampled group as its own reference set; reward agreement only among verified-correct rollouts. Works whenever a group has >= 2 correct responses; degrades gracefully to zero bonus otherwise. Caution: this selects for consensus — it suppresses legitimately divergent valid solutions (the paper's own comparison shows diversity-reward methods lose pass@4); pair with diversity-preserving components if exploration matters, and watch stylistic homogenization.

## 激活关键词
- rollout agreement / consensus reward (rollout 一致性奖励)
- spurious reasoning, internal inconsistency, correct-but-flawed traces (伪推理/正确但推理错误)
- GRPO reward design, process reward without PRM
- trace similarity: semantic embedding cosine + token F1
- verified-correct gating, agreement bonus (正确性门控一致性奖励)

Related: elitereplay-quality-diversity-replay-grpo (the diversity-side counterpart), wrong-votes-right-gradients-majority-vote-rl (bad gradients from flawed votes), hindsight-privileged-rlvr and rshd-grounding-hindsight-distillation (alternative advantage corrections), cleanrm-ot-noise-corrected-reward-modeling (reward noise), dars-predicate-dependency-reward-shaping (step-level shaping alternative).