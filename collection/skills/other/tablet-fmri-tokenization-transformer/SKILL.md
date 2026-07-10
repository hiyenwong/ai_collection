---
name: tablet-fmri-tokenization-transformer
description: "TABLeT framework for fMRI volume tokenization using pre-trained 2D natural image autoencoders, enabling long-range spatiotemporal dynamics modeling with Transformer encoders. Activation triggers: fMRI tokenization, brain transformer, TABLeT, neuroimaging autoencoder, long-range brain dynamics, UK Biobank fMRI."
---

# TABLeT: Two-dimensionally Autoencoded Brain Latent Transformer

> Novel approach that tokenizes fMRI volumes using pre-trained 2D natural image autoencoders, enabling efficient long-sequence modeling of brain spatiotemporal dynamics.

## Metadata
- **Source**: arXiv:2604.03619v1
- **Authors**: Peter Yongho Kim, Juhyeon Park, Jungwoo Park, Jubin Choi, Jungwoo Seo, Jiook Cha, Taesup Moon
- **Published**: 2026-04-04
- **Category**: Neuroimaging, Deep Learning, fMRI Analysis
- **Code**: https://github.com/beotborry/TABLeT

## Core Methodology

### Problem Statement

**Challenges in fMRI Spatiotemporal Modeling**:
1. **High Dimensionality**: 4D signals (3D spatial + time) are extremely large
2. **Memory Constraints**: Voxel-based models limited by VRAM
3. **Temporal Windows**: Can only capture limited temporal context
4. **Scalability**: Large-scale datasets (UK Biobank, HCP) demand efficient methods

**Existing Approaches**:
- Voxel-based models: Excellent performance but memory-prohibitive
- ROI-based models: Lose spatial resolution
- Simple downsampling: Loss of fine-grained information

### TABLeT Innovation

**Core Idea**: Use pre-trained 2D natural image autoencoders to tokenize 3D fMRI volumes into compact, continuous token representations.

**Why Natural Image Autoencoders?**
- Pre-trained on ImageNet (massive datasets)
- Learned rich visual representations
- Transferable to neuroimaging (brain activity patterns are spatially structured)
- Avoids training from scratch

### Architecture

```
Input: 3D fMRI Volume (X × Y × Z × T)
           ↓
[2D Slice Extraction]
           ↓
[Pre-trained Autoencoder Encoder]
           ↓
[Continuous Token Sequence]
           ↓
[Transformer Encoder]
           ↓
Output: Brain dynamics prediction / Classification
```

#### Detailed Components

**1. Volume-to-2D Slicing**
```python
# 3D volume → 2D axial slices
volume shape: (H, W, D)  # Height, Width, Depth (slices)
slices: [slice_1, slice_2, ..., slice_D]  # D 2D images
```

**2. Autoencoder Tokenization**
```python
# Using pre-trained autoencoder (e.g., VQ-VAE, Stable Diffusion VAE)
for each 2D slice:
    tokens = encoder(slice)  # e.g., 16×16 tokens per slice
    token_dim = 512 or 768  # channel dimension
```

**3. Token Sequence Construction**
```python
# Concatenate tokens from all slices
total_tokens = D × tokens_per_slice
sequence_length = total_tokens
```

**4. Transformer Processing**
```python
# Standard Transformer encoder
output = TransformerEncoder(token_sequence)
```

### Key Advantages

| Feature | TABLeT | Voxel-Based | ROI-Based |
|---------|--------|-------------|-----------|
| Spatial Resolution | High | Full | Low |
| Memory Efficiency | High | Poor | High |
| Temporal Context | Long | Short | Long |
| Pre-training | Transfer | From scratch | From scratch |
| Interpretability | Token-level | Voxel-level | Region-level |

### Self-Supervised Pre-training

**Masked Token Modeling (MTM)**:
```python
# Similar to BERT's masked language modeling
1. Randomly mask ~15% of tokens
2. Predict masked tokens from context
3. Pre-train on large unlabeled fMRI datasets
```

**Benefits**:
- Learns meaningful brain representations
- Improves downstream task performance
- Reduces need for labeled data

## Implementation Guide

### Prerequisites
```bash
pip install torch torchvision transformers
pip install nibabel nilearn  # Neuroimaging
pip install accelerate  # Training efficiency
```

### Step-by-Step Implementation

