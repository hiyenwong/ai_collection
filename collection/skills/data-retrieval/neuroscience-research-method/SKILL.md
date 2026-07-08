---
name: neuroscience-research-method
version: 1.0.0
description: "CNN + Adversarial Autoencoder (AAE) for EEG signal classification — from raw EEG to image representations, latent-space regularization, and robust brain-computer interface (BCI) decoding."
keywords:
  - eeg-classification
  - adversarial-autoencoder
  - cnn-eeg
  - brain-computer-interface
  - spectrogram
  - topographic-map
  - latent-space-regularization
  - 脑电图分类
  - 对抗自编码器
  - 脑机接口
  - 深度学习
  - 神经信号处理
related:
  - signal-processing
  - time-series-analysis
  - computer-vision
  - generative-models
  - domain-adaptation
  - eeg-preprocessing
---

# CNN + Adversarial Autoencoder for EEG Classification

## Overview

This skill covers the methodology for classifying electroencephalography (EEG) signals using a hybrid **Convolutional Neural Network (CNN)** + **Adversarial Autoencoder (AAE)** architecture. The approach transforms raw multi-channel EEG time-series into 2D image representations, encodes them with a CNN-based encoder, and regularizes the latent space via adversarial training to improve generalization and reduce overfitting — a persistent challenge in EEG/BCI research.

### Why AAE for EEG?

| Challenge | AAE Solution |
|-----------|-------------|
| Small labeled datasets (10-100 subjects) | Adversarial regularization prevents degenerate latent codes |
| Non-stationary EEG signals | Distribution matching stabilizes feature representations |
| High inter-subject variability | Latent prior (Gaussian/mixture) enforces compact representations |
| Artifact contamination | AAE reconstruction loss acts as implicit denoiser |

---

## 1. EEG-to-Image Transformation Methods (EEG转图像变换方法)

### 1.1 Time-Frequency Spectrograms (时频图谱)

Convert each EEG channel into a spectrogram via Short-Time Fourier Transform (STFT) or Continuous Wavelet Transform (CWT).

```python
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

def eeg_to_spectrogram(eeg_data, fs=256, nperseg=64, noverlap=32):
    """
    Transform multi-channel EEG into spectrogram images.
    
    Args:
        eeg_data: (n_channels, n_samples) ndarray
        fs: sampling frequency in Hz
        nperseg: window size for STFT
        noverlap: overlap between windows
        
    Returns:
        spectrograms: (n_channels, freq_bins, time_bins) ndarray
    """
    n_channels = eeg_data.shape[0]
    freqs, times, Sxx = signal.spectrogram(
        eeg_data[0], fs=fs, nperseg=nperseg, noverlap=noverlap
    )
    
    spectrograms = np.zeros((n_channels, len(freqs), len(times)))
    for ch in range(n_channels):
        _, _, Sxx = signal.spectrogram(
            eeg_data[ch], fs=fs, nperseg=nperseg, noverlap=noverlap
        )
        spectrograms[ch] = np.log1p(np.abs(Sxx))  # log-scale for dynamic range
    
    return spectrograms

# --- Continuous Wavelet Transform (CWT) variant ---
def eeg_to_scalogram(eeg_data, fs=256, widths=None, wavelet='morl'):
    """CWT-based scalogram for better time-frequency resolution."""
    import pywt
    if widths is None:
        widths = np.arange(1, 128)
    
    n_channels = eeg_data.shape[0]
    scalograms = []
    for ch in range(n_channels):
        coeffs = pywt.cwt(eeg_data[ch], widths, wavelet, sampling_period=1.0/fs)
        scalograms.append(np.log1p(np.abs(coeffs[0])))
    return np.array(scalograms)
```

**Stacking channels into a single image:**
- **(n_channels, freq_bins, time_bins)** → treat channels as "color" channels (like RGB)
- Or concatenate along frequency axis for single-channel input to CNN

### 1.2 Topographic Maps (地形图)

Project electrode voltages onto a 2D scalp map using spatial interpolation. Ideal for ERP/SSVEP analysis where spatial distribution is discriminative.

