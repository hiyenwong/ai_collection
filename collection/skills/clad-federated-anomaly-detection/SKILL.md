---
name: clad-federated-anomaly-detection
description: >
  Clustered Label-Agnostic Federated Learning (CLAD) framework for anomaly detection
  in distributed systems. Combines unsupervised clustering with supervised detection
  via DM²A (Dual-Mode Multi-Stage Aggregation), enabling privacy-preserving anomaly
  detection across heterogeneous federated clients without shared labels.
---

## When to Use
- Anomaly detection across distributed/federated systems without centralized data
- Scenarios where clients have heterogeneous anomaly types and no shared label schema
- Privacy-sensitive environments requiring federated learning without data sharing
- Systems needing joint unsupervised + supervised anomaly detection
- Edge computing environments with communication bandwidth constraints

## Core Concepts

### CLAD Framework
A federated learning architecture that performs anomaly detection without requiring clients to share labels. Handles label heterogeneity by clustering clients based on anomaly patterns rather than label agreement.

### DM²A (Dual-Mode Multi-Stage Aggregation)
A two-phase aggregation mechanism:
1. **Unsupervised mode**: Cluster clients by feature distribution similarity
2. **Supervised mode**: Aggregate model weights within clusters where label semantics align

### Label-Agnostic Federated Learning
Traditional FL requires shared label schemas. CLAD removes this constraint by using a joint detection pipeline that works across heterogeneous label spaces through dynamic clustering.

## Implementation Steps

### Step 1: Setup Federated Environment
```
Clients: C_1, C_2, ..., C_N (each with local data D_i)
Server: Aggregator with DM²A module
Communication: Round-based weight exchange (not data)
```

### Step 2: Unsupervised Clustering Phase
1. Each client trains local autoencoder on normal data
2. Clients send embedding statistics (not raw data) to server
3. Server clusters clients using similarity of embedding distributions
4. Form clusters K = {K_1, K_2, ..., K_m}

### Step 3: Supervised Detection Phase
1. Within each cluster, clients with compatible labels perform federated training
2. DM²A aggregates model weights using cluster-aware weighted averaging
3. Anomaly score threshold calibrated per-cluster

### Step 4: Joint Detection Pipeline
```
Input: new sample x
Step A: Pass through unsupervised autoencoder → anomaly score s_u
Step B: Pass through supervised classifier → anomaly score s_s
Step C: Combine: s_final = α·s_u + (1-α)·s_s
Output: anomaly if s_final > threshold
```

### Step 5: Dynamic Cluster Maintenance
1. Monitor cluster quality (silhouette score, inter-cluster divergence)
2. Re-cluster when distribution shift detected (client data drift)
3. Handle new client joining: assign to nearest cluster via embedding similarity

## Key Parameters
- `α`: Weight balancing unsupervised vs supervised scores (typically 0.3-0.7)
- `n_clusters`: Number of client clusters (auto-determined or set to 3-10)
- `communication_rounds`: FL training rounds per phase
- `compression_ratio`: Gradient compression for bandwidth reduction (achieves 30% comm cost reduction)
- `threshold`: Anomaly detection threshold (per-cluster calibrated)

## Performance Characteristics
- 30% communication cost reduction vs. standard federated learning
- Up to 30% accuracy improvement over label-heterogeneous baselines
- Scales to 100+ clients with dynamic clustering overhead O(N log N)

## Pitfalls
- **Label collision**: Different clients may use same label for different anomaly types; clustering mitigates this
- **Cluster instability**: Frequent re-clustering can cause oscillation; use hysteresis threshold
- **Cold start**: New clients need warm-up rounds before cluster assignment
- **Communication bottleneck**: Use gradient compression and asynchronous aggregation for large-scale deployments

## Verification
1. Evaluate F1-score per anomaly type across clusters
2. Measure communication overhead (bytes per round)
3. Test with heterogeneous label schemas (non-overlapping, partially overlapping)
4. Compare against centralized baseline (upper bound) and local-only baseline (lower bound)

## References
- arXiv: 2605.06571v1 — "CLAD: Clustered Label-Agnostic Federated Learning Framework"
- Category: cs.LG / cs.DC (Machine Learning / Distributed Computing)
