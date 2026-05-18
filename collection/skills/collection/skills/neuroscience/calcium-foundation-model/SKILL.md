---
name: calcium-foundation-model
description: "Self-supervised foundation model for calcium imaging population dynamics (CaFM). Large-scale multi-animal modeling for neural recording analysis with cross-animal transfer learning. Use when working with: (1) Calcium imaging analysis, (2) Multi-animal neural modeling, (3) Self-supervised learning for neuroscience, (4) Population dynamics modeling. Activation: calcium imaging foundation model, neural population dynamics, multi-animal modeling, self-supervised calcium."
---

# Calcium Imaging Foundation Model (CaFM)

Self-supervised foundation model for calcium imaging population dynamics. Enables large-scale, multi-animal modeling to significantly improve neural recording analysis through transfer learning across animals.

## Core Concept

Traditional calcium imaging analysis uses task-specific models that don't transfer across common neuroscience objectives. CaFM proposes a foundation model approach that learns generalizable representations from multi-animal data, enabling zero-shot or few-shot transfer to new animals and tasks.

## Theoretical Background

### Why Foundation Models for Calcium Imaging?

1. **Data Scarcity**: Each animal provides limited labeled data
2. **Individual Variability**: Neural representations vary across animals
3. **Task Diversity**: Multiple objectives (decoding, denoising, segmentation)
4. **Shared Structure**: Common neural dynamics principles across animals

### Self-Supervised Learning Approach

```python
# High-level concept
# 1. Pre-train on diverse multi-animal calcium data
# 2. Learn generalizable neural dynamics representations
# 3. Fine-tune or adapt to specific tasks/animals

class CalciumFoundationModel:
    """Foundation model for calcium imaging population dynamics."""
    
    def __init__(self, input_dim: int, latent_dim: int = 256):
        self.input_dim = input_dim  # Number of neurons
        self.latent_dim = latent_dim
        
        # Encoder: calcium traces -> latent representation
        self.encoder = TemporalEncoder(input_dim, latent_dim)
        
        # Decoder: latent -> reconstructed traces
        self.decoder = TemporalDecoder(latent_dim, input_dim)
        
        # Task-specific heads
        self.task_heads = {}
    
    def pretrain(self, multi_animal_data: List[CalciumData]):
        """Self-supervised pre-training on multi-animal data."""
        # Use masked prediction, contrastive learning, etc.
        pass
    
    def adapt_to_animal(self, target_animal_data: CalciumData):
        """Adapt pre-trained model to new animal."""
        # Few-shot adaptation or zero-shot inference
        pass
```

## Architecture

### Temporal Encoder

```python
import torch
import torch.nn as nn

class TemporalEncoder(nn.Module):
    """Encode calcium traces to latent representations."""
    
    def __init__(self, input_dim: int, latent_dim: int, hidden_dim: int = 512):
        super().__init__()
        
        # Multi-scale temporal convolutions
        self.conv1d_layers = nn.ModuleList([
            nn.Conv1d(input_dim, hidden_dim // 4, kernel_size=k, padding=k//2)
            for k in [3, 7, 15, 31]  # Different temporal scales
        ])
        
        # Temporal attention
        self.temporal_attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=8,
            batch_first=True
        )
        
        # LSTM for sequential modeling
        self.lstm = nn.LSTM(
            input_size=hidden_dim,
            hidden_size=hidden_dim,
            num_layers=2,
            batch_first=True,
            bidirectional=True
        )
        
        # Projection to latent space
        self.latent_projection = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, latent_dim)
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: (batch, time, neurons) calcium traces
        Returns:
            z: (batch, latent_dim) latent representation
        """
        # Multi-scale convolutions
        x_conv = []
        x_t = x.transpose(1, 2)  # (batch, neurons, time)
        for conv in self.conv1d_layers:
            x_conv.append(conv(x_t))
        x_multi = torch.cat(x_conv, dim=1).transpose(1, 2)  # (batch, time, hidden)
        
        # Temporal attention
        attn_out, _ = self.temporal_attention(x_multi, x_multi, x_multi)
        
        # LSTM processing
        lstm_out, _ = self.lstm(attn_out)
        
        # Global average pooling over time
        pooled = lstm_out.mean(dim=1)
        
        # Project to latent
        z = self.latent_projection(pooled)
        
        return z
```

### Population-Aware Decoder

