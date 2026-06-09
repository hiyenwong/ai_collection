---
name: ulps-uncertainty-aware-llm-policy-shaping
description: Uncertainty-Aware LLM-Guided Policy Shaping for sparse-reward RL. Integrates calibrated LLM into RL training loop with uncertainty-modulated behavioral guidance.
version: 1.0
created: 2026-06-10
source: arXiv 2606.06673v1
tags: [RL, LLM, policy-shaping, uncertainty, sparse-reward, PPO]
---

# ULPS: Uncertainty-Aware LLM-Guided Policy Shaping

Methodology for integrating Large Language Models into Reinforcement Learning training loops with uncertainty-modulated behavioral guidance for sparse-reward domains.

## Key Concepts

1. **A*-Based Oracle**: Synthesize optimal symbolic trajectories for fine-tuning language model
2. **Monte Carlo Dropout Uncertainty**: Estimate epistemic uncertainty for action suggestions
3. **Entropy-Based Blending**: Adaptively balance LLM guidance vs learned policy
4. **PPO Integration**: Work with Proximal Policy Optimization base policy

## When to Use

- Sparse reward environments (MiniGrid, grid-world tasks)
- Multi-task RL with heterogeneous task sequences
- Partially observable settings
- When exploration is inefficient with vanilla RL

## Core Components

### 1. Symbolic Trajectory Synthesis
```python
# Use A* oracle to generate optimal symbolic trajectories
# These become training data for the LLM guidance model
class AStarOracle:
    def synthesize_trajectory(self, task_spec):
        # Generate symbolic action sequence
        return optimal_actions, path_cost
```

### 2. Uncertainty Estimation
```python
# Monte Carlo dropout for epistemic uncertainty
def estimate_uncertainty(model, state, n_samples=10):
    model.train()  # Enable dropout
    predictions = [model.predict(state) for _ in range(n_samples)]
    variance = np.var(predictions, axis=0)
    return variance  # Epistemic uncertainty
```

### 3. Entropy-Based Blending
```python
# Blend LLM guidance with learned policy based on uncertainty
def blend_policies(llm_action, policy_action, uncertainty, entropy_threshold):
    if uncertainty < entropy_threshold:
        # High confidence in LLM -> prioritize guidance
        return llm_action, alpha=0.8
    else:
        # Low confidence -> rely more on learned policy
        return policy_action, alpha=0.3
```

### 4. Full Training Loop
```python
def ulps_training_loop(env, llm_model, ppo_agent, n_episodes):
    for episode in range(n_episodes):
        state = env.reset()
        while not done:
            # Get LLM suggestion
            llm_action = llm_model.predict_action(state)
            uncertainty = estimate_uncertainty(llm_model, state)
            
            # Get policy action
            policy_action = ppo_agent.act(state)
            
            # Blend based on uncertainty
            action = blend_policies(llm_action, policy_action, uncertainty)
            
            # Execute and update
            next_state, reward, done = env.step(action)
            ppo_agent.update(state, action, reward, next_state)
```

## Results (MiniGridUnlockPickUp)

- +9% improvement in execution accuracy after fine-tuning
- Fewer environment interactions required
- Higher reward AUC vs unguided baselines

## Activation Triggers

- `uncertainty-aware RL`, `LLM-guided policy`, `sparse reward`, `A* oracle RL`, `epistemic uncertainty policy`

## References

- arXiv:2606.06673v1 - Bhatta et al., "Uncertainty-Aware LLM-Guided Policy Shaping for Sparse-Reward Reinforcement Learning"
- MiniGrid benchmark environments
- Monte Carlo dropout uncertainty estimation (Gal & Ghahramani, 2016)