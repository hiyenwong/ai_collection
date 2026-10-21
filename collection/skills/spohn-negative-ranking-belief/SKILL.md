---
name: spohn-negative-ranking-belief
description: Elicit Spohn disbelief ranks to test graded human belief.
category: neuroscience
trigger: negative ranking theory, Spohn ranks, degrees of disbelief, belief measurement, formal epistemology experiments, Law of Negation, Law of Disjunction, Ellsberg paradox ambiguity aversion, subjective probability alternatives, belief revision, two-sided rank function, disbelief elicitation protocol
---

# Negative Ranking Functions as an Empirical Measure of Human Belief

**Source**: "What I Disbelieve: Quantifying Belief With Negative Ranking Functions" — Hanbin Go & Britt Anderson (Univ. of Waterloo), arXiv:2610.28357 (q-bio.NC, 20 Oct 2026). Reproducible manuscript: codeberg.org/brittAnderson/neg-rank-belief (all R analyses in goAnderson.Rnw).

## Core Finding

First systematic empirical test of Wolfgang Spohn's Negative Ranking Theory (NRT) as a *descriptive* model of human belief, across 6 experiments (N = 168/63/200/201/209/290). Human belief has the **bipolar, negation-respecting structure** NRT proposes, but **combines disjuncts by averaging, not minimization** — the first quantitative signature separating rank-based belief from both probability and the normative theory.

- **Ranks are reliable**: online/lab replication pairs concord; moderately difficult (modal 4/7) but usable; whole numbers avoid the renormalization burden that probabilities impose (no need to keep all options in working memory or rescale when a new option appears).
- **Law of Negation respected everywhere except lotteries**: people never disbelieve both A and Ā (κ(A)>0 ∧ κ(Ā)>0 counts as disbelieving existence) — except in gambling, where skepticism licenses nonzero disbelief in BOTH winning and losing. Gedanken lottery arguments in philosophy that assume deductive coherence fail empirically here.
- **Law of Disjunction violated by averaging**: instead of κ(A∨B)=min(κ(A),κ(B)), participants give intermediate ranks. LME on arsinh-transformed ranks: minimum rank predicted disjunction only for the temperature scenario (β=1.05); for music/language scenarios the MAXIMUM rank carried the larger effect (interactions β=−0.92/−1.06 for min, +0.84/+0.59 for max). Participants weigh the larger disbelief too — averaging, not min.
- **Ranks ≠ transformed probability**: the relation is nonlinear, context-dependent, and noisy; exponential decay often fits better than the theory's predicted logarithm (log with infinitesimal base). BUT in a learnable-probability hide-and-seek task (Exp 4), ranks aligned MORE closely with objective probabilities than subjective probability reports did — ranks are the better measurement instrument even when probability is the latent construct.
- **Ellsberg paradox nearly vanishes under ranks**: ambiguity aversion 6.4% (ranks only, Exp 5) and 8.6% (Exp 6) vs ~50% in the betting literature; same participants betting in round 1 showed 48.97% paradoxical choices, collapsing to 1.38% once 4 rounds allowed neutrality. No correlation between rank differences and bets (r=0.07). Randomization null (within-proposition shuffle ×1000) yields 21.2%/20.0% paradox rates — the reduction is a within-participant property, not a number-assignment quirk. **Ambiguity aversion is a betting-context artifact, not an epistemic estimate.**

## The Formalism (testable commitments)

An NRT state assigns each proposition a disbelief rank κ(A) ∈ {0,1,2,…,∞}:
- κ=0: not disbelieved (0 ≠ believed — equipoise); κ=∞: impossible; ranks are ORDINAL magnitudes (participant picks own scale; most use 0–10 or 0–100).
- **Conjunction**: κ(A∧B) = κ(A)+κ(B) (log-probability-like: ranks are logs of probabilities in an infinitesimal base).
- **Law of Negation**: min(κ(A), κ(Ā)) = 0 always.
- **Law of Disjunction**: κ(A∨B) = min(κ(A), κ(B)) — the tested-and-failed law.
- **Two-sided rank** τ(A) = κ(Ā) − κ(A): >0 belief, <0 disbelief, 0 suspension of judgment. This TRIPLE (believe/disbelieve/suspend) cannot be expressed by probability: a Bayesian 0.5 prior is a *strongly held* conviction of uniformity, whereas τ=0 is genuine ignorance — mirrors Dempster–Shafer's separation of ignorance from uniform chance.

## Elicitation & Testing Protocol (reusable)

1. **Disbelief question format**: "How much do you disbelieve [proposition]? 0 = not surprising; >0 = surprising; ∞ = impossible" — integers, participant-chosen range, ∞ via checkbox. Ask negations for two-sided ranks; add a yes/no belief question to cross-validate τ sign.
2. **Scenario design**: pick propositions with no natural probability (Quebec language demographics, September weather, co-worker karaoke tastes) to avoid probabilistic priming; include one known-probability item (lottery 900/1000) and one learnable item (hide-and-seek vs. sampled opponent distributions 40-40-20 / 100-0-0 / 80-15-5 / 70-30-0) for ground truth.
3. **Disjunction test**: LME predicting arsinh(κ(disjunction)) from arsinh(min-rank) + arsinh(max-rank) + scenario interactions, random intercept per subject; exclude min=max ties (~25%); beware min/max multicollinearity (r≈0.96 when disjuncts similar — design DISCREPANT disjuncts, Exp 3 fix).
4. **arsinh transform** for unbounded ranks (handles 0, unlike log); report medians + IQR (IQR = disbelief consensus).
5. **Ellsberg rank version**: collect κ for red / black / red∨yellow / black∨yellow (90 balls: 30 red, 60 unknown split); paradox = κ(red)<κ(black) ∧ κ(red∨yellow)>κ(black∨yellow); benchmark against the within-proposition permutation null, not just the sign pattern.
6. **Probability comparison**: collect subjective probabilities ONLY after all rank tasks (avoid priming); an interactive 10×10 card grid (OSF) measures implicit probabilities without numeric priming.

## When to Use This

- Measuring belief/uncertainty where probability is undefined, unknowable, or primes the construct you're studying.
- Testing logical structure of belief representations (negation coherence, disjunction composition) — the averaging-not-min result is a target signature for any cognitive/LLM belief model.
- Dissociating epistemic estimates from choice behavior (Ellsberg-type artifacts): ask ranks AND bets in the same participants; four betting rounds with neutrality expression.
- Belief-revision dynamics: NRT updates are LOCAL (adjust ranks the evidence touches) vs Bayesian global renormalization — natural fit for studying nonmonotonic revision (ostrich/lottery exceptions).

## Pitfalls

- A κ=0 is ambiguous between "believed" and "suspended" in one-sided protocols — use two-sided τ when the belief/suspension distinction matters.
- Lottery contexts license double disbelief (both win and lose κ>0) — a domain-specific violation of negation, not noise.
- Disjunction averaging means normative min-combination will fail as a participant model; model the intermediate behavior (weighted average with larger weight on the minimum).
- ANOVA on ranks violates normality (Shapiro-Wilk p<.001 even after log) — Kruskal-Wallis as check, disclose the violation; ranks are robust to it at large N.
