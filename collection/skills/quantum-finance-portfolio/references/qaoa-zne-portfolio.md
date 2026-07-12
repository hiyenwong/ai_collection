# QAOA+ZNE for Multi-Objective Portfolio Optimization — Hardware Guide

Source: arXiv:2602.09047 (Hugo José Ribeiro, 2026-02-13)

## Problem Setup

- **Variables**: 88 binary (asset/project selection)
- **Objectives**: Carbon sequestration + biodiversity connectivity + social impact
- **Constraints**: Cardinality (fixed number of selections), budget limits
- **Encoding**: Multi-objective QUBO → Ising Hamiltonian

## QAOA Circuit

|0⟩^n → H^{⊗n} → [U_C(γ) · U_M(β)]^p → Measure

- U_C(γ): e^{-iγH_C} encodes portfolio objective
- U_M(β): e^{-iβH_M} explores solution space (X-mixer)
- Depth p: 1-2 for NISQ hardware

## ZNE Implementation

### Step 1: Noise Scaling via Gate Folding

Replace gate G with G·G†·G to triple effective noise.
Scale factors: λ = {1, 2, 3, 5}

### Step 2: Multi-Level Measurement

Run QAOA circuit at each noise level λ_i.
Collect expectation values E(λ_i) for each λ.

### Step 3: Richardson Extrapolation

Fit polynomial through (λ_i, E(λ_i)) points.
Extrapolate to λ=0: E(0) ≈ Σ_i c_i · E(λ_i)

Richardson coefficients for λ={1,2,3}:
c = [3, -3, 1] (linear extrapolation)

### Step 4: Classical Optimization Loop

for iteration in range(max_iters):
    expectation = run_qaoa_zne(θ, noise_levels=[1,2,3])
    θ = optimizer.step(expectation, θ)

## Key Results

- QAOA+ZNE on IBM hardware outperforms classical greedy baseline
- ZNE is essential — raw QAOA results degraded by hardware noise
- 88-variable problem with 3 objectives

## Hardware Tips

- Use Qiskit Runtime for efficient ZNE execution
- Start with p=1 on real hardware due to coherence limits
- ZNE shot budget: 3-5× normal (multiply by number of noise levels)
- Consider constraint-native encoding vs penalty terms
