---
name: turn-opd-turn-level-budgeting
description: TurnOPD methodology for efficient on-policy distillation of long-horizon agents. Uses adaptive rollout-depth budgeting and progressive turn-normalized loss to address inefficiencies in vanilla agent OPD.
date: 2026-07-10
arxiv: 2607.05804v1
authors: Yuhang Zhou, Kai Zheng, Haoling Li, Dengyun Peng, Can Xu et al.
tags: [distillation, on-policy-distillation, long-horizon, agent-training, efficiency]
activation: turn-opd, turn-level-budgeting, rollout-depth, progressive-loss, long-horizon-agents
---

# TurnOPD: Turn-Level Budgeting for On-Policy Distillation

## Core Innovation

TurnOPD addresses two key inefficiencies in vanilla on-policy distillation (OPD) for long-horizon agentic tasks through turn-level budgeting strategies.

## Key Problems Identified

### 1. Wasted Rollout Resources
- **Issue**: Full-horizon rollouts waste wall-clock time on tail turns
- **Problem**: Tail turns provide weak and noisy KL supervision
- **Impact**: Inefficient use of compute budget

### 2. Uneven Loss Distribution
- **Issue**: Trajectory-level KL objectives concentrate loss on shallow tokens
- **Problem**: Deeper decision turns are under-trained once initial behaviors align
- **Impact**: Poor learning of late-stage decision making

## Key Methodology

### 1. Adaptive Rollout-Depth Budgeting
- **Mechanism**: Use probe-based turn statistics to determine rollout length
- **Process**:
  1. Run short probe rollouts to estimate turn distribution
  2. Identify turns with high KL variance (informative turns)
  3. Set rollout depth to capture informative turns, skip noisy tails
- **Benefit**: Focuses compute on turns with strong supervision signal

### 2. Progressive Turn-Normalized Loss Budgeting
- **Mechanism**: Gradually shift KL weighting from token-level to turn-balanced
- **Process**:
  - **Early training**: Token-level KL (focus on initial alignment)
  - **Mid training**: Mix token and turn-level weighting
  - **Late training**: Turn-normalized KL (ensure all turns trained)
- **Benefit**: Prevents shallow tokens from dominating, ensures deep turns learn

## Implementation Details

```python
# Pseudocode for TurnOPD
class TurnOPD:
    def __init__(self):
        self.phase = "early"  # early, mid, late
        
    def probe_rollout_depth(self, student, prompts):
        # Run short probes to estimate turn statistics
        turn_stats = []
        for prompt in prompts:
            rollout = student.generate(prompt, max_turns=5)
            kl_per_turn = compute_kl_per_turn(rollout, teacher)
            turn_stats.append(kl_per_turn)
        
        # Find turns with high KL variance (informative)
        informative_turns = find_high_variance_turns(turn_stats)
        return max(informative_turns) + 2  # buffer
    
    def compute_loss(self, student_rollout, teacher_rollout):
        token_kl = compute_token_kl(student_rollout, teacher_rollout)
        turn_kl = compute_turn_kl(student_rollout, teacher_rollout)
        
        if self.phase == "early":
            # Token-level focus
            return token_kl
        elif self.phase == "mid":
            # Mixed weighting
            return 0.5 * token_kl + 0.5 * turn_kl
        else:  # late
            # Turn-normalized focus
            return turn_kl
    
    def update_phase(self, step):
        if step < 1000:
            self.phase = "early"
        elif step < 3000:
            self.phase = "mid"
        else:
            self.phase = "late"
```

## Results

- **Benchmarks**: ALFWorld, WebShop, Multi-Hop Search
- **Teachers**: Task-specialized teacher models
- **Efficiency**: Superior validation accuracy under equal wall-clock budget
- **Frontier**: Advances accuracy-time Pareto frontier beyond vanilla OPD

## When to Use

- Long-horizon agentic tasks (multi-turn dialogue, tool use, search)
- When vanilla OPD is too slow or inefficient
- When deep decision turns are under-trained
- When compute budget is limited

## Diagnostic Signs

Watch for these indicators that TurnOPD might help:
- Long rollouts (10+ turns) with diminishing returns
- Early turns improve but late turns stagnate
- Wall-clock time dominated by rollout generation
- KL loss concentrated on first few tokens

## Key Insight

"Trajectory-level KL objectives concentrate most of the loss on shallow tokens, leaving deeper decision turns under-trained once initial behaviors are aligned." TurnOPD fixes this by progressively shifting to turn-level supervision.

## Activation Patterns

- `turn-opd` - Turn-level On-Policy Distillation
- `turn-level-budgeting` - Budgeting at turn granularity
- `rollout-depth` - Adaptive rollout length selection
- `progressive-loss` - Progressive loss weighting strategy
- `long-horizon-agents` - Agents with many sequential decisions
