---
name: hgf-robust-volatility-updates
description: "Robust volatility updates for Hierarchical Gaussian Filtering (HGF). Improves stability and convergence of uncertainty estimation in perceptual inference. Activation: hierarchical gaussian filter, volatility update, perceptual inference, active inference, uncertainty estimation."
---

# Robust Volatility Updates for Hierarchical Gaussian Filtering

> Improved HGF volatility update rules for stable uncertainty estimation in hierarchical perceptual inference.

## Metadata
- **Source**: arXiv:2605.04235
- **Authors**: Christoph Mathys, Nicolas Legrand, Peter Thestrup Waade, Nace Mikus, Lilian Aline Weber
- **Published**: 2026-05-07
- **Categories**: cs.LG, cs.NE, q-bio.NC, stat.ML

## Core Methodology

### HGF Volatility Robustness
- Standard HGF can exhibit instability in volatility estimation
- New update rules ensure bounded, well-behaved volatility estimates
- Maintains theoretical guarantees while improving numerical stability
- Compatible with existing HGF implementations (TAPAS, hgf R package)

### Technical Framework
1. Hierarchical Gaussian Filter: beliefs at multiple timescales
2. Volatility level: estimates environmental change rate
3. Robust updates: bounded influence functions prevent runaway estimates
4. Convergence: proved stability under mild conditions

## Applications
- Computational psychiatry (belief updating in patient populations)
- Decision-making under uncertainty
- Adaptive learning rate control
- fMRI/EEG model-based fMRI analysis

## Related Skills
- free-energy-moe-routing
- online-generalised-predictive-coding
- neural-dynamics-decision-making
