---
name: adp-dit-brain-alzheimer-progression
description: "Text-Guided Diffusion Transformer (ADP-DiT) for generating longitudinal Alzheimer's disease brain MRI progression. Subject-specific synthesis with clinically interpretable control over follow-up time, enabling personalized disease trajectory modeling. 触发词: ADP-DiT, Alzheimer's disease progression, brain MRI synthesis, longitudinal brain imaging, diffusion transformer."
---

# ADP-DiT: Alzheimer's Disease Progression Brain Image Generation

Text-Guided Diffusion Transformer (ADP-DiT) methodology for subject-specific synthesis of follow-up brain MRI images to support Alzheimer's disease (AD) progression assessment with clinically interpretable control over disease trajectory.

## Core Concept

Alzheimer's disease progresses heterogeneously across individuals, motivating subject-specific synthesis of follow-up MRI scans. ADP-DiT extends Diffusion Transformers (DiT) - transformer-based diffusion models - for longitudinal AD MRI generation with clinically interpretable control over:
- Follow-up time prediction
- Disease progression stage
- Individual subject characteristics

## Key Features

| Feature | Description |
|---------|-------------|
| Architecture | Diffusion Transformer (DiT) |
| Modality | Structural MRI (sMRI) |
| Control | Text-guided (follow-up time) |
| Personalization | Subject-specific synthesis |
| Clinical Focus | Alzheimer's progression |
| Generation | Longitudinal (baseline → follow-up) |

## Architecture

### ADP-DiT Framework

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional, Tuple, List

