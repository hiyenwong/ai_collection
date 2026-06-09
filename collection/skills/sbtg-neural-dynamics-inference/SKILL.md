---
name: sbtg-neural-dynamics-inference
description: "Score-Block Time Graphs (SBTG) methodology for inferring lag-specific directed neural circuit interactions from population activity data using denoising score models. Activates: neural circuit inference, diffusion score, SBTG, directed connectivity, calcium imaging circuit mapping, lag-specific interaction, Jacobian recovery, brain state transition, C. elegans neural circuit."
---

# Score-Block Time Graphs (SBTG) for Neural Circuit Inference

> Infers lag-specific directed interactions in sampled neuronal population data by estimating joint-window scores over consecutive brain states and converting them into calibrated directed edge tests via cross-block score products.

## Metadata
- **Source**: arXiv:2605.02852
- **Authors**: Savik Kinger, Johannes Bertram, Luciano Dyballa, Eviatar Yemini, Steven W. Zucker
- **Published**: 2026-05-04
- **Category**: q-bio.NC

## Core Methodology

### Key Innovation
Uses denoising score matching to recover the **Jacobian of the transition map** between brain states under nonlinear dynamics, enabling discovery of lag-specific directed circuit structure without assuming parametric dynamics.

### Technical Framework

1. **Joint-Window Score Estimation**: Estimate scores over consecutive activity snapshots (brain states)
2. **Cross-Block Score Products**: Convert scores into calibrated, directed edge tests
3. **Multi-Block Windows**: Condition on intermediate time points to separate lag-specific effects, avoiding omitted-lag bias from pairwise analyses
4. **Jacobian Recovery**: Score products recover the Jacobian of the transition map between brain states

### Mathematical Insight
The cross-block score product between consecutive brain state windows directly estimates the Jacobian of the underlying dynamical system's transition function, revealing directed causal structure.

## Implementation Guide

### Prerequisites
- Neural population time-series data (e.g., calcium imaging, multi-electrode recordings)
- Score-based generative model framework
- Sufficient sampling rate to resolve desired time lags

### Step-by-Step

1. **Data Preparation**: Collect neural population activity time-series under varying stimuli
2. **Window Construction**: Create minimal multi-block windows conditioning on intermediate time points
3. **Score Estimation**: Train denoising score models on joint windows of consecutive brain states
4. **Cross-Block Products**: Compute cross-block score products to obtain directed edge estimates
5. **Statistical Testing**: Apply calibrated threshold tests to identify significant directed interactions
6. **Circuit Validation**: Compare inferred circuits against independent connectomes or known receptor kinetics

### Validation Applications
- Alignment with structural connectomes
- Cell-type-specific temporal organization detection
- Neuromodulatory profile consistency with known receptor kinetics

## Applications
- Whole-brain calcium imaging circuit mapping (e.g., C. elegans)
- Multi-electrode array neural circuit inference
- fMRI/EEG directed functional connectivity
- Translating population recordings into testable circuit hypotheses

## Pitfalls
- Requires sufficient data density across behavioral contexts
- Score estimation quality depends on sampling rate relative to neural dynamics
- Pairwise analyses suffer from omitted-lag bias — must use multi-block conditioning
- Validated primarily on C. elegans; generalization to mammalian data requires empirical validation

## Related Skills
- neural-dynamics-universal-translator
- connectome-constrained-neural-network
- time-varying-brain-connectivity
- sparse-neural-connectivity-recovery
- gp-cake-brain-connectivity
