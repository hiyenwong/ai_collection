---
name: eeg-foundation-temporal-correlations-blindness
description: "EEG foundation models lose long-range temporal correlations: framework for analyzing spectral-temporal dissociation and cross-population fragility in EEG foundation models. Provides methodology for testing LRTC recovery via DFA exponent and evaluating cross-cohort transfer performance."
metadata:
  arxiv_id: "2607.24834"
  authors: "Marzieh Zare"
  published: "2026-07-23"
  tags: [eeg-foundation-models, temporal-correlations, lrtc, dfa-exponent, cross-population-transfer, neuromorphic-computing]
license: Complete terms in LICENSE.txt
---

# EEG Foundation Models Lose Long-Range Temporal Correlations: A Spectral-Temporal Dissociation Behind Their Cross-Population Fragility

## Overview

This skill implements the methodology from arXiv:2607.24834 for analyzing how EEG foundation models (FMs) fail to preserve long-range temporal correlations (LRTC) quantified by the detrended fluctuation analysis (DFA) exponent. The framework reveals a critical spectral-temporal dissociation where FMs recover static 1/f aperiodic slopes but lose dynamic LRTC, leading to cross-population fragility.

## Key Findings

### Temporal Representation Failure
- **None of five tested EEG FMs** represented LRTC in temporal order
- **Raw-waveform models** (REVE, LaBraM, BENDR): Recover neither DFA exponent nor 1/f slope (R² ≤ 0.12)
- **Spectral-input models** (CBraMod, BIOT): Recover 1/f strongly (R² = 0.59-0.73) but not DFA across cohorts
- **Classical DFA feature**: Recovers exponent (R² = 0.32-0.38 against 0.64 reliability ceiling)

### Cross-Population Transfer Issues
- **Frozen REVE embedding**: Does not beat chance (W to K, 0.45)
- **DFA exponent**: Transfers directionally but not at family-wise significance
- **Recording-site axis dominance**: All FMs dominated by site axis (decodable at 0.98-1.00 vs 0.500 chance)
- **Site robustness**: DFA exponent is site-robust (0.71) while FMs discard it

### Orthogonality Discovery
- **LRTC orthogonal to aperiodic slope**: r = -0.06
- **Spectral-temporal dissociation**: FMs capture spectral but not temporal dynamics

## Methodology

### Experimental Setup
- **Five EEG FMs tested**: REVE, LaBraM, BENDR, CBraMod, BIOT
- **Two out-of-distribution cohorts**: Cross-population evaluation
- **Probes**: DFA exponent vs 1/f aperiodic slope recovery
- **Controls**: Order-preserving and residualization for pooling/aperiodic shadowing
- **Zero-shot transfer task**: Montage-harmonized across three cohorts (Western reference added)

### Analysis Framework
1. **Temporal correlation measurement**: Compute DFA exponent of alpha-band envelope
2. **Spectral analysis**: Measure 1/f aperiodic slope
3. **FM embedding probing**: Linear probe on frozen FM embeddings
4. **Cross-cohort transfer**: Zero-shot evaluation with montage harmonization
5. **Site robustness testing**: Decodability analysis of recording sites

### Validation Metrics
- **DFA recovery R²**: Against ground truth DFA exponent
- **Transfer accuracy**: Classification performance across cohorts  
- **Site decodability**: How well recording sites can be decoded from embeddings
- **Reliability ceiling**: Intra-subject reliability as upper bound

## Practical Applications

### EEG FM Evaluation Protocol
1. **Test LRTC preservation**: Always include DFA exponent analysis alongside standard metrics
2. **Evaluate cross-population robustness**: Test on out-of-distribution cohorts
3. **Check site bias**: Measure recording-site decodability as confound indicator
4. **Compare spectral vs temporal**: Analyze both 1/f slope and DFA exponent recovery

### Model Selection Guidelines
- **Avoid raw-waveform FMs** for temporal dynamics tasks
- **Consider classical features** when LRTC is critical
- **Use spectral-input models cautiously**: They may have hidden temporal blind spots
- **Prioritize site-robust models**: Lower site decodability indicates better generalization

### Research Design Recommendations
1. **Include LRTC metrics** in EEG FM benchmarking suites
2. **Report both spectral and temporal** performance separately
3. **Test cross-cohort transfer** as standard evaluation
4. **Document site bias** and mitigation strategies

## Pitfalls and Limitations

### Common Evaluation Gaps
- **Over-reliance on standard metrics**: Accuracy, loss don't capture temporal dynamics
- **Ignoring cross-population effects**: In-distribution performance ≠ real-world utility  
- **Missing site bias analysis**: Site information can dominate embeddings
- **Spectral-only focus**: Missing critical temporal dynamics

### Implementation Challenges
- **DFA computation complexity**: Requires careful parameter selection
- **Montage harmonization**: Critical for cross-cohort comparison
- **Reliability ceiling estimation**: Need multiple sessions per subject
- **Statistical power**: Family-wise significance requires careful correction

## Activation Keywords
- EEG foundation models
- long-range temporal correlations
- DFA exponent
- spectral-temporal dissociation
- cross-population fragility
- site robustness EEG
- temporal dynamics EEG

## References
- Original paper: https://arxiv.org/abs/2607.24834
- Related work:
  - "EEG Foundation Model Audit Systematic Evaluation" (eeg-fm-audit-systematic-evaluation)
  - "EEG Foundation Models for Stress Testing Clinical Decoding" (eeg-fm-stress-testing-clinical-decoding)
  - "Variance Brain Foundation Models Forgot" (variance-brain-foundation-models-forgot)

## Verification Steps

To validate this framework:
1. **Reproduce DFA analysis**: Compute DFA exponent on your EEG dataset
2. **Probe FM embeddings**: Train linear probes for both DFA and 1/f slope
3. **Test cross-cohort transfer**: Evaluate on out-of-distribution data
4. **Measure site bias**: Decode recording sites from embeddings
5. **Compare against classical features**: Benchmark FM performance vs traditional DFA features
6. **Assess reliability ceiling**: Estimate intra-subject reliability limits