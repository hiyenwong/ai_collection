---
name: federated-ecg-wearable
description: Federated Learning methodology for privacy-preserving ECG monitoring on ultra-resource-constrained wearable devices. Family-grouped hierarchical FL for sub-5KB cardiovascular models. Activation: federated learning ECG, wearable cardiac monitoring, privacy-preserving ML, sub-5KB model, arrhythmia detection.
---

# Federated ECG Monitoring on Wearables

## Overview

Based on arXiv:2605.18862 — studies feasibility of **family-grouped hierarchical federated learning** for sub-5KB models deployed on ultra-resource-constrained wearable devices for early arrhythmia detection through continuous ECG monitoring.

Cardiovascular disease is the leading cause of death worldwide. Continuous ECG monitoring on wearables can prevent life-threatening events, but privacy and resource constraints limit deployment.

## Core Methodology

### Three-Level Hierarchy

```
Individual Device (Sub-5KB) → Family Group Aggregation → Global Server
```

1. **Device Level**: Tiny models (<5KB) trained locally on wearable ECG data
2. **Family Group**: Aggregation among devices sharing physiological/genetic similarity
3. **Global**: Final model aggregation across family groups

### Why Family Grouping?

- Family members share cardiac physiology patterns → faster convergence
- Reduces non-IID data problem in federated learning
- Privacy-preserving: only model weights shared, no raw ECG data
- Smaller aggregation groups → less communication overhead

### Implementation Pattern

```python
# Device-level training (sub-5KB model)
model = TinyECGClassifier(params=<5000)  # Ultra-compact architecture

for batch in local_ecg_stream:
    loss = model.train(batch)
    model.update_gradients(loss)

# Family-group aggregation
family_updates = collect_family_weights(device_ids)
family_model = weighted_average(family_updates, weights=device_confidence)

# Global aggregation
global_model = federated_avg(family_models, method='hierarchical')
```

### Resource Constraints

| Constraint | Target | Rationale |
|-----------|--------|-----------|
| Model size | <5KB | On-device SRAM limits on microcontrollers |
| Inference latency | <100ms | Real-time arrhythmia detection requirement |
| Communication | Compressed gradients | Bandwidth-limited wearable connectivity |
| Energy | <1mW average | Battery life for multi-day wear |

### Key Advantages

1. **Privacy**: No raw ECG leaves the device
2. **Personalization**: Family grouping captures shared physiology
3. **Scalability**: Hierarchical reduces global communication bottleneck
4. **Accessibility**: Sub-5KB models run on commodity wearables
5. **Clinical value**: Early arrhythmia detection from continuous monitoring

## When to Use

- Wearable cardiac monitoring systems
- Privacy-sensitive medical ML on edge devices
- Federated learning with physiological data
- Ultra-low-resource embedded ML deployment

## Pitfalls

- Sub-5KB models have limited capacity — careful architecture selection needed
- Family grouping requires device registration logic
- Non-IID data across families may cause bias
- Model compression may lose subtle arrhythmia patterns
- Communication failures on wearable devices require fault-tolerant aggregation

## Related Papers

- 2605.18862: Towards Family-Grouped Hierarchical Federated Learning on Sub-5KB Models: A Feasibility Study of Privacy-Preserving ECG Monitoring for Ultra-Resource-Constrained Wearables
- 2605.18936: FedMental: Evaluating Federated Learning for Mental Health Detection from Social Media Data
