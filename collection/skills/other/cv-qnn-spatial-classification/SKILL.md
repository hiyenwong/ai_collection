---
name: cv-qnn-spatial-classification
description: Continuous-variable QNN advantage for spatial classification tasks. Controlled comparison showing CV-QNN outperforms DV-QNN by 18+ percentage points on wafer-map defect classification. CV structured layer captures fine spatial distinctions that DV misses. Use when designing QNNs for image/spatial classification, semiconductor yield, or any task requiring fine spatial pattern recognition.
version: 1.0.0
tags: [quantum, CV-QNN, DV-QNN, spatial-classification, image, defect-detection]
source: arXiv:2607.00961
authors: [Yeonhong Kim, Jonghyeok Im, Monu Nath Baitha, Kyoungsik Kim]
published: 2026-07-01
trigger_words: [CV QNN vs DV QNN, continuous variable quantum neural network, quantum spatial classification, wafer map defect, quantum image classification, QNN representational capacity]
---

# CV-QNN Advantage for Spatial Classification

## Core Insight

CV-QNNs consistently outperform DV-QNNs on spatial classification tasks by 18+ percentage points. The CV advantage comes from two intrinsic properties: structured neural-network-analogue layer and continuous phase-space encoding, NOT Hilbert-space dimensionality.

## Key Findings

### 1. Performance Gap
- At 4 qumodes/qubits: CV = 79.7% vs DV = 61.6% (non-overlapping 18-point gap)
- Gap is sharpest on spatially localized classes (Edge-Loc: CV recall 0.66, DV recall < 0.05)
- DV limitation is representational-capacity ceiling, not optimization failure

### 2. Why CV Wins
- Structured CV layer better captures fine spatial distinctions
- Continuous phase-space encoding preserves spatial information
- CV acts as neural-network-analogue layer (unlike DV)

### 3. Hardware Validation
- DV accuracy holds at shallow depth on IBM hardware
- DV degrades only at deepest circuit
- CV advantage expected to grow as noise improves

## Implementation Pattern

1. Use shared convolutional backbone for feature extraction
2. Replace classical dense head with CV-QNN head
3. Scale CV head over multiple qumode counts (3, 4, 8)
4. Compare against DV-QNN head with same qubit count
5. Validate on hardware at shallow depth

## Practical Applications

### Financial Spatial Data
- Geographic risk mapping
- Regional market pattern classification
- Spatial-temporal financial data analysis

### General Spatial Classification
- Image defect detection
- Medical image classification
- Any task requiring fine spatial pattern distinction

## Activation

Use when:
- Designing QNNs for spatial/image classification
- Choosing between CV and DV quantum paradigms
- Needing fine spatial pattern recognition
- Building hybrid classical-quantum classifiers