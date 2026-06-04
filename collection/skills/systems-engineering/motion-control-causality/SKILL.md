---
name: motion-control-causality
description: Disentangled motion control with causality reasoning for video generation. Use when: motion-controlled video generation, disentangled control systems, motion causality modeling, active-passive motion decomposition, camera-object motion separation, forward/inverse reasoning for dynamics, physically plausible motion synthesis, or interactive motion control.
---

# Motion Control with Causality Reasoning

## Overview

This skill provides methodology for generating motion-controlled videos where user-specified actions drive physically plausible scene dynamics under freely chosen viewpoints. MoRight (Motion Control Done Right) addresses two critical limitations: entangled camera-object motion and lack of motion causality modeling.

**Key Innovation**: Unified framework enabling (1) disentangled motion control (separate object motion and camera viewpoint) and (2) motion causality (user-driven actions trigger coherent object reactions).

## Core Problem

### Existing Method Limitations

1. **Entangled Motion**: Camera and object motion combined into single tracking signal
2. **No Causality**: Motion treated as kinematic displacement without modeling causal relationships
3. **Pixel-Level Only**: Merely displacing pixels without physical plausibility
4. **Limited Control**: Cannot separately adjust camera and object motion

### Requirements for Ideal System

**Disentangled Motion Control**:
- Separate object motion specification
- Independent camera viewpoint adjustment
- Object motion transfer across viewpoints
- Canonical view to arbitrary view mapping

**Motion Causality**:
- User-driven actions trigger reactions
- Coherent object interaction dynamics
- Active vs passive motion decomposition
- Forward and inverse reasoning capability

## Framework Architecture

### 1. Disentangled Motion Modeling

**Canonical Static View**:
- Object motion specified in canonical view (static camera)
- Motion defined in object's local coordinate frame
- Independent of camera viewpoint

**Temporal Cross-View Attention**:
- Transfer motion from canonical view to target camera
- Viewpoint-dependent motion adaptation
- Maintain motion consistency across views
- Enable arbitrary camera control

**Implementation**:
```python
class DisentangledMotionModel:
    def __init__(self):
        self.canonical_view_encoder = Encoder()
        self.target_view_encoder = Encoder()
        self.cross_view_attention = TemporalCrossViewAttention()
        
    def forward(self, canonical_motion, target_camera):
        """
        Args:
            canonical_motion: motion in static view
            target_camera: desired camera viewpoint
        Returns:
            motion adapted to target view
        """
        canonical_features = self.canonical_view_encoder(canonical_motion)
        target_features = self.target_view_encoder(target_camera)
        adapted_motion = self.cross_view_attention(
            canonical_features, target_features
        )
        return adapted_motion
```

### 2. Motion Causality Decomposition

**Active Motion** (User-driven):
- Actions user explicitly controls
- Primary motion driver
- Example: hand pushing object, person walking

**Passive Motion** (Consequence):
- Reactions triggered by active motion
- Coherent physical responses
- Example: teapot sliding from hand push, door swinging open

**Forward Reasoning**:
- Input: Active motion specification
- Output: Predicted passive outcomes
- Use case: "What happens if I push this?"

**Inverse Reasoning**:
- Input: Desired passive outcomes
- Output: Plausible driving actions
- Use case: "What action causes teapot trajectory?"

### 3. Motion Decomposition Training

**Dataset Requirements**:
- Videos with object interactions
- Motion causality examples
- Active-passive motion annotations

**Training Objective**:
```python
def train_motion_causality(model, video_data):
    """
    Train model to decompose and predict motion
    
    Args:
        model: MoRight model
        video_data: annotated video clips
    """
    for clip in video_data:
        # Extract active motion
        active_motion = extract_active_motion(clip)
        
        # Extract passive motion (consequence)
        passive_motion = extract_passive_motion(clip)
        
        # Forward reasoning: predict passive from active
        predicted_passive = model.forward_reasoning(active_motion)
        loss_forward = mse(predicted_passive, passive_motion)
        
        # Inverse reasoning: recover active from passive
        recovered_active = model.inverse_reasoning(passive_motion)
        loss_inverse = mse(recovered_active, active_motion)
        
        # Combined loss
        total_loss = loss_forward + loss_inverse
        optimize(total_loss)
```

