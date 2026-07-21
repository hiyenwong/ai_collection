---
name: eeg-foundation-lrp-interpretability
description: "Layer-wise Relevance Propagation (LRP) methodology for interpreting EEG foundation models. Extends LRP from CNN-based to Transformer-based EEG models, enabling verification and hypothesis discovery. Activation: EEG interpretability, LRP, EEG foundation model, transformer attribution, Clever Hans EEG, post-hoc attribution."
---

# EEG Foundation Model Interpretability via LRP

Methodology for applying Layer-wise Relevance Propagation (LRP) to EEG foundation models for post-hoc attribution, based on Meyer zu Bexten et al. (2026), arXiv:2605.11885.

## Core Concept

EEG foundation models (FMs) promise scalable deep learning for diagnostics and brain-computer interfaces despite data scarcity, but their opaque Transformer architectures remain a barrier. This methodology extends LRP — a well-established post-hoc attribution method for CNNs — to Transformer-based EEG models.

## Key Contributions

1. **LRP for EEG Transformers**: First systematic application of attention-aware LRP to Transformer-based EEG FMs
2. **Verification**: LRP can verify that FM decisions align with expected neurophysiological patterns
3. **Discovery**: LRP surfaces novel, biologically plausible hypotheses from FM behavior

## Application to LaBraM

### Motor Imagery (PhysioMI)
- **Finding**: "Clever Hans" behavior — model prioritizes task-correlated ocular signals (EOG artifacts) over intended motor cortex correlates
- **Implication**: FMs may learn spurious correlations that work in-distribution but fail to capture intended neural mechanisms
- **LRP heatmap pattern**: Attribution concentrated on frontal channels (eye movement artifacts) rather than sensorimotor regions

### Affective Prediction (Naturalistic Paradigm)
- **Finding**: Recurring reliance on central electrode cluster for arousal prediction
- **Hypothesis**: Central electrodes may capture a sensorimotor signature of arousal state
- **Valence prediction**: Less consistent attribution patterns, suggesting valence is harder to decode from EEG alone

### R-Peak Detection (Verification Task)
- **Purpose**: Well-understood physiological signal used to verify LRP correctness
- **Result**: ~75% balanced accuracy, attribution patterns consistent with expected ECG morphology
- **Significance**: Validates that LRP produces meaningful attributions before applying to less-understood tasks

## Implementation

```python
# LRP for Transformer-based EEG models
def apply_lrp_to_eeg_transformer(model, eeg_input, lrp_rule="epsilon"):
    """Apply Layer-wise Relevance Propagation to EEG Transformer.
    
    Args:
        model: Trained EEG foundation model (Transformer-based)
        eeg_input: EEG tensor [batch, channels, time]
        lrp_rule: Propagation rule (epsilon, gamma, z-plus)
    
    Returns:
        relevance_map: Attribution per electrode and time point
    """
    # Forward pass with relevance tracking
    model.eval()
    output = model(eeg_input)
    
    # Initialize relevance at output layer
    relevance = output  # target class relevance = 1, others = 0
    
    # Backward propagation through Transformer layers
    for layer in reversed(model.transformer_layers):
        # Attention-aware LRP
        relevance = lrp_attention_layer(layer, relevance, rule=lrp_rule)
        relevance = lrp_feedforward_layer(layer, relevance, rule=lrp_rule)
    
    # Map back to input electrode-time space
    relevance_map = lrp_input_projection(relevance)
    
    return relevance_map
```

## LRP Rules for EEG Transformers

| Rule | Description | Best For |
|------|-------------|----------|
| ε-rule | Stabilizes division with small epsilon | General purpose, default choice |
| γ-rule | Emphasizes positive contributions | Excitatory pattern detection |
| z-plus | Propagates only positive relevance | Binary classification |

## Pitfalls

1. **Heatmap ambiguity**: In complex domains like EEG, heatmaps are suggestive but not definitive. Always cross-validate with domain knowledge.
2. **Clever Hans detection is crucial**: FMs may exploit artifacts (EOG, EMG) rather than neural signals. LRP helps identify this but requires careful interpretation.
3. **Transformer-specific LRP**: Standard LRP rules designed for CNNs need adaptation for attention mechanisms. Use attention-aware propagation.
4. **Performance vs attribution tradeoff**: Finetuned vs from-scratch training shows minimal performance difference, but attribution patterns may differ significantly.
5. **Baseline comparison**: Always compare FM attribution patterns with established methods (e.g., CSP-LDA) to validate biological plausibility.

## Verification Strategy

1. **Known signal validation**: Apply LRP to tasks with well-understood neurophysiology (R-Peak detection, P300)
2. **Artifact detection**: Use LRP to identify if model relies on non-neural signals (EOG, ECG, muscle artifacts)
3. **Cross-paradigm comparison**: Compare attribution patterns across different experimental paradigms
4. **Expert validation**: Have neuroscientists/clinicians review LRP heatmaps for biological plausibility

## Related Skills

- eeg-foundation-model-adapters: EEG foundation model domain adaptation
- eeg-preprocessing-reliability: EEG decoding reliability and preprocessing assessment
- neural-encoding-evaluation-ground-truth: Ground-truth approximation for neural encoding evaluation
