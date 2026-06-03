---
name: quantum-feature-map-benchmarking
description: "Matched spectral benchmarking methodology for quantum-inspired feature maps. Evaluates amplitude, angle, and basis encoding as deterministic feature maps under matched output dimensionality with strong classical controls. Analyzes geometry through effective rank, condition number, CKA, and predictive performance. Key finding: fixed quantum-inspired encoding geometry alone is NOT a reliable ML advantage source on classical data. Activation: quantum feature map, quantum encoding benchmark, amplitude encoding, angle encoding, basis encoding."
---

# Quantum Feature Map Benchmarking Methodology

Based on arXiv:2605.24324 — "A Matched Spectral Benchmark of Quantum Inspired Feature Maps" by Ogunade, Kassim, Osaro (May 2026).

## Core Finding

**Fixed quantum-inspired encoding geometry alone is not a reliable source of machine learning advantage on classical data.** This is a crucial negative result that prevents wasted effort on naive quantum encoding approaches.

## Three Encoding Strategies Analyzed

### 1. Amplitude Encoding

**Mechanism:** Data vector → amplitudes of quantum state
```
|x⟩ = Σ_i x_i / ||x|| |i⟩
```

**Finding:** Removes magnitude information through unit-sphere normalization. All inputs mapped to unit sphere — loses scale information critical for many ML tasks.

**When to use:** Only when relative proportions matter, not absolute magnitudes.

### 2. Angle Encoding

**Mechanism:** Data values → rotation angles
```
|ψ⟩ = ⊗_i Ry(x_i * π) |0⟩
```

**Finding:** Becomes geometrically redundant with raw linear features. The encoding geometry doesn't add expressive power beyond what a simple linear model already has.

**When to use:** When data is naturally periodic or bounded to [0, π].

### 3. Basis Encoding

**Mechanism:** Binary features → computational basis states
```
|x₁, x₂, ...⟩ where x_i ∈ {0, 1}
```

**Finding:** Imposes a binary Hamming geometry that is poorly aligned with smooth decision structures in most real-world datasets.

**When to use:** Only for inherently binary/categorical data.

## Benchmark Protocol

### Step 1: Matched Output Dimensionality

Ensure fair comparison by matching the output dimensionality of quantum and classical feature maps:
```python
def matched_benchmark(quantum_features, classical_features):
    assert quantum_features.shape[1] == classical_features.shape[1]
    return compare_performance(quantum_features, classical_features)
```

### Step 2: Geometry Analysis

Evaluate each encoding through multiple geometric lenses:

```python
def analyze_geometry(features):
    metrics = {}
    
    # Effective rank — how many dimensions are actually used
    svd_values = np.linalg.svd(features, compute_uv=False)
    metrics['effective_rank'] = effective_rank(svd_values)
    
    # Condition number — numerical stability
    metrics['condition_number'] = svd_values[0] / svd_values[-1]
    
    # Centered Kernel Alignment (CKA) — similarity to target structure
    metrics['cka'] = centered_kernel_alignment(features, targets)
    
    return metrics
```

### Step 3: Strong Classical Controls

Always compare against strong classical baselines:
- **Raw linear models** — simplest possible baseline
- **Random Fourier features** — classical analog of quantum feature maps
- **Polynomial features** — classical high-dimensional expansion
- **PCA** — dimensionality-reduced features
- **RBF SVM** — non-linear classical model
- **Shallow neural networks** — standard deep learning baseline

### Step 4: Practical Overhead

Measure not just accuracy but also:
- Feature computation time
- Memory requirements
- Training time
- Inference latency

## Key Metrics

| Metric | What It Measures | Good Value |
|--------|-----------------|------------|
| Effective rank | Intrinsic dimensionality | Higher = richer features |
| Condition number | Numerical stability | Lower = more stable |
| CKA | Kernel alignment with targets | Higher = better alignment |
| Predictive accuracy | End-task performance | Higher = better |
| Practical overhead | Computational cost | Lower = more efficient |

## Decision Framework

```
Is quantum encoding better than classical?
├── No for amplitude encoding → loses magnitude info
├── No for angle encoding → redundant with linear features
└── No for basis encoding → poor geometry match

When might quantum encoding help?
├── When encoding is adaptive/learnable (not fixed)
├── When quantum dynamics are exploited (not just encoding)
└── When data has quantum structure (not classical data)
```

## Pitfalls

1. **Don't expect advantage from fixed encodings alone** — the encoding geometry itself doesn't create ML advantage
2. **Magnitude matters** — amplitude encoding destroys it; consider preserving scale information
3. **Match dimensionality** — unfair to compare 1024-d quantum features against 10-d classical
4. **Use strong baselines** — weak classical baselines give false impression of quantum advantage
5. **Consider practical overhead** — quantum feature computation may be slower than classical
6. **Focus on adaptive/learnable encodings** — fixed encodings are insufficient; learned quantum circuits may help

## When to Use Quantum Feature Maps

- **NOT** for simple classical data with fixed encodings
- **YES** when combined with quantum dynamics (entanglement, interference)
- **YES** for data with quantum structure
- **YES** with adaptive/parameterized encoding circuits
