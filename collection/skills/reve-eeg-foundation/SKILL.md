---
name: reve-eeg-foundation
description: "REVE (Representation for EEG with Versatile Embeddings) - EEG foundation model trained on 60,000 hours from 25,000 subjects with novel 4D positional encoding for arbitrary electrode configurations. Achieves SOTA on 10 downstream tasks. Activation triggers: EEG foundation model, REVE, versatile embeddings, 4D positional encoding, cross-dataset EEG, brain-computer interface."
---

# REVE: Foundation Model for EEG

> A foundation model for EEG that adapts to any setup with large-scale pretraining on 25,000 subjects, introducing novel 4D positional encoding for flexible electrode configuration handling.

## Metadata
- **Source**: arXiv:2510.21585
- **Authors**: Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent Gripon, Karim Jerbi, Giulia Lioi
- **Published**: 2025-10
- **Institution**: IMT Atlantique, Université de Montréal, Mila, UNIQUE
- **Code & Weights**: https://github.com/brain-bzh/reve

## Core Methodology

### Key Innovation

REVE addresses the fundamental challenge of EEG data heterogeneity through three core contributions:

1. **4D Positional Encoding**: Novel encoding scheme supporting arbitrary temporal lengths and electrode configurations
2. **Large-Scale Pretraining**: 60,000+ hours from 92 datasets spanning 25,000 subjects
3. **Cross-Setup Generalization**: Handles varying protocols, devices, and montages without fine-tuning

### Comparison with Existing EEG Foundation Models

| Model | Training Data | Subjects | Positional Encoding | Cross-Setup |
|-------|--------------|----------|---------------------|-------------|
| BIOT | TUH only | ~10K | Absolute | No |
| Labram | TUH only | ~10K | Absolute | No |
| CBraMod | Limited | ~5K | Convolutional | Limited |
| NeuroGPT | TUH | ~10K | Learned | No |
| **REVE** | **92 datasets** | **25,000** | **4D Adaptive** | **Yes** |

### Technical Framework

#### 1. 4D Positional Encoding

Traditional positional encodings fail for EEG due to:
- Fixed montages (19 or 21 channels)
- Inflexible spatial representations
- No adaptation to electrode layouts

REVE's 4D encoding:
```
Position encoding = [x, y, z, t]

where:
  x, y, z: 3D electrode coordinates in standard space
  t:       Temporal position within recording
```

**Key Properties**:
- **Coordinate-based**: Each electrode encoded by its 3D location
- **Time-aware**: Temporal position explicitly modeled
- **Flexible**: Handles any number and arrangement of electrodes
- **Generalizable**: Projects unseen montages into learned space

#### 2. Architecture

```
Raw EEG (channels × time)
│
├─► 4D Positional Encoding
│   ├─ Spatial: Lookup electrode coordinates
│   ├─ Temporal: Sinusoidal encoding
│   └─ Combine: Additive fusion
│
├─► Transformer Encoder (×N layers)
│   ├─ Multi-head self-attention
│   ├─ Channel-wise temporal convolutions
│   └─ Layer normalization
│
├─► Masked Autoencoding Objective
│   └─ Reconstruct masked time-electrode segments
│
└─► Task-Specific Head
    └─ Linear probing or fine-tuning
```

### Mathematical Formulation

#### 4D Position Encoding

For electrode $i$ at position $(x_i, y_i, z_i)$ and time step $t$:

$$\text{PE}_{spatial} = \text{MLP}([x_i, y_i, z_i]) \in \mathbb{R}^d$$

$$\text{PE}_{temporal}^{(t, 2k)} = \sin\left(\frac{t}{10000^{2k/d}}\right)$$
$$\text{PE}_{temporal}^{(t, 2k+1)} = \cos\left(\frac{t}{10000^{2k/d}}\right)$$

$$\text{PE}_{total} = \text{PE}_{spatial} + \text{PE}_{temporal}$$

#### Masked Autoencoding

$$\mathcal{L} = \mathbb{E}_{\mathcal{M}} \left[ \sum_{(i,t) \in \mathcal{M}} \| x_{i,t} - \hat{x}_{i,t} \|^2 \right]$$

where $\mathcal{M}$ is the set of masked (electrode, time) pairs.

## Implementation Guide

### Prerequisites

```python
# Required packages
pip install torch torchvision torchaudio
pip install mne              # EEG processing
pip install scipy numpy pandas
pip install huggingface_hub  # For model weights
```

