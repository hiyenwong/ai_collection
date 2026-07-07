---
name: uncertainty-aware-llm-guided-policy-shaping
description: Uncertainty-aware LLM-guided policy shaping for sparse-reward RL using A* oracle trajectories and entropy-based blending with MC dropout uncertainty estimation.
authors:
  - Ujjwal Bhatta
  - Utsabi Dangol
  - Sumaly Bajracharya
date: 2026-06-04
arxiv: 2606.06673v1
tags:
  - RL
  - LLM-guided
  - uncertainty-aware
  - sparse-reward
  - policy-shaping
---

# Uncertainty-Aware LLM-Guided Policy Shaping (ULPS)

## Overview

Framework integrating calibrated LLM into RL training loop for structured, uncertainty-modulated behavioral guidance in sparse-reward environments. Combines A* oracle trajectories, BERT-based language model, MC dropout uncertainty, and entropy-based blending.

## Key Innovation

**Three-Component Integration:**
1. **A* Oracle**: Synthesize optimal symbolic trajectories
2. **Calibrated LLM**: Fine-tuned BERT provides action suggestions
3. **Uncertainty-Aware Blending**: MC dropout + entropy mechanism adaptively balances LLM vs. learned policy

**Results (MiniGridUnlockPickup):**
- >9% improvement in execution accuracy after fine-tuning
- Fewer environment interactions
- Higher reward AUC

## Methodology

### Phase 1: Oracle Trajectory Synthesis

```
# A* search for optimal symbolic trajectory
def synthesize_oracle_trajectory(env, goal):
    symbolic_states = abstract(env.state)
    trajectory = A_star_search(symbolic_states, goal)
    return trajectory  # Sequence of symbolic actions
```

### Phase 2: LLM Fine-Tuning

```
# Use oracle trajectories as training data
oracle_dataset = {(state, action) for all synthesized trajectories}

# Fine-tune BERT-based language model
LLM_policy = fine_tune(
    model=BERT_base,
    data=oracle_dataset,
    task=action_prediction
)
```

### Phase 3: Uncertainty Estimation

```
# Monte Carlo dropout for epistemic uncertainty
def estimate_uncertainty(LLM, state, n_samples=10):
    predictions = []
    for i in range(n_samples):
        # Enable dropout during inference
        pred = LLM(state, dropout_active=True)
        predictions.append(pred)
    
    # Epistemic uncertainty: variance across predictions
    uncertainty = variance(predictions)
    return uncertainty
```

### Phase 4: Entropy-Based Blending

```
# Adaptive blending between LLM guidance and learned policy
def blended_action(state, LLM, learned_policy):
    # LLM suggestion and uncertainty
    llm_action = LLM(state)
    llm_uncertainty = estimate_uncertainty(LLM, state)
    
    # Learned policy action
    policy_action = learned_policy(state)
    
    # Entropy-based blending weight
    # Low uncertainty → trust LLM
    # High uncertainty → trust learned policy
    blend_weight = f(llm_uncertainty)  # Monotonically decreasing
    
    # Combine actions
    final_action = blend(
        llm_action, 
        policy_action, 
        weight=blend_weight
    )
    return final_action
```

### Phase 5: PPO Training Loop

```
for episode in training:
    state = env.reset()
    while not done:
        # Get blended action
        action = blended_action(state, LLM, PPO_policy)
        
        # Execute action
        next_state, reward, done = env.step(action)
        
        # Store transition for PPO
        store_transition(state, action, reward)
        
        state = next_state
    
    # PPO policy update
    PPO_policy.update(transitions)
```

## Reusable Patterns

### Pattern 1: A* Oracle Trajectory Synthesis
**Use when:** Sparse-reward environment with symbolic abstraction
**Steps:**
1. Abstract state space (discrete symbolic representation)
2. Run A* search from initial to goal
3. Convert symbolic trajectory to action sequence
4. Use as expert demonstration for fine-tuning

