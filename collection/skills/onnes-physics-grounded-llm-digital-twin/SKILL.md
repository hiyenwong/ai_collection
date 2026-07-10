---
name: onnes-physics-grounded-llm-digital-twin
description: Onnes methodology — physics-grounded digital twin simulator driving multi-agent LLM operations layer for cryogenic fault diagnosis. Combines forward physics model with learned noise fingerprint, enabling zero-shot fault classification via contrastive few-shot demonstrations and self-consistency voting.
tags: [digital twin, multi-agent systems, LLM, fault diagnosis, quantum computing, cyber-physical systems]
source: arxiv:2607.05805
---

# Onnes: Physics-Grounded Multi-Agent LLM Simulator for Fault Diagnosis

## Core Innovation

Onnes introduces a **physics-grounded digital twin + multi-agent LLM** architecture for fault diagnosis in complex cyber-physical systems (specifically dilution refrigerators for quantum computing):

1. **Physics-Grounded Digital Twin**: Forward physics model + learned real-fridge noise fingerprint
2. **Multi-Agent LLM Panel**: Zero-shot reasoning over physics fault classes
3. **Contrastive Few-Shot Learning**: 6 demonstrations boost classification from 0.685 → 0.990
4. **Confidence Gating**: Suppresses pre-onset false alarms

## System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Physical System                      │
│  (Dilution Refrigerator / BlueFors logs)             │
└────────────────────┬────────────────────────────────┘
                     │ telemetry
┌────────────────────▼────────────────────────────────┐
│           Physics-Grounded Digital Twin              │
│  ┌──────────────┐  ┌──────────────────────────────┐ │
│  │ Forward      │  │ Learned Noise Fingerprint    │ │
│  │ Physics Model│  │ (correlation structure from  │ │
│  │ (cooling     │  │  real operational logs)      │ │
│  │  stages)     │  │                              │ │
│  └──────────────┘  └──────────────────────────────┘ │
│  6 fault classes (3 overlapping on temperature,     │
│  separable on flow/pressure)                        │
└────────────────────┬────────────────────────────────┘
                     │ simulated observations
┌────────────────────▼────────────────────────────────┐
│           Multi-Agent LLM Operations Layer           │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │ Diagnostic   │  │ Physics      │  │ Confidence│ │
│  │ Agent        │  │ Reasoning    │  │ Gate      │ │
│  │              │  │ Agent        │  │           │ │
│  └──────────────┘  └──────────────┘  └───────────┘ │
│  Self-consistency voting + contrastive few-shot     │
└─────────────────────────────────────────────────────┘
```

## Key Technical Components

### 1. Digital Twin Design
```python
class PhysicsGroundedTwin:
    def __init__(self, physics_model, noise_fingerprint):
        self.physics_model = physics_model  # Forward cooling model
        self.noise_fingerprint = noise_fingerprint  # Learned from real logs
        
    def simulate_fault(self, fault_class, seed):
        """
        Generate realistic fault scenarios with physics constraints
        Fault classes:
        - 3 classes overlap on temperature but separate on flow/pressure
        - 3 classes are distinguishable on all channels
        """
        base_signal = self.physics_model.run_normal()
        fault_signal = self.physics_model.inject_fault(fault_class)
        noisy_signal = self.noise_fingerprint.add_correlated_noise(fault_signal)
        return noisy_signal
```

### 2. Multi-Agent LLM Panel
```python
class MultiAgentLLMPanel:
    def __init__(self, agents, voting_threshold=0.7):
        self.agents = agents  # [DiagnosticAgent, PhysicsReasoningAgent, ...]
        self.voting_threshold = voting_threshold
        
    def diagnose(self, observation, demonstrations=None):
        """
        Zero-shot or few-shot fault diagnosis via multi-agent consensus
        """
        votes = []
        for agent in self.agents:
            if demonstrations:
                response = agent.diagnose_with_examples(observation, demonstrations)
            else:
                response = agent.diagnose_zero_shot(observation)
            votes.append(response)
        
        # Self-consistency voting
        consensus = self.weighted_vote(votes)
        confidence = self.compute_confidence(votes)
        
        return consensus, confidence
    
    def confidence_gate(self, confidence, threshold=0.8):
        """Suppress low-confidence predictions (pre-onset false alarms)"""
        return confidence >= threshold
```

### 3. Contrastive Few-Shot Selection
```python
def select_contrastive_demonstrations(fault_classes, n_per_class=1):
    """
    Select demonstrations that maximally separate confusable faults
    Key insight: 6 demonstrations (one per fault class) suffice to 
    raise accuracy from 0.685 to 0.990
    """
    demonstrations = []
    for fault_class in fault_classes:
        # Select example that maximally differs from other classes
        example = select_maximally_contrastive(fault_class, fault_classes)
        demonstrations.append((example, fault_class))
    return demonstrations
```

## Performance Results

| Metric | Zero-Shot | + Few-Shot | Supervised ML |
|--------|-----------|------------|---------------|
| Detection | ✓ (matches) | ✓ | ✓ |
| Classification | 0.685 | **0.990** | 0.985 |
| False Alarm Rate | backend-dependent | suppressed by gate | 6.4% |
| Recall | 100% | 100% | 100% |

**Key Finding**: Contrastive few-shot demonstrations + self-consistency voting match supervised classifier performance with **no parameter updates** and only 6 labeled examples.

## Implementation Pattern for General CPS

### Step 1: Build Physics-Grounded Twin
1. Identify forward physics model of the system
2. Collect operational logs under normal conditions
3. Learn noise/correlation fingerprint from logs
4. Define fault classes with physics-grounded overlap structure

### Step 2: Design Multi-Agent Panel
1. **Diagnostic Agent**: Pattern matching on observed signals
2. **Physics Reasoning Agent**: Causal reasoning from physics principles
3. **Confidence Gate**: Monitors agreement across agents

### Step 3: Deploy with Continuous Monitoring
1. Run twin alongside physical system
2. Agent panel monitors in real-time
3. Confidence gate suppresses pre-onset false alarms
4. Log all predictions for offline improvement

## Activation Triggers

Use this skill when:
- Building fault diagnosis systems for complex CPS
- Need physics-grounded simulation for training/evaluation
- Deploying LLM agents for operational monitoring
- Designing digital twins with bidirectional coupling
- Implementing confidence-gated decision systems

## Pitfalls

1. **Ignoring Noise Correlation**: Real CPS noise is correlated, not i.i.d. — learn the fingerprint
2. **Too Many Fault Classes**: Start with physics-grounded overlap structure, not arbitrary labels
3. **No Confidence Gate**: LLM agents hallucinate — always gate on multi-agent agreement
4. **Overfitting Demonstrations**: Use contrastive selection, not random examples
5. **Sim-to-Real Gap**: Validate twin against real hardware before deploying agents

## References

- "Onnes: A Physics-Grounded Multi-Agent LLM Simulator for Cryogenic Fault Diagnosis in Quantum Computing Infrastructure" arXiv:2607.05805 (2026)