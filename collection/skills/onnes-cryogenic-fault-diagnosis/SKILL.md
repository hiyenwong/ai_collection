---
name: onnes-cryogenic-fault-diagnosis
description: "Multi-agent LLM physics-grounded digital twin simulator for cryogenic fault diagnosis in quantum computing infrastructure. Uses dilution refrigerator forward physics model with learned noise fingerprint + multi-agent LLM operations layer. Activation: cryogenic fault diagnosis, dilution refrigerator, quantum computing infrastructure, digital twin, multi-agent LLM, BlueFors, quantum hardware monitoring"
---

## Onnes: Physics-Grounded Multi-Agent LLM for Cryogenic Fault Diagnosis

**Source**: arXiv:2607.05805
**Title**: Onnes: A Physics-Grounded Multi-Agent LLM Simulator for Cryogenic Fault Diagnosis in Quantum Computing Infrastructure
**Authors**: Praneeth Narisetty, Uday Kumar Reddy Kattamanchi, Shiva Nagendra Babu Kore

## Overview

Dilution refrigerators are the enabling infrastructure of superconducting quantum computers, but their fault diagnosis is dominated by threshold alarms that report "something is wrong" rather than "what is wrong." Onnes presents a physics-grounded digital-twin simulator of a dilution refrigerator that drives a live multi-agent LLM operations layer for cryogenic fault diagnosis.

## Core Methodology

### 1. Physics-Grounded Digital Twin
- **Forward Physics Model**: Dilution refrigerator physics model with real-fridge noise fingerprint
- **Noise Learning**: Correlation fingerprint learned from real BlueFors operational logs
- **Six Fault Classes**: Including three engineered to overlap on temperature but separate on flow and pressure
- **Sim-to-Real Bridge**: Twin validated against real hardware telemetry

### 2. Multi-Agent LLM Operations Layer
- **Zero-Shot LLM Agent Panel**: First attempt at fault diagnosis without examples
- **Contrastive Few-Shot**: Curated demonstrations distinguishing confusable faults
- **Self-Consistency Voting**: Ensemble agreement for confidence scoring
- **Confidence Gate**: Suppresses pre-onset false alarms

### 3. Diagnostic Pipeline

```
1. Physics Twin Simulation
   ├── Forward physics model (dilution cooler dynamics)
   ├── Learned noise fingerprint (BlueFors logs)
   └── Six fault classes (overlapping on temperature, separable on flow/pressure)

2. LLM Agent Diagnosis
   ├── Zero-shot detection (no parameter updates)
   ├── Few-shot classification (6 labeled demonstrations)
   └── Self-consistency voting (ensemble confidence)

3. Continuous Monitoring
   ├── Real-time fault catching (within one poll interval)
   ├── Confidence gate (suppresses pre-onset false alarms)
   └── Sim-to-real validation (6.4% false alarm rate, 100% recall)
```

### 4. Implementation Architecture

```python
class OnnesDiagnoser:
    """Multi-agent LLM cryogenic fault diagnosis."""

    def __init__(self, physics_model, noise_fingerprint, fault_classes):
        self.physics_model = physics_model  # Forward dilution cooler model
        self.noise_fingerprint = noise_fingerprint  # Learned from real BlueFors
        self.fault_classes = fault_classes  # 6 classes (3 confusable on T)
        self.few_shot_demos = []  # Contrastive demonstrations
        self.confidence_threshold = 0.85

    def diagnose(self, telemetry_window):
        """Diagnose fault from telemetry window."""
        # Step 1: Zero-shot detection
        detection = self.zero_shot_detect(telemetry_window)
        if not detection.confident:
            return None  # Confidence gate suppresses

        # Step 2: Classification with few-shot demos
        if self.few_shot_demos:
            classification = self.few_shot_classify(
                telemetry_window, self.few_shot_demos
            )
        else:
            classification = self.zero_shot_classify(telemetry_window)

        # Step 3: Self-consistency voting
        votes = [self.single_agent_vote(telemetry_window) for _ in range(N)]
        consensus = self.majority_vote(votes)

        if consensus.confidence > self.confidence_threshold:
            return consensus
        return None

    def add_contrastive_demo(self, fault_a, fault_b, features):
        """Add demonstration distinguishing confusable faults."""
        self.few_shot_demos.append({
            'fault_a': fault_a,
            'fault_b': fault_b,
            'distinguishing_features': features
        })
```

## Key Results

| Metric | Zero-shot | + Few-shot (6 demos) | Supervised ML |
|--------|-----------|---------------------|---------------|
| Detection Accuracy | No significant difference | — | Baseline |
| Classification Accuracy | 0.685 | **0.990** | 0.985 |
| False Alarm Rate | Backend-dependent | Suppressed by confidence gate | 6.4% |
| Recall | — | 100% (physics faults) | 100% |

## Key Advantages

1. **No parameter updates needed**: 6 labeled demos match supervised classifier
2. **Physics-grounded**: Forward model + real noise fingerprint, not synthetic
3. **Confusable fault resolution**: Temperature-overlapping faults separated by flow/pressure
4. **Continuous monitoring**: Catches every developing fault within one poll interval
5. **Sim-to-real validated**: 6.4% false alarm rate on real BlueFors hardware

## Pitfalls

- Zero-shot LLM trails supervised classifier on classification (0.685 vs 0.985)
- Errors concentrate on confusable faults without few-shot demonstrations
- False alarm rate is backend-dependent (varies by LLM provider)
- Sim-to-real gap: 6.4% false alarm rate on real hardware vs 0% on sim
- Requires real BlueFors telemetry logs for noise fingerprint training
- Only 6 fault classes tested — real systems have more failure modes

## Applications

- Superconducting quantum computer maintenance
- Dilution refrigerator operational monitoring
- Cryogenic system fault detection and classification
- AI-assisted quantum hardware operations
- Predictive maintenance for quantum computing infrastructure

## Related Skills

- `quantum-neural-network-designer`
- `quantum-computing-patterns`
- `digital-twin-multi-agent-consensus`
