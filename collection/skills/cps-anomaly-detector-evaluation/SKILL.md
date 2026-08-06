---
name: cps-anomaly-detector-evaluation
title: CPS Anomaly Detector Evaluation Framework
version: 1.0.0
description: Methodology for evaluating Cyber-Physical Systems (CPS) anomaly detectors independently of decision rules using normalized residual energy and Kullback-Leibler divergence analysis.
trigger: When evaluating or comparing CPS anomaly detection systems across different benchmarks like SWaT, WADI, and HAI.
---

# CPS Anomaly Detector Evaluation Framework

## Overview
This skill implements the methodology from arXiv:2608.02821 "What the Detector Can See: Evaluating CPS Anomaly Detectors Independently of the Decision Rule" by Peiran Shi et al. The approach treats CPS anomaly detectors as two-stage pipelines:
1. **Stage 1**: Maps observations to residuals (representation learning)
2. **Stage 2**: Maps residuals to alarms (decision rule/thresholding)

Instead of only evaluating final alarm performance (precision, recall, F1), this framework evaluates Stage 1 directly using **normalized residual energy**, which has an exact connection to the Kullback-Leibler divergence from the trained-normal reference distribution.

## Key Benefits
- **Decision-rule-free evaluation**: Separates representation quality from threshold calibration
- **Cross-benchmark comparison**: Enables fair comparison across different CPS testbeds (SWaT, WADI, HAI)
- **Attack separation analysis**: Measures how well detectors separate attack patterns from normal operation
- **Stability assessment**: Evaluates robustness across train-test gaps
- **Compactness measurement**: Quantifies how efficiently a detector encodes the physical plant

## Implementation Steps

### 1. Data Preparation
- Collect normal training data from CPS benchmarks (SWaT, WADI, HAI)
- Prepare test datasets with known attack scenarios
- Ensure consistent preprocessing across all detectors

### 2. Detector Training
- Train multiple anomaly detectors (GDN, FuSAGNet, TranAD, NSIBF, GeCo, etc.)
- Use identical training protocols where possible
- Record residual outputs for all test samples

### 3. Normalized Residual Energy Calculation
```python
# Pseudocode for normalized residual energy
def calculate_normalized_residual_energy(residuals, normal_residuals):
    """
    Calculate normalized residual energy as proxy for KL divergence
    residuals: array of test residuals
    normal_residuals: array of training residuals (reference distribution)
    """
    # Estimate reference distribution parameters
    mean_normal = np.mean(normal_residuals, axis=0)
    cov_normal = np.cov(normal_residuals.T)
    
    # Calculate Mahalanobis distance (equivalent to KL divergence for Gaussian)
    inv_cov = np.linalg.inv(cov_normal + 1e-8 * np.eye(cov_normal.shape[0]))
    diff = residuals - mean_normal
    mahalanobis_dist = np.sum(diff @ inv_cov * diff, axis=1)
    
    # Normalize by degrees of freedom
    normalized_energy = mahalanobis_dist / residuals.shape[1]
    
    return normalized_energy
```

### 4. Evaluation Metrics
- **Attack Separation**: Mean residual energy difference between attack and normal samples
- **Stability Score**: Variance of residual energy across different test periods
- **Compactness Ratio**: Residual energy per channel vs. total channels
- **Cross-Benchmark Ranking**: Consistency of detector performance across SWaT, WADI, HAI

### 5. Analysis Workflow
1. Compute normalized residual energy for all detectors on all benchmarks
2. Generate residual energy distributions for normal vs. attack samples
3. Calculate attack separation scores at multiple false alarm rates
4. Analyze detector rankings across different testbeds
5. Identify failure modes: weak representation vs. poor threshold vs. low-impact attacks

## Use Cases
- **Detector Selection**: Choose the best detector for a specific CPS based on representation quality rather than tuned performance
- **Failure Analysis**: Diagnose whether detection failures stem from representation or thresholding issues
- **Benchmark Development**: Design more comprehensive CPS evaluation protocols
- **Research Comparison**: Fairly compare novel anomaly detection algorithms

## References
- **Primary Paper**: Shi, P., Xiang, J., Zhang, X., & Fu, C. (2026). What the Detector Can See: Evaluating CPS Anomaly Detectors Independently of the Decision Rule. arXiv:2608.02821 [cs.CR]
- **Code Repository**: https://zenodo.org/records/20653309
- **Benchmarks**: SWaT, WADI, HAI CPS datasets

## Activation Keywords
cyber-physical systems, anomaly detection, residual energy, decision-rule-free evaluation, CPS security, attack separation, normalized residuals, KL divergence, detector evaluation, SWaT, WADI, HAI