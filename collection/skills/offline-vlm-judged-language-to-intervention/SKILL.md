---
name: offline-vlm-judged-language-to-intervention
description: Learn language-to-biology control offline from archives plus VLM judge.
category: ai_collection
trigger: language-controlled biology, VLM-as-judge reward, offline archive learning, prompt-to-intervention mapping, xenobot behavioral control, bioelectric stimulation control, zero-shot reward model validation, contextual bandit biology, Le Levin Bongard living systems interface
---

# Offline VLM-Judged Language-to-Intervention Learning for Living Systems (P2I)

**Paper**: Le, Blackiston, Levin, Bongard — "Toward Controlling Biology with Language: Offline Learning of Prompt-Conditioned Interventions for Cells, Organoids, and Biobots" (arXiv:2610.02247, Tufts Allen Discovery Center / UVM, 30 Sep 2026)

## Core Insight

A natural-language interface for a *living organism* can be learned entirely offline: treat an existing archive of (intervention, outcome) pairs as a fixed dataset, use a pretrained VLM as a zero-shot judge scoring whether an archived outcome matches a prompt, and train a prompt→intervention network against the VLM's judgment alone — no new wet-lab experiments, no human labeling. Validated end-to-end on real xenobots (synthetic multicellular constructs, *no nervous system*): 80.0% held-out accuracy on both unseen prompts *and* unseen archive data vs 66.7% chance baseline, matching a network trained on ground-truth labels.

## Problem Structure

- Archive A = {(d_i, x_i)}: real electrical-stimulation durations d_i and tracked PRE/POST trajectories x_i (101 batches: 26 'faster', 75 'slower', from 149 tracked, 48 excluded as unreliable — biological replicates, each a distinct construct).
- No ground-truth (prompt, duration) pairs exist — no human ever paired them. Direct supervision impossible.
- Online collection is prohibitive: every paired datum = one wet-lab experiment.
- Multi-task with opposing goals ("speed up" vs "stop") → gradient interference if pooled in one unconstrained shared head.

## Pipeline (5 components)

1. **Trajectory extraction**: SAM-based 3-tier tracking (bounding-box re-detection, optical-flow-guided prompting, grid-search prompting), cross-checked against dish geometry — robust to stimulus-induced air bubbles, specular reflection, debris. Frames where all tiers fail = missing data, not stillness.
2. **Assessment windows**: fixed-length PRE/POST windows (30 pre-frames, 50 post-frames, median aggregation) selected by 112-point grid search maximizing Mann–Whitney separation of real faster/slower batches. **Window length must NOT scale with duration d** — xenobots naturally decelerate post-stimulus; a d-scaled window confounds duration with observation time.
3. **Judge J(p, x) ∈ [0,1]**: VLM scores real trajectory vs prompt. Crucially J sees *raw position trajectories, not precomputed velocities* — giving J the velocity number lets a numerical rule do the job, defeating the point. Verified: raw-position judge r=0.843 with 97% sign agreement vs independent ground truth; velocity-plot judge only r=0.49–0.66. Forcing genuine inference makes the judge *more* reliable, not just harder to game.
4. **P2I network f_θ**: frozen SBERT (384-d) → 64 (ReLU, dropout 0.2) → 32 → **one sigmoid head per behavior category** (2 heads, 26,786 params). Per-category heads prevent opposing gradients from sharing an output. A distributional single shared head (µ,σ + tuned regularization) tested directly: worse and less stable on unseen language.
5. **Reward table**: r_i(p) = J(p, x_i) for all 101×33 = 3,333 (archive, prompt) pairs, computed once offline, never queried during training.

## Two Training Routes from One Reward Table

**(a) Discrete (ablation)**: snap predicted duration to nearest archive point, take its raw score — piecewise-constant, non-differentiable → REINFORCE or CMA-ES required.

**(b) Differentiable (reference)**: fit per-prompt logistic curve r̂_p(d) = σ(w_p d̃ + b_p), d̃ = (d − d_min)/(d_max − d_min); reduce to single target d†(p) = duration at midpoint of r̂_p's achieved range, clipped to nearest archive-verified correctly-labeled interval; ordinary MSE + Adam backprop. No VLM/archive/simulation queried during training steps.

