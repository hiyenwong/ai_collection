# Thermodynamics of Quantum Reservoir Computing (arXiv: 2607.02157)

## Paper Summary
Non-equilibrium thermodynamic framework linking macroscopic predictive performance of driven open quantum systems to microscopic energetic costs.

## Key Results

### 1. Holevo Capacity → BKM Manifold Mapping
- Maps Holevo information capacity onto Bogoliubov-Kubo-Mori geometric manifold
- Computational peak in quantum critical region originates from strict spectral resonance
- Closing energy gap forces reservoir transition frequencies to align with chaotic drive

### 2. Generalized Landauer Bound for Temporal Processing
- Introduces quantum informational dissipation: quantifies non-predictive historical data retained by reservoir
- Reveals fundamental trade-off: critical resonance maximizing predictive capacity ALSO maximizes informational dissipation and irreversible work

### 3. Coherence Decomposition
- Dynamic quantum coherences STRICTLY amplify predictive capacity
- WITHOUT demanding additional mechanical work
- This is a "free lunch" — coherence enhances computation without extra thermodynamic cost

## Design Implications
1. Operate near quantum critical point (energy gap → 0)
2. Maximize coherence utilization for free computational amplification
3. Minimize informational waste to reduce Landauer erasure cost
4. Accept the fundamental trade-off: optimal prediction = higher dissipation

## Mathematical Core
```
Holevo Capacity: χ = S(ρ) - Σ p_i S(ρ_i)
BKM Metric: g_BKM(A, B) = ∫₀¹ Tr(ρ^s A ρ^(1-s) B) ds
Landauer Bound: W ≥ kT · I_dissipated
Coherence: C(ρ) = S(ρ_diag) - S(ρ)
```