```python
import numpy as np
from scipy.interpolate import griddata

# Standard 10-20 system electrode positions (x, y in normalized units)
ELECTRODE_POSITIONS = {
    'Fp1': (-0.35, 0.45), 'Fp2': (0.35, 0.45),
    'F3':  (-0.25, 0.25), 'Fz':  (0.0,   0.3),  'F4':  (0.25, 0.25),
    'C3':  (-0.35, 0.0),  'Cz':  (0.0,   0.0),  'C4':  (0.35, 0.0),
    'P3':  (-0.25, -0.25),'Pz':  (0.0,  -0.3),  'P4':  (0.25, -0.25),
    'O1':  (-0.2,  -0.45),'Oz':  (0.0,  -0.5),  'O2':  (0.2,  -0.45),
}

def eeg_to_topomap(eeg_values, electrode_names, grid_size=32):
    """
    Convert single-timepoint EEG values to a topographic scalp map image.
    
    Args:
        eeg_values: dict or list of voltage values per electrode
        electrode_names: list of electrode names (10-20 system)
        grid_size: output image resolution (grid_size x grid_size)
        
    Returns:
        topomap: (grid_size, grid_size) ndarray
    """
    if isinstance(eeg_values, dict):
        values = [eeg_values[el] for el in electrode_names]
    else:
        values = list(eeg_values)
    
    points = np.array([ELECTRODE_POSITIONS[el] for el in electrode_names])
    
    # Create grid
    xi = np.linspace(-0.6, 0.6, grid_size)
    yi = np.linspace(-0.6, 0.6, grid_size)
    XI, YI = np.meshgrid(xi, yi)
    
    # Interpolate using radial basis / cubic
    ZI = griddata(points, values, (XI, YI), method='cubic', fill_value=0)
    ZI = np.nan_to_num(ZI, nan=0.0)
    
    # Normalize to [0, 1]
    ZI = (ZI - ZI.min()) / (ZI.ptp() + 1e-8)
    
    return ZI

def eeg_epoch_to_topomap_sequence(eeg_epoch, electrode_names, 
                                   time_window=None, grid_size=32):
    """Convert an EEG epoch to a sequence of topographic maps."""
    n_samples = eeg_epoch.shape[1]
    if time_window is not None:
        # Average over the specified window
        eeg_epoch = eeg_epoch[:, time_window[0]:time_window[1]].mean(axis=1, keepdims=True)
    
    topomaps = []
    for t in range(eeg_epoch.shape[1]):
        topomaps.append(eeg_to_topomap(
            eeg_epoch[:, t], electrode_names, grid_size
        ))
    return np.array(topomaps)  # (n_timepoints, grid_size, grid_size)
```

### 1.3 Combined Representations (组合表示法)

For maximum information, stack multiple representations:

```python
def build_multi_view_input(eeg_epoch, fs=256, electrode_names=None, grid_size=32):
    """
    Create multi-view tensor from a single EEG epoch.
    
    Returns:
        (n_views, H, W) tensor suitable for multi-branch CNN
    """
    views = []
    
    # View 1: Spectrogram (concatenate all channels along freq axis)
    spec = eeg_to_spectrogram(eeg_epoch, fs=fs)
    views.append(np.concatenate([spec[ch] for ch in range(spec.shape[0])], axis=0))
    
    # View 2: Topographic maps at key time windows
    if electrode_names:
        topo_seq = eeg_epoch_to_topomap_sequence(eeg_epoch, electrode_names, grid_size=grid_size)
        views.append(topo_seq.mean(axis=0))  # average over time
    
    return np.array(views)  # (n_views, H, W)
```

---

## 2. CNN Architecture for EEG (EEG卷积神经网络架构)

### 2.1 Core CNN Encoder

