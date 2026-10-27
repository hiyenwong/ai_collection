---
name: entropy-drift-sign-law-sampler-mismatch-rlvr
description: "Use when RLVR entropy drifts under truncated sampling."
category: reinforcement-learning
---

# A Sign Law for Entropy Drift under Sampler Mismatch in RLVR

Source: arXiv:2610.34044 (Zhiyuan Wang, Jacob Steeves, Chang Liu, Oct 2026). Entropy in RLVR moves up or down on choices that should be neutral (mask vs. fail over-length responses); traced to sampler mismatch and captured by a first-order sign law plus one batch statistic, the token-weighted net advantage. On a 9B reasoning model, zeroing the net advantage gains +8.2 held-out points and learner renormalization +8.8 over the uncorrected rule, with no effect under exact sampling.

Use when: diagnosing RLVR entropy collapse or explosion, choosing mask-vs-fail handling for over-length responses, deciding sampler/learner consistency, or auditing entropy regularization recipes.

## Problem
Policy entropy is the watched health signal in RLVR, and it fails in both directions (collapse kills exploration; explosion degrades responses). Yet its direction hinges on seemingly neutral choices: masking over-length responses drives entropy DOWN, counting them as failures drives it UP, and with exact sampling the two runs are indistinguishable. On-policy theory (entropy drift = covariance of advantage with log-probability; baseline invariance) predicts no difference — the asymmetry comes from sampler mismatch: rollouts are drawn with top-k/top-p/min-p truncation or a temperature the learner does not apply, while the learner differentiates the full-support softmax at T=1.

## Key insight
Under sampler mismatch a constant advantage shift is no longer entropy-neutral. One gradient step of size eta on advantage A at a prefix changes entropy by dH = -eta*A*Phi(a) + O(eta^2), where Phi(a) := u_a - E_pi[u] and u_v := pi_v*(log pi_v + H). Under exact sampling E_pi[Phi] = 0 (classical baseline invariance). Under a sampler mu the same constant shift c gives E_mu[dH] = -eta*c*delta(mu) + O(eta^2), with the sharpness gap delta(mu) := E_mu[u] - E_pi[u] — a pull toward the sampler (Eq. 2: E_y~mu[c*grad log pi] = -c*grad KL(mu||pi)).

## The sign law (Theorem 1)
A sampler mu is SHARPER than pi if mu_u/pi_u >= mu_v/pi_v whenever pi_u > pi_v (monotone likelihood ratio). Theorem: any sharper sampler — top-k, top-p, min-p, their sequential composition, temperature T < 1, T<=1-then-truncation — has delta(mu) > 0; any flatter sampler — T > 1, mixing with uniform — has delta(mu) < 0 (T>1-then-truncation is neither; sign depends on pi). Hence a positive constant shift lowers entropy at first order under sharper samplers and raises it under flatter ones. Proof core: for a truncation to set S, delta = pi(S^c)*(E_pi[u|S] - E_pi[u|S^c]) > 0 by nested level-set comparison against {v: pi_v >= e^-H}; a sharper sampler is a mixture of truncations over level sets of mu/pi, and delta is linear in mu.

## The batch statistic (Definition 2 + Proposition 1)
Group-based RLVR with token weights omega_i (set by the aggregation rule) and a group baseline applies, to each group g, its token-weighted net advantage N_g = sum_i omega_i*L_i*A_i / W_g, W_g = sum_i omega_i*L_i. The first-order total entropy change over visited prefixes decomposes as dH_tot = D_net + D_cov + D_on:
- D_net = -eta * sum_g W_g*N_g*delta_bar_g / sum_g W_g — the only baseline-controlled part; under a sharper sampler each group pushes with the sign of -N_g.
- D_cov = -eta * sum_g W_g*Cov_g(A, delta_bar) — covariance between advantages and the sharpness gap; failed responses visit less confident prefixes (larger gaps), so in practice it raises entropy, though its sign is not fixed in general. Both mismatch terms scale with the gap, and the gap grows as the policy drifts away from a sharper sampler (fixed-size top-k keeps it growing): a self-accelerating loop. On real 9B batches D_net carries 66-78% of the mismatch drift under FAIL/PEN.
- D_on — the on-policy covariance between advantages and token probabilities (Cui et al.); vanishes under exact sampling.
Under a group-mean baseline, N_g = Cov_g(r, L)/L_bar_g. MASK (overlong filtering: zero reward, exclude from loss AND baseline) makes N positive in their runs -> entropy down; FAIL (train on them: long responses fail more, negative advantages with the largest L) makes N negative -> entropy up. That single statistic explains the Figure-1 asymmetry.

