# Quantum-Analogue Cloud-Function Formalism — Session Notes (2026-05-27)

## Source
arXiv:2605.25214 — "A Quantum-Analogue Formalism for Modeling Supraliminal Information Processing"
Authors: Vasily Lubashevskiy, Ihor Lubashevsky
Institutions: Tokyo International University, HSE University
Category: q-bio.NC

## Key Mathematical Structure

### Cloud Function
ψ(x,t) = Σ_k c_k(t) · φ_k(x)
- φ_k(x): connectome harmonic modes (eigenmodes of brain structural connectivity Laplacian)
- c_k(t): time-varying complex coefficients

### Governing Equation
i·∂ψ/∂t = Ĥ·ψ
where Ĥ includes:
1. Neural field operator with polynomial nonlinearities
2. Non-Hermitian terms (gain/loss → excitation/inhibition)
3. Lotka-Volterra competition terms
4. Global phase-shift invariance constraint

### Lotka-Volterra Competition
∂n_i/∂t = n_i · (r_i - Σ_j α_ij · n_j)
n_i = |ψ_i|² (population density)
r_i = intrinsic growth rate
α_ij = competitive inhibition between populations

### Physical Interpretation
- Non-Hermitian ≠ quantum: represents open system dynamics (energy input/dissipation)
- Phase-shift invariance: only relative phases matter, matching neural oscillation empirics
- "Quantum-analogue" = mathematical structure mirrors QM, but describes classical neural fields

## Application: Change-of-Mind Decision Making
- Fast preconscious processing → initial choice
- Slower conscious comparison → alternative evaluation
- Continuous post-decisional evidence accumulation
- Revision mechanism explains why initial choices can be reversed during execution

## Search Discovery Path
- Discovered via: browser_navigate → arxiv.org/list/q-bio.NC/recent
- Filtered titles for quantum/medicine/bio keywords
- This paper appeared with title: "A Quantum-Analogue Formalism for Modeling Supraliminal Information Processing"
- NOT found via keyword search "quantum medical OR quantum healthcare" (arXiv search returned no results for some queries)
- Category listing browsing was the only reliable discovery method

## Skill Created
`quantum-analogue-supraliminal-processing` — full methodology with implementation guidelines, pitfalls, and activation keywords.