## Key Capabilities

### Disentangled Camera-Object Control

**User Controls**:
- **Object Motion**: Specify in canonical view
- **Camera Viewpoint**: Adjust freely (zoom-in, orbit, zoom-out)

**Benefits**:
- Explore scene with custom viewpoints
- Specify motion without camera constraints
- Transfer motion across viewpoints
- Independent control channels

### Motion Causality Reasoning

**Forward Reasoning**:
```
Input: Active motion (hand push)
Output: Passive motion (teapot trajectory)
```

**Inverse Reasoning**:
```
Input: Desired outcome (teapot trajectory)
Output: Driving action (hand push direction)
```

**Applications**:
- Interactive motion control
- Physical plausibility enforcement
- Action-reaction consistency
- Scene dynamics modeling

## Implementation Workflow

### Step 1: Define Motion in Canonical View

```python
# Specify object motion in static camera view
canonical_motion = {
    'object': 'hand',
    'trajectory': [(x1, y1), (x2, y2), ...],
    'velocity': [vx, vy],
    'duration': t
}
```

### Step 2: Define Target Camera Viewpoint

```python
# Specify desired camera viewpoint
target_camera = {
    'position': (cam_x, cam_y, cam_z),
    'orientation': (yaw, pitch, roll),
    'zoom': scale_factor
}
```

### Step 3: Apply Temporal Cross-View Attention

```python
# Transfer motion from canonical to target view
adapted_motion = model.transfer_motion(
    canonical_motion,
    target_camera
)

# Generate video frames with adapted motion
video_frames = generate_video(adapted_motion, target_camera)
```

### Step 4: Motion Causality Reasoning

```python
# Forward reasoning example
active_motion = {
    'action': 'push',
    'direction': 'right',
    'force': 'moderate'
}

# Predict consequences
passive_motion = model.forward_reasoning(active_motion)

# Inverse reasoning example
desired_outcome = {
    'object': 'teapot',
    'trajectory': [(0, 0), (0.5, 0), (1.0, 0)],
    'final_position': (1.0, 0)
}

# Recover driving action
driving_action = model.inverse_reasoning(desired_outcome)
```

### Step 5: Generate Video

```python
# Combine all components
final_motion = {
    'active': active_motion,
    'passive': passive_motion,
    'camera': target_camera
}

# Render video
video = render_motion_controlled_video(final_motion)
```

## Technical Components

### Temporal Cross-View Attention

**Purpose**: Transfer motion across viewpoints

**Mechanism**:
- Encode canonical motion features
- Encode target camera features
- Attention-based feature alignment
- Motion adaptation to new viewpoint

**Architecture**:
```
Canonical Features -> Encoder -> Feature Map
Target Camera -> Encoder -> View Features
Cross-View Attention -> Alignment -> Adapted Motion
```

### Motion Decomposition Network

**Active Motion Encoder**:
- Identifies user-driven actions
- Extracts primary motion components
- Represents motion intent

**Passive Motion Encoder**:
- Identifies consequence motion
- Extracts reaction components
- Represents physical responses

**Causality Module**:
- Models active-passive relationships
- Forward prediction network
- Inverse recovery network

### Video Generation Model

**Input**:
- Adapted motion sequences
- Camera viewpoint parameters
- Scene context

**Output**:
- Video frames with motion
- Physically plausible dynamics
- Viewpoint-consistent rendering

## Performance Metrics

### Generation Quality

- Visual fidelity
- Motion smoothness
- Physical plausibility
- Temporal coherence

### Motion Controllability

- Control precision
- Disentanglement accuracy
- Viewpoint flexibility
- Motion specification ease

### Interaction Awareness

- Causality correctness
- Forward prediction accuracy
- Inverse recovery plausibility
- Physical consistency

## Benchmarks

Tested on three benchmarks demonstrating:
- State-of-the-art generation quality
- Superior motion controllability
- Enhanced interaction awareness

**Benchmark Categories**:
- Visual quality metrics
- Control accuracy tests
- Causality validation
- User preference studies

## Applications

### Interactive Video Generation

**Use Cases**:
- Controllable video creation
- Custom viewpoint exploration
- Interactive storytelling
- Dynamic scene generation

