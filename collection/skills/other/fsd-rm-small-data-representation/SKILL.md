---
name: fsd-rm-small-data-representation
description: "FSD-RM for small-data representation learning with NAS."
---

# Beyond Foundation Models: Dimension-Aware Neural Architecture Search

## Overview
FSD-RM (Family of Small-Data Representation Models) is a practical alternative to large-scale pretrained time-series models for industrial and scientific domains that lack abundant, diverse data. Instead of relying on large-scale pretraining, it focuses on capacity-controlled representation learning using established encoder architectures (CNN1D, LSTM, GRU, Transformer) selected for small-data settings and interpretability.

## Key Components
- **Established Encoders**: Uses proven architectures (CNN1D, LSTM, GRU, Transformer) suitable for small-data regimes
- **Unsupervised Pretraining**: Trains encoders unsupervised on multivariate telemetry data
- **Two-Stage Pipeline**: Integrates representation learning with downstream prediction tasks
- **Dimension-Aware NAS**: Employs neural architecture search to jointly optimize model capacity and input dimensionality

## Implementation Steps
1. **Select Encoder Architecture**: Choose from CNN1D, LSTM, GRU, or Transformer based on domain requirements
2. **Unsupervised Representation Learning**: Train encoder on multivariate telemetry data without labels
3. **Apply Dimension-Aware NAS**: Use NAS to optimize both model capacity and input dimensionality
4. **Integrate Downstream Task**: Connect the representation model to the specific prediction task (e.g., lifetime prediction)
5. **Evaluate Performance**: Assess predictive performance, training cost, and model complexity

## Advantages
- **Competitive Performance**: Achieves competitive predictive performance compared to large foundation models
- **Reduced Training Cost**: Significantly lower computational requirements than large-scale pretraining
- **Model Simplicity**: Reduced model complexity through appropriate inductive bias and capacity control
- **Domain-Specific**: Tailored specifically for limited, domain-specific telemetry data

## Design Principles
- **Capacity Control**: Explicitly control model capacity to prevent overfitting in small-data regimes
- **Inductive Bias**: Apply appropriate inductive bias through architecture selection
- **Interpretability**: Prioritize interpretable architectures for scientific and industrial applications
- **Systematic Evaluation**: Use NAS-driven framework to systematically examine architectural trade-offs

## Use Cases
- Cryocooler lifetime prediction
- Industrial telemetry analysis
- Scientific time-series modeling
- Small-data regime applications
- Domain-specific prediction tasks

## Activation Keywords
fsd-rm, small-data, representation learning, dimension-aware nas, telemetry, cryocooler, time-series

## References
- arXiv: [2608.06993v1](https://arxiv.org/abs/2608.06993v1)
- Original paper: "Beyond Foundation Models: Dimension-Aware Neural Architecture Search with Small-Data Representation Models for Cryocooler Lifetime Prediction"