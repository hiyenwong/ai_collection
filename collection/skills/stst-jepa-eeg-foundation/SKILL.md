---
name: stst-jepa-eeg-foundation
description: "STST-JEPA EEG foundation model methodology using Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture for self-supervised learning. Pretrained on 47,703 sessions (ages 5-81) achieving 3.06 years MAE for brain age prediction and rank-1 on NeuralBench leaderboard. Activation: EEG foundation model, self-supervised learning, brain age prediction, JEPA, spatio-temporal embedding, NeuralBench, cross-site montage"
metadata:
  arxiv_id: "2607.06629"
  published: "2026-07-07"
  authors: "Roy Segal, Yoni Svechinsky, Tomer Fekete"
  tags: [EEG foundation model, self-supervised learning, brain age prediction, JEPA, transformer, NeuralBench]
---

# STST-JEPA: EEG Foundation Model via Spatio-Temporal Joint Embedding Prediction

## Core Concept

STST-JEPA (Shallow-Target Spatio-Temporal Joint Embedding Prediction Architecture) is a self-supervised transformer for EEG that learns universal representations across resting-state and task EEG. The model combines latent-prediction with signal reconstruction to achieve state-of-the-art performance on brain age prediction and multiple EEG benchmarks.

## Key Innovations

### 1. Joint Embedding Prediction Architecture (JEPA) for EEG
- **Latent prediction objective**: Predict masked-token representations against EMA-of-tokenizer target
- **Auxiliary signal reconstruction**: Reconstruct raw EEG signals from embeddings
- **Spatiotemporal block masks**: Apply masks across both time and channel dimensions

### 2. Large-Scale Pretraining
- **Dataset**: 47,703 EEG sessions spanning ages 5-81
- **Sources**: brain.space and Healthy Brain Network (HBN) corpora
- **Coverage**: Pediatric to older adult lifespan
- **Window**: 30-second multi-channel windows

### 3. Cross-Site Montage Heterogeneity
- Handles varying electrode montages across sites
- Robust to subject-level non-stationarity
- Works with small labeled cohorts

## Performance

### Brain Age Prediction
- **MAE**: 3.06 years (held-out validation on 3,367 sessions)
- **Correlation**: r = 0.924
- **Baseline**: ~10 years MAE (predict-the-mean)
- **Clinical relevance**: Age prediction residual negatively correlated with cognitive efficiency

### NeuralBench Leaderboard (Rank-1 Placements)
- **Sex classification**: Balanced accuracy 0.911
- **Age prediction**: r = 0.749
- **Psychopathology composite regression**: r = 0.215
- **Native 30-second windows**: No task-specific preprocessing required

## Methodology

### Pretraining Pipeline
1. **Input**: 30-second multi-channel EEG windows
2. **Masking**: Apply spatiotemporal block masks (time + channel dimensions)
3. **Encoding**: Transformer encoder processes masked windows
4. **Prediction targets**:
   - Primary: EMA-of-tokenizer representations (latent prediction)
   - Auxiliary: Raw signal reconstruction
5. **Training**: Joint optimization of prediction and reconstruction losses

### Fine-tuning Strategy
- **Frozen embeddings**: Lightweight attentive probe for zero-shot evaluation
- **Light fine-tuning**: Task-specific adaptation of final layers
- **Minimal data**: Effective with small labeled cohorts

### Architecture Details
- **Transformer-based**: Self-attention over spatiotemporal tokens
- **Shallow target**: Predict against early-layer representations (not deep features)
- **EMA tokenizer**: Exponential moving average of tokenizer for stable targets

## Applications

### Clinical Neuroscience
- **Brain age biomarker**: Track neurological and psychiatric burden
- **Cognitive efficiency**: Age prediction residual correlates with cognitive performance
- **Psychopathology screening**: Composite regression for mental health assessment

### Research Applications
- **Cross-site studies**: Handle montage heterogeneity across labs
- **Lifespan studies**: Pediatric to geriatric age ranges
- **Task-agnostic features**: Generalizable across resting-state and task EEG

### Brain-Computer Interfaces
- **Universal embeddings**: Pretrained features for diverse BCI tasks
- **Few-shot adaptation**: Effective with limited labeled data
- **Real-time processing**: 30-second window inference

## Implementation Considerations

### Data Requirements
- **Pretraining**: Large-scale EEG dataset (47k+ sessions recommended)
- **Fine-tuning**: Small labeled cohort sufficient (3k+ sessions)
- **Montage flexibility**: Handle varying electrode configurations

### Training Strategy
- **Spatiotemporal masking**: Balance time vs. channel mask ratios
- **EMA decay**: Tune exponential moving average rate for tokenizer
- **Auxiliary loss weight**: Balance prediction vs. reconstruction objectives

### Pitfalls
- **Subject-level confounds**: Age prediction may capture subject identity rather than neural age
- **Montage mismatch**: Performance degrades with extreme electrode configuration differences
- **Overfitting**: Large models require careful regularization on small fine-tuning sets

## Validation Metrics

### Brain Age Prediction
- Mean Absolute Error (MAE) in years
- Pearson correlation (r) with chronological age
- Age bias analysis (systematic over/under-prediction)

### Downstream Tasks
- Balanced accuracy (classification)
- Pearson correlation (regression)
- Leaderboard ranking (NeuralBench)

### Clinical Relevance
- Correlation with cognitive efficiency scores
- Sensitivity to neurological/psychiatric conditions
- Test-retest reliability

## Related Work

- Brain age prediction via deep learning
- Self-supervised learning for EEG
- Joint Embedding Predictive Architecture (JEPA)
- Foundation models for neuroscience

## References

- Paper: arXiv:2607.06629 (July 7, 2026)
- NeuralBench x brain.space EEG leaderboard
- brain.space and Healthy Brain Network (HBN) corpora
