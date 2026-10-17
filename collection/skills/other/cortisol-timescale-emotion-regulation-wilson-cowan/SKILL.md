---
name: cortisol-timescale-emotion-regulation-wilson-cowan
description: Cortisol delay-kernel effects on cortico-limbic dynamics.
trigger_words: cortisol, emotion regulation, distributed delay, Gamma kernel, bifurcation, infra-slow oscillation
category: ai_collection
---

# Cortisol Time-Scales in a Wilson-Cowan Model of Emotion Regulation

**Source**: Buccino, Ginart, Kaslik, Rădulescu (SUNY New Paltz / W. Univ. Timișoara), arXiv:2610.19282 (Oct 2026), q-bio.NC

## Core question

Stress cortisol acts on prefrontal–amygdala circuitry on **multiple timescales** (fast non-genomic endocannabinoid disinhibition within minutes; slow genomic/structural effects over tens of minutes to hours). Does the dynamical impact on circuit-level emotion regulation depend only on the *characteristic timescale* of cortisol action, or also on the **shape of the temporal memory** through which past activity influences present coupling?

## Circuit architecture (4-node Wilson-Cowan)

State variables = signed normalized population-recruitment deviations in [−1,1]:

- **P** — prefrontal pyramidal (excitatory, recurrent microcircuit)
- **S** — cortical SST+ interneurons (dendritic feedback/feed-forward inhibition onto P)
- **C** — BLA principal neurons (reciprocal PFC↔amygdala excitation)
- **B** — BLA interneurons (PV+/SOM+, recurrent inhibition onto C)

Dynamics: τ_i Ẋ_i = −X_i + (1 − X_i)·S_{β_i,θ_i}(Σ_j w_ij X_j + I_i), with baseline couplings w_PP ∈ [0,8] (recurrent PFC excitation), w_CB ∈ [−7,0] (BLA inhibition), w_PC = 0.3, w_CP = 1.5, w_SP = 2.2, w_SC = 1.2, w_SS = w_BB = −0.4, w_BP = 0.8, w_BC = 2.2, w_CC = 2, w_PS = −3; tonic inputs only on principal populations (I_P = 0.18, I_C = 0.2) — interneurons are recruited by local principal drive, not independent tone. Time constants: τ_B = 4 (fastest, GABA_A kinetics), τ_P = 8, τ_C = 10, τ_S = 12; common threshold θ = 0.4, gains β ≈ 3.5–4.

## Cortisol as history-dependent coupling modulation

Cortisol is NOT a state variable or direct drive — it modulates the two stress-sensitive couplings via **distributed delays** driven by amygdala principal activity C(t):

    R_j(t) = ∫₀^∞ g_j(θ; n_j, τ_j) C(t−θ) dθ,  g_j = Gamma kernel (shape n_j, scale τ_j, mean μ_j = n_j τ_j)

- **Fast action** (endocannabinoid disinhibition of BLA): w_CB(t) = w_CB·(1 − β_CB·R_f), mean delay μ_f = n_f τ_f ∈ [2,8] min — acute glucocorticoids suppress GABAergic inhibition onto BLA principal cells (increases anxiety/fear facilitation).
- **Slow action** (structural PFC remodeling): w_PP(t) = w_PP·(1 − β_PP·R_s), mean delay μ_s ∈ [15,120] min — chronic stress retracts dendritic arbors and reduces spine density in mPFC pyramidal neurons, weakening recurrent excitation and top-down control.

β_CB = β_PP = 2, bounded so w stays sign-preserving.

**Linear chain trick**: integer-shape Gamma kernels convert exactly to a finite ODE chain ż_1 = (C−z_1)/τ_f, ż_k = (z_{k−1}−z_k)/τ_f, with R_f = z_{n_f} (analogous y-chain for slow). This yields a finite Jacobian → polynomial characteristic equation → MatCont continuation for equilibria AND cycles. The discrete-delay limit requires the pseudospectral importer (order M=10) instead.

## Experimental design (the three-kernel comparison)

Fix the mean delays, vary only the memory **shape**:

1. **No delay** (reference): intrinsic dynamics — oscillations born by supercritical Hopf as w_PP rises, terminated either by LPC (weak inhibition) or SNIC-like period blow-up (mid inhibition); termination w_PP nearly invariant across inhibition levels.
2. **Weak Gamma (n=1)**: kernel maximal at zero delay (emphasizes immediate past).
3. **Strong Gamma (n=2)**: delayed peak, smaller variance μ²/n at same mean.
4. **Discrete delay (n→∞ limit)**: modulation from activity at one sharply specified past time.

