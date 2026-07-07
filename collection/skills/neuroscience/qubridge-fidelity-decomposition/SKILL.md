---
name: qubridge-fidelity-decomposition
description: >
  Pipeline analysis tool for decomposing quantum computation fidelity contributions by decision
  layer. Use when analyzing how different compilation decisions (qubit selection, gate scheduling,
  pulse shaping, error detection) contribute to final circuit output quality, or when optimizing
  quantum circuit execution under calibrated noise models. Based on arXiv:2605.11529 (QuBridge).
  Activation: quantum fidelity decomposition, compilation pipeline analysis, qubridge, fidelity
  contribution, quantum ablation, error detection encoding, qubit selection optimization,
  pulse shape assignment, quantum computation pipeline.
tags: [quantum-fidelity, compilation-pipeline, ablation-analysis, noise-models, IBMQ]
arxiv_id: "2605.11529"
paper_title: "QuBridge: Layer-wise Fidelity Decomposition in Quantum Computation Pipeline"
authors: "Kisho Sotokawa, Hideaki Kawaguchi, Shin Nishio, Takahiko Satoh"
---

# QuBridge: Layer-wise Fidelity Decomposition

## Problem

Running a quantum circuit on current hardware involves sequential engineering decisions,
each with tunable parameters and distinct error characteristics. Existing tools optimize
each decision in isolation, making it impossible to determine how much each decision
contributes to final output quality.

## QuBridge Methodology

### Three Decision Layers

1. **Qubit Selection**: Which physical qubits to use
2. **Gate Pulse Assignment**: Pulse shapes for each gate
3. **Error Detection Encoding**: Whether and how to use error-detecting codes

### Analysis Method

```
Progressive Ablation → Isolate each layer's fidelity contribution
  → Hold downstream layers fixed
  → Measure fidelity band narrowing
  → Attribute gains to upstream vs downstream decisions
```

## Key Findings

### 1. Qubit Selection Dominates
- Narrows worst-case fidelity band from **11.8% to < 2%**
- Does not change peak fidelity (that is determined by downstream layers)
- Most impactful single decision in the pipeline

### 2. Per-Gate Pulse Shaping Adds Marginal Gains
- **+0.9% residual gain** after optimal qubit selection
- Magnitude depends on upstream layout quality
- Diminishing returns when qubit selection is already optimized

### 3. Error Detection is Context-Dependent
- **Not uniformly advantageous** across all input states
- Conditional benefit emerges when:
  - Input state's dominant error channel is detectable by chosen code
  - Noise profile matches error-detection capability

## Usage

### Evaluating a quantum compilation pipeline

1. Decompose pipeline into decision layers
2. Fix downstream layers, sweep upstream decisions
3. Measure fidelity range at each layer
4. Identify the layer with widest fidelity band (highest impact)
5. Focus optimization effort on that layer

### When NOT to use error detection

- Input state error channels are not aligned with code detection capability
- Noise is dominated by undetectable error types
- Overhead of encoding exceeds fidelity benefit

### Practical implementation

```python
# Layer-wise ablation pattern
for layer in pipeline_layers:
    baseline_fidelity = measure(circuit, fixed_downstream=True)
    optimized_fidelity = optimize_and_measure(layer, downstream_fixed=True)
    contribution = optimized_fidelity - baseline_fidelity
    print(f"{layer}: +{contribution:.3%}")
```

## Operating Constraints

- Operates on **cached calibration data** without live hardware access
- Tested under IBM-calibrated noise models
- Analysis methodology generalizes to other backends

## Related Skills

- `tuniq-quantum-compiler-rl`: RL-based compilation pass optimization
- `quantum-compiler-routing`: Qubit mapping and routing
- `quantum-fault-tolerance-blocks`: Fault-tolerant building blocks

## References

- arXiv: https://arxiv.org/abs/2605.11529
- PDF: https://arxiv.org/pdf/2605.11529
