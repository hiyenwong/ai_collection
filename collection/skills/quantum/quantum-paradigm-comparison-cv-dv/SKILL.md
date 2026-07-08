---
name: quantum-paradigm-comparison-cv-dv
category: quantum
description: Controlled comparison methodology for continuous-variable (CV) vs discrete-variable (DV) quantum computing paradigms. Uses shared classical backbone with interchangeable quantum heads to isolate quantum circuit as sole variable. CV outperforms DV with 18-point accuracy gap on wafer-map defect classification.
tags: [quantum, CV, DV, comparison, quantum-machine-learning, paradigm]
arxiv_id: "2607.00961v1"
created: "2026-07-07"
---

# CV vs DV Quantum Paradigm Comparison

## Overview
When deploying quantum neural networks in industry, knowing which quantum computing paradigm suits which task is essential. This methodology provides a controlled comparison framework between continuous-variable (CV) and discrete-variable (DV) quantum computing paradigms, isolating the quantum circuit as the sole experimental variable.

## Core Methodology

### Controlled Experimental Design
To isolate the quantum circuit as the **sole variable**:
1. **Shared Backbone**: Use identical classical convolutional backbone (~4.3M parameters) for feature extraction
2. **Interchangeable Heads**: Swap only the classification head (classical dense, CV-QNN, or DV-QNN)
3. **Scale Variation**: Test each quantum head at multiple sizes (3, 4, 8 qumodes/qubits)
4. **Fixed Conditions**: Keep all other parameters constant (dataset, training procedure, evaluation)

### Key Finding: CV Superiority
At 4 qumodes/qubits on WM-811K wafer-map defect classification:
- **CV accuracy**: 79.7 ± 1.8%
- **DV accuracy**: 61.6 ± 1.4%
- **Gap**: Non-overlapping 18-point advantage for CV

### Fine-Grained Advantage
The CV advantage is sharpest on spatially localized defect types:
- **Edge-Loc class**: CV recall 0.66 ± 0.06 vs DV recall ≤ 0.05 at every size
- Edge-Loc is easily confused with Scratch — CV captures fine spatial distinctions that DV misses
- This shows the structured CV layer better captures spatial patterns

### Root Cause Analysis
- DV limitation is a **representational-capacity ceiling**, not an optimization failure
- At Fock cutoff d=2, CV advantage reflects:
  1. A structured, neural-network-analogue layer
  2. Continuous phase-space encoding
- Not simply Hilbert-space dimensionality

### Hardware Validation
On IBM hardware:
- DV accuracy holds at shallow depth
- Degrades only at the deepest circuit
- Both quantum heads remain below classical baseline (85.0%)

## Implementation Pattern

### Step 1: Choose Shared Backbone
- Select a classical feature extractor appropriate for the data modality
- Ensure sufficient capacity for the task
- Keep frozen during quantum head comparison

### Step 2: Implement Interchangeable Heads
```
Classical Baseline: backbone → dense layer → output
CV Head:            backbone → CV-QNN (qumodes) → output  
DV Head:            backbone → DV-QNN (qubits) → output
```

### Step 3: Scale Analysis
- Test at multiple sizes (small, medium, large)
- Plot accuracy vs size for each paradigm
- Identify where advantages emerge

### Step 4: Class-Level Analysis
- Don't just look at overall accuracy
- Analyze per-class performance to find where paradigms differ
- Identify which data characteristics favor which paradigm

## When to Use
- Choosing between CV and DV quantum computing for a specific task
- Benchmarking quantum vs classical approaches
- Understanding where quantum advantage might first appear
- Designing hybrid quantum-classical architectures
- Spatial pattern recognition tasks (image classification, defect detection)

## Activation Keywords
CV-QNN, DV-QNN, continuous-variable, discrete-variable, quantum paradigm comparison, wafer-map classification, quantum head, qumodes, qubits, Fock cutoff, phase-space encoding, quantum benchmark
