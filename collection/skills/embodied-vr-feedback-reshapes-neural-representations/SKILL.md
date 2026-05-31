---
name: embodied-vr-feedback-reshapes-neural-representations
description: Embodied Virtual Reality feedback reshapes neural representations to support continuous three-dimensional motor imagery decoding. First systematic investigation showing VR feedback elicits more decodable and generalisable neural representations for BCI applications.
created: 2026-05-31
updated: 2026-05-31
source: arXiv:2605.29677
authors: Niall McShane, Attila Korik, Karl McCreadie, Naomi Du Bois, Darryl Charles, Damien Coyle
tags: [neuroscience, BCI, VR, motor-imagery, neural-representations, EEG, deep-learning, CNN-LSTM]
activation_keywords: [VR feedback, embodied feedback, motor imagery BCI, 3D decoding, neural representation, sensorimotor-parietal, functional connectivity]
---

# Embodied Virtual Reality Feedback Reshapes Neural Representations

## Overview
This study presents the first systematic investigation of embodied virtual reality (VR) feedback during real-time 3D virtual limb control driven by motor imagery across ten longitudinal sessions. Key finding: embodied VR feedback elicits inherently more decodable and generalisable neural representations compared to traditional screen feedback.

## Core Methodology

### Experimental Design
- **Participants**: 10 participants, 10 longitudinal sessions each
- **Task**: Continuous 3D motor imagery (virtual limb control)
- **Feedback Modalities**: VR vs. Screen feedback comparison
- **Decoding Strategies**:
  1. Fixed Decoder Generalisation (FDG) - actual online performance
  2. Sequential Adaptive Training (SAT) - periodic retraining
  3. Within-Session Reconstruction (WSR) - upper-bound estimation

### CNN-LSTM Decoder Architecture
- Achieved within-session imagined movement correlations:
  - **VR feedback**: r = 0.762
  - **Screen feedback**: r = 0.672
- VR significantly outperformed screen across all strategies (8.9-13.0% improvement, p <= 0.002, d = 1.42-2.05)

## Key Findings

### 1. Neural Representation Quality
- VR feedback produces inherently more decodable neural patterns
- Advantage persists even without decoder retraining
- Demonstrates that embodied feedback shapes neural representations at the source

### 2. Neurophysiological Mechanisms
- **Stronger sensorimotor-parietal desynchronisation** under VR
- **Enhanced motor-frontal functional connectivity**
- **Pervasive anterior insula engagement** across all frequency bands
- **Increased superior parietal lobule coupling**
- Patterns parallel those seen in real movement execution

### 3. Movement Dimension Effects
- Linear mixed-effects modelling confirmed:
  - Robust main effects of feedback modality
  - Movement axis effects
  - No interaction (independent effects)

## Practical Applications

### BCI Design Principles
1. **Embodied spatial feedback** as key design principle
2. Target intuitive motor control applications
3. Neurorehabilitation optimization
4. Real-time adaptive decoding strategies

### Implementation Guidelines
```python
# CNN-LSTM decoder for 3D motor imagery
class MotorImageryDecoder:
    def __init__(self):
        self.cnn_encoder = ConvNet()  # Feature extraction
        self.lstm_decoder = LSTMNet()  # Temporal trajectory decoding
        
    def decode_trajectory(self, eeg_signal):
        features = self.cnn_encoder.extract(eeg_signal)
        trajectory = self.lstm_decoder.predict(features)
        return trajectory  # 3D coordinates
```

## Technical Insights

### VR Feedback Advantages
- Spatial embodiment creates stronger motor imagery
- Immersive feedback loop enhances neural encoding
- Multi-dimensional movement representation
- Better generalisation to unseen data

### Neural Mechanisms
- Anterior insula: Interoceptive awareness during embodied movement
- Superior parietal: Spatial processing and body schema
- Motor cortex: Movement planning and execution
- Sensorimotor integration network activation

## Research Questions Addressed
1. How does feedback modality shape neural representations?
2. Can embodied VR produce inherently better decodable signals?
3. What neurophysiological mechanisms underlie VR advantage?
4. How does longitudinal training affect decoding performance?

## Limitations
- Small sample size (n=10)
- Laboratory VR setup (not home-use ready)
- Requires specialised EEG equipment
- Motor imagery training intensity varies across participants

## Future Directions
- Home-based VR BCI systems
- Multi-modal feedback (VR + haptic)
- Transfer learning across participants
- Real-time adaptive decoder optimisation
- Integration with neurorehabilitation protocols

## Related Work
- Continuous BCI trajectory decoding
- Motor imagery neural representations
- Embodied cognition in BCI
- VR neurofeedback systems
- Functional connectivity in motor imagery

## References
- arXiv:2605.29677 - Full paper
- Zenodo DOI: 10.5281/zenodo.16047021 - Data availability
- Nature Biomedical Engineering (submitted)

## Activation
Use when:
- Designing motor imagery BCI systems
- Optimising feedback modalities for neurorehabilitation
- Studying neural representation quality
- Implementing 3D trajectory decoding
- Comparing VR vs. screen feedback efficacy
- Investigating embodied cognition effects on neural encoding