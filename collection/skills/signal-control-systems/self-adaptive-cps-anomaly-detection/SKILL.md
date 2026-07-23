---
name: self-adaptive-cps-anomaly-detection
description: >
  Self-adaptive anomaly detection for autonomous cyber-physical systems.
  Integrates RL-based detector selection, ensemble drift detection,
  and human-in-the-loop retraining with catastrophic forgetting prevention.
---

# Self-Adaptive CPS Anomaly Detection

## Context

Autonomous CPS (connected vehicles, IoT fleets, industrial control systems)
evolve continuously through OTA updates, configuration changes, and workload
shifts. Static diagnostic methods degrade silently when concept drift occurs.
This skill provides a framework for self-adaptive anomaly detection that
combines automated adaptation with operator oversight.

Based on: Weiss et al., "Self-Adaptive Anomaly Detection with Reinforcement
Learning and Human Feedback in Connected Vehicles" (arXiv:2607.08373, 2026)

## Core Architecture

### Three-Coordinated-Mechanism Design

1. **Factorized Deep Q-Network (DQN) with Self-Attention**
   - Selects optimal detector from candidate pool per service
   - Exploits inter-service dependencies in microservice topology
   - Self-attention captures cross-service correlations

2. **Ensemble Drift Detection (Conjunctive Rule)**
   - Three statistical drift detectors run in parallel
   - Alarm raised ONLY when all three concur (precision-first)
   - Reduces false positives in production environments

3. **Human-in-the-Loop Retraining**
   - Pending transition buffer stores flagged transitions
   - 60/40 prioritized replay: 60% new distribution, 40% historical
   - Prevents catastrophic forgetting while adapting to new patterns

## Implementation Patterns

### Pattern 1: Detector Pool Management

```python
# Maintain diverse detector pool for different anomaly types
detectors = {
    "isolation_forest": IsolationForest(),
    "one_class_svm": OneClassSVM(),
    "autoencoder": DeepAutoencoder(),
    "statistical": StatisticalBaseline()
}

# DQN agent selects detector per service
class DetectorSelector(nn.Module):
    def __init__(self, n_services, n_detectors, embed_dim):
        super().__init__()
        self.attention = nn.MultiheadAttention(embed_dim, num_heads=4)
        self.dqn = FactorizedDQN(n_services, n_detectors)

    def forward(self, service_states):
        # Attention over microservice topology
        attended = self.attention(service_states)
        # DQN selects detector per service
        actions = self.dqn(attended)
        return actions
```

### Pattern 2: Conjunctive Drift Detection

```python
def check_drift(current_window, reference_distribution):
    """Conjunctive drift detection -- all must agree."""
    detectors = [
        ks_test(current_window, reference_distribution),
        mmd_test(current_window, reference_distribution),
        pca_drift(current_window, reference_distribution)
    ]
    # Only alarm if ALL detectors agree (precision-first)
    return all(detectors)
```

### Pattern 3: Prioritized Replay for Retraining

```python
def retrain_with_expert_feedback(agent, pending_buffer, historical_buffer):
    """60/40 replay strategy prevents catastrophic forgetting."""
    # 60% from new (pending) distribution
    new_batch = sample(pending_buffer, size=0.6 * batch_size)
    # 40% from historical distribution
    old_batch = sample(historical_buffer, size=0.4 * batch_size)
    combined = merge(new_batch, old_batch)
    agent.update(combined)
```

## Deployment Checklist

- [ ] Define microservice topology graph for attention mechanism
- [ ] Deploy >=3 diverse anomaly detectors in candidate pool
- [ ] Configure drift detection ensemble with conjunctive rule
- [ ] Set up pending transition buffer for flagged events
- [ ] Establish 60/40 replay ratio for retraining
- [ ] Define operator feedback interface for labeling
- [ ] Monitor F1 score degradation after OTA updates

## Pitfalls

- **Single detector deployment**: F1 <= 0.11 vs 0.69 for attention-augmented
- **Disjunctive drift alarm**: Too many false positives; use conjunctive
- **Full replay overwrite**: Causes catastrophic forgetting; use 60/40 split
- **No operator loop**: Black-box adaptation misses domain expertise

## Verification

- F1 score should exceed 0.65 on production microservice testbed
- After OTA update causing concept drift, retraining should recover F1 to
  >= 0.65 on new distribution while maintaining >= 0.65 on prior distribution
- Drift detector false positive rate should be < 5% with conjunctive rule

## Activation

**Keywords**: cps anomaly detection, concept drift, self-adaptive monitoring,
RL detector selection, human-in-the-loop, connected vehicles, microservice
diagnostics, OTA update validation, ensemble drift detection, catastrophic
forgetting prevention, factorized DQN, prioritized replay

**When to use**: When building anomaly detection for evolving CPS, monitoring
microservice health in autonomous systems, handling concept drift from OTA
updates, or designing human-in-the-loop diagnostic systems.
