---
name: physics-aware-spiking-har
description: "PAS-Net methodology for Physics-Aware Spiking Neural Networks in energy-efficient wearable IMU-based Human Activity Recognition. Features adaptive symmetric topology mixer and O(1)-memory causal neuromodulator with 98% dynamic energy reduction via early-exit capability. Activation: spiking neural network, human activity recognition, wearable, physics-aware, energy-efficient, IMU"
---

# PAS-Net: Physics-Aware Spiking Neural Network for HAR

> Fully multiplier-free SNN architecture for wearable Human Activity Recognition achieving state-of-the-art accuracy with 98% dynamic energy reduction via confidence-driven early-exit and human-joint physical constraints.

## Metadata
- **Source**: arXiv:2604.10458
- **Authors**: Naichuan Zheng, Hailun Xia, Zepeng Sun, Weiyi Li, Yinzhe Zhou
- **Published**: 2026-04-12
- **Category**: Machine Learning (cs.LG), Human-Computer Interaction (cs.HC)

## Core Methodology

### Key Innovation
PAS-Net bridges the gap between SNNs' energy efficiency and complex biomechanical understanding through three key innovations:

1. **Adaptive Symmetric Topology Mixer (ASTM)**: Enforces human-joint physical constraints spatially
2. **O(1)-Memory Causal Neuromodulator**: Adapts dynamically to non-stationary movement rhythms temporally
3. **Temporal Spike Error Objective**: Enables flexible early-exit for continuous IMU streams

### Technical Framework

#### 1. Spatial: Adaptive Symmetric Topology Mixer (ASTM)
Incorporates human body kinematic constraints into network architecture:
- **Symmetric constraint**: Bilateral body parts share weights
- **Topology constraint**: Adjacent joints interact more strongly
- **Adaptive fusion**: Learnable mixing of constraints

Human body graph representation:
```
Joints: head, neck, shoulders(2), elbows(2), wrists(2), spine, hips(2), knees(2), ankles(2)
Edges: physical connections between joints
```

#### 2. Temporal: O(1)-Memory Causal Neuromodulator
Dynamic threshold adaptation without storing full history:
- **Causal**: Only uses past information
- **O(1) memory**: Fixed-size state, no sequence buffering
- **Neuromodulation**: Adapts firing threshold based on activity

Threshold dynamics:
```
θ(t) = θ_base + α * m(t)
m(t) = β * m(t-1) + (1-β) * activity(t-1)
```
Where `m(t)` is the neuromodulatory state.

#### 3. Early-Exit: Temporal Spike Error Objective
Confidence-driven early termination:
- **Spike error**: Measures prediction uncertainty from spike patterns
- **Confidence threshold**: Exit when confident enough
- **Dynamic energy**: Only process timesteps needed for decision

### Performance Results

| Dataset | Accuracy | Energy Reduction |
|---------|----------|------------------|
| UCI HAR | 96.2% | 85% |
| WISDM | 98.7% | 92% |
| PAMAP2 | 94.5% | 98% |
| Opportunity | 91.3% | 94% |
| SHL | 97.1% | 96% |

**Hardware Implementation**:
- 0.1 pJ per integer accumulation (vs. ~1 pJ for FP16 MAC)
- Fully multiplier-free architecture
- Sparse event-driven computation

## Implementation Guide

### Prerequisites
- IMU sensor data (accelerometer + gyroscope)
- Human body joint configuration
- Spiking neuron framework (spikingjelly, snnTorch)
- Edge device with integer arithmetic support

### Step-by-Step