## Corrections (Proposition 2) — what each removes
1. Net-zero advantages (NZ): a length-weighted baseline (OPO-style) sets every N_g = 0 — removes D_net only; the gap covariance remains and can still start the runaway.
2. Gap-weighted baseline (GAPW): b_g = sum_i omega_i*L_i*delta_bar_i*r_i / sum_i omega_i*L_i*delta_bar_i makes the two mismatch terms cancel (D_net + D_cov = 0) without changing the learner; since delta_bar_i >= 0 under a sharper sampler, b_g is a weighted group reward mean.
3. Support renormalization = score centering: learner renormalizes over the sampled support, log pi_S(y) = log pi(y) - log pi(S); its gradient is the centered score (Marek & Ryabinin 2026), the learner's distribution equals mu, and BOTH mismatch terms vanish.
4. Token-level importance ratios only rescale the drift (exact ratio pi/mu = pi(S) on S): they leave ~98% of it — they are not a fix. Applying the sampling temperature to the learner shrinks the drift to 2-4%.

## Evidence
- 2B model: entropy slope linear in shifts of N under truncated sampling; indistinguishable from flat under exact sampling; token-level importance ratios leave 98% of the drift; the mask-vs-fail gap grows with measured sampler sharpness across six samplers and reverses sign at temperature 1.2.
- 100-step runs: the net-zero baseline only delays an entropy explosion that exact sampling never shows; a fixed positive shift delays it further; the gap-weighted baseline keeps entropy stable without changing the learner.
- 9B reasoning model, ten steps, truncated sampling: the uncorrected rule loses held-out accuracy; zeroing N gains +8.2 points and renormalizing the learner +8.8 (95% intervals 4.2-12.1 / over training seeds); no held-out effect under exact sampling. Replicated on OLMo-3-7B. Includes a survey of practice: vLLM-style sequential truncation is the norm; recent systems (DeepSeek-AI, torchtitan, Xiaomi LLM-Core, Cognition) remove the mismatch by replaying the sampling mask or centering the score.

## Reuse pattern
Any group-based RLVR/GRPO pipeline: (1) log the token-weighted net advantage N per batch — it predicts the sign of the baseline-controlled entropy drift before you see it; (2) treat mask-vs-fail of over-length responses as an entropy-control decision, not a neutral implementation detail; (3) if you cannot sample exactly, either renormalize the learner over the sampled support (= score centering) or use the gap-weighted baseline — importance ratios do not help; (4) use the sharper/flatter taxonomy to predict the sign of ANY constant-shift artifact (fixed format bonus, constant KL penalty) before running.

## 激活关键词
- entropy drift / entropy explosion / entropy collapse (RLVR 熵漂移/熵爆炸/熵塌缩)
- sampler mismatch, sharpness gap (采样器失配, 锐度间隙)
- top-k / top-p / min-p truncation, temperature != 1
- overlength filtering: MASK vs FAIL vs PEN (超长响应掩码 vs 判失败)
- token-weighted net advantage (token 加权净优势)
- score centering, support renormalization (分数中心化/支撑重归一)

Related: two-clocks-rlvr-batch-scaling (progress vs failure clocks), ase-activation-space-exploration-rlvr and elitereplay-quality-diversity-replay-grpo (diversity/explosion handling), epic-exact-kl-prefix-clipping (off-policy corrections that do work), policy-gradient-baselines-score-centering (centering in the estimator space), router-drift-control-moe-rl (response filtering vs drift).