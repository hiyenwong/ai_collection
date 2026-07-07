---
name: exclusion-statistics-quantum-heat-engines
description: "Exclusion statistics as a thermodynamic resource in quantum heat engines — using particle statistics interpolation (fermion/boson/anyon) as a design parameter for quantum thermal machines. From arXiv:2606.19310."
metadata:
  arxiv_id: "2606.19310"
  published: "2026-06-17"
  authors: "Sampurna Karmakar, Aziz Hasan, Sourin Das"
---

# Exclusion Statistics as Thermodynamic Resource

## Core Concept

Particle statistics (fermionic, bosonic, anyonic) are not just fundamental properties — they are **tunable thermodynamic resources** for quantum heat engines. The maximum power extractable from a quantum thermoelectric heat engine depends on the statistics of the working medium.

## Key Results

### Fermion Power Bound (Whitney Limit)

For free fermion carriers:
```
P_fermion^max ≈ 0.0321 π² kB² (TL-TR)² / h
```

### Bosonic Enhancement

Within the nonlinear Landauer-Büttiker framework, a bosonic working medium yields:
```
P_boson^max = (π²/6) · P_fermion^max
```
This is a **~5.1x enhancement** over the fermionic Whitney limit.

### Anyonic Interpolation

Anyons interpolate between fermionic and bosonic statistics, providing a **continuously tunable parameter** (exclusion parameter g ∈ [0,1]) for optimizing heat engine performance between the fermionic and bosonic bounds.

## Methodology

### 1. Identify the Statistical Regime
- Determine the effective exclusion parameter g of the working medium
- g=0 → bosonic, g=1 → fermionic, 0<g<1 → anyonic

### 2. Apply Landauer-Büttiker Framework
- Use nonlinear Landauer-Büttiker formalism for transport
- Account for quantum statistics in the occupation functions
- Calculate transmission coefficients for the heat engine

### 3. Optimize Power Output
- The Whitney limit is NOT fundamental — it is an artifact of fermionic statistics
- Bosonic or anyonic working media can exceed this bound
- Tune the exclusion parameter to maximize power for given temperature gradient

## Usage Patterns

### Pattern 1: Statistical Advantage Analysis
When analyzing quantum thermal devices:
1. Check if the working medium has tunable statistics (e.g., in cold atom systems, fractional quantum Hall systems)
2. Calculate the theoretical power bound for each statistical regime
3. Design the engine to operate in the most advantageous statistical regime

### Pattern 2: Anyonic Engine Design
For engines with anyonic working media:
1. Identify the exclusion parameter g of the quasiparticles
2. Use interpolation formulas between fermionic and bosonic limits
3. Account for the generalized Pauli exclusion principle in transport calculations

## Pitfalls

### Whitney Limit is NOT Fundamental
- The Whitney limit (0.0321π²kB²ΔT²/h) applies ONLY to fermionic carriers
- Using bosonic or anyonic media can significantly exceed this bound
- Do not treat this as a universal quantum heat engine limit

### Linear vs Nonlinear Regime
- Results depend on the nonlinear Landauer-Büttiker framework
- Linear response theory may not capture the full statistical advantage
- Use nonlinear transport for accurate power estimates

## Activation
- exclusion statistics, quantum heat engine, Whitney limit, Landauer-Büttiker
- 量子热机, 排除统计, 玻色子增强
- quantum thermodynamics, anyonic statistics, bosonic enhancement
