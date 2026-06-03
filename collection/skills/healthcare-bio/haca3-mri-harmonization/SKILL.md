---
name: haca3-mri-harmonization
version: 1.0.0
description: "HACA3+ MRI harmonization algorithm validated across 100+ scanners with traveling subjects. Incorporates improved artifact encoder, comprehensive multi-site validation, and real-world protocol robustness testing. Most comprehensive multi-site MRI harmonization validation to date. arXiv:2604.19474."
date: 2026-04-23
arxiv_id: "2604.19474"
authors: "Savannah P. Hays, Lianrui Zuo, Muhammad Faizyab Ali Chaudhary, Kathleen M. Bartz et al."
categories: "eess.IV"
activation:
  - MRI harmonization
  - multi-site neuroimaging
  - scanner harmonization
  - artifact removal
  - HACA3
  - traveling subject validation
  - clinical trial imaging
  - ComBat MRI
---

# HACA3+: Harmonizing MR Images Across 100+ Scanners

## Overview
Presents **HACA3+**, an enhanced MRI harmonization algorithm validated with traveling subjects across 100+ scanners. Addresses the critical challenge of combining heterogeneous MR data from multi-center clinical trials by removing scanner-specific artifacts while preserving biological signal.

## Key Methodology

### HACA3+ Enhancements over HACA3
1. **Improved Artifact Encoder**: Better isolation and mitigation of scanner-specific image artifacts
2. **Traveling Subject Validation**: Ground-truth validation using same subjects scanned across 100+ sites
3. **Real-World Protocol Robustness**: Tested on pragmatic clinical trial acquisition protocols (not just research-grade data)

### Algorithm Pipeline
1. **Image preprocessing**: Standardize resolution, orientation, intensity range
2. **Artifact encoding**: Extract scanner-specific artifact features using improved encoder
3. **Harmonization transform**: Apply site-adaptive normalization while preserving biological variation
4. **Quality control**: Automated checks for residual scanner effects

### Validation Framework
- **Traveling subjects**: Same individuals scanned at multiple sites provide ground truth
- **Quantitative metrics**: Intra-class correlation (ICC), coefficient of variation (CV)
- **Downstream tasks**: Validate harmonization preserves diagnostic utility
- **Scanner diversity**: 100+ unique scanners across manufacturers (Siemens, GE, Philips)

## Implementation Guidance
- Input: T1-weighted or T2-FLAIR MR volumes
- Preprocessing: N4 bias field correction, skull stripping, registration to template
- Model: Encoder-decoder architecture with artifact disentanglement
- Output: Harmonized volumes with reduced inter-scanner variance

## Advantages
- Largest multi-site MRI harmonization validation (100+ scanners)
- Works with pragmatic clinical trial data (not just research acquisitions)
- Preserves biological variation while removing scanner effects
- Improved artifact handling over predecessor methods

## Pitfalls
- Requires sufficient per-site samples for reliable harmonization
- May not fully handle extreme protocol deviations
- Computational cost scales with number of sites
- Validation limited to specific MRI contrasts (T1w, T2-FLAIR)

## References
- arXiv: [2604.19474](https://arxiv.org/abs/2604.19474)
- Key terms: MRI harmonization, multi-site imaging, traveling subjects, artifact removal, clinical trials, neuroimaging