#### Step 1: fMRI Preprocessing
```python
import nibabel as nib
import numpy as np
from nilearn import image, plotting

def preprocess_fmri(fmri_path, mask_path=None):
    """
    Preprocess fMRI data for TABLeT.
    
    Args:
        fmri_path: Path to 4D fMRI NIfTI file
        mask_path: Path to brain mask (optional)
    
    Returns:
        preprocessed: Preprocessed 4D array (x, y, z, t)
    """
    # Load fMRI
    img = nib.load(fmri_path)
    data = img.get_fdata()
    
    # Standard preprocessing steps
    # 1. Motion correction (if not done)
    # 2. Spatial smoothing
    # 3. Temporal filtering
    # 4. Confound regression (motion, CSF, WM)
    
    # Normalize
    data = (data - np.mean(data)) / (np.std(data) + 1e-8)
    
    return data

# Example
fmri_data = preprocess_fmri('sub-01_task-rest_bold.nii.gz')
print(f"fMRI shape: {fmri_data.shape}")  # (x, y, z, time)
```

#### Step 2: 2D Slice Extraction
```python
class FMRIVolumeSlicer:
    """Extract 2D axial slices from 3D fMRI volumes."""
    
    def __init__(self, target_shape=(256, 256)):
        self.target_shape = target_shape
    
    def extract_slices(self, volume_3d):
        """
        Extract 2D axial slices from 3D volume.
        
        Args:
            volume_3d: 3D numpy array (x, y, z)
        
        Returns:
            slices: List of 2D arrays
        """
        slices = []
        for z in range(volume_3d.shape[2]):
            slice_2d = volume_3d[:, :, z]
            
            # Resize to target shape
            from scipy.ndimage import zoom
            zoom_factors = (
                self.target_shape[0] / slice_2d.shape[0],
                self.target_shape[1] / slice_2d.shape[1]
            )
            slice_resized = zoom(slice_2d, zoom_factors, order=1)
            
            slices.append(slice_resized)
        
        return np.array(slices)  # (z, x, y)

# Example
slicer = FMRIVolumeSlicer(target_shape=(256, 256))
volume_3d = fmri_data[:, :, :, 0]  # First timepoint
slices = slicer.extract_slices(volume_3d)
print(f"Slices shape: {slices.shape}")  # (z, 256, 256)
```

#### Step 3: Autoencoder Tokenization
```python
import torch
from torchvision import transforms
from transformers import AutoencoderKL

class FMRITokenizer:
    """Tokenize fMRI using pre-trained 2D autoencoder."""
    
    def __init__(self, model_name="stabilityai/sd-vae-ft-ema"):
        """
        Initialize with pre-trained autoencoder.
        
        Args:
            model_name: HuggingFace model name for VAE
        """
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Load pre-trained autoencoder
        self.vae = AutoencoderKL.from_pretrained(model_name)
        self.vae = self.vae.to(self.device)
        self.vae.eval()
        
        # Image preprocessing
        self.transform = transforms.Compose([
            transforms.Normalize(mean=[0.5], std=[0.5])  # Adjust for single channel
        ])
    
    @torch.no_grad()
    def tokenize_volume(self, slices):
        """
        Tokenize 3D volume represented as 2D slices.
        
        Args:
            slices: Array of 2D slices (z, h, w)
        
        Returns:
            tokens: Token sequence (num_tokens, latent_dim)
        """
        tokens_list = []
        
        for slice_2d in slices:
            # Convert to tensor
            x = torch.from_numpy(slice_2d).float().unsqueeze(0).unsqueeze(0)  # (1, 1, h, w)
            x = x.to(self.device)
            
            # Repeat to 3 channels (for models expecting RGB)
            x = x.repeat(1, 3, 1, 1)
            
            # Encode to latent space
            latent = self.vae.encode(x).latent_dist.sample()
            # latent shape: (1, c, h', w') where h', w' are downsampled
            
            # Flatten spatial dimensions to get tokens
            b, c, h, w = latent.shape
            slice_tokens = latent.view(b, c, h * w).permute(0, 2, 1)  # (1, h*w, c)
            
            tokens_list.append(slice_tokens[0])  # (h*w, c)
        
        # Concatenate all slice tokens
        all_tokens = torch.cat(tokens_list, dim=0)  # (z*h*w, c)
        
        return all_tokens.cpu().numpy()

# Example
tokenizer = FMRITokenizer()
tokens = tokenizer.tokenize_volume(slices)
print(f"Token shape: {tokens.shape}")  # (num_tokens, latent_dim)
```