Adapted for EEG image inputs with spectrogram/topographic map characteristics:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class EEGCNNEncoder(nn.Module):
    """
    CNN Encoder for EEG image representations.
    Designed for spectrogram (freq × time) and topomap (spatial) inputs.
    """
    def __init__(self, input_channels=1, latent_dim=64, dropout=0.5):
        super().__init__()
        
        self.encoder = nn.Sequential(
            # Block 1: Low-level feature extraction
            nn.Conv2d(input_channels, 32, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(32),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(dropout),
            
            # Block 2: Mid-level feature extraction
            nn.Conv2d(32, 64, kernel_size=5, stride=1, padding=2),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(dropout),
            
            # Block 3: High-level feature extraction
            nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            nn.MaxPool2d(2, 2),
            
            # Block 4: Additional depth for complex patterns
            nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2),
            nn.AdaptiveAvgPool2d(1),  # Global pooling → spatial invariance
        )
        
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256, latent_dim),
        )
    
    def forward(self, x):
        features = self.encoder(x)      # (B, 256, 1, 1)
        latent = self.fc(features)      # (B, latent_dim)
        return latent, features

class EEGCNNDecoder(nn.Module):
    """CNN Decoder for AAE reconstruction."""
    def __init__(self, input_dim=64, output_channels=1, output_size=(32, 32)):
        super().__init__()
        self.output_size = output_size
        
        self.fc = nn.Sequential(
            nn.Linear(input_dim, 256 * 4 * 4),
            nn.LeakyReLU(0.2),
        )
        
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(256, 128, 4, stride=2, padding=1),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2),
            
            nn.ConvTranspose2d(128, 64, 4, stride=2, padding=1),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2),
            
            nn.ConvTranspose2d(64, output_channels, 4, stride=2, padding=1),
            nn.Sigmoid(),
        )
    
    def forward(self, z):
        x = self.fc(z)
        x = x.view(-1, 256, 4, 4)
        return self.decoder(x)
```

### 2.2 EEG-Specific CNN Variants

```python
class MultiBranchEEGCNN(nn.Module):
    """
    Multi-branch CNN that processes different EEG views separately,
    then fuses them in latent space.
    
    Branches:
      1. Spectrogram branch (temporal-frequency features)
      2. Topographic branch (spatial features)
      3. Raw signal branch (temporal features via 1D conv)
    """
    def __init__(self, latent_dim=64):
        super().__init__()
        
        # Branch 1: Spectrogram (2D)
        self.spec_branch = nn.Sequential(
            nn.Conv2d(1, 32, 5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
        )
        
        # Branch 2: Topographic map (2D spatial)
        self.topo_branch = nn.Sequential(
            nn.Conv2d(1, 32, 5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
        )
        
        # Fusion + projection to latent space
        self.fusion = nn.Sequential(
            nn.Linear(64 + 64, latent_dim),
            nn.BatchNorm1d(latent_dim),
            nn.ReLU(),
        )
    
    def forward(self, spec_input, topo_input):
        spec_feat = self.spec_branch(spec_input)   # (B, 64)
        topo_feat = self.topo_branch(topo_input)    # (B, 64)
        fused = torch.cat([spec_feat, topo_feat], dim=1)
        latent = self.fusion(fused)
        return latent
```

---

## 3. AAE Latent Space Regularization (对抗自编码器潜在空间正则化)

### 3.1 Adversarial Autoencoder (AAE) Core

The AAE adds a discriminator that enforces the aggregated posterior distribution Q(z) to match a prior P(z) (typically N(0,I) or a Gaussian Mixture Model).

```python
class AAE(nn.Module):
    """
    Adversarial Autoencoder for EEG classification.
    
    Components:
      - Encoder: EEG image → latent code z
      - Decoder: latent code z → reconstructed EEG image
      - Discriminator: distinguishes real samples from prior vs. encoded z
      - Classifier: latent code z → class label (optional, semi-supervised)
    """
    def __init__(self, input_channels=1, latent_dim=64, n_classes=4):
        super().__init__()
        self.encoder = EEGCNNEncoder(input_channels, latent_dim)
        self.decoder = EEGCNNDecoder(latent_dim, input_channels)
        
        # Discriminator for adversarial regularization
        self.discriminator = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.LeakyReLU(0.2),
            nn.Linear(64, 1),  # real/fake
            nn.Sigmoid(),
        )
        
        # Optional classifier (for semi-supervised AAE)
        self.classifier = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(64, n_classes),
        )
    
    def encode(self, x):
        return self.encoder(x)
    
    def decode(self, z):
        return self.decoder(z)
    
    def forward(self, x):
        z, features = self.encode(x)
        x_recon = self.decode(z)
        class_logits = self.classifier(z)
        return z, x_recon, class_logits