#### Step 1: Human Body Graph Construction
```python
import torch
import torch.nn as nn

class HumanBodyGraph:
    """
    Graph representation of human body kinematics
    """
    def __init__(self):
        # 15 joints: head, neck, shoulders(2), elbows(2), 
        # wrists(2), spine, hips(2), knees(2), ankles(2)
        self.joints = [
            'head', 'neck', 'L_shoulder', 'R_shoulder',
            'L_elbow', 'R_elbow', 'L_wrist', 'R_wrist',
            'spine', 'L_hip', 'R_hip', 'L_knee', 'R_knee',
            'L_ankle', 'R_ankle'
        ]
        
        # Symmetric pairs (left-right)
        self.symmetric_pairs = [
            ('L_shoulder', 'R_shoulder'),
            ('L_elbow', 'R_elbow'),
            ('L_wrist', 'R_wrist'),
            ('L_hip', 'R_hip'),
            ('L_knee', 'R_knee'),
            ('L_ankle', 'R_ankle'),
        ]
        
        # Physical connections (edges)
        self.connections = [
            ('head', 'neck'), ('neck', 'spine'),
            ('neck', 'L_shoulder'), ('neck', 'R_shoulder'),
            ('L_shoulder', 'L_elbow'), ('L_elbow', 'L_wrist'),
            ('R_shoulder', 'R_elbow'), ('R_elbow', 'R_wrist'),
            ('spine', 'L_hip'), ('spine', 'R_hip'),
            ('L_hip', 'L_knee'), ('L_knee', 'L_ankle'),
            ('R_hip', 'R_knee'), ('R_knee', 'R_ankle'),
        ]
    
    def get_symmetry_matrix(self):
        """
        Returns matrix enforcing symmetric joint weights
        """
        S = torch.eye(len(self.joints))
        for left, right in self.symmetric_pairs:
            i, j = self.joints.index(left), self.joints.index(right)
            S[i, j] = S[j, i] = 0.5  # Share weights
        return S
    
    def get_topology_matrix(self):
        """
        Returns adjacency matrix for physical connections
        """
        A = torch.zeros(len(self.joints), len(self.joints))
        for i, j in self.connections:
            idx_i, idx_j = self.joints.index(i), self.joints.index(j)
            A[idx_i, idx_j] = A[idx_j, idx_i] = 1.0
        return A

# Usage
body_graph = HumanBodyGraph()
symmetry_mat = body_graph.get_symmetry_matrix()
topology_mat = body_graph.get_topology_matrix()
```

#### Step 2: Adaptive Symmetric Topology Mixer (ASTM)
```python
class ASTM(nn.Module):
    """
    Adaptive Symmetric Topology Mixer
    Enforces human-joint physical constraints
    """
    def __init__(self, num_joints, feature_dim):
        super().__init__()
        self.num_joints = num_joints
        self.feature_dim = feature_dim
        
        # Learnable fusion weights
        self.alpha = nn.Parameter(torch.tensor(0.5))
        self.beta = nn.Parameter(torch.tensor(0.5))
        
        # Learnable transformations
        self.W_sym = nn.Linear(feature_dim, feature_dim, bias=False)
        self.W_topo = nn.Linear(feature_dim, feature_dim, bias=False)
        
        # Body graph (can be learned or fixed)
        self.register_buffer('S', self._init_symmetry_matrix())
        self.register_buffer('A', self._init_topology_matrix())
    
    def _init_symmetry_matrix(self):
        # Simplified: all joints symmetric to themselves
        # Full implementation uses HumanBodyGraph
        return torch.eye(self.num_joints)
    
    def _init_topology_matrix(self):
        # Adjacency for connected joints
        A = torch.eye(self.num_joints)
        # Add connections based on body graph
        return A
    
    def forward(self, x):
        """
        x: [batch, num_joints, feature_dim]
        Returns: mixed features respecting physical constraints
        """
        # Symmetric pathway
        x_sym = torch.einsum('ij,bjf->bif', self.S, x)  # [B, J, F]
        x_sym = self.W_sym(x_sym)
        
        # Topology pathway
        x_topo = torch.einsum('ij,bjf->bif', self.A, x)
        x_topo = self.W_topo(x_topo)
        
        # Adaptive fusion
        alpha_sig = torch.sigmoid(self.alpha)
        beta_sig = torch.sigmoid(self.beta)
        
        out = alpha_sig * x_sym + beta_sig * x_topo + \
              (1 - alpha_sig - beta_sig) * x
        
        return out

# Example: Process IMU data
class IMUEncoder(nn.Module):
    def __init__(self, num_imus=6, feature_dim=64):
        super().__init__()
        # Map IMU sensors to body joints
        self.joint_mapping = nn.Linear(num_imus * 6, num_imus * feature_dim)  # 6 = acc(3) + gyro(3)
        self.astm = ASTM(num_imus, feature_dim)
        
    def forward(self, imu_data):
        """
        imu_data: [batch, time, num_imus, 6]
        """
        batch, time, num_imus, feat = imu_data.shape
        
        # Flatten IMU features
        x = imu_data.reshape(batch * time, num_imus, feat)
        x = x.reshape(batch * time, num_imus * feat)
        
        # Project to joint features
        x = self.joint_mapping(x)  # [B*T, num_imus*feature_dim]
        x = x.reshape(batch * time, num_imus, -1)
        
        # Apply physical constraints
        x = self.astm(x)
        
        return x.reshape(batch, time, num_imus, -1)
```

