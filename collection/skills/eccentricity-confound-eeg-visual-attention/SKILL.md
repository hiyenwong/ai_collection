---
name: eccentricity-confound-eeg-visual-attention
description: "Eccentricity confound analysis for EEG-based visual attention decoding during natural video viewing. Methodological framework for separating true neural attention from stimulus and eye movement artifacts. Keywords: visual attention, EEG, eye movements, eccentricity, natural video, artifact removal."
---

# Eccentricity Confound in EEG-based Visual Attention Decoding

> A methodological framework for disentangling true neural attention signals from confounding factors (eye movements and stimulus eccentricity) during naturalistic video-based brain-computer interfaces.

## Metadata
- **Source**: arXiv:2604.15223
- **Authors**: Yuanyuan Yao, Celina Salamanca Gonzalez, Simon Geirnaert, et al.
- **Published**: 2026-04-16
- **Category**: Human-Computer Interaction (cs.HC), Neurons and Cognition (q-bio.NC)

## Core Methodology

### The Eccentricity Confound Problem

Naturalistic video-based BCI aims to decode what viewers attend to:

**Traditional Assumption**: Stronger coupling between object motion and neural activity = higher attention

**Reality**: This coupling is confounded by:
1. **Visual eccentricity**: Distance from fixation point affects neural response
2. **Eye movements**: Saccades and microsaccades create artifacts
3. **Stimulus properties**: Size, contrast, and motion vary with eccentricity

### Key Finding

Neural responses to identical stimuli differ dramatically based on eccentricity:
- **Foveal** (0-2°): High-resolution processing
- **Parafoveal** (2-5°): Reduced acuity
- **Peripheral** (>5°): Low spatial frequency dominance

Without accounting for eccentricity, BCI systems confound:
- "Attending to moving object" vs "Object happens to be in fovea"

### Framework Components

#### 1. Eye Tracking Integration

Precise gaze position enables eccentricity calculation:

```python
def compute_eccentricity(object_position, gaze_position):
    """Calculate visual angle between object and fixation"""
    dx = object_position.x - gaze_position.x
    dy = object_position.y - gaze_position.y
    distance_pixels = np.sqrt(dx**2 + dy**2)
    
    # Convert to visual angle (degrees)
    visual_angle = pixels_to_degrees(distance_pixels, screen_distance, screen_width)
    
    return visual_angle
```

#### 2. Eccentricity-Aware Feature Extraction

Separate neural responses by eccentricity bin:

```
EEG Features:
├── Foveal condition (0-2°): High frequency, detailed features
├── Parafoveal (2-5°): Mid-band features
└── Peripheral (>5°): Low frequency, coarse features
```

#### 3. Motion-Eccentricity Decoupling

Statistical separation of motion and eccentricity effects:

```
Original Model: EEG ~ β₁ × Motion + β₂ × Eccentricity + error
Decoupled Model: 
  - Residual = EEG - (β₂ × Eccentricity)  # Remove eccentricity effect
  - Attention = Correlation(Residual, Motion)  # Pure motion-attention coupling
```

### Experimental Design

#### Paradigm
- Natural video viewing with free eye movements
- Simultaneous EEG (64+ channels) and eye tracking
- Annotated object trajectories in video frames

#### Conditions
1. **Controlled**: Fixation + peripheral moving object
2. **Free viewing**: Natural exploration with attention manipulation
3. **Pursuit**: Following moving object with eyes

#### Analysis Pipeline
```
Raw Data:
├── EEG: 64 channels, 500 Hz
├── Eye tracking: 1000 Hz, binocular
└── Video: 30 fps with object annotations

Preprocessing:
├── EEG: Bandpass 0.5-45 Hz, ICA artifact removal
├── Eye tracking: Saccade detection, drift correction
└── Synchronization: Event alignment

Analysis:
├── Trial segmentation by eccentricity
├── Motion-energy regression per eccentricity bin
└── Cross-validation across subjects
```

## Implementation Guide

### Prerequisites
- EEG system (64+ channels recommended)
- High-speed eye tracker (1000 Hz)
- Natural video stimuli with object annotations
- Python/MATLAB analysis environment

### Step-by-Step

