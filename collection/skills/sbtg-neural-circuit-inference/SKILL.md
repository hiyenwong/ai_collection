---
name: sbtg-neural-circuit-inference
version: v1.0.0
last_updated: 2026-05-05
description: "Score-Block Time Graphs (SBTG) methodology for inferring lag-specific directed neural circuit interactions from population activity data. Uses denoising score models and cross-block score products to recover the Jacobian of transition maps under nonlinear dynamics. Based on arXiv:2605.02852 (Kinger et al., 2026)."
category: ai_collection
---

# Score-Block Time Graphs (SBTG) — Neural Circuit Inference

## Description
SBTG is a method for inferring directed, lag-specific neural circuit interactions from sampled neural population activity under varying stimuli, without assuming a parametric form for the underlying dynamics. It leverages denoising score models to estimate joint-window scores over consecutive brain state snapshots and converts these into calibrated, directed edge tests via cross-block score products.

**Paper:** Kinger, S., Bertram, J., Dyballa, L. et al. "Inferring Active Neural Circuits Using Diffusion Scores." arXiv:2605.02852 (2026).

## Activation Keywords
- sbtg
- score-block time graphs
- neural circuit inference
- diffusion score neural
- directed connectivity neural
- lag-specific interactions
- 神经回路推断
- 扩散分数
- brain state transition

## Core Methodology

### Key Insight
Cross-block score products recover the **Jacobian of the transition map** between brain states under nonlinear dynamics:
- Score products → directed edge weights
- Jacobian → lag-specific interaction strengths
- Multi-block windows → conditioning on intermediate time points to avoid omitted-lag bias

### Workflow

#### Step 1: Data Preparation
- Input: Time series of neural population activity (e.g., calcium imaging, electrophysiology)
- Format: N neurons × T time points matrix
- Preprocess: Normalize, detrend, optionally smooth

#### Step 2: Train Denoising Score Model
- Train a denoising diffusion model on the neural state space
- The score model learns: s(x) = ∇_x log p(x)
- Use noise-conditioned score matching (NCSM) or denoising score matching (DSM)

#### Step 3: Estimate Joint-Window Scores
- Define time windows of consecutive activity snapshots
- Estimate scores over joint windows: s(x_t, x_{t+1}, ..., x_{t+k})
- This captures multi-time-point dependencies

#### Step 4: Cross-Block Score Products
- Compute cross-block score products between time windows
- Product = E[s(x_{t→t+1}) · s(x_{t+1→t+2})^T]
- This recovers the Jacobian J = ∂x_{t+1}/∂x_t

#### Step 5: Multi-Block Window Conditioning
- Use minimal multi-block windows to separate lag-specific effects
- Condition on intermediate time points to avoid pairwise analysis bias
- This isolates direct vs. indirect interactions

#### Step 6: Directed Edge Tests
- Convert Jacobian estimates to calibrated, directed edge tests
- Apply statistical significance testing
- Build directed connectivity graph

#### Step 7: Validation
- Compare with known connectomes (e.g., electron microscopy)
- Check cell-type-specific temporal organization
- Verify neuromodulatory profiles against known receptor kinetics

## Implementation Notes

### Score Model Architecture
- Use a neural network (MLP or transformer) for the score model
- Input: noisy neural state vector
- Output: score vector (gradient of log density)
- Train with denoising score matching objective

### Cross-Block Product Computation
```python
# Pseudocode for cross-block score product
def cross_block_score_product(score_model, states, lag=1):
    """Compute cross-block score product for lag-specific interactions."""
    scores_t = score_model(states[:-lag])
    scores_tplus = score_model(states[lag:])
    # Cross-product recovers Jacobian
    jacobian_estimate = np.mean(scores_t[:, None] * scores_tplus[None, :], axis=0)
    return jacobian_estimate
```

### Advantages Over Existing Methods
1. **Non-parametric**: No assumption about functional form of dynamics
2. **Lag-specific**: Separates direct from indirect interactions
3. **Calibrated**: Statistical tests for edge significance
4. **Validated**: Successfully applied to C. elegans whole-brain calcium imaging

### Applications
- Whole-brain circuit mapping (C. elegans, zebrafish, mouse)
- Cell-type-specific temporal organization analysis
- Neuromodulatory pathway identification
- Dynamic functional connectivity estimation
- AI for science: turning population recordings into testable hypotheses

## Resources
- **Paper:** https://arxiv.org/abs/2605.02852
- **PDF:** https://arxiv.org/pdf/2605.02852
- **Related:** denoising score matching, neural ODEs, dynamic causal modeling

## Related Skills
- odebrain-continuous-eeg-graph (continuous-time neural dynamics)
- hermes-brain-connectivity (brain connectivity analysis toolkit)
- neural-dynamics-universal-translator (neural dynamics alignment)
- time-varying-brain-connectivity (dynamic brain networks)
