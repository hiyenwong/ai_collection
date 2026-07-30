---
name: reinformed-dreamer-asymmetric-world-model
description: Reinforced Dreamer methodology for asymmetric reinforcement learning using latent guidance to improve world model representations and behaviors in model-based RL.
paper_id: "2607.26040"
---

# Reinforced Dreamer: Asymmetric World Model Training with Latent Guidance

## Overview
This methodology addresses limitations in privileged information representations learned by asymmetric model-based reinforcement learning algorithms like Informed Dreamer. It proposes a novel asymmetric representation learning objective using latent guidance, resulting in the Reinforced Dreamer algorithm.

## Key Contributions
- Identifies limitations in privileged information representations in existing asymmetric model-based RL approaches
- Proposes a novel asymmetric representation learning objective using latent guidance
- Demonstrates consistent improvement over standard Dreamer across multiple benchmarks
- Effective under both partial observability (with additional state info) and full observability (with refined state info)

## Implementation Guidelines
1. **World Model Architecture**: Use a standard Dreamer-style world model with observation encoder, transition model, and reward predictor
2. **Asymmetric Learning Setup**: Provide additional supervision beyond rewards during training:
   - Under partial observability: use additional state information
   - Under full observability: use more refined state information
3. **Latent Guidance Objective**: Implement the proposed latent guidance objective to improve privileged information representations
4. **Training Protocol**: Train the asymmetric world model using the latent guidance objective alongside standard RL objectives

## Use Cases
- Model-based reinforcement learning with partial observability
- Scenarios where additional state information is available during training but not deployment
- Applications requiring improved representation learning in world models
- Benchmark environments where standard Dreamer shows inconsistent performance

## Activation Keywords
reinforced dreamer, asymmetric reinforcement learning, latent guidance, world model, model-based RL, privileged information

## References
- arXiv:2607.26040 [cs.LG]
- Original Dreamer paper
- Informed Dreamer methodology