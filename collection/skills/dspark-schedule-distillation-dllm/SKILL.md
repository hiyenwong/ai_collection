---
name: dspark-schedule-distillation-dllm
description: Use when diffusion LMs decode too slowly in parallel.
category: ai_collection
trigger: dLLM parallel decoding, diffusion language model, unmasking schedule, tokens per forward, LLaDA, Dream, schedule distillation
arxiv: "2610.35804"
---

# dSpark — Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models

arXiv 2610.35804 (VILA-Lab). Code: https://github.com/VILA-Lab/dSpark

## Problem
Diffusion LMs (LLaDA, Dream) generate tokens in parallel but need many decoding rounds. Confidence-based unmasking commits the most predictable tokens first — but a highly predictable token often provides little context for other positions, while revealing a *less* predictable token can make several other positions predictable sooner. Efficient decoding depends on **when** to commit, not just **which** tokens are easy.

## Method

### 1. Uncertainty-area objective
Per-position surprisal under frozen teacher p0: h_j(s) = −log p0(y_j | s, j).
Remaining uncertainty at round r: H(s_r; y) = Σ_{j∈M_r} h_j(s_r).
Schedule quality: A(π; y) = Σ_{r=0}^{T−1} H(s_r; y). Promoting tokens that help others shifts the uncertainty curve left → same response, fewer rounds.

### 2. Uncertainty-guided schedule construction (offline, frozen teacher)
For a fixed CORRECT response y (base model's own correct generations):
- Candidate set: C_r = {i ∈ M_r : p0(y_i|s_r,i) ≥ p_min AND rank0(y_i|s_r,i) ≤ k}  (p_min=0.02, k=10)
- Reveal score: i* = argmax_{i∈C_r} Σ_{j∈M_r∖{i}} [h_j(s_r) − h_j(s_r^(i))] — reduction of surprisal at OTHER masked positions when i is revealed
- Promote argmax only if the score is positive; else follow natural (confidence) order
- Repeat → optimized trajectory τ*(y)

### 3. Schedule distillation (student training, LoRA)
Positive trajectories (correct responses):
- L+ = E[CE(s*_r, y) + sharp(s*_r, y)]
- CE: cross-entropy on masked positions given promoted states
- sharp: minimize predictive entropy H(p(·|s*_r, j)) on positions where the student is already correct (confidence sharpening → earlier commitment)
Negative trajectories (failed responses):
- L− = E[KL(p0(·|s−,j) ‖ p(·|s−,j))] — anchor to frozen base model where token-level supervision is unavailable
Full objective: L = L+ + β·L− (β=1).

### Training data
Correct + incorrect base-model generations on reasoning corpora (GSM8K, PRM12K, NuminaMath-CoT, AceCode; ≤256 tokens, block 32). Subsample incorrect to 4:1 correct:incorrect. LLaDA: 52k/13k; Dream: 80k/20k. Multi-block decoding at inference; metrics: TPF (tokens per forward), AUP (accuracy under parallelism).

## Results
- LLaDA-8B-Instruct GSM8K: 10.12× TPF at 78.9% acc (base 78.8%); AUP 761.7 vs 571.3 (d3LLM)
- Dream-7B-Instruct GSM8K: 5.12× TPF, acc +1.5 over base
- Calibration: confident predictions correct 91% (vs 82% for dParallel/d3LLM, which are overconfident in every bin)
- Ablation: schedule alone raises TPF but drops acc; KL alone raises acc but lowers TPF; combination wins AUP

## Reusable patterns
1. Reveal scoring for masked models — score a candidate token by uncertainty reduction at other positions, not its own confidence. Generalizes to any iterative-reveal model.
2. Trajectory-order distillation — change only the ORDER of reveals on fixed responses, train on intermediate states; shapes decoding behavior without rewards or new rollouts.
3. Asymmetric positive/negative supervision — CE+sharpening on successes, KL-anchor to frozen teacher on failures; prevents confidence corruption off-distribution.

## Related
dParallel, d3LLM, D2F, Fast-dLLM (confidence-based parallel decoding); on-policy dLLM distillation skills (on-policy-distillation-dlm-transformation) cover training-time distillation — dSpark targets inference-time unmasking order.
