# Quantum Measurement Temperature (QMT) — VQC Training Stability Fix

Based on arXiv: 2606.22551 (Mondal et al., 2026-06-21)

## Problem
Hybrid QNN classifiers produce logits as expectation values of quantum measurement operators. For standard Pauli measurements, outputs are bounded to [-1, 1]. When used with cross-entropy loss + softmax for multi-class classification:
- Loss operates in weak sensitivity regime
- Parameter gradients are suppressed
- Training becomes unstable across random initializations

## Solution: QMT
Add a learnable scaling parameter τ ("Quantum Measurement Temperature"):
```
rescaled_logit = quantum_measurement_output / τ
```

## Implementation
```python
class QMTLayer(nn.Module):
    def __init__(self, init_temperature=0.1):
        super().__init__()
        self.temperature = nn.Parameter(torch.tensor(init_temperature))
    def forward(self, quantum_logits):
        return quantum_logits / self.temperature.clamp(min=1e-4)
```

## Key Properties
- Architecture-agnostic (no circuit changes needed)
- Acts during training (not post-hoc calibration)
- Increases gradient magnitude and variance
- Validated on fluorescence microscopy + 6-class Fashion MNIST

## When to Use
- Training instability in VQCs
- Bounded measurement outputs (Pauli, etc.)
- Multi-class classification with cross-entropy loss
- When you don't want to redesign the quantum circuit