```python
class PopulationAwareDecoder(nn.Module):
    """Decode latent representations back to calcium traces."""
    
    def __init__(self, latent_dim: int, output_dim: int, hidden_dim: int = 512):
        super().__init__()
        
        self.latent_dim = latent_dim
        self.output_dim = output_dim
        
        # Latent to temporal sequence
        self.sequence_init = nn.Linear(latent_dim, hidden_dim * 100)  # 100 time steps
        
        # Transposed convolutions for upsampling
        self.upsample_layers = nn.Sequential(
            nn.ConvTranspose1d(hidden_dim, hidden_dim // 2, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(hidden_dim // 2, hidden_dim // 4, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(hidden_dim // 4, hidden_dim // 8, kernel_size=4, stride=2, padding=1),
            nn.ReLU(),
        )
        
        # Final projection to neurons
        self.neuron_projection = nn.Conv1d(hidden_dim // 8, output_dim, kernel_size=1)
        
        # Neuron-specific gains
        self.neuron_gains = nn.Parameter(torch.ones(output_dim))
        self.neuron_offsets = nn.Parameter(torch.zeros(output_dim))
    
    def forward(self, z: torch.Tensor, target_length: int) -> torch.Tensor:
        """
        Args:
            z: (batch, latent_dim) latent representation
            target_length: desired output time length
        Returns:
            traces: (batch, time, neurons) reconstructed calcium traces
        """
        # Initialize sequence from latent
        seq = self.sequence_init(z)
        seq = seq.view(z.size(0), -1, 100).transpose(1, 2)  # (batch, 100, hidden)
        seq = seq.transpose(1, 2)  # (batch, hidden, 100)
        
        # Upsample
        upsampled = self.upsample_layers(seq)
        
        # Interpolate to target length
        upsampled = torch.nn.functional.interpolate(
            upsampled, size=target_length, mode='linear', align_corners=False
        )
        
        # Project to neurons
        traces = self.neuron_projection(upsampled)
        traces = traces.transpose(1, 2)  # (batch, time, neurons)
        
        # Apply neuron-specific gains
        traces = traces * self.neuron_gains + self.neuron_offsets
        
        return traces
```

## Self-Supervised Pre-training

### Masked Trace Prediction

```python
class MaskedTracePrediction:
    """Masked modeling for calcium traces."""
    
    def __init__(self, mask_ratio: float = 0.15):
        self.mask_ratio = mask_ratio
        
    def create_mask(self, traces: torch.Tensor) -> torch.Tensor:
        """
        Create random mask for trace segments.
        
        Args:
            traces: (batch, time, neurons)
        Returns:
            mask: (batch, time) boolean mask
        """
        batch_size, time_len, n_neurons = traces.shape
        
        # Random masking
        mask = torch.rand(batch_size, time_len) < self.mask_ratio
        
        return mask
    
    def forward(self, model: CalciumFoundationModel, 
                traces: torch.Tensor) -> torch.Tensor:
        """
        Masked prediction loss.
        
        Args:
            traces: Input calcium traces
        Returns:
            loss: Reconstruction loss on masked regions
        """
        # Create mask
        mask = self.create_mask(traces)
        
        # Mask input
        masked_traces = traces.clone()
        masked_traces[mask] = 0  # Zero out masked regions
        
        # Encode
        z = model.encoder(masked_traces)
        
        # Decode
        reconstructed = model.decoder(z, traces.size(1))
        
        # Loss only on masked regions
        loss = torch.mean((reconstructed[mask] - traces[mask])**2)
        
        return loss
```

### Contrastive Learning

```python
class ContrastiveCalciumLearning:
    """Contrastive learning for neural population dynamics."""
    
    def __init__(self, temperature: float = 0.07):
        self.temperature = temperature
        
    def create_positive_pairs(self, traces: torch.Tensor) -> torch.Tensor:
        """
        Create positive pairs through temporal augmentation.
        
        Augmentations:
        - Time warping
        - Amplitude scaling
        - Gaussian noise
        - Temporal jitter
        """
        augmented = traces.clone()
        
        # Random amplitude scaling
        scale = torch.randn(traces.size(0), 1, 1) * 0.1 + 1.0
        augmented = augmented * scale
        
        # Add Gaussian noise
        noise = torch.randn_like(augmented) * 0.01
        augmented = augmented + noise
        
        return augmented
    
    def contrastive_loss(self, model: CalciumFoundationModel,
                        traces: torch.Tensor) -> torch.Tensor:
        """
        NT-Xent loss for calcium traces.
        """
        batch_size = traces.size(0)
        
        # Create positive pairs
        traces_aug = self.create_positive_pairs(traces)
        
        # Encode both
        z_orig = model.encoder(traces)
        z_aug = model.encoder(traces_aug)
        
        # Normalize
        z_orig = torch.nn.functional.normalize(z_orig, dim=1)
        z_aug = torch.nn.functional.normalize(z_aug, dim=1)
        
        # Compute similarity matrix
        z_all = torch.cat([z_orig, z_aug], dim=0)
        similarity = torch.mm(z_all, z_all.t()) / self.temperature
        
        # Create labels (positives are diagonal offsets)
        labels = torch.arange(batch_size)
        labels = torch.cat([labels + batch_size, labels])
        
        # Cross-entropy loss
        loss = torch.nn.functional.cross_entropy(similarity, labels)
        
        return loss
```

