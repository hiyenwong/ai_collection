---
name: rhythm-switching-adaptive-time-constants-rnn
description: "Multiple mechanisms of rhythm switching in recurrent neural networks (RNNs) with adaptive/learnable time constants. Analyzes how RNNs switch between rhythms across multiple frequency bands (theta, alpha, beta, gamma) and how neuronal time constants relate to rhythm-specific functional differentiation. Use when: (1) studying RNN rhythm switching mechanisms, (2) analyzing neuron-specific time constant learning in recurrent networks, (3) understanding frequency-band-specific functional differentiation in neural systems, (4) investigating degeneracy of learned solutions in RNNs, (5) examining active subpopulation turnover and baseline shift mechanisms in trained RNNs, (6) modeling cognitive flexibility through rhythm switching."
---

# Rhythm Switching with Adaptive Time Constants in RNNs

Methodology from arXiv:2605.14388 (Yamaguti & Nakamura, 2026).

## Core Contribution

Trained leaky integrator RNNs with **neuron-specific learnable time constants** on a four-band (theta, alpha, beta, gamma) rhythm-switching task. Analyzed 20 independently trained networks to reveal the internal mechanisms of rhythm switching.

## Key Findings

### 1. Frequency-Dependent Subpopulation Organization

| Frequency | Participation | Dominant Neurons |
|-----------|--------------|------------------|
| Low (theta) | Distributed (many neurons) | No clear dominance |
| High (gamma) | Concentrated (small subpopulation) | Short-time-constant neurons |

- **Negative correlation** between time constant and matched-mode amplitude **strengthens monotonically with frequency**
- High-frequency rhythms are dominated by a small subpopulation of short-time-constant neurons

### 2. Three Coexisting Rhythm Switching Mechanisms

1. **Subpopulation turnover**: Different subsets of neurons become active for different rhythms
2. **Network-wide baseline shifts**: Reposition the operating point near distinct unstable fixed points
3. **Inter-neuronal phase reorganization**: Selectively cancels or supports band components in population output

### 3. Degeneracy of Solutions

- The mechanism deployed for each mode pair **varied across training runs**
- Multiple distinct internal solutions achieve the same behavioral output
- Parallels the coexistence of rhythm-specific and multi-rhythm interneurons in biological circuits

## RNN Model Specification

### Leaky Integrator with Learnable Time Constants

\[
\tau_i \frac{dh_i}{dt} = -h_i + \sum_j W_{ij} \phi(h_j) + b_i + u_i(t)
\]

where:
- \(\tau_i\): neuron-specific time constant (learnable)
- \(h_i\): hidden state
- \(W_{ij}\): recurrent weights
- \(\phi\): activation function (typically tanh)
- \(u_i(t)\): input signal specifying target frequency band

### Training Task

- Input: one-hot encoding of target frequency band (theta/alpha/beta/gamma)
- Output: sinusoidal signal at the specified frequency
- Loss: MSE between generated and target oscillation

## Analysis Pipeline

### 1. Time Constant Distribution Analysis
- Plot distribution of learned \(\tau_i\) values
- Check for bimodality or clustering

### 2. Mode-Amplitude Correlation
- Compute matched-mode amplitude for each frequency band
- Correlate with time constants across neurons
- Verify monotonic strengthening with frequency

### 3. Mechanism Decomposition
For each rhythm transition, identify which mechanism dominates:
- **Subpopulation turnover**: Track which neurons are active in each band
- **Baseline shift**: Compute mean activity level across the network
- **Phase reorganization**: Analyze phase relationships between neuron pairs

### 4. Cross-Run Comparison
- Compare mechanisms across independently trained networks
- Quantify solution degeneracy

## Implications for Biological Systems

1. **Functional differentiation**: Short-time-constant neurons specialize for high-frequency processing
2. **Degeneracy**: Multiple neural implementations can produce identical behavior
3. **Multi-rhythm neurons**: Some neurons participate in multiple bands, parallel to biological findings

## Related Skills

- `neural-population-dynamics` - Neural population analysis methods
- `rhythm-switching-adaptive-time-constants-rnn` - This skill
