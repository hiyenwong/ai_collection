---
name: neural-decoder-confidence-qec
description: "Graph neural network decoder confidence as learned proxy for logical gap in quantum error correction. The logit of a pretrained GNN decoder acts as a reliable proxy for minimum-weight perfect matching (MWPM) logical gap, enabling soft-information error correction without the computational overhead. Use when designing QEC decoders, implementing soft-decision quantum error correction, or evaluating decoder reliability."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.08758"
  published: "2026-06-07"
  authors: "David Dentelski"
  tags: [quantum-error-correction, GNN-decoder, logical-gap, MWPM]
allowed-tools: exec, read, write
---

# Neural Decoder Confidence as Logical Gap Proxy

## Description

Methodology from arXiv:2606.08758 (June 2026). Tests whether the logit of a graph neural network (GNN) decoder can act as a learned proxy for the logical gap in quantum error correction decoding.

## Core Methodology

### Problem

QEC decoders must infer the logical sector from measured syndrome. Beyond hard decisions, soft information estimating reliability is valuable. For MWPM, the logical gap (complementary gap) is a common confidence measure but computationally expensive.

### Solution

Use the logit output of a pretrained GNN decoder as a learned proxy for the logical gap:

1. **Train GNN decoder** on surface code syndrome data for hard logical decisions
2. **Extract logit values** from the GNN output layer
3. **Compare logit distribution** against MWPM logical gap
4. **Calibrate reliability** — logits correlate with logical gap magnitude

### Key Findings

- Pretrained GNN logits correlate strongly with MWPM logical gap
- GNN-based soft information is orders of magnitude faster to compute
- Enables real-time soft-decision decoding on quantum hardware
- Maintains decoding accuracy while providing confidence estimates

## Implementation Patterns

### Pattern 1: GNN Decoder with Confidence Output

```python
import torch
import torch.nn as nn

class GNNQECDecoder(nn.Module):
    def __init__(self, hidden_dim=64):
        super().__init__()
        self.message_pass = GNNLayer(hidden_dim)
        self.readout = nn.Linear(hidden_dim, 1)
    
    def forward(self, syndrome_graph):
        # Message passing over syndrome graph
        node_features = self.message_pass(syndrome_graph)
        # Global pooling
        graph_repr = torch.mean(node_features, dim=0)
        # Logit output (proxy for logical gap)
        logit = self.readout(graph_repr).squeeze()
        return logit
    
    def decode(self, syndrome_graph):
        """Return hard decision + confidence."""
        logit = self.forward(syndrome_graph)
        prediction = torch.sign(logit)
        confidence = torch.sigmoid(torch.abs(logit))
        return prediction, confidence
```

### Pattern 2: Calibration Against MWPM

```python
def calibrate_gnn_confidence(gnn_model, mwpm_decoder, dataset):
    """Calibrate GNN logits against MWPM logical gap."""
    logits = []
    gaps = []
    
    for syndrome in dataset:
        logit = gnn_model(syndrome).item()
        gap = mwpm_decoder.logical_gap(syndrome)
        logits.append(logit)
        gaps.append(gap)
    
    # Fit calibration: |logit| ~ logical_gap
    correlation = np.corrcoef(np.abs(logits), gaps)[0, 1]
    return correlation
```

### Pattern 3: Soft-Decision QEC Pipeline

```python
class SoftQECDecoder:
    def __init__(self, gnn_model, threshold=0.5):
        self.model = gnn_model
        self.threshold = threshold
    
    def decode_with_confidence(self, syndrome):
        """Decode syndrome with reliability estimate."""
        prediction, confidence = self.model.decode(syndrome)
        
        if confidence < self.threshold:
            # Low confidence: flag for additional verification
            return {
                'decision': prediction,
                'confidence': confidence,
                'flagged': True
            }
        
        return {
            'decision': prediction,
            'confidence': confidence,
            'flagged': False
        }
```

## When to Use

- Quantum error correction decoder design
- Real-time soft-decision decoding
- QEC systems requiring confidence estimates
- Replacing MWPM logical gap computation
- Neural QEC decoder development

## Pitfalls

1. **Logit scale differs from gap**: GNN logits are not directly in gap units — calibration needed
2. **Model generalization**: GNN trained on one code distance may not transfer to others
3. **Syndrome graph construction**: Graph topology must match the underlying QEC code

## References

- arXiv:2606.08758
- Related: `dart-q-realtime-qldpc-decoding` — real-time QLDPC decoding
- Related: `sparse-mamba-qec-decoder` — sparse Mamba QEC decoder