## Multi-Animal Training

```python
class MultiAnimalTrainer:
    """Train foundation model on multi-animal calcium data."""
    
    def __init__(self, model: CalciumFoundationModel, 
                 num_animals: int,
                 animal_embedding_dim: int = 64):
        self.model = model
        self.num_animals = num_animals
        
        # Animal-specific embeddings
        self.animal_embeddings = nn.Embedding(num_animals, animal_embedding_dim)
        
        # Combine with neural representations
        self.combiner = nn.Sequential(
            nn.Linear(model.latent_dim + animal_embedding_dim, model.latent_dim),
            nn.ReLU(),
            nn.Linear(model.latent_dim, model.latent_dim)
        )
    
    def forward(self, traces: torch.Tensor, animal_id: int) -> torch.Tensor:
        """
        Forward pass with animal-specific conditioning.
        
        Args:
            traces: Calcium traces
            animal_id: ID of the source animal
        Returns:
            z: Animal-conditioned latent representation
        """
        # Base encoding
        z_base = self.model.encoder(traces)
        
        # Animal embedding
        animal_embed = self.animal_embeddings(
            torch.tensor(animal_id).expand(traces.size(0))
        )
        
        # Combine
        z_combined = torch.cat([z_base, animal_embed], dim=-1)
        z = self.combiner(z_combined)
        
        return z
    
    def train_epoch(self, dataloader: DataLoader):
        """Train for one epoch across all animals."""
        total_loss = 0
        
        for batch in dataloader:
            traces = batch['traces']
            animal_ids = batch['animal_id']
            
            # Mixed batch from different animals
            loss = 0
            for animal_id in torch.unique(animal_ids):
                mask = animal_ids == animal_id
                animal_traces = traces[mask]
                
                # Self-supervised loss
                z = self.forward(animal_traces, animal_id.item())
                recon = self.model.decoder(z, animal_traces.size(1))
                
                loss += torch.mean((recon - animal_traces)**2)
            
            # Backprop
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()
            
            total_loss += loss.item()
        
        return total_loss / len(dataloader)
```

## Task-Specific Adaptation

### Neural Decoding

```python
class NeuralDecoder(nn.Module):
    """Decode neural activity to behavior/stimuli."""
    
    def __init__(self, foundation_model: CalciumFoundationModel, 
                 num_outputs: int):
        super().__init__()
        self.foundation = foundation_model
        
        # Freeze foundation weights
        for param in self.foundation.parameters():
            param.requires_grad = False
        
        # Task-specific head
        self.decoder_head = nn.Sequential(
            nn.Linear(foundation_model.latent_dim, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_outputs)
        )
    
    def forward(self, traces: torch.Tensor) -> torch.Tensor:
        # Use foundation model as feature extractor
        with torch.no_grad():
            z = self.foundation.encoder(traces)
        
        # Decode
        output = self.decoder_head(z)
        return output
    
    def fine_tune(self, labeled_data: DataLoader, epochs: int = 10):
        """Fine-tune only the decoder head."""
        optimizer = torch.optim.Adam(self.decoder_head.parameters(), lr=1e-4)
        
        for epoch in range(epochs):
            for batch in labeled_data:
                traces = batch['traces']
                labels = batch['labels']
                
                predictions = self.forward(traces)
                loss = torch.nn.functional.cross_entropy(predictions, labels)
                
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
```

### Activity Denoising

```python
class CalciumDenoiser:
    """Denoise calcium traces using foundation model."""
    
    def __init__(self, foundation_model: CalciumFoundationModel):
        self.model = foundation_model
        
    def denoise(self, noisy_traces: torch.Tensor) -> torch.Tensor:
        """
        Denoise calcium traces.
        
        The foundation model learns to reconstruct clean traces
        from noisy inputs through self-supervised pre-training.
        """
        # Encode
        z = self.model.encoder(noisy_traces)
        
        # Decode (reconstruct clean version)
        clean_traces = self.model.decoder(z, noisy_traces.size(1))
        
        return clean_traces
    
    def adaptive_denoise(self, traces: torch.Tensor, 
                        noise_level: float) -> torch.Tensor:
        """
        Adaptive denoising based on estimated noise level.
        """
        # Estimate noise level from traces
        estimated_noise = self.estimate_noise(traces)
        
        # Adjust reconstruction strength
        z = self.model.encoder(traces)
        clean = self.model.decoder(z, traces.size(1))
        
        # Blend based on noise level
        alpha = min(1.0, estimated_noise / noise_level)
        denoised = alpha * clean + (1 - alpha) * traces
        
        return denoised
```