### Step-by-Step

#### Step 1: 4D Positional Encoding Implementation

```python
import torch
import torch.nn as nn
import numpy as np

class PositionalEncoding4D(nn.Module):
    """
    4D Positional Encoding for EEG
    
    Combines 3D electrode spatial coordinates with 1D temporal position
    """
    
    def __init__(self, d_model=512, max_len=10000, coordinate_scale=100.0):
        super().__init__()
        self.d_model = d_model
        self.coordinate_scale = coordinate_scale
        
        # MLP for spatial encoding (3D coordinates → d_model)
        self.spatial_encoder = nn.Sequential(
            nn.Linear(3, d_model // 2),
            nn.ReLU(),
            nn.Linear(d_model // 2, d_model)
        )
        
        # Temporal positional encoding (sinusoidal)
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2).float() * 
            (-np.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe)
    
    def forward(self, eeg_data, electrode_coords):
        """
        Args:
            eeg_data: (batch, channels, time) - EEG signals
            electrode_coords: (channels, 3) - 3D coordinates (x, y, z)
        
        Returns:
            encoded: (batch, channels, time, d_model)
        """
        batch_size, n_channels, seq_len = eeg_data.shape
        
        # Encode spatial positions
        # electrode_coords: (channels, 3)
        spatial_pe = self.spatial_encoder(electrode_coords)  # (channels, d_model)
        
        # Get temporal encodings
        temporal_pe = self.pe[:seq_len]  # (time, d_model)
        
        # Combine: broadcast spatial across time, temporal across channels
        # spatial_pe: (channels, 1, d_model)
        # temporal_pe: (1, time, d_model)
        pe_combined = spatial_pe.unsqueeze(1) + temporal_pe.unsqueeze(0)
        # Result: (channels, time, d_model)
        
        # Expand for batch
        pe_combined = pe_combined.unsqueeze(0).expand(batch_size, -1, -1, -1)
        
        # Project EEG data to match dimension
        eeg_projected = eeg_data.unsqueeze(-1)  # (B, C, T, 1)
        
        # Add positional encoding
        encoded = eeg_projected + pe_combined
        
        return encoded


def load_electrode_coordinates(montage_name='standard_1020'):
    """
    Load standard electrode coordinates in 3D space
    
    Args:
        montage_name: Name of electrode montage
    
    Returns:
        coords: Dict mapping channel names to (x, y, z) coordinates
    """
    import mne
    
    # Load standard montage
    montage = mne.channels.make_standard_montage(montage_name)
    
    # Extract coordinates
    coords = {}
    for ch_name, pos in zip(montage.ch_names, montage.get_positions()['ch_pos'].values()):
        coords[ch_name] = pos  # (x, y, z) in meters
    
    return coords


def create_coordinate_tensor(channel_names, coords_dict):
    """
    Create coordinate tensor for given channel names
    
    Args:
        channel_names: List of channel names in order
        coords_dict: Dictionary mapping names to coordinates
    
    Returns:
        coords_tensor: (n_channels, 3) tensor
    """
    coords_list = []
    for ch in channel_names:
        if ch in coords_dict:
            coords_list.append(coords_dict[ch])
        else:
            # Handle missing channels with interpolation or default
            coords_list.append([0.0, 0.0, 0.0])  # Default/unknown
    
    return torch.tensor(coords_list, dtype=torch.float32)
```

#### Step 2: REVE Model Architecture

