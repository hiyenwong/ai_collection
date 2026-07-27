---
name: universal-bci-personalization-api
title: Universal BCI Personalization API for Frozen EEG Trunks
version: 1.0.0
description: Trunk-agnostic API for BCI personalization that works with heterogeneous frozen EEG encoders and foundation models without per-architecture personalization stacks
tags:
  - bci
  - eeg
  - personalization
  - foundation-models
  - nimbus-personalizer
arxiv_id: 2607.22397
date: 2026-07-24
authors:
  - Sergey Musienko
---

# Universal BCI Personalization: One API for Frozen EEG Trunks and Foundation Models

## Overview
Nimbus Personalizer provides a trunk-agnostic API that enables BCI personalization across heterogeneous frozen EEG encoders without requiring a new personalization stack per architecture. This systems-level contribution allows OEMs to integrate once and swap trunks seamlessly.

## Key Contributions
- **Trunk-Agnostic API**: Single contract encode to Bayesian head to BrainState architecture
- **Broad Compatibility**: Works with five classical trunks (EEGNet, Shallow, Deep, Conformer, ATCNet) and foundation encoders (REVE)
- **Cost Efficiency**: Orders of magnitude less adaptation wall time while recovering much of fine-tune accuracy gain
- **Scalable Integration**: OEMs integrate once and can swap trunks without new personalization stacks

## Problem Addressed
The proliferation of frozen EEG encoders creates a scaling problem where per-model fine-tuning defaults don't scale across different architectures and datasets.

## Technical Approach
The Nimbus Personalizer uses a three-tier architecture:
1. **Contract Encode**: Standardized input encoding
2. **Bayesian Head**: Adaptive classification layer  
3. **BrainState**: Optional affine mid-tier for additional capacity

## Experimental Results
- Tested on 4 MI datasets across 18 cells
- Calibration-only-when-clean holds in 12/18 cells
- Subject-level confidence intervals identify clearest dataset performance
- All results are exploratory (subject-level bootstrap, no confirmatory tests)

## Use Cases
- BCI system integration for OEMs
- Cross-architecture model deployment
- Foundation model personalization
- Resource-constrained adaptation scenarios

## Activation Keywords
- BCI personalization
- frozen EEG encoders
- trunk-agnostic API
- foundation model adaptation
- nimbus personalizer

## References
- arXiv:2607.22397
- Companion paper on control layer forthcoming