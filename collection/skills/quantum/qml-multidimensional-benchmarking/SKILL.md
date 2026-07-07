---
name: qml-multidimensional-benchmarking
description: "Multidimensional benchmarking framework for comparing Quantum vs Classical ML models across accuracy, runtime, parameter count, and memory. Provides practical operating points (qubit count, sample size) that balance accuracy vs cost. Use when: deciding whether to use QML vs classical ML, benchmarking quantum advantage, resource allocation for ML pipelines, parameter/memory efficiency analysis."
arxiv_id: "2605.27923"
paper_title: "Do We Really Need Quantum Machine Learning?: A Multidimensional Empirical Study"
authors: "Sudip Vhaduri, Ryan Gammon, Sayanton Dibbo"
category: ai_collection
---

# QML Multidimensional Benchmarking

## Description

Systematic benchmarking methodology from arXiv:2605.27923 (May 2026). Compares classical and quantum ML models for image recognition across four performance dimensions: **classification accuracy**, **computational runtime**, **parameter count**, and **memory requirements**. Experiments conducted as functions of feature dimensionality and sample size, across CPU and GPU execution environments.

**Activation**: QML benchmarking, quantum vs classical ML comparison, quantum ML resource efficiency, QML parameter count, quantum memory efficiency, quantum ML decision framework, 量子机器学习基准测试, qml accuracy comparison, QML operating points

## Core Methodology

### Four-Dimensional Evaluation Framework

Compare any pair of classical/quantum models across these dimensions:

| Dimension | Classical | Quantum | Key Finding |
|-----------|-----------|---------|-------------|
| **Accuracy** | CSVM ~0.85, CCNN >0.96 | QSVM ~0.90, QCNN >0.96 | QSVM beats CSVM; CNNs comparable |
| **Runtime** | Faster | Slower | Classical wins on speed |
| **Parameter Count** | Higher | ~94% fewer | Quantum wins dramatically |
| **Memory** | Higher | ~75% less | Quantum wins significantly |

### Model Families Benchmarked

**SVM-based:**
- CSVM (Classical Support Vector Machine)
- QSVM (Quantum Support Vector Machine with quantum kernel)

**Neural Network-based:**
- CCNN (Classical Convolutional Neural Network)
- QCNN (Quantum Convolutional Neural Network)

### Key Operating Points

From the empirical study, two critical operating points emerge:

1. **Qubit-Sample Sweet Spot**: 10 qubits + 200-500 samples
   - Balances QSVM accuracy and runtime
   - Below 200 samples: accuracy too low
   - Above 500 samples: runtime too high
   - 10 qubits: manageable circuit depth

2. **Feature Scaling Regime**: 64 features + 60,000 samples
   - CCNN and QCNN both exceed 0.96 accuracy
   - QCNN: 94% fewer parameters, 75% less memory
   - Quantum advantage emerges at higher feature counts

## Decision Framework

### When to Use Quantum ML

| Condition | Recommendation |
|-----------|---------------|
| High feature dimensionality | ✅ QML — accuracy gap widens |
| Large sample size | ✅ QML — parameter/memory savings matter |
| Resource-constrained deployment | ✅ QML — 94% fewer parameters |
| Low-latency requirement | ❌ Classical — quantum is slower |
| Small feature dimension (<10) | ❌ Classical — overhead outweighs benefits |
| Very small datasets (<200) | ❌ Classical — quantum accuracy suffers |

### Step-by-Step Benchmarking Protocol

```
Step 1: Define the Problem
- Dataset: X (samples), D (features), C (classes)
- Hardware: CPU, GPU, or quantum simulator/QPU
- Budget: max_runtime, max_memory, max_parameters

Step 2: Establish Classical Baseline
- Train CSVM → record accuracy_cs, runtime_cs, params_cs, mem_cs
- Train CCNN → record accuracy_cc, runtime_cc, params_cc, mem_cc

Step 3: Run Quantum Experiments
- Sweep: n_qubits ∈ {4, 8, 10, 12, 16}
- Sweep: n_samples ∈ {100, 200, 500, 1000, 5000}
- For each (n_qubits, n_samples):
  - Train QSVM → accuracy_qs, runtime_qs
  - Train QCNN → accuracy_qc, runtime_qc, params_qc, mem_qc

Step 4: Compute Efficiency Ratios
- Parameter efficiency = params_classical / params_quantum
- Memory efficiency = mem_classical / mem_quantum
- Accuracy gap = accuracy_quantum - accuracy_classical
- Runtime overhead = runtime_quantum / runtime_classical

Step 5: Identify Operating Points
- Find (n_qubits, n_samples) where:
  accuracy_quantum >= accuracy_classical AND
  parameter_efficiency > 2x AND
  runtime_overhead < acceptable_threshold
```

