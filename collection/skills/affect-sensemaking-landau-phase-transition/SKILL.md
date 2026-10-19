---
name: affect-sensemaking-landau-phase-transition
description: Affect emerges from Landau sense-making landscape minima.
category: ai_collection
trigger: affect modeling, valence arousal relation, emotion phase transition, sense-making landscape, mixed affect, affective disorders formalization
---

# Affect from the Sense-Making Phase Transition Framework (arXiv:2610.18115)

Use when formalizing affect/emotion theoretically, modeling valence-arousal relations, mixed emotional states, or building physics-based models of evaluation and mood dynamics. Source: Bosch, Fanfarillo, Diez, Gómez Mayordomo, Arias-Gonzalez, Valenzuela, "Sense-Making phase transition framework for Affect", arXiv:2610.18115 (Oct 2026). Builds on the sense-making Landau framework of Refs. [17,18] (inner sensation perception).

## Core construction
Affect is NOT an independent ingredient — it is READ OFF the sense-making landscape F(φ) that models evaluation of a sensation:

F(φ) = −h_ext·φ + (a/2)φ² + (h_int/3)φ³ + (b/4)φ⁴  (homogeneous limit)

- **Valence = position of a minimum** φ̄: sign gives pleasant/unpleasant, magnitude |φ̄| gives intensity. Neutral = φ̄ = 0.
- **Arousal = depth of the minimum** A(φ̄) = −F(φ̄) relative to the F=0 reference: measures stability and relevance of the state.
- **Affect = the point** (φ̄, A(φ̄)) in the valence-arousal plane. Dominant affect = global (deepest) minimum; shallower co-existing minima = secondary affect.

## Parameters (cognitive mapping)
| Symbol | Meaning |
|---|---|
| φ | valence order parameter (φ<0 unpleasant, φ>0 pleasant) |
| T | sensory context informativeness — high T noisy/uninformative → neutral evaluation; low T informative → polarized evaluation possible |
| a = a₀(T−T₀) | quadratic coefficient; T₀ = threshold where neutral state destabilizes (for h_ext=0) |
| h_int | learned historical valuation (internal bias; h_int>0 favors unpleasant sector) — KEEPS φ̄=0 stationary at all T |
| h_ext | socially mediated/external information (h_ext>0 favors pleasant) — SHIFTS the stationary state off neutrality already at high T (finite affect in noisy contexts) |
| b > 0 | intrinsic quartic stabilization |
| κ | stiffness of spatial variations over the network of vital norms — proxy for mental rigidity/coherence |

Microscopic basis: spin model on a network of "vital norms" (organic/sensorimotor/social/existential), spins ∈ {+1,0,−1}; coarse-graining yields φ and F.

## Phase structure (as T is lowered = context more informative)
**Symmetric (h=0)**: pitchfork at T₀ — continuous 2nd-order transition; two degenerate minima φ̄± = ±√(−a/b), equal arousal A = a²/4b growing as (T₀−T)²; spontaneous selection of one valence.

**Internal bias only (h_int≠0)**: sequence T₂ > T₁ > T_c > T₀ with c_i·h_int²/(a₀b) shifts (c₂=1/3, c₁=1/4, c_c=2/9):
- T₂: inflection appears (landscape begins deforming toward the biased sector)
- T₁: latent biased minimum appears with divergent susceptibility — SENSITIZATION onset
- T_c: coexistence — biased minimum reaches equal depth with neutral state, takes over as adapted state DISCONTINUOUSLY (first-order switch; at coexistence it sits at φ̄ = −2h_int/3b, both depths F=0 → zero arousal)
- T₀: neutral loses stability; SECONDARY opposite-valence minimum emerges → asymmetric mixed affect
- Metastability between T₀ and T₁: history-dependent persistence of a consolidated evaluation above T_c (inertia mechanism)

**External bias only (h_ext≠0)**: NO phase transition — adapted state moves continuously; a latent opposite-valence minimum appears at T_s (new affective options without changing the adapted state). Changing the SIGN of h_ext at low T swaps global stability between opposite-valence minima — FIRST-order in h_ext, enabling hysteresis: externally induced evaluations persist after the cue weakens/reverses (candidate formal language for placebo/nocebo persistence).