```python
class REVEncoder(nn.Module):
    """
    REVE: Representation for EEG with Versatile Embeddings
    Transformer-based encoder with 4D positional encoding
    """
    
    def __init__(
        self,
        d_model=512,
        nhead=8,
        num_layers=12,
        dim_feedforward=2048,
        dropout=0.1,
        max_channels=128,
        max_time=10000
    ):
        super().__init__()
        
        self.d_model = d_model
        
        # Input projection: raw EEG to embedding dimension
        self.input_projection = nn.Linear(1, d_model)
        
        # 4D Positional encoding
        self.pos_encoding = PositionalEncoding4D(d_model, max_time)
        
        # Transformer encoder layers
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_feedforward,
            dropout=dropout,
            batch_first=True,
            norm_first=True  # Pre-norm for stability
        )
        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers=num_layers
        )
        
        # Channel-wise temporal convolution
        self.temporal_conv = nn.Conv1d(
            in_channels=d_model,
            out_channels=d_model,
            kernel_size=3,
            padding=1,
            groups=d_model  # Depthwise separable
        )
        
        self.norm = nn.LayerNorm(d_model)
    
    def forward(self, eeg_data, electrode_coords, mask=None):
        """
        Args:
            eeg_data: (batch, channels, time)
            electrode_coords: (channels, 3) - 3D coordinates
            mask: Optional mask for attention
        
        Returns:
            features: (batch, channels, time, d_model)
        """
        batch_size, n_channels, seq_len = eeg_data.shape
        
        # Apply 4D positional encoding
        x = self.pos_encoding(eeg_data, electrode_coords)
        # x: (batch, channels, time, d_model)
        
        # Reshape for transformer: flatten channels and time
        x = x.view(batch_size, n_channels * seq_len, self.d_model)
        
        # Transformer encoding
        x = self.transformer(x, src_key_padding_mask=mask)
        
        # Reshape back
        x = x.view(batch_size, n_channels, seq_len, self.d_model)
        
        # Channel-wise temporal convolution
        # Reshape: (batch*channels, d_model, time)
        x_conv = x.permute(0, 1, 3, 2).reshape(-1, self.d_model, seq_len)
        x_conv = self.temporal_conv(x_conv)
        x_conv = x_conv.view(batch_size, n_channels, self.d_model, seq_len)
        x_conv = x_conv.permute(0, 1, 3, 2)  # Back to (B, C, T, D)
        
        # Residual and norm
        x = self.norm(x + x_conv)
        
        return x


class REVE(nn.Module):
    """
    Complete REVE model with pretraining and evaluation modes
    """
    
    def __init__(
        self,
        d_model=512,
        nhead=8,
        num_layers=12,
        mask_ratio=0.15
    ):
        super().__init__()
        
        self.mask_ratio = mask_ratio
        
        # Encoder
        self.encoder = REVEncoder(d_model, nhead, num_layers)
        
        # Decoder for masked autoencoding
        self.decoder = nn.Sequential(
            nn.Linear(d_model, d_model),
            nn.ReLU(),
            nn.Linear(d_model, 1)  # Reconstruct single channel value
        )
        
    def forward(self, eeg_data, electrode_coords, mode='pretrain'):
        """
        Args:
            eeg_data: (batch, channels, time)
            electrode_coords: (channels, 3)
            mode: 'pretrain' or 'encode'
        
        Returns:
            If pretrain: reconstructed signal
            If encode: feature representation
        """
        batch_size, n_channels, seq_len = eeg_data.shape
        
        if mode == 'pretrain':
            # Create random mask
            mask = self.create_random_mask(batch_size, n_channels, seq_len)
            
            # Mask input
            masked_eeg = eeg_data.clone()
            masked_eeg[mask] = 0  # Zero out masked positions
            
            # Encode
            features = self.encoder(masked_eeg, electrode_coords)
            
            # Decode
            reconstructed = self.decoder(features).squeeze(-1)
            
            return reconstructed, mask
        
        else:  # encode mode
            features = self.encoder(eeg_data, electrode_coords)
            return features
    
    def create_random_mask(self, batch_size, n_channels, seq_len):
        """Create random mask for spatial-temporal positions"""
        mask = torch.zeros(batch_size, n_channels, seq_len, dtype=torch.bool)
        
        n_positions = batch_size * n_channels * seq_len
        n_mask = int(n_positions * self.mask_ratio)
        
        # Randomly select positions to mask
        flat_indices = torch.randperm(n_positions)[:n_mask]
        
        # Convert to 3D indices
        b_idx = flat_indices // (n_channels * seq_len)
        c_idx = (flat_indices % (n_channels * seq_len)) // seq_len
        t_idx = flat_indices % seq_len
        
        mask[b_idx, c_idx, t_idx] = True
        
        return mask
```

#### Step 3: Pretraining on Large-Scale EEG

