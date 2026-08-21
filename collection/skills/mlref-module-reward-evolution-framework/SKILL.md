---
name: mlref-module-reward-evolution-framework
description: "MLREF (Module Level Reward Evolution Framework) for efficient module reuse in reinforcement learning reward design via large language models. Use when designing reward functions for RL that need to evolve across iterations while preserving and reusing effective components."
metadata:
  arxiv_id: "2608.18827"
  authors: "Various Authors"
  published: "2026-08-21"
  tags: [reinforcement-learning, reward-design, module-reuse, LLM, evolution]
license: Complete terms in LICENSE.txt
---

# MLREF: Module Level Reward Evolution Framework

## Overview
MLREF (Module Level Reward Evolution Framework) addresses the bottleneck of reward function design in reinforcement learning by enabling efficient module reuse through large language models. Instead of treating reward functions as monolithic programs, MLREF maintains a persistent module pool of reusable reward components that evolves across iterations.

## Core Components

### Module Pool
- **Persistent repository** of reusable reward components
- Serves as the primary optimization object
- Evolves by accumulating successful modules, refining underperforming ones, and reusing proven components

### Reward Construction
- Reward functions are constructed as **linear combinations of modules** drawn from the pool
- Enables reliable preservation of effective components discovered in earlier iterations
- Provides more stable performance across iterations compared to monolithic approaches

### Evolution Mechanisms
MLREF integrates three key mechanisms to drive module pool evolution:

1. **Reflection-based refinement**: Analyzes module performance and suggests improvements
2. **Hybrid credit assignment**: Distributes credit appropriately across modules
3. **Merge strategy with rollback**: Safely integrates new modules while maintaining stability

## Implementation Workflow

### Step 1: Initialize Module Pool
Create an empty module pool to store reward components:
```python
module_pool = {}
```

### Step 2: Generate Initial Modules
Use LLM to generate initial reward modules based on task description:
```python
# Example prompt for LLM
prompt = f"Generate reward modules for {task_description}. Each module should be a self-contained function that returns a scalar reward component."
modules = llm_generate(prompt)
```

### Step 3: Construct Reward Function
Combine modules from pool into linear combination:
```python
def reward_function(state, action, next_state):
    total_reward = 0
    for module_name, weight in module_weights.items():
        module = module_pool[module_name]
        total_reward += weight * module(state, action, next_state)
    return total_reward
```

### Step 4: Evaluate and Update
After each iteration:
1. Evaluate performance of each module using hybrid credit assignment
2. Apply reflection-based refinement to underperforming modules
3. Add successful new modules to the pool
4. Apply merge strategy with rollback for stability

### Step 5: Optimize Weights
Optimize the linear combination weights using standard RL techniques:
```python
# Use policy gradient or other RL methods to optimize weights
optimize_module_weights(module_pool, trajectories)
```

## Best Practices

### Module Design
- Keep modules **small and focused** on specific aspects of the reward
- Ensure modules are **composable** and can work together effectively
- Design modules to be **interpretable** for easier debugging and refinement

### Pool Management
- **Regularly prune** unused or consistently underperforming modules
- **Version control** important modules to track evolution
- **Monitor diversity** to avoid over-specialization

### Stability Considerations
- Use **conservative learning rates** for weight optimization
- Implement **rollback mechanisms** for unstable updates
- **Validate** new modules on held-out trajectories before full integration

## Performance Benefits
- **25.2% improvement** in locomotion tasks
- **6.6% improvement** in manipulation tasks  
- **More stable optimization dynamics** across iterations

## Activation Keywords
- mlref
- module reward evolution
- reward function design
- reinforcement learning modules
- LLM reward generation

## References
- Original paper: https://arxiv.org/abs/2608.18827
- Related skills: reinforcement-learning, llm-agent-tool-deference-blindness