class AAETrainer:
    """Training loop for AAE with three adversarial phases."""
    
    def __init__(self, model, device='cuda'):
        self.model = model.to(device)
        self.device = device
        
        # Separate optimizers for different phases
        self.recon_opt = torch.optim.Adam(
            list(model.encoder.parameters()) + 
            list(model.decoder.parameters()), lr=1e-4, weight_decay=1e-5
        )
        self.disc_opt = torch.optim.Adam(model.discriminator.parameters(), lr=1e-4)
        self.gen_opt = torch.optim.Adam(model.encoder.parameters(), lr=1e-4)
        self.clf_opt = torch.optim.Adam(model.classifier.parameters(), lr=1e-3)
        
        self.bce_loss = nn.BCELoss()
        self.mse_loss = nn.MSELoss()
        self.ce_loss = nn.CrossEntropyLoss()
    
    def train_step(self, eeg_images, labels=None):
        """
        Single training step with 3 adversarial phases:
          1. Reconstruction: minimize ||x - x̂||²
          2. Discriminator: distinguish prior samples from encoded z
          3. Generator (encoder): fool the discriminator
          4. Classification (optional): predict labels from z
        """
        eeg_images = eeg_images.to(self.device)
        
        # --- Phase 1: Reconstruction ---
        z, x_recon, class_logits = self.model(eeg_images)
        recon_loss = self.mse_loss(x_recon, eeg_images)
        
        self.recon_opt.zero_grad()
        recon_loss.backward()
        self.recon_opt.step()
        
        # --- Phase 2: Discriminator training ---
        batch_size = eeg_images.shape[0]
        real_samples = torch.randn(batch_size, z.shape[1]).to(self.device)  # prior N(0,I)
        
        real_labels = torch.ones(batch_size, 1).to(self.device)
        fake_labels = torch.zeros(batch_size, 1).to(self.device)
        
        d_real = self.model.discriminator(real_samples)
        d_fake = self.model.discriminator(z.detach())  # detach z from encoder
        
        d_loss = self.bce_loss(d_real, real_labels) + \
                 self.bce_loss(d_fake, fake_labels)
        
        self.disc_opt.zero_grad()
        d_loss.backward()
        self.disc_opt.step()
        
        # --- Phase 3: Generator (encoder) adversarial training ---
        d_fake_for_gen = self.model.discriminator(z)
        g_loss = self.bce_loss(d_fake_for_gen, real_labels)  # want D(z) = 1
        
        self.gen_opt.zero_grad()
        g_loss.backward()
        self.gen_opt.step()
        
        # --- Phase 4: Classification (if labels available) ---
        clf_loss = torch.tensor(0.0, device=self.device)
        if labels is not None:
            labels = labels.to(self.device)
            clf_loss = self.ce_loss(class_logits, labels)
            
            self.clf_opt.zero_grad()
            clf_loss.backward()
            self.clf_opt.step()
        
        return {
            'recon_loss': recon_loss.item(),
            'disc_loss': d_loss.item(),
            'gen_loss': g_loss.item(),
            'clf_loss': clf_loss.item(),
        }
```

### 3.2 Gaussian Mixture Prior (高斯混合先验)

For classification tasks, a GMM prior with one component per class creates well-separated clusters:

```python
class GMMPrior:
    """Gaussian Mixture Model prior for class-conditioned AAE."""
    
    def __init__(self, n_classes, latent_dim, device='cuda'):
        self.n_classes = n_classes
        self.latent_dim = latent_dim
        self.device = device
        
        # Pre-compute cluster centers on a hypersphere
        centers = torch.zeros(n_classes, latent_dim)
        for i in range(n_classes):
            centers[i, i % latent_dim] = 1.0
        # Normalize to unit sphere
        centers = F.normalize(centers, p=2, dim=1) * 2.0
        self.register_buffer('centers', centers)
    
    def sample(self, batch_size, labels=None):
        """Sample from GMM prior."""
        if labels is None:
            labels = torch.randint(0, self.n_classes, (batch_size,))
        
        centers = self.centers[labels].to(self.device)
        noise = torch.randn_like(centers) * 0.5  # variance per cluster
        return centers + noise
