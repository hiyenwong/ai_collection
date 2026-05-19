---
name: loop-aware-transformer-quantization
description: "Loop-aware post-training quantization (PTQ) methodology for recursive/looped Transformers. Addresses distribution shift across loop roles, state reuse across transitions, and recursive error accumulation. Combines activation scaling, selective transformation, cross-loop state alignment, and trajectory-aware optimization. Use when: LoopLM quantization, looped model PTQ, recursive Transformer quantization, LoopQ, post-training quantization looped models, parameter-efficient LM quantization, recursive neural network quantization."
---

# Loop-Aware Transformer Quantization (LoopQ)

## Core Problem

Looped LMs (LoopLMs) reuse Transformer blocks recursively, enabling deeper computation under fixed model size. But this reuse creates three quantization-specific challenges:

1. **Distribution shift across roles** — Same block serves different functions at different loop iterations
2. **State reuse across loop transitions** — Quantization errors propagate and accumulate across loops
3. **Recursive error accumulation** — Small per-loop errors compound multiplicatively

## LoopQ Framework

```
Shared Quantized Backbone + Lightweight Loop Adaptations
```

### Components

1. **Activation Scaling** — Per-role scaling factors compensate for distribution shifts
2. **Selective Transformation** — Only transform sensitive layers; keep others shared
3. **Cross-Loop State Alignment** — Align hidden states across loop transitions to prevent drift
4. **Trajectory-Aware Optimization** — Optimize quantization parameters considering full loop trajectory, not per-layer independently

## Implementation Pattern

```python
class LoopQConfig:
    def __init__(self, model, n_bits=8, n_loops=4):
        self.model = model
        self.n_bits = n_bits
        self.n_loops = n_loops
        # Per-role scaling factors
        self.role_scales = {}  # {loop_idx: scale_factor}
        # Cross-loop alignment matrices
        self.alignment = {}  # {(from_loop, to_loop): alignment_matrix}
    
    def calibrate(self, calibration_data):
        """Calibrate quantization with loop-aware statistics"""
        for loop_idx in range(self.n_loops):
            # Collect activation statistics per role
            activations = self.collect_activations(calibration_data, loop_idx)
            self.role_scales[loop_idx] = self.compute_scale(activations)
        
        # Cross-loop state alignment
        for i in range(self.n_loops - 1):
            state_i = self.get_loop_state(calibration_data, i)
            state_next = self.get_loop_state(calibration_data, i + 1)
            self.alignment[(i, i+1)] = self.compute_alignment(state_i, state_next)
    
    def quantize_with_alignment(self):
        """Apply quantization with cross-loop alignment"""
        for name, module in self.model.named_modules():
            if isinstance(module, nn.Linear):
                # Apply per-role scaling
                scaled_weight = module.weight * self.role_scales[loop_idx]
                module.weight = self.quantize(scaled_weight, self.n_bits)
```

## Application Scenarios

**Scenario 1: Parameter-efficient deployment** — LoopLMs achieve deep computation with fewer parameters; LoopQ enables their quantized deployment on edge devices.

**Scenario 2: Multi-role models** — When a single block plays different roles at different iterations, standard PTQ fails due to distribution mismatch.

## Pitfalls

- **Calibration data must cover all loop roles** — Use diverse inputs spanning the full loop trajectory
- **Error accumulation is multiplicative** — Even 1% per-loop error becomes (1.01)^n after n loops; must be < 0.1% per loop for 4+ loops
- **Shared backbone constraint** — Cannot quantize each loop iteration independently; must maintain shared quantized weights

## Activation

循环Transformer量化, LoopQ quantization, looped model PTQ, recursive Transformer compression, loop-aware quantization, parameter-efficient LM deployment