### Pattern 2: Calibrated LLM Policy Guidance
**Use when:** Language model provides behavioral priors
**Implementation:**
- Fine-tune LLM on oracle/synthetic trajectories
- LLM outputs action suggestions given state description
- Use as "soft expert" in RL loop

### Pattern 3: MC Dropout Uncertainty for RL
**Use when:** Need to estimate reliability of LLM suggestions
**Technique:**
- Enable dropout during inference (non-standard)
- Sample multiple predictions (n=10-20 typical)
- Variance = epistemic uncertainty
- Use to modulate guidance strength

### Pattern 4: Entropy-Based Guidance Blending
**Use when:** Balancing learned policy vs. external guidance
**Mechanism:**
- Low uncertainty → high LLM weight (reliable prior)
- High uncertainty → high learned policy weight (LLM unreliable)
- Smooth transition via entropy-based weighting function

### Pattern 5: Symbolic Trajectory + Language Prior Integration
**Use when:** Combining symbolic planning with language models
**Pipeline:**
- A* provides optimal symbolic plan
- LLM learns to predict actions from symbolic states
- RL policy learns from blended supervision
- Uncertainty controls blending dynamics

## Implementation Considerations

### MiniGridUnlockPickup Benchmark
- Sparse rewards (success/failure only)
- Multi-step task sequences
- Partial observability (ULPS handles this)
- Demonstrated improvements: 9% accuracy, fewer interactions, higher reward AUC

### LLM Choice
- Paper uses BERT-based model
- Alternative: Transformer decoder, any sequence model
- Key: Fine-tune on symbolic state→action pairs

### Uncertainty Thresholds
- High uncertainty (e.g., > threshold): Full learned policy control
- Low uncertainty (e.g., < threshold): Strong LLM guidance
- Intermediate: Proportional blending

### Entropy Function Design
- Monotonically decreasing with uncertainty
- Smooth transition (sigmoid, exponential decay)
- Preserve adaptability (never fully suppress either source)

### Training Dynamics
- Early training: High LLM weight (prior guidance crucial)
- Later training: Learned policy takes over as it improves
- Uncertainty adapts blending throughout

## Extensions

### Partially Observable Settings
- ULPS demonstrated extensibility to partial observability
- LLM can reason over partial information
- Uncertainty captures observation gaps

### Multi-Agent RL
- Each agent with own LLM guidance
- Shared uncertainty estimation
- Coordinated blending across agents

### Transfer Learning
- Pre-train LLM on diverse oracle trajectories
- Transfer to new environments with same symbolic abstraction

### Other Benchmarks
- Extend beyond MiniGrid
- Apply to navigation, manipulation, dialogue

## Pitfalls

1. **A* Scalability**: Large symbolic spaces → slow oracle synthesis
2. **LLM Calibration Quality**: Poor fine-tuning → unreliable suggestions
3. **MC Dropout Sampling Cost**: n=10 samples → 10x forward passes
4. **Symbolic Abstraction Design**: Poor abstraction → meaningless trajectories
5. **Blend Weight Function**: Wrong weighting → over/under guidance
6. **PPO Stability**: Blending can destabilize PPO convergence if weights change abruptly

## Related Methods

- Behavioral cloning (BC)
- Learning from demonstrations (LfD)
- Policy distillation
- Reward shaping
- Curriculum learning
- Uncertainty estimation in deep learning

## Code Availability

Implementation details in paper, MiniGridUnlockPickup results documented

## Applications

- Sparse-reward RL environments
- Multi-task RL with heterogeneous sequences
- Partially observable settings
- Environments with symbolic state abstraction
- Real-time decision-making with language priors

## Activation Keywords

`ULPS`, `uncertainty-aware LLM`, `LLM-guided RL`, `sparse-reward RL`, `policy shaping`, `A* oracle`, `MC dropout uncertainty`, `entropy-based blending`, `MiniGrid`, `symbolic trajectory synthesis`, `calibrated language model`, `PPO integration`, `epistemic uncertainty`