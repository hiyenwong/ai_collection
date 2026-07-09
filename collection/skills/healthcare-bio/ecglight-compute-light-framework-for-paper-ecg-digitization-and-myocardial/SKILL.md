---
name: ecglight-compute-light-framework-for-paper-ecg-digitization-and-myocardial
description: 'Electrocardiography (ECG) is one of the most widely used tests for diagnosing cardiovascular disease. Yet several remote clinics still utilize paper ECG printouts for their analysis due to limited con. Based on arXiv:2607.07683.'
---

# ECGLight: Compute-Light Framework For Paper ECG Digitization and Myocardial Infarction Screening

**arXiv**: 2607.07683 | **Authors**: Shreyasvi Natraj, Cyrus Achtari, Felice Gragnano, Andrea Milzi, Marco Valgimigli et al. | **Utility**: 0.85

## Overview

Electrocardiography (ECG) is one of the most widely used tests for diagnosing cardiovascular disease. Yet several remote clinics still utilize paper ECG printouts for their analysis due to limited connectivity and computational capacity. As a result, vast numbers of physical ECGs obtained in remote areas still remain incapable of being accessed by contemporary artificial-intelligence (AI)-based decision support as they require high computational resources or strong high-speed internet connectivity. This causes several cases where conditions like acute coronary occlusion (ACS) is overlooked and reperfusion therapy delayed. Although prior work has tackled digitization and diagnosis separately, and utilized advanced AI models for them, there still remains a lack of a compute-light, on-device framework that reconstructs paper ECGs at high fidelity, while accurately supporting multiple clinically relevant endpoints. We address this need with an end-to-end lightweight on-device digitization-to-diagnosis pipeline that converts a smartphone photo or scan of a paper ECG into a calibrated 12-lead signal and screens for Myocardial Infarction (MI) pathologies, with SHapley Additive exPlanations (SHAP) to support interpretability. Trained and evaluated on 21,799 ECGs from the PTB-XL dataset and further validated on hospital-acquired ECG-Matrix dataset, the complete system runs in <30 s per ECG on CPU-only resources, achieving 95.51% accuracy (F1 = 0.9519) for MI detection on PTB-XL and 88.89% accuracy (F1 = 0.8862) for OMI detection on ECG-Matrix. This work showcases that legacy paper records can be reliably democratized in any part of the world, providing a scalable decision support when digital ECG export, connectivity, or high-end compute are unavailable

## Key Contributions

1. Electrocardiography (ECG) is one of the most widely used tests for diagnosing cardiovascular disease.
2. Yet several remote clinics still utilize paper ECG printouts for their analysis due to limited connectivity and computational capacity.
3. As a result, vast numbers of physical ECGs obtained in remote areas still remain incapable of being accessed by contemporary artificial-intelligence (AI)-based decision support as they require high computational resources or strong high-speed internet connectivity.
4. This causes several cases where conditions like acute coronary occlusion (ACS) is overlooked and reperfusion therapy delayed.

## Implementation Notes

- **Keywords**: graph-neural-network
- **Categories**: cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: graph-neural-network.
