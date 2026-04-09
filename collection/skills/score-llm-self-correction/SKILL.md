# SCoRe: Self-Correction via Reinforcement Learning

## Description

SCoRe (Self-Correction via Reinforcement Learning) is a multi-turn online RL approach that significantly improves LLM self-correction using entirely self-generated data. Addresses the failure of supervised fine-tuning (SFT) approaches which suffer from distribution mismatch and behavior collapse.

**Key Innovation:**
- Multi-turn online RL for self-correction
- No need for external models or supervision
- Addresses SFT failure modes (distribution mismatch, behavior collapse)
- 15.6% improvement on MATH, 9.1% on HumanEval

## Tools Used

- read: Load model responses
- write: Save correction traces
- exec: Run RL training
- browser: Access evaluation benchmarks
- memory_search: Retrieve correction patterns

## Instructions for Agents

### Self-Correction Pipeline

1. Generate initial response
2. Identify potential errors
3. Generate correction
4. Evaluate correction quality
5. Update via RL

### Key Challenges

1. **Distribution Mismatch** - SFT data ≠ model's own mistakes
2. **Behavior Collapse** - Learning ineffective correction modes

## Overview

**Source:** arXiv:2409.12917v2
**Utility:** 0.92
**Authors:** Google DeepMind

## Activation Keywords

- SCoRe
- LLM self-correction
- reinforcement learning self-correction
- behavior collapse
- multi-turn RL

---

## Problem: Why SFT Fails

### SFT Failure Modes

```python
# SFT on offline correction traces
def sft_training(model, correction_data):
    for prompt, mistake, correction in correction_data:
        # Problem 1: Distribution mismatch
        # mistake is from another model, not current model
        loss = model.loss(prompt, correction)
        loss.backward()
    
    # Problem 2: Behavior collapse
    # Model learns to mimic corrections without understanding
```

### Distribution Mismatch

```
SFT Data Collection Model:
"I think the answer is 5." → [Correction: "Actually, it's 7..."]

Current Model:
"I believe it's 8." → ???
(Mistake patterns differ!)
```

### Behavior Collapse

```
Effective Self-Correction:
1. Identify error
2. Explain what went wrong
3. Provide correct reasoning
4. Give final answer

Collapsed Behavior (SFT):
"Actually, [some template]" → Doesn't actually correct
```

---

## SCoRe Solution

### Two-Stage Training

```python
class SCoRe:
    def __init__(self, model, reward_fn):
        self.model = model
        self.reward = reward_fn
    
    def train(self, prompts, num_iterations=1000):
        # Stage 1: Initialize policy to avoid collapse
        self.stage1_train(prompts)
        
        # Stage 2: Amplify self-correction
        self.stage2_train(prompts)
    
    def stage1_train(self, prompts):
        """Multi-turn RL to get good initialization"""
        for iteration in range(num_iterations // 2):
            for prompt in prompts:
                # Generate initial response
                response1 = self.model.generate(prompt)
                reward1 = self.reward(response1)
                
                # Generate correction
                response2 = self.model.generate(
                    prompt + response1 + "Wait, let me reconsider..."
                )
                reward2 = self.reward(response2)
                
                # RL update
                self.update_policy(reward1, reward2)
    
    def stage2_train(self, prompts):
        """Amplify self-correction with reward bonus"""
        for iteration in range(num_iterations // 2):
            for prompt in prompts:
                response1 = self.model.generate(prompt)
                response2 = self.model.generate_correction(prompt, response1)
                
                # Reward bonus for successful correction
                correction_bonus = self.reward_bonus(response1, response2)
                
                total_reward = self.reward(response2) + correction_bonus
                self.update_policy(total_reward)
```

---

## Implementation Details

### Multi-Turn RL

