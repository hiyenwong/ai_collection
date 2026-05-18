---
name: brain-inspired-capture-evidence-driven-neuromimetic-perceptual
description: "Brain-Inspired Capture (BI-Cap) methodology for evidence-driven neuromimetic perceptual simulation. Biologically-inspired visual perception framework for visual decoding and brain-computer interfaces. Triggers: brain-inspired perception, neuromimetic simulation, visual decoding, evidence-driven perception, BI-Cap."
---

# Brain-Inspired Capture: Evidence-Driven Neuromimetic Perceptual Simulation

> BI-Cap methodology for brain-inspired visual perception simulation that captures biological evidence accumulation mechanisms for robust visual decoding.

## Metadata
- **Source**: arXiv:2604.17927v1
- **Published**: 2026-04

## Core Methodology

### Key Innovation
Biologically-inspired visual perception framework that implements evidence-driven perceptual decision-making based on cortical processing mechanisms. The method uses neuromimetic simulation of ventral stream processing to accumulate evidence over time, enabling robust visual decoding even with noisy or limited inputs.

### Biological Basis
- **Hierarchical Processing**: Mimics V1 → V2 → V4 → IT pathway
- **Evidence Accumulation**: Drift-diffusion-like decision process
- **Feedback Connections**: Top-down modulation of feature extraction
- **Temporal Integration**: Accumulates evidence over multiple fixation

### Architecture
```
Visual Input → V1 Features → V2/V4 Features → IT Representations
                      ↓              ↓              ↓
              Evidence Units → Accumulation → Decision
```

## Implementation Guide

### Prerequisites
- Knowledge of ventral visual stream anatomy
- Pre-trained visual feature extractors (e.g., task-driven CNNs)
- Decision-making models (drift-diffusion)
- Eye tracking or fixation data (optional)

### Step-by-Step
1. **Feature Extraction**: Extract hierarchical visual features
2. **Evidence Modeling**: Map features to evidence for categories
3. **Accumulation Simulation**: Simulate evidence accumulation over time
4. **Decision Rule**: Implement threshold-crossing decision
5. **Feedback Integration**: Add top-down modulation if available
6. **Decoding**: Map to output categories or representations

### Code Example
```python
import torch
import torch.nn as nn
import numpy as np
from scipy.stats import norm

class EvidenceAccumulator:
    def __init__(self, num_categories, drift_rate=0.1, threshold=1.0, noise_std=0.1):
        self.num_categories = num_categories
        self.drift_rate = drift_rate
        self.threshold = threshold
        self.noise_std = noise_std
        self.evidence = np.zeros(num_categories)
        self.time = 0
        
    def accumulate(self, new_evidence):
        """Accumulate new evidence with drift-diffusion dynamics"""
        # Add drift toward new evidence
        drift = self.drift_rate * (new_evidence - self.evidence)
        
        # Add noise
        noise = np.random.normal(0, self.noise_std, self.num_categories)
        
        # Update
        self.evidence += drift + noise
        self.time += 1
        
        return self.evidence
    
    def check_decision(self):
        """Check if threshold crossed"""
        max_evidence = np.max(self.evidence)
        if max_evidence >= self.threshold:
            decision = np.argmax(self.evidence)
            confidence = max_evidence / (max_evidence + np.sum(self.evidence))
            return decision, confidence, self.time
        return None, None, None
    
    def reset(self):
        """Reset accumulator"""
        self.evidence = np.zeros(self.num_categories)
        self.time = 0


class BrainInspiredCapture:
    def __init__(self, feature_extractor, evidence_transform):
        """
        BI-Cap model for visual perception
        
        feature_extractor: Hierarchical CNN (e.g., ResNet, task-driven)
        evidence_transform: Maps features to category evidence
        """
        self.feature_extractor = feature_extractor
        self.evidence_transform = evidence_transform
        self.accumulator = EvidenceAccumulator(
            num_categories=evidence_transform.output_dim
        )
        
    def extract_features(self, image, fixations=None):
        """Extract hierarchical visual features"""
        # Multi-scale feature extraction
        features = {}
        
        # Early features (V1-like)
        with torch.no_grad():
            x = image
            for i, layer in enumerate(self.feature_extractor.layers):
                x = layer(x)
                # Extract features at different stages
                if i in [2, 6, 12]:  # V1, V2, V4-like
                    features[f'layer_{i}'] = x
                if i == len(self.feature_extractor.layers) - 1:  # IT-like
                    features['IT'] = x
        
        # If fixations provided, pool features at fixation locations
        if fixations is not None:
            features = self._pool_at_fixations(features, fixations)
        
        return features
    
    def compute_evidence(self, features):
        """Map features to category evidence"""
        # Combine hierarchical features
        combined = torch.cat([
            features['layer_2'].flatten(),
            features['layer_6'].flatten(),
            features['layer_12'].flatten(),
            features['IT'].flatten()
        ])
        
        # Transform to evidence
        evidence = self.evidence_transform(combined)
        
        # Apply softmax for evidence normalization
        evidence = torch.softmax(evidence, dim=-1)
        
        return evidence.cpu().numpy()
    
    def simulate_perception(self, images, max_time=100):
        """Simulate perceptual decision over multiple fixations"""
        self.accumulator.reset()
        
        decisions = []
        for t in range(max_time):
            # Extract features from current view
            features = self.extract_features(images[t])
            
            # Compute evidence
            evidence = self.compute_evidence(features)
            
            # Accumulate
            self.accumulator.accumulate(evidence)
            
            # Check decision
            decision, confidence, time = self.accumulator.check_decision()
            if decision is not None:
                return {
                    'decision': decision,
                    'confidence': confidence,
                    'reaction_time': time,
                    'evidence_trajectory': self.accumulator.evidence.copy()
                }
        
        # No decision reached
        return {
            'decision': np.argmax(self.accumulator.evidence),
            'confidence': 0.5,
            'reaction_time': max_time,
            'evidence_trajectory': self.accumulator.evidence.copy()
        }
    
    def decode_brain_activity(self, neural_activity, visual_stimuli):
        """
        Decode visual stimuli from brain activity using BI-Cap
        
        neural_activity: Recorded activity (EEG, fMRI, etc.)
        visual_stimuli: Candidate visual inputs
        """
        # Compare neural activity to BI-Cap simulations
        similarities = []
        for stimulus in visual_stimuli:
            # Simulate perception of this stimulus
            sim_result = self.simulate_perception([stimulus], max_time=50)
            
            # Compare simulation to actual brain activity
            similarity = self._compare_to_neural(sim_result, neural_activity)
            similarities.append(similarity)
        
        # Select best match
        best_idx = np.argmax(similarities)
        return visual_stimuli[best_idx], similarities[best_idx]

# Usage
bicap = BrainInspiredCapture(feature_extractor, evidence_transform)
result = bicap.simulate_perception(images_sequence)
print(f"Decision: {result['decision']}, RT: {result['reaction_time']}ms")
```

## Applications
- Brain-computer interfaces for visual communication
- Attention modeling for AI systems
- Visual perception modeling
- Psychophysical experiment design

## Pitfalls
- **Simplification**: Real biological evidence accumulation is more complex
- **Parameter tuning**: Accumulator parameters need careful calibration
- **Computational cost**: Simulating multiple fixations is expensive
- **Feature extraction**: Task-driven features may not match biological processing

## Related Skills
- brain-inspired-attention-mechanisms
- drift-diffusion-models
- ventral-visual-stream-modeling
