---
name: quantum-timeseries-transformer-fmri
description: "Quantum Time-series Transformer (QTS) methodology for resting-state fMRI analysis using Linear Combination of Unitaries (LCU) and Quantum Singular Value Transformation (QSVT). Achieves polylogarithmic complexity with superior small-sample performance. Activation: quantum transformer fMRI, quantum time-series, QTS, quantum fMRI analysis, resting-state quantum."
---

# Quantum Time-series Transformer (QTS) for fMRI

Quantum-enhanced transformer architecture for resting-state fMRI analysis leveraging Linear Combination of Unitaries (LCU) and Quantum Singular Value Transformation (QSVT).

**Source**: arXiv:2509.00711 — "Resting-state fMRI Analysis using Quantum Time-series Transformer"
**Authors**: Junghoon Justin Park, Jungwoo Seo, Sangyoon Bae, Samuel Yen-Chi Chen, Huan-Hsin Tseng, Jiook Cha, Shinjae Yoo
**Categories**: eess.IV, cs.CE, cs.LG

## Core Methodology

### Quantum Time-series Transformer Architecture

1. **Linear Combination of Unitaries (LCU)**: Decomposes self-attention into unitary operations executable on quantum hardware
2. **Quantum Singular Value Transformation (QSVT)**: Performs matrix functions (e.g., attention weights) with polylogarithmic query complexity
3. **Quantum State Encoding**: Maps fMRI time-series into quantum amplitude states for efficient processing

### Key Advantages

- **Polylogarithmic Complexity**: O(polylog(N)) vs classical O(N^2) for self-attention
- **Small-Sample Superiority**: Quantum advantage most pronounced when training data is limited
- **Parameter Efficiency**: Achieves comparable/better performance with fewer trainable parameters
- **Clinical Interpretability**: SHAP analysis reveals meaningful neural biomarkers

## Implementation Workflow

### Step 1: Data Preparation

```python
# fMRI time-series preprocessing
# Input: resting-state fMRI BOLD signals (regions x timepoints)
# Output: quantum state amplitudes

def prepare_fmri_data(bold_signals):
    """Preprocess fMRI BOLD signals for quantum encoding."""
    # 1. Temporal filtering (bandpass 0.01-0.1 Hz)
    # 2. Spatial normalization to standard atlas
    # 3. Amplitude encoding: normalize each region's time-series
    # 4. Quantum state preparation via amplitude encoding
    return quantum_states
```

### Step 2: Quantum Self-Attention via LCU + QSVT

```python
# Quantum attention computation
# Classical: Attention = softmax(QK^T / sqrt(d)) V  — O(N^2)
# Quantum: Use QSVT to compute matrix functions in O(polylog(N))

def quantum_self_attention(query_state, key_state, value_state):
    """Compute attention using quantum primitives."""
    # 1. Encode Q, K, V as quantum states
    # 2. Use QSVT to compute QK^T efficiently
    # 3. Apply softmax via quantum amplitude amplification
    # 4. Multiply with V via quantum matrix multiplication
    return attention_output
```

### Step 3: Quantum Classification Head

```python
# Quantum classifier for downstream tasks
# e.g., ADHD diagnosis, subject identification

def quantum_classifier(quantum_features):
    """Variational quantum classifier on transformer output."""
    # 1. Apply parameterized quantum circuit (PQC)
    # 2. Measure expectation values
    # 3. Classical post-processing for final prediction
    return predictions
```

## Validation Protocol

### Datasets (as used in paper)
1. **ABCD Study** (Adolescent Brain Cognitive Development): Largest-scale fMRI dataset
2. **UK Biobank**: Large population-scale neuroimaging dataset

### Evaluation Metrics
- Prediction accuracy (classification/regression)
- Sample efficiency (performance vs. training set size)
- Parameter count comparison with classical transformers
- SHAP interpretability scores for biomarker identification

### Key Results from Paper
- Comparable or superior performance vs. SOTA classical transformers
- **Especially pronounced gains in small-sample scenarios**
- SHAP analysis reveals clinically meaningful ADHD biomarkers
- Polylogarithmic complexity enables scalable analysis

## Pitfalls

### Quantum Hardware Requirements
- LCU and QSVT require fault-tolerant quantum hardware
- Current NISQ devices cannot execute full QTS architecture
- Use classical simulation for algorithm development (exponential overhead)

### Data Encoding Bottleneck
- Quantum state preparation (amplitude encoding) is non-trivial
- O(N) classical-to-quantum data loading may negate quantum advantage
- Consider quantum RAM (QRAM) or efficient encoding schemes

### Interpretability
- Quantum attention weights are not directly observable
- Use classical proxy models or measurement-based interpretation
- SHAP analysis requires classical post-processing of quantum outputs

## When to Use

- **Trigger**: Need to analyze resting-state fMRI with limited training data
- **Trigger**: Looking for quantum advantage in neuroimaging
- **Trigger**: Building quantum-enhanced brain-computer interface systems
- **Trigger**: Small-sample clinical neuroscience studies
- **Avoid**: When large datasets are available (classical transformers suffice)
- **Avoid**: When real-time processing is required (quantum overhead)

## Related Skills

- [[stochastic-quantum-neural-network-ai]] — Stochastic QNNs for AI
- [[quantum-neural-network-designer]] — QNN architecture design
- [[quantum-ml-patterns]] — QML research patterns
- [[neuroscience-of-transformers]] — Transformers for brain data modeling
