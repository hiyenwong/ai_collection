---
name: bi-fork-bifurcating-systems
description: "Bi-FORK: Generative modeling of high-dimensional bifurcating systems via latent flow matching and repulsion-guided sampling. Recovers distinct solution branches in single amortized pass, scaling to 260,000 points."
tags: [bifurcation, generative-models, flow-matching, physical-systems, one-to-many, symmetry-breaking]
source: "arXiv:2610.12449"
utility_score: 0.86
---

# Bi-FORK: Generative Modeling of High-Dimensional Bifurcating Systems

## Paper Metadata

- **arXiv ID**: 2610.12449
- **Title**: Bi-FORK: Generative Modeling of High-Dimensional Bifurcating Systems
- **Authors**: Anna Zimmel, Fleur Hendriks, Markus Holzleitner, Florian Sestak, Martin Weichselbaumer, Vlado Menkovski, Johannes Brandstetter
- **Published**: 2026-10-08
- **Categories**: cs.LG, cs.AI, cs.CE, physics.comp-ph
- **Link**: https://arxiv.org/abs/2610.12449

## Abstract Summary

Bifurcations are ubiquitous in physical systems, from structural buckling to fluid and climate dynamics, yet they remain largely unexplored in deep learning. At a symmetry-breaking bifurcation, a single input admits multiple equally valid solutions, violating the one-to-one assumption underlying most learned physical surrogates. Bi-FORK is a generative framework for learning these one-to-many solution maps in high-dimensional systems. Bi-FORK generates complete trajectories through latent flow matching, preserving space and time coherence, and uses repulsion-guided sampling to recover distinct solution branches in a single amortized pass. Bi-FORK is evaluated on buckling beams, mechanical metamaterials, and Allen-Cahn phase separation, spanning continuous, discrete, and field-valued bifurcations with discretizations up to 260,000 points. Bi-FORK recovers the multimodal solution structure while scaling several orders of magnitude beyond prior approaches.

## Key Contributions

1. **Bifurcation modeling**: First deep learning framework for high-dimensional bifurcating systems
2. **One-to-many maps**: Handles symmetry-breaking bifurcations where single input has multiple valid solutions
3. **Latent flow matching**: Generates complete trajectories preserving space and time coherence
4. **Repulsion-guided sampling**: Recovers distinct solution branches in single amortized pass
5. **Extreme scale**: Works with discretizations up to 260,000 points, orders of magnitude beyond prior work

## Research Implications

- **Physical surrogates**: Opens generative modeling to high-dimensional bifurcating physical systems
- **Beyond one-to-one**: Challenges assumption that physical surrogates must be one-to-one mappings
- **Multimodal solutions**: Captures full multimodal solution structure, not just mean behavior
- **Scalability**: Demonstrates feasibility of generative models at extreme discretization scales
- **Cross-domain applicability**: Works across continuous, discrete, and field-valued bifurcations

## Practical Applications

- Model structural buckling in engineering design
- Simulate phase separation in materials science
- Predict bifurcation behavior in fluid dynamics
- Generate multiple plausible outcomes for climate models
- Build surrogate models for mechanical metamaterials

## Related Work

- Generative models for physics
- Flow matching
- Neural surrogates for PDEs
- Bifurcation theory
- Uncertainty quantification in physical systems
