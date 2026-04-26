---
name: neuromorphic-continual-nuclear-ics
description: "SNN-based anomaly detection with continual learning for nuclear industrial control systems. Spike-encoded asynchronous sensor fusion with delta-based encoding achieving 92.7% input sparsity. Activation: neuromorphic, anomaly detection, nuclear ICS, continual learning, SNN, industrial control"
---

# Neuromorphic Continual Learning for Nuclear ICS

> First spiking neural network-based anomaly detection system with continual learning for nuclear industrial control systems, using spike-encoded asynchronous sensor fusion with 92.7% input sparsity and 12.6x fewer operations than ANN.

## Metadata
- **Source**: arXiv:2604.18611
- **Authors**: Samrendra Roy, Sajedul Talukder, Syed Bahauddin Alam
- **Published**: 2026-04-13
- **Categories**: cs.NE, cs.AI, cs.LG

## Core Methodology

### Key Innovation
Nuclear ICS monitoring faces two critical challenges:
1. **Catastrophic forgetting**: ANNs forget previous anomaly patterns when trained on new subsystems
2. **Energy efficiency**: Continuous monitoring requires low-power solutions

This work presents the first SNN-based solution with:
- Spike-encoded asynchronous sensor fusion for heterogeneous data
- Continual learning strategies for sequential subsystem deployment
- 12.6x fewer operations than equivalent ANN (estimated 2.5x energy savings)

### Technical Framework

#### Spike-Encoded Asynchronous Sensor Fusion
- **Delta-based encoding**: Converts continuous sensor streams to sparse spike trains
- **Rate-adaptive**: Spike rates match each sensor's natural dynamics
- **Input sparsity**: 92.7% sparsity achieved

#### Continual Learning Strategies
Evaluated five approaches:
1. Sequential fine-tuning (baseline)
2. Elastic Weight Consolidation (EWC)
3. Synaptic Intelligence (SI)
4. Experience Replay
5. **Hybrid EWC+Replay** (best performance)

#### SNN Architecture
- Leaky Integrate-and-Fire (LIF) neurons
- Event-driven computation
- Compatible with neuromorphic hardware (e.g., Intel Loihi)

## Implementation Guide

### Prerequisites
- SNN framework (snnTorch, SpykeTorch, or CARLsim)
- Nuclear ICS dataset (e.g., HAI 21.03)
- Neuromorphic hardware (optional, for deployment)
- Python 3.8+, PyTorch

### Step-by-Step

1. **Delta-Based Spike Encoding**
   ```python
   class DeltaModulator:
       """Converts sensor data to spike trains"""
       def __init__(self, threshold, min_interval):
           self.threshold = threshold
           self.min_interval = min_interval
           self.last_spike_time = {}
           self.last_value = {}
       
       def encode(self, sensor_id, value, timestamp):
           if sensor_id not in self.last_value:
               self.last_value[sensor_id] = value
               return 0
           
           delta = abs(value - self.last_value[sensor_id])
           time_since_spike = timestamp - self.last_spike_time.get(sensor_id, 0)
           
           if delta > self.threshold and time_since_spike > self.min_interval:
               self.last_spike_time[sensor_id] = timestamp
               self.last_value[sensor_id] = value
               return 1  # spike
           return 0  # no spike
   ```

2. **Asynchronous Fusion**
   ```python
   def asynchronous_fusion(sensor_streams, delta_modulators):
       """Fuse spikes from heterogeneous sensors at their natural rates"""
       fused_events = []
       for sensor_id, stream in sensor_streams.items():
           modulator = delta_modulators[sensor_id]
           for timestamp, value in stream:
               spike = modulator.encode(sensor_id, value, timestamp)
               if spike:
                   fused_events.append((timestamp, sensor_id, value))
       return sorted(fused_events)  # chronologically sorted
   ```

3. **Continual Learning Setup**
   ```python
   class NuclearSNNWithContinualLearning:
       def __init__(self, ewc_lambda=1.0, replay_buffer_size=1000):
           self.model = SNNClassifier(...)
           self.ewc = EWCLoss(self.model, lambda_=ewc_lambda)
           self.replay_buffer = ReplayBuffer(replay_buffer_size)
       
       def train_task(self, task_data, task_id):
           # Combine current task with replay
           replay_data = self.replay_buffer.sample()
           combined_data = merge(task_data, replay_data)
           
           for batch in combined_data:
               # Standard SNN loss
               classification_loss = self.model.compute_loss(batch)
               
               # EWC penalty for important weights
               ewc_loss = self.ewc.penalty(self.model)
               
               total_loss = classification_loss + ewc_loss
               total_loss.backward()
               optimizer.step()
           
           # Update EWC importance after task
           self.ewc.update_importance(task_data)
           
           # Store samples for replay
           self.replay_buffer.store(task_data)
   ```

4. **Evaluation Pipeline**
   - Train on subsystem 1 (boiler)
   - Evaluate forgetting on subsystem 1
   - Train on subsystem 2 (turbine)
   - Evaluate on both subsystems
   - Continue sequentially

### Performance Results

#### Accuracy Metrics
- **Average F1**: 0.979
- **Average Forgetting (AF)**: 0.000 (single seed), 0.035 ± 0.039 (3 seeds)
- **Attack Detection**: All tested attacks detected
- **Mean Latency**: < detection threshold

#### Efficiency Metrics
- **Operations**: 12.6x fewer than ANN
- **Estimated Energy**: 2.5x better (based on published hardware specs)
- **Input Sparsity**: 92.7%

## Applications
- Nuclear power plant monitoring
- Industrial control system security
- Multi-subsystem anomaly detection
- Energy-constrained edge AI
- Safety-critical continual learning

## Pitfalls
- EWC+Replay requires additional memory for replay buffer
- Delta modulator thresholds need sensor-specific tuning
- SNN training slower than ANN on conventional hardware
- Real neuromorphic hardware deployment requires platform-specific optimization
- Catastrophic forgetting not completely eliminated (small AF remains)

## Related Skills
- isi-cv-gradient-free-continual-learning-snn
- neuromorphic-parameter-estimation-power-converter
- continual-learning-fmri-brain-disorder
- cps-security-anomaly-detection

## References
- Paper: https://arxiv.org/abs/2604.18611
- Dataset: HAI 21.03 Nuclear ICS Security Dataset
