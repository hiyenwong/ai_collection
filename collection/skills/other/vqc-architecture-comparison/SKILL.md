---
name: vqc-architecture-comparison
description: >
  Systematic VQC architecture comparison methodology for quantum machine learning on tabular data.
  Evaluates four VQC families — FC-VQC, ResNet-VQC, Quantum Transformer, Fully Quantum Transformer —
  across regression and classification benchmarks. Use when selecting quantum circuit architectures
  for tabular ML tasks, benchmarking VQC designs, or analyzing accuracy-parameter tradeoffs
  in near-term quantum machine learning.
  Activation: VQC architecture, quantum transformer, variational quantum circuit comparison,
  quantum tabular learning, QML benchmark, VQC design selection
---

# VQC Architecture Comparison for Tabular Benchmarks

## Core Idea

Variational quantum circuits are a leading approach to QML on NISQ devices, but it remains unclear which circuit architecture yields the best accuracy-parameter tradeoff on classical tabular data.

This methodology systematically compares four VQC families:
1. **FC-VQC**: Multi-layer fully-connected parameterized circuits
2. **ResNet-VQC**: Residual-connected quantum circuits
3. **QT**: Hybrid quantum-classical transformer
4. **FQT**: Fully quantum transformer

## Architecture Analysis

### FC-VQC (Fully-Connected)
- **Structure**: Dense parameterized gates across all qubits per layer
- **Parameters**: O(n²) per layer for n qubits
- **Strengths**: Maximum expressivity per layer
- **Weaknesses**: Deep circuits, prone to barren plateaus
- **Best for**: Small datasets, few qubits

### ResNet-VQC (Residual)
- **Structure**: Skip connections between quantum layers
- **Parameters**: O(n²) per layer, but effective depth reduced
- **Strengths**: Mitigates vanishing gradient, trainable at greater depth
- **Weaknesses**: Still suffers from noise accumulation
- **Best for**: Medium-depth circuits, structured data

### QT (Hybrid Quantum-Classical Transformer)
- **Structure**: Classical attention + quantum feature maps
- **Parameters**: Split between classical attention weights and quantum gates
- **Strengths**: Leverages classical attention for long-range dependencies
- **Weaknesses**: Classical-quantum interface overhead
- **Best for**: Mixed classical-quantum workflows

### FQT (Fully Quantum Transformer)
- **Structure**: Quantum attention mechanism with swap tests
- **Parameters**: Fully quantum, no classical components
- **Strengths**: Fully exploits quantum parallelism
- **Weaknesses**: Very deep circuits, NISQ-unfriendly
- **Best for**: Future fault-tolerant devices

## Evaluation Framework

```python
def evaluate_vqc_architectures(benchmarks, n_qubits_list, depth_list):
    architectures = ['FC-VQC', 'ResNet-VQC', 'QT', 'FQT']
    results = {}
    for arch in architectures:
        for n_qubits in n_qubits_list:
            for depth in depth_list:
                circuit = build_circuit(arch, n_qubits, depth)
                accuracy, params, time = train_and_evaluate(circuit, benchmarks)
                results[(arch, n_qubits, depth)] = {
                    'accuracy': accuracy,
                    'parameters': params,
                    'training_time': time
                }
    return results
```

## Key Findings

- No single architecture dominates across all benchmarks
- ResNet-VQC provides best accuracy-parameter tradeoff for most tasks
- Quantum transformers (QT/FQT) show promise but require more qubits
- FC-VQC is best baseline but degrades rapidly with depth

## When to Use

- Selecting VQC architecture for tabular QML tasks
- Designing quantum neural network architectures
- Benchmarking quantum vs. classical performance
- Analyzing scaling behavior of quantum circuits

## Related Papers

- arXiv:2604.23931 - "Do Quantum Transformers Help? A Systematic VQC Architecture Comparison on Tabular Benchmarks"

## Pitfalls

- Results are benchmark-dependent — may not generalize to all domains
- NISQ noise significantly affects deep architectures
- Parameter count is not the only factor — gate connectivity matters