**Competing biases**: thresholds shift as T_i ~ T₀ + c_i·h_int²/(a₀b) − d_i·b·h_ext/(a₀h_int), d₁=2, d_c=3. External info opposing internal bias LOWERS T_c (needs more informative context for the learned tendency to dominate); reinforcing info raises it. Coexistence arousal scales as (h_ext/h_int)². Asymmetric hysteresis: established tendencies are easier to reinforce than reverse (matches pain-expectation self-reinforcement findings).

## Emergent valence-arousal relation (the V-shape is a THEOREM, not an input)
A(φ̄) = (h_ext/2)φ̄ + (h_int/6)φ̄³ + (b/4)φ̄⁴  — along any minimum (T implicit via φ̄(T)).
- Symmetric case: A = (b/4)φ̄⁴ — smooth upper-open curve; arousal rises with valence intensity in BOTH sectors.
- Biases break left/right symmetry → asymmetric V; empirical variability of V-shapes across studies/individuals/cultures = different trajectories through parameter space, not different laws.
- Each locally stable minimum contributes a point; only minima crossing below F=0 acquire positive arousal.

## Susceptibility & dynamics
χ(φ̄) = ∂φ̄/∂h_ext = 1/curvature — diverges at: T→T₀ (neutral flattening), T₁ (latent minimum birth), and any curvature-zero point. Shallow minima are easily displaced (flexible affect); deep minima are robust (consolidated affect).
Relaxation on fixed landscape: dφ/dt = −Γφ·∂F/∂φ → δφ(t) = δφ₀·e^{−t/τ}, **τ_φ = χ/Γφ** — critical slowing down near the uncertainty regime; susceptibility and recovery time COVARY (testable prediction: perturbation-recovery time tracks external-influence responsiveness for the same sensation). Mood-transition early-warning and emotional inertia connect here.

## Affective regimes (cognitive interpretation)
- **Neutral** (T>T₂): no relevance — zero arousal
- **Uncertainty** (near T₀/curvature→0): evaluation weakly stabilized, maximal receptivity to external info (also a candidate window for meditation/psychedelic low-prior-precision states)
- **Sensitization** (T_c<T<T₁): latent evaluation encoded but not dominant
- **Consolidation** (T<T_c): dominant state deepens with context informativeness
- **Mixed-valence** (T<T₀ or h_ext≠0): dominant + secondary opposite-valence states coexist — mixed affect WITHOUT independent positive/negative axes (contrast: Affective Ising Model, PANAS orthogonality)
- Negative-affect bias = recurrent privileging of the unpleasant branch; rigidification ACROSS contexts = candidate formalization of affective pathology (both Barrett-allostatic and enactive views converge here)

## Why it matters / when to use
- Bridges Barrett's allostatic account and enactive sense-making (Colombetti) in ONE formal object — affect = evaluative orientation read off the same landscape that organizes evaluation.
- Distinguishes valence INTENSITY from arousal (often conflated) while making them non-independent.
- Design parameter-specific experiments: vary context informativeness (T), prior learning (h_int), socially supplied info (h_ext); predict changes in valence/arousal, branch asymmetry, minimum curvature, susceptibility. Existing V-shape data (IAPS/OASIS/GAPED ratings, EDA/HR/pupil) are compatible but not yet a clean T-scan — experience-sampling with context annotation is the right test bed.
- Dynamics extension: time-dependent coefficients (h_int(t), T(t), h_ext(t)) → affect trajectory (φ̄(t), A(t)); emotions = dynamic attractors on the evolving landscape (Lewis' neurodynamical emotion program formalized).

## Pitfalls
- The T-scan V-shape is ONE projection; real protocols vary T, h_int, h_ext simultaneously — don't fit a single universal curve.
- Stimulus-set sampling bias: arousal-rich stimulus sets emphasize the V; naturalistic sampling may not.
- Arousal here is landscape depth, not any single physiological readout (EDA, HR, pupil are correlates, not definitions).
- Static framework: relaxation on FIXED landscape keeps arousal constant — true arousal dynamics requires time-dependent coefficients.
- "Adapted" state is relational/history-dependent, NOT an external optimum — do not interpret global minimum as normative health.

**Activation**: affect modeling, valence arousal V-shape, mixed affect, emotion dynamics, Landau theory psychology, sense-making, phase transition affect, sensitization consolidation, placebo nocebo persistence, mood early warning critical slowing down, allostatic enactive bridge
