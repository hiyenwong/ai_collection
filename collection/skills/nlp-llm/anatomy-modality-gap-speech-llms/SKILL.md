---
name: anatomy-modality-gap-speech-llms
title: "Anatomy of the Modality Gap: Dissecting the Internal States of End-to-End Speech LLMs"
description: "Analysis of modality gap in speech LLMs through cross-layer alignment patterns, revealing that speech representations exhibit broad cross-layer alignment due to redundant nature of speech signals."
trigger_words:
  - modality gap
  - speech LLMs
  - cross-layer alignment
  - speech-text alignment
  - end-to-end speech models
---

# Anatomy of the Modality Gap: Dissecting the Internal States of End-to-End Speech LLMs

## Overview
This methodology investigates the dynamic roots of the modality gap in Large Speech-Language Models (SLLMs) beyond static geometric alignment, analyzing how speech and text representations evolve layer-by-layer through cross-layer CKA analysis.

## Key Findings

### 1. Cross-Layer Alignment Patterns
- **Observation**: Speech representations exhibit a broad cross-layer alignment band
- **Cause**: Redundant nature of speech where semantic content spans multiple frames
- **Stability**: Alignment patterns are structurally stable across different analysis configurations

### 2. Statistical Calibration Limitations
- **Finding**: Simple statistical calibration is insufficient and can be detrimental at input layer
- **Implication**: Modality gap is not merely a distribution shift problem
- **Evidence**: Performance degradation when applying naive calibration techniques

### 3. Bottleneck Identification
- **Location**: Late-layer decision making process
- **Nature**: Difficulty in condensing redundant speech into stable decisions
- **Solution Direction**: Token or temporal granularity approaches over feature-level matching

## Methodology

### Evaluation Framework
- **Models**: Four open-weight end-to-end SLLMs
- **Benchmarks**: SpeechMMLU and VoiceBench BBH
- **Analysis**: Cross-layer CKA with speech-text token alignment

### Technical Approach
- Layer-by-layer representation evolution tracking
- Dynamic alignment pattern analysis
- Structural stability verification across configurations

## Applications
- Speech LLM architecture design
- Modality gap reduction strategies
- Multi-modal representation learning
- Speech-text alignment optimization
- End-to-end speech processing systems

## Implementation Guidelines
When addressing modality gaps in speech LLMs:
1. Focus on token or temporal granularity solutions rather than feature-level matching
2. Analyze cross-layer alignment patterns to understand redundancy structure
3. Avoid simple statistical calibration at input layers
4. Design architectures that effectively condense speech redundancy into stable decisions
5. Use cross-layer CKA analysis for systematic evaluation

## References
- arXiv:2603.01502
- Published: March 2026
- Categories: Computation and Language (cs.CL), Audio and Speech Processing (eess.AS)