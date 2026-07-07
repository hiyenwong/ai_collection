---
name: krylov-mean-field-chaos-rnn
description: "Krylov Mean-Field Chaos in Random Recurrent Networks - Deterministic prediction theory for individual trajectories in mean-field dynamics. Analytic nonlinearities with fast Fourier decay expose latent determinism via Krylov state space hierarchy. Krylov growth rate sets prediction complexity and bounds largest Lyapunov exponent. Extends Hamiltonian chaotic dynamics ideas to classical dissipative systems. Activation: mean-field theory, Krylov chaos, RNN prediction, Lyapunov exponent, temporal modes, deterministic chaos, neural networks."
---

## Context

**arXiv**: 2606.08805 (2026-06-07)  
**Authors**: Alkesh Yadav, Vladimir Shaidurov, Jonathan Kadmon  
**Categories**: cond-mat.dis-nn, q-bio.NC

Dynamical mean-field theory recasts deterministic chaos in random recurrent networks as an effective stochastic process. For analytic nonlinearities with sufficiently fast Fourier decay, this stochasticity is only apparent: the continuous past of a realized mean-field trajectory uniquely determines its future.

## Core Methodology

1. **Mean-Field Determinism**: Show that mean-field theory is not merely ensemble description, but conditional prediction theory for individual trajectories
2. **Krylov State Space Unfolding**: Unfold power spectrum into infinite hierarchy of temporal modes exposing latent determinism
3. **Krylov Growth Rate**: Sets complexity of finite-resolution prediction and upper-bounds largest Lyapunov exponent
4. **Microscopic vs Predictive**: Distinguish microscopic sensitivity (Lyapunov) from predictive complexity (Krylov growth)
5. **Hamiltonian Extension**: Extend Krylov growth ideas from Hamiltonian chaotic dynamics to classical dissipative systems (RNNs)

## Key Results

- Mean-field chaos is deterministic: past trajectory uniquely determines future (for analytic nonlinearities)
- Krylov hierarchy organizes latent determinism across infinite temporal modes
- Krylov growth rate bounds largest Lyapunov exponent in this network class
- Microscopic sensitivity ≠ predictive complexity (distinct aspects of mean-field chaos)
- Classical dissipative systems can use Hamiltonian chaos analysis tools

## Implementation Steps

1. Identify analytic nonlinearities with fast Fourier decay in RNN activation functions
2. Compute power spectrum of mean-field trajectory
3. Unfold spectrum into Krylov state space (infinite hierarchy)
4. Calculate Krylov growth rate (temporal mode complexity)
5. Compare with largest Lyapunov exponent (microscopic sensitivity)
6. Verify determinism: unique trajectory reconstruction from past history
7. Apply to neural network chaos analysis (learning dynamics, recurrent computation)

## Pitfalls

- **Fourier Decay Requirement**: Analytic nonlinearities needed; polynomial/sigmoid functions may not qualify
- **Krylov Complexity**: Infinite hierarchy — finite-resolution prediction requires truncation strategy
- **Lyapunov vs Krylov**: Both measure chaos but different aspects — careful interpretation needed
- **Mean-Field Validity**: Requires large network size for mean-field approximation accuracy
- **Hamiltonian Assumption Transfer**: Classical dissipative systems differ from Hamiltonian — verify each extension

## Verification

1. Fourier decay analysis: verify activation function analyticity
2. Trajectory reconstruction: unique past → unique future (determinism test)
3. Krylov vs Lyapunov comparison: growth rate should bound exponent
4. Prediction accuracy: finite-resolution forecast based on Krylov truncation
5. Network size scaling: mean-field accuracy increases with N

## Activation

mean-field theory, Krylov chaos, RNN prediction, Lyapunov exponent, temporal modes, deterministic chaos, neural networks, Hamiltonian dynamics, dissipative systems