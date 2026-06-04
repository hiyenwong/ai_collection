---
name: medgym-continuous-time-medical-rl
description: MedGym - Unified continuous-time benchmark for dynamic medical treatment reinforcement learning using Physics-Informed Neural Networks
platforms: [linux, macos, windows]
---

# MedGym: Continuous-Time Medical Treatment RL Benchmark

## Core Methodology

MedGym addresses critical gaps in medical reinforcement learning by providing a **continuous-time** benchmark environment for dynamic treatment recommendation. Key innovations:

### 1. Continuous-Time Framework
- Models patient physiology evolution in continuous time (not discrete MDP/POMDP)
- Handles irregular measurement and intervention intervals
- Captures patient-specific dynamics using Physics-Informed Neural Networks (PINNs)

### 2. Clinical Data Integration
- Constructs configurable RL benchmark from real clinical data
- Supports both offline and online RL evaluation
- Enables comparison between discrete-time and continuous-time methods

### 3. Evaluation Dimensions
- **Personalization**: Patient-specific treatment response
- **Trajectory-level safety**: Safety between consecutive measurement points
- **Model-based offline learning**: Performance gap between offline learning and online deployment

## Implementation Points

### Environment Design
```python
# Continuous-time state evolution
class MedGymEnv:
    def __init__(self, patient_data, config):
        self.pinns_model = PhysicsInformedNN(patient_data)
        self.time_horizon = config.time_horizon
        self.treatment_actions = config.action_space
        
    def step(self, action, time_interval):
        # Continuous-time state transition
        next_state = self.pinns_model.evolve(
            self.current_state, 
            action, 
            time_interval
        )
        reward = self.compute_reward(next_state, action)
        return next_state, reward, done, info
```

### Key Features
1. **Irregular timing handling**: Treatments at arbitrary time points
2. **Patient heterogeneity**: Individualized dynamics models
3. **Safety constraints**: Trajectory-level safety metrics

## Use Cases

- **Dynamic treatment recommendation**: Personalized medication dosing
- **Clinical trial simulation**: Testing RL policies on patient trajectories
- **Offline RL evaluation**: Comparing continuous vs discrete formulations
- **Medical RL research**: Benchmarking new algorithms on realistic medical scenarios

## Activation Keywords

- `medgym`, `continuous-time medical RL`, `medical treatment benchmark`
- `physics-informed neural networks medical`, `dynamic treatment recommendation`
- `patient-specific RL`, `trajectory-level safety medical`
- `offline RL medical`, `irregular measurement RL`

## Related Skills

- [[physics-guided-neural-networks]] - PINNs methodology
- [[offline-rl]], [[model-based-rl]] - RL paradigms
- [[safe-rl]], [[constrained-rl]] - Safety in RL
- [[reinforcement-learning-healthcare]] - Medical RL applications

## Reference

arXiv:2606.01028 - "MedGym: A Unified Continuous-Time Benchmark for Dynamic Medical Treatment Reinforcement Learning" (Wang et al., 2026)