```

### 3.3 Additional Regularization Techniques

```python
def add_latent_regularization(z, reg_type='kl', beta=0.1):
    """
    Additional latent space regularization beyond adversarial loss.
    
    reg_type: 'kl' (KL divergence), 'mmd' (Maximum Mean Discrepancy), 
              'coral' (CORAL domain alignment)
    """
    if reg_type == 'kl':
        # KL(Q(z) || N(0,I))
        mu = z.mean(dim=0)
        var = z.var(dim=0)
        kl = 0.5 * torch.sum(mu**2 + var - torch.log(var) - 1)
        return beta * kl
    
    elif reg_type == 'mmd':
        # Linear MMD between z and prior samples
        prior = torch.randn_like(z)
        K_zz = torch.mm(z, z.t()) / z.shape[1]
        K_pp = torch.mm(prior, prior.t()) / prior.shape[1]
        K_zp = torch.mm(z, prior.t()) / z.shape[1]
        mmd = K_zz.mean() + K_pp.mean() - 2 * K_zp.mean()
        return beta * mmd
    
    elif reg_type == 'coral':
        # CORAL: align covariance matrices
        cov_z = z - z.mean(dim=0)
        cov_z = torch.mm(cov_z.t(), cov_z) / (z.shape[0] - 1)
        prior = torch.randn_like(z)
        cov_p = prior - prior.mean(dim=0)
        cov_p = torch.mm(cov_p.t(), cov_p) / (prior.shape[0] - 1)
        coral = torch.sum((cov_z - cov_p) ** 2)
        return beta * coral
    
    return torch.tensor(0.0, device=z.device)
```

---

## 4. Implementation Patterns (实现模式)

### 4.1 Data Pipeline (数据处理流水线)

```python
from torch.utils.data import Dataset, DataLoader
import h5py

class EEGDataset(Dataset):
    """EEG dataset with on-the-fly image transformation."""
    
    def __init__(self, data_path, transform='spectrogram', 
                 electrode_names=None, fs=256, augment=False):
        self.transform = transform
        self.electrode_names = electrode_names
        self.fs = fs
        self.augment = augment
        
        # Load from HDF5 / MATLAB / EDF
        if data_path.endswith('.h5'):
            with h5py.File(data_path, 'r') as f:
                self.data = f['eeg_data'][:]       # (n_trials, n_channels, n_samples)
                self.labels = f['labels'][:]        # (n_trials,)
        else:
            self.data, self.labels = self._load_custom(data_path)
    
    def _apply_augmentation(self, eeg):
        """EEG-specific augmentations."""
        if np.random.rand() > 0.5:
            # Time shift (circular)
            shift = np.random.randint(-50, 50)
            eeg = np.roll(eeg, shift, axis=-1)
        
        if np.random.rand() > 0.5:
            # Add Gaussian noise (SNR ~20dB)
            noise_level = np.std(eeg) * 0.1
            eeg = eeg + np.random.randn(*eeg.shape) * noise_level
        
        if np.random.rand() > 0.5:
            # Channel dropout (randomly zero out 1-2 channels)
            n_drop = np.random.randint(1, 3)
            channels = np.random.choice(eeg.shape[0], n_drop, replace=False)
            eeg[channels] = 0
        
        return eeg
    
    def __getitem__(self, idx):
        eeg = self.data[idx].copy()
        
        if self.augment:
            eeg = self._apply_augmentation(eeg)
        
        # Band-pass filter (common: 0.5-45 Hz for motor imagery)
        from scipy.signal import butter, filtfilt
        b, a = butter(4, [0.5/(self.fs/2), 45/(self.fs/2)], btype='band')
        eeg = filtfilt(b, a, eeg, axis=-1)
        
        # Transform to image
        if self.transform == 'spectrogram':
            img = eeg_to_spectrogram(eeg, fs=self.fs)
        elif self.transform == 'topomap' and self.electrode_names:
            img = eeg_epoch_to_topomap_sequence(eeg, self.electrode_names)
        else:
            img = eeg_to_spectrogram(eeg, fs=self.fs)
        
        # Normalize
        img = (img - img.mean()) / (img.std() + 1e-8)
        img = torch.tensor(img, dtype=torch.float32).unsqueeze(0)
        
        return img, torch.tensor(self.labels[idx], dtype=torch.long)
    
    def __len__(self):
        return len(self.data)

