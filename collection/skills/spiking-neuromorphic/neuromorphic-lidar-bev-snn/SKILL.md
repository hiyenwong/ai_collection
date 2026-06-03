---
name: neuromorphic-lidar-bev-snn
version: "1.0"
description: "End-to-end Spiking Neural Network for 3D LiDAR-based Bird's Eye View object detection in autonomous driving, with neuromorphic energy analysis and learned spike encoding."
triggers:
  - neuromorphic lidar
  - spiking neural network object detection
  - bird eye view SNN autonomous driving
  - LiDAR point cloud spiking
  - neuromorphic perception autonomous vehicle
  - energy efficient 3D detection SNN
  - spike encoding LiDAR BEV
  - surrogate gradient 3D detection
source: "arXiv:2605.25293"
authors: ["Sambit Mohapatra", "Senthil Yogamani", "Heinrich Gotzig", "Patrick Mader"]
---

# Neuromorphic LiDAR-based Bird's Eye View Object Detection using SNNs

## Overview

First end-to-end Spiking Neural Network for **3D LiDAR-based BEV object detection** in autonomous driving. Demonstrates that complex real-world 3D perception is achievable with sparse event-driven computation, achieving **3.33× synaptic energy reduction** over equivalent CNNs while matching competitive AP on the KITTI benchmark.

**Key Results (KITTI benchmark, IoU=0.5)**:
- Membrane potential variant: 92.05/87.04/86.51 AP (Easy/Moderate/Hard)
- Fully binary variant: direct neuromorphic deployment ready
- 3.33× energy reduction in synaptic operations vs. CNN baseline

## Core Architecture

### Spiking Encoder-Decoder for BEV
- **Input**: LiDAR point cloud → Bird's Eye View representation (2D projection + height features)
- **Architecture**: Encoder-decoder (U-Net style) with LIF neurons
- **Two variants**:
  1. **Membrane potential (MP) variant**: reads continuous V_mem at output → maximum accuracy
  2. **Fully binary (FB) variant**: all layers output binary spikes → direct neuromorphic hardware deployment

### Input Spike Encoding Strategies (Ranked by Performance)
1. **Learned encoding** 🏆 — let network learn optimal spike representation from data (best)
2. **Z-axis encoding** — encode LiDAR height information as spike timing
3. **Latency encoding** — first-spike timing proportional to intensity
4. **Poisson encoding** — random Poisson spike trains proportional to feature magnitude

**Key Finding**: Learned encoding significantly outperforms all hand-crafted methods. Let the network learn its own spike representations.

## Methodology

### BEV Representation Pipeline
```python
def lidar_to_bev(point_cloud, grid_res=0.16, max_height=4.0, n_height_bins=4):
    """
    Convert LiDAR point cloud to Bird's Eye View feature map
    
    Args:
        point_cloud: (N, 4) array [x, y, z, intensity]
        grid_res: grid resolution in meters
        n_height_bins: number of height channels
    
    Returns:
        bev_map: (H, W, C) feature map where C = n_height_bins + density
    """
    # Discretize x-y plane
    x_idx = ((point_cloud[:, 0] - x_min) / grid_res).int()
    y_idx = ((point_cloud[:, 1] - y_min) / grid_res).int()
    
    # Encode height and density per cell
    bev_map = create_height_density_features(point_cloud, x_idx, y_idx, n_height_bins)
    return bev_map
```

### Spiking Encoder-Decoder
```python
import spikingjelly.activation_based as sj

class SpikingBEVDetector(nn.Module):
    def __init__(self, in_channels, n_classes, T=4):
        super().__init__()
        self.T = T  # timesteps
        
        # Learned spike encoding (outperforms Poisson/latency/z-axis)
        self.spike_encoder = sj.layer.Conv2d(in_channels, 32, 3, padding=1)
        self.encoder_lif = sj.neuron.LIFNode(tau=2.0)
        
        # Encoder backbone
        self.encoder = nn.ModuleList([
            SpikingConvBlock(32, 64),
            SpikingConvBlock(64, 128),
            SpikingConvBlock(128, 256),
        ])
        
        # Decoder with skip connections
        self.decoder = nn.ModuleList([
            SpikingUpBlock(256, 128),
            SpikingUpBlock(128, 64),
            SpikingUpBlock(64, 32),
        ])
        
        # Detection head
        # MP variant: read V_mem continuously
        # FB variant: read spike outputs only
        self.det_head = DetectionHead(32, n_classes)
    
    def forward(self, bev_input):
        sj.functional.reset_net(self)
        
        outputs = []
        for t in range(self.T):
            # Present BEV input repeatedly across timesteps
            spikes = self.spike_encoder(bev_input)
            spikes = self.encoder_lif(spikes)
            
            # Encoder
            enc_features = []
            x = spikes
            for enc_block in self.encoder:
                x = enc_block(x)
                enc_features.append(x)
            
            # Decoder
            for i, dec_block in enumerate(self.decoder):
                x = dec_block(x, enc_features[-(i+1)])
            
            outputs.append(self.det_head(x))
        
        # Aggregate over timesteps (mean for MP, vote for FB)
        return torch.stack(outputs).mean(0)
```

### Energy Analysis Model
```python
def compute_snn_energy(model, input_data, mac_energy_pJ=0.1):
    """
    Estimate SNN energy via SynOps/MAC proxy
    SynOps = number of spike-triggered synaptic operations
    """
    total_synops = 0
    total_macs = 0
    
    for layer in model.modules():
        if isinstance(layer, sj.neuron.LIFNode):
            spike_rate = layer.spike_count / (layer.total_ops * T)
            synops = spike_rate * layer.total_ops
            total_synops += synops
            total_macs += layer.total_ops
    
    snn_energy = total_synops * mac_energy_pJ
    ann_energy = total_macs * mac_energy_pJ
    
    energy_reduction = ann_energy / snn_energy
    return snn_energy, energy_reduction
```

## Training Details

- **Dataset**: KITTI 3D Object Detection benchmark (cars)
- **Training**: Surrogate gradient backpropagation through time (BPTT)
- **Temporal input**: BEV features presented repeatedly across T timesteps (sequential frames unavailable in KITTI — a known limitation)
- **Timesteps**: T=4 (balance accuracy vs. latency)
- **Surrogate**: Piecewise linear (arctangent) for ∂S/∂U

## Key Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Spike encoding | Learned | Outperforms Poisson/latency/z-axis on all metrics |
| Output reading | Membrane potential OR spike | MP→accuracy, spike→hardware deployment |
| Temporal proxy | Repeat BEV across timesteps | KITTI lacks sequential frames |
| Training | Surrogate gradient BPTT | End-to-end, no complex conversion |

## Limitations & Future Work

1. **Static input repetition**: KITTI lacks temporal sequences; BEV is repeated across timesteps rather than processing genuine video
2. **Energy model is conservative**: Real neuromorphic hardware gains may be higher than 3.33×
3. **Single class (cars)**: Multi-class detection not yet evaluated

## Applications

- Autonomous vehicles with neuromorphic co-processors (Intel Loihi 2, BrainScaleS)
- Drone-based aerial object detection with strict power budgets
- Smart infrastructure LiDAR processing on edge devices
- Robotics perception with battery-powered platforms

## Why This Matters

This work extends SNN applicability **beyond classification** into complex 3D spatial reasoning tasks. The combination of learned spike encoding + membrane potential readout + surrogate gradients shows that the "accuracy gap" between SNNs and ANNs in perception tasks is closable, enabling a genuine path to neuromorphic deployment in safety-critical autonomous systems.