class ADPDiT(nn.Module):
    """
    Alzheimer's Disease Progression Diffusion Transformer
    
    Generates follow-up brain MRI conditioned on:
    - Baseline MRI scan
    - Follow-up time (text description)
    - Subject ID (for personalization)
    """
    
    def __init__(
        self,
        img_size: int = 128,
        patch_size: int = 8,
        in_channels: int = 1,  # Grayscale MRI
        hidden_size: int = 768,
        depth: int = 12,
        num_heads: int = 12,
        mlp_ratio: float = 4.0,
        num_classes: int = 3,  # CN, MCI, AD
        max_timesteps: int = 1000
    ):
        super().__init__()
        
        self.img_size = img_size
        self.patch_size = patch_size
        self.in_channels = in_channels
        self.num_patches = (img_size // patch_size) ** 2
        
        # Patch embedding
        self.patch_embed = PatchEmbed(
            img_size=img_size,
            patch_size=patch_size,
            in_chans=in_channels,
            embed_dim=hidden_size
        )
        
        # Text encoder for follow-up time
        self.time_encoder = TimeTextEncoder(
            hidden_size=hidden_size,
            max_months=120  # Up to 10 years
        )
        
        # Subject embedding (for personalization)
        self.subject_embed = nn.Embedding(10000, hidden_size)  # Support 10k subjects
        
        # Positional embedding
        self.pos_embed = nn.Parameter(torch.zeros(1, self.num_patches, hidden_size))
        
        # Transformer blocks
        self.blocks = nn.ModuleList([
            DiTBlock(hidden_size, num_heads, mlp_ratio)
            for _ in range(depth)
        ])
        
        # Final layer
        self.final_layer = FinalLayer(hidden_size, patch_size, in_channels)
        
        # Initialize
        nn.init.normal_(self.pos_embed, std=0.02)
    
    def forward(
        self,
        x: torch.Tensor,
        t: torch.Tensor,
        time_text: List[str],
        subject_id: Optional[torch.Tensor] = None,
        baseline: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        """
        Forward pass.
        
        Args:
            x: Noised image patches (B, C, H, W)
            t: Diffusion timestep (B,)
            time_text: Text descriptions of follow-up time (e.g., "6 months", "2 years")
            subject_id: Subject IDs for personalization (B,)
            baseline: Baseline MRI scan (B, C, H, W)
        
        Returns:
            Predicted noise (B, C, H, W)
        """
        # Patchify input
        x = self.patch_embed(x)  # (B, N, D)
        
        # Add positional embedding
        x = x + self.pos_embed
        
        # Encode time text
        time_emb = self.time_encoder(time_text)  # (B, D)
        
        # Add subject embedding if provided
        if subject_id is not None:
            subj_emb = self.subject_embed(subject_id)  # (B, D)
            time_emb = time_emb + subj_emb
        
        # Broadcast time embedding to all patches
        time_emb = time_emb.unsqueeze(1).expand(-1, x.size(1), -1)
        x = x + time_emb
        
        # Process through transformer
        for block in self.blocks:
            x = block(x)
        
        # Final layer
        x = self.final_layer(x, time_emb[:, 0])
        
        # Unpatchify
        x = self.unpatchify(x)
        
        return x
    
    def unpatchify(self, x: torch.Tensor) -> torch.Tensor:
        """Convert patches back to image."""
        c = self.in_channels
        p = self.patch_size
        h = w = self.img_size // p
        
        x = x.reshape(shape=(x.shape[0], h, w, p, p, c))
        x = torch.einsum('nhwpqc->nchpwq', x)
        imgs = x.reshape(shape=(x.shape[0], c, h * p, w * p))
        return imgs
```

### Patch Embedding

```python
class PatchEmbed(nn.Module):
    """2D Image to Patch Embedding."""
    
    def __init__(
        self,
        img_size: int = 128,
        patch_size: int = 8,
        in_chans: int = 1,
        embed_dim: int = 768
    ):
        super().__init__()
        self.img_size = img_size
        self.patch_size = patch_size
        self.num_patches = (img_size // patch_size) ** 2
        
        self.proj = nn.Conv2d(
            in_chans, embed_dim,
            kernel_size=patch_size,
            stride=patch_size
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, C, H, W = x.shape
        x = self.proj(x).flatten(2).transpose(1, 2)  # (B, N, D)
        return x
```

### Time Text Encoder

```python
class TimeTextEncoder(nn.Module):
    """
    Encode follow-up time descriptions into embeddings.
    
    Examples:
    - "6 months"
    - "1 year"
    - "2 years 3 months"
    - "baseline" (0 months)
    """
    
    def __init__(self, hidden_size: int = 768, max_months: int = 120):
        super().__init__()
        self.hidden_size = hidden_size
        self.max_months = max_months
        
        # Vocabulary for time descriptions
        self.vocab = {
            '<PAD>': 0, '<UNK>': 1,
            'baseline': 2, 'month': 3, 'months': 4,
            'year': 5, 'years': 6, 'and': 7
        }
        for i in range(1, max_months + 1):
            self.vocab[str(i)] = len(self.vocab)
        
        self.vocab_size = len(self.vocab)
        
        # Embedding
        self.token_embed = nn.Embedding(self.vocab_size, hidden_size // 2)
        self.pos_embed = nn.Embedding(10, hidden_size // 2)  # Max 10 tokens
        
        # Encoder
        self.encoder = nn.LSTM(
            hidden_size, hidden_size,
            num_layers=2,
            batch_first=True,
            bidirectional=True
        )
        
        # Projection
        self.proj = nn.Sequential(
            nn.Linear(hidden_size * 2, hidden_size),
            nn.LayerNorm(hidden_size),
            nn.GELU(),
            nn.Linear(hidden_size, hidden_size)
        )
    
    def tokenize(self, text: str) -> List[int]:
        """Tokenize time description."""
        tokens = []
        parts = text.lower().replace(',', ' ').split()
        
        for part in parts:
            if part in self.vocab:
                tokens.append(self.vocab[part])
            elif part.isdigit():
                if int(part) <= self.max_months:
                    tokens.append(self.vocab[part])
                else:
                    tokens.append(self.vocab['<UNK>'])
            else:
                tokens.append(self.vocab['<UNK>'])
        
        return tokens
    
    def forward(self, texts: List[str]) -> torch.Tensor:
        """
        Encode batch of time descriptions.
        
        Args:
            texts: List of time descriptions
        
        Returns:
            Embeddings (B, D)
        """
        # Tokenize
        token_ids = [self.tokenize(text) for text in texts]
        max_len = max(len(t) for t in token_ids)
        
        # Pad
        padded = []
        for tokens in token_ids:
            padded.append(tokens + [self.vocab['<PAD>']] * (max_len - len(tokens)))
        
        token_tensor = torch.tensor(padded, device=self.token_embed.weight.device)
        
        # Embed
        token_emb = self.token_embed(token_tensor)
        pos_ids = torch.arange(max_len, device=token_tensor.device).unsqueeze(0).expand(len(texts), -1)
        pos_emb = self.pos_embed(pos_ids)
        
        x = torch.cat([token_emb, pos_emb], dim=-1)
        
        # Encode
        _, (h_n, _) = self.encoder(x)
        
        # Concatenate final hidden states
        h_n = torch.cat([h_n[-2], h_n[-1]], dim=-1)
        
        # Project
        out = self.proj(h_n)
        
        return out
```

### DiT Block

```python
class DiTBlock(nn.Module):
    """
    Diffusion Transformer block with adaptive layer norm.
    """
    
    def __init__(self, hidden_size: int, num_heads: int, mlp_ratio: float = 4.0):
        super().__init__()
        self.norm1 = nn.LayerNorm(hidden_size, elementwise_affine=False, eps=1e-6)
        self.attn = nn.MultiheadAttention(
            hidden_size, num_heads,
            batch_first=True
        )
        self.norm2 = nn.LayerNorm(hidden_size, elementwise_affine=False, eps=1e-6)
        
        mlp_hidden_dim = int(hidden_size * mlp_ratio)
        self.mlp = nn.Sequential(
            nn.Linear(hidden_size, mlp_hidden_dim),
            nn.GELU(),
            nn.Linear(mlp_hidden_dim, hidden_size)
        )
        
        # AdaLN modulation
        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(),
            nn.Linear(hidden_size, 6 * hidden_size)
        )
    
    def forward(self, x: torch.Tensor, c: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input (B, N, D)
            c: Conditioning embedding (B, D)
        
        Returns:
            Output (B, N, D)
        """
        # AdaLN parameters
        shift_msa, scale_msa, gate_msa, shift_mlp, scale_mlp, gate_mlp = \
            self.adaLN_modulation(c).chunk(6, dim=1)
        
        # Self-attention with AdaLN
        x_norm = self.modulate(self.norm1(x), shift_msa, scale_msa)
        attn_out, _ = self.attn(x_norm, x_norm, x_norm)
        x = x + gate_msa.unsqueeze(1) * attn_out
        
        # MLP with AdaLN
        x_norm = self.modulate(self.norm2(x), shift_mlp, scale_mlp)
        mlp_out = self.mlp(x_norm)
        x = x + gate_mlp.unsqueeze(1) * mlp_out
        
        return x
    
    def modulate(self, x: torch.Tensor, shift: torch.Tensor, scale: torch.Tensor) -> torch.Tensor:
        """Apply scale and shift for AdaLN."""
        return x * (1 + scale.unsqueeze(1)) + shift.unsqueeze(1)
```

### Final Layer

```python
class FinalLayer(nn.Module):
    """
    Final layer with adaptive layer norm.
    """
    
    def __init__(self, hidden_size: int, patch_size: int, out_channels: int):
        super().__init__()
        self.norm_final = nn.LayerNorm(hidden_size, elementwise_affine=False, eps=1e-6)
        self.linear = nn.Linear(hidden_size, patch_size * patch_size * out_channels)
        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(),
            nn.Linear(hidden_size, 2 * hidden_size)
        )
    
    def forward(self, x: torch.Tensor, c: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input (B, N, D)
            c: Conditioning (B, D)
        
        Returns:
            Output (B, N, patch_size^2 * C)
        """
        shift, scale = self.adaLN_modulation(c).chunk(2, dim=1)
        x = self.modulate(self.norm_final(x), shift, scale)
        x = self.linear(x)
        return x
    
    def modulate(self, x: torch.Tensor, shift: torch.Tensor, scale: torch.Tensor) -> torch.Tensor:
        return x * (1 + scale.unsqueeze(1)) + shift.unsqueeze(1)
```

## Training

### Diffusion Training

```python
def train_adp_dit(
    model: ADPDiT,
    dataloader: torch.utils.data.DataLoader,
    optimizer: torch.optim.Optimizer,
    num_epochs: int = 100,
    device: str = 'cuda'
):
    """
    Train ADP-DiT model.
    
    Args:
        model: ADP-DiT model
        dataloader: Training data loader
        optimizer: Optimizer
        num_epochs: Number of epochs
        device: Device to train on
    """
    model.to(device)
    model.train()
    
    # Noise schedule
    noise_scheduler = DDPMScheduler(num_train_timesteps=1000)
    
    for epoch in range(num_epochs):
        total_loss = 0
        
        for batch_idx, batch in enumerate(dataloader):
            baseline = batch['baseline'].to(device)
            followup = batch['followup'].to(device)
            time_text = batch['time_text']  # List of strings
            subject_id = batch['subject_id'].to(device)
            
            # Sample noise
            noise = torch.randn_like(followup)
            
            # Sample timesteps
            timesteps = torch.randint(
                0, noise_scheduler.config.num_train_timesteps,
                (followup.size(0),), device=device
            ).long()
            
            # Add noise
            noisy_images = noise_scheduler.add_noise(followup, noise, timesteps)
            
            # Predict noise
            predicted_noise = model(
                noisy_images,
                timesteps,
                time_text,
                subject_id=subject_id,
                baseline=baseline
            )
            
            # Compute loss
            loss = F.mse_loss(predicted_noise, noise)
            
            # Backward
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        avg_loss = total_loss / len(dataloader)
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {avg_loss:.4f}")
    
    return model
```

### Loss Functions

```python
class ADP_DiT_Loss(nn.Module):
    """
    Combined loss for ADP-DiT training.
    """
    
    def __init__(self, lambda_recon: float = 1.0, lambda_perceptual: float = 0.1):
        super().__init__()
        self.lambda_recon = lambda_recon
        self.lambda_perceptual = lambda_perceptual
        
        # Perceptual loss using pre-trained brain MRI encoder
        self.perceptual_encoder = self._load_pretrained_encoder()
    
    def forward(
        self,
        pred: torch.Tensor,
        target: torch.Tensor,
        mask: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        """
        Compute combined loss.
        
        Args:
            pred: Predicted image
            target: Target image
            mask: Brain mask (optional)
        
        Returns:
            Combined loss
        """
        # Reconstruction loss (MSE)
        if mask is not None:
            recon_loss = F.mse_loss(pred * mask, target * mask)
        else:
            recon_loss = F.mse_loss(pred, target)
        
        # Perceptual loss
        pred_features = self.perceptual_encoder(pred)
        target_features = self.perceptual_encoder(target)
        perceptual_loss = F.mse_loss(pred_features, target_features)
        
        # Combine
        total_loss = self.lambda_recon * recon_loss + \
                     self.lambda_perceptual * perceptual_loss
        
        return total_loss
    
    def _load_pretrained_encoder(self) -> nn.Module:
        """Load pre-trained brain MRI encoder for perceptual loss."""
        # Load pre-trained model (e.g., from previous stage)
        encoder = BrainMRIEncoder()
        encoder.eval()
        for param in encoder.parameters():
            param.requires_grad = False
        return encoder
```

## Inference

### Progressive Generation

```python
def generate_progression(
    model: ADPDiT,
    baseline: torch.Tensor,
    subject_id: int,
    time_points: List[str],
    num_inference_steps: int = 50,
    device: str = 'cuda'
) -> List[torch.Tensor]:
    """
    Generate disease progression at multiple time points.
    
    Args:
        model: Trained ADP-DiT model
        baseline: Baseline MRI scan
        subject_id: Subject ID for personalization
        time_points: List of time descriptions (e.g., ["6 months", "1 year", "2 years"])
        num_inference_steps: Number of diffusion steps
        device: Device
    
    Returns:
        List of generated follow-up images
    """
    model.eval()
    model.to(device)
    
    # Noise scheduler
    noise_scheduler = DDPMScheduler(num_train_timesteps=1000)
    noise_scheduler.set_timesteps(num_inference_steps)
    
    generated_images = []
    
    for time_text in time_points:
        # Start from noise or baseline
        if len(generated_images) > 0:
            # Start from previous prediction (progressive generation)
            latents = generated_images[-1].clone()
        else:
            # Start from random noise
            latents = torch.randn_like(baseline)
        
        latents = latents.to(device)
        baseline_batch = baseline.unsqueeze(0).to(device)
        subject_tensor = torch.tensor([subject_id], device=device)
        
        # Denoising loop
        for t in noise_scheduler.timesteps:
            with torch.no_grad():
                # Predict noise
                noise_pred = model(
                    latents,
                    t.unsqueeze(0),
                    [time_text],
                    subject_id=subject_tensor,
                    baseline=baseline_batch
                )
                
                # Compute previous sample
                latents = noise_scheduler.step(noise_pred, t, latents).prev_sample
        
        generated_images.append(latents.squeeze(0).cpu())
    
    return generated_images
```

### Subject-Specific Fine-tuning

```python
def personalize_model(
    model: ADPDiT,
    subject_data: torch.utils.data.DataLoader,
    num_steps: int = 100,
    lr: float = 1e-4,
    device: str = 'cuda'
) -> ADPDiT:
    """
    Fine-tune model for specific subject.
    
    Args:
        model: Base ADP-DiT model
        subject_data: Subject-specific data
        num_steps: Number of fine-tuning steps
        lr: Learning rate
        device: Device
    
    Returns:
        Personalized model
    """
    model.to(device)
    model.train()
    
    # Only optimize subject embedding
    optimizer = torch.optim.Adam(
        [model.subject_embed.weight],
        lr=lr
    )
    
    for step in range(num_steps):
        for batch in subject_data:
            # Standard training loop
            pass
    
    return model
```

## Evaluation

### Clinical Metrics

```python
def evaluate_progression_model(
    model: ADPDiT,
    test_dataloader: torch.utils.data.DataLoader,
    device: str = 'cuda'
) -> dict:
    """
    Evaluate model on clinical metrics.
    
    Metrics:
    - Image quality (PSNR, SSIM)
    - Structural similarity to real follow-up
    - Clinical score prediction accuracy
    - Longitudinal consistency
    """
    from skimage.metrics import peak_signal_noise_ratio, structural_similarity
    
    metrics = {
        'psnr': [],
        'ssim': [],
        'ventricle_volume_error': [],
        'hippocampus_volume_error': []
    }
    
    model.eval()
    model.to(device)
    
    with torch.no_grad():
        for batch in test_dataloader:
            baseline = batch['baseline'].to(device)
            real_followup = batch['followup'].to(device)
            time_text = batch['time_text']
            subject_id = batch['subject_id'].to(device)
            
            # Generate
            generated = generate_progression(
                model, baseline, subject_id[0].item(),
                time_text, device=device
            )[0]
            
            # Compute image metrics
            psnr = peak_signal_noise_ratio(
                real_followup[0].cpu().numpy(),
                generated.numpy()
            )
            ssim = structural_similarity(
                real_followup[0].cpu().numpy(),
                generated.numpy()
            )
            
            metrics['psnr'].append(psnr)
            metrics['ssim'].append(ssim)
            
            # Compute structural metrics
            # (ventricle and hippocampus volume errors)
            
    # Aggregate
    results = {k: np.mean(v) for k, v in metrics.items()}
    
    return results
```

## Applications

### 1. Disease Progression Prediction
- Generate expected follow-up scans
- Identify deviation from typical progression
- Early detection of rapid progression

### 2. Treatment Planning
- Simulate treatment effects
- Compare expected vs. actual progression
- Adjust treatment strategies

### 3. Clinical Trial Design
- Identify homogeneous subgroups
- Predict required sample sizes
- Optimize follow-up intervals

### 4. Synthetic Data Generation
- Augment training datasets
- Preserve privacy while sharing
- Balance class distributions

## Dataset Preparation

```python
class LongitudinalBrainDataset(torch.utils.data.Dataset):
    """
    Dataset for longitudinal brain MRI.
    
    Expects data organized as:
    - subject_id/
      - baseline.nii.gz
      - followup_6mo.nii.gz
      - followup_1yr.nii.gz
      - ...
    """
    
    def __init__(self, data_dir: str, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        
        # Load subject list
        self.subjects = self._load_subjects()
        self.samples = self._create_samples()
    
    def _load_subjects(self) -> List[str]:
        """Load list of subject directories."""
        import os
        return [d for d in os.listdir(self.data_dir)
                if os.path.isdir(os.path.join(self.data_dir, d))]
    
    def _create_samples(self) -> List[dict]:
        """Create list of (baseline, followup, time) tuples."""
        samples = []
        
        for subject_id in self.subjects:
            subject_dir = os.path.join(self.data_dir, subject_id)
            
            # Find baseline
            baseline_path = os.path.join(subject_dir, 'baseline.nii.gz')
            
            # Find follow-ups
            import glob
            followups = glob.glob(os.path.join(subject_dir, 'followup_*.nii.gz'))
            
            for followup_path in followups:
                # Extract time from filename
                time_str = os.path.basename(followup_path).replace('followup_', '').replace('.nii.gz', '')
                time_text = self._parse_time(time_str)
                
                samples.append({
                    'subject_id': subject_id,
                    'baseline': baseline_path,
                    'followup': followup_path,
                    'time_text': time_text
                })
        
        return samples
    
    def _parse_time(self, time_str: str) -> str:
        """Parse time string to description."""
        # Convert "6mo" to "6 months"
        # Convert "1yr" to "1 year"
        # etc.
        if 'mo' in time_str:
            months = int(time_str.replace('mo', ''))
            return f"{months} month{'s' if months > 1 else ''}"
        elif 'yr' in time_str:
            years = int(time_str.replace('yr', ''))
            return f"{years} year{'s' if years > 1 else ''}"
        return time_str
```

## References

- Lee, J., Baek, G., & Jang, I. (2026). "ADP-DiT: Text-Guided Diffusion Transformer for Brain Image Generation in Alzheimer's Disease Progression"
- Peebles & Xie (2023): Scalable Diffusion Models with Transformers
- Ho et al. (2020): Denoising Diffusion Probabilistic Models
- Jack et al. (2013): Tracking pathophysiological processes in Alzheimer's disease

## Related Skills

- **brain-mri-foundation-models**: Self-supervised learning for brain MRI
- **brain-dit-fmri-foundation-model**: Brain-DiT foundation model
- **meta-learning-in-context-brain-decoding**: Cross-subject brain decoding
- **neural-encoding-evaluation-ground-truth**: Neural encoding model evaluation