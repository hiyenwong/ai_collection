---
name: compiler-world-model-tensor-optimization
description: World-model-inspired evaluator for tensor program optimization. Models schedule evaluation as action-conditioned latent dynamics over program states.
version: 1.0
created: 2026-06-10
source: arXiv 2606.09312v1
tags: [compiler, tensor-program, world-model, optimization, TVM, auto-scheduler]
---

# Compiler World Models for Tensor Program Optimization

World-model-inspired evaluator that models schedule evaluation as action-conditioned latent dynamics, achieving significant efficiency gains over traditional auto-schedulers.

## Key Innovation

Unlike traditional auto-schedulers that evaluate candidates as static code snapshots, this approach:
- Models schedule evaluation as action-conditioned latent dynamics
- Captures the schedule trajectory that produced each candidate
- Makes evaluation sensitive to action dependencies

## Architecture

### Latent Dynamics Model
```python
class CompilerWorldModel:
    def __init__(self, latent_dim, transition_model):
        self.latent_state = None
        self.transition = transition_model
    
    def rollout_schedule(self, initial_program, scheduling_actions):
        # Start from initial program latent state
        z = self.encode_program(initial_program)
        
        # Roll out actions in latent space
        for action in scheduling_actions:
            z = self.transition(z, action)  # Lightweight transition
        
        return z  # Final dynamic representation
```

### Action-Conditioned Transition
```python
class ScheduleTransitionModel(nn.Module):
    def forward(self, latent_state, action):
        # Lightweight latent transition (no AST mutation)
        delta = self.action_encoder(action)
        new_state = latent_state + delta
        return new_state
```

### Candidate Ranking
```python
def rank_candidates(world_model, programs, actions, hardware_features):
    scores = []
    for program, action_seq in zip(programs, actions):
        # Get latent representation
        latent = world_model.rollout_schedule(program, action_seq)
        
        # Combine with action + hardware features
        score = world_model.rank(latent, action_seq, hardware_features)
        scores.append(score)
    
    return sorted(zip(programs, scores), key=lambda x: x[1])
```

## Results (TVM AutoScheduler)

- **GPU**: 1.37x improvement in representative-subgraph latency over Ansor
- **CPU**: 1.54x improvement
- Matches Ansor-10K within 2.2% geometric mean using 10x fewer measurements
- PyTorch inference: 4.61x / 3.67x geometric mean speedup

## Integration with TVM

```python
def optimize_with_world_model(auto_scheduler, world_model, tensor_program):
    # Generate candidate schedules
    candidates = auto_scheduler.generate_candidates(tensor_program)
    
    # Use world model for efficient evaluation
    ranked = rank_candidates(
        world_model,
        candidates['programs'],
        candidates['actions'],
        hardware_features
    )
    
    # Select best without expensive measurement
    best_schedule = ranked[0]
    return best_schedule
```

## When to Use

- Tensor program optimization (TVM, MLIR, XLA)
- When measurement budget is limited
- GPU/CPU kernel scheduling
- Auto-scheduler integration

## Activation Triggers

- `tensor program optimization`, `world model compiler`, `TVM auto-scheduler`, `schedule evaluation`, `latent dynamics compilation`

## References

- arXiv:2606.09312v1 - Pan et al., "Toward Compiler World Models"
- TVM AutoScheduler (Ansor)
- World models in reinforcement learning