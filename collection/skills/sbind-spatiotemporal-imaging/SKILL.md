# SBIND: Spatiotemporal Brain Imaging Neural Dynamics

**Source:** arXiv:2509.18507 (ICML 2025)
**Utility:** 0.94
**Created:** 2026-03-25

## Activation Keywords

- SBIND
- spatiotemporal neural imaging
- behaviorally relevant dynamics
- widefield calcium imaging
- functional ultrasound imaging
- neural-behavioral prediction
- disentangle neural dynamics

## Description

A deep learning framework for modeling spatiotemporal dependencies in neural imaging data and disentangling behaviorally relevant dynamics from irrelevant neural activity.

## Core Methodology

### 1. Problem: High-Dimensional Neural Imaging

**Challenges:**
- High dimensionality of imaging data
- Complex spatiotemporal dependencies
- Behaviorally irrelevant dynamics obscure signal
- Existing preprocessing discards relevant information

**Modalities:**
- Widefield calcium imaging
- Functional ultrasound imaging (fUS)

### 2. SBIND Framework

**Key Components:**

1. **Spatiotemporal Modeling**
   - Captures local and long-range spatial dependencies
   - Models temporal dynamics across brain regions

2. **Behavioral Disentanglement**
   - Separates behaviorally relevant dynamics
   - Filters out behaviorally irrelevant activity

3. **End-to-End Learning**
   - No separate preprocessing/dimensionality reduction
   - Preserves behaviorally relevant information

### 3. Architecture

```python
# Conceptual SBIND architecture
class SBIND(nn.Module):
    """
    Spatiotemporal Brain Imaging Neural Dynamics model
    
    Key features:
    - Spatial attention for long-range dependencies
    - Temporal convolution for dynamics
    - Behavioral disentanglement module
    """
    
    def __init__(self, spatial_dim, temporal_dim, behavioral_dim):
        super().__init__()
        
        # Spatial encoder with attention
        self.spatial_encoder = SpatialAttentionEncoder(spatial_dim)
        
        # Temporal dynamics module
        self.temporal_module = TemporalConvNet(temporal_dim)
        
        # Behavioral disentanglement
        self.disentangle = BehavioralDisentanglement(behavioral_dim)
        
        # Prediction head
        self.predictor = BehavioralPredictor()
    
    def forward(self, neural_images):
        """
        Args:
            neural_images: [B, T, H, W] spatiotemporal imaging data
        Returns:
            behavioral_prediction: [B, T, behavioral_dim]
            relevant_dynamics: disentangled behaviorally relevant activity
        """
        # Extract spatiotemporal features
        features = self.spatial_encoder(neural_images)
        dynamics = self.temporal_module(features)
        
        # Disentangle behavioral relevance
        relevant, irrelevant = self.disentangle(dynamics)
        
        # Predict behavior
        prediction = self.predictor(relevant)
        
        return prediction, relevant
```

## Applications

### 1. Neural-Behavioral Prediction
- Predict behavior from neural activity
- Outperforms existing models
- Works across imaging modalities

### 2. Functional Ultrasound Imaging
- First dynamical model for fUS
- Extends naturally to new modalities
- No modality-specific engineering

### 3. Mechanism Investigation
- Identify behaviorally relevant brain regions
- Discover spatiotemporal patterns
- Understand neural encoding of behavior

## Key Results

| Metric | SBIND vs Baselines |
|--------|-------------------|
| Neural-behavioral prediction | Superior |
| Spatial dependency capture | Both local & long-range |
| Behavioral relevance | Successfully disentangled |

## Implementation

```bash
# Install SBIND
pip install sbind

# Or from source
git clone https://github.com/ShanechiLab/SBIND/
cd SBIND
pip install -e .
```

## When to Use

- Analyzing widefield calcium imaging data
- Working with functional ultrasound imaging
- Need to disentangle behavioral relevance
- High-dimensional neural imaging analysis
- Neural-behavioral prediction tasks

## Related Skills

- `eeg-brain-connectivity-bci` - EEG analysis
- `time-varying-brain-connectivity` - Dynamic connectivity
- `dnn-neural-decoding` - Neural decoding

## References

- Hosseini, S.M., et al. "Dynamical Modeling of Behaviorally Relevant Spatiotemporal Patterns in Neural Imaging Data." ICML 2025.
- Code: https://github.com/ShanechiLab/SBIND/