Parameters used: weak n=1 (τ_f = 120s, τ_s = 1000s); strong n=2 (τ_f = 60s, τ_s = 500s, same means); discrete τ_f = 120, τ_s = 1000.

## Headline results

1. **Memory presence vs memory shape are separable axes.** Introducing temporal memory (any distributed kernel) reshapes the oscillatory region: Hopf onset shifts to LARGER w_PP (history initially stabilizes the equilibrium), but once cycling is established it persists over a much broader w_PP range; very strong inhibition (w_CB ≲ −4) now cuts cycling short via LPC/homoclinic — a lower inhibition cutoff absent in the instantaneous system. Rich codim-2 structure (GH, BT, ZH, HH, cusp clusters) appears, esp. mid-w_CB.
2. **Weak ≈ strong Gamma (robustness).** At fixed mean delays, n=1 vs n=2 produce nearly coincident two-parameter bifurcation diagrams — global dynamics are buffered against moderate variation in temporal spread. Caveat: only one step in the Gamma family; not a proof across all orders.
3. **Discrete delay is qualitatively different.** The infinite characteristic spectrum produces a flurry of Hopf branches and an extensive **Neimark-Sacker (NS) boundary**: for w_CB from −1 to −4, increasing w_PP past the supercritical Hopf region ends regular periodic cycling via NS into **stable quasiperiodic motion on invariant tori** — not a suppression of oscillation but a modulation of timing/shape of successive loops; stronger inhibition (w_CB < −4) still ends cycles via LPC. Increasing w_PP lengthens the torus-return time: recurrent excitation changes not just *whether* the circuit oscillates but *how regularly/quickly* cortico-limbic states are revisited.

## Interpretation

- Infra-slow (0.01–0.1 Hz) alternation between reactive (high C, high arousal) and regulated (high P control) phases is the model's oscillatory regime; period/duty cycle encode duration of reactive vs suppressed phases.
- Cortisol memory does NOT translate the oscillatory region monotonically — it **reshapes** the (w_PP, w_CB) region where cycling can persist (effective couplings = baseline ⋅ history-filtered reductions; the circuit experiences time-varying effective coupling that can transiently sit inside the cycling window even when baseline values are outside it).
- Distributed memory smooths delayed feedback enough to preserve a robust periodic organization; sharply localized feedback adds a temporal modulation of the cycle → quasiperiodicity. **The shape of temporal integration may be functionally meaningful in its own right** — different kernels could characterize different circuits/states/tasks, and shifts in integration profile may be a route to atypical or pathological rhythmic regimes (hypothesis, but the NS-torus result makes it concrete).
- Empirical anchors: infra-slow oscillations exist in vitro without endocrine coupling (dissociated cortical nets <0.01 Hz; BLA/parahippocampal slices 5–30s periodicity; glutamate-driven 0.015 Hz with uptake blockade → NMDA depolarized state at stronger blockade — matching the insufficient/optimal/excessive excitation tri-phasic window).

## Methodological patterns to reuse

- **Separate memory presence from memory shape**: fix mean delay, sweep kernel shape (n=1, 2, …, ∞). Most systems conflate the two; this design isolates them.
- **History-dependent coupling modulation** (not state variables, not inputs): a compact way to model slow endocrine/metabolic/structural modulation of a fast circuit — keeps the fast system's phase portrait interpretable while letting slow variables wander through it.
- **Linear chain trick** for Gamma-distributed delays → exact finite ODE → MatCont two-parameter continuation in the two stress-sensitive couplings (the "cortisol targets") rather than raw delay lengths.
- **Extension protocol from equilibria**: continue from w_PP = w_CB = 0 (where delays have no effect) outward to avoid spurious stiff-integration results.
- **Read the two-parameter plane as an interaction map**: oscillatory window boundaries change mechanism (Hopf onset; LPC vs SNIC vs NS termination) — report which mechanism, not just the region.

## Activation

cortisol, emotion regulation, distributed delay, Gamma kernel, Wilson-Cowan, bifurcation analysis, infra-slow oscillation, quasiperiodicity, Neimark-Sacker, stress modeling, cortico-limbic, HPA axis, temporal memory shape, linear chain trick, MatCont
