---
name: spikf-go-spiking-fourier-graph
title: "SpikF-GO: Spiking Fourier Graph Operators for Multivariate Time Series Forecasting"
description: "First graph-based multivariate SNN framework for time series forecasting combining hypervariate graph formulation with spike-driven spectral processing and Hard Concrete frequency gating"
arxiv_id: "2606.13901"
authors: "Jafar Bakhshaliyev, Niels Landwehr"
date: "2026-06-11"
categories: ["cs.LG", "cs.NE"]
venue: "ECML PKDD 2026"
trigger_words: ["spiking neural network", "time series forecasting", "multivariate", "Fourier graph", "frequency gate", "Complex LIF", "hypervariate graph", "energy-efficient forecasting"]
---

# SpikF-GO: Spiking Fourier Graph Operators for Multivariate Time Series Forecasting

## Summary

SpikF-GO is the first framework to bring graph-based multivariate modeling into the spiking domain for time series forecasting (TSF). It combines a **hypervariate graph formulation** (every scalar observation → graph node) with **spike-driven spectral processing**, achieving state-of-the-art among SNN methods while consuming less energy than its ANN counterpart (FourierGNN).

## Core Innovation

Previous SNN forecasting methods process variables **independently**, missing inter-variable dependencies. SpikF-GO addresses this through:

1. **Hypervariate Graph Formulation**: Every scalar observation becomes a graph node, explicitly encoding cross-variable relationships
2. **Hard Concrete Frequency Gate**: Learnable sparse frequency selection in Fourier domain
3. **Complex LIF Gate**: Independent spiking neurons applied to real and imaginary Fourier components — preserving binary event-driven computation throughout spectral domain
4. **CPG Positional Encoding**: Central Pattern Generator-based encoding for stronger long-range temporal modeling (variant)

## Methodology

### Architecture
```
Multivariate Time Series
    → Hypervariate Graph Construction (scalar obs → nodes)
    → Fourier Transform
    → Hard Concrete Frequency Gate (sparse frequency selection)
    → Complex LIF Gate (separate real/imaginary spiking processing)
    → Inverse Fourier Transform
    → Forecast Output
```

### Key Design Choices
- **Fully spiking**: Binary, event-driven computation throughout
- **Graph-based**: Explicitly models variable dependencies (unlike prior SNN TSF)
- **Spectral domain**: Fourier processing enables efficient frequency selection
- **Energy-efficient**: Competitive accuracy at smaller embedding dimensions

## Results

- **Best average rank** among all SNN methods across 8 benchmarks
- **Outperforms FourierGNN** (ANN counterpart) at reduced energy cost
- **First unified comparison** across SNN forecasting architectures
- Maintains competitive accuracy at substantially smaller embeddings → significant energy reduction

## Significance

1. **First SNN multivariate TSF with graph modeling** — fills gap in inter-variable dependency modeling
2. **Bridges SNN and graph neural networks** for time series
3. **Energy efficiency**: Demonstrates SNN advantage in forecasting (not just classification)
4. **Benchmark protocol**: First unified evaluation framework for SNN TSF methods

## Applications

1. **Multivariate forecasting**: Weather, finance, sensor networks
2. **Edge AI**: Low-power time series prediction on neuromorphic hardware
3. **IoT**: Energy-efficient temporal modeling for distributed sensors
4. **Neuromorphic computing**: Showcases SNN advantages beyond image classification

## Code

- GitHub: https://github.com/jafarbakhshaliyev/SpikF-GO

## References

- Paper: https://arxiv.org/abs/2606.13901
- Venue: ECML PKDD 2026
