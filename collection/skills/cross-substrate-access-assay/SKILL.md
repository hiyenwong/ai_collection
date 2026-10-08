---
name: cross-substrate-access-assay
description: Use when transferring brain tests to AI substrates.
category: ai_collection
---

# Cross-Substrate Access Assay (CSAA)

**Source**: arXiv:2609.22300 (van Rooyen, Sep 2026, cond-mat.dis-nn/q-bio.NC)

## When to Use
- Testing a consciousness/cognition indicator (e.g., global neuronal workspace "ignition") on a language model when the measurement was developed on brains
- Any cross-substrate model comparison where two systems share no physical measurement scale (microvolts vs activations)
- Designing calibration batteries of synthetic datasets with known generating families
- Auditing whether a statistical decision procedure keeps error rates after substrate transfer

## Core Problem
A measurement calibrated on ONE substrate instance (human brain, n=1) cannot separate phenomenon from substrate. A transferred measurement can change **what it measures** without any sign. Every component justified by the first substrate (20 brains, trial-to-trial neural noise, a time axis) loses its justification on a fixed LLM checkpoint (deterministic, no participants, layer depth ≠ time).

## The Five Declared Components (the complete interface)
Any procedure turning a readout into a verdict must declare ALL five. Once these + the readout are fixed, the verdict is determined by data alone:

1. **Predictors** (hypothesis space): competing families of conditional densities. Human EEG case: null/graded/two-state mixture models. Critical pitfall: fixed models were adequate only because each participant was fitted separately; a pooled fixed checkpoint has item heterogeneity that a one-state law can exploit to imitate two states.
2. **Fitting** (estimation map): optimizer + nested model selection. Solver changes <0.2% of projection spread yet moved the two-state onset boundary 315→285 ms — a boundary that moves with the solver is a property of the fitting, not the brain.
3. **Sampling unit** (exchangeability): what the inference generalizes over. Human: participant. LLM: the CONCEPT (variability must be placed in stimuli by design since the substrate is deterministic). Check claimed SE vs replicate SD: ratio 1.04–1.13 at homogeneous settings, degrading to 3.3× under item-scale heterogeneity ω=1.
4. **Uncertainty target** (estimand): the named quantity the interval is about. Coverage is UNDEFINED until the estimand is named. The transferred procedure made zero false calls yet its nominal 95% interval failed the 0.90 inclusion floor at 6 of 12 graded settings (down to 0.216) — an error-rate audit alone would have passed it.
5. **Decision rule**: statistic+uncertainty → the quoted sentence. Same fits supported three different sentences (single window at 315 ms, sustained run from 315 ms, corrected set from 375 ms) depending on the rule.

## Information-Theoretic Footing (why it enables the transfer)
- **Common scale**: score every description by held-out cross-entropy in nats per trial — dimensionless, no unit conversion needed. Δ_c = (log q_X,c − log q_G,c)/n_c per concept.
- **Proper scoring rule**: held-out log loss not improved by mere flexibility (in expectation).
- **Estimand itself in nats**: θ_g = expected cross-entropy difference under a declared generator.
- **Hypothesis is an entropy claim**: workspace ignition ⇒ latent state S carries ≤1 bit about dose: I(K;S) ≤ ln 2; graded ⇒ all of I(K;Y) in one continuous state.

## The Two Competing Families (test case: GNWT ignition)
- **Graded family G**: one state, logistic-location μ(k) with spread tied to mean σ(k)=|aμ(k)+b|; members add concept random threshold (τ), concept random scale (ω), skew-normal (α) — the three literature mechanisms by which one-state data fakes all-or-none structure.
- **Mixture family X**: two states with dose-dependent occupancy A(k)=logistic; ordered (high>low at every dose); members add concept effect, separate scales, free catch-level occupancy π₀.

## Procedure (one layer)
1. Split concepts into 5 concept-disjoint outer folds (stratified by family)
2. Per outer fold: 4 inner concept-disjoint folds; fit every retained member (L-BFGS-B multi-start, analytic gradients: 4 starts inner, 8 refit, recovery chain +16/+16); select best member per family by inner held-out joint log-score (integrates concept random effects)
3. Score held-out concepts; statistic Δ_c = per-trial difference of family held-out log scores
4. Interval: B=2,000 concept-level bootstrap resamples (fixed out-of-fold scores), I_0.95 = [Q_0.025, Q_0.975]
5. Decision: mixture support if Q_0.025>0; graded support if Q_0.975<0; else inconclusive; assay failure if any fit/score non-finite → "unavailable" (recorded as failure, not as evidence)