#### Step 4: TABLeT Model
```python
import torch.nn as nn
import math

class TABLeT(nn.Module):
    """
    TABLeT: Two-dimensionally Autoencoded Brain Latent Transformer
    """
    
    def __init__(
        self,
        token_dim=512,
        num_tokens=1024,
        num_layers=12,
        num_heads=8,
        hidden_dim=2048,
        dropout=0.1,
        num_classes=2,
        max_seq_len=4096
    ):
        super().__init__()
        
        self.token_dim = token_dim
        
        # Token embedding (if needed to project to model dim)
        self.token_projection = nn.Linear(token_dim, hidden_dim)
        
        # Positional encoding
        self.pos_encoding = PositionalEncoding(hidden_dim, max_seq_len)
        
        # Transformer encoder
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=hidden_dim,
            nhead=num_heads,
            dim_feedforward=hidden_dim * 4,
            dropout=dropout,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim // 2, num_classes)
        )
        
        # Pooling
        self.pool = nn.AdaptiveAvgPool1d(1)
    
    def forward(self, tokens, mask=None):
        """
        Args:
            tokens: (batch, seq_len, token_dim)
            mask: (batch, seq_len) attention mask
        
        Returns:
            logits: (batch, num_classes)
        """
        batch_size, seq_len, _ = tokens.shape
        
        # Project tokens
        x = self.token_projection(tokens)  # (batch, seq_len, hidden_dim)
        
        # Add positional encoding
        x = self.pos_encoding(x)
        
        # Transformer
        if mask is not None:
            # Convert boolean mask to attention mask
            attn_mask = mask.unsqueeze(1).unsqueeze(2)  # (batch, 1, 1, seq_len)
            x = self.transformer(x, src_key_padding_mask=~mask.bool())
        else:
            x = self.transformer(x)
        
        # Pool and classify
        x = x.transpose(1, 2)  # (batch, hidden_dim, seq_len)
        x = self.pool(x).squeeze(-1)  # (batch, hidden_dim)
        
        logits = self.classifier(x)
        
        return logits


class PositionalEncoding(nn.Module):
    """Sinusoidal positional encoding."""
    
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        self.register_buffer('pe', pe.unsqueeze(0))
    
    def forward(self, x):
        return x + self.pe[:, :x.size(1)]

# Example
model = TABLeT(token_dim=512, num_classes=10)
tokens_batch = torch.randn(2, 1024, 512)  # (batch, seq_len, token_dim)
logits = model(tokens_batch)
print(f"Output shape: {logits.shape}")  # (batch, num_classes)
```

#### Step 5: Masked Token Modeling Pre-training
```python
class MaskedTokenModeling(nn.Module):
    """Masked token modeling for self-supervised pre-training."""
    
    def __init__(self, tablet_model, mask_token_id=None):
        super().__init__()
        self.tablet = tablet_model
        self.mask_ratio = 0.15
        
        # Token prediction head
        self.token_predictor = nn.Linear(
            self.tablet.transformer.layers[0].linear1.in_features,
            self.tablet.token_dim
        )
    
    def forward(self, tokens):
        """
        Args:
            tokens: (batch, seq_len, token_dim)
        
        Returns:
            predicted_tokens: (batch, seq_len, token_dim)
            mask: (batch, seq_len) boolean mask
        """
        batch_size, seq_len, token_dim = tokens.shape
        
        # Create random mask
        mask = torch.rand(batch_size, seq_len) < self.mask_ratio
        
        # Replace masked tokens with learned mask token
        masked_tokens = tokens.clone()
        masked_tokens[mask] = 0  # Or use learned mask embedding
        
        # Forward through transformer
        x = self.tablet.token_projection(masked_tokens)
        x = self.tablet.pos_encoding(x)
        x = self.tablet.transformer(x)
        
        # Predict original tokens
        predicted_tokens = self.token_predictor(x)
        
        return predicted_tokens, mask
    
    def compute_loss(self, predicted_tokens, original_tokens, mask):
        """MSE loss on masked tokens."""
        loss = F.mse_loss(predicted_tokens[mask], original_tokens[mask])
        return loss

# Pre-training loop
def pretrain_tablet(model, dataloader, epochs=100, lr=1e-4):
    """Pre-train TABLeT with masked token modeling."""
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    
    mtm = MaskedTokenModeling(model)
    optimizer = torch.optim.AdamW(mtm.parameters(), lr=lr)
    
    for epoch in range(epochs):
        total_loss = 0
        
        for batch in dataloader:
            tokens = batch['tokens'].to(device)
            
            # Forward pass
            predicted, mask = mtm(tokens)
            loss = mtm.compute_loss(predicted, tokens, mask)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(dataloader):.4f}")
    
    return model
```

