# Witness Expansion Framework (arXiv: 2606.27105, June 2026)

## Paper Summary
Tang et al. propose "Witness Expansion" — a unified framework for constructing nonlinear criteria for detecting quantum resources in mixed states. Works for coherence, entanglement, nonstabilizerness (magic), and fermionic non-Gaussianity.

## Key Results

### Framework Construction
- For any resource with free unitary group $\mathcal{U}$, construct polynomial moments $p_k(\rho) = \text{Tr}(\rho^{\otimes k} W_k)$
- Moments estimated via multi-copy measurements (SWAP tests, Bell measurements, classical shadows)
- Nonlinear witnesses detect resources that linear witnesses miss entirely

### Recovered Known Quantities
| Resource | Witness | Measurement |
|----------|---------|-------------|
| Coherence | $l_2$ norm | $\text{Tr}(\rho^2) - \sum_i \langle i|\rho|i\rangle^2$ |
| Entanglement | Partial-transpose moments | $\text{Tr}((\rho^{T_A})^k)$ |
| Magic | Stabilizer entropy | $\text{Tr}(\rho \Pi_{\text{stab}})$ |
| Fermionic Non-Gaussianity | Fermionic antiflatness | Polynomial in fermionic correlators |

### New Contributions
1. Enhanced witness criteria for qubit and qudit magic states
2. **First analytical criterion** for mixed-state fermionic non-Gaussianity wrt convex hull of pure Gaussian states, nontrivial for arbitrary qubit numbers

## Implementation Notes
- Experimental: use multi-copy measurements, no full tomography
- Scalable: detection criteria remain efficient as system size grows
- Application: quantum device benchmarking, phase transition detection, advantage certification

## Activation
witness expansion, quantum resource detection, mixed-state resource, stabilizer entropy, nonstabilizerness, fermionic non-Gaussianity