**User Workflow**:
1. Specify object motion
2. Choose camera viewpoint
3. See motion causality unfold
4. Adjust and iterate

### Simulation and Training

**Use Cases**:
- Robotics training scenarios
- Physical interaction simulation
- Motion planning visualization
- Control system testing

**Benefits**:
- Physically plausible dynamics
- Controllable scenarios
- Multiple viewpoint options
- Action-reaction modeling

### Entertainment and Media

**Use Cases**:
- Movie previsualization
- Animation control
- Game scene generation
- Interactive experiences

**Benefits**:
- Motion control flexibility
- Causality enforcement
- Custom viewpoint rendering
- Real-time iteration

## Research Paper Reference

**Paper**: "MoRight: Motion Control Done Right"
- **Authors**: Shaowei Liu, Xuanchi Ren, Tianchang Shen, et al.
- **arXiv ID**: 2604.07348
- **Published**: April 8, 2026
- **Categories**: cs.CV, cs.AI, cs.GR, cs.LG, cs.RO
- **Link**: https://arxiv.org/abs/2604.07348
- **Project Page**: https://research.nvidia.com/labs/sil/projects/moright

## Related Skills

- **video-generation**: General video generation techniques
- **motion-synthesis**: Motion generation methods
- **physical-simulation**: Physics-based simulation
- **control-systems**: Control theory fundamentals

## Implementation Examples

### Example 1: Hand Push Teapot

```python
# Forward reasoning: push action -> teapot trajectory
action = MotionAction(
    type='push',
    object='hand',
    direction=(1.0, 0.0),  # rightward
    force=0.5
)

consequence = model.predict_consequence(action)
# Returns: teapot sliding trajectory, rotation, etc.

# Generate video with free viewpoint
camera = CameraView(
    position=(2.0, 1.0, 3.0),
    zoom=1.5
)

video = model.generate(action, consequence, camera)
```

### Example 2: Inverse Reasoning

```python
# Inverse reasoning: desired outcome -> driving action
desired_trajectory = Trajectory(
    object='door',
    path=[closed, partially_open, fully_open],
    duration=2.0
)

# Recover plausible action
action = model.recover_action(desired_trajectory)
# Returns: hand pull motion, direction, timing, etc.

# Generate with recovered action
video = model.generate_with_recovered_action(
    desired_trajectory, 
    action, 
    custom_camera
)
```

### Example 3: Multi-Object Interaction

```python
# Complex scene with multiple objects
scene = Scene([
    Object('hand', initial_pos=(0, 0)),
    Object('teapot', initial_pos=(1, 0)),
    Object('table', static=True)
])

# Define active motion
active_motion = [
    Motion('hand', trajectory=[(0, 0) -> (1, 0) -> (2, 0)]),
]

# Predict all passive motions
passive_motions = model.predict_consequences(scene, active_motion)
# Returns: teapot sliding, table contact response, etc.

# Generate with viewpoint control
for viewpoint in ['front', 'top', 'side']:
    video = model.generate_view(scene, viewpoint)
```

## Technical Details

### Model Architecture

**Encoder Networks**:
- CNN backbone for visual features
- Temporal encoder for motion dynamics
- View encoder for camera parameters

**Attention Mechanisms**:
- Spatial attention for object focus
- Temporal attention for motion coherence
- Cross-view attention for viewpoint transfer

**Decoder Networks**:
- Frame decoder for video synthesis
- Motion decoder for trajectory output
- Control decoder for action parameters

### Training Data

**Data Requirements**:
- Interaction videos with annotations
- Active-passive motion labels
- Camera viewpoint variations
- Physical dynamics examples

**Annotation Types**:
- Object motion trajectories
- Action type labels
- Consequence descriptions
- Viewpoint metadata

## Future Directions

**Real-time Generation**:
- Faster inference methods
- Streaming generation
- Interactive editing
- Live control

**More Complex Interactions**:
- Multi-object causality chains
- Indirect interactions
- Environmental responses
- Human-like motion patterns

**Extended Applications**:
- Virtual reality scenarios
- Augmented reality integration
- Robotics planning
- Autonomous vehicle simulation

## See Also

- Video generation frameworks
- Physical simulation engines
- Motion control systems
- Causality reasoning methods