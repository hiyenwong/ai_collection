---
name: neural-behavioral-whole-body-movement-monkeys
description: "Neural-behavioral representation framework for natural whole-body movement in primates. Combines large-scale epidural cortical signals with synchronized multi-view motion capture to decode unconstrained whole-body kinematics. Use when: (1) decoding natural whole-body movements, (2) modeling neural-behavioral representations, (3) primate motor neuroscience research, (4) developing behavior priors for movement decoding. Keywords: whole-body movement, motor decoding, primate neuroscience, neural-behavioral representation, behavior prior, motion capture, epidural signals"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.29355"
  published: "2026-05-28"
  authors: "Jieshi He, Puzhe Li, Yanan Sui, Mu-ming Poo"
  tags: [whole-body-movement, motor-decoding, primate, neural-behavioral, behavior-prior, epidural, motion-capture]
---

# Neural-Behavioral Representation of Natural Whole-body Movement

Research methodology from arXiv:2605.29355 — neural-behavioral recording and modeling framework for freely moving monkeys, enabling decoding of natural whole-body movements.

## Core Contribution

**Breakthrough**: First framework combining large-scale epidural cortical signals with multi-view motion capture to decode accurate and realistic whole-body movement in freely moving primates, without explicit physical constraints.

## Methodology Overview

### Data Collection Platform

1. **Neural Recording**: Large-scale epidural cortical signals from distributed sensory- and motor-related areas
2. **Motion Capture**: Synchronized multi-view video capture
3. **Subjects**: Freely moving monkeys (unconstrained behavior)

### Behavior Prior Learning

```python
# Autoregressive encoder-decoder for behavior prior
class BehaviorPrior:
    def __init__(self):
        self.encoder = AutoregressiveEncoder()
        self.decoder = AutoregressiveDecoder()
        self.latent_dim = 64  # Compact representation
    
    def learn_prior(self, kinematics_sequence):
        # Learn compact behavior prior from motion capture
        latent = self.encoder(kinematics_sequence)
        reconstruction = self.decoder(latent)
        return latent, reconstruction
```

### Neural-Conditioned Decoding

```python
# Neural-to-whole-body decoding
class WholeBodyDecoder:
    def __init__(self, behavior_prior):
        self.neural_encoder = NeuralSignalEncoder()
        self.prior = behavior_prior
        self.trajectory_generator = TrajectoryGenerator()
    
    def decode(self, neural_signals):
        # Condition on neural signals, generate whole-body movement
        neural_features = self.neural_encoder(neural_signals)
        trajectory = self.trajectory_generator(neural_features, self.prior)
        return trajectory  # Realistic whole-body kinematics
```

## Key Innovations

### 1. Unconstrained Natural Behavior

- Previous studies: Constrained tasks, limited limb movements
- This framework: Free movement, diverse whole-body behaviors
- Advantage: Captures natural motor repertoire

### 2. Implicit Physical Constraints

- Traditional: Explicit physics models required
- This approach: Behavior prior learns realistic dynamics
- Benefit: Accurate and naturalistic movement reconstruction

### 3. Large-Scale Neural Integration

- **Distributed recording**: Sensorimotor-related cortical areas
- **Scale**: Epidural signals from multiple regions simultaneously
- **Synchronization**: Neural-behavioral temporal alignment

## Implementation Guide

### Motion Capture Processing

```python
# Multi-view kinematics reconstruction
def reconstruct_whole_body(multi_view_videos):
    """
    Steps:
    1. Pose estimation per view
    2. 3D triangulation
    3. Kinematics parameterisation
    """
    poses = [estimate_pose(v) for v in multi_view_videos]
    kinematics_3d = triangulate_3d(poses)
    body_params = parameterise_kinematics(kinematics_3d)
    return body_params
```

### Behavior Prior Architecture

```python
# Compact behavior prior model
class AutoregressivePrior:
    """
    Autoregressive encoder-decoder for:
    - Learning compact movement representation
    - Generating realistic trajectories
    - Implicit dynamics constraints
    """
    def encode(self, kinematics):
        # Temporal compression
        return self.rnn_encoder(kinematics)
    
    def decode(self, latent, steps):
        # Trajectory generation
        return self.rnn_decoder(latent, steps)
```

## Experimental Framework

| Component | Description |
|-----------|-------------|
| Neural Signals | Epidural cortical from sensorimotor areas |
| Behavior Data | Multi-view motion capture |
| Behavior Prior | Autoregressive encoder-decoder |
| Decoder | Neural-conditioned trajectory generator |
| Output | Whole-body kinematics without physics constraints |

## Applications

1. **Motor Neuroscience**: Understanding cortical representation of natural movement
2. **Neural Prosthetics**: Whole-body assistive device control
3. **Behavior Modeling**: Animal locomotion simulation
4. **Rehabilitation**: Motor recovery assessment

## Comparison with Previous Approaches

| Aspect | Traditional | This Framework |
|--------|-------------|----------------|
| Task Type | Constrained | Free movement |
| Movement Scope | Limited limbs | Whole-body |
| Physics Constraints | Explicit | Implicit (learned) |
| Neural Scale | Single region | Distributed cortical |

## Pitfalls & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Behavior diversity | Unconstrained movement | Behavior prior captures repertoire |
| Kinematic realism | Physics constraints needed | Prior learns implicit dynamics |
| Neural-behavior alignment | Temporal synchronization | Multi-view + neural sync hardware |

## References

- arXiv:2605.29355 — Full paper (3,889 KB)
- Submitted to cs.LG / q-bio.NC

## Activation

Keywords: whole-body movement, primate motor, neural-behavioral, behavior prior, motor decoding, epidural, natural behavior