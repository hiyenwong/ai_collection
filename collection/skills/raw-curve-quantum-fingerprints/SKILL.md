---
name: raw-curve-quantum-fingerprints
description: "Quantum cloud platform authentication framework using multi-dimensional quantum fingerprints from raw measurement data. Constructs Mahalanobis-based fingerprints with drift early warning and adversarial detection to verify which physical device executes workloads, preventing hardware substitution attacks. Activation: quantum authentication, cloud verification, hardware fingerprinting, quantum cloud, device authentication, Mahalanobis distance, drift detection, adversarial detection, raw-curve"
metadata:
  arxiv_id: "2606.11644"
  published: "2026-06-10"
  authors: "Geyuyan Ma, Xiangdong Meng, Yangyang Fei, Zhiqiang Fan, Hanshi Zhao"
  tags: [quantum, cloud-security, authentication, fingerprinting, hardware-verification, mahalanobis, adversarial-detection]
---

## Raw-Curve Quantum Fingerprint Authentication Framework

### Problem: Cloud Hardware Substitution

Quantum cloud platforms offer powerful computing but users cannot verify which physical device executes their workload. Malicious adversaries can redirect jobs to substituted or inferior processors.

### Solution: Multi-Dimensional Quantum Fingerprints

Construct fingerprints directly from raw measurement data without curve fitting:

1. **Collect raw measurement traces** from the target quantum device
2. **Extract multi-dimensional features** across the trace (timing, amplitude, noise characteristics)
3. **Compute Mahalanobis distance** between reference and test fingerprints
4. **Statistical authentication** with confidence bounds

### Key Components

#### Mahalanobis Authentication

```
D² = (x - μ)ᵀ Σ⁻¹ (x - μ)
```

where μ is the reference fingerprint mean and Σ is the covariance matrix. Unlike Euclidean distance, Mahalanobis accounts for correlations between features.

#### Drift Early Warning System

- Monitor fingerprint statistics over time
- Detect gradual degradation before authentication fails
- Distinguish natural drift from malicious substitution
- Alert thresholds based on statistical significance

#### Adversarial Detection

- Identify patterns inconsistent with genuine hardware
- Detect substituted processors via anomaly scoring
- Multi-dimensional analysis catches sophisticated attacks
- Statistical hypothesis testing with controlled false positive rate

### Implementation Steps

1. **Baseline collection**: Gather N reference traces from authentic device
2. **Feature extraction**: Compute multi-dimensional fingerprint vector per trace
3. **Statistical modeling**: Estimate μ and Σ from reference set
4. **Online verification**: Compare new traces via Mahalanobis distance
5. **Drift monitoring**: Track fingerprint statistics over time windows
6. **Alert generation**: Trigger warnings when distance exceeds threshold

### Advantages

- **No curve fitting needed**: Works with raw measurement data directly
- **Multi-dimensional**: Captures more device characteristics than single-metric approaches
- **Early warning**: Detects drift before complete authentication failure
- **Adversarial detection**: Identifies both substitution and manipulation attacks
- **General framework**: Applicable across different quantum hardware types

### When to Apply

- Quantum cloud platform security audits
- Hardware-as-a-service verification
- Quantum computing service level agreements
- Multi-tenant quantum computer isolation verification

### Pitfalls

- Requires sufficient reference data for stable covariance estimation
- Hardware maintenance/replacement changes the legitimate fingerprint
- Temperature and calibration variations cause natural drift
- False positives increase with small reference set sizes
- Need periodic re-baselining after legitimate hardware changes
