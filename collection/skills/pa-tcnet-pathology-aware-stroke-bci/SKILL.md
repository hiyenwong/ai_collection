---
name: pa-tcnet-pathology-aware-stroke-bci
description: "PA-TCNet: Pathology-Aware Temporal Calibration for cross-subject motor imagery EEG decoding in stroke patients. Clinical BCI with physiological guidance and pathology-aware adaptation. Keywords: stroke, BCI, motor imagery, clinical, cross-subject, pathology-aware."
---

# PA-TCNet: Pathology-Aware Temporal Calibration for Stroke Patient BCI

> A clinical brain-computer interface framework for motor imagery EEG decoding in stroke patients, addressing lesion-related temporal dynamics and inter-patient heterogeneity through pathology-aware calibration.

## Metadata
- **Source**: arXiv:2604.16554
- **Authors**: Xiangkai Wang, Yun Zhao, Dongyi He, et al.
- **Published**: 2026-04-17
- **Category**: Neural and Evolutionary Computing (cs.NE), Human-Computer Interaction (cs.HC)

## Core Methodology

### Clinical Challenge

Stroke patient motor imagery (MI) BCI presents unique challenges:

1. **Lesion-related abnormal dynamics**: Brain damage alters neural signal timing
2. **Pathological slow-wave activity**: Delta/theta activity from damaged tissue
3. **Inter-patient heterogeneity**: Lesion locations and sizes vary widely
4. **Standard adaptation fails**: Generic methods misled by pathology

### PA-TCNet Framework

PA-TCNet introduces three key components:

#### 1. Pathology-Aware Temporal Calibration

Instead of assuming uniform temporal dynamics, PA-TCNet:
- Identifies patient-specific optimal time windows
- Calibrates for lesion-induced temporal shifts
- Filters out pathological slow-wave artifacts

**Temporal Calibration Process:**
```
Raw EEG → Band Filtering → Pathology Detection → 
Temporal Window Optimization → Feature Extraction
```

#### 2. Physiology-Guided Target Refinement

Uses physiological priors to improve pseudo-label quality:

```
Standard Pseudo-Labels: Argmax(model(unlabeled_data))
PA-TCNet Refinement: 
  - Apply motor cortex physiology constraints
  - Discard implausible activations
  - Smooth across similar motor tasks
```

#### 3. Cross-Subject Transfer with Pathology Awareness

Transfer learning accounts for lesion location:

```
Source Patients: [Healthy-like, Frontal lesion, Parietal lesion, ...]
Target Patient: Classify pathology type → Select matching sources
Adaptation: Weighted combination of similar pathology sources
```

### Key Innovations

#### Lesion-Aware Feature Extraction

Different brain lesions produce characteristic EEG signatures:

| Lesion Location | Expected Pattern | Adaptation Strategy |
|----------------|------------------|---------------------|
| Motor cortex | Severely attenuated MI signals | Boost alternative motor areas |
| Thalamus | Disrupted timing, increased latency | Expand temporal search window |
| Subcortical | Preserved cortical activity | Standard calibration |
| Diffuse | Global slow-wave increase | Aggressive high-pass filtering |

#### Physiological Constraint Network

Incorporates neuroscientific knowledge as soft constraints:

```python
class PhysiologicalConstraint(nn.Module):
    """Ensures predictions align with motor physiology"""
    
    def forward(self, predictions, eeg_features):
        # Motor cortex should activate during hand MI
        motor_cortex_activity = eeg_features[:, MOTOR_CHANNELS]
        
        # Constraint: Hand MI → Lateralized motor cortex activation
        constraint_loss = torch.relu(
            -predictions['hand'] * 
            (motor_cortex_activity[LEFT] - motor_cortex_activity[RIGHT])
        )
        
        return constraint_loss
```

## Implementation Guide

### Prerequisites
- Clinical EEG system (32-64 channels)
- Stroke patient population
- Lesion imaging (MRI/CT)
- Motor imagery paradigm

### Step-by-Step

1. **Patient Stratification**
   ```python
   def classify_pathology_type(lesion_mask, clinical_scores):
       """Classify stroke patient by lesion characteristics"""
       
       if lesion_mask[MOTOR_CORTEX].sum() > threshold:
           return "MOTOR_CORTEX"
       elif lesion_mask[THALAMUS].sum() > threshold:
           return "THALAMIC"
       elif lesion_mask.sum() > diffuse_threshold:
           return "DIFFUSE"
       else:
           return "FOCAL_OTHER"
   ```

