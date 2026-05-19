---
name: ven-circuit-snn-social-learning
description: "VENCircuit methodology — Von Economo neurons (VENs) as acquisition scaffolds in recurrent spiking neural networks. Combines computational modeling with clinical predictions for bvFTD and autism. Use when: studying VENs, social learning in SNNs, gradient pathway analysis, clinical prediction from computational models, developmental scaffolding in neural networks."
---

# VENCircuit: VENs as Acquisition Scaffolds in Recurrent SNNs

Methodology from Keskin (2026) arXiv:2605.17399.

## Core Finding

Von Economo neurons (VENs) function as **acquisition scaffolds** — their presence enables reliable convergence in recurrent SNNs (98% vs 70% convergence). VEN ablation causes stochastic learning failure (not mere speed reduction), providing a computational analogue of variable social skill acquisition in autism spectrum conditions.

## Key Experimental Design

### Network Architecture
- VEN-like projection neurons: K=40, 2% of total neurons
- Recurrent pyramidal circuit
- Trained on binary classification task
- 50 matched random initializations with/without VENs

### Phase-Ablation Protocol
1. Train intact network
2. Ablate VENs at different training phases
3. Most disruptive: mid-training (epochs 5-25)
4. Reveals co-adaptive dependency in pyramidal circuit

## Formal Account

VENs provide a **direct gradient pathway** immune to Jacobian instabilities affecting the recurrent circuit. This explains:
- Why VEN loss causes complete learning failure (not slowdown)
- Why mid-training ablation is most disruptive
- Why inference-time ablation causes variable collapse

## Clinical Predictions

| Condition | VEN Status | Prediction |
|-----------|-----------|------------|
| bvFTD | Selective VEN loss | Stochastic learning failure |
| ASC | Reduced VENs | Variable social skill acquisition |
| Organoid models | VEN manipulation | Falsifiable electrophysiology tests |

## Implementation Pattern

```python
# VENCircuit training loop pattern
for epoch in range(epochs):
    # Forward pass through recurrent circuit
    hidden, spikes = recurrent_circuit(inputs, hidden)
    
    # VEN gradient pathway (bypasses recurrent Jacobian)
    if ven_enabled:
        ven_output = ven_layer(inputs, hidden)
        loss = compute_loss(ven_output, target)
    else:
        # Degraded gradient through unstable Jacobian
        loss = compute_loss(hidden, target)
    
    # Backprop with VEN-mediated stability
    loss.backward()
```

## Reproducibility Notes
- 50 random seeds essential for statistical significance
- Fisher's exact test: OR=21.0, 95% CI [2.7, 167], p=8.7e-5
- Inference ablation: Wilcoxon p=0.022
- Performance drop range: minimal to catastrophic (0.989→0.620)

## Activation Keywords
ven-circuit, von economo neurons, VEN, social learning SNN, acquisition scaffold, bvFTD computational model, autism computational model, gradient pathway SNN
