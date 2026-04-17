# Implementation Patterns: Brain-DiT fMRI Foundation Model

## 1. Diffusion Transformer (DiT) Backbone for fMRI

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class DiTBlock(nn.Module):
    """Single DiT block with adaptive layer norm for conditioning."""
    def __init__(self, hidden_dim: int, num_heads: int, mlp_ratio: float = 4.0, dropout: float = 0.1):
        super().__init__()
        self.norm1 = nn.LayerNorm(hidden_dim, elementwise_affine=False)
        self.attn = nn.MultiheadAttention(hidden_dim, num_heads, dropout=dropout, batch_first=True)
        self.norm2 = nn.LayerNorm(hidden_dim, elementwise_affine=False)
        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim, int(hidden_dim * mlp_ratio)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(int(hidden_dim * mlp_ratio), hidden_dim),
        )
        # Adaptive layer norm parameters (conditioned on diffusion timestep + metadata)
        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(),
            nn.Linear(hidden_dim, 6 * hidden_dim),  # scale, shift for 2 norms
        )
        
    def forward(self, x: torch.Tensor, cond: torch.Tensor) -> torch.Tensor:
        """Forward pass with adaptive conditioning.
        
        Args:
            x: (B, L, D) input tokens (noisy fMRI latent)
            cond: (B, D) conditioning vector (timestep embedding + metadata)
        """
        shift_msa, scale_msa, gate_msa, shift_mlp, scale_mlp, gate_mlp = \
            self.adaLN_modulation(cond).chunk(6, dim=-1)
        
        # Self-attention with adaptive norm
        x = x + gate_msa.unsqueeze(1) * self.attn(
            self.norm1(x) * (1 + scale_msa.unsqueeze(1)) + shift_msa.unsqueeze(1),
            self.norm1(x) * (1 + scale_msa.unsqueeze(1)) + shift_msa.unsqueeze(1),
            self.norm1(x) * (1 + scale_msa.unsqueeze(1)) + shift_msa.unsqueeze(1),
        )[0]
        
        # MLP with adaptive norm
        x = x + gate_mlp.unsqueeze(1) * self.mlp(
            self.norm2(x) * (1 + scale_mlp.unsqueeze(1)) + shift_mlp.unsqueeze(1)
        )
        return x

