---
name: affective-valence-jacobian-scale
description: Valence as Jacobian-scale rate of change via interoception.
trigger: valence, affect, interoception, Jacobian scale, homeostasis, allostasis, pain, hunger, essential variables, self-sustaining system, terminal set, negativity bias, alliesthesia, phantom pain, pain asymbolia, wireheading, homeostatic reinforcement learning, free energy valence, affective computing, forecasting dread relief, Weber-Fechner
category: ai_collection
---

# Affective Valence as the Interoceptive Rate of Change of Jacobian Scale

Source: arXiv:2610.26350 (David Balduzzi; q-bio.NC cross nlin.AO, 19 Oct 2026; companion paper "Differential Functionalism" arXiv:2609.09306. Code: github.com/dbalduzzi/valence). A formal theory in which feeling good/bad is the rate at which interoception moves a self-sustaining system's responsiveness — the log scale of its parameter Jacobian — relative to its terminal set (death).

## Why it matters

- One quantity answers four open questions about affect: what fixes the reference point (the terminal set Z, fixed by the system's physics, not stipulated by a modeller), why some losses are unfelt (they bypass internal inputs), where a feeling is located (chain-rule split over locations), and when feelings mislead (ungrounded drives on internal inputs).
- Reproduces clinical dissociations in one minimal model: congenital insensitivity to pain (no receptors), pain asymbolia (no gain), phantom limb pain (driven receptors), hypoglycaemia unawareness (blocked reserve signal), hunger with undepleted reserve (driven signal), hunger suppressing pain (learned c>0), wireheading (gain learned to maximise its own scale).
- Clean criterion for machine valence: language models have none (not self-sustaining — externally powered, no essential variables their actions affect); a robot that smoothly scaled its responsiveness with a charge signal and recharged itself would qualify.

## Core formalism

1. **Log scale and terminal set.** For system S with actions y, inputs x, parameters W: J_S(s) := J_{y←W}(s). Scale ‖J_S‖ = Frobenius norm; log scale λ := log ‖J_S‖. Terminal set Z := {s : ‖J_S‖ = 0}, at λ = −∞. Z is where no action of the system makes any difference — it is attracting (responsive systems are energetically expensive, Jonas's "needful freedom", Di Paolo's precariousness).
2. **Hypothesis V (Definition 4).** Valence v = ∂_u λ · du/dt: the change of λ due to the system's internal inputs u (receptors, signals of energy reserve, forecasts built on them). Motion through no internal input (anaesthetic, brain damage — brain tissue has no nociceptors) changes experience but is not felt. Valence is a second-order quantity (d/dt of a first-order sensitivity) and the experience of a rescaling of experience.
3. **Essential variables (Def 3).** State variables e with J_{e←y} ≠ 0 (actions affect them), dλ/de ≠ 0 (they affect the scale), and precarious (min_y dλ/de < 0). Self-sustaining := has essential variables. Internal inputs: state variables u with J_{u←e} ≠ 0 and ∂_u λ ≠ 0 that do not run down on their own.
4. **Split over locations — Eq (1).** v = Σ_i v_i with v_i = w_i · d/dt log ℓ_i, shares w_i = ℓ_i²/‖J_S‖², where ℓ_i = ‖J_i‖ is the norm of the Jacobian row of action i. A change confined to one action is diluted by its share (intensity grows with spread); a scalar gain m (J_S = m J₀) has v = d/dt log m and no residual field — diffuse. **Residual field** δ_i = v_i − w_i v sums to zero (verified numerically: 2e-17), vanishes for pure rescaling, and localises valence — hunger is diffuse, pain is localised. Mixed feelings = concurrent terms of opposite sign, not a midpoint.
5. **Split over causes — Eq (2).** v = ⟨∂_u λ, J_{u←e} ė⟩ (grounded: essential variables) + ⟨∂_u λ, J_{u←ξ} ξ̇⟩ (ungrounded: phantom drives, false cues, drugs). Grounded and ungrounded terms can oppose; the direct unsignalled term ⟨∂_e λ, ė⟩ moves the scale but is never felt.
6. **Geometry.** J̇_S = v J_S + J̇_⊥ with ⟨J_S, J̇_⊥⟩ = 0: radial motion is valence; tangential motion changes shape Ĵ_S (transparency/integrity of companion paper) and locates/individuates the feeling. Conjecture: arousal ~ spectral norm σ₁(J_S) (fixed scale, largest when responsiveness concentrates).
7. **Why the logarithm.** Unit-free (derivative removes unit rescaling); Z at −∞ so the same absolute loss matters more the nearer the end (Weber-Fechner); separates gain from content (λ = log m + log ‖J₀‖).

## Model 1 — a differentiable body (six-term split, Eq 5)

Activity ỹ_{i,t} = m(Ê_t) · q(E_t) · h_{i,t} · G_i(r_t) · y_{i,t} with content y = f_W(x) (recurrent net, 16 hidden units); reserve E_t = (1−κ)E_{t−1} + γ·E_repl(ỹ) − C_t; tissue h_{i,t} = h_{i,t−1} + ε(1−h) − z L; receptors r_{i,t} = (1−ω_t)z_{i,t} + ν(1−h_{i,t}) + ξ_{i,t}; metabolic gain m(Ê) = Ê/(Ê+E₀); direct factor q(E) = E/(E+E_q); receptor gain log G_i(r) = a·r_i + (b+cη)Σ_j r_j; hunger η = m(E_sat) − m(Ê).

λ̇ decomposes EXACTLY into six terms (chain rule over the gains; verified numerically against direct finite-difference of log‖J_S‖, |diff| = 2.3e-9):
- d/dt log m — reserve signal — **felt**, diffuse
- d/dt log q — reserve acting directly — not felt
- a Σ_i w_i ṙ_i — local receptor gain — **felt**, localised (the only term that localises valence)
- (b+cη) Σ_j ṙ_j — global receptor gain — **felt**, diffuse
- Σ_i w_i d/dt log h_i — tissue — not felt
- Σ_i w_i d/dt log k_i — content — not felt

## Key results (Experiments 1–7, S1)

- **Alliesthesia (Exp 1):** same meal = larger Δλ at low reserve; intensity falls >10× from nearly-empty to full reserve (verified: 19.4× for ΔE=0.5, E₀=1). Reserve decay moves log m at rate κE₀/(E+E₀) — faster as E falls, never faster than the leak (verified: converges to analytic as step→0).
- **Negativity bias:** Z is a floor at −∞ with no ceiling; log scale is concave so a loss moves λ more than an equal gain (verified: 0.154 vs 0.105). Positive affect = relief scaled by need; negative affect anchored to a hard floor.
- **Hunger needs a signal (Exp 2):** actions cut → felt fall; signal blocked → reserve falls identically but v = 0 throughout (unfelt depletion accumulates); signal driven to half → immediate hunger, and the lowered gain cuts foraging so the reserve really falls (ungrounded feelings have real consequences through the loop).
- **Forecasts (Exp 3–4):** allostatic gain m(Ê) with Ê a fitted/learned τ-step forecast. Valence turns negative at the cue 5 steps before the drain; false cue → dread then relief while the reserve barely moves; delta-rule learning shifts valence to the cue (Schultz-dopamine analogue); the SAME forecast revision is felt more strongly the nearer Z (valence tracks motion relative to Z, not error size). Information (reassurance) moves valence with no reserve change.
- **Pain dissociations (Exp 5):** without receptors → zero valence under damage (congenital insensitivity; more tissue lost because withdrawal no longer tracks damage); without gain → nociception without affect (asymbolia); receptors driven with no damage → felt, no tissue loss (phantom). Tissue dimming its own activity moves the scale but is unfelt.
- **Learned feeling (Exp 6):** gain learned by gradient ascent on Σ_t log(m(E_t)‖h_t⊙k‖) (log scale with gain removed) learns a<0, b<0 (guard + rest): injuries hurt in proportion to repair cost, are felt at once, and less tissue is lost. "Damage matters to the whole body" is learned, not assumed.
- **Hunger suppresses pain (Exp 7):** with hunger routed into the global gain, the learner sets c>0 (cf. Alhadeff 2018 hypothalamic circuit): receptor-pain falls with hunger but total hurt is unchanged — the cost migrates from receptors to the reserve signal (deeper hunger); the body pays in tissue. With hunger unable to reach the gain, total hurt instead grows.
- **Wirehead (Exp 6b):** gain learned to maximise the log scale ITSELF (gain included) → injury feels good at first, then the reserve collapses (Goodhart's law: optimising the signal in place of the essential variables). Learning itself is felt only when driven by signals of what is at stake.
- **Metabolism as constraint (S1):** primal-dual policy under m ≥ m_min: valence ≈ 0 while the constraint is slack, several × larger and negative once it binds.

## Measuring valence

Jacobians are estimable by probing: evoked potentials, TMS response amplitude (Massimini/Casali perturbational complexity), pupil-linked neural gain. When motion is a gain, input and parameter Jacobians rescale together, so d/dt log(size of evoked response) ≈ λ̇; the felt part is isolated by blocking/driving a signal (as Exp 2). Claims are falsifiable: valence in a non-self-sustaining system, felt unsignalled damage, an "experience invert", or intensity not rising with |v| would all refute Hypothesis V.

## When to use

- Formalising affect/valence for agents or organisms without a generative model or stipulated set points — the reference is fixed by Jacobian structure.
- Designing homeostatic/allostatic agents and reward functions grounded in essential variables; predicting wireheading failure modes (reward = the signal vs what it signals).
- Explaining or simulating affect dissociations (anaesthesia vs neuromuscular block, lesion location vs size predicting affect change, deafferentation patterns).
- Analysing whether a machine system could have valence: check (1) self-sustaining? (2) internal inputs that its essential variables affect? (3) one subject (integrity > 0)?
- Neural coding work where gain modulation is the operative variable — valence here is precisely interoceptively-sourced gain dynamics.
