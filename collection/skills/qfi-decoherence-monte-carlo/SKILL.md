---
name: qfi-decoherence-monte-carlo
description: "Quantum Fisher Information estimation under decoherence using Monte Carlo sampling of wavefunction-derived probability distributions. Maps QFI lower bounds to classical expectation values for efficient estimation beyond exact diagonalization. Use when: (1) estimating QFI of noisy quantum states, (2) analyzing metrological content of many-body systems, (3) evaluating entanglement under noise, (4) benchmarking quantum sensors, (5) studying open quantum system metrology."
metadata:
  arxiv_id: "2605.22917"
  published: "2026-05-21"
  authors: "Francesco Musso, Vittorio Vitale, Sara Murciano"
  tags: [quantum, fisher-information, decoherence, metrology, monte-carlo, many-body]
---

# QFI Estimation Under Decoherence via Monte Carlo

## Description

Method for estimating Quantum Fisher Information (QFI) of many-body quantum states under decoherence using Monte Carlo sampling of wavefunction-derived classical probability distributions.

## Core Problem

Direct QFI evaluation requires full spectral resolution of the density matrix, which is intractable for large systems under decoherence.

## Methodology

### Wavefunction-to-Probability Mapping

For many-body wavefunctions known analytically in the occupation-number basis:
- Map QFI lower bounds to expectation values over a classical probability distribution
- Distribution defined by wavefunction amplitudes squared
- Enables efficient estimation via Markov-chain Monte Carlo

### Computational Scaling

- Scales as "slow" exponential: e^(bL) with b ≲ 0.6
- Manageable for system sizes well beyond exact diagonalization
- Polynomial and Krylov-based lower bounds available

### Noise Channel Analysis

Framework handles three physically motivated noise channels:
1. **Local dephasing**: Phase coherence loss at individual sites
2. **Local amplitude damping**: Energy relaxation at individual sites
3. **Global depolarizing**: Uniform noise across the system

### Jastrow-Gutzwiller Wavefunctions

Framework specifically applied to Jastrow-Gutzwiller wavefunctions:
- Identify observables that maximize QFI
- Characterize scaling with system size L
- Compare polynomial vs Krylov-based bounds

## When to Use

- Estimating QFI of noisy many-body states
- Quantum metrology benchmarking under realistic noise
- Entanglement detection in open quantum systems
- Sensor performance analysis with decoherence
- Scaling analysis of quantum advantage in metrology

## Verification Steps

1. Confirm wavefunction is known in occupation-number basis
2. Verify probability distribution sums to 1
3. Check MCMC convergence for expectation values
4. Compare polynomial and Krylov bounds for consistency
5. Validate against exact results for small system sizes

## Error Handling

### MCMC Not Converging
Increase sample count or use Krylov-based bounds as alternative.

### Wavefunction Not Analytic
Framework requires analytic wavefunctions in occupation-number basis. Use numerical methods or variational approaches.

### Noise Model Unknown
Test across all three standard noise channels (dephasing, amplitude damping, depolarizing) and compare results.

## Resources

- arXiv: 2605.22917
- Categories: quant-ph; cond-mat.stat-mech
