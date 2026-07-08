---
name: onnes-llm-cryogenic-diagnosis
description: >
  Physics-grounded digital twin + multi-agent LLM methodology for fault diagnosis 
  in critical infrastructure. Uses a forward physics model with learned noise fingerprint 
  to drive LLM agents for diagnostic tasks. Trigger words: fault diagnosis, digital twin, 
  multi-agent LLM, cryogenic, physics-grounded, diagnostic simulator.
---

# Onnes: Physics-Grounded Multi-Agent LLM Simulator for Fault Diagnosis

## Source

- **Paper**: Onnes: A Physics-Grounded Multi-Agent LLM Simulator for Cryogenic Fault Diagnosis in Quantum Computing Infrastructure
- **arXiv**: 2607.05805v1 (2026-07-07)
- **Authors**: Praneeth Narisetty, Uday Kumar Reddy Kattamanchi, Shiva Nagendra Babu Kore
- **Categories**: cs.AI, cs.LG, quant-ph

## Methodology

A unified framework combining physics-based simulation with multi-agent LLM reasoning for infrastructure fault diagnosis.

### Core Architecture

```
┌─────────────────────────────────────────┐
│          Physics-Grounded Twin           │
│  ┌───────────────────────────────────┐  │
│  │ Forward Physics Model             │  │
│  │ + Learned Noise Fingerprint       │  │
│  │ (from real hardware logs)         │  │
│  └───────────────────────────────────┘  │
│                  ↓                       │
│  ┌───────────────────────────────────┐  │
│  │ Fault Classes (physics-grounded)  │  │
│  │ - Some overlap on temperature     │  │
│  │ - Separate on flow/pressure       │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│        Multi-Agent LLM Layer            │
│  ┌─────────────┐ ┌─────────────┐       │
│  │ LLM Agent 1 │ │ LLM Agent 2 │ ...   │
│  └─────────────┘ └─────────────┘       │
│                  ↓                       │
│  Confidence Gate (suppresses             │
│  pre-onset false alarms)                 │
└─────────────────────────────────────────┘
```

### Key Components

1. **Digital Twin Simulator**:
   - Forward physics model of the target system
   - Learned noise-and-correlation fingerprint from real operational logs
   - Physics-grounded fault classes (engineered to be distinguishable)

2. **Multi-Agent LLM Operations Layer**:
   - Zero-shot LLM agent panel for diagnosis
   - Few-shot contrastive demonstrations for confusable faults
   - Self-consistency voting across agents

3. **Confidence Gate**:
   - Suppresses pre-onset false alarms
   - Backend-dependent false alarm rate calibration

### Performance Results

- Zero-shot panel: no significant difference from supervised classifier on detection
- With curated contrastive few-shot demonstrations + self-consistency voting:
  - Classification accuracy: 0.685 → 0.990 (matching supervised classifier at 0.985)
  - Requires only 6 labeled demonstrations, no parameter updates
- Continuous monitoring: catches every developing fault within one poll interval
- Sim-to-real: detector trained on real telemetry achieves 6.4% false-alarm rate, 100% recall

### Implementation Workflow

```python
class PhysicsGroundedTwin:
    def __init__(self, physics_model, noise_fingerprint, fault_classes):
        self.physics = physics_model          # Forward simulation
        self.noise_fp = noise_fingerprint     # Learned from real logs
        self.faults = fault_classes           # Physics-grounded categories
    
    def simulate(self, scenario, fault_type=None):
        """Run physics simulation with optional fault injection."""
        base = self.physics.forward(scenario)
        noise = self.noise_fp.sample()
        if fault_type:
            fault_signal = self.faults.apply(fault_type, base)
            return base + noise + fault_signal
        return base + noise

class LLMDiagnosticAgent:
    def __init__(self, llm, demonstrations=None):
        self.llm = llm
        self.demos = demonstrations or []
    
    def diagnose(self, observation, use_demos=True):
        """Diagnose fault from observation."""
        prompt = self._build_prompt(observation, use_demos)
        return self.llm.generate(prompt)
    
    def self_consistency_vote(self, observation, n_votes=5):
        """Aggregate multiple diagnostic attempts."""
        votes = [self.diagnose(observation) for _ in range(n_votes)]
        return self._majority_vote(votes)

class ConfidenceGate:
    def __init__(self, threshold=0.8):
        self.threshold = threshold
    
    def check(self, diagnosis, confidence):
        """Suppress low-confidence diagnoses."""
        return confidence >= self.threshold
```

### Few-Shot Demonstration Strategy

1. **Contrastive Pairs**: Select examples from confusable fault classes
2. **Minimal Set**: 6 demonstrations sufficient to match supervised baseline
3. **Ablation**: Performance gain attributed almost entirely to demonstrations

### Application Domains

- **Cryogenic systems**: Dilution refrigerator fault diagnosis
- **Industrial IoT**: Equipment failure prediction
- **Medical diagnostics**: Multi-agent symptom analysis
- **Infrastructure monitoring**: Anomaly detection with physics constraints

### Best Practices

1. **Learn noise fingerprint from real data** — do not use synthetic noise alone
2. **Design fault classes to overlap on some dimensions but separate on others**
3. **Use few-shot demonstrations for confusable cases, not all cases**
4. **Implement confidence gating to suppress false alarms**
5. **Validate sim-to-real transfer with held-out real data**

### Activation Keywords

fault diagnosis, digital twin, multi-agent LLM, cryogenic, physics-grounded, diagnostic simulator, noise fingerprint, contrastive demonstrations, confidence gate, self-consistency voting, sim-to-real