class BrainDiT(nn.Module):
    """Diffusion Transformer for fMRI foundation model pretraining.
    
    Applies diffusion process to fMRI latent representations conditioned
    on metadata (brain state, subject info, task labels).
    """
    def __init__(self, 
                 n_regions: int,           # number of fMRI ROI/voxels
                 hidden_dim: int = 768,
                 num_heads: int = 12,
                 num_blocks: int = 12,
                 metadata_dim: int = 256):
        super().__init__()
        self.n_regions = n_regions
        self.hidden_dim = hidden_dim
        
        # Input projection: raw fMRI → latent
        self.input_proj = nn.Linear(1, hidden_dim)  # per-region feature
        self.pos_embed = nn.Parameter(torch.randn(1, n_regions, hidden_dim) * 0.02)
        
        # Diffusion blocks
        self.blocks = nn.ModuleList([
            DiTBlock(hidden_dim, num_heads) for _ in range(num_blocks)
        ])
        self.final_norm = nn.LayerNorm(hidden_dim)
        self.output_proj = nn.Linear(hidden_dim, 1)
        
        # Timestep + metadata embedding
        self.timestep_embed = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        self.metadata_embed = nn.Sequential(
            nn.Linear(metadata_dim, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        
    def forward(self, x_noisy: torch.Tensor, t: torch.Tensor, metadata: torch.Tensor) -> torch.Tensor:
        """Predict noise added to x at timestep t.
        
        Args:
            x_noisy: (B, N, 1) noisy fMRI latent (N = regions/voxels)
            t: (B, 1) diffusion timesteps (normalized 0..1)
            metadata: (B, metadata_dim) conditioning metadata
            
        Returns:
            noise_pred: (B, N, 1) predicted noise
        """
        # Embed inputs
        h = self.input_proj(x_noisy) + self.pos_embed
        
        # Combine timestep and metadata conditioning
        t_emb = self.timestep_embed(t)
        m_emb = self.metadata_embed(metadata)
        cond = t_emb + m_emb
        
        # Transformer blocks
        for block in self.blocks:
            h = block(h, cond)
        
        h = self.final_norm(h)
        noise_pred = self.output_proj(h)
        return noise_pred
```

## 2. Diffusion Process & Training Loop

```python
class fMRIDiffusionScheduler:
    """DDPM-style diffusion scheduler for fMRI latents."""
    def __init__(self, n_timesteps: int = 1000, beta_start: float = 1e-4, beta_end: float = 0.02):
        self.n_timesteps = n_timesteps
        self.betas = torch.linspace(beta_start, beta_end, n_timesteps)
        self.alphas = 1.0 - self.betas
        self.alpha_bars = torch.cumprod(self.alphas, dim=0)
    
    def add_noise(self, x: torch.Tensor, t: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        """Add noise to x at timestep t.
        
        Args:
            x: (B, N, 1) clean fMRI latent
            t: (B,) timesteps
            
        Returns:
            x_noisy: (B, N, 1) noisy latent
            noise: (B, N, 1) added noise
        """
        noise = torch.randn_like(x)
        alpha_bar = self.alpha_bars[t].view(-1, 1, 1)
        x_noisy = torch.sqrt(alpha_bar) * x + torch.sqrt(1 - alpha_bar) * noise
        return x_noisy, noise
    
    def sample(self, model: nn.Module, x_noisy: torch.Tensor, 
               metadata: torch.Tensor) -> torch.Tensor:
        """Reverse diffusion sampling loop."""
        x = x_noisy
        for t in reversed(range(self.n_timesteps)):
            t_tensor = torch.full((x.shape[0], 1), t / self.n_timesteps, device=x.device)
            noise_pred = model(x, t_tensor, metadata)
            
            alpha = self.alphas[t]
            alpha_bar = self.alpha_bars[t]
            beta = self.betas[t]
            
            x = (1 / torch.sqrt(alpha)) * (x - (beta / torch.sqrt(1 - alpha_bar)) * noise_pred)
            if t > 0:
                x += torch.sqrt(beta) * torch.randn_like(x)
        return x

def train_brain_dit(model: BrainDiT,
                    scheduler: fMRIDiffusionScheduler,
                    fmri_data: torch.Tensor,
                    metadata: torch.Tensor,
                    n_epochs: int = 100,
                    batch_size: int = 64,
                    lr: float = 1e-4) -> list[float]:
    """Train Brain-DiT with metadata-conditioned diffusion objective.
    
    Args:
        model: BrainDiT model
        scheduler: diffusion noise scheduler
        fmri_data: (N_sessions, N_regions, 1) fMRI sessions
        metadata: (N_sessions, metadata_dim) conditioning metadata
    """
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.05)
    losses = []
    
    for epoch in range(n_epochs):
        epoch_loss = 0.0
        n_batches = 0
        
        for batch_idx in range(0, len(fmri_data), batch_size):
            batch_fmri = fmri_data[batch_idx:batch_idx + batch_size]
            batch_meta = metadata[batch_idx:batch_idx + batch_size]
            B = batch_fmri.shape[0]
            
            # Sample random timesteps
            t = torch.randint(0, scheduler.n_timesteps, (B,), device=batch_fmri.device)
            
            # Add noise
            x_noisy, noise = scheduler.add_noise(batch_fmri, t)
            
            # Predict noise
            t_normalized = t.float().unsqueeze(-1) / scheduler.n_timesteps
            noise_pred = model(x_noisy, t_normalized, batch_meta)
            
            # MSE loss on noise prediction
            loss = F.mse_loss(noise_pred, noise)
            
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            
            epoch_loss += loss.item()
            n_batches += 1
        
        avg_loss = epoch_loss / n_batches
        losses.append(avg_loss)
        
    return losses
```

## 3. Metadata Conditioning

```python
class MetadataEncoder(nn.Module):
    """Encodes heterogeneous metadata into a unified conditioning vector.
    
    Handles:
    - Categorical brain state (resting, task, naturalistic, disease, sleep)
    - Continuous subject variables (age, sex encoding)
    - Dataset/source identifiers
    - Task-specific descriptors
    """
    def __init__(self, 
                 n_brain_states: int = 5,
                 n_datasets: int = 24,
                 metadata_hidden: int = 256,
                 output_dim: int = 768):
        super().__init__()
        
        # Categorical embeddings
        self.brain_state_emb = nn.Embedding(n_brain_states, 64)
        self.dataset_emb = nn.Embedding(n_datasets, 64)
        
        # Continuous variables projection
        self.continuous_proj = nn.Sequential(
            nn.Linear(2, 64),  # e.g., [age_normalized, sex_encoded]
            nn.LayerNorm(64),
            nn.GELU(),
        )
        
        # Task descriptor (optional free-form)
        self.task_proj = nn.Sequential(
            nn.Linear(128, 128),
            nn.GELU(),
        )
        
        # Fusion into unified conditioning vector
        self.fusion = nn.Sequential(
            nn.Linear(64 + 64 + 64 + 128, metadata_hidden),
            nn.GELU(),
            nn.Linear(metadata_hidden, output_dim),
        )
        
    def forward(self, brain_state: torch.Tensor, dataset: torch.Tensor,
                continuous: torch.Tensor, task_desc: torch.Tensor) -> torch.Tensor:
        """Encode metadata into conditioning vector.
        
        Args:
            brain_state: (B,) categorical brain state IDs
            dataset: (B,) dataset source IDs
            continuous: (B, 2) continuous subject variables
            task_desc: (B, 128) task-specific descriptor (optional)
        """
        bs_emb = self.brain_state_emb(brain_state)    # (B, 64)
        ds_emb = self.dataset_emb(dataset)             # (B, 64)
        cont_emb = self.continuous_proj(continuous)    # (B, 64)
        task_emb = self.task_proj(task_desc)           # (B, 128)
        
        fused = torch.cat([bs_emb, ds_emb, cont_emb, task_emb], dim=-1)
        return self.fusion(fused)  # (B, output_dim)
```

## 4. Multi-Scale Feature Extraction

```python
class MultiScalefMRIExtractor(nn.Module):
    """Extract multi-scale representations from pretrained Brain-DiT.
    
    Different downstream tasks prefer different scales:
    - Global semantics (ADNI disease classification)
    - Fine-grained local structure (age/sex prediction)
    """
    def __init__(self, pretrained_dit: BrainDiT, n_regions: int, hidden_dim: int = 768):
        super().__init__()
        self.dit = pretrained_dit
        # Freeze backbone
        for param in self.dit.parameters():
            param.requires_grad = False
            
        # Global pooling: mean over regions
        self.global_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        
        # Local features: per-region projections
        self.local_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.GELU(),
            nn.LayerNorm(hidden_dim // 2),
        )
        
    def forward(self, x: torch.Tensor, metadata: torch.Tensor) -> dict[str, torch.Tensor]:
        """Extract multi-scale features.
        
        Args:
            x: (B, N, 1) fMRI input
            metadata: (B, metadata_dim) conditioning
            
        Returns:
            dict with 'global' (B, D) and 'local' (B, N, D/2) features
        """
        # Use denoised representation at intermediate diffusion timestep
        t_mid = torch.full((x.shape[0], 1), 0.5, device=x.device)
        h = self.dit.input_proj(x) + self.dit.pos_embed
        
        t_emb = self.dit.timestep_embed(t_mid)
        m_emb = self.dit.metadata_embed(metadata)
        cond = t_emb + m_emb
        
        # Partial forward through some blocks for intermediate representation
        for block in self.dit.blocks[:6]:  # use first half for features
            h = block(h, cond)
        
        # Global features
        global_feat = self.global_head(h.mean(dim=1))  # (B, D)
        
        # Local features (per-region)
        local_feat = self.local_head(h)  # (B, N, D/2)
        
        return {'global': global_feat, 'local': local_feat}
```

## 5. Downstream Task Fine-tuning

```python
class fMRIClassifier(nn.Module):
    """Downstream classifier using Brain-DiT features.
    
    Example: ADNI disease classification (uses global features)
             or age/sex prediction (uses local features).
    """
    def __init__(self, extractor: MultiScalefMRIExtractor,
                 n_classes: int, use_global: bool = True,
                 hidden_dim: int = 768):
        super().__init__()
        self.extractor = extractor
        self.use_global = use_global
        
        input_dim = hidden_dim if use_global else hidden_dim // 2
        self.classifier = nn.Sequential(
            nn.Linear(input_dim, input_dim),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(input_dim, n_classes),
        )
        
    def forward(self, x: torch.Tensor, metadata: torch.Tensor) -> torch.Tensor:
        features = self.extractor(x, metadata)
        feat = features['global'] if self.use_global else features['local'].mean(dim=1)
        return self.classifier(feat)

def fine_tune_downstream(classifier: fMRIClassifier,
                         train_data: tuple[torch.Tensor, torch.Tensor],
                         val_data: tuple[torch.Tensor, torch.Tensor],
                         n_epochs: int = 50,
                         lr: float = 1e-4) -> dict:
    """Fine-tune downstream task on Brain-DiT features.
    
    Args:
        classifier: fMRIClassifier (global or local)
        train_data: (fmri, metadata, labels) tuples
        val_data: validation data
    """
    optimizer = torch.optim.AdamW(classifier.classifier.parameters(), lr=lr)
    best_val_acc = 0.0
    
    for epoch in range(n_epochs):
        # Training step
        classifier.train()
        fmri, meta, labels = train_data
        logits = classifier(fmri, meta)
        loss = F.cross_entropy(logits, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # Validation
        classifier.eval()
        with torch.no_grad():
            val_fmri, val_meta, val_labels = val_data
            val_logits = classifier(val_fmri, val_meta)
            val_preds = val_logits.argmax(dim=-1)
            val_acc = (val_preds == val_labels).float().mean().item()
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
    
    return {'best_val_acc': best_val_acc}
```

## 6. Pretraining Objective Comparison

```python
def compare_pretraining_objectives():
    """Key finding: Diffusion > Masked Reconstruction > Alignment
    
    This function demonstrates the three pretraining paradigms:
    
    1. DIFFUSION (Brain-DiT - BEST):
       - Objective: Predict noise ε added at timestep t to corrupted latent
       - Loss: MSE(noise_pred, noise)
       - Learns multi-scale generative understanding of fMRI manifold
       - Captures both fine-grained and global structure
    
    2. MASKED RECONSTRUCTION:
       - Objective: Reconstruct masked fMRI regions/timepoints from context
       - Loss: MSE(reconstruction, original) at masked positions
       - Learns local correlations but misses global semantics
    
    3. ALIGNMENT:
       - Objective: Align fMRI representations with behavioral/clinical targets
       - Loss: Contrastive or regression loss on paired data
       - Limited by label availability and task-specific bias
    """
    pass

# Diffusion pretraining loss (Brain-DiT)
def diffusion_loss(noise_pred: torch.Tensor, noise: torch.Tensor) -> torch.Tensor:
    return F.mse_loss(noise_pred, noise)

# Masked reconstruction loss (prior approaches)
def masked_reconstruction_loss(recon: torch.Tensor, original: torch.Tensor, 
                               mask: torch.Tensor) -> torch.Tensor:
    return F.mse_loss(recon[mask], original[mask])

# Alignment loss (prior approaches)
def alignment_loss(feat: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    return F.mse_loss(feat, target)
```
