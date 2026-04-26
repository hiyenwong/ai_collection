---
name: eeg-3d-visual-reconstruction
description: EEG-to-3D visual reconstruction framework using diffusion models and EEG foundation models. Maps non-invasive EEG signals to 3D voxel representations, surpassing 2D reconstruction approaches.
---

# EEG-to-3D Visual Reconstruction

## Source
- **Paper:** EEG2Vision3D: A Multimodal EEG-Based Framework for 3D Visual Reconstruction
- **arXiv:** 2604.12685v1
- **Published:** 2026-04-08
- **Categories:** cs.CV, eess.SP, q-bio.NC
- **Authors:** Shao-Yu Tseng, Yu-Cheng Chou, Yi-Chun Chen, Chin-Teng Lin, Kuan-Wen Chen, Yung-Hui Li

## Core Idea

Reconstructs **3D voxel representations** of visual stimuli from non-invasive EEG signals using a modular architecture that combines EEG foundation models with diffusion-based generation. Demonstrates that **3D reconstructions surpass 2D** in visual similarity and information recovery.

## Key Contributions

### 1. EEG2Vision3D Architecture

**Three-Component Pipeline:**
1. **EEG Foundation Model Encoder** (EEG2Rep)
   - Domain-adapters for subject/session variability
   - Extracts robust visual representations

2. **Cross-Modal Projection** (EEGRep2VisRep)
   - Maps EEG representations to visual space
   - Contrastive alignment with image features

3. **3D Diffusion Decoder** (VisRep2Voxel)
   - Generates 3D voxel grids from visual representations
   - Captures depth and spatial structure

### 2. EEG-to-3D Mapping

```python
class EEG2Vision3D(nn.Module):
    def __init__(self, eeg_encoder, projector, diffusion_decoder):
        self.eeg_encoder = EEG2Rep()  # Foundation model
        self.projector = EEGRep2VisRep()  # Cross-modal mapping
        self.decoder = VisRep2Voxel()  # 3D diffusion
    
    def forward(self, eeg_signal):
        eeg_rep = self.eeg_encoder(eeg_signal)
        vis_rep = self.projector(eeg_rep)
        voxel_3d = self.decoder(vis_rep)
        return voxel_3d
```

### 3. Training Strategy

**Stage 1: EEG Encoder Pre-training**
- Self-supervised learning on large EEG corpus
- Domain adapters for individual differences

**Stage 2: Cross-Modal Alignment**
- Contrastive loss between EEG and image features
- Ensures semantic correspondence

**Stage 3: 3D Diffusion Training**
- Conditional diffusion on voxel grids
- Progressive refinement of 3D structure

## Methodology

### EEG Signal Processing

```python
def preprocess_eeg(raw_eeg, sampling_rate=250):
    """Preprocess EEG signals"""
    # Bandpass filter (1-50 Hz)
    filtered = bandpass_filter(raw_eeg, 1, 50, sampling_rate)
    # Remove artifacts (ICA)
    cleaned = ica_artifact_removal(filtered)
    # Epoch into trials
    epochs = epoch_data(cleaned, tmin=-0.2, tmax=1.0)
    return epochs
```

### Cross-Modal Contrastive Learning

```python
def contrastive_loss(eeg_features, image_features, temperature=0.07):
    """InfoNCE contrastive loss for EEG-image alignment"""
    # Normalize features
    eeg_norm = F.normalize(eeg_features, dim=1)
    img_norm = F.normalize(image_features, dim=1)
    
    # Similarity matrix
    sim = eeg_norm @ img_norm.T / temperature
    
    # Labels (positive pairs on diagonal)
    labels = torch.arange(len(eeg_norm))
    
    # Cross-entropy loss
    loss = F.cross_entropy(sim, labels)
    return loss
```

### 3D Diffusion Generation

```python
class VisRep2Voxel(nn.Module):
    def __init__(self, voxel_size=(32, 32, 32)):
        self.unet = UNet3D()
        self.voxel_size = voxel_size
    
    def forward(self, vis_rep, noise=None):
        # Reverse diffusion process
        x = torch.randn(vis_rep.shape[0], 1, *self.voxel_size)
        for t in reversed(range(num_steps)):
            predicted_noise = self.unet(x, t, vis_rep)
            x = denoise_step(x, predicted_noise, t)
        return x
```

## Applications

1. **Brain-Computer Interfaces**
   - Non-invasive visual decoding
   - Communication for locked-in patients

2. **Neuroscience Research**
   - Study visual processing hierarchy
   - Validate computational models

3. **Clinical Applications**
   - Visual function assessment
   - Neurological disorder diagnosis

## Advantages over 2D Reconstruction

| Metric | 2D Reconstruction | 3D Reconstruction |
|--------|-------------------|-------------------|
| Depth Information | Lost | Preserved |
| Spatial Structure | Flat | Volumetric |
| Object Recognition | Moderate | High |
| Visual Similarity | Lower | Higher |

## Implementation Workflow

### Step 1: Data Preparation

```python
# Load EEG dataset
eeg_data = load_eeg_dataset('thalamo')
# Load corresponding 3D stimuli
voxel_data = load_3d_voxels('shapenet')
# Align trials
aligned = align_trials(eeg_data, voxel_data)
```

### Step 2: Train EEG Encoder

```python
# Pre-train with domain adaptation
encoder = EEG2Rep(num_subjects=aligned.num_subjects)
encoder.train_with_adapters(aligned.eeg_signals)
```

### Step 3: Align Modalities

```python
# Contrastive alignment
projector = EEGRep2VisRep()
optimizer = Adam(projector.parameters(), lr=1e-4)
for epoch in range(100):
    eeg_rep = encoder(aligned.eeg_signals)
    img_rep = image_encoder(aligned.images)
    loss = contrastive_loss(eeg_rep, img_rep)
    loss.backward()
    optimizer.step()
```

### Step 4: Train 3D Decoder

```python
# Conditional diffusion training
decoder = VisRep2Voxel()
decoder.train(vis_rep=projector(encoder(eeg_data)),
              target=voxel_data)
```

### Step 5: Generate Reconstructions

```python
# Reconstruct 3D from new EEG
with torch.no_grad():
    voxel_3d = model(new_eeg_signal)
# Render/visualize
render_voxel(voxel_3d)
```

## Related Work

- **EEG2Vision (2D):** Earlier 2D reconstruction framework
- **fMRI-to-Image:** Higher spatial resolution, less portable
- **MEG Decoding:** Better temporal resolution, expensive

## References

- Paper: "EEG2Vision3D: A Multimodal EEG-Based Framework for 3D Visual Reconstruction"
- arXiv: 2604.12685v1
- Published: 2026-04-08
- Categories: cs.CV, eess.SP, q-bio.NC

## Trigger Words

EEG 3D reconstruction, EEG-to-3D, visual reconstruction diffusion, EEG foundation model visual, brain-computer interface 3D, EEG2Vision3D, non-invasive visual decoding, voxel reconstruction EEG, Tseng EEG 3D