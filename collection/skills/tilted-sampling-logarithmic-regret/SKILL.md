---
name: tilted-sampling-logarithmic-regret
description: "Use when learning to sample from Gibbs targets; log sampling regret."
category: reinforcement-learning
---

# The Tilted Sampling Problem: Optimism, Posterior Sampling, and Logarithmic Regret

Source: arXiv:2610.21908 (Pedramfar & Ravanbakhsh — Mila/McGill, Oct 2026). Theory: defines tilted sampling — an online problem where the learner must SAMPLE from the Gibbs distribution S_beta(f_theta) ~ exp(beta*f_theta) of an unknown reward instead of maximizing it — and proves sampling regret is governed by SQUARED confidence widths, giving logarithmic-in-T regret where optimization regret gives sqrt(T).

Use when: analyzing entropy-regularized RL / RLHF / reward-guided generative modeling (GFlowNets, energy-based sampling) as bandit problems, designing exploration for "sample diverse high-quality outputs" systems, or transferring UCB/Thompson-Sampling regret analyses to distribution-matching objectives.

## Setup
Rounds t = 1..T; revealed action set A_t; unknown f_theta in F, rewards in [0, C]; learner picks function g_t and SAMPLES A_t ~ S_beta,t(g_t) (controls a distribution, not a single action). Target: Gibbs distribution S_beta,t(f_theta)(da) = exp(beta*f_theta(a)) * mu_t(da) / Z, mu_t = base measure conditioned on A_t.

## Sampling regret (the key quantity)
SRegret(T) = (1/beta) * sum_t D_KL( S_beta(g_t) || S_beta(f_theta) )
- Exact duality: equals the suboptimality gap of KL-regularized reward maximization J_beta(pi) = E_pi[f] - (1/beta)*D_KL(pi||mu_t), since J(S_beta(f)) - J(pi) = (1/beta)*D_KL(pi||S_beta(f)). The Gibbs target is the unique maximizer.
- As beta -> infinity, S_beta(f) -> argmax: UCS and TS2 recover UCB/TS (Gibbs operator interpolates sampling and maximization).
- Variants: forward-KL regret (mass the learner fails to cover); TV-regret <= sqrt(T*SRegret/2) via Pinsker.

## Structural theorem (why log, not sqrt)
Bandit optimization: max f(a), non-smooth, FIRST-order uncertainty, regret ~ sqrt(sum w_t), algorithms UCB/TS.
Tilted sampling: pi ~ exp(beta f), smooth KL geometry, SECOND-order regret sum w_t^2, algorithms UCS/TS2.
KL geometry converts first-order uncertainty into second-order regret: when squared widths accumulate logarithmically (Eluder-dimension arguments, Russo-Van Roy style), sampling regret is LOGARITHMIC in T at fixed beta.

## Algorithms
- UCS (Upper Confidence Sampling): g_t = U_t (upper confidence envelope), sample A_t ~ S_beta(U_t). Pointwise optimism removes the exp(beta*C) factor.
- TS2 (Thompson Sampling for Sampling): draw theta_tilde ~ posterior, sample A_t ~ S_beta(f_theta_tilde). Posterior exchangeability (true theta and posterior draw i.i.d. given history) gives TWO-SIDED KL guarantees.
- SWC (Sampling With Confidence) framework: any g_t with L_t <= g_t <= U_t. Generic SWC pays exp(beta*C); UCS/TS2 do not.

## Guarantees
- Thm 2 (SWC): E[SRegret] <= (beta/2)*exp(beta*C)*E[sum w_t(A_t)^2] + 2CT*P(E^c)
- Thm 3 (UCS): <= E[sum w_t] + 2CT*P(E^c) AND <= (beta/2)*E[sum w_t^2] + 2CT*P(E^c)
- Thm 4 (TS2, Bayesian): <= E[sum w_t] + 4CT*P(E^c) AND <= beta*E[sum w_t^2] + 4CT*P(E^c)
- Thm 5: with least-squares confidence sets + Eluder-type arguments, UCS/TS2 regret is O~( min{ (1+gamma T)^dE * sqrt(T), beta*(1+gamma T)^dE } ) — at fixed beta the log branch wins as T grows; crossover beta*(T) ~ sqrt(T/D).
- Black-box transfer: ANY UCB/TS-style width analysis converts to a sampling-regret guarantee by replacing maximization with Gibbs sampling.

## Limitations
Bounded rewards, direct noisy reward feedback, exact Gibbs sampling; log guarantees hold at FIXED beta; matching lower bound open. Greedy SWC has no temperature-independent sublinear guarantee (hard-max limits can be linear regret).

## Reuse pattern
When a system's goal is distribution-matching rather than argmax (GFlowNets, entropy-regularized policies, RLHF with KL-to-reference, diverse generation, energy-based samplers): (a) state the objective as matching S_beta(f_theta); (b) define regret as (1/beta)*sum KL; (c) run optimism/posterior exploration in FUNCTION space (UCS/TS2); (d) reuse existing confidence-width analyses for log regret. Second-order regret means uncertainty-driven exploration is CHEAPER than in optimization.

Related: DMRL (density-matrix RL), GPPO (f-divergence family), multi-armed sampling (Pedramfar & Ravanbakhsh 2025, arXiv:2507.10797), GFlowNet foundations, soft actor-critic.