```python
class MultiTurnRL:
    def __init__(self, model, kl_coef=0.1):
        self.model = model
        self.reference_model = copy.deepcopy(model)  # For KL penalty
        self.kl_coef = kl_coef
    
    def generate_turn(self, context, temperature=1.0):
        return self.model.generate(context, temperature=temperature)
    
    def compute_reward(self, response, ground_truth):
        # Task-specific reward
        accuracy = check_correctness(response, ground_truth)
        return accuracy
    
    def compute_advantage(self, rewards, values):
        returns = compute_returns(rewards)
        advantages = returns - values
        return advantages
    
    def update(self, trajectories):
        for traj in trajectories:
            # Compute advantages
            advantages = self.compute_advantage(
                traj.rewards, traj.values
            )
            
            # PPO-style update with KL penalty
            ratio = self.model.prob(traj.actions) / traj.old_probs
            kl = self.kl_divergence(self.model, self.reference_model)
            
            loss = -advantages * ratio + self.kl_coef * kl
            loss.backward()
```

---

## Training Pipeline

### Stage 1: Policy Initialization

```python
def stage1_initialization(model, train_prompts, val_prompts):
    """
    Goal: Prevent behavior collapse
    - Train on model's own distribution
    - Use regularization to prevent collapse
    """
    for epoch in range(num_epochs):
        # Generate self-correction traces
        traces = []
        for prompt in train_prompts:
            # Model's own mistakes
            response1 = model.generate(prompt)
            
            # Model's own corrections
            correction = model.generate(
                f"{prompt}\n{response1}\nWait, let me reconsider:"
            )
            
            traces.append((prompt, response1, correction))
        
        # RL update on self-generated data
        rl_update(model, traces)
        
        # Validate
        if not check_collapse(model, val_prompts):
            break
    
    return model
```

### Stage 2: Amplify Self-Correction

```python
def stage2_amplify(model, train_prompts):
    """
    Goal: Strengthen correction behavior
    - Reward bonus for successful corrections
    - Continue multi-turn RL
    """
    for epoch in range(num_epochs):
        for prompt in train_prompts:
            # Generate and evaluate
            response1 = model.generate(prompt)
            reward1 = evaluate(response1)
            
            correction = model.generate_correction(prompt, response1)
            reward2 = evaluate(correction)
            
            # Bonus for correction improvement
            if reward2 > reward1:
                bonus = reward2 - reward1
            else:
                bonus = 0
            
            # Update with bonus
            update_with_bonus(model, correction, reward2 + bonus)
    
    return model
```

---

## Results

| Model | Benchmark | Improvement |
|-------|-----------|-------------|
| Gemini 1.0 Pro + SCoRe | MATH | +15.6% |
| Gemini 1.5 Flash + SCoRe | MATH | +9.1% |
| Gemini 1.0 Pro + SCoRe | HumanEval | +15.6% |
| Gemini 1.5 Flash + SCoRe | HumanEval | +9.1% |

---

## Comparison with Other Methods

| Method | External Model | Self-Generated | Collapse Risk |
|--------|----------------|----------------|---------------|
| SFT on corrections | Required | No | High |
| Multiple models | Required | No | Medium |
| SCoRe | **Not needed** | **Yes** | **Low** |

---

## Best Practices

1. **Use model's own distribution** - Don't use external correction traces
2. **Regularize appropriately** - KL penalty prevents collapse
3. **Two-stage training** - Initialize properly, then amplify
4. **Reward shaping** - Bonus for successful corrections
5. **Validate during training** - Check for behavior collapse

---

## Applications

| Domain | Use Case |
|--------|----------|
| Math Reasoning | Correct calculation errors |
| Code Generation | Fix bugs in generated code |
| Question Answering | Refine incorrect answers |
| General Reasoning | Improve multi-step reasoning |

---

## Examples

### Example 1: Basic Application

**User:** I need to apply SCoRe: Self-Correction via Reinforcement Learning to my analysis.

**Agent:** I'll help you apply score-llm-self-correction. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for score-llm-self-correction?

**Agent:** Let me search for the latest research and best practices...

## References

- Paper: https://arxiv.org/abs/2409.12917
- DOI: https://doi.org/10.48550/arXiv.2409.12917
- Authors: Google DeepMind

---

**Created:** 2026-03-28
**Source:** arXiv:2409.12917v2 - "Training Language Models to Self-Correct via RL"