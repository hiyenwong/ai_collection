---
name: eeg-3d-visual-decoding
description: Multimodal architecture for EEG-to-3D visual reconstruction using geometry-aware generative reasoning. Progressively transforms neural representations into 3D domain using EEG-to-image decoding followed by multimodal LLM-based 3D-aware description extraction.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, EEG, 3D-reconstruction, visual-decoding, multimodal, LLM, brain-computer-interface]
    source_paper: "Brain3D: EEG-to-3D Decoding of Visual Representations via Multimodal Reasoning (arXiv:2604.08068)"
    citations: 0
    published: "2026-04-09"
---

# EEG-to-3D Visual Decoding

## Overview

This skill implements **Brain3D**, a multimodal architecture for EEG-to-3D reconstruction of visual representations. It progressively transforms neural representations from EEG signals into the 3D domain using geometry-aware generative reasoning.

## Key Innovation

**3D Visual Reconstruction from EEG**: While most EEG decoding focuses on 2D image reconstruction, this approach enables geometric understanding by reconstructing 3D representations, opening new applications in spatial reasoning and immersive interfaces.

## Core Concepts

### 1. Progressive 3D Reconstruction Pipeline
```
EEG Signal → 2D Image → Structured Description → 3D Representation
     ↓           ↓              ↓                    ↓
  Neural    Visually       LLM-based          Geometry-aware
Activity   Grounded       3D-aware            Generation
```

### 2. Architecture Components
```python
import torch
import torch.nn as nn
from diffusers import StableDiffusionPipeline
from transformers import CLIPProcessor, CLIPModel, AutoModelForCausalLM, AutoTokenizer

class Brain3D(nn.Module):
    """
    Brain3D: EEG-to-3D reconstruction via multimodal reasoning.
    """
    
    def __init__(self):
        super(Brain3D, self).__init__()
        
        # Stage 1: EEG-to-Image Decoder
        self.eeg_encoder = EEGEncoder()
        self.image_decoder = EEG2ImageDecoder()
        
        # Stage 2: Multimodal LLM for 3D-aware description
        self.vision_encoder = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.multimodal_llm = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b")
        self.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b")
        
        # Stage 3: 3D-aware generation
        self.diffusion_3d = Diffusion3DGenerator()
    
    def forward(self, eeg_signal):
        """
        Args:
            eeg_signal: Raw EEG data (channels, timepoints)
        
        Returns:
            image_2d: Reconstructed 2D image
            description_3d: Structured 3D description
            representation_3d: Generated 3D representation
        """
        # Stage 1: EEG to 2D image
        eeg_features = self.eeg_encoder(eeg_signal)
        image_2d = self.image_decoder(eeg_features)
        
        # Stage 2: Generate 3D-aware description
        description_3d = self.generate_3d_description(image_2d, eeg_features)
        
        # Stage 3: Generate 3D representation
        representation_3d = self.diffusion_3d.generate(description_3d, image_2d)
        
        return image_2d, description_3d, representation_3d
```

### 3. EEG Encoder
```python
class EEGEncoder(nn.Module):
    """
    Encode EEG signals into latent representations.
    Uses temporal and spatial feature extraction.
    """
    
    def __init__(self, n_channels=64, n_timepoints=256, latent_dim=512):
        super(EEGEncoder, self).__init__()
        
        # Temporal convolution
        self.temporal_conv = nn.Sequential(
            nn.Conv1d(n_channels, 128, kernel_size=25, stride=4),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Conv1d(128, 256, kernel_size=13, stride=2),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Conv1d(256, 512, kernel_size=7, stride=2),
            nn.BatchNorm1d(512),
            nn.ReLU()
        )
        
        # Spatial attention
        self.spatial_attention = SpatialAttention(n_channels)
        
        # Final projection
        self.projection = nn.Linear(512 * 8, latent_dim)
    
    def forward(self, eeg):
        """
        Args:
            eeg: (batch, channels, timepoints)
        
        Returns:
            features: (batch, latent_dim)
        """
        # Apply spatial attention
        eeg = self.spatial_attention(eeg)
        
        # Temporal convolution
        features = self.temporal_conv(eeg)
        
        # Flatten and project
        features = features.view(features.size(0), -1)
        features = self.projection(features)
        
        return features

class SpatialAttention(nn.Module):
    """Spatial attention for EEG channels."""
    
    def __init__(self, n_channels):
        super(SpatialAttention, self).__init__()
        self.attention = nn.Sequential(
            nn.Linear(n_channels, n_channels // 4),
            nn.ReLU(),
            nn.Linear(n_channels // 4, n_channels),
            nn.Sigmoid()
        )
    
    def forward(self, eeg):
        # Compute channel-wise attention
        avg_features = eeg.mean(dim=2)  # (batch, channels)
        attention_weights = self.attention(avg_features)  # (batch, channels)
        
        # Apply attention
        attended = eeg * attention_weights.unsqueeze(2)
        return attended
```

### 4. EEG-to-Image Decoder
```python
class EEG2ImageDecoder(nn.Module):
    """
    Decode EEG features into 2D images using diffusion model conditioning.
    """
    
    def __init__(self, latent_dim=512, image_size=256):
        super(EEG2ImageDecoder, self).__init__()
        
        self.latent_dim = latent_dim
        self.image_size = image_size
        
        # Latent to image features
        self.feature_mapper = nn.Sequential(
            nn.Linear(latent_dim, 1024),
            nn.ReLU(),
            nn.Linear(1024, 4096),
            nn.ReLU()
        )
        
        # Upsampling to image
        self.upsampler = nn.Sequential(
            nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.ConvTranspose2d(64, 32, kernel_size=4, stride=2, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.ConvTranspose2d(32, 3, kernel_size=4, stride=2, padding=1),
            nn.Tanh()
        )
    
    def forward(self, eeg_features):
        """
        Args:
            eeg_features: (batch, latent_dim)
        
        Returns:
            image: (batch, 3, image_size, image_size)
        """
        # Map to spatial features
        features = self.feature_mapper(eeg_features)
        features = features.view(-1, 256, 4, 4)
        
        # Upsample to image
        image = self.upsampler(features)
        
        return image
```

### 5. 3D-Aware Description Generation
```python
class Multimodal3DDescriber:
    """
    Generate structured 3D-aware descriptions using multimodal LLM.
    """
    
    def __init__(self):
        self.clip = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.llm = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b")
        self.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b")
    
    def generate_description(self, image, eeg_features):
        """
        Generate 3D-aware description from image and EEG.
        
        Args:
            image: Reconstructed 2D image
            eeg_features: EEG latent features
        
        Returns:
            description: Structured 3D description
        """
        # Encode image with CLIP
        image_inputs = self.processor(images=image, return_tensors="pt")
        image_features = self.clip.get_image_features(**image_inputs)
        
        # Create prompt
        prompt = self._create_3d_prompt(image_features, eeg_features)
        
        # Generate description with LLM
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.llm.generate(
            **inputs,
            max_length=512,
            temperature=0.7,
            do_sample=True
        )
        
        description = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Parse structured description
        structured_desc = self._parse_description(description)
        
        return structured_desc
    
    def _create_3d_prompt(self, image_features, eeg_features):
        """Create prompt for 3D description generation."""
        prompt = """Based on the brain activity pattern and visual input, describe the 3D structure:

Scene Type: [indoor/outdoor/object]
Main Objects: [list of objects with 3D positions]
Spatial Relationships: [how objects relate in 3D space]
Depth Information: [near/far regions]
Geometry: [shapes and forms]

Provide a structured description suitable for 3D reconstruction:"""
        return prompt
    
    def _parse_description(self, text):
        """Parse LLM output into structured format."""
        # Extract structured information
        structured = {
            'scene_type': self._extract_field(text, 'Scene Type'),
            'objects': self._extract_objects(text),
            'spatial_relations': self._extract_field(text, 'Spatial Relationships'),
            'depth': self._extract_field(text, 'Depth Information'),
            'geometry': self._extract_field(text, 'Geometry')
        }
        return structured
```

