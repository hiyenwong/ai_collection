---
name: nonstabilizerness-diffusive-dynamics
description: "Diffusive dynamics of nonstabilizerness methodology — computing stabilizer Rényi entropies and analyzing symmetry effects on magic state dynamics in many-body quantum systems. Covers the resource complementary to entanglement."
category: "quantum-physics"
metadata:
  arxiv_id: "2606.13606"
  published_date: "2026-06-12"
---

## Context

In quantum information theory, "nonstabilizerness" (or "magic") is the resource complementary to entanglement that enables universal quantum computation beyond Clifford gates. Stabilizer states can be efficiently classically simulated; nonstabilizer states provide the computational advantage. This paper studies how nonstabilizerness diffuses in many-body quantum systems and how symmetries shape this dynamics.

## Core Methodology

1. **Stabilizer Rényi Entropy (SRE)**: Define the SRE as M_n(ψ) = -log(∑_P |⟨ψ|P|ψ⟩|^{2n} / 2^N) where P runs over all N-qubit Pauli strings. This quantifies how far a state is from the stabilizer manifold.

2. **Diffusive Dynamics Model**: Under random Clifford dynamics, nonstabilizerness spreads diffusively through the system. The diffusion coefficient depends on the circuit architecture and gate set.

3. **Symmetry Effects**: Global symmetries (e.g., U(1), Z_2) constrain the diffusion of nonstabilizerness. Symmetric sectors may have different diffusion rates, leading to sector-dependent magic dynamics.

4. **Stabilizer 2-Rényi Entropy**: The n=2 case is most tractable: M_2(ψ) = -log(∑_P |⟨ψ|P|ψ⟩|^4 / 2^N). This can be computed using stabilizer decomposition techniques.

## Implementation Steps

1. Compute the Pauli string expectation values ⟨ψ|P|ψ⟩ for the state of interest
2. Calculate the stabilizer Rényi entropy M_n from the Pauli spectrum
3. For many-body systems, use tensor network methods to compute SRE efficiently
4. Analyze the spatial profile of SRE to extract diffusion coefficients
5. Study symmetry sectors separately to identify sector-dependent diffusion rates
6. Compare with entanglement entropy dynamics to understand the interplay

## Key Results

- Nonstabilizerness spreads diffusively under random Clifford circuits, analogous to entanglement spreading
- Symmetries can suppress or enhance magic diffusion in specific sectors
- The diffusion coefficient for magic is generally different from the entanglement diffusion coefficient
- Magic states can be generated and manipulated through controlled diffusion processes

## Pitfalls

- **Computational Cost**: Computing SRE requires summing over all 4^N Pauli strings — use randomized estimation or tensor network approximations for large systems.
- **Stabilizer Decomposition**: Not all states have efficient stabilizer decompositions; the stabilizer rank can grow exponentially.
- **Symmetry Breaking**: Spontaneous symmetry breaking can create domain walls that block magic diffusion.
- **Circuit Depth**: Diffusive behavior emerges only at sufficient circuit depth; shallow circuits show ballistic behavior.

## Verification

1. Verify SRE = 0 for stabilizer states (by definition)
2. Verify SRE scales extensively for Haar-random states
3. Check that diffusion coefficient matches theoretical predictions for random Clifford circuits
4. Compare symmetry-resolved diffusion rates against group-theoretic predictions

## Activation

nonstabilizerness, magic states, stabilizer renyi entropy, quantum resource theory, clifford circuits, quantum computation beyond clifford, diffusive dynamics, many-body quantum systems, symmetry-protected dynamics