1. **Data Collection Setup**
   ```python
   # Synchronize EEG and eye tracking
   import pygaze
   import pylsl
   
   # Start LSL streams
   eeg_stream = pylsl.resolve_stream('type', 'EEG')[0]
   eye_stream = pylsl.resolve_stream('type', 'Gaze')[0]
   
   # Record with timestamps
   recorder = SynchronizedRecorder(eeg_stream, eye_stream, video_path)
   ```

2. **Preprocessing**
   ```python
   import mne
   
   # Load EEG
   raw = mne.io.read_raw_eeglab('subject_data.set')
   raw.filter(0.5, 45)
   
   # ICA artifact removal
   ica = mne.preprocessing.ICA(n_components=20)
   ica.fit(raw)
   raw_clean = ica.apply(raw, exclude=[0, 3])  # Remove eye blink components
   
   # Load eye tracking
   eye_data = pd.read_csv('gaze_data.csv')
   eye_data = detect_saccades(eye_data, velocity_threshold=30)  # deg/s
   ```

3. **Eccentricity Calculation**
   ```python
   def compute_trial_eccentricities(eeg_epochs, eye_data, object_positions):
       """Calculate eccentricity for each trial"""
       eccentricities = []
       
       for epoch_idx in range(len(eeg_epochs)):
           epoch_time = eeg_epochs[epoch_idx].times
           
           # Get gaze position during epoch
           gaze_x = interpolate_gaze(eye_data['x'], epoch_time)
           gaze_y = interpolate_gaze(eye_data['y'], epoch_time)
           
           # Get object position at corresponding time
           obj_x = object_positions[epoch_idx]['x']
           obj_y = object_positions[epoch_idx]['y']
           
           # Calculate eccentricity
           ecc = np.sqrt((gaze_x - obj_x)**2 + (gaze_y - obj_y)**2)
           eccentricities.append(ecc.mean())
       
       return np.array(eccentricities)
   ```

4. **Decoupling Analysis**
   ```python
   from sklearn.linear_model import Ridge
   
   # Prepare features
   X_motion = extract_motion_energy(video, times)  # Optical flow
   X_eccentricity = eccentricities
   X_combined = np.column_stack([X_motion, X_eccentricity])
   
   y = eeg_epochs.get_data()[:, :, :].mean(axis=2)  # Average EEG amplitude
   
   # Fit full model
   model_full = Ridge(alpha=1.0)
   model_full.fit(X_combined, y)
   
   # Fit eccentricity-only model
   model_ecc = Ridge(alpha=1.0)
   model_ecc.fit(X_eccentricity.reshape(-1, 1), y)
   
   # Compute residual (EEG not explained by eccentricity)
   y_pred_ecc = model_ecc.predict(X_eccentricity.reshape(-1, 1))
   y_residual = y - y_pred_ecc
   
   # Pure motion-attention correlation
   attention_score = np.corrcoef(y_residual, X_motion)[0, 1]
   ```

### Validation Metrics

- **Decoding accuracy**: Attention classification with/without eccentricity control
- **Generalization**: Cross-subject, cross-video performance
- **Confound magnitude**: Proportion of variance explained by eccentricity

## Applications

- **Video-based BCI**: Attention-aware content recommendation
- **Advertising research**: Implicit attention measurement
- **Clinical assessment**: Visual attention disorders
- **Driver monitoring**: Distraction detection

## Pitfalls

1. **Eye tracking errors**: Poor calibration invalidates eccentricity calculation
2. **Temporal misalignment**: EEG and eye tracking must be precisely synchronized
3. **Head movements**: Unaccounted head motion creates additional variance
4. **Individual differences**: Visual field size varies across subjects
5. **Task demands**: Top-down attention can override bottom-up eccentricity effects

## Related Skills
- naturalistic-bci-paradigms
- eeg-eye-tracking-fusion
- visual-attention-decoding
- motion-energy-analysis

## Citation
```bibtex
@article{yao2026eccentricity,
  title={Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos},
  author={Yao, Yuanyuan and Salamanca Gonzalez, Celina and Geirnaert, Simon and others},
  journal={arXiv preprint arXiv:2604.15223},
  year={2026}
}
```
