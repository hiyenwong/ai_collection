---
name: vector-policy-optimization
description: "Vector Policy Optimization (VPO) methodology for training language models to produce diverse, high-entropy response distributions that improve test-time search performance"
category: machine-learning
---

# Vector Policy Optimization (VPO)

## Description
Methodology for training language models using Vector Policy Optimization (VPO), which optimizes for response diversity rather than a single scalar reward. Enables models to produce high-entropy distributions that improve test-time search procedures like AlphaEvolve.

## Activation Keywords
- vector policy optimization
- VPO training
- test-time search
- diversity training LLM
- 向量策略优化
- inference scaling
- response diversity

## Tools Used
- exec: Run training scripts
- search_files: Find related training code
- write: Create VPO implementations

## Core Concepts

### Test-Time Search
Modern LLMs are used inside inference-scaling search procedures that generate multiple rollouts and select the best using task-specific reward functions. Standard post-training optimizes for a single scalar reward, leading to low-entropy responses that hurt search performance.

### Vector Policy Optimization
Instead of optimizing a scalar reward, VPO trains models to handle a variety of task-specific reward functions simultaneously. The model learns to produce diverse responses that cover multiple solution strategies.

### Diversity-Performance Tradeoff
There is a fundamental tradeoff between response quality (expected reward) and diversity (entropy). VPO finds the optimal balance for search-augmented inference.

## Mathematical Framework

### Standard RLHF Objective
$$\max_\pi \mathbb{E}_{x \sim \mathcal{D}, y \sim \pi(\cdot|x)}[r(x, y)] - \beta \text{KL}(\pi || \pi_{ref})$$

### VPO Objective
$$\max_\pi \mathbb{E}_{x \sim \mathcal{D}}[\sum_i w_i \mathbb{E}_{y \sim \pi(\cdot|x)}[r_i(x, y)]] - \beta H(\pi(\cdot|x))$$
where $r_i$ are multiple reward functions and $H$ is entropy regularization.

## Usage Patterns

### Pattern 1: Training for Search
1. Define diverse reward functions for target task
2. Construct VPO training objective with multiple rewards
3. Train model with entropy regularization
4. Evaluate test-time search performance

### Pattern 2: Diversity Evaluation
1. Measure response entropy on test queries
2. Compare search improvement over scalar-trained baseline
3. Analyze coverage of solution strategies

## Instructions for Agents

### Step 1: Define Reward Ensemble
Collect or construct multiple reward functions that represent different aspects of task quality.

### Step 2: Set Up VPO Training
```python
# Pseudocode for VPO training loop
for batch in data:
    for reward_fn in reward_functions:
        rewards = reward_fn(batch, model_outputs)
        loss += weighted_reward_loss(rewards)
    loss -= beta * entropy(model_outputs)
    loss.backward()
    optimizer.step()
```

### Step 3: Evaluate Search Performance
Use the trained model inside a test-time search procedure. Measure improvement over baselines.

### Step 4: Tune Diversity Parameter
Adjust entropy regularization strength $\beta$ to find optimal diversity-quality tradeoff.

## Error Handling

### Low Diversity Output
If model still produces low-entropy responses:
- Increase entropy regularization $\beta$
- Use more diverse reward functions
- Add explicit diversity bonus

### Training Instability
If VPO training diverges:
- Reduce learning rate
- Use gradient clipping
- Apply trust region constraints

## Resources
- arXiv: 2605.22817 - "Vector Policy Optimization: Training for Diversity Improves Test-Time Search"
- GRPO/DPO training methodologies
- AlphaEvolve and inference-scaling search

## Related Skills
- gaussian-grpo
- local-rl-alignment-engineering
- fine-tuning-with-trl