---
name: sensorless-gaze-following-neuroscience
description: "Neuroscience framework for low-cost sensorless gaze-following using perception mechanisms. Enables human-robot interaction without gaze-tracking hardware. Activation: gaze-following, perception, sensorless, human-robot interaction, neuroscience, attention."
---

# Sensorless Gaze-Following: A Neuroscience Framework

> Low-cost sensorless gaze-following framework for human-robot interaction based on neuroscience principles of attention and perception.

## Metadata
- **Source**: arXiv:2604.09829v1
- **Authors**: Multiple (Neuroscience/HRI researchers)
- **Published**: 2026-04-10
- **Category**: Human-Robot Interaction, Neuroscience, Computer Vision

## Core Methodology

### Key Innovation
A neuroscience-inspired framework for gaze-following that eliminates the need for expensive eye-tracking hardware. Leverages perceptual mechanisms and attention models to infer gaze direction from scene context, head pose, and environmental cues.

### Theoretical Framework

#### 1. Perception-Based Gaze Inference
Traditional gaze-following requires:
- Eye-tracking cameras
- IR illuminators
- Calibration procedures

This framework uses:
- **Head pose estimation**: Direction of head provides gaze proxy
- **Scene saliency**: Attention-grabbing objects attract gaze
- **Social cues**: Group attention patterns
- **Task context**: Current activity predicts gaze targets

#### 2. Neuroscience Principles
**Peripheral Vision Integration**:
- Humans use peripheral vision for coarse gaze direction
- Framework simulates peripheral processing
- Reduces need for high-resolution eye images

**Attention Guidance**:
- Bottom-up saliency (visual prominence)
- Top-down goals (task-dependent attention)
- Social attention (following others' gaze)

**Predictive Coding**:
- Brain predicts gaze targets
- Framework uses predictive models
- Reduces uncertainty without eye data

### Technical Approach

#### 1. Multi-Cue Integration
```
Gaze_Target = f(Head_Pose, Scene_Saliency, Task_Context, Social_Cues)

where f combines cues with learned weights
```

#### 2. Probabilistic Framework
Bayesian inference over possible gaze targets:
```
P(Gaze | Observations) ∝ P(Observations | Gaze) * P(Gaze)

Priors:
- Spatial bias (center, upper visual field)
- Temporal continuity (gaze doesn't jump randomly)
- Task bias (relevant objects more likely)
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- OpenCV for head pose estimation
- PyTorch/TensorFlow for neural networks
- MediaPipe or similar for face detection

### Step-by-Step Implementation

#### 1. Head Pose Estimation
```python
import cv2
import numpy as np
from typing import Tuple, Optional

class HeadPoseEstimator:
    """
    Estimate 3D head pose from 2D image.
    Provides gaze direction proxy without eye tracking.
    """
    
    def __init__(self, model_path: Optional[str] = None):
        # Use MediaPipe Face Mesh or OpenCV DNN
        self.face_detector = cv2.dnn.readNetFromCaffe(
            "deploy.prototxt",
            "res10_300x300_ssd_iter_140000.caffemodel"
        )
        
        # 3D facial landmark model
        self.model_points = np.array([
            (0.0, 0.0, 0.0),        # Nose tip
            (0.0, -330.0, -65.0),   # Chin
            (-225.0, 170.0, -135.0), # Left eye left corner
            (225.0, 170.0, -135.0),  # Right eye right corner
            (-150.0, -150.0, -125.0), # Left mouth corner
            (150.0, -150.0, -125.0)   # Right mouth corner
        ])
    
    def estimate_pose(self, image: np.ndarray) -> Tuple[bool, np.ndarray, np.ndarray]:
        """
        Estimate head pose from image.
        
        Returns:
            success: Whether face was detected
            rotation_vec: 3D rotation vector
            translation_vec: 3D translation vector
        """
        h, w = image.shape[:2]
        
        # Detect face
        blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), [104.0, 177.0, 123.0])
        self.face_detector.setInput(blob)
        detections = self.face_detector.forward()
        
        if detections.shape[2] == 0:
            return False, None, None
        
        # Get best detection
        i = np.argmax(detections[0, 0, :, 2])
        confidence = detections[0, 0, i, 2]
        
        if confidence < 0.5:
            return False, None, None
        
        # Extract face region
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        
        # Use facial landmarks (simplified - use dlib or MediaPipe in practice)
        # For now, approximate landmark positions
        face_center = ((startX + endX) // 2, (startY + endY) // 2)
        
        # Camera matrix
        focal_length = w
        center = (w // 2, h // 2)
        camera_matrix = np.array([
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1]
        ], dtype="double")
        
        dist_coeffs = np.zeros((4, 1))
        
        # Solve PnP (simplified - would use actual landmarks)
        # Placeholder for landmark detection
        image_points = np.array([
            face_center,
            (face_center[0], face_center[1] + 30),
            (startX, startY + 20),
            (endX, startY + 20),
            (startX + 10, endY - 10),
            (endX - 10, endY - 10)
        ], dtype="double")
        
        success, rotation_vec, translation_vec = cv2.solvePnP(
            self.model_points, image_points, camera_matrix, dist_coeffs
        )
        
        return success, rotation_vec, translation_vec
    
    def get_gaze_direction(self, rotation_vec: np.ndarray) -> np.ndarray:
        """
        Convert rotation vector to gaze direction in world coordinates.
        
        Returns unit vector indicating approximate gaze direction.
        """
        # Convert rotation vector to rotation matrix
        rotation_mat, _ = cv2.Rodrigues(rotation_vec)
        
        # Forward direction (Z-axis of head coordinate system)
        forward = np.array([0, 0, 1])
        gaze_dir = rotation_mat @ forward
        
        return gaze_dir / np.linalg.norm(gaze_dir)
```

#### 2. Scene Saliency Computation
```python
class SceneSaliency:
    """
    Compute visual saliency map for attention prediction.
    """
    
    def __init__(self):
        self.saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
    
    def compute_saliency_map(self, image: np.ndarray) -> np.ndarray:
        """
        Compute bottom-up saliency map.
        
        Returns normalized saliency map (0-1).
        """
        success, saliency_map = self.saliency.computeSaliency(image)
        
        if success:
            return saliency_map
        else:
            return np.ones(image.shape[:2]) / 2
    
    def get_salient_regions(self, saliency_map: np.ndarray, 
                           n_regions: int = 5) -> list:
        """
        Extract top salient regions.
        
        Returns list of (x, y, saliency_score) tuples.
        """
        # Find local maxima
        from scipy.ndimage import maximum_filter
        
        local_max = (saliency_map == maximum_filter(saliency_map, size=30))
        max_coords = np.where(local_max)
        
        regions = []
        for y, x in zip(max_coords[0], max_coords[1]):
            regions.append((x, y, saliency_map[y, x]))
        
        # Sort by saliency
        regions.sort(key=lambda r: r[2], reverse=True)
        
        return regions[:n_regions]
```

#### 3. Probabilistic Gaze Target Inference
```python
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class GazeCandidate:
    """Potential gaze target with probability."""
    position: Tuple[float, float]
    probability: float
    source: str  # 'head_pose', 'saliency', 'context'

class SensorlessGazeFollower:
    """
    Main gaze-following system combining multiple cues.
    """
    
    def __init__(self, 
                 head_weight: float = 0.4,
                 saliency_weight: float = 0.3,
                 context_weight: float = 0.3):
        self.head_estimator = HeadPoseEstimator()
        self.saliency_model = SceneSaliency()
        
        self.weights = {
            'head': head_weight,
            'saliency': saliency_weight,
            'context': context_weight
        }
        
        self.previous_gaze = None
        self.gaze_history = []
    
    def infer_gaze(self, image: np.ndarray, 
                   task_context: Optional[str] = None) -> GazeCandidate:
        """
        Infer gaze target from image and context.
        
        Combines head pose, scene saliency, and task context.
        """
        h, w = image.shape[:2]
        candidates = []
        
        # 1. Head pose cue
        success, rotation_vec, translation_vec = self.head_estimator.estimate_pose(image)
        
        if success:
            gaze_dir = self.head_estimator.get_gaze_direction(rotation_vec)
            
            # Project gaze vector to image plane
            # Simplified: assume gaze lands on some point ahead
            head_center = (translation_vec[0], translation_vec[1])
            gaze_point = (
                int(head_center[0] + gaze_dir[0] * 200),
                int(head_center[1] + gaze_dir[1] * 200)
            )
            
            # Clip to image bounds
            gaze_point = (
                max(0, min(w, gaze_point[0])),
                max(0, min(h, gaze_point[1]))
            )
            
            candidates.append(GazeCandidate(
                position=gaze_point,
                probability=self.weights['head'],
                source='head_pose'
            ))
        
        # 2. Saliency cue
        saliency_map = self.saliency_model.compute_saliency_map(image)
        salient_regions = self.saliency_model.get_salient_regions(saliency_map)
        
        for (x, y, score) in salient_regions[:3]:
            candidates.append(GazeCandidate(
                position=(x, y),
                probability=score * self.weights['saliency'],
                source='saliency'
            ))
        
        # 3. Task context cue (simplified)
        if task_context:
            # Task-specific regions of interest
            # Example: if task is "reading", look at text regions
            context_candidates = self._get_task_regions(image, task_context)
            candidates.extend(context_candidates)
        
        # 4. Temporal smoothing (gaze doesn't jump randomly)
        if self.previous_gaze:
            candidates.append(GazeCandidate(
                position=self.previous_gaze.position,
                probability=0.2,  # Persistence prior
                source='temporal'
            ))
        
        # Combine candidates (simplified: weighted average)
        if candidates:
            total_prob = sum(c.probability for c in candidates)
            
            x = sum(c.position[0] * c.probability for c in candidates) / total_prob
            y = sum(c.position[1] * c.probability for c in candidates) / total_prob
            
            best_candidate = GazeCandidate(
                position=(x, y),
                probability=1.0,
                source='combined'
            )
            
            self.previous_gaze = best_candidate
            self.gaze_history.append(best_candidate)
            
            return best_candidate
        
        # Fallback: center of image
        return GazeCandidate(position=(w/2, h/2), probability=0.5, source='default')
    
    def _get_task_regions(self, image: np.ndarray, task: str) -> List[GazeCandidate]:
        """Get task-relevant regions."""
        h, w = image.shape[:2]
        
        if task == 'reading':
            # Look for text-like regions (simplified)
            return [GazeCandidate(position=(w*0.5, h*0.6), probability=0.5, source='context')]
        elif task == 'conversation':
            # Look at face regions
            return [GazeCandidate(position=(w*0.5, h*0.4), probability=0.5, source='context')]
        else:
            return []
```

#### 4. Complete System Usage
```python
def run_gaze_following_demo():
    """Demonstrate sensorless gaze following."""
    import cv2
    
    follower = SensorlessGazeFollower(
        head_weight=0.5,
        saliency_weight=0.3,
        context_weight=0.2
    )
    
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Infer gaze
        gaze = follower.infer_gaze(frame, task_context='conversation')
        
        # Visualize
        x, y = int(gaze.position[0]), int(gaze.position[1])
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)
        cv2.putText(frame, f"Gaze prob: {gaze.probability:.2f}", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow('Sensorless Gaze Following', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Run demo
# run_gaze_following_demo()
```

## Applications

### 1. Human-Robot Interaction
- **Social Robots**: Robots that follow human attention
- **Collaborative Robots**: Understanding human focus during collaboration
- **Assistive Technology**: Helping disabled users without invasive tracking

### 2. Virtual/Augmented Reality
- **Foveated Rendering**: Approximate gaze for performance optimization
- **Social VR**: Avatar eye gaze animation
- **Interaction Design**: Context-aware UI responses

### 3. Automotive
- **Driver Monitoring**: Attention tracking without eye cameras
- **Passenger Interaction**: Understanding rear passenger gaze

### 4. Accessibility
- **Low-Cost Assistive Devices**: Gaze-based control without expensive hardware
- **Privacy-Preserving**: No video recording of eyes

## Advantages

1. **Low Cost**: No specialized hardware
2. **Privacy**: No eye images recorded
3. **Calibration-Free**: Works without per-user calibration
4. **Robust**: Handles varying lighting conditions
5. **Scalable**: Can be deployed widely

## Limitations

- **Accuracy**: Less precise than eye tracking (~10-15° vs. ~1°)
- **Ambiguity**: Multiple possible gaze targets
- **Head-Eye Decoupling**: When eyes look away from head direction
- **Individual Differences**: People vary in head-eye coordination

## Pitfalls

- Assuming head direction = gaze direction (not always true)
- Ignoring individual differences in eye-head coordination
- Not handling edge cases (closed eyes, sunglasses)
- Over-relying on one cue when multiple should be combined

## Related Skills

- `perception-neuroscience-framework-sensorless-gaze`: Extended neuroscience framework
- `neuroscience-inspired-graph-virtual-sensing': Attention modeling
- `multi-agent-active-inference-digital-twins': Social attention modeling

## References

- Perception Is All You Need: A Neuroscience Framework for Low Cost Sensorless Gaze-Following. arXiv:2604.09829v1.