# Usage
train_dataset = EEGDataset('data/train.h5', transform='spectrogram', augment=True)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, num_workers=4)
```

### 4.2 Cross-Validation Setup (交叉验证)

```python
from sklearn.model_selection import StratifiedKFold

def cross_validate_eeg(data_path, n_folds=5, seed=42):
    """Subject-wise or trial-wise cross-validation for EEG."""
    
    dataset = EEGDataset(data_path, transform='spectrogram')
    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=seed)
    
    fold_results = []
    for fold, (train_idx, val_idx) in enumerate(skf.split(dataset.data, dataset.labels)):
        print(f"--- Fold {fold+1}/{n_folds} ---")
        
        # Train/val split
        train_data = torch.utils.data.Subset(dataset, train_idx)
        val_data = torch.utils.data.Subset(dataset, val_idx)
        
        train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
        val_loader = DataLoader(val_data, batch_size=32)
        
        # Initialize model
        model = AAE(input_channels=1, latent_dim=64, n_classes=4)
        trainer = AAETrainer(model)
        
        # Train
        best_acc = 0
        for epoch in range(50):
            model.train()
            for imgs, labels in train_loader:
                losses = trainer.train_step(imgs, labels)
            
            # Validate
            model.eval()
            correct = 0
            total = 0
            with torch.no_grad():
                for imgs, labels in val_loader:
                    _, _, logits = model(imgs.to(trainer.device))
                    preds = logits.argmax(dim=1)
                    correct += (preds.cpu() == labels).sum().item()
                    total += labels.shape[0]
            
            acc = correct / total
            best_acc = max(best_acc, acc)
        
        fold_results.append(best_acc)
        print(f"  Best accuracy: {best_acc:.4f}")
    
    print(f"\nMean accuracy: {np.mean(fold_results):.4f} ± {np.std(fold_results):.4f}")
    return fold_results
```

### 4.3 Inference & Visualization

```python
def visualize_latent_space(model, dataloader, method='tsne'):
    """Visualize the learned latent space."""
    from sklearn.manifold import TSNE
    import matplotlib.pyplot as plt
    
    model.eval()
    all_z, all_labels = [], []
    
    with torch.no_grad():
        for imgs, labels in dataloader:
            z, _ = model.encoder(imgs.to(model.device))
            all_z.append(z.cpu().numpy())
            all_labels.append(labels.numpy())
    
    all_z = np.concatenate(all_z)
    all_labels = np.concatenate(all_labels)
    
    # Dimensionality reduction
    if method == 'tsne':
        reducer = TSNE(n_components=2, perplexity=30, random_state=42)
    elif method == 'umap':
        import umap
        reducer = umap.UMAP(n_components=2, random_state=42)
    
    z_2d = reducer.fit_transform(all_z)
    
    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    classes = np.unique(all_labels)
    for cls in classes:
        mask = all_labels == cls
        ax.scatter(z_2d[mask, 0], z_2d[mask, 1], 
                   label=f'Class {cls}', alpha=0.6, s=50)
    ax.legend()
    ax.set_title('AAE Latent Space Visualization')
    plt.tight_layout()
    return fig