2. **Temporal Calibration**
   ```python
   class TemporalCalibrator:
       def calibrate(self, eeg_data, subject_id):
           # Detect pathological slow waves
           slow_power = band_power(eeg_data, band=(0.5, 4))
           
           # Optimize window based on pathology
           if self.pathology_type == "THALAMIC":
               # Delayed responses need later windows
               optimal_window = (500, 2500)  # ms
           elif self.pathology_type == "MOTOR_CORTEX":
               # Alternative areas activate earlier
               optimal_window = (200, 1500)
           else:
               optimal_window = (250, 1750)  # Default
           
           return optimal_window
   ```

3. **PA-TCNet Model**
   ```python
   import torch.nn as nn
   
   class PATCNet(nn.Module):
       def __init__(self, n_channels, n_classes, n_pathology_types):
           super().__init__()
           
           # Pathology-specific temporal convolution
           self.temporal_calibrators = nn.ModuleList([
               TemporalConv(pathology_type=i) 
               for i in range(n_pathology_types)
           ])
           
           # Shared feature extractor
           self.feature_extractor = nn.Sequential(
               nn.Conv2d(1, 32, kernel_size=(n_channels, 1)),
               nn.BatchNorm2d(32),
               nn.ReLU(),
               nn.Conv2d(32, 64, kernel_size=(1, 25)),
               nn.AdaptiveAvgPool2d((1, 1))
           )
           
           # Classifier with physiology guidance
           self.classifier = nn.Linear(64, n_classes)
           self.physio_constraint = PhysiologicalConstraint()
       
       def forward(self, x, pathology_type):
           # Apply pathology-specific calibration
           x = self.temporal_calibrators[pathology_type](x)
           
           # Feature extraction
           features = self.feature_extractor(x)
           features = features.view(features.size(0), -1)
           
           # Classification
           logits = self.classifier(features)
           
           return logits, features
   ```

4. **Training with Pseudo-Label Refinement**
   ```python
   def train_step(model, labeled_data, unlabeled_data, optimizer):
       # Standard supervised loss
       sup_loss = F.cross_entropy(model(labeled_data), labels)
       
       # Generate pseudo-labels with physiological refinement
       pseudo_logits = model(unlabeled_data)
       pseudo_probs = F.softmax(pseudo_logits, dim=1)
       
       # Refine using physiological constraints
       refined_probs = apply_physiological_constraints(pseudo_probs)
       pseudo_labels = refined_probs.argmax(dim=1)
       
       # Consistency loss
       cons_loss = F.cross_entropy(pseudo_logits, pseudo_labels)
       
       # Total loss
       loss = sup_loss + 0.5 * cons_loss
       
       loss.backward()
       optimizer.step()
   ```

### Clinical Validation Protocol

1. **Inclusion criteria**: Chronic stroke (>6 months), unilateral motor deficit
2. **Assessment**: Fugl-Meyer, modified Rankin Scale
3. **Lesion mapping**: Standardized lesion-symptom mapping
4. **BCI training**: 10-15 sessions, 40 trials per class
5. **Outcome metrics**: Classification accuracy, clinical improvement

## Applications

- **Motor rehabilitation**: Post-stroke hand/arm recovery
- **Assistive devices**: Wheelchair/control interface for paralyzed patients
- **Neurofeedback**: Real-time motor cortex engagement training
- **Clinical trials**: BCI-based therapy efficacy assessment

## Pitfalls

1. **Small sample sizes**: Rare disease, difficult to collect large datasets
2. **Severe impairment**: Some patients lack sufficient residual motor imagery
3. **Fatigue effects**: Stroke patients tire quickly during BCI sessions
4. **Medication effects**: CNS-active drugs alter EEG signals
5. **Ethical considerations**: Vulnerable population requires extra protections

## Related Skills
- motor-imagery-bci
- clinical-neurotechnology
- stroke-rehabilitation
- transfer-learning-bci

## Citation
```bibtex
@article{wang2026patcnet,
  title={PA-TCNet: Pathology-Aware Temporal Calibration with Physiology-Guided Target Refinement for Cross-Subject Motor Imagery EEG Decoding in Stroke Patients},
  author={Wang, Xiangkai and Zhao, Yun and He, Dongyi and others},
  journal={arXiv preprint arXiv:2604.16554},
  year={2026}
}
```
