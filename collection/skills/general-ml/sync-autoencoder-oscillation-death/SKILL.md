---
name: sync-autoencoder-oscillation-death
description: "Sync-theoretic autoencoder for oscillation death analysis."
category: ai_collection
trigger: synchronization-theoretic autoencoder, oscillation death, oscillation quenching, coupled Stuart-Landau identification, phase reduction, limit-cycle coordinate transformation, vortex suppression prediction, linear stability analysis latent space, coupled oscillator data-driven modeling, amplitude death neural oscillators
---

# Synchronization-Theoretic Autoencoder: Oscillation Death from Data

**Source**: Ushida, Beppu, Kato & Fukami, "Studying oscillation death in two-dimensional cylinder-airfoil interactions with synchronization-theoretic autoencoder" (arXiv:2610.05762, physics.flu-dyn/nlin.AO, Oct 2026, Tohoku Univ.)
Code: https://github.com/kfukami/Synch_AE

## Core Thesis

High-dimensional interacting systems (here: cylinder + NACA0012 airfoil wakes at Re=100) can show **oscillation death** — both oscillators quenched by diffusive coupling. To predict it from data, transform each body's observable (lift coefficient C_L and its time derivative) into a latent space where the **isolated dynamics lie on a unit circle** (Stuart-Landau-compatible), using an autoencoder whose loss functions directly encode synchronization-theoretic structure. Then identify a **pair of coupled Stuart-Landau ODEs**, read the coupling matrices T_c, T_w, and run **linear stability analysis in latent space** — the eigenvalue's real part approaching zero flags oscillation death. Coupling appears as ellipse deformation from the isolated unit circle, and ‖T‖ quantifies interaction magnitude in an interpretable form.

## Pipeline (reusable recipe)

1. **Parametric sweep + regime map**: DNS over (Δx, Δy, α) parameter space; classify 4 observed regimes — weak shedding / **suppression** (target) / shedding-with-feedback / shedding-from-both. Frequency spectra (FFT) + DMD modes locate the suppression sweet spot (here α=30°, Δx=3, Δy≈0: dominant and secondary spectral peaks both vanish; DMD inter-body mode weakens).
2. **Per-body sync autoencoder**: encoder f_enc: R^d → R² maps the observable to a 2D latent ξ; decoder f_dec reconstructs. Two separate AEs per body (their trajectory complexity differs — cylinder circle-like, airfoil skewed/squished in phase space).
3. **Structure-constrained latent dynamics**: require ξ_{t+τ} = R(θ)S r(ωτ) S⁻¹R(θ)⁻¹(ξ_t − ξ̄) + ξ̄ where r(ωτ) is rotation at learnable frequency ω, S=diag(a,b) allows ellipse axes, R(θ) allows tilt; ‖S⁻¹R(θ)⁻¹ξ‖₂=1 projects onto unit circle. Isolated case: fix θ=0, a=b=1, learn only ω.
4. **Four-loss training** (weights (w_recon, w_shape, w_dyn, w_mass) = (1, 0.1, 0.1, 1e-2) cylinder / (1, 10, 1e-2, 1e-2) airfoil):
   - L_recon: input reconstruction (Frobenius, RMS over orbit)
   - L_shape: Σᵢ[(R S D_t)ᵢ² − 1] — forces transformed latent onto the unit circle
   - L_dyn: ‖f_enc(D_{t+Δt}) − r(ωΔt)S⁻¹R⁻¹f_enc(D_t)‖ — one-step latent rotation at learned ω (Δt=0.2, scaled to cycle period)
   - L_mass: Σᵢξᵢ² — pins ellipse center to origin. **Critical pitfall caught by this loss**: without it, L_shape has a local solution with off-origin ellipse center, which injects a nonphysical constant term into the identified coupling (exponential latent growth).
5. **Identify coupled Stuart-Landau** in latent coordinates: ξ̇_c = f_c(ξ_c) + T_c ξ_w; ξ̇_w = f_w(ξ_w) + T_w ξ_c, where f is the SL cubic nonlinearity ξ̇ = ξ − dξ⊥ − ‖ξ‖²(ξ − βξ⊥). Isolated eigenvalues 1.00±1.31i (cylinder), 1.00±2.03i (airfoil) recovered from data.
6. **Linear stability + coupling diagnosis**: eigenvalues of the identified coupled system on the Gaussian plane; near-zero real part = oscillation death. ‖T_c‖₂, ‖T_w‖₂ vs parameter (α) give interpretable coupling-magnitude curves.

## Key Findings (what the analysis revealed)
- Oscillation death at α=30° (Δx=3, Δy=0): eigenvalue real part → ~0; one other eigenvalue shows **stronger instability** at α=30° than higher α — hints at additional solutions (matches Mizushima & Suehiro 2005 multiple-solutions report).
- ‖T_w‖ (cylinder→airfoil coupling) peaks at α=30° (suppression) then decays; ‖T_c‖ (airfoil→cylinder feedback) grows with α. α=40° is a transitional state: eigenvalue real part turns back toward zero after rising.
- Latent interaction magnitude ∝ time-averaged lift for the cylinder, but NOT for the airfoil — ellipse shape/position encode the difference from isolated flow, not the raw fluctuation amplitude.
- Suppression mechanism (DMD): balance between leading-edge bluff structure and the inter-body modal structure at St≈0.13; small leading-edge structures at St≈0.26 vanish at α=30°.

## When to Apply / Integration Patterns

- **Any two (or few) coupled self-sustained oscillators observed through scalar/paired observables**: wake-body aeroelastic interactions, coupled neuron populations, VCO arrays, power-grid swing equations, biochemical oscillators (repressilators). The recipe only needs periodic (limit-cycle) data per unit + their interaction variants.
- **Predicting quenching regimes without full simulations**: after identification, sweep coupling matrices T and do linear stability offline — cheap parametric screening for suppression/optimal-placement (here: optimal airfoil placement to suppress shedding; analogously optimal stimulation to quench pathological oscillations).
- **Phase-reduction successor**: extends phase-autoencoder phase-reduction work (Cenedese/Kato-style) by keeping amplitude structure (ellipse deformation) so coupling strength is readable, not just phase.
- **Diagnostic reading**: coupling norm curves vs parameter = interpretable interaction map; eigenvalue trajectory on Gaussian plane = regime atlas (suppression / transition / decoupled).

## Pitfalls

- **Off-origin ellipse local solution** — always include the center-of-mass loss L_mass; a constant coupling term otherwise masquerades as physical interaction.
- Observable must actually live on (or near) a limit cycle; quasi-periodic or transient data breaks the unit-circle constraint (regime classification FIRST).
- Per-body AE weights are not interchangeable — trajectory geometry differs per unit (cylinder vs airfoil); re-tune w_shape/w_dyn per body.
- Identified eigenvalues are in the LATENT Stuart-Landau coordinates — quantitative claims about physical stability need the coordinate map made explicit.
- DMD/FFT regime map is the grounding step; skipping it risks "identifying" a model for a regime where the assumption (periodicity) fails.

## Related Skills

- `stuart-landau-oscillatory-gnn` — SL oscillator dynamics used as GNN ARCHITECTURE (inverse direction: this skill uses SL as analysis target)
- `izhikevich-weak-coupling-phase-model` — weak-coupling phase reduction for neuron synchronization
- `phase-model-m-current-hippocampal-synchrony` — phase-model neural synchrony analysis
- `bipartite-oscillator-synchronization` — synchronization mode analysis of E/I oscillator networks
