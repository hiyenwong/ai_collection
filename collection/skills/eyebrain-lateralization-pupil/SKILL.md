---
name: eyebrain-lateralization-pupil
description: "EyeBrain methodology for classifying left and right brain lateralization activity using pupil diameter and fixation duration. Non-invasive cognitive state detection via eye-tracking. Triggers: eyebrain, brain lateralization, pupil diameter, fixation duration, eye-tracking, cognitive load."
---

# EyeBrain: Brain Lateralization via Pupil Tracking

> EyeBrain classifies left and right brain hemisphere activity through non-invasive eye-tracking metrics, using pupil diameter and fixation duration as neural correlates of cognitive lateralization.

## Metadata
- **Source**: arXiv:2604.23562
- **Authors**: Ko Watanabe, Pooja Pol, Nicolas Großmann, Shoya Ishimaru
- **Published**: 2026-04-26
- **Category**: cs.CV, q-bio.NC

## Core Methodology

### Key Innovation
**EyeBrain** establishes that **pupil diameter and fixation duration** can effectively distinguish between left and right hemisphere brain activity, providing a non-invasive alternative to EEG/fMRI for studying brain lateralization.

### Biological Basis
- **Left Hemisphere**: Language processing, arithmetic, analytical tasks
- **Right Hemisphere**: Spatial processing, creative activities, holistic thinking
- **Autonomic Nervous System**: Pupil size controlled by sympathetic (dilation) and parasympathetic (constriction) pathways
- **Cognitive Load**: Task difficulty modulates pupil dilation via LC-NE system

### Eye-Brain Connection
1. **Pupil Diameter**: Reflects cognitive effort, arousal, and attention
   - Larger pupils → Higher cognitive load/engagement
   - Smaller pupils → Lower arousal/fatigue

2. **Fixation Duration**: Indicates processing depth
   - Longer fixations → Deeper processing
   - Shorter fixations → Rapid scanning

## Implementation Guide

### Prerequisites
- Eye-tracking device (Tobii, Pupil Labs, or webcam-based)
- Python libraries: `opencv-python`, `pandas`, `scikit-learn`, `numpy`
- Optional: `pupil-labs` SDK for advanced analysis

### Step-by-Step Implementation

#### Step 1: Data Collection
```python
import cv2
import numpy as np

def capture_eye_tracking_data(video_path=None):
    """
    Capture eye-tracking data from camera or video.
    
    Args:
        video_path: Path to recorded video (None for live capture)
    
    Returns:
        List of frames with eye regions
    """
    cap = cv2.VideoCapture(0 if video_path is None else video_path)
    
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert to grayscale for processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray)
        
        # Display (optional)
        cv2.imshow('Eye Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    return frames
```

#### Step 2: Pupil Detection
```python
def detect_pupil(eye_roi):
    """
    Detect pupil in eye region.
    
    Args:
        eye_roi: Grayscale image of eye region
    
    Returns:
        (pupil_center, pupil_radius)
    """
    # Preprocess
    blurred = cv2.GaussianBlur(eye_roi, (7, 7), 0)
    
    # Threshold to isolate dark pupil
    _, thresh = cv2.threshold(blurred, 0, 255, 
                              cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, 
                                     cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return None, None
    
    # Select largest contour (pupil)
    pupil_contour = max(contours, key=cv2.contourArea)
    
    # Fit ellipse to get center and size
    if len(pupil_contour) >= 5:
        ellipse = cv2.fitEllipse(pupil_contour)
        center = (int(ellipse[0][0]), int(ellipse[0][1]))
        axes = (int(ellipse[1][0]/2), int(ellipse[1][1]/2))
        radius = np.mean(axes)
        return center, radius
    
    return None, None


def calculate_pupil_diameter(pupil_radius, calibration_factor=1.0):
    """
    Convert pixel radius to real-world diameter.
    
    Args:
        pupil_radius: Radius in pixels
        calibration_factor: mm per pixel (from calibration)
    
    Returns:
        Pupil diameter in mm
    """
    return 2 * pupil_radius * calibration_factor
```

