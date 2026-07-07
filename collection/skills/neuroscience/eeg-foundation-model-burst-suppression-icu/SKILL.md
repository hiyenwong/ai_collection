---
trigger_words:
  - EEG foundation model
  - burst suppression
  - ICU monitoring
  - REVE-base
  - LUNA-large
  - LuMamba-Tiny
  - event-based detection
  - reduced montage
  - fine-tuning strategy
  - sedation monitoring
  - induced coma
  - patient-specific calibration
related_skills:
  - eeg-foundation-model-adapters
  - tta-eeg-foundation-models
  - eeg-foundation-sae-interpretability
  - eeg-criticality-deep-sleep-classification-neurofeedback
papers:
  - arxiv:2606.20074
---

# EEG Foundation Models for Event-Based Burst-Suppression Detection in ICU

## Summary

First comprehensive evaluation of EEG Foundation Models (FMs) for burst suppression detection in reduced-montage ICU EEG without patient-specific calibration. **REVE-base achieves highest event-based F1-score (0.868)**, reducing burst-per-minute error by 52.1% and 36.2% compared to EEGNet and adaptive thresholding respectively. Demonstrates FMs enable scalable EEG monitoring in clinical settings.

## Clinical Significance

### Burst Suppression Context
- **Definition**: EEG pattern for monitoring sedation depth in induced coma
- **Clinical Use**: ICU patient monitoring, anesthesia depth
- **Challenge**: High inter-patient variability, scarce annotated data
- **Importance**: Direct impact on patient outcomes

### Practical Impact
- **No Patient Calibration**: Works across different patients
- **Reduced Montage**: Fewer electrodes, easier deployment
- **Scalable Monitoring**: Foundation model approach enables deployment
- **Real-time Detection**: Event-based evaluation matches clinical needs

## Foundation Models Evaluated

### Model Comparison
| Model | Event F1-Score | BPM Error Reduction |
|-------|---------------|---------------------|
| **REVE-base** | **0.868 ± 0.167** | **52.1% vs EEGNet** |
| LUNA-large | Competitive | 36.2% vs adaptive |
| LuMamba-Tiny | Good | Significant |
| EEGNet baseline | Lower | Reference |
| Adaptive thresholding | Lowest | Reference |

### Best Model: REVE-base
- Highest F1-score: 0.868
- Robust across patients
- Effective with limited data
- Best fine-tuning strategy

## Evaluation Methodology

### Event-Based vs Window-Based
1. **Window-Based**: Traditional classification accuracy
2. **Event-Based**: Clinically relevant metric
   - Correct burst episode detection
   - Matches clinical decision needs
   - Reduces annotation variability impact

### Metrics
- **Event F1-Score**: Burst episode detection accuracy
- **Burst-Per-Minute Error**: Clinical monitoring accuracy
- **Cross-Subject Generalization**: No patient calibration

## Fine-Tuning Strategies

### Adaptation Methods Evaluated
1. **Full Fine-Tuning**: **BEST** (+0.102 F1 vs frozen)
2. **Frozen Backbone**: Limited adaptation
3. **Two-Step Fine-Tuning**: Intermediate performance
4. **LoRA-based**: Parameter-efficient but lower accuracy

### Key Finding
Full fine-tuning most effective for burst detection with EEG FMs, contrary to common parameter-efficient assumptions.

## Limited Data Performance

### Data Efficiency
- **25% of cohort**: REVE-base achieves **+0.723 F1** vs random init
- **Strong pretraining benefit**: Foundation models crucial for scarce data
- **Label efficiency**: High performance with limited annotations

### Practical Implications
- Small labeled datasets sufficient
- Pretrained representations transfer effectively
- Clinical deployment feasible with minimal data

## Technical Framework

### Model Architecture
```python
# EEG Foundation Model evaluation pipeline

# Models evaluated
models = {
    'REVE-base': REVEBaseModel(),
    'LUNA-large': LUNALargeModel(),
    'LuMamba-Tiny': LuMambaTinyModel()
}

# Baselines
baselines = {
    'EEGNet': EEGNetBaseline(),
    'adaptive_threshold': AdaptiveThresholding()
}

# Event-based evaluation
def evaluate_burst_events(predictions, annotations):
    """
    Clinical-focused evaluation:
    - Burst episode detection (not just window accuracy)
    - Tolerance for annotation variability
    """
    burst_episodes = extract_events(predictions)
    true_episodes = extract_events(annotations)
    
    precision = match_episodes(burst_episodes, true_episodes)
    recall = match_episodes(true_episodes, burst_episodes)
    f1 = 2 * precision * recall / (precision + recall)
    
    return f1

# Fine-tuning strategies
def fine_tune_strategy(model, data, strategy='full'):
    """
    strategy: 'full', 'frozen', 'two_step', 'lora'
    """
    if strategy == 'full':
        # Full model fine-tuning - BEST results
        train_all_parameters(model, data)
    elif strategy == 'frozen':
        # Freeze backbone, train head only
        freeze_backbone(model)
        train_head_only(model, data)
    # ... other strategies
```

## Clinical Deployment Guidance

### Reduced Montage Setup
- Fewer electrodes than traditional ICU EEG
- Foundation models handle limited channels
- Easier clinical implementation
- Faster setup time

### No Calibration Requirement
- Works without patient-specific tuning
- Immediate deployment after fine-tuning
- Cross-patient generalization
- Reduces clinical workflow complexity

### Real-Time Monitoring
- Event-based detection matches clinical timing
- Burst-per-minute tracking
- Sedation depth estimation
- Alert generation

## Research Contributions

1. **First FM evaluation for burst suppression**: Novel application domain
2. **Event-based metrics**: Clinically relevant evaluation
3. **Fine-tuning comparison**: Full fine-tuning superiority
4. **Data efficiency**: Foundation models with limited labels

## Future Directions

### Model Improvements
1. **Domain adaptation**: ICU-specific pretraining
2. **Multi-task learning**: Burst + other EEG patterns
3. **Real-time inference**: Optimization for deployment
4. **Continuous learning**: Online adaptation

### Clinical Integration
1. **Alert systems**: Automated notifications
2. **Sedation protocols**: Closed-loop control
3. **Multi-center validation**: Broader deployment
4. **Outcome tracking**: Long-term monitoring

## Related Skills

- **eeg-foundation-model-adapters**: Domain adaptation methods
- **tta-eeg-foundation-models**: Test-time adaptation
- **eeg-foundation-sae-interpretability**: FM interpretability
- **eeg-criticality-deep-sleep-classification**: Criticality-based EEG

## References

- arXiv:2606.20074 - Original ICU burst suppression FM paper
- REVE, LUNA, LuMamba papers - EEG foundation models
- EEGNet papers - Baseline architecture
- Burst suppression literature - Clinical background