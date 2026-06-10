---
name: neural-decoder-confidence-qec
description: "Neural network decoder confidence as a learned proxy for logical gap in quantum error correction — using soft decoder information to estimate decoding reliability."
category: quantum-systems-engineering
version: "1.0.0"
created: "2026-06-11"
source: "arxiv:2606.08758"
---

# Neural Decoder Confidence for QEC

## Description

Methodology for using neural network decoder confidence as a learned proxy for the logical gap in quantum error correction. Extends hard-decision decoders with soft information that estimates decoding reliability.

**Source Paper**: arXiv:2606.08758 — "Neural network decoder confidence as a learned proxy for the logical gap" (Dentelski, 2026-06-07)

## Activation Keywords
- neural decoder confidence
- logical gap proxy
- QEC soft decoding
- quantum decoder reliability
- neural error correction confidence
- soft syndrome decoding

## Core Concepts

### 1. Hard vs Soft Decoding
- **Hard Decision**: Decoder outputs single correction (which logical sector)
- **Soft Information**: Decoder outputs confidence estimate (probability of correctness)
- **Logical Gap**: Energy difference between best and second-best correction — indicates how confident the decoder should be

### 2. Confidence as Proxy
- Neural decoders can learn to estimate the logical gap without explicit computation
- Confidence correlates with actual decoding reliability
- Enables downstream systems (control planes, protocols) to make informed decisions

### 3. Implementation Pattern
```
Syndrome → Neural Decoder → (Correction, Confidence)
     ↓                           ↓
  QEC Result              Reliability Estimate
                               ↓
                    Use by Control Plane / Protocol
```

## Applications
- **Adaptive QEC**: Adjust code distance based on confidence
- **Network Routing**: Prefer paths with higher decoder confidence
- **Protocol Selection**: Choose protocols based on reliability estimates
- **Resource Allocation**: Focus resources on low-confidence regions

## Key Insight
Neural decoders naturally produce confidence scores during inference (softmax outputs, attention weights) that can serve as proxies for the logical gap without additional computation.

## Related Methodologies
- [[scope-qec-control-plane]] — Uses logical error estimates for routing (arXiv:2606.08873)
- [[coset-ensemble-decoder-qec]] — Ensemble decoding with voting (arXiv:2606.11076)

## References
- arXiv:2606.08758 — Neural network decoder confidence as a learned proxy for the logical gap