### 6. 3D Generation
```python
class Diffusion3DGenerator:
    """
    Generate 3D representations from descriptions using diffusion model.
    """
    
    def __init__(self):
        # 3D-aware diffusion model (e.g., based on Point-E or similar)
        self.diffusion_model = self._load_3d_diffusion_model()
    
    def generate(self, description, image_condition):
        """
        Generate 3D representation from description.
        
        Args:
            description: Structured 3D description
            image_condition: 2D image for conditioning
        
        Returns:
            representation_3d: Generated 3D representation (point cloud or mesh)
        """
        # Encode description
        text_embedding = self._encode_description(description)
        
        # Encode image condition
        image_embedding = self._encode_image(image_condition)
        
        # Combine embeddings
        condition = torch.cat([text_embedding, image_embedding], dim=-1)
        
        # Generate 3D via diffusion
        representation_3d = self.diffusion_model.sample(condition)
        
        return representation_3d
```

## Implementation Pattern

### Complete Pipeline
```python
class EEG3DReconstructionPipeline:
    """
    Complete pipeline for EEG-to-3D visual reconstruction.
    """
    
    def __init__(self, device='cuda'):
        self.device = device
        self.model = Brain3D().to(device)
        
        # Load pretrained components
        self._load_pretrained()
    
    def _load_pretrained(self):
        """Load pretrained weights for components."""
        # Load EEG encoder
        self.model.eeg_encoder.load_state_dict(
            torch.load('eeg_encoder_pretrained.pth')
        )
        
        # Load image decoder
        self.model.image_decoder.load_state_dict(
            torch.load('eeg2image_pretrained.pth')
        )
    
    def reconstruct(self, eeg_signal):
        """
        Reconstruct 3D representation from EEG.
        
        Args:
            eeg_signal: EEG data (channels, timepoints) or (batch, channels, timepoints)
        
        Returns:
            result: Dict with 'image_2d', 'description_3d', 'representation_3d'
        """
        if eeg_signal.dim() == 2:
            eeg_signal = eeg_signal.unsqueeze(0)
        
        eeg_signal = eeg_signal.to(self.device)
        
        with torch.no_grad():
            image_2d, description_3d, representation_3d = self.model(eeg_signal)
        
        return {
            'image_2d': image_2d.cpu(),
            'description_3d': description_3d,
            'representation_3d': representation_3d.cpu()
        }
    
    def train_step(self, eeg_batch, image_batch, description_batch, representation_batch):
        """Single training step."""
        # Forward pass
        image_pred, desc_pred, rep_pred = self.model(eeg_batch)
        
        # Compute losses
        image_loss = F.mse_loss(image_pred, image_batch)
        desc_loss = self._description_loss(desc_pred, description_batch)
        rep_loss = self._3d_loss(rep_pred, representation_batch)
        
        # Combined loss
        total_loss = image_loss + 0.5 * desc_loss + rep_loss
        
        # Backward pass
        total_loss.backward()
        
        return total_loss.item()
```

## Applications

1. **Immersive BCI**: 3D environment control via brain signals
2. **Spatial Memory Research**: Study how brain encodes 3D space
3. **Virtual Reality**: Brain-driven VR content generation
4. **Robotics**: 3D scene understanding for brain-controlled robots
5. **Neuroprosthetics**: Spatial navigation aids for visually impaired

## Advantages

| Aspect | 2D Decoding | 3D Decoding (Brain3D) |
|--------|-------------|----------------------|
| Spatial understanding | Limited | Full 3D geometry |
| Applications | Image retrieval | VR, robotics, navigation |
| Information content | 2D projection | Depth + structure |
| Cognitive relevance | Basic vision | Spatial cognition |

## References

- Balloni, E., et al. (2026). Brain3D: EEG-to-3D Decoding of Visual Representations via Multimodal Reasoning. arXiv:2604.08068.
- Related: EEG2Image (Xu et al., 2023), Multimodal LLMs (Liu et al., 2023)

## See Also

- `in-context-brain-decoding`: Cross-subject brain decoding
- `eeg-cnn-autoencoder`: EEG classification methods
