---
name: shot-based-quantum-encoding
description: >
  Shot-Based Quantum Encoding (SBQE) methodology for quantum neural network data loading.
  Addresses the bottleneck of inefficient data loading on NISQ devices by distributing shots
  according to data-dependent classical distributions over multiple input states. Use when
  designing QML data loading strategies, optimizing quantum encoding for near-term hardware,
  or comparing encoding schemes (angle, amplitude, basis, shot-based). 
  Activation: shot-based encoding, SBQE, quantum data loading, quantum encoding, 
  data loading QNN, quantum neural network encoding, quantum embedding strategy
---

# Shot-Based Quantum Encoding (SBQE)

## Core Idea

Efficient data loading is a bottleneck for near-term QML. Traditional schemes (angle, amplitude, basis encoding) either underuse Hilbert-space capacity or require circuit depths exceeding NISQ coherence budgets.

SBQE distributes the hardware's native resource — shots — according to a data-dependent classical distribution over multiple input states, achieving better expressivity with shallower circuits.

## Key Insights

1. **Shot allocation as encoding**: Instead of deep circuits, use classical probability distributions to decide which quantum states to prepare, then allocate shots accordingly
2. **Hardware-native resource**: Shots are the natural resource on NISQ devices — SBQE optimizes directly for this constraint
3. **Expressivity-depth tradeoff**: Achieves comparable expressivity to deep encoding circuits with significantly fewer gates

## Encoding Strategies Comparison

| Strategy | Circuit Depth | Expressivity | NISQ-Friendly |
|----------|--------------|--------------|---------------|
| Angle Encoding | Low | Moderate | Yes |
| Amplitude Encoding | High | High | No |
| Basis Encoding | Moderate | Low-Moderate | Yes |
| **SBQE (Shot-Based)** | **Low** | **High** | **Yes** |

## Implementation Pattern

```python
def sbqe_encode(classical_data, n_states, n_shots):
    # Step 1: Classical preprocessing to probability distribution
    probs = classical_to_distribution(classical_data)
    # Step 2: Shot allocation proportional to distribution
    shot_counts = allocate_shots(probs, n_shots)
    # Step 3: Prepare each state, measure with allocated shots
    results = []
    for state_id, shots in enumerate(shot_counts):
        if shots > 0:
            circuit = prepare_state(state_id)
            result = run_circuit(circuit, shots=shots)
            results.append(result)
    # Step 4: Aggregate results as encoded representation
    return aggregate_results(results, shot_counts)
```

## When to Use

- Designing QML pipelines for NISQ devices
- Comparing data loading strategies for quantum neural networks
- Optimizing shot allocation for quantum inference
- Building hybrid quantum-classical encoding schemes

## Related Papers

- arXiv:2604.06135 - "Shot-Based Quantum Encoding: A Data-Loading Paradigm for Quantum Neural Networks"
- arXiv:2604.06523 - "Soft-Quantum Algorithms" (complementary: direct matrix optimization)

## Pitfalls

- SBQE requires careful design of the classical distribution — poor distributions lose information
- Not suitable for problems requiring deep quantum feature maps
- Works best when the classical data has structure that maps well to simple quantum states
