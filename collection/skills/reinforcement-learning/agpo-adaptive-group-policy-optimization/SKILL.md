---
name: agpo-adaptive-group-policy-optimization
description: "AGPO (Adaptive Group Policy Optimization) methodology — a critic-free refinement of GRPO that uses group-level statistics to adaptively control update magnitude and exploration. Uses a shared probe-derived statistical state to drive adaptive clipping (based on reward dispersion, skewness, probe entropy, policy entropy, KL drift) and bidirectional adaptive temperature sampling. Outperforms PPO/GRPO on 9 math/STEM benchmarks with Qwen2.5-14B. Use when: improving GRPO training stability, reducing hyperparameter tuning burden in LLM RL post-training, adaptive exploration for reasoning models. Activation: AGPO, adaptive group policy optimization, adaptive clipping GRPO, bidirectional adaptive temperature, critic-free RLVR, statistical feedback control."
---

# AGPO: Adaptive Group Policy Optimization with Dual Statistical Feedback

**Paper**: arXiv:2605.20722 | Submitted: 20 May 2026
**Authors**: Miaobo Hu, Shuhao Hu, Bokun Wang, Ruohan Wang, Xin Wang, Xiaobo Guo, Daren Zha, Jun Xiao

## Core Problem

PPO/GRPO in LLM reasoning training uses **fixed clipping thresholds** and **fixed decoding temperature**, making training brittle and requiring extensive hyperparameter tuning. When reward distributions shift during training (e.g., as the model improves, response quality distribution changes), fixed parameters become suboptimal.

## Key Innovations

### 1. Shared Probe-Driven Statistical State

AGPO uses a **shared probe** (a lightweight model head) that provides group-level statistical signals:

- **Reward dispersion and skewness**: How spread out and asymmetric rewards are within a group
- **Probe vote entropy**: Uncertainty of the probe's evaluations
- **Policy entropy**: How diverse the model's token probabilities are
- **Step-wise KL drift**: How much the policy changes per step

These statistics drive two adaptive controllers.

### 2. Adaptive Clipping

Instead of a fixed ε clip parameter (standard in PPO/GRPO), AGPO sets the **trust-region size dynamically**:

```
epsilon_t = g(reward_dispersion, skewness, probe_entropy, policy_entropy, KL_drift)
```

When uncertainty is high → wider clipping (allow more exploration)
When confidence is high → tighter clipping (conservative learning)

### 3. Bidirectional Adaptive Temperature Sampling

Instead of a fixed decoding temperature, AGPO uses **bidirectional adjustment**:

```
temperature_t = base_temperature + delta * centered_uncertainty
```

- **Heats** (increases temperature) when uncertainty is above a running baseline → more exploration
- **Cools** (decreases temperature) when uncertainty is below baseline → more exploitation
- Centered relative to a running baseline for stability

## Experimental Results

| Model | Benchmark | AGPO | PPO | GRPO |
|-------|-----------|:----:|:---:|:----:|
| Qwen2.5-14B | GSM8K | **67.3%** | - | - |
| Qwen2.5-14B | MATH | **40.5%** | - | - |
| Llama-3-8B | Math avg | **✓** | - | - |
| Gemma-2-9B | Math avg | **✓** | - | - |

- Gains transfer across multiple backbone architectures
- Ablations confirm both adaptive clipping and adaptive temperature are complementary
- Public implementation available

## Relationship to Existing Skills

- [[advantage-collapse-grpo-avspo]] - Addresses GRPO advantage collapse via different mechanism (virtual samples vs statistical adaptation)
- [[gcpo-cooperative-policy-optimization]] - Cooperative GRPO variant addressing exploration collapse
- [[d2evo-dual-difficulty-self-evolution]] - Difficulty-aware sample selection (complementary to AGPO)
- [[delta-discriminative-token-credit-assignment]] - Token-level credit (complementary: AGPO controls group-level dynamics)
- [[gaussian-grpo]] - GRPO improvement via Gaussian modeling

## Implementation Notes

- **Critic-free**: No need for a separate critic network (unlike PPO)
- **Shared probe**: Lightweight head, minimal overhead
- **Running statistics**: Maintain running baseline for temperature centering
- **Complementary to other GRPO improvements**: Can be combined with DelTA, D²Evo, etc.
- Public implementation: see paper for repository link

## Use Cases

1. **LLM Reasoning RL Post-Training**: Direct drop-in for GRPO/PPO
2. **Hyperparameter-Sensitive Training**: Reduces tuning burden for clipping and temperature
3. **Training With Shifting Distributions**: Adapts to changing reward landscape as model improves

## Activation Keywords

AGPO, adaptive group policy optimization, adaptive clipping GRPO, bidirectional adaptive temperature, critic-free RLVR, statistical feedback control, probe-derived statistics, trust-region adaptation, dual statistical feedback, adaptive exploration LLM RL, Qwen2.5 RL training, group-level statistics, reward dispersion clipping, policy entropy adaptation