## Scaling Laws

From the empirical data, the following scaling behaviors emerge:

### SVM Family Scaling
```
Accuracy(QSVM) - Accuracy(CSVM) ~ +0.05 at 1000 samples
Runtime(QSVM) / Runtime(CSVM) ~ 10-100x (depends on simulator)
```

### Neural Network Scaling
```
Parameters(QCNN) / Parameters(CCNN) ~ 0.06 (94% reduction)
Memory(QCNN) / Memory(CCNN) ~ 0.25 (75% reduction)
Accuracy(QCNN) ≈ Accuracy(CCNN) at sufficient data
```

### Feature Dimension Scaling
```
For both families: quantum advantage gap increases with feature dimensionality
Quantum models consistently outperform classical by greater margins
as feature dimensionality or sample size increases
```

## Implementation Template

```python
class QMLBenchmark:
    """Multidimensional QML vs Classical benchmarking framework."""
    
    dimensions = ['accuracy', 'runtime', 'parameters', 'memory']
    
    def __init__(self, dataset, n_qubits_range, n_samples_range):
        self.dataset = dataset
        self.n_qubits_range = n_qubits_range
        self.n_samples_range = n_samples_range
        self.results = {}
    
    def run_sweep(self):
        """Run full parameter sweep across all dimensions."""
        for n_q in self.n_qubits_range:
            for n_s in self.n_samples_range:
                self.results[(n_q, n_s)] = {
                    'cs': self.run_csvm(n_s),
                    'qs': self.run_qsvm(n_q, n_s),
                    'cc': self.run_ccnn(n_s),
                    'qc': self.run_qcnn(n_q, n_s),
                }
    
    def find_operating_point(self, min_accuracy=0.90, 
                              max_runtime_ratio=50,
                              min_param_efficiency=2):
        """Find practical operating points balancing all criteria."""
        for (nq, ns), r in self.results.items():
            param_eff = r['cc']['params'] / r['qc']['params']
            runtime_ratio = r['qc']['runtime'] / r['cc']['runtime']
            if (r['qc']['accuracy'] >= min_accuracy and
                runtime_ratio <= max_runtime_ratio and
                param_eff >= min_param_efficiency):
                return nq, ns, r
        return None
```

## Pitfalls

1. **Simulator overhead**: QSVM/QCNN runtime on classical simulators includes exponential
   simulation overhead. On real QPU, runtime profile changes.
   
2. **Sample size effects**: Below 200 samples, QSVM accuracy drops significantly.
   The quantum kernel needs sufficient data to learn effective decision boundaries.

3. **Feature count vs qubit count**: With amplitude encoding, D features need log₂(D) qubits.
   But angle encoding needs D qubits for D features. Choose encoding based on qubit budget.

4. **GPU vs CPU**: Classical CCNN benefits more from GPU acceleration than QSVM.
   Always compare on equivalent hardware where possible.

5. **Parameter counting**: QCNN parameters are quantum gate angles, not weight matrices.
   Direct comparison of "parameter count" requires careful definition of what counts.

## Practical Recommendations

### For Research
- Start with 10 qubits, 200-500 samples as baseline
- Compare QSVM vs CSVM for initial proof of concept
- Move to QCNN vs CCNN for full comparison

### For Production
- Use QML when parameter/memory constraints are critical
- Accept 10-100x runtime overhead for 94% parameter savings
- Hybrid approach: classical preprocessing + quantum classifier

### For Decision Making
- If your priority is accuracy + resource efficiency → QML
- If your priority is speed → Classical
- If feature dimension > 64 and sample size > 1000 → Strong QML candidate

## References

- **Paper**: "Do We Really Need Quantum Machine Learning?: A Multidimensional Empirical Study"
- **arXiv**: 2605.27923
- **Date**: May 27, 2026
- **Authors**: Sudip Vhaduri, Ryan Gammon, Sayanton Dibbo
- **Categories**: cs.CV, cs.AI, cs.LG, quant-ph
- **Dataset**: MNIST handwritten digits
