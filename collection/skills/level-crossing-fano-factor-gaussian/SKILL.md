---
name: level-crossing-fano-factor-gaussian
description: "Exact variance and Fano factor analytical formulae for arbitrary level crossings in stationary Gaussian processes. Extends the Kac-Rice mean crossing rate to capture clustering vs. regularity statistics, critical for neuronal spike train analysis, neural coding reliability, and stochastic neural dynamics. Use when analyzing spike train variability, threshold crossing statistics, or neural coding Fano factors."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.25278"
  published: "2026-05-26"
  tags: [level-crossing, fano-factor, gaussian-process, neuronal-spikes, stochastic-dynamics, kac-rice, neural-coding]
---

# Exact Variance and Fano Factor for Level Crossings in Stationary Gaussian Processes

## Core Concept

The traditional Kac-Rice formula provides only the **mean rate** of level crossings, missing temporal correlation structure. This methodology derives **exact analytical formulae** for the variance and Fano factor of arbitrary level crossings in smooth stationary Gaussian processes, revealing how temporal correlations dictate whether crossing events (e.g., neuronal spikes) cluster or become regular.

## Key Technical Insights

1. **Beyond Kac-Rice**: The mean crossing rate is blind to temporal correlation structure. The exact variance and Fano factor derived here capture the full temporal organization of crossing events, enabling more robust parameter estimation and model selection.

2. **Oscillatory Systems (Sub-Poissonian)**: In systems with oscillatory correlations (e.g., stochastic damped harmonic oscillator), a recent crossing suppresses immediate subsequent ones, producing sub-Poissonian statistics — more regular than random.

3. **Damped Systems (Super-Poissonian)**: As damping increases and oscillations disappear, large slow excursions above threshold produce multiple closely-spaced crossings, yielding super-Poissonian clustering statistics.

4. **Reentrant Transitions**: In purely relaxational systems (e.g., OU-driven mean-reverting process), competition between driving noise and relaxation timescales produces reentrant transitions between sub- and super-Poissonian statistics as threshold level varies.

## Mathematical Framework

- **Input**: Smooth stationary Gaussian process X(t) with autocorrelation R(τ)
- **Level crossings**: Times where X(t) = θ (threshold)
- **Mean rate** (Kac-Rice): ν = (1/2π)√(-R''(0)/R(0)) · exp(-θ²/(2R(0)))
- **Variance**: Exact formula via double integral of second factorial crossing moment density
- **Fano factor**: F = Var[N(T)]/E[N(T)] — F<1: regular, F>1: clustered, F=1: Poisson

## Applications to Neuroscience

- **Spike train analysis**: Classify neurons as regular spikers (sub-Poisson) vs. bursters (super-Poisson)
- **Neural coding reliability**: Fano factor quantifies coding precision — sub-Poisson = reliable, super-Poisson = noisy
- **Model selection**: Distinguish between oscillatory (damped harmonic oscillator) and relaxational (OU) neural dynamics
- **Parameter estimation**: More robust than mean-rate fitting alone
- **Criticality analysis**: Crossing statistics reveal proximity to dynamical regime transitions

## Key Predictions

1. Stochastic damped harmonic oscillators → sub-Poissonian crossings (regular spiking)
2. Heavily damped systems → super-Poissonian crossings (burst clustering)
3. OU-driven relaxational systems → reentrant sub↔super-Poissonian transitions with threshold variation
4. Fano factor captures oscillatory vs. relaxational neural dynamics classification

## Activation Keywords

level crossing, Fano factor, Gaussian process, spike train, neuronal variability, Kac-Rice, crossing statistics, sub-Poissonian, super-Poissonian, stochastic dynamics, neural coding reliability, threshold crossing
