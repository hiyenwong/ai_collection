---
name: "qutrit-entropy-neural-estimation"
description: "Von Neumann entropy estimation in multi-qutrit systems using VQA and classical CNN approaches. CNN achieves accurate estimation using only 12.5% of full tomography measurements. Use when estimating quantum state entropy, benchmarking VQA ansatzes, or applying neural networks to quantum state characterization."
metadata:
  arxiv_id: "2606.20504"
  published: "2026-06-18"
  authors: "Daniel Molpeceres et al."
  tags: [quantum-entropy, qutrit, vqa, cnn, quantum-state-estimation, tomography]
---

# Qutrit Entropy Neural Estimation

## Core Idea

Estimate von Neumann entropy in multi-qutrit systems using two complementary approaches:
- **VQAs** (effective for small systems up to 3 qutrits)
- **Classical CNNs** (scale to 5+ qutrits, use only 12.5% of full tomography measurements)

## VQA Approach (Small Systems)

### SU(3)-Inspired Ansatzes
- 11 hardware-efficient ansatz architectures evaluated
- Accuracy primarily determined by number of trainable parameters (~120 optimal)
- Sufficient entanglement is prerequisite for accuracy
- Increasing entangling gates beyond threshold yields marginal improvements

### Parameter Sweep Results
- Fix parameter count to ~120 for balanced accuracy/complexity
- Beyond threshold, more entangling gates don't significantly improve results

## CNN Approach (Larger Systems)

### Architecture
- Classical CNN trained on measurement outcomes
- Uses tensor-product mutually unbiased bases (MUBs)
- Input: measurement outcome statistics
- Output: von Neumann entropy estimate

### Performance
- **2-5 qutrit systems**: Systematic improvement with system size
- **Measurement efficiency**: 12.5% of full tomography sufficient for 90th-percentile errors ~0.13-0.16 nats
- **Shot noise robustness**: Maintains accuracy under realistic measurement noise
- **OOD generalization**: Generalizes well to out-of-distribution states

## Decision Guide

| System Size | Recommended Method | Reason |
|------------|-------------------|--------|
| 1-2 qutrits | VQA | Simple, effective |
| 3 qutrits | VQA or CNN | Both viable |
| 4-5+ qutrits | CNN | Better scalability |
| Noisy hardware | CNN | Shot noise robustness |

## Workflow

1. **Determine system size**: Count qutrits in target system
2. **Choose method**: VQA for small, CNN for large
3. **VQA path**: Select ansatz, fix ~120 parameters, optimize
4. **CNN path**: Collect MUB measurements (12.5% of full set), train CNN
5. **Validate**: Compare against known entropy values if available

## Pitfalls

- **VQA entanglement requirement**: VQAs need sufficient entanglement in ansatz
- **CNN training data**: Requires diverse training set covering state space
- **MUB availability**: Mutually unbiased bases may not exist for all dimensions
- **Simulation-only**: Results validated on noiseless simulator — hardware performance TBD
- **Entropy range**: May not work well for extreme entropy values

## Activation Keywords

- quantum entropy estimation
- qutrit entropy
- von Neumann entropy neural
- VQA entropy
- quantum state tomography reduction
- MUB measurements
- multi-qutrit systems