```python
from torch.utils.data import Dataset, DataLoader
import mne

class LargeScaleEEGDataset(Dataset):
    """
    Dataset for large-scale EEG pretraining
    Handles multiple datasets with different montages
    """
    
    def __init__(self, dataset_list, segment_length=30, sampling_rate=200):
        """
        Args:
            dataset_list: List of paths to EEG datasets
            segment_length: Segment length in seconds
            sampling_rate: Target sampling rate
        """
        self.dataset_list = dataset_list
        self.segment_length = segment_length
        self.sampling_rate = sampling_rate
        self.samples_per_segment = segment_length * sampling_rate
        
        # Build index of all available segments
        self.index = self._build_index()
    
    def _build_index(self):
        """Index all available segments across datasets"""
        index = []
        
        for dataset_path in self.dataset_list:
            # Load dataset metadata
            # This is simplified - actual implementation would
            # handle various EEG formats (EDF, FIFF, etc.)
            recordings = self._list_recordings(dataset_path)
            
            for recording in recordings:
                info = self._get_recording_info(recording)
                duration = info['duration']
                n_segments = int(duration / self.segment_length)
                
                for seg_idx in range(n_segments):
                    index.append({
                        'recording': recording,
                        'segment_idx': seg_idx,
                        'montage': info['montage'],
                        'channels': info['channels']
                    })
        
        return index
    
    def __len__(self):
        return len(self.index)
    
    def __getitem__(self, idx):
        sample = self.index[idx]
        
        # Load segment
        eeg_data = self._load_segment(
            sample['recording'],
            sample['segment_idx'],
            self.segment_length
        )
        
        # Get electrode coordinates for this montage
        coords = load_electrode_coordinates(sample['montage'])
        coord_tensor = create_coordinate_tensor(sample['channels'], coords)
        
        return {
            'eeg': torch.tensor(eeg_data, dtype=torch.float32),
            'coords': coord_tensor,
            'channels': sample['channels']
        }


def pretrain_reve(model, train_loader, epochs=100, lr=1e-4, device='cuda'):
    """
    Pretrain REVE with masked autoencoding
    """
    model = model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.01)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, epochs)
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for batch_idx, batch in enumerate(train_loader):
            eeg = batch['eeg'].to(device)
            coords = batch['coords'].to(device)
            
            optimizer.zero_grad()
            
            # Forward pass with masking
            reconstructed, mask = model(eeg, coords, mode='pretrain')
            
            # Compute reconstruction loss only on masked positions
            loss = F.mse_loss(reconstructed[mask], eeg[mask])
            
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            
            if batch_idx % 100 == 0:
                print(f'Epoch {epoch}, Batch {batch_idx}: '
                      f'Loss = {loss.item():.4f}')
        
        scheduler.step()
        avg_loss = total_loss / len(train_loader)
        print(f'Epoch {epoch} complete: Avg Loss = {avg_loss:.4f}')
        
        # Save checkpoint
        if epoch % 10 == 0:
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'loss': avg_loss
            }, f'reve_checkpoint_epoch_{epoch}.pt')
    
    return model
```

#### Step 4: Linear Probing and Fine-tuning

```python
class REVEClassifier(nn.Module):
    """
    Linear probe or fine-tuned classifier on top of REVE
    """
    
    def __init__(self, reve_model, num_classes, mode='linear'):
        super().__init__()
        
        self.reve = reve_model
        self.mode = mode
        
        if mode == 'linear':
            # Freeze REVE encoder
            for param in self.reve.parameters():
                param.requires_grad = False
        
        # Classification head
        d_model = self.reve.encoder.d_model
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, d_model)),  # Global pooling
            nn.Flatten(),
            nn.Linear(d_model, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes)
        )
    
    def forward(self, eeg_data, electrode_coords):
        """
        Args:
            eeg_data: (batch, channels, time)
            electrode_coords: (channels, 3)
        
        Returns:
            logits: (batch, num_classes)
        """
        # Encode
        features = self.reve(eeg_data, electrode_coords, mode='encode')
        # features: (batch, channels, time, d_model)
        
        # Classify
        logits = self.classifier(features)
        
        return logits


def linear_probe_evaluation(reve_model, task_loaders, n_classes_per_task):
    """
    Evaluate REVE with linear probing on multiple tasks
    """
    results = {}
    
    for task_name, loader in task_loaders.items():
        print(f"\nEvaluating on {task_name}...")
        
        n_classes = n_classes_per_task[task_name]
        classifier = REVEClassifier(reve_model, n_classes, mode='linear')
        classifier = classifier.to('cuda')
        
        # Train linear classifier
        optimizer = torch.optim.Adam(
            classifier.classifier.parameters(),
            lr=1e-3
        )
        
        for epoch in range(20):
            classifier.train()
            for batch in loader['train']:
                eeg = batch['eeg'].cuda()
                coords = batch['coords'].cuda()
                labels = batch['label'].cuda()
                
                optimizer.zero_grad()
                logits = classifier(eeg, coords)
                loss = F.cross_entropy(logits, labels)
                loss.backward()
                optimizer.step()
        
        # Evaluate
        classifier.eval()
        correct = 0
        total = 0
        
        with torch.no_grad():
            for batch in loader['test']:
                eeg = batch['eeg'].cuda()
                coords = batch['coords'].cuda()
                labels = batch['label'].cuda()
                
                logits = classifier(eeg, coords)
                preds = logits.argmax(dim=1)
                
                correct += (preds == labels).sum().item()
                total += labels.size(0)
        
        accuracy = 100. * correct / total
        results[task_name] = accuracy
        print(f"{task_name} Accuracy: {accuracy:.2f}%")
    
    return results
```