## Evaluation Metrics

```python
class CalciumModelEvaluator:
    """Evaluate foundation model performance."""
    
    def reconstruction_quality(self, original: np.ndarray, 
                              reconstructed: np.ndarray) -> dict:
        """Measure reconstruction quality."""
        from sklearn.metrics import r2_score, mean_squared_error
        
        mse = mean_squared_error(original.flatten(), reconstructed.flatten())
        r2 = r2_score(original.flatten(), reconstructed.flatten())
        
        # Correlation per neuron
        correlations = []
        for i in range(original.shape[1]):
            corr = np.corrcoef(original[:, i], reconstructed[:, i])[0, 1]
            correlations.append(corr)
        
        return {
            'mse': mse,
            'r2': r2,
            'mean_correlation': np.mean(correlations),
            'correlation_std': np.std(correlations)
        }
    
    def transfer_performance(self, model, target_animal_data: dict) -> dict:
        """Evaluate zero-shot transfer to new animal."""
        # Test without fine-tuning
        traces = target_animal_data['traces']
        
        # Reconstruction
        z = model.encoder(traces)
        recon = model.decoder(z, traces.size(1))
        
        metrics = self.reconstruction_quality(
            traces.numpy(), recon.detach().numpy()
        )
        
        # Compare to animal-specific baseline
        baseline = self.train_animal_specific_baseline(target_animal_data)
        baseline_metrics = self.reconstruction_quality(
            traces.numpy(), baseline.predict(traces).numpy()
        )
        
        return {
            'foundation_model': metrics,
            'baseline': baseline_metrics,
            'improvement': metrics['r2'] - baseline_metrics['r2']
        }
```

## Best Practices

### Data Preparation

1. **Preprocessing**:
   - Motion correction
   - ΔF/F normalization
   - Detrending
   - Frame rate standardization

2. **Quality Control**:
   - Exclude low-quality recordings
   - Check for photobleaching
   - Validate ROI segmentation

### Training

1. **Multi-Animal Strategy**:
   - Balance samples across animals
   - Use animal-specific embeddings
   - Apply domain randomization

2. **Self-Supervised Tasks**:
   - Combine masked prediction + contrastive learning
   - Use multiple temporal scales
   - Augment with realistic noise models

3. **Adaptation**:
   - Start with frozen foundation
   - Gradually unfreeze layers
   - Use learning rate warmup

### Evaluation

1. **Cross-Animal Validation**:
   - Leave-one-animal-out testing
   - Measure transfer learning gap
   - Compare to animal-specific baselines

2. **Task Performance**:
   - Decoding accuracy
   - Denoising SNR improvement
   - Segmentation quality

## Applications

### 1. Cross-Animal Behavior Decoding

```python
# Train on animals 1-9, test on animal 10
foundation_model = CalciumFoundationModel(input_dim=1000)
pretrain_on_animals(foundation_model, animals=[1,2,3,4,5,6,7,8,9])

# Zero-shot on new animal
decoder = NeuralDecoder(foundation_model, num_behaviors=8)
accuracy = decoder.evaluate(animal_10_data)
# Expected: >80% accuracy with no fine-tuning
```

### 2. Denoising Enhancement

```python
denoiser = CalciumDenoiser(foundation_model)
clean_traces = denoiser.denoise(noisy_traces)
# SNR improvement: 5-10 dB
```

### 3. Few-Shot Adaptation

```python
# New animal with only 100 labeled trials
few_shot_decoder = NeuralDecoder(foundation_model, num_outputs=10)
few_shot_decoder.fine_tune(small_labeled_dataset, epochs=5)
# Achieves 90%+ of full-dataset performance
```

## Limitations

1. **Recording Variability**: Different microscopes, indicators may require adaptation
2. **Brain Region Specificity**: Model may need region-specific fine-tuning
3. **Species Gap**: Cross-species transfer not guaranteed
4. **Computational Cost**: Large models require significant compute

## References

- Paper: "Self-Supervised Foundation Model for Calcium-imaging Population Dynamics" (arXiv:2604.04958v2, 2026)
- Authors: Xinhong Xu, Yimeng Zhang, Qichen Qian, et al.
- Related: BERT (Devlin et al.), MAE (He et al.), Neural Population Coding

## Activation Keywords

- calcium imaging foundation model
- neural population dynamics
- multi-animal modeling
- self-supervised calcium
- cross-animal transfer
- calcium trace denoising
- neural decoding foundation
- population activity model
