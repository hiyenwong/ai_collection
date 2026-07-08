---
name: omnimouse-brain-model-scaling
description: "OmniMouse methodology for multi-modal, multi-task brain models at scale. Uses 150B neural tokens dataset to study scaling properties of brain activity modeling, revealing that brain models are data-limited unlike language/vision models. Activation: OmniMouse, brain model scaling, neural tokens, multi-modal brain, mouse visual cortex, data-limited scaling."
---

# OmniMouse: Brain Model Scaling Properties

> Multi-modal, multi-task brain models trained on 150B neural tokens reveal unique scaling properties where brain modeling remains data-limited despite vast datasets.

## Metadata
- **Source**: arXiv:2604.18827
- **Authors**: Konstantin F. Willeke, Polina Turishcheva, Alex Gilbert, et al.
- **Published**: 2026-04-20 (ICLR 2026)
- **Categories**: Neurons and Cognition (q-bio.NC); Artificial Intelligence (cs.AI)

## Core Methodology

### Dataset
**Massive Scale Mouse Neural Recordings:**
- 3.1 million neurons from visual cortex
- 73 mice across 323 sessions
- 150+ billion neural tokens
- Multiple modalities: natural movies, images, parametric stimuli, behavior

### Model Architecture
**OmniMouse** supports three flexible test-time regimes:
1. **Neural Prediction**: Predict neural responses to stimuli
2. **Behavioral Decoding**: Decode behavior from neural activity
3. **Neural Forecasting**: Predict future neural states

Any combination of the three can be used at test time.

### Key Innovation
Multi-task learning across prediction, decoding, and forecasting with modality-agnostic architecture.

## Key Findings

### Scaling Properties
**Inverts Standard AI Scaling Story:**
- **Language/Vision**: Massive datasets → parameter scaling drives progress
- **Brain Modeling**: Models remain **data-limited** despite 150B tokens

### Model Size vs Data
- Performance scales reliably with more data
- Gains from increasing model size **saturate**
- Even mouse visual cortex (relatively simple) requires more data

### Phase Transition Hypothesis
Systematic scaling raises possibility of emergent capabilities with larger, richer datasets - paralleling large language model phase transitions.

## Implementation Guide

### Prerequisites
- Large-scale neural recording data
- Multi-modal stimuli (visual, behavioral)
- Computational resources for 150B+ token training

### Model Design Principles
```python
# Conceptual architecture
class OmniMouse(nn.Module):
    """Multi-modal, multi-task brain model"""
    def __init__(self):
        self.neural_encoder = NeuralEncoder()
        self.stimulus_encoder = StimulusEncoder()
        self.behavior_encoder = BehaviorEncoder()
        self.fusion_transformer = FusionTransformer()
        
    def forward(self, neural, stimulus, behavior, mode='all'):
        # Flexible test-time regimes
        outputs = {}
        if 'prediction' in mode:
            outputs['neural_pred'] = predict_neural(stimulus)
        if 'decoding' in mode:
            outputs['behavior_decoded'] = decode_behavior(neural)
        if 'forecasting' in mode:
            outputs['future_neural'] = forecast_neural(neural)
        return outputs
```

### Training Strategy
1. **Multi-task pretraining** on all available modalities
2. **Scale data** rather than model parameters for brain modeling
3. **Cross-subject generalization** evaluation

## Applications

### Neuroscience Research
- Large-scale neural population modeling
- Cross-subject neural response prediction
- Behavior-neural coupling analysis

### Brain-Computer Interfaces
- Neural decoding for BCIs
- Multi-modal neural signal processing
- Real-time neural prediction

### AI-Neuroscience Bridge
- Understanding what makes brain modeling unique
- Data collection strategy optimization
- Scaling law predictions for neural AI

## Pitfalls

### Common Misconceptions
- Assuming brain models follow language model scaling laws
- Under-investing in data collection vs. model capacity
- Treating brain regions as independent prediction targets

### Best Practices
- Prioritize data scaling over model scaling
- Design for multi-task, multi-modal objectives
- Account for biological variability across subjects

## Related Skills
- spikingbrain2.0-foundation-models
- brain-dit-fmri-foundation-model
- eeg-foundation-model-adapters

## Code Availability
Code available at: [GitHub repository referenced in paper]

## References
- Willeke et al. (2026). OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens. ICLR 2026. arXiv:2604.18827.
