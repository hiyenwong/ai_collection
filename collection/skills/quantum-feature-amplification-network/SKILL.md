---
name: quantum-feature-amplification-network
description: "Quantum Feature Amplification Network (QFAN) methodology for autoregressive quantum generative modeling with fixed qubit budget. Use when generating quantum images, designing quantum generative models, or reducing qubit requirements for quantum demonstrations."
---

# Quantum Feature Amplification Network (QFAN)

## Description

Quantum generative models tie the required qubit register size to the output image dimension, creating a fundamental bottleneck for detector-scale applications. QFAN removes this bottleneck by generating images autoregressively as sequences of blocks, reusing a small parameterized quantum circuit conditioned on compressed summaries of previously generated pixels.

## Core Innovation

Instead of a one-to-one qubit-to-pixel mapping, QFAN:
1. **Generates in blocks**: Each block produced by same small quantum circuit
2. **Reuses circuit**: Fixed qubit requirement by block size, not full image
3. **Autoregressive conditioning**: Each step conditioned on compressed summary of prior pixels
4. **Per-step cost independent of image size**: For Pauli-observable family

## Key Results

- **3-qubit circuit with 12 shared variational parameters** reproduces calorimeter shower distributions
- **Closed-form ridge decoders** + post-hoc residual sampler
- **Hardware verified**: IBM quantum hardware, simulator gap consistent with optimization-budget limits (not device noise)
- **Shot-noise propagation bound**: Conservative worst-case bound derived through generation chain
- **Empirical decoder-capacity heuristic** for reachable sequential depth

## Architecture

```
[Compressed Summary] → [Small Parameterized Quantum Circuit] → [Block Output]
         ↑                                                      ↓
         └────────────── Autoregressive Loop ───────────────────┘
```

### Components:
1. **Parameterized Quantum Circuit (PQC)**: Fixed small circuit, reused per block
2. **Compression Encoder**: Compresses generated pixels into summary state
3. **Ridge Decoder**: Maps quantum measurement outcomes to pixel values
4. **Residual Sampler**: Post-hoc refinement for distribution accuracy

## Implementation Pattern

```python
# QFAN autoregressive generation loop
for block_idx in range(num_blocks):
    # Compress previously generated pixels into summary
    summary = compress_summary(generated_pixels)
    
    # Run small quantum circuit conditioned on summary
    quantum_state = run_pqc(summary, variational_params)
    
    # Measure Pauli observables
    measurements = measure_observables(quantum_state)
    
    # Decode measurements to pixel values
    new_pixels = ridge_decode(measurements, decoder_weights)
    
    # Append to generated output
    generated_pixels.append(new_pixels)
```

## Activation Keywords
- quantum feature amplification
- QFAN
- autoregressive quantum generation
- quantum generative model blocks
- quantum image generation
- qubit-efficient quantum generative
- 量子特征放大
- 量子自回归生成

## Tools Used
- exec: Run quantum circuit simulations (Qiskit, PennyLane)
- read: Load quantum circuit configurations
- write: Save generation results

## Usage Patterns

### Quantum Image Generation with Fixed Qubits
Generate large images using small quantum circuits through autoregressive block generation.

### Hardware-Efficient Quantum Generative Models
Deploy on near-term hardware with limited qubits by reusing circuits.

## Error Handling

### Shot Noise Accumulation
- Use conservative worst-case bound on shot-noise propagation
- Increase shots for deeper autoregressive chains
- Apply empirical decoder-capacity heuristic to limit sequential depth

### Optimization Budget Limits
- Hardware-simulator gap dominated by optimization budget, not device noise
- Allocate more optimization iterations before attributing to noise

## Related Papers
- arXiv:2605.16044 - QFAN: Quantum Feature Amplification Network
- arXiv:2605.15370 - Quantum Feature Pyramid Gating
