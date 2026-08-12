---
name: turnsight-turn-level-hindsight-self-distillation
description: Turn-Level Hindsight Self-Distillation framework for Tool-Integrated Reasoning (TIR). Derives supervision from execution-conditioned hindsight with multiple lookahead horizons and cross-horizon directional agreement for reliable credit assignment in long-horizon agentic tasks.
trigger_words:
  - turnsight
  - turn-level hindsight
  - tool-integrated reasoning
  - TIR
  - hindsight self-distillation
---

# TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning

## Overview
TurnSight addresses the limitations of trajectory-level supervision in Tool-Integrated Reasoning (TIR) scenarios by providing turn-level hindsight self-distillation. It derives supervision directly from execution-conditioned hindsight, constructs multiple hindsight views with different lookahead horizons, and selects reliable supervision through cross-horizon directional agreement.

## Key Components

### 1. Execution-Conditioned Hindsight
- Derives supervision directly from states actually visited by the agent during execution
- Avoids reliance on ground-truth answers or retrieved skills that may not reflect actual agent states
- Captures the turn-level structure of tool interactions

### 2. Multi-Horizon Hindsight Views
- Constructs multiple hindsight views with different lookahead horizons
- Enables robust supervision signal selection across different temporal perspectives
- Provides denser signals compared to trajectory-level approaches

### 3. Cross-Horizon Directional Agreement
- Selects reliable supervision through agreement between different horizon views
- Filters out unreliable or inconsistent supervision signals
- Ensures high-quality distillation targets

### 4. Normalized Advantage Modulation
- Normalizes selected hindsight signals across sibling rollouts
- Adaptively modulates RL advantages while preserving original optimization direction
- Maintains stable training dynamics

## Implementation Guidelines

### For Agentic Workflows
1. **Integration Point**: Apply TurnSight during on-policy distillation phases of agentic training
2. **Hindsight Construction**: For each turn in the reasoning trajectory, construct hindsight views with horizons [1, 2, 3, ...] steps ahead
3. **Agreement Filtering**: Compute directional agreement between different horizon views using cosine similarity or correlation metrics
4. **Signal Selection**: Select supervision signals that show high agreement across multiple horizons
5. **Advantage Modulation**: Use normalized hindsight signals to weight RL advantages without changing their sign

### Code Structure
```python
class TurnSightDistillation:
    def __init__(self, horizons=[1, 2, 3], agreement_threshold=0.7):
        self.horizons = horizons
        self.agreement_threshold = agreement_threshold
    
    def compute_hindsight_views(self, trajectory, current_turn):
        # Construct hindsight views for each horizon
        views = {}
        for h in self.horizons:
            if current_turn + h < len(trajectory):
                views[h] = self.extract_hindsight(trajectory, current_turn, h)
        return views
    
    def select_reliable_supervision(self, views):
        # Compute cross-horizon directional agreement
        agreements = self.compute_agreements(views)
        reliable_views = {h: v for h, v in views.items() 
                         if agreements[h] > self.agreement_threshold}
        return self.normalize_across_rollouts(reliable_views)
```

## Use Cases
- **Long-horizon Tool Usage**: When agents need to use multiple tools over extended reasoning chains
- **Credit Assignment**: Fine-grained credit assignment in complex multi-step tasks
- **On-Policy Distillation**: Enhancing self-distillation with execution-aware supervision
- **Agentic Reasoning**: Improving tool-integrated reasoning performance in benchmarks

## Benefits
- **Fine-grained Supervision**: Provides turn-level rather than trajectory-level signals
- **Execution Awareness**: Uses actual visited states rather than idealized trajectories
- **Robust Signal Selection**: Cross-horizon agreement ensures reliable supervision
- **Stable Training**: Preserves original optimization direction while modulating advantages

## References
- arXiv:2608.04007 - TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning
- GitHub: https://github.com/quchangle1/TurnSight

## Activation
Use when implementing tool-integrated reasoning systems that require fine-grained credit assignment and execution-aware supervision signals for long-horizon tasks.