## Calibration Battery (the method's core deliverable)
- **Specificity**: 12,000 synthetic datasets (R=1,000 × 12 graded null settings: base, τ∈{0,.5,1,2}, α∈{0,1,3}, ω∈{0,.5,1,2}), all graded by construction = adversarial nulls. Result: expanded families+selection → **0 false mixture calls** (exact one-sided 95% bound 0.003/setting); inherited pair from the published human study → **989 false calls**, all where the generator carries item heterogeneity both its models omit (651 at τ=2).
- **Sensitivity**: separate 600 mixture datasets → rule returns mixture on 599. NEVER pool specificity and sensitivity counts.
- **Interval inclusion**: Ĉ_g = share of intervals containing the procedure's own replicate mean; draft floor 0.90; failed at 6 settings (0.216 at ω=2, where the reference itself is unstable: mean −6.87 vs median −2.07, one dataset dominates).
- Rules: F̂_g ≤ 0.05+2√(0.05·0.95/R) (=0.064 at R=1000); Ĉ_g ≥ 0.90 for every null. Zero-false-call bound: F⁺=1−0.05^(1/R).

## Key Results (measured costs of skipping components)
| Skipped component | Measured cost |
|---|---|
| Predictors (inherited pair) | 989/12,000 false two-state calls under graded truth |
| Fitting (solver swap) | onset 315→285 ms, late boundary 675→735 ms |
| Sampling unit (concept vs participant) | claimed SE under-estimates replicate spread up to 3.3× under ω=1 |
| Uncertainty target | 95% interval misses 0.90 inclusion floor at 6/12 settings (min 0.216) |
| Decision rule | 3 different published-sounding sentences from identical fits |

## LM-Side Protocol (draft, to be frozen before confirmatory data)
- Stimuli: natural-text packets, dose k∈{0,1,2,3,4,6,8} informative clues, 6 carriers × 7 levels; readout = frozen per-layer dose-decoder (trained on 16 calibration concepts, extremes 0 vs 8)
- Unit: concept (unnamed target); inference to NEW concepts on ONE frozen checkpoint
- Three registered predictions: (a) statistical — mixture beats graded in workspace band with interval excluding zero; (b) bridge — same preference on target–foil projection (without it: result about the coherence readout only); (c) causal — swapped representation's effect size depends on the mixture-assigned state. (a)+(b) can stand with (c) unsupported.
- Pilot (16 concepts, layer 41): all three predictors returned GRADED (−0.09 to −0.12 nat/trial, all intervals below zero) — a development run, NOT evidence about access (sensitivity used 64 synthetic concepts).

## Implementation Notes
- Concept random effects: likelihood integrates over the per-concept effect (joint predictive score, NOT sum of single-trial entropies)
- Non-nested families by design: each is the smallest set within which the other could be imitated by named mechanisms
- Decoder fitted at dose extremes then applied near threshold — whether the projection itself creates two-state structure is untested; requires activation-generating simulation
- Reported human preference: 0.0025–0.003 nat/trial at plateau; magnitudes across substrates are NOT comparable (common scale ≠ common effect)

## Honest-Limits Checklist (apply when reusing)
- [ ] Are all five components declared for BOTH substrates?
- [ ] Was variability relocated to stimuli (unit=concept) since checkpoint is deterministic?
- [ ] Specificity AND sensitivity run on separate dataset banks, never pooled?
- [ ] Interval checked against named estimand, not just error rates?
- [ ] Verdict sentence traceable to the pre-declared decision rule?
- [ ] Any cross-substrate magnitude comparison avoided?

## Cross-References
- Sergent et al. EEG dataset (20 participants, auditory vowel-in-noise) — anchored reproduction
- Gurnee et al. workspace directions + linear lens in LLM middle layers
- Related skills: [[llm-self-correction-confidence-signals]], [[biology-consciousness-ai-testability]]