#### Step 3: O(1)-Memory Causal Neuromodulator
```python
class O1CausalNeuromodulator(nn.Module):
    """
    O(1)-Memory Causal Neuromodulator for SNN
    Adapts threshold dynamically with constant memory
    """
    def __init__(self, num_neurons, theta_base=1.0, tau_m=0.9):
        super().__init__()
        self.num_neurons = num_neurons
        self.theta_base = theta_base
        self.tau_m = tau_m  # Neuromodulation time constant
        
        # Learnable modulation parameters
        self.alpha = nn.Parameter(torch.ones(num_neurons) * 0.5)
        self.beta = nn.Parameter(torch.ones(num_neurons) * 0.1)
    
    def forward(self, v, spike, t, state=None):
        """
        v: membrane potential [batch, num_neurons]
        spike: spike output [batch, num_neurons]
        t: current timestep
        state: previous neuromodulatory state (or None for init)
        
        Returns: (adaptive_threshold, new_state)
        """
        batch_size = v.shape[0]
        
        if state is None or t == 0:
            # Initialize state
            m = torch.zeros(batch_size, self.num_neurons, device=v.device)
        else:
            m = state
        
        # Update neuromodulatory state (causal: uses past spike)
        activity = spike.detach()  # Prevent backprop through threshold
        m = self.tau_m * m + (1 - self.tau_m) * activity
        
        # Compute adaptive threshold
        # θ(t) = θ_base + α * tanh(β * m)
        theta_adaptive = self.theta_base + \
                        self.alpha * torch.tanh(self.beta * m)
        
        return theta_adaptive, m

class NeuromodulatedLIF(nn.Module):
    """
    LIF neuron with causal neuromodulation
    """
    def __init__(self, in_features, out_features):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        
        self.linear = nn.Linear(in_features, out_features, bias=False)
        self.tau = nn.Parameter(torch.ones(out_features) * 2.0)
        
        # Neuromodulator
        self.neuromod = O1CausalNeuromodulator(out_features)
        
        # State
        self.v = None
        self.neuro_state = None
        self.t = 0
    
    def forward(self, x):
        """
        x: [batch, in_features]
        Returns: spikes [batch, out_features]
        """
        batch_size = x.shape[0]
        
        if self.v is None or self.v.shape[0] != batch_size:
            self.v = torch.zeros(batch_size, self.out_features, device=x.device)
            self.neuro_state = None
            self.t = 0
        
        # Integrate
        i = self.linear(x)
        self.v = self.v + (i - self.v) / self.tau
        
        # Get adaptive threshold
        prev_spike = (self.v >= self.theta_base).float() if self.t > 0 else torch.zeros_like(self.v)
        theta, self.neuro_state = self.neuromod(
            self.v, prev_spike, self.t, self.neuro_state
        )
        
        # Fire
        spike = (self.v >= theta).float()
        self.v = self.v * (1 - spike)  # Reset
        
        self.t += 1
        
        return spike
    
    def reset(self):
        """Reset states"""
        self.v = None
        self.neuro_state = None
        self.t = 0
```

#### Step 4: Temporal Spike Error for Early Exit
```python
class TemporalSpikeError(nn.Module):
    """
    Confidence measure for early exit based on spike patterns
    """
    def __init__(self, num_classes, confidence_threshold=0.8):
        super().__init__()
        self.num_classes = num_classes
        self.confidence_threshold = confidence_threshold
        
        # Learnable readout
        self.readout = nn.Linear(num_classes * 2, num_classes)
    
    def forward(self, spike_history):
        """
        spike_history: list of spike tensors [batch, num_classes] over time
        Returns: (predictions, confidence, should_exit)
        """
        if len(spike_history) == 0:
            return None, 0.0, False
        
        # Stack history
        spikes = torch.stack(spike_history, dim=1)  # [batch, time, classes]
        
        # Spike count per class
        spike_counts = spikes.sum(dim=1)  # [batch, classes]
        
        # Spike timing (mean time of first spike)
        time_indices = torch.arange(spikes.shape[1], device=spikes.device).float()
        first_spike_time = []
        for b in range(spikes.shape[0]):
            for c in range(self.num_classes):
                spike_times = time_indices[spikes[b, :, c] > 0]
                if len(spike_times) > 0:
                    first_spike_time.append(spike_times[0])
                else:
                    first_spike_time.append(float(spikes.shape[1]))
        first_spike_time = torch.tensor(first_spike_time, device=spikes.device).reshape(spikes.shape[0], -1)
        
        # Concatenate features
        features = torch.cat([spike_counts, first_spike_time], dim=-1)
        
        # Prediction
        logits = self.readout(features)
        probs = F.softmax(logits, dim=-1)
        
        # Confidence = max probability
        confidence, predictions = probs.max(dim=-1)
        
        # Should exit if confident enough
        should_exit = confidence.mean() > self.confidence_threshold
        
        return predictions, confidence, should_exit

class PASNet(nn.Module):
    """
    Full PAS-Net architecture
    """
    def __init__(self, num_joints=15, num_classes=12):
        super().__init__()
        self.encoder = IMUEncoder(num_imus=num_joints)
        self.temporal_snn = nn.ModuleList([
            NeuromodulatedLIF(64, 128),
            NeuromodulatedLIF(128, 256),
            NeuromodulatedLIF(256, num_classes),
        ])
        self.spike_error = TemporalSpikeError(num_classes)
    
    def forward(self, x, max_time=100, early_exit=True):
        """
        x: [batch, time, joints, 6] - IMU data
        Returns: (predictions, actual_time)
        """
        # Encode IMU to joint features
        joint_features = self.encoder(x)  # [batch, time, joints, features]
        
        # Flatten joints
        batch, time, joints, feat = joint_features.shape
        joint_features = joint_features.reshape(batch, time, -1)
        
        # Process with SNN
        spike_history = []
        predictions = None
        
        for t in range(min(time, max_time)):
            x_t = joint_features[:, t, :]
            
            for layer in self.temporal_snn:
                x_t = layer(x_t)
            
            spike_history.append(x_t)
            
            # Check for early exit
            if early_exit and len(spike_history) >= 10:
                pred, conf, exit_now = self.spike_error(spike_history)
                if exit_now:
                    predictions = pred
                    break
        
        if predictions is None:
            predictions, _, _ = self.spike_error(spike_history)
        
        # Reset all layers
        for layer in self.temporal_snn:
            if hasattr(layer, 'reset'):
                layer.reset()
        
        return predictions, len(spike_history)
```

## Applications
- **Fitness wearables**: Real-time activity tracking with extended battery life
- **Healthcare monitoring**: Patient activity detection in hospitals
- **Sports analytics**: Athlete performance monitoring
- **Elderly care**: Fall detection and activity monitoring
- **Industrial safety**: Worker ergonomics and fatigue detection

## Pitfalls
- ASTM requires accurate joint-IMU mapping - miscalibration reduces accuracy
- O(1) neuromodulator parameters need task-specific tuning
- Early-exit threshold trades accuracy vs energy - adjust based on use case
- Continuous IMU streams require online spike encoding
- Hardware-specific optimizations needed for maximum energy savings

## Related Skills
- spike-mllm-multimodal-spiking
- snn-learning-neuromorphic
- wearable-bci-dataset
