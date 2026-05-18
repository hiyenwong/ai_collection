---
name: neuromorphic-continual-nuclear-ics
description: >
  Skill covering neuromorphic continual learning for anomaly detection in nuclear
  industrial control systems (ICS). Implements spike-based encoding, asynchronous
  sensor fusion, and continual learning strategies (EWC, SI, Replay, Hybrid) for
  sequential deployment of nuclear plant monitoring systems. Based on
  arXiv:2604.18611 by Roy, Talukder & Alam.
triggers:
  - neuromorphic
  - continual learning
  - anomaly detection
  - nuclear
  - SNN
  - spiking neural network
  - ICS
  - industrial control system
  - spike encoding
  - delta encoding
  - sensor fusion
  - catastrophic forgetting
  - EWC
  - elastic weight consolidation
  - synaptic intelligence
  - replay
  - HAI dataset
  - safety-critical
  - energy-efficient inference
  - spike-timing
---

# Neuromorphic Continual Learning for Nuclear ICS

**Paper:** *Neuromorphic Continual Learning for Sequential Deployment of Nuclear Plant Monitoring Systems*
**Authors:** Samrendra Roy, Sajedul Talukder, Syed Bahauddin Alam
**arXiv:** [2604.18611](https://arxiv.org/abs/2604.18611)
**Categories:** cs.NE, cs.AI, cs.LG

---

## 1. Overview

This paper presents the **first Spiking Neural Network (SNN)-based anomaly detection framework with continual learning (CL)** tailored for nuclear Industrial Control Systems (ICS). The key innovation is enabling sequential deployment of monitoring systems across plant subsystems **without catastrophic forgetting**, while leveraging neuromorphic efficiency.

### Why It Matters

- **Nuclear ICS** require anomaly detection that is fast, energy-efficient, and accurate.
- Traditional deep learning models suffer from **catastrophic forgetting** when sequentially trained on new subsystems.
- Neuromorphic hardware (e.g., Intel Loihi, IBM TrueNorth) offers orders-of-magnitude energy savings through **event-driven, spike-based computation**.
- This work bridges neuromorphic computing, continual learning, and safety-critical infrastructure monitoring.

### Key Results

| Metric | Value |
|---|---|
| Best F1 Score (Hybrid EWC+Replay) | **0.979** |
| Input Sparsity (delta encoding) | **92.7%** |
| Forgetting Measure (AF) | **0.000–0.035** |
| Operation Reduction vs. Dense NN | **12.6×** |
| Estimated Energy Savings | **2.5×** |
| Mean Detection Latency | **0.6 s** |
| Dataset | HAI 21.03 (nuclear ICS) |

---

## 2. Core Methodology

### 2.1 Spike Encoding: Delta-Based Encoding

Raw sensor readings are converted to sparse spike trains using **delta-based (threshold-based) encoding**. A spike is generated only when the change in sensor value exceeds a configurable threshold θ.

```
Spike(t) = 1  if |x(t) - x(t-1)| > θ
         = 0  otherwise
```

**Properties:**
- Achieves **92.7% input sparsity**, meaning only ~7.3% of time-steps produce spikes.
- Sparsity directly translates to reduced computation on neuromorphic hardware (no operation when spike = 0).
- The threshold θ is a critical hyperparameter: too low → noise spikes; too high → missed subtle anomalies.

**Implementation sketch:**

```python
import numpy as np

def delta_encode(sensor_stream: np.ndarray, threshold: float) -> np.ndarray:
    """
    Delta-based spike encoding for a 1-D sensor stream.
    
    Args:
        sensor_stream: shape (T,) raw sensor values over T time steps.
        threshold: minimum absolute change to emit a spike.
    
    Returns:
        spikes: shape (T,) binary spike train {0, 1}.
    """
    diff = np.abs(np.diff(sensor_stream, prepend=sensor_stream[0]))
    spikes = (diff > threshold).astype(np.float32)
    return spikes
```

### 2.2 Asynchronous Sensor Fusion

Multiple heterogeneous sensors (temperature, pressure, flow rate, radiation, etc.) are fused at the spike level:

1. Each sensor channel is independently **delta-encoded** into its own spike train.
2. Spike trains are aligned temporally and **concatenated** into a multi-channel spike tensor.
3. The SNN processes spikes **asynchronously** — computation is triggered only by incoming spikes, not by a global clock.

**Advantages over synchronous fusion:**
- No need to wait for the slowest sensor to report.
- Natural handling of **missing or delayed readings** (absence of spikes is meaningful).
- Preserves temporal precision of fast-changing sensors.

```python
def asynchronous_sensor_fusion(sensor_streams: list[np.ndarray],
                               thresholds: list[float]) -> np.ndarray:
    """
    Fuse multiple sensor channels via delta encoding.
    
    Args:
        sensor_streams: list of 1-D arrays, one per sensor channel.
        thresholds: per-channel encoding thresholds.
    
    Returns:
        fused_spikes: shape (T, C) binary spike tensor (time × channels).
    """
    encoded = [delta_encode(s, t) for s, t in zip(sensor_streams, thresholds)]
    return np.stack(encoded, axis=-1)  # (T, C)
```

### 2.3 Spiking Neural Network Architecture

The SNN uses **Leaky Integrate-and-Fire (LIF)** neurons:

**LIF Neuron Dynamics:**

```
τ · du(t)/dt = -u(t) + Σᵢ wᵢ · sᵢ(t)

if u(t) ≥ V_th:
    emit spike;  u(t) → V_reset
```

Where:
- `u(t)` = membrane potential
- `τ` = membrane time constant
- `wᵢ` = synaptic weight from pre-synaptic neuron i
- `sᵢ(t)` = incoming spike from neuron i
- `V_th` = firing threshold
- `V_reset` = reset potential (typically 0)

The network is trained using **Surrogate Gradient Descent** (e.g., ATen sigmoid surrogate) to backpropagate through the non-differentiable spike threshold.

### 2.4 Continual Learning Strategies

The paper evaluates five CL strategies for sequential deployment across plant subsystems (tasks):

#### 1. Sequential Fine-Tuning (Baseline)
- Train on Task A, then continue training on Task B with no regularization.
- **Result:** Severe catastrophic forgetting (high AF).

#### 2. Elastic Weight Consolidation (EWC)
- Adds a quadratic penalty to the loss that anchors important weights to their previously learned values.

```
L_EWC = L_task + (λ / 2) · Σᵢ Fᵢ · (θᵢ - θᵢ*)²
```

Where `Fᵢ` is the Fisher information matrix diagonal for parameter `θᵢ`, and `θᵢ*` is the optimal value after the previous task.

#### 3. Synaptic Intelligence (SI)
- Online measure of parameter importance based on the path integral of parameter changes during training.

```
L_SI = L_task + (λ / 2) · Σᵢ Ωᵢ · (θᵢ - θᵢ_ref)²
```

Where `Ωᵢ` accumulates importance online based on how much each parameter contributed to loss reduction.

#### 4. Replay
- Stores a subset of examples from previous tasks in a memory buffer.
- Interleaves replayed examples with current task training.
- Simple but requires memory proportional to the number of tasks.

#### 5. Hybrid EWC + Replay (Best Performer)
- Combines EWC regularization with replay buffering.
- **Achieves F1 = 0.979, AF = 0.000–0.035** — best balance of accuracy and forgetting prevention.

---

## 3. Implementation Guide

### 3.1 Dependencies

```bash
pip install torch snntorch numpy scikit-learn
```

### 3.2 End-to-End Pipeline

```python
import torch
import torch.nn as nn
import snntorch as snn
from snntorch import surrogate

class NeuromorphicCLDetector(nn.Module):
    """
    SNN-based anomaly detector for nuclear ICS with continual learning.
    """
    def __init__(self, n_inputs: int, n_hidden: int = 128,
                 n_output: int = 2, beta: float = 0.9,
                 threshold: float = 1.0, n_steps: int = 50):
        super().__init__()
        self.n_steps = n_steps
        
        # Surrogate gradient for non-differentiable spike function
        spike_grad = surrogate.sigmoid()
        
        # Network layers
        self.fc1 = nn.Linear(n_inputs, n_hidden)
        self.lif1 = snn.Leaky(beta=beta, threshold=threshold,
                               spike_grad=spike_grad)
        
        self.fc2 = nn.Linear(n_hidden, n_hidden // 2)
        self.lif2 = snn.Leaky(beta=beta, threshold=threshold,
                               spike_grad=spike_grad)
        
        self.fc_out = nn.Linear(n_hidden // 2, n_output)
        self.lif_out = snn.Leaky(beta=beta, threshold=threshold,
                                  spike_grad=spike_grad)
    
    def forward(self, x_spike: torch.Tensor):
        """
        Args:
            x_spike: (batch, n_steps, n_inputs) binary spike tensor.
        Returns:
            mem_out: (batch, n_output) membrane potentials for classification.
        """
        mem1 = self.lif1.init_leaky()
        mem2 = self.lif2.init_leaky()
        mem_out = self.lif_out.init_leaky()
        
        spk_rec = []
        
        for step in range(self.n_steps):
            cur1 = self.fc1(x_spike[:, step, :])
            spk1, mem1 = self.lif1(cur1, mem1)
            
            cur2 = self.fc2(spk1)
            spk2, mem2 = self.lif2(cur2, mem2)
            
            cur_out = self.fc_out(spk2)
            spk_out, mem_out = self.lif_out(cur_out, mem_out)
            
            spk_rec.append(spk_out)
        
        # Aggregate output spikes over time → classification logits
        return torch.stack(spk_rec, dim=0).sum(dim=0)
```

### 3.3 Continual Learning with Hybrid EWC + Replay

```python
import copy

class HybridEWCReplay:
    """
    Hybrid EWC + Replay continual learning handler.
    """
    def __init__(self, model: nn.Module, ewc_lambda: float = 1000.0,
                 replay_capacity: int = 200):
        self.model = model
        self.ewc_lambda = ewc_lambda
        self.replay_capacity = replay_capacity
        self.replay_buffer = []
        
        # EWC state
        self.fisher_matrix = {}
        self.optimal_params = {}
    
    def _compute_fisher(self, dataloader, criterion):
        """Compute diagonal Fisher Information Matrix after task training."""
        fisher = {n: torch.zeros_like(p) for n, p in self.model.named_parameters()
                  if p.requires_grad}
        self.model.eval()
        
        for x, y in dataloader:
            self.model.zero_grad()
            out = self.model(x)
            loss = criterion(out, y)
            loss.backward()
            
            for n, p in self.model.named_parameters():
                if p.requires_grad:
                    fisher[n] += p.grad.data.pow(2)
        
        n_samples = len(dataloader.dataset)
        for n in fisher:
            fisher[n] /= n_samples
        
        return fisher
    
    def update_replay_buffer(self, task_data, task_labels):
        """Reservoir sampling to maintain diverse replay buffer."""
        for x, y in zip(task_data, task_labels):
            if len(self.replay_buffer) < self.replay_capacity:
                self.replay_buffer.append((x, y))
            else:
                idx = np.random.randint(0, self.replay_capacity + 1)
                if idx < self.replay_capacity:
                    self.replay_buffer[idx] = (x, y)
    
    def post_task_update(self, dataloader, criterion):
        """Call after finishing training on a task."""
        self.fisher_matrix = self._compute_fisher(dataloader, criterion)
        self.optimal_params = {n: p.data.clone()
                               for n, p in self.model.named_parameters()
                               if p.requires_grad}
    
    def ewc_penalty(self):
        """Compute EWC regularization loss."""
        penalty = torch.tensor(0.0)
        for n, p in self.model.named_parameters():
            if n in self.fisher_matrix:
                penalty += (self.fisher_matrix[n] *
                            (p - self.optimal_params[n]).pow(2)).sum()
        return self.ewc_lambda * penalty
```

### 3.4 Training Loop for Sequential Tasks

```python
def train_sequential(model, cl_handler, tasks, criterion, optimizer_cls,
                     epochs_per_task=50, replay_ratio=0.3):
    """
    Sequentially train on multiple nuclear subsystem monitoring tasks.
    
    Args:
        tasks: list of (train_loader, val_loader) tuples, one per subsystem.
    """
    for task_id, (train_loader, val_loader) in enumerate(tasks):
        optimizer = optimizer_cls(model.parameters(), lr=1e-3)
        
        # Update replay buffer with current task data
        all_x, all_y = [], []
        for x, y in train_loader:
            all_x.append(x)
            all_y.append(y)
        cl_handler.update_replay_buffer(torch.cat(all_x), torch.cat(all_y))
        
        for epoch in range(epochs_per_task):
            model.train()
            for x_batch, y_batch in train_loader:
                optimizer.zero_grad()
                
                # Current task loss
                out = model(x_batch)
                loss = criterion(out, y_batch)
                
                # EWC regularization (from task 1 onward)
                if task_id > 0:
                    loss = loss + cl_handler.ewc_penalty()
                
                # Replay loss (from task 1 onward)
                if task_id > 0 and len(cl_handler.replay_buffer) > 0:
                    replay_x = torch.stack([r[0] for r in
                                            cl_handler.replay_buffer])
                    replay_y = torch.stack([r[1] for r in
                                            cl_handler.replay_buffer])
                    
                    # Sample replay batch
                    idx = torch.randint(0, len(replay_x),
                                        (int(x_batch.size(0) * replay_ratio),))
                    replay_out = model(replay_x[idx])
                    replay_loss = criterion(replay_out, replay_y[idx])
                    loss = loss + replay_loss
                
                loss.backward()
                optimizer.step()
        
        # Post-task: compute Fisher matrix and store optimal params
        cl_handler.post_task_update(val_loader, criterion)
        print(f"Task {task_id} complete. EWC + Replay updated.")
```

---

## 4. Key Equations

### 4.1 Delta-Based Spike Encoding

```
S(t) = H(|x(t) - x(t-1)| - θ)

where H(·) is the Heaviside step function, θ is the encoding threshold.
```

### 4.2 LIF Neuron Dynamics (Discrete-Time)

```
u[t+1] = β · u[t] + Σᵢ wᵢ · sᵢ[t] - V_th · s_out[t]

s_out[t] = H(u[t] - V_th)

β = exp(-Δt / τ_m)   (decay factor)
```

### 4.3 EWC Regularization

```
L_total = L_task(θ) + (λ_EWC / 2) · Σᵢ F_i^(k) · (θᵢ - θᵢ*^(k))²

F_i^(k) = 𝔼[∂log p(y|x,θ)/∂θᵢ]²   (Fisher information, task k)
```

### 4.4 Synaptic Intelligence (SI) Importance

```
ωᵢ = Σₖ ∫(∂L/∂θᵢ) · dθᵢ   (path integral over training trajectory)

Ωᵢ = ωᵢ / (ε + |θᵢ - θᵢ_init|)   (normalized importance)
```

### 4.5 Forgetting Measure (Average Forgetting — AF)

```
AF_j = (1 / (j-1)) · Σₖ₌₁ʲ⁻¹ max(0, A_{k,j-1}^* - A_{k,j})

where A_{k,t} = accuracy on task k after training task t
      A_{k,j-1}^* = best accuracy on task k before task j
```

### 4.6 Sparsity

```
Sparsity = 1 - (Σ_t Σ_c S[t,c]) / (T × C)

92.7% sparsity means only 7.3% of time-step × channel pairs produce spikes.
```

---

## 5. Evaluation on HAI 21.03 Dataset

### Dataset: HAI (HIL-based Augmented ICS) 21.03

- **Source:** Realistic hardware-in-the-loop nuclear ICS testbed.
- **Signals:** Multi-channel time series from sensors (temperature, pressure, flow, etc.).
- **Labels:** Binary (normal / anomaly) with realistic attack and fault scenarios.
- **Sequential tasks:** Simulates deployment across different plant subsystems (e.g., reactor coolant, steam generation, containment).

### Results Summary

| CL Strategy | F1 Score | AF (Forgetting) | Notes |
|---|---|---|---|
| Sequential Fine-Tuning | Low | High (>0.3) | Catastrophic forgetting |
| EWC | 0.941 | 0.042–0.098 | Good regularization alone |
| SI | 0.928 | 0.055–0.112 | Weaker than EWC for this domain |
| Replay | 0.963 | 0.018–0.055 | Strong but memory-dependent |
| **Hybrid EWC+Replay** | **0.979** | **0.000–0.035** | **Best overall** |

### Efficiency Gains

- **12.6× fewer operations** than dense neural networks (due to 92.7% input sparsity + spike-driven computation).
- **~2.5× energy savings** estimated for neuromorphic hardware deployment (e.g., Loihi 2).
- **0.6 s mean detection latency** — suitable for near-real-time monitoring in nuclear plants.

---

## 6. Pitfalls and Safety Considerations for Critical Infrastructure

### 6.1 Safety-Critical Deployment Pitfalls

| Pitfall | Mitigation |
|---|---|
| **False negatives in anomaly detection** | Use conservative detection thresholds; implement ensemble with traditional rule-based monitors as safety backup |
| **Catastrophic forgetting during updates** | Always use Hybrid EWC+Replay (not fine-tuning alone) when adding new subsystems |
| **Threshold sensitivity in delta encoding** | Cross-validate θ per sensor channel; monitor sparsity and spike rate during deployment |
| **Concept drift in sensor behavior** | Periodically re-evaluate encoding thresholds; implement drift detection on spike statistics |
| **Replay buffer contamination** | Validate replay examples; ensure buffer represents normal operating conditions correctly |
| **Neuromorphic hardware faults** | Redundant computation paths; watchdog timers; graceful degradation to conventional fallback |

### 6.2 Nuclear ICS-Specific Considerations

1. **Regulatory compliance:** Any AI-based monitoring system in nuclear facilities must comply with NRC (Nuclear Regulatory Commission) guidelines. The SNN should be treated as an **advisory** system, not a primary safety system.

2. **Explainability:** Spike-based models are inherently less interpretable than rule-based monitors. Maintain **parallel rule-based anomaly detection** as the primary safety system. The SNN provides supplementary early warning.

3. **Latency bounds:** The 0.6 s mean detection latency is promising, but safety analyses must consider **worst-case latency** (not just mean). Hard real-time guarantees require worst-case analysis on target neuromorphic hardware.

4. **Fail-safe design:** The system must fail **safe** — false alarms are far preferable to missed anomalies. Tune the SNN to favor **high recall** over high precision in nuclear applications.

5. **Validation rigor:** Before deployment, validate against:
   - Known attack scenarios (Stuxnet-like, data injection, sensor spoofing)
   - Normal operational transients (startup, shutdown, load following)
   - Component degradation patterns
   - The full HAI 21.03 benchmark suite

6. **Data provenance:** Ensure training data is **authenticated and untampered**. Adversarial contamination of the replay buffer can degrade all previously learned tasks.

7. **Configuration management:** All encoding thresholds, model weights, Fisher matrices, and replay buffer contents must be under strict configuration control with audit trails.

### 6.3 Continual Learning Risks

- **Replay buffer memory limits:** In long-running deployments with many subsystems, the fixed-capacity replay buffer may not adequately represent all prior tasks. Consider **adaptive buffer management** prioritizing rare-event examples.
- **Fisher matrix staleness:** The Fisher matrix computed after task k may not remain valid as a regularization anchor after many subsequent tasks. Consider **online Fisher updates**.
- **Task boundary detection:** The paper assumes known task boundaries. In real deployment, **automatic task boundary detection** is needed (e.g., change-point detection on sensor statistics).

---

## 7. References

1. **Roy, S., Talukder, S., & Alam, S. B.** (2026). *Neuromorphic Continual Learning for Sequential Deployment of Nuclear Plant Monitoring Systems.* arXiv:2604.18611.
2. **Kirkpatrick, J. et al.** (2017). *Overcoming catastrophic forgetting in neural networks.* PNAS, 114(13), 3521–3526. (EWC)
3. **Zenke, F., Poole, B., & Ganguli, S.** (2017). *Continual learning through synaptic intelligence.* ICML. (SI)
4. **Shin, H. et al.** (2017). *Continual learning with deep generative replay.* NeurIPS. (Replay)
5. **Eshraghian, J. K. et al.** (2023). *Training spiking neural networks using lessons from deep learning.* arXiv. (snntorch / surrogate gradients)
6. **Shin, D. J. et al.** (2021). *HAI 1.19: A hardware-in-the-loop augmented ICS dataset with realistic attacks.* arXiv. (HAI dataset)
7. **Maass, W.** (1997). *Networks of spiking neurons: The third generation of neural network models.* Neural Networks, 10(9), 1659–1671.
8. **Davies, M. et al.** (2018). *Loihi: A neuromorphic manycore processor with on-chip learning.* IEEE Micro, 38(1), 82–99.

---

*Skill created from arXiv:2604.18611 — Neuromorphic Continual Learning for Sequential Deployment of Nuclear Plant Monitoring Systems.*
