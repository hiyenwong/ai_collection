---
name: ase-activation-space-exploration-rlvr
description: "Use when RLVR rollouts revisit the same reasoning paths."
category: reinforcement-learning
---

# ASE: Exploration via Activation-Space Steering for RLVR

Source: arXiv:2610.27012 (Zeng, Jing, Cheng, Wang — Fudan / CUHK-Shenzhen / Kunlun / Tsinghua, Oct 2026). Online rollout diversification by steering hidden activations along clustered correct-vs-incorrect contrast directions. +4.87pp (Qwen3-1.7B) / +1.87pp (8B) Mean@8 over GRPO on 6 math benchmarks at the same rollout budget; evaluation and deployment are steering-free.

Use when: RLVR exploration collapses to similar reasoning paths, zero-variance groups waste rollouts, temperature or data-level heuristics are not enough, or you want training-time-only steering interventions.

## Problem
The policy learns only from behaviors that appear in its rollouts. More rollouts = more Monte Carlo samples from the SAME proposal distribution; as probability mass concentrates, samples revisit similar solution modes, reproduce the same intermediate steps, and make correlated errors. Existing fixes change WHERE the budget goes (adaptive sampling, curricula, filtering) or token-level randomness (temperature), or replay old trajectories — none uses the model's internal representations to propose genuinely different reasoning.

## Method (ASE-GRPO)
1. Within-problem positive-negative pairing: only groups containing BOTH reward types contribute; pair n_pair = min(|P|, |N|) correct/incorrect trajectories of the same problem (controls for problem content and difficulty).
2. Activation readout: replay each selected full prompt-response with the current actor WITHOUT steering; take h = phi_{l,p}(x, y) at Transformer block l under position rule p; raw contrast d = h+ - h-.
3. Difference clustering (NOT one mean direction): accumulate pairs in a buffer; fit PCA on the pooled positive+negative activations; cluster the projected differences delta = Qh+ - Qh- with K-means into K clusters; each direction is the within-cluster mean difference in the ORIGINAL hidden space u_k = mean_{b in C_k}(h+ - h-). Diverse patterns (early strategy choice vs step sequencing vs late checking) stay separate; no semantic interpretation is assumed.
4. Cross-iteration stabilization: Hungarian-match new candidate directions to the existing bank by max sum cos(u_k^t, u_{P(k)}); EMA u^{t+1} = beta*u^t + (1-beta)*u_{P(k)}; L2-normalize into the bank V = {v_k}. The new bank is staged until actor optimization and rollout weight synchronization finish; update when buffer >= B_min and interval >= Delta.
5. Routed steering: per problem, split the rollout group uniformly across K+1 routes (s_i = 0 clean, 1..K steered); intervention h^l -> h^l + alpha*v_{s_i} on EVERY forward pass of the target layer (prefill + decode), executed by the rollout engine with frozen actor, OUTSIDE backprop; token sampling stays stochastic within each route. Defaults K = 3, alpha = 0.5, beta = 0.5. If the bank is empty the rollout distribution reduces to plain GRPO.
6. Off-policy-corrected GRPO: group advantage A_i = (r_i - mu)/(sigma + eps); token ratio rho vs theta^(t); truncated importance weight w_{i,tau} = min(c_IS, pi_{theta^(t)}(y_tau) / pi_tilde_steered(y_tau)) computed per position — steered rollouts are off-policy proposals and MUST be reweighted; loss L(theta) = -E_{x,i,tau}[ w * min(rho*A, clip(rho, 1-eps, 1+eps)*A) ].
7. Loop: structured exploration -> verifier outcome -> policy update -> vector-bank update. Evaluation and deployment disable steering entirely, so checkpoints are intervention-free.

## Why it works
Steering creates MULTIPLE proposal distributions instead of one; GRPO then raises the probability of useful steered behaviors under the BASE policy, making exploration gains persistent without deployment-time intervention. Within-problem contrasts isolate outcome-associated directions while removing problem-content variance (same prompt, same readout rule).

## Evidence
Qwen3-1.7B-Base / Qwen3-8B-Base on DAPO-Math-17k, same rollout budget as GRPO (8 rollouts/problem, no KL loss, no entropy regularization, verl + vLLM, 4/8 A800): 1.7B +4.87pp average Mean@8 over GRPO across MATH500, Minerva, AIME24, AIME25, AMC24, OlympiadBench; 8B +1.87pp; beats DAPO (+6.06 math avg at 8B), Dr.GRPO, GSPO, RePO; transfers OOD (MMLU-Pro, GPQA-Diamond, BBH).

## Reuse pattern
Any RLVR setup with verifier scores already generates within-prompt correct/incorrect pairs: harvest their activation contrasts, cluster them into a small bank of exploration directions, route a fraction of each group's rollouts through each direction with an off-policy IS correction in the loss, and keep a clean route. Generalizes to: diversity rescue for pass@k collapse, zero-variance-group rescue (mixed steered groups restore reward variance), and any setting where the proposal distribution — not the budget — is the bottleneck.

Related: EliteReplay (diversity preservation via replay), entropy-guided exploration, GSPO / DAPO / RePO baselines, activation steering (Beaglehole et al.); complements two-clocks (budget allocation).
