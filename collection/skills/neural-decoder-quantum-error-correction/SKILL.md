name: neural-decoder-quantum-error-correction
description: >
  Neural decoder-based quantum error correction methodology. Combines deep
  learning with topological error correction codes for high-fidelity quantum
  computation. Use when: (1) Implementing ML-based decoders for QEC codes,
  (2) Comparing neural decoders to traditional MWPM, (3) Designing
  real-time error correction for surface/toric codes, (4) Analyzing decoder
  performance under circuit-level noise. Trigger: neural decoder QEC, ML
  error correction, neural surface code, deep learning quantum decoder.
---

# Neural Decoder Quantum Error Correction

Deep learning-based decoders for quantum error correction (QEC) that
outperform traditional algorithms (MWPM, belief propagation) in speed and
adaptability to realistic noise models.

## Key Principles

- **Pattern Recognition**: Neural decoders learn error syndromes →
  correction mappings from training data rather than relying on simplified
  noise models
- **Real-Time Capability**: Trained models decode in microseconds, enabling
  real-time feedback for fault-tolerant QC
- **Circuit-Level Noise**: Handle correlated errors from actual gate sequences
- **Code Families**: Surface code, color code, toric code, LDPC codes

## Architecture Patterns

### 1. CNN-Based Decoders (Surface Code)
```python
# Syndrome → correction via convolutional network
syndrome_input = (d, d, 2)  # d×d lattice, X+Z stabilizers
conv_layers = [Conv2D(64, 3, relu), Conv2D(128, 3, relu)]
output = Dense(d*d, sigmoid)  # per-qubit correction probabilities
```

### 2. Transformer-Based Decoders
```python
# Self-attention over syndrome graph
syndrome_tokens = LinearProjection(syndrome_positions)
attn = MultiHeadSelfAttention(tokens, n_heads=8)
correction = MLP(attn_output)
```

### 3. Graph Neural Network Decoders
```python
# Natural graph structure of stabilizer codes
G = build_syndrome_graph(syndrome)  # nodes=syndromes, edges=adjacency
x = GNN_convolution(G, node_features)
correction = GNN_readout(x)
```

## Training Workflow

1. **Data Generation**: Simulate syndrome data under target noise model
   ```python
   syndromes, errors = simulate_surface_code(d=5, p=0.01, n_samples=100000)
   ```
2. **Model Training**: Cross-entropy on correction predictions
   ```python
   loss = BCEWithLogits(predictions, target_corrections)
   # Optional: logical error rate as differentiable reward
   ```
3. **Evaluation**: Measure logical error rate vs physical error rate
   ```python
   logical_error_rates = [evaluate(model, d, p) for p in noise_levels]
   threshold = find_threshold(logical_error_rates)
   ```

## Performance Benchmarks

| Decoder | Speed | Accuracy | Adaptability |
|---------|-------|----------|-------------|
| MWPM | O(n³) | Optimal (depolarizing) | Poor |
| BP | O(n) | Suboptimal | Moderate |
| CNN | O(1) inference | Near-optimal | High |
| Transformer | O(n) inference | Near-optimal | High |
| GNN | O(n) inference | Near-optimal | High |

## Error Types to Handle

- **Depolarizing noise**: X, Y, Z with equal probability
- **Biased noise**: Z errors dominant (superconducting qubits)
- **Circuit-level noise**: Gate errors, measurement errors, idling errors
- **Correlated noise**: Crosstalk, leakage, spatially correlated errors

## Implementation Checklist

- [ ] Generate training data with realistic noise models
- [ ] Choose architecture matching code topology
- [ ] Train with data augmentation for symmetry
- [ ] Validate logical error rate below code threshold
- [ ] Benchmark inference latency for real-time requirements
- [ ] Test generalization to unseen noise parameters

## Related Concepts

- Surface code, toric code, color code
- Minimum-weight perfect matching (MWPM)
- Belief propagation decoders
- Fault-tolerant quantum computation
- Code concatenation and code switching