#### Step 5: Cross-Dataset Generalization

```python
def evaluate_cross_dataset(reve_model, source_loader, target_loader):
    """
    Evaluate zero-shot and few-shot transfer to new dataset
    with different electrode montage
    """
    
    # Train classifier on source dataset
    classifier = REVEClassifier(reve_model, num_classes=5)
    
    print("Training on source dataset...")
    # ... training code ...
    
    # Evaluate on target dataset (different montage)
    print("\nEvaluating on target dataset (different montage)...")
    
    # Zero-shot: directly apply without adaptation
    print("Zero-shot performance:")
    zero_shot_acc = evaluate(classifier, target_loader)
    print(f"Accuracy: {zero_shot_acc:.2f}%")
    
    # Few-shot: fine-tune classifier on small target sample
    print("\nFew-shot (10 samples per class):")
    few_shot_loader = create_few_shot_loader(target_loader, n_samples=10)
    
    # Fine-tune only classifier head
    for param in classifier.reve.parameters():
        param.requires_grad = False
    
    optimizer = torch.optim.Adam(
        classifier.classifier.parameters(),
        lr=1e-4
    )
    
    for epoch in range(10):
        for batch in few_shot_loader:
            # Training loop
            pass
    
    few_shot_acc = evaluate(classifier, target_loader)
    print(f"Few-shot Accuracy: {few_shot_acc:.2f}%")
    
    return zero_shot_acc, few_shot_acc
```

## Applications

### 1. Motor Imagery BCI

```python
class MotorImageryBCI:
    """
    Motor imagery brain-computer interface using REVE
    """
    
    def __init__(self, reve_model, n_classes=4):
        self.model = REVEClassifier(reve_model, n_classes)
        self.model.eval()
        
        # 4 classes: left hand, right hand, feet, tongue
        self.class_names = ['left', 'right', 'feet', 'tongue']
    
    def predict(self, eeg_segment, coords):
        """Predict motor imagery class from EEG"""
        with torch.no_grad():
            logits = self.model(eeg_segment, coords)
            probs = F.softmax(logits, dim=-1)
            pred = probs.argmax(dim=-1)
        
        return {
            'class': self.class_names[pred],
            'confidence': probs[pred].item(),
            'all_probs': probs
        }
    
    def calibrate(self, calibration_data):
        """
        Quick calibration with minimal data
        Adapts classifier to new user
        """
        # Few-shot adaptation
        pass


# Usage example
bci = MotorImageryBCI(reve_model)

# Real-time prediction loop
for eeg_window in eeg_stream:
    result = bci.predict(eeg_window, electrode_coords)
    print(f"Predicted: {result['class']} "
          f"({result['confidence']:.2%} confident)")
```

### 2. Sleep Staging

```python
class SleepStaging:
    """
    Automated sleep staging using REVE
    """
    
    STAGES = ['Wake', 'N1', 'N2', 'N3', 'REM']
    
    def __init__(self, reve_model):
        self.model = REVEClassifier(reve_model, num_classes=5)
        self.window_size = 30  # 30-second epochs
    
    def stage_recording(self, eeg_recording, coords):
        """
        Stage full night recording
        
        Args:
            eeg_recording: (channels, total_time)
            coords: (channels, 3)
        
        Returns:
            hypnogram: List of sleep stages per epoch
        """
        n_epochs = eeg_recording.shape[1] // (self.window_size * sampling_rate)
        
        hypnogram = []
        for epoch_idx in range(n_epochs):
            start = epoch_idx * self.window_size * sampling_rate
            end = start + self.window_size * sampling_rate
            
            epoch_data = eeg_recording[:, start:end]
            
            # Predict stage
            logits = self.model(epoch_data.unsqueeze(0), coords)
            stage_idx = logits.argmax(dim=-1).item()
            
            hypnogram.append(self.STAGES[stage_idx])
        
        return hypnogram
    
    def compute_sleep_metrics(self, hypnogram):
        """Compute sleep quality metrics"""
        total_epochs = len(hypnogram)
        
        metrics = {
            'sleep_efficiency': 1 - hypnogram.count('Wake') / total_epochs,
            'deep_sleep_pct': hypnogram.count('N3') / total_epochs,
            'rem_pct': hypnogram.count('REM') / total_epochs,
            'sleep_onset_latency': self._find_first_sleep(hypnogram)
        }
        
        return metrics
```