```

---

## 5. Activation Keywords (激活关键词)

### English Keywords
```
eeg-classification, adversarial-autoencoder, aae, cnn-eeg, 
brain-computer-interface, bci, motor-imagery, erp, ssvep,
spectrogram, topographic-map, scalp-map, eeg-image,
latent-space, adversarial-regularization, gmm-prior,
domain-adaptation, cross-subject, transfer-learning,
mne-python, neurodsp, pytorch, time-frequency,
eeg-preprocessing, artifact-removal, ica-eeg,
few-shot-eeg, self-supervised-eeg, contrastive-learning
```

### Chinese Keywords (中文关键词)
```
脑电图分类, 对抗自编码器, 卷积神经网络脑电, 脑机接口,
运动想象, 事件相关电位, 稳态视觉诱发电位,
频谱图, 地形图, 头皮地图, 脑电图像,
潜在空间, 对抗正则化, 高斯混合先验,
域适应, 跨被试, 迁移学习,
时间频率分析, 脑电预处理, 伪影去除, 独立成分分析,
少样本脑电, 自监督学习, 对比学习
```

---

## 6. Pitfalls & Mitigations (常见陷阱与应对策略)

### 6.1 Overfitting (过拟合)

| Symptom | Cause | Mitigation |
|---------|-------|------------|
| Train acc >> Val acc | Too few trials per subject | Use AAE adversarial regularization; data augmentation |
| Model memorizes noise | High model capacity | Dropout (0.3-0.5); weight decay (1e-5); early stopping |
| Latent collapse | Weak discriminator | Increase discriminator capacity; use WGAN-GP loss |
| Spectrogram overfitting | Too large nperseg | Reduce window size; use multi-scale spectrograms |

```python
# Anti-overfitting checklist
anti_overfit = {
    'dropout': 0.3,           # Dropout after every conv block
    'weight_decay': 1e-5,     # L2 regularization
    'label_smoothing': 0.1,   # Soften targets
    'early_stop_patience': 10,# Stop if val loss doesn't improve
    'data_augmentation': True,# Time shift, noise, channel dropout
    'spectral_augmentation':  # Frequency masking (SpecAugment-style)
        lambda x: mask_freq_bands(x, mask_ratio=0.15),
}
```

### 6.2 Domain Shift (域偏移)

| Type | Description | Solution |
|------|-------------|----------|
| Cross-subject | Different electrode impedances, skull thickness | Domain adversarial training (DANN); CORAL alignment |
| Cross-session | Day-to-day variability, fatigue | Batch normalization statistics update; test-time adaptation |
| Cross-device | Different EEG amplifiers, sampling rates | Harmonization; style transfer in latent space |
| Cross-task | MI vs. ERP paradigms | Multi-task learning; shared encoder with task-specific heads |

```python
class DomainAdversarialAAE(AAE):
    """AAE with domain adversarial training for cross-subject generalization."""
    
    def __init__(self, input_channels=1, latent_dim=64, n_classes=4, n_domains=10):
        super().__init__(input_channels, latent_dim, n_classes)
        
        # Domain classifier (gradient reversal)
        self.domain_classifier = nn.Sequential(
            GradientReversalLayer(alpha=1.0),
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Linear(64, n_domains),
        )
    
    def forward(self, x, domain_labels=None):
        z, features = self.encode(x)
        x_recon = self.decode(z)
        class_logits = self.classifier(z)
        domain_logits = self.domain_classifier(z)
        return z, x_recon, class_logits, domain_logits
```

### 6.3 Artifact Contamination (伪影污染)

| Artifact | Source | Detection | Removal |
|----------|--------|-----------|---------|
| Ocular (EOG) | Eye blinks, movements | High amplitude frontal channels | ICA; regression; AAE reconstruction |
| Muscular (EMG) | Jaw clenching, tension | High-frequency content (>30 Hz) | Low-pass filter; wavelet thresholding |
| Cardiac (ECG) | Heartbeat | Periodic ~1 Hz pattern | Template subtraction; ICA |
| Line noise | 50/60 Hz electrical | Sharp spectral peak | Notch filter; adaptive filtering |
| Electrode pop | Poor contact | Sudden step-change | Interpolation; channel rejection |

```python
def detect_and_remove_artifacts(eeg_data, fs=256, eog_channels=None):
    """
    Multi-stage artifact detection and removal pipeline.
    Returns cleaned EEG and artifact mask.
    """
    from mne.preprocessing import ICA
    import mne
    
    # 1. High-pass filter (remove slow drifts)
    from scipy.signal import butter, filtfilt
    b, a = butter(4, 0.5/(fs/2), btype='high')
    eeg_clean = filtfilt(b, a, eeg_data, axis=-1)
    
    # 2. Notch filter (line noise)
    b_notch, a_notch = scipy.signal.iirnotch(50.0, 30.0, fs)
    eeg_clean = filtfilt(b_notch, a_notch, eeg_clean, axis=-1)
    
    # 3. Artifact detection via amplitude threshold
    threshold = np.median(np.abs(eeg_clean)) * 5
    artifact_mask = np.abs(eeg_clean) > threshold
    
    # 4. AAE-based denoising (uses reconstruction as implicit denoiser)
    # Feed through trained AAE; reconstruction removes non-typical patterns
    # eeg_denoised = aae_denoise(eeg_clean, model)
    
    return eeg_clean, artifact_mask