#### Step 6: Full Training Pipeline
```python
class TABLeTTrainer:
    """Complete training pipeline for TABLeT."""
    
    def __init__(self, config):
        self.config = config
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Initialize model
        self.model = TABLeT(**config['model'])
        self.model = self.model.to(self.device)
        
        # Initialize tokenizer
        self.tokenizer = FMRITokenizer(config.get('vae_model', 'stabilityai/sd-vae-ft-ema'))
        
        # Optimizer
        self.optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=config['training']['lr'],
            weight_decay=config['training']['weight_decay']
        )
        
        # Scheduler
        self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer,
            T_max=config['training']['epochs']
        )
    
    def train_epoch(self, dataloader):
        self.model.train()
        total_loss = 0
        correct = 0
        total = 0
        
        for batch in dataloader:
            tokens = batch['tokens'].to(self.device)
            labels = batch['label'].to(self.device)
            
            # Forward
            logits = self.model(tokens)
            loss = F.cross_entropy(logits, labels)
            
            # Backward
            self.optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
            self.optimizer.step()
            
            # Metrics
            total_loss += loss.item()
            _, predicted = logits.max(1)
            total += labels.size(0)
            correct += predicted.eq(labels).sum().item()
        
        accuracy = 100. * correct / total
        return total_loss / len(dataloader), accuracy
    
    def evaluate(self, dataloader):
        self.model.eval()
        total_loss = 0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for batch in dataloader:
                tokens = batch['tokens'].to(self.device)
                labels = batch['label'].to(self.device)
                
                logits = self.model(tokens)
                loss = F.cross_entropy(logits, labels)
                
                total_loss += loss.item()
                _, predicted = logits.max(1)
                total += labels.size(0)
                correct += predicted.eq(labels).sum().item()
        
        accuracy = 100. * correct / total
        return total_loss / len(dataloader), accuracy

# Configuration
config = {
    'model': {
        'token_dim': 512,
        'num_layers': 8,
        'num_heads': 8,
        'hidden_dim': 512,
        'num_classes': 2
    },
    'training': {
        'lr': 1e-4,
        'weight_decay': 0.01,
        'epochs': 50,
        'batch_size': 16
    }
}
```

## Applications

### Brain State Classification
- **Rest vs. Task**: Classify cognitive states
- **Disease Diagnosis**: ADHD, Alzheimer's, Depression
- **Brain-Computer Interfaces**: Decode intentions

### Long-Range Temporal Modeling
- **Dynamic Functional Connectivity**: Track network changes over long timescales
- **Learning and Memory**: Model neural plasticity
- **Sleep Staging**: Analyze sleep cycles

### Cross-Dataset Generalization
- **UK Biobank**: Population-scale imaging (40,000+ subjects)
- **Human Connectome Project**: High-resolution data
- **ADHD-200**: Clinical population

### Interpretable Brain Mapping
- **Token-to-Brain Mapping**: Map learned tokens to anatomical regions
- **Attention Visualization**: Understand what the model attends to
- **Clinical Biomarkers**: Identify disease-relevant patterns

## Pitfalls

### Technical Limitations
- **Slice Independence**: 2D processing may miss 3D relationships
- **VAE Artifacts**: Pre-trained VAE may introduce biases
- **Token Resolution**: Trade-off between compression and detail

### Domain-Specific Challenges
- **Head Motion**: Still requires good preprocessing
- **Scanner Differences**: Transfer across sites may degrade
- **Individual Variability**: Single model may not fit all

### Practical Considerations
- **Memory**: Still requires significant GPU memory for long sequences
- **Training Time**: Pre-training on large datasets is time-consuming
- **Interpretability**: Token representations less intuitive than voxels

## Related Skills
- brain-dit-fmri-foundation-model
- brain-foundation-model-inversion
- eeg-foundation-model-adapters
- meta-learning-in-context-brain-decoding
- transformer-prototype-readout

## References
- Kim et al. (2026). Can Natural Image Autoencoders Compactly Tokenize fMRI Volumes for Long-Range Dynamics Modeling? arXiv:2604.03619v1
- Van Den Oord et al. (2017). Neural Discrete Representation Learning. NeurIPS.
- Rombach et al. (2022). High-Resolution Image Synthesis with Latent Diffusion Models. CVPR.
- Dosovitskiy et al. (2021). An Image is Worth 16x16 Words. ICLR.
- UK Biobank: https://www.ukbiobank.ac.uk/
- Human Connectome Project: https://www.humanconnectome.org/
