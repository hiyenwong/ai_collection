---
name: harmonic-theory-behavior
description: First-principles theory deriving individual and collective behavior from neural ring-manifold representations via harmonic decomposition. Use for collective behavior without ad hoc rules.
category: neuroscience
tags: [neuroscience, collective-behavior, neural-manifold, ring-attractor, harmonic-decomposition, self-organization, decision-landscape, coarse-graining]
version: 1.0
arxiv: 2609.33896
date: 2026-09-27
trigger: collective behavior, flocking, swarming, milling, fission-fusion, ring attractor, heading direction, decision landscape, effective Hamiltonian, spatial decision-making, coarse-graining neural dynamics, harmonic modes, parity principle
---

# Harmonic Theory of Behavior

## Overview

First-principles framework (Salahshour & Couzin, Max Planck Institute of Animal Behavior / U Konstanz) deriving **movement, decision-making, and collective organization** by coarse-graining fast neural dynamics on a topological representation (ring manifold S¹) of directional space. Behavior emerges from a **spectral (harmonic) organization of directional information** rather than prescribed interaction rules — unifying neural representations, behavioral decisions, and collective dynamics in a single mathematical description.

**arXiv**: [2609.33896](https://arxiv.org/abs/2609.33896) (physics.bio-ph, 27 Sep 2026)
**Authors**: Mohammad Salahshour, Iain D. Couzin

## Core Idea

Rule-based collective-motion models (Vicsek, Couzin zones, Cucker-Smale) treat the heading vector as the fundamental dynamical variable and impose interaction rules — leaving the link between **neural representations of space and behavior** outside the theory (and circular: rules are assumed, not explained).

Harmonic Theory replaces the rule catalogue with: **organisms represent spatial information on structured neural manifolds (ring topology S¹ for heading), and behavior emerges from how that representation is processed.**

## Four Axioms

1. **Additive sensory integration**: sensory inputs sum post-synaptically (standard neural integration)
2. **Topological manifold representation**: directional space mapped onto a ring manifold (S¹ ≅ R/2πZ) — consistent with empirically observed ring/toroidal/grid manifolds and continuous-attractor orientation coding
3. **Bump-state decisions**: current heading = localized activity bump on the ring, with center φ(a) (heading) and width W (decision uncertainty — narrow = precise, wide = uncertain)
4. **Timescale separation**: neural bump-shape dynamics fast vs. behavioral change → eliminate fast variables (non-equilibrium statistical mechanics style coarse-graining)

## The Effective Hamiltonian

Coarse-graining yields a **decision landscape** (Hamiltonian) over directions admitting harmonic decomposition:

```
H_eff = − Σ_a Σ_t Σ_{n=1}^∞ K_nt(d_at) cos(n(φ(a) − T(a,t)))      (individual–environment)
        − Σ_{a≠b} Σ_{n=1}^∞ K_n(d_ab) cos(n(φ(a) − T(a,b)))       (pairwise social)
```

φ(a) = agent heading; T(a,t)/T(a,b) = allocentric bearings to target t / agent b; d = distances. Social and asocial interactions share identical harmonic structure — social perception is just "conspecifics as stimuli".

### Coupling Coefficient Factorization

```
K_n(d) = J_int(d) · c_n(σ) · M_n(W)
```

Three biologically meaningful filters:

| Factor | Formula | Meaning |
|--------|---------|---------|
| **J_int(d)** | e.g. h, h·e^{−d/ξ}, or long-range attraction + short-range repulsion (h_coll < 0 for d < r_coll) | ecological interaction kernel: sign/strength/distance-decay of influence |
| **c_n(σ)** = (1/π)·exp(−n²σ²/2) | Gaussian sensory kernel Fourier coefficient | sensory filter: large σ smooths fine detail → attenuates high harmonics |
| **M_n(W)** = (4/(nπ))·sin(nW/2) | square-bump integration coefficient | decision filter: oscillatory in bump width W — can enhance, suppress, or REVERSE harmonic contributions |

**Behavior = weighted superposition of harmonic modes**, weights predictable from ecological attenuation (J), perceptual filtering (σ), and internal integration (W).

## Individual-Level Phenomenology

- **n=1 (first harmonic)**: direct approach (attractive) / direct escape (repulsive); W-independent preferred headings for 0 < W < π
- **n=2**: alignment with target bearing — approach and escape both minima; for aversive: perpendicular headings
- **n-th harmonic**: n minima at fixed bearing
- **Sign reversal** (h < 0): repulsive stimulus rotates fixed-bearing minima by π/n
- **Small σ** (high harmonics survive): spiral approach interrupted by direct escape; late "decision point" for aversive targets (approach then turn away)
- **Large σ** (first harmonic dominates): direct approach + back-and-forth oscillation near target; early decision for aversive
- **Higher-harmonic sign flips with W**: same trajectory can arise from attractive stimulus at one bump width and repulsive at another — high harmonics alone don't encode attraction/aversion
- **Noise facilitates** target reaching and avoidance when higher harmonics dominate
- **Harmonic Theory of Bifurcations**: back-and-forth motion = spatial, distance-dependent bifurcations alternating stability of approach/escape

### Binary Choice (two equal targets)

Potential on the symmetry axis:
```
U(φ; y) = −2 Σ_n K_n cos(nΔ(y)/2) cos(n(φ − π/2))
```
- Symmetric averaging trajectory φ = π/2 is an extremum for all n; stability governed by **K_n cos(nΔ(y)/2)**
- First harmonic: cosine always positive → stable averaging, **no choice ever occurs**
- Higher harmonics: cosine alternates sign as angular separation Δ(y) grows on approach → **bifurcation from averaging to choice** at critical separation where coefficient crosses zero
- Explains empirical bifurcation data: animals average at large distances, suddenly commit to one target as separation grows

## Collective-Level Phenomenology: Parity Principle

Physical exchange of agents reverses bearings (T → T + π). Harmonic response depends on **mode parity**:

- **Odd harmonics**: cos(n(x+π)) = −cos(nx) → phase-shifted (π/n) preferred headings → **conflict/separation modes** — rotational milling, fission-fusion dynamics, opposition
- **Even harmonics**: cos(n(x+π)) = +cos(nx) → identical potentials for both agents → **consensus modes** — synchronization, ordered motion

Pair configurations: n-th harmonic admits n minima per agent, n² joint fixed-bearing configurations. Collective phenomenology arises from modulating the harmonic spectrum:

| Phenomenon | Harmonic driver |
|------------|------------------|
| Ordered motion / alignment | dominant even harmonics |
| Synchronization / consensus | even harmonics |
| Rotational milling | odd harmonics |
| Fission-fusion | odd/even modulation balance |

## Validation

- **Dual derivation**: axiomatic (general assumptions) AND mechanistic (explicit microscopic neural models — spin system + neural-field model — coarse-grained)
- **Agent-based models**: neural ring-attractor implementations reproduce target-seeking, avoidance, choice bifurcations, and collective modes
- Tracking-error formalism: transform to ψ = φ(a) − T(a,t) for nullcline/bifurcation analysis of moving trajectories

## Use When

- Modeling collective behavior WITHOUT imposing ad hoc interaction rules
- Deriving behavioral rules from neural manifold representations (ring/toroidal/grid)
- Analyzing spatial decision-making bifurcations (averaging → choice)
- Explaining/predicting collective modes (milling, fission-fusion) from perceptual parameters
- Bridging neuroscience of perception and ecology of behavior
- Robotic/swarm control derived from neurobiological principles

## Limitations

- Ring manifold S¹ covers 2D directional space — 3D orientation requires toroidal/higher-dimensional manifolds
- Coarse-graining assumes fast bump dynamics (timescale separation)
- Linear environmental coupling axiom

## Related Skills

- `frustrated-neurons-phase-oscillators` — geometric frustration in neural phase dynamics
- `kuramoto-brain-network` — Kuramoto phase dynamics for brain networks
- `heterophily-synergistic-interdependencies` — self-organized structures from heterophily
- `neural-fields-world-models` — neural fields as world models

## References

- Salahshour & Couzin (2026). "Harmonic Theory of Behavior." arXiv:2609.33896
- Couzin et al. (2002). Collective memory and spatial sorting in animal groups
- Wilson & Cowan / continuous-attractor ring networks (bump-based heading coding)
- Anderson (1972). "More Is Different" — the order paradigm this theory extends beyond
