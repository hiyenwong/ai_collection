---
name: modular-rbm-hopfield-dual-classification
description: "Modular RBMs with coupled hidden layers classify and disentangle pattern mixtures."
category: ai_collection
trigger: modular restricted Boltzmann machine, HM-RBM duality, coupled hidden layers, anti-Hebbian competition, supervised contrastive divergence, planted weights fixed point, pattern disentanglement classification, mixture classification RBM, class-wise empirical mean initialization, memristor Boltzmann machines
---

# Classifications in Modular Restricted Boltzmann Machines

**Source**: Agliari, Lepre, Roscani (Sapienza Roma / CNR-Nanotec), arXiv:2610.08612 (6 Oct 2026), cond-mat.dis-nn / stat.ML.

## Core Idea

The HM–RBM duality (Hopfield model ≡ restricted Boltzmann machine under mild conditions) extended to the **modular** setting: L Hopfield modules with intra-module Hebbian + inter-module anti-Hebbian couplings map to an assembly of **L RBMs whose hidden layers are coupled**. The central question: is the weight configuration suggested by the duality one that *learning actually reaches*, or only one a theorist plants by hand? Answer (Theorem 1): for simple classification, the **class-wise empirical-mean weights η̄ are a fixed point in mean of one-step supervised contrastive divergence (CD-1)**, for ANY number of modules L, with an explicit non-asymptotic bound on residual drift. For hard classification (mixture inputs), the same planted weights still work across the theoretically predicted disentanglement region.

## Architecture

- L modules of N binary visible neurons; K archetypes ξ^µ stored per class-tuple.
- Equivalent RBM: visible layer a ↔ module a; hidden units z^µ_a (one per archetype) with **inter-module coupling g_ab**: hidden clamp `ẑ^µ_a = δ_µµ_a − λ Σ_{c≠a} δ_µµ_c` (a Hebb-anti-Hebb structure: own label excites, other modules' labels inhibit).
- Coupling matrix g must stay positive-definite; margin condition **λ(L−1) < 1** simultaneously guarantees (i) positive field margin at reconstruction, (ii) g > 0, (iii) stationarity of the learning rule.
- Supervised hypothesis used in full: the label is not an O(1) perturbation of a sampled hidden state — it IS the hidden state at its own scale.

## Supervised CD-1 (Algorithm 1)

1. **Planted init**: `w_iµ,a ← η̄_i^µ = (1/M)Σ_m η̂_i^{µ,m}` (empirical mean over M noisy examples per archetype; shared across modules a) — or random Gaussian for the attractor test.
2. **Positive phase**: visible clamped to majority-vote cue `s_i^µa(B_µa) = sign(Σ_m∈B η̂_i^{µ,m})` over odd batch B; hidden clamped per the supervised rule above.
3. **Reconstruction**: sample visible `P(σ|z)` via local field `h_i = N^{-1/2}Σ_µ w_iµ,a ẑ^µ_a`.
4. **Negative phase**: resample hidden `P(z|σ)` with Gaussian noise ζ ~ N(0, β⁻¹g).
5. **Update**: `Δw_iµ,a ← (ϵβ/√N)[(σ_i^a)′ ẑ^µ_a − (σ_i^a)″ (z^µ_a)″]`.

## Theorem 1 (fixed point in mean, the quantitative core)

With archetypes' typical pairwise overlap O(N^{-1/2}), dataset entropy ρ, label examples ≥ B each:

`max E[Δw_iµ,a] ≤ ϵβ [ C·e^{−β(1−λ(L−1))² − c1/ρ} (thermal) + L·e^{−Br²/2} (mini-batch) + C′√(2 ln(2KLN)/N) (finite size) ]`

with probability ≥ 1 − 2KLN·e^{−Nγ²/2} over archetypes. **Four independent noise channels**:
1. **Thermal**: reconstruction flips; exponentially suppressed in β, margin shrinks by inter-module inhibition to 1 − λ(L−1) — stays positive iff λ(L−1) < 1.
2. **Dataset**: empirical archetype estimate points the wrong way; depends on data ONLY through entropy ρ; exponentially small once M·r² ≫ 1 (r = example-archetype overlap/quality).
3. **Mini-batch**: majority-vote cue mismatch; exponentially small in B·r².
4. **Finite-size**: accidental archetype overlaps; survives ALL limits (typical O(N^{-1/2}), uniform over KLN triples costs the log).

Corollary: E[Δw] → 0 as β,M,B,N → ∞ in any order (ln K = o(N)); η̄ is a fixed point in mean. Generalizes the single-RBM asymptotic result [Decelle et al.] in three ways: L coupled modules (inhibition via λ(L−1)), non-asymptotic bound, full supervised clamping.

## Numerical Verification

- Observable: `G = max E[Δw]/(ϵβ)` (drift stripped of learning rate and temperature — essential, else any lr makes it small). Channel-by-channel panels confirm: G falls exponentially in β (thermal), in 1/ρ (dataset), in B (mini-batch), each saturating on the N^{-1/2} finite-size plateau which orders curves by system size. Analytic closed-form of the three CD-1 averages matches direct simulation with Pearson r = 0.9999.
- **Attractor, not just fixed point**: cosine similarity during training — from zero init AND from random Gaussian inits of increasing variance, CD-1 drives weights toward η̄ (time-to-reach scales with init variance). Planted weights are interpretable AND reached by genuine learning dynamics.
- **Simple classification** (each module sees noisy examples of one archetype): planted weights solve it.
- **Hard classification** (EVERY module receives the same noisy mixture of all L archetypes): network must jointly classify and disentangle. Success region in the (ρ, λ) plane matches the modular-HM theory boundaries [mixture unstable ∩ disentangled stable]. Success = L modules end on L DISTINCT archetypes, checked via Hungarian-algorithm optimal assignment of module→archetype with activation threshold θ. Failure modes are visible in hidden activation histograms: stuck-in-mixture (low activation peak) vs. duplicate retrieval (two modules claim the same archetype).

## When to Use

- **Closed-form initialization for energy-based models**: replace trial-and-error RBM init with class-wise empirical means — proven stationary, no warm-up waste.
- **Physical/neuromorphic Boltzmann machines** (memristor-based): where weights are slow to reprogramme, starting AT the analytic solution matters far more than in software.
- **Compositional data classification** (chords, multi-concept images, multi-topic documents): coupled-hidden-layer RBM classifies AND disentangles in one relaxation, no explicit mixture model needed.
- Design rule of thumb: keep **λ(L−1) < 1** — inhibition strength × module count controls the margin, definiteness, and stationarity together.
- Open question flagged by authors: does CD-1 started from random coupling x converge to the antagonistic g by itself? ("Do cells asked to fire apart learn to stay apart?") — a self-organization test for anti-Hebbian emergence.

## Related (in collection)

- [[dense-auto-hetero-associative-disentanglement]] — same group's dense (high-order) version of the modular Hopfield architecture; this paper is the RBM-side dual with learning dynamics.
- [[energy-based-neurocomputation]] — broader EBMs; contrastive divergence listed as intractable-partition-function workaround; here CD-1 gets a provable planted fixed point.
- [[replica-fragmentation-glassy-parity-learning]] — companion statistical-mechanics-of-learning analysis using overlap observables (function-level), vs. this weight-level duality.