### 3. Seizure Detection

```python
class SeizureDetector:
    """
    Real-time seizure detection using REVE
    """
    
    def __init__(self, reve_model, threshold=0.9):
        self.model = REVEClassifier(reve_model, num_classes=2)
        self.threshold = threshold
        self.buffer = []
        
    def process_window(self, eeg_window, coords):
        """
        Process a single EEG window
        
        Returns:
            is_seizure: Boolean
            confidence: Probability
        """
        with torch.no_grad():
            logits = self.model(eeg_window, coords)
            probs = F.softmax(logits, dim=-1)
            seizure_prob = probs[0, 1].item()  # Class 1 = seizure
        
        return seizure_prob > self.threshold, seizure_prob
    
    def run_detection(self, eeg_stream, coords):
        """
        Run continuous seizure detection
        """
        detections = []
        
        for window in eeg_stream:
            is_seizure, confidence = self.process_window(window, coords)
            
            if is_seizure:
                detections.append({
                    'time': window.timestamp,
                    'confidence': confidence
                })
                
                if confidence > 0.95:
                    self.trigger_alarm()
        
        return detections
```

## Benchmarks

### Performance on Downstream Tasks

| Task | Dataset | Metric | REVE | Previous SOTA |
|------|---------|--------|------|---------------|
| Motor Imagery | BCI Competition IV | Accuracy | 78.5% | 72.3% |
| Seizure Detection | TUH EEG | AUC | 0.94 | 0.89 |
| Sleep Staging | Sleep-EDF | F1 | 0.86 | 0.81 |
| Cognitive Load | WLData | MAE | 0.12 | 0.18 |
| Emotion Recognition | DEAP | Accuracy | 71.2% | 65.4% |

### Cross-Dataset Generalization

| Source → Target | Zero-Shot | Few-Shot (10/class) |
|-----------------|-----------|---------------------|
| TUH → Clinical | 64.3% | 82.1% |
| BCI → Motor Imagery | 58.7% | 79.4% |
| Sleep-EDF → SHHS | 71.2% | 88.6% |

### Computational Efficiency

| Model | Params | FLOPs | Inference Time (1s EEG) |
|-------|--------|-------|-------------------------|
| EEGNet | 2.4K | 5M | 2.1ms |
| DeepConvNet | 200K | 150M | 12.4ms |
| Labram | 5M | 800M | 45.2ms |
| **REVE** | **50M** | **2B** | **78.3ms** |
| REVE (pruned) | 10M | 400M | 22.1ms |

## Pitfalls

- **Data Quality Sensitivity**: Performance degrades with high electrode impedance or motion artifacts
- **Coordinate Standardization**: Requires accurate electrode localization for optimal 4D encoding
- **Computational Requirements**: Large model (50M params) requires GPU for real-time inference
- **Montage Mismatch**: Extreme differences in electrode placement (e.g., 10-20 vs. 10-10) may require coordinate mapping
- **Temporal Resolution**: Designed for standard clinical EEG (128-512 Hz); very high-frequency recordings may need downsampling

## Related Skills

- neurostorm-fmri-foundation
- neural-dynamics-universal-translator-foundation
- eeg-diffusion-visual-reconstruction
- mind2drive-eeg-driver-intention
- eeg-brain-connectivity-bci

## References

```bibtex
@article{elouahidi2025reve,
  title={REVE: A Foundation Model for EEG Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects},
  author={El Ouahidi, Yassine and Lys, Jonathan and Th{\"o}lke, Philipp and Farrugia, Nicolas and Pasdeloup, Bastien and Gripon, Vincent and Jerbi, Karim and Lioi, Giulia},
  journal={arXiv preprint arXiv:2510.21585},
  year={2025}
}
```
