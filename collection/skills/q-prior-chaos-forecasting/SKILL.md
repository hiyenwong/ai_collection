---
name: q-prior-chaos-forecasting
description: Quantum statistical prior (Q-Prior) methodology for chaotic system forecasting. Based on arXiv:2606.13422 — provable quantum advantage via two-copy Bell measurement for invariant measure estimation.
category: quantum
trigger_words: quantum statistical prior, Q-Prior, chaos forecasting, turbulent flow, weather forecasting, quantum advantage
arxiv_id: 2606.13422v3
---

# Quantum Statistical Priors for Chaotic System Forecasting

## Overview
Theoretical foundations for practical quantum advantage in quantum-informed machine learning for chaotic dynamical systems. k-indexed quantum statistical priors (Q-Priors) store non-factorisable spatial correlations of invariant measures on nq = kq qubits.

## Two-Stage Quantum Advantage

### Stage 1: Representation
- Superposition and entanglement compactly store non-factorisable spatial correlations
- k-point marginal of invariant measure encoded on nq = kq qubits
- Extends single-site construction to multi-site k >= 2

### Stage 2: Extraction
- Joint Bell measurements on two copies estimate any post hoc Pauli functional
- Copy-pair count independent of nq
- Provable quantum-classical separation: adaptive single-copy requires Omega(2^nq) copies
- Realized on IQM superconducting processors

## Case Studies

### Turbulent Channel Flow
- Two-copy read-out yields velocity-direction coherence
- Multi-site k=2 Q-Prior recovers DNS-level invariant-measure statistics
- Unregularised baseline loses these statistics

### Weather Forecasting (ERA5)
- Diagonal k <= 2 Q-Prior steers Koopman rollout
- Improves anomaly correlation skill by 10% to 39%
- Lead times: 48 to 240 hours
- Stabilises long-horizon rollouts against collapse onto static mean field

## Practical Advantage Definition
Mechanism + case studies satisfy practical-advantage definition, identifying a candidate route to practical quantum advantage before fault-tolerant hardware.

## When to Use
- Chaotic system prediction (weather, fluid dynamics)
- Invariant measure estimation
- Quantum machine learning with provable advantage
- Koopman operator-based forecasting