```

### 6.4 Additional Pitfalls

| Pitfall | Description | Fix |
|---------|-------------|-----|
| Information leakage | Train/test trials from same continuous recording | Strict epoch separation; subject-wise split |
| Class imbalance | Some classes have far fewer trials | Weighted loss; oversampling; focal loss |
| Spectrogram resolution | Wrong window size misses key frequency bands | Use multiple window sizes; validate on domain knowledge |
| Ignoring phase info | Spectrograms lose phase information | Use complex-valued CNN; add phase as separate channel |
| Non-stationarity | EEG statistics change over time | Sliding window normalization; adaptive batch norm |

---

## 7. Related BCI/EEG Skills (相关脑机接口/脑电图技能)

| Skill | Description | Connection |
|-------|-------------|------------|
| `eeg-preprocessing` | MNE-based preprocessing, ICA, filtering | Prerequisite: clean data before CNN input |
| `signal-processing` | FFT, wavelet, STFT, filter design | Core: spectrogram generation |
| `time-series-analysis` | Temporal patterns, sequence modeling | Complementary: RNN/Transformer for raw EEG |
| `computer-vision` | CNN architectures, data augmentation | Core: image-based EEG classification |
| `generative-models` | VAEs, GANs, diffusion models | Core: AAE is a generative approach |
| `domain-adaptation` | CORAL, DANN, MMD alignment | Critical: cross-subject generalization |
| `self-supervised-learning` | Contrastive learning, masked modeling | Extension: pre-training on unlabeled EEG |
| `csp-features` | Common Spatial Patterns for motor imagery | Alternative: handcrafted features vs. CNN |
| `eeg-spatial-filtering` | Laplacian, surface Laplacian, source localization | Enhancement: improve signal-to-noise ratio |
| `transfer-learning-eeg` | Pre-trained models for EEG | Extension: leverage large EEG corpora |

---

## Quick Start Checklist

```
☐ 1. Preprocess EEG: filter (0.5-45Hz), remove artifacts (ICA), re-reference
☐ 2. Segment into epochs: e.g., [-0.5s, 2.5s] relative to cue
☐ 3. Transform to image: spectrogram (STFT/CWT) or topographic maps
☐ 4. Build CNN encoder/decoder: 4 conv blocks + adaptive pooling
☐ 5. Add AAE discriminator: 2-3 FC layers, BCE loss
☐ 6. Train with 3 phases: reconstruction → discriminator → generator
☐ 7. Validate: cross-subject or cross-session split (NOT random trial split!)
☐ 8. Visualize: t-SNE/UMAP of latent space; check class separation
☐ 9. Deploy: optimize for real-time (quantization, TensorRT)
☐ 10. Monitor: track BCI accuracy over time for drift detection
```

## References

1. Makhzani et al. (2015). "Adversarial Autoencoders." arXiv:1511.05644.
2. Schirrmeister et al. (2017). "Deep Learning with Convolutional Neural Networks for EEG Decoding." Human Brain Mapping.
3. Roy et al. (2019). "EEG-based Brain-Computer Interfaces using Deep Learning: A Review." IEEE T-NSRE.
4. Craik et al. (2019). "Deep Learning-Based Electroencephalography Analysis: A Systematic Review." Journal of Neural Engineering.
5. Lotte et al. (2018). "A Review of Classification Algorithms for EEG-based BCIs." Journal of Neural Engineering.
