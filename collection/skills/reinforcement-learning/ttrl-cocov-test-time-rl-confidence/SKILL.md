---
name: ttrl-cocov-test-time-rl-confidence
description: Test-Time Reinforcement Learning with Confidence-Conditioned Verification (TTRL-CoCoV) methodology for optimizing Pass@k coverage and Pass@1 performance in label-free settings.
---

# TTRL-CoCoV: Test-Time Reinforcement Learning with Confidence-Conditioned Verification

## Core Methodology

TTRL-CoCoV addresses the challenge of optimizing Pass@k (generation coverage) in test-time RL without ground-truth labels. Key insight: **verification capability generally leads generation capability**, enabling a confidence-adaptive framework.

### Three Confidence-Conditioned Mechanisms

1. **High-confidence samples**: Bootstrap verifier + exploration-enhancing reward to prevent diversity collapse
2. **Low-confidence samples**: Delegate pseudo-label selection to verifier to filter incorrect pseudo-labels  
3. **Medium-confidence samples**: Bypass verification entirely

### Verification-Generation Gap

The core insight is that verifiers can reliably evaluate quality even when generators struggle:
- Low-confidence pseudo-labels have high probability of being incorrect
- High-confidence candidates suffer from severe diversity collapse
- Medium-confidence region is most uncertain

## Implementation Details

### Algorithm Components

1. **Confidence Estimation**: Model's own confidence scores on generated samples
2. **Confidence Thresholds**: Three regions (high/medium/low) with calibrated boundaries
3. **Verifier Bootstrapping**: Use high-confidence samples to improve verifier
4. **Exploration Reward**: For high-confidence samples, add diversity bonus
5. **Pseudo-label Filtering**: Verifier selects best candidates for low-confidence samples

### Key Design Decisions

- **Label-free**: No ground truth required during test-time optimization
- **Non-parametric**: Feature-space update direction via dipole preference field
- **Reference Drift**: Frozen base generator provides stability anchor

## Results

- +9.8% average absolute gain in Pass@1 over TTRL
- +18.7% average absolute gain in Pass@16 over TTRL
- +5.0% absolute Pass@1 improvement over fully supervised RL methods on multiple reasoning benchmarks

## Applications

Use when:
- Test-time model adaptation without ground-truth labels
- Improving Pass@k coverage for exploration tasks
- Balancing Pass@1 accuracy vs Pass@k diversity
- Label-free RL for reasoning models

## Trigger Keywords

- test-time RL
- label-free optimization
- Pass@k optimization
- confidence-conditioned verification
- pseudo-label estimation
- diversity collapse prevention

## Related Skills

- [[self-verification]]
- [[confidence-dynamics-early-stop]]
- [[mcts-encoding-discovery-qml]]
- [[reasonmaxxer-entropy-gated-selection]]