**Cross-optimizer validation**: backprop / REINFORCE / CMA-ES all consume the identical reward table; their agreement validates the optimum (backprop best: Train 89.1%, GT2 80.0%; REINFORCE 66.9%, CMA-ES 62.9% on GT2).

## Evaluation Protocol (4-cell design)

Train = P_train × A_train; GT3 = P_train × A_test; GT1 = P_test × A_train; **GT2 = P_test × A_test** (both axes held out). k-NN (k=3) vote against independently-tracked behavior labels. Chance is 66.7%, NOT 50% — 2 of 3 prompt buckets ('stop', 'slow') map to the same 'slower' archive direction; a constant-'slower' baseline wins 2/3 by construction. Head inference for held-out prompts via nearest-centroid embedding similarity, never category lookup.

## Key Validations

- **VLM judge trustworthy**: net score s(b) (mean faster-prompt score minus slower-prompt score per batch) vs true label: r=0.843, 97% sign agreement, all disagreements within ±0.02px/s of true zero change. Against raw velocity delta only r=0.49 — J separates categories, doesn't linearly track fine-grained speed (consistent with per-prompt target use).
- **Anti-p-hacking**: the 112-way window grid search was permutation-tested (200 shuffles × full search) — real p=1.57e-4 more extreme than all 200 null best-cases.
- **VLM reward non-redundant**: replacing d†(p) with a single fixed duration per direction chosen from real velocity extremes trains to identical loss but **collapses GT2 to 59.1% (below chance)** — the fixed 'faster' duration happens to land in held-out 'slower' territory; a placement failure invisible in training accuracy. Curve-fitting the full scored distribution avoids it; a single extremal point cannot.
- **Paraphrase stress**: 120 new paraphrases (8× scale) on the frozen trained model: 85.0% (vs 80.0% original) — 'stop' most robust bucket (97.8% land on true stops).
- **Honest negative**: 'stop' vs 'mild slower' sub-distinction exists in data (p=7.5e-6, velocity-within-10%-of-baseline rule) but 3 attempts to learn it from language collapsed to the majority answer — data scarcity (n=14 mild), not model limitation. 'motion reduction' over-shoots to full stop 33.3% of cases.

## Implementation Checklist

1. Assemble fixed archive of (intervention, outcome-video); track with SAM multi-tier detection; never force-classify unreliable batches — exclude.
2. Fix PRE/POST assessment window lengths independent of intervention magnitude; select by grid search + permutation test.
3. Query VLM judge on raw trajectories (withhold precomputed metrics); validate judge against independent ground truth before trusting it.
4. Fit per-prompt logistic curves over the reward table; derive d†(p) targets; one output head per opposing behavior category.
5. Train by backprop; cross-validate with one gradient-free optimizer (CMA-ES) on the same table.
6. Evaluate on the 4-cell prompt×archive split; report chance level honestly (label-structure-dependent).
7. Deployment = retrieval: prediction snaps to nearest archived intervention; its real PRE/POST trajectory + velocities are shown to the user.

## Scope Limits (authors')

- One intervention parameter (stimulus duration); small archive; predefined behavior categories.
- No prospective experiment yet: does a predicted intervention on a *newly-stimulated* xenobot reproduce the intended behavior? Untested.
- System retrieves, doesn't generate — compositional recombination beyond archive untested.

## Application Beyond Xenobots

Same archive + VLM-judgment paradigm applies wherever intervention-outcome archives exist: cell/tissue cultures under electrical or optogenetic control, organoids, other synthetic living machines, and (further out) clinical bioelectric therapy — the offline half is the tractable starting point.

## Relation Map

- VLM-as-judge: Rocamonde et al. 2023 (zero-shot reward models) — here validated against independent non-VLM ground truth, not trusted by assumption.
- Predecessors: Le et al. 2025 (P2I in simulated cells, fixed vocabulary, non-differentiable assumed, (1+1)-ES/GA only); Le et al. 2026 (continuous VLM score, single prompt, gradient-trainability left open) — this paper answers both: differentiable reward fit + backprop cross-validated against 4 optimizers, 33 prompts, real living organism.
- Multi-task heads: Yu et al. 2020, Caruana 1997 — opposing-goal interference handled per-category heads.
- Offline contextual bandit: Levine et al. 2020 — reward shown differentiable, so both gradient and derivative-free search apply.
