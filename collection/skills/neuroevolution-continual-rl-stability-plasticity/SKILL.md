---
name: neuroevolution-continual-rl-stability-plasticity
description: NE beats RL at continual task switches. Use for stability-plasticity tradeoff or plasticity loss topics.
category: ai_collection
trigger: continual reinforcement learning, plasticity loss, stability-plasticity tradeoff, neuroevolution, evolution strategies, genetic algorithm policy search, population-based training, forgetting in RL, return landscape neighborhood
---

# Neuroevolution for Continual RL: Stability-Plasticity via Wide Return Neighborhoods

**Source**: Nisioti, Cossu, Korte, Risi — "Continual Reinforcement Learning with Neuroevolution" (arXiv:2610.01583, IT University Copenhagen / Sakana AI / Univ. Pisa, Oct 2026)
Code: https://github.com/eleninisioti/continual_neuroevolution

## Core Thesis

Gradient-based RL (PPO) loses plasticity under task switches; continual-RL patches (ReDo, TRAC, C-CHAIN) restore plasticity at the cost of stability. Neuroevolution (NE) — searching in weight space via mutation+selection over a population — achieves the best stability-plasticity trade-off (ES) or the highest plasticity (GA), without any continual-learning-specific machinery. The mechanism: **parameter-space exploration biases solutions toward wide return-landscape neighborhoods, whose overlap between consecutive tasks predicts the stability-plasticity trade-off.**

## Key Empirical Findings

1. **ES best trade-off** (LA−F): best in 8/18 settings; no RL method best in any. ES fails under action reversal on Acrobot/MountainCar (fitness variance collapses to ~0 at switch).
2. **GA most plastic**: highest learning accuracy in 10/18 settings; only method fully learning both action orderings under reversal; forgets more than ES everywhere.
3. **ES highest zero-shot transfer** (10/14 settings). No method transfers to unseen Kinetix levels.
4. **Neighborhood width predicts trade-off**: shared-neighborhood fraction (perturb centroid at radius ϵ=0.1; fraction solving both tasks) correlates with LA−F (Spearman ρ=0.77; NE 0.90, RL 0.70). ES neighborhoods ~2.3–3.9× wider than PPO's; measured in random directions AND along each method's actual update path (PPO's neighborhood is equally narrow along its own path; only ReDo-PPO's is ~2× wider along-path).
5. **RL plasticity-loss symptoms don't transfer to NE**: dormant-neuron fraction does not accumulate at switches in NE (task-dependent but flat); weight drift does not cost GA plasticity (GA weights drift by orders of magnitude, most plastic method). → These symptoms stem from gradient-based optimization, not from non-stationarity itself.
6. **Novelty search (Dominated Novelty Search + AURORA descriptors) raises plasticity further**: DeepSea action-map re-found after 57% of switches (vs 11% plain GA); the gain accrues to the *elite*, NOT the centroid — centroid averages members that solve different tasks and solves none.
7. **PBT-PPO** (population of gradient learners) helps only via reduced per-agent experience (8 members take turns → 1/8 updates each); its population diversity collapses early, so it does NOT exhibit GA-like plasticity.

## Method Mechanics

- **ES (Salimans-style)**: single centroid θ; evaluate P perturbations θ+σεᵢ; move θ along fitness-weighted sum = Monte-Carlo estimate of ∇ of expected return under N(θ, σ²I). ES *averages* perturbed copies → wide neighborhoods.
- **GA (Such-style)**: archive of N networks; perturb uniformly-drawn parents with Gaussian noise σ; keep fittest N of archive+offspring. GA *keeps best individuals, mutates them* → spread population, narrow per-individual neighborhoods, but a far member may already solve the new task → plasticity via selection.
- **GA centroid-lag heuristic**: GA never evaluates its centroid; when diverse, centroid scores far below best. Fix: lower mutation width while centroid lags; keep ¼ offspring at original width to preserve exploration.
- **Neighborhood definition**: region of weight space around solution where perturbed policy still solves task (rescaled return ≥0.5). Width = radius ϵ at which half of perturbed policies fail. Perturbations: random Gaussian direction per layer, length = fraction ϵ of that layer's weight norm (scale-free, per Li et al. 2018).
- **Shared neighborhood**: perturb at fixed ϵ=0.1, report fraction solving both current AND next task.

## Evaluation Protocol (reusable)

- Continual RL = sequence of T MDPs, **boundary-free** (no task-switch signal).
- Metrics: learning accuracy LA (return at end of training each task), forgetting F (return lost between end-of-training-on-task and end-of-run), trade-off **LA−F**, cumulative return, zero-shot transfer ZT.
- Population methods evaluated via **centroid** (mean of member weights), NOT best member — avoids max-over-noisy-evals bias.
- Stats: 10 trials, 95% bootstrap CI, one-sided Mann-Whitney U with Holm correction (p<0.05). LA/F rescaled per setting (0=untrained, 1=best method).
- Environments: CartPole/Acrobot/MountainCar, MiniGrid, Brax HalfCheetah, Kinetix (million-parameter conv policies), DeepSea. Change types: observation offsets, physics/dynamics rescaling, action reversal. 20-task sequence or 2-task alternation ×10.
- Fairness: all methods tuned to solve stationary version first; compute-matched.

## When to Apply / Integration Patterns

- **Continual or non-stationary control** where forgetting is the failure mode: consider ES as the policy optimizer; the population + noise IS the continual-learning mechanism (no rehearsal buffers, no regularization needed).
- **Diagnosing plasticity loss**: measure neighborhood width (random + along-path) before blaming non-stationarity — if gradient methods show narrow along-path neighborhoods, the symptom is optimization-side.
- **Diversity as plasticity lever**: behavioral novelty (AURORA-style learned descriptors) raises the chance a population member lands in the next task's neighborhood; harvest via elite selection, not averaging.
- **Averaging caveat**: centroid of a diverse population is a fiction — the average of weights solving different tasks solves none. Report both elite and centroid; use centroid only for comparison fairness.

## Limitations (honest)

- NE less sample-efficient; complex tasks need large populations.
- Where solutions are finely tuned (HalfCheetah locomotion), ES smooths over narrow peaks; RL wins even stationary.
- ES can freeze under action reversal when population fitness variance → 0.
- Novelty gains show on elite, not centroid.

## Related Skills

- `plasticity-prediction-deep-continual-learning` — theoretical framework for plasticity prediction in deep continual learning
- `noracl-neurogenesis-continual-learning` — neurogenesis alternative to NE for oracle-free continual learning
- `recap-regime-adaptive-portfolio` — regime-switching analogy in finance
