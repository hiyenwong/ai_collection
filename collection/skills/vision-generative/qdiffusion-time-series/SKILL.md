---
name: qdiffusion-time-series
description: "Quantum generative diffusion model for time series synthesis (QDiffusion-TS). First quantum diffusion model validated on real quantum hardware (IQM processor). Replaces feed-forward components with quantum neural networks, reducing parameters by ~3 orders of magnitude. Reduces Wasserstein distance by ~44% vs classical. Use when: quantum generative modeling, time series synthesis, quantum-enhanced data augmentation, parameter-efficient diffusion models."
---

## Core Methodology

### QDiffusion-TS Architecture
Extends classical diffusion architecture by replacing feed-forward components within the denoising transformer with **Quantum Neural Networks (QNNs)**, yielding a hybrid quantum transformer.

### Key Innovation: Parameter Reduction
- Reduces trainable parameters in each replaced component by **nearly 3 orders of magnitude**
- Maintains or exceeds classical performance with substantially fewer parameters

### Performance Metrics
- **Wasserstein distance**: ~44% reduction vs classical counterpart
- **Downstream forecasting**: up to 71% improvement in RMSE with synthetic data augmentation
- Validated on financial time series (Apple, Amazon) on IQM quantum processor

### Pipeline

```
Real Time Series → Diffusion Process (noisy) 
                → Denoising Transformer with QNN layers 
                → Synthetic Time Series 
                → Downstream Task (e.g., forecasting)
```

### Quantum-Classical Hybrid Design
- Quantum layers handle the core denoising transformation
- Classical layers handle preprocessing and postprocessing
- Joint training of quantum and classical components

### Data Augmentation Strategy
Generated synthetic data is used to augment real training data, improving downstream model performance significantly (up to 71% RMSE improvement).

## Implementation Notes

- Requires access to quantum hardware (IQM processor or similar)
- Hybrid architecture allows training with classical simulation, then deployment on quantum hardware
- Particularly effective for small datasets where quantum expressivity provides advantage

## Activation

quantum diffusion, quantum generative model, time series synthesis, QDiffusion, quantum data augmentation, hybrid quantum transformer, quantum ML time series
