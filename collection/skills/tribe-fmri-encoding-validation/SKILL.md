---
name: tribe-fmri-encoding-validation
description: "Validation framework for brain-encoding models like TRIBE — testing whether predicted fMRI signals correlate with behavioral engagement metrics. Use when evaluating brain-encoding models, testing fMRI predictions against behavioral data, or validating neural prediction models."
---

## TRIBE fMRI Encoding Model Validation

### Context
The TRIBE model (Llama-3.2 + V-JEPA2 + Wav2Vec-BERT) won the 2025 Algonauts brain-encoding challenge but its predicted cortical responses do not correlate with behavioral engagement (YouTube replay heatmaps). This reveals a critical gap between neural prediction accuracy and behavioral relevance.

### Key Findings (arXiv:2607.01400)
- **Null correlation**: Global field power from TRIBE predictions shows no evidence of predicting re-watch behavior (r=+0.058, p=0.23)
- **Baseline comparison**: Simple loudness and motion baselines perform equivalently
- **Genre artifacts**: Moderate correlations in music videos reflect intro/onset-replay artifacts, not content prediction
- **Robust null**: Results hold across six cortical-network readouts and autocorrelation-preserving permutation tests

### Validation Protocol
1. Run brain-encoding model on naturalistic stimuli
2. Reduce predicted cortical response to engagement curves (global field power)
3. Correlate against behavioral engagement proxies
4. Compare against simple baselines (loudness, motion)
5. Test across multiple cortical-network readouts
6. Run autocorrelation-preserving permutation tests

### Pitfalls
- **Behavioral disconnect**: High fMRI prediction accuracy ≠ behavioral relevance
- **Genre confounds**: Apparent correlations may reflect artifacts rather than genuine prediction
- **Baseline necessity**: Always compare against simple baselines before claiming model superiority

### Activation: brain-encoding validation, TRIBE model, fMRI prediction, behavioral engagement, Algonauts challenge