#### Step 3: Fixation Detection
```python
def detect_fixations(gaze_positions, velocity_threshold=30, 
                     min_duration=100):
    """
    Detect fixations from gaze position time series.
    
    Args:
        gaze_positions: List of (x, y, timestamp) tuples
        velocity_threshold: Velocity threshold for fixation (pixels/s)
        min_duration: Minimum fixation duration (ms)
    
    Returns:
        List of fixations: [(start_time, end_time, mean_x, mean_y, duration)]
    """
    fixations = []
    
    # Calculate velocities
    velocities = []
    for i in range(1, len(gaze_positions)):
        dx = gaze_positions[i][0] - gaze_positions[i-1][0]
        dy = gaze_positions[i][1] - gaze_positions[i-1][1]
        dt = gaze_positions[i][2] - gaze_positions[i-1][2]  # ms
        velocity = np.sqrt(dx**2 + dy**2) / (dt / 1000)  # pixels/s
        velocities.append(velocity)
    
    # Detect fixations (low velocity periods)
    i = 0
    while i < len(velocities):
        if velocities[i] < velocity_threshold:
            # Start of potential fixation
            start_idx = i
            while i < len(velocities) and velocities[i] < velocity_threshold:
                i += 1
            end_idx = i
            
            # Calculate fixation parameters
            start_time = gaze_positions[start_idx][2]
            end_time = gaze_positions[end_idx][2] if end_idx < len(gaze_positions) else gaze_positions[-1][2]
            duration = end_time - start_time
            
            if duration >= min_duration:
                # Valid fixation
                x_positions = [p[0] for p in gaze_positions[start_idx:end_idx]]
                y_positions = [p[1] for p in gaze_positions[start_idx:end_idx]]
                mean_x = np.mean(x_positions)
                mean_y = np.mean(y_positions)
                
                fixations.append({
                    'start_time': start_time,
                    'end_time': end_time,
                    'duration': duration,
                    'mean_x': mean_x,
                    'mean_y': mean_y,
                    'dispersion': np.std(x_positions) + np.std(y_positions)
                })
        else:
            i += 1
    
    return fixations
```

#### Step 4: Feature Extraction
```python
import pandas as pd

def extract_eyetracking_features(pupil_diameters, fixations, 
                                  sampling_rate=60):
    """
    Extract EyeBrain features from pupil and fixation data.
    
    Args:
        pupil_diameters: Time series of pupil diameters (mm)
        fixations: List of fixation dictionaries
        sampling_rate: Eye tracker sampling rate (Hz)
    
    Returns:
        Dictionary of features
    """
    features = {}
    
    # Pupil diameter features
    if pupil_diameters:
        features['pupil_mean'] = np.mean(pupil_diameters)
        features['pupil_std'] = np.std(pupil_diameters)
        features['pupil_max'] = np.max(pupil_diameters)
        features['pupil_min'] = np.min(pupil_diameters)
        features['pupil_range'] = features['pupil_max'] - features['pupil_min']
        
        # Frequency domain features
        from scipy import fft
        fft_vals = fft.fft(pupil_diameters)
        freqs = fft.fftfreq(len(pupil_diameters), 1/sampling_rate)
        # Low frequency power (0.04-0.15 Hz - typical for pupillometry)
        low_freq_mask = (freqs >= 0.04) & (freqs <= 0.15)
        features['pupil_low_freq_power'] = np.sum(np.abs(fft_vals[low_freq_mask])**2)
    
    # Fixation features
    if fixations:
        durations = [f['duration'] for f in fixations]
        features['fixation_mean_duration'] = np.mean(durations)
        features['fixation_std_duration'] = np.std(durations)
        features['fixation_count'] = len(fixations)
        features['fixation_rate'] = len(fixations) / (len(pupil_diameters) / sampling_rate)
        
        # Dispersion features
        dispersions = [f['dispersion'] for f in fixations]
        features['fixation_mean_dispersion'] = np.mean(dispersions)
    
    return features
```

#### Step 5: Hemisphere Classification
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def train_eyebrain_classifier(features_left, features_right):
    """
    Train EyeBrain classifier for hemisphere lateralization.
    
    Args:
        features_left: List of feature dicts from left-brain tasks
        features_right: List of feature dicts from right-brain tasks
    
    Returns:
        Trained classifier and scaler
    """
    # Combine features
    X_left = pd.DataFrame(features_left)
    X_right = pd.DataFrame(features_right)
    
    X = pd.concat([X_left, X_right], ignore_index=True)
    y = ['left'] * len(features_left) + ['right'] * len(features_right)
    
    # Handle missing values
    X = X.fillna(X.median())
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train_scaled, y_train)
    
    # Evaluate
    accuracy = clf.score(X_test_scaled, y_test)
    print(f"EyeBrain Classifier Accuracy: {accuracy:.3f}")
    
    return clf, scaler


