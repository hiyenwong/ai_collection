---
name: highfidelity-networkbased-alzheimers-progression
description: "High-fidelity spatio-temporal PDE mathematical models of Alzheimer's disease progression on brain networks. Combines network-based diffusion dynamics with PET-SUVR biomarker data to model and predict amyloid/tau propagation across brain connectome. (arXiv:2604.18470, April 2026)"
tags: [Alzheimer's disease, brain network, PDE model, spatio-temporal dynamics, PET-SUVR, amyloid propagation, tau spreading, connectome, neurodegeneration]
---

# High-Fidelity Network-Based Spatio-Temporal Models of Alzheimer's Progression

**arXiv:** 2604.18470 (April 20, 2026)
**Categories:** math.NA, q-bio.NC

## Summary

High-fidelity mathematical framework for modeling Alzheimer's disease progression using spatio-temporal PDE models on brain networks. Integrates PET-SUVR (Standard Uptake Value Ratio) biomarker data with connectome-based diffusion dynamics to simulate and predict the spatial-temporal propagation of amyloid-beta and tau pathology across the brain.

## Key Methodology

### Network-Based PDE Framework
1. **Brain Connectome Substrate:** Uses structural connectivity (DTI-derived) as the network substrate for pathology propagation
2. **Reaction-Diffusion PDE:** Models protein misfolding as a reaction-diffusion process on graph-structured domains
3. **Spatio-Temporal Dynamics:** Captures both local production (reaction terms) and network-mediated spreading (diffusion terms)
4. **PET-SUVR Integration:** Calibrates model parameters against longitudinal PET imaging biomarkers

### Mathematical Formulation
1. **Graph Laplacian Diffusion:** Network diffusion operator based on structural connectivity weights
2. **Kinetics Terms:** Prion-like propagation kinetics for amyloid and tau species
3. **Source Terms:** Region-specific production rates derived from empirical data
4. **Boundary Conditions:** Reflective boundary conditions on network nodes

### Parameter Estimation
1. **PET-SUVR Fitting:** Model parameters optimized against observed PET-SUVR trajectories
2. **Cross-Validation:** Leave-one-out and k-fold validation across subjects
3. **Individual vs Group Models:** Both population-average and subject-specific parameter fitting
4. **Longitudinal Calibration:** Multi-timepoint data for temporal validation

### Key Findings
- Network-based PDE models capture spatial-temporal Alzheimer's pathology patterns
- Connectome structure constrains and shapes disease propagation pathways
- PET-SUVR data provides sufficient calibration signal for parameter estimation
- Model predicts future biomarker trajectories from baseline measurements

## Practical Applications

### When to Use This Approach
- Modeling proteinopathy spreading in neurodegenerative diseases
- Predicting individual patient disease trajectories from baseline scans
- Evaluating therapeutic intervention timing and targeting
- Understanding connectome-mediated disease propagation mechanisms

### Implementation Steps
1. Construct structural connectivity matrix from DTI data
2. Extract PET-SUVR time series from ROI parcellation
3. Set up reaction-diffusion PDE on graph domain
4. Define kinetic parameters and source terms
5. Calibrate model using longitudinal PET data
6. Validate predictions against held-out timepoints
7. Generate individual-level progression forecasts

## Limitations & Considerations

- **Connectome Quality:** DTI tractography limitations affect diffusion modeling
- **Temporal Resolution:** PET scans typically annual — limits temporal precision
- **Model Complexity:** Balance between fidelity and identifiability
- **Subject Variability:** Inter-subject heterogeneity in propagation patterns
- **Computational Cost:** High-fidelity numerical solutions require efficient solvers

## Related Skills
- `brain-network-controllability` — Brain network control theory
- `alzheimer-pet-suvr-network-models` — Alzheimer PET-SUVR modeling
- `neural-dynamics-deep-snn` — Neural dynamics modeling
