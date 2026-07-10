---
name: quantum-machine-learning-uav-anomaly-detection
description: "Leakage-free evaluation of quantum ML for UAV anomaly detection. Group-aware temporal protocol + three-mode feature audit + hybrid XGBoost-DRU classifier."
category: quantum-ml
---

# Quantum ML for Cyber-Physical Anomaly Detection in UAVs

**arXiv**: 2605.19233 (cs.CR, cs.LG, quant-ph)
**Authors**: Carlos A. Durán Paredes, Javier E. León Calderón, Nicolás Sánchez Perea, German Darío Díaz, Camilo Segura Quintero

## Core Methodology

Rigorous, **leakage-free evaluation** of quantum machine learning for unmanned aerial vehicle (UAV) anomaly detection on the multi-sensor TLM:UAV benchmark.

### Three Key Contributions

1. **Group-Aware Temporal Protocol (B2)**:
   - Partitions dataset into 10 contiguous TimeUS blocks
   - Evaluates over 10 seeds
   - Eliminates inflation from random stratified splits that mix neighboring samples

2. **Three-Mode Feature Audit (Full/Loose/Strict)**:
   - Quantifies how much accuracy comes from instantaneous physical signals vs. contextual proxies
   - Proxies: cumulative energy, battery state, GPS trajectory
   - Strict mode removes proxy features for fair evaluation

3. **Hybrid XGBoost + Data Reuploading (DRU) Classifier**:
   - Benchmarked against 5 paired nonlinear controls under identical budgets
   - Controls: raw, PCA, polynomial-2, random-RBF, untrained DRU map

### Key Finding

- Standalone DRU does NOT consistently match strongest classical baseline
- **Trained-DRU hybrid** is the only model whose mean F1 macro shifts upward from full to strict (+0.05)
- Lowest mean false-alarm rate under proxy-free evaluation

## Implementation Patterns

- Use temporal partitioning (not random splits) for time-series evaluation
- Feature audit: separate physical signals from contextual proxies
- Hybrid quantum-classical: quantum feature map + classical classifier
- Evaluate under proxy-free conditions to avoid inflated metrics
- Open Qiskit 2.x implementation for reproducibility

## Evaluation Protocol

1. Partition by time blocks (contiguous, not random)
2. Test across multiple seeds for variance estimation
3. Audit features: full → loose → strict (removing proxies)
4. Compare against multiple classical baselines under identical budgets
5. Report inter-seed variance honestly (don't overclaim incremental gains)

## Applications

- Aerospace cybersecurity analytics
- NISQ-era quantum-enhanced anomaly detection
- Cyber-physical system security monitoring
- Multi-sensor fusion evaluation

## Activation

quantum anomaly detection, UAV security, data reuploading, leakage-free evaluation, temporal protocol, feature audit, Qiskit, cyber-physical systems
