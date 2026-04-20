---
name: eccentricity-confound-eeg-based-visual-attention-decoding
description: "EEG-based visual attention decoding methodology addressing the eccentricity confound. Demonstrates that retinal eccentricity (not just attention) drives decoding accuracy in gaze-fixated paradigms. Uses control experiments with matched visual stimuli to isolate attention effects. Activation: EEG, visual attention, gaze fixation, eccentricity, brain decoding"
---

# Eccentricity Confound in EEG-based Visual Attention Decoding

## Overview

A critical methodological finding in EEG-based visual attention decoding: when participants fixate on objects in different positions during naturalistic video viewing, the decoding of "which object is attended" is confounded by **retinal eccentricity** (distance from fixation point). This study proves that neural tracking still works under gaze fixation but reveals that coupling strength is significantly affected by eccentricity, not attention alone.

## Source Paper

- **Title**: Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos
- **Authors**: Yuanyuan Yao, Celina Salamanca Gonzalez, Simon Geirnaert, Celine R. Gillebert, Tinne Tuytelaars, Alexander Bertrand
- **arXiv**: 2604.15223v1
- **Published**: 2026-04-16
- **Categories**: N/A
- **PDF**: https://arxiv.org/pdf/2604.15223v1

## Core Concepts

### The Eccentricity Confound

In standard visual attention decoding experiments:
- Stimuli are placed at different positions in the visual field
- Participants fixate on one stimulus vs another
- EEG signals decode which stimulus is attended via neural tracking of motion

**The problem**: Different visual field positions have different retinal eccentricities (distance from fovea). Neural tracking of object motion is **weaker at larger eccentricities**, creating a confound where decoding may reflect **stimulus eccentricity** rather than **attentional allocation**.

### Key Findings

1. **Neural tracking works under gaze fixation**: Object motion can still be tracked from EEG even with controlled eye movements
2. **Attention prediction**: Tracking strength under gaze fixation is predictive of attention state
3. **Eccentricity effect**: Significantly poorer neural tracking at larger eccentricities — a major confound
4. **Free-viewing validation**: Previous free-viewing studies reflect genuine neural processing, not just oculomotor artifacts

### Match-Mismatch Decoding Framework

```python
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

def match_mismatch_decoding(eeg_data, stimulus_features, labels):
    """
    Match-mismatch decoder: train classifier to distinguish
    whether EEG matches stimulus A or stimulus B features.
    
    This is the standard paradigm for attention decoding from EEG.
    """
    # Build feature matrix: correlation between EEG and each stimulus
    features = np.zeros((len(eeg_data), 2))
    for i, eeg in enumerate(eeg_data):
        features[i, 0] = np.corrcoef(eeg, stimulus_features[0])[0, 1]
        features[i, 1] = np.corrcoef(eeg, stimulus_features[1])[0, 1]
    
    clf = SVC(kernel='linear')
    accuracy = np.mean(cross_val_score(clf, features, labels, cv=5))
    
    return accuracy


def quantify_eccentricity_confound(eeg_data, stimulus_configs, labels):
    """
    Compare decoding accuracy across eccentricity conditions.
    Returns the confound magnitude: how much eccentricity alone
    (without attention) affects decoding performance.
    """
    results = {}
    for config_name, (eeg, stimuli) in stimulus_configs.items():
        acc = match_mismatch_decoding(eeg, stimuli, labels)
        results[config_name] = acc
    
    # Confound = difference between high and low eccentricity conditions
    confound = results.get('low_ecc', 0) - results.get('high_ecc', 0)
    
    return {
        'accuracies': results,
        'eccentricity_confound': confound,
        'confound_percent': (confound / max(results.values())) * 100 if results else 0
    }
```

## Practical Applications

### BCI Design Implications

1. **Gaze-based attention BCI**: Account for eccentricity when interpreting decoding accuracy
2. **Stimulus placement**: Optimize visual field positions for reliable attention decoding
3. **Calibration**: Include eccentricity-matched conditions in BCI calibration protocols

### EEG Analysis Pipeline for Visual Attention

```python
def preprocess_eeg_visual_tracking(eeg_raw, gaze_data, stimulus_motion):
    """
    Preprocessing for neural tracking of visual motion.
    """
    # 1. Bandpass filter (1-40 Hz for neural tracking)
    eeg_filtered = bandpass_filter(eeg_raw, 1, 40)
    
    # 2. Remove eye movement artifacts (ICA or regression)
    eeg_clean = remove_ocular_artifacts(eeg_filtered, gaze_data)
    
    # 3. Extract object motion features from video
    motion_features = extract_motion_features(stimulus_motion)
    
    # 4. Compute temporal response functions (TRF)
    trf = compute_trf(eeg_clean, motion_features)
    
    # 5. Check eccentricity effects
    eccentricity_map = compute_eccentricity_map(gaze_data, stimulus_positions)
    
    return eeg_clean, motion_features, eccentricity_map
```

## Validation Checklist

- [ ] Control for eccentricity differences between stimuli
- [ ] Verify neural tracking works under gaze fixation
- [ ] Test whether decoding generalizes across eccentricity conditions
- [ ] Include eccentricity-matched control conditions
- [ ] Account for retinotopic organization in analysis

## Related Work

- Neural tracking of speech and motion in naturalistic stimuli
- Retinotopic organization of visual cortex
- Gaze-contingent display paradigms
- Oculomotor artifact removal in EEG

## Activation Keywords

- eccentricity confound
- EEG visual attention
- gaze fixation decoding
- neural tracking
- match-mismatch decoder
- visual attention BCI
- retinotopic EEG

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Eccentricity Confound Eeg Based Visual Attention Decoding usage
```
User: "Help me with eccentricity confound eeg based visual attention decoding"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed eccentricity confound eeg based visual attention decoding assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