def classify_hemisphere(features, classifier, scaler):
    """
    Classify hemisphere activity from eye-tracking features.
    
    Args:
        features: Dictionary of eye-tracking features
        classifier: Trained classifier
        scaler: Fitted scaler
    
    Returns:
        Predicted hemisphere ('left' or 'right') and confidence
    """
    X = pd.DataFrame([features])
    X_scaled = scaler.transform(X)
    
    prediction = classifier.predict(X_scaled)[0]
    probabilities = classifier.predict_proba(X_scaled)[0]
    confidence = max(probabilities)
    
    return prediction, confidence
```

### Complete Example
```python
# Experimental setup for EyeBrain
# 1. Present left-brain tasks (language, arithmetic)
# 2. Record eye-tracking during task
# 3. Present right-brain tasks (spatial, creative)
# 4. Record eye-tracking during task
# 5. Train classifier

# Collect data for left-brain tasks
left_task_features = []
for task in left_brain_tasks:
    pupil_data, fixations = run_eyetracking_session(task)
    features = extract_eyetracking_features(pupil_data, fixations)
    left_task_features.append(features)

# Collect data for right-brain tasks
right_task_features = []
for task in right_brain_tasks:
    pupil_data, fixations = run_eyetracking_session(task)
    features = extract_eyetracking_features(pupil_data, fixations)
    right_task_features.append(features)

# Train classifier
clf, scaler = train_eyebrain_classifier(left_task_features, right_task_features)

# Test on new data
test_pupil, test_fixations = run_eyetracking_session(new_task)
test_features = extract_eyetracking_features(test_pupil, test_fixations)
hemisphere, confidence = classify_hemisphere(test_features, clf, scaler)
print(f"Detected: {hemisphere} hemisphere activity (confidence: {confidence:.2f})")
```

## Applications

### Cognitive Assessment
- **Dyslexia screening**: Detect atypical lateralization patterns
- **Cognitive load monitoring**: Real-time mental workload assessment
- **Fatigue detection**: Decreased pupil reactivity indicates fatigue

### Human-Computer Interaction
- **Adaptive interfaces**: Adjust UI complexity based on cognitive load
- **Gaze-aware systems**: Context-sensitive help and guidance
- **Accessibility**: Alternative input for motor-impaired users

### Neuroscience Research
- **Non-invasive lateralization studies**: Cheaper than fMRI/EEG
- **Naturalistic settings**: Real-world cognitive activity monitoring
- **Longitudinal studies**: Track changes over time

### Clinical Applications
- **Stroke rehabilitation**: Monitor recovery of lateralized functions
- **ADHD diagnosis**: Atypical eye movement patterns
- **Mental health**: Depression/anxiety affect pupillary responses

## Pitfalls

1. **Lighting Conditions**: Pupil size affected by ambient light
   - **Solution**: Controlled lighting, normalization, or IR illumination

2. **Individual Differences**: Baseline pupil sizes vary significantly
   - **Solution**: Within-subject baselines, z-score normalization

3. **Task Design**: Must elicit clear lateralization
   - **Solution**: Use validated lateralized tasks (verbal vs. spatial)

4. **Eye Tracking Quality**: Requires good calibration
   - **Solution**: Regular calibration checks, quality metrics

5. **Cognitive Confounds**: Arousal, emotion also affect pupils
   - **Solution**: Control for emotional content, use multiple metrics

## Related Skills
- `eeg-visual-attention-decoding`: EEG-based visual attention decoding
- `bci-rehabilitation-protocols`: BCI protocols for stroke recovery
- `cognition-inspired-dual-stream-emotion`: Dual-stream emotion processing

## References
- Watanabe et al. (2026). EyeBrain: Left and Right Brain Lateralization Activity Classification Through Pupil Diameter and Fixation Duration. arXiv:2604.23562
- Beatty & Lucero-Wagoner (2000). The pupillary system. Handbook of psychophysiology
- Hess & Polt (1964). Pupil size in relation to mental activity during simple problem-solving. Science
