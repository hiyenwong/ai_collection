---
name: rl-compositional-reasoning-strategies
category: reinforcement-learning
tags: [rl, reasoning, composition, rl-post-training, strategy-discovery]
source: arXiv:2607.07646v1
authors: Azwar Abdulsalam, Nishil Patel, Andrew Saxe
date: 2026-07-08
---

# RL Post-Training Builds Compositional Reasoning Strategies

Understanding and leveraging how RL composes primitive skills into higher-level reasoning strategies.

## Key Finding

RL post-training does NOT merely amplify primitive skills latent in a base model — it **composes** primitive skills into new higher-level strategies through a phased compositional mechanism.

## Phased Compositional Mechanism

1. **Phase 1**: RL first strengthens primitive reductions already in the base model
2. **Phase 2**: RL discovers valid composed procedures:
   - **Sequential composition**: collapses ordered chains of primitive contractions
   - **Parallel composition**: combines independent primitive contractions in a single step
3. **Phase 3**: Composed procedures are reused and consolidated into a stable repertoire

## Key Insights

- **RL vs Rejection Fine-Tuning (RFT)**: The key difference is selectivity, not exploration volume
  - RFT produces many shortcut-like rewrites, much of them invalid
  - RL concentrates exploration into valid reusable structure
- **Pretraining gates composition**: Compositional strategies emerge not from primitive exposure alone, but from whether pretraining organizes primitive competence into reduction procedures that RL can later compress
- **Base model provides ingredients; RL builds strategies**: Weak procedural ingredients become reliable higher-level strategies through RL

## Practical Implications

- Design pretraining to organize primitive competence into reduction procedures (not just exposure)
- RL post-training with binary final-answer reward can discover composed strategies
- Monitor trace analysis to verify phased composition is occurring
- Rejection fine-tuning alone cannot discover composed strategies (plateaus early)

## Verification

- Analyze solution traces to identify sequential vs parallel compositions
- Compare RL vs RFT on held-out problems requiring composition
- Ablate pretraining to verify composition is gated by reduction procedures
