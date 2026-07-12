---
name: interpretable-ml-parkinsons-qsm-fmri
description: "Interpretable machine learning methodology for predicting Parkinson's disease motor severity (MDS-UPDRS Part III) from neuroimaging features — Quantitative Susceptibility Mapping (QSM) MRI and multiband multiecho resting-state fMRI Regional Homogeneity (ReHo). Uses SVR, Elastic Net, Random Forest, XGBoost with nested CV and SHAP interpretability. Full multimodal model explains 45.4% variance. QSH+c clinical model achieves 75% within ±5 UPDRS points. Activation: Parkinson's prediction, QSM MRI, ReHo fMRI, MDS-UPDRS, motor severity prediction, SHAP neuroimaging, multiband multiecho fMRI, interpretable ML Parkinson, quantitative susceptibility mapping"
metadata:
  arxiv_id: "2607.02553"
  published: "2026-06-26"
  authors: "Aixa X. Andrade"
  tags: [Parkinsons-disease, QSM, fMRI, ReHo, MDS-UPDRS, interpretable-ML, SHAP, biomarker]
---

# Interpretable ML for Parkinson's Disease Severity Prediction

## Overview

Predicts Parkinson's motor severity (MDS-UPDRS Part III) from QSM MRI and multiband multiecho fMRI-derived ReHo features using interpretable ML (SHAP).

## Dataset

- 28 participants (24 PD, 4 controls)
- Features: regional QSM (structural, iron deposition) + ReHo (functional, local connectivity)

## Experimental Design

13 feature-set experiments:
1. **Imaging-only** (QSM features)
2. **Imaging-only** (fMRI ReHo features)
3. **Clinical-only**
4. **Full fMRI**
5. **Full QSM**
6. **Full fMRI + Full QSM + Clinical** — best global fit (R² = 0.454)
7. **Selected QSM + Clinical** — best clinical proximity (75% within ±5 UPDRS points, lowest MAE)
8. **Reduced, multimodal** variants

## Models

- Support Vector Regression (SVR)
- Elastic Net
- Random Forest
- XGBoost
- Nested cross-validation for all models

## Key Results

| Model | R² | Clinical Accuracy | Notes |
|-------|-----|-------------------|-------|
| Full fMRI + Full QSM + Clinical | 0.454 | — | Best global fit |
| Selected QSM + Clinical | — | 75% within ±5 | Best clinical proximity, lowest MAE |
| Imaging-only (QSM) | meaningful | — | Carries predictive signal |
| Imaging-only (fMRI ReHo) | meaningful | — | Carries predictive signal |
| Clinical-only | weak | — | Baseline |

## SHAP Feature Importance

Top features: cerebellar, thalamic, striatal, insular, and motor cortical regions.

## Key Insight

Structural (QSM) and functional (ReHo) imaging contribute differently depending on the clinical prediction goal:
- **Global fit** → combine all modalities
- **Clinical precision** → selected QSM + clinical variables

## Methodology Steps

1. Extract regional QSM features (iron deposition, structural)
2. Extract ReHo from multiband multiecho resting-state fMRI (local functional connectivity)
3. Design 13 feature-set experiments (imaging-only, clinical-only, multimodal, reduced)
4. Train 4 model types with nested CV
5. Evaluate: R², RMSE, MAE, Pearson r, permutation testing, within ±5 UPDRS accuracy
6. SHAP for interpretability

## Pitfalls

- **Small sample size**: 28 participants limits generalizability — always report permutation tests
- **Control imbalance**: 24 PD vs 4 controls — may affect model calibration
- **Nested CV essential**: With small N, standard CV overestimates performance
- **SHAP for interpretability**: Essential for clinical adoption — black-box predictions insufficient

## References

- Andrade, A.X. (2026). "Interpretable machine learning predicts Parkinson's disease severity using motion-corrected QSM MRI and multiband multiecho fMRI features" — arXiv:2607.02553
