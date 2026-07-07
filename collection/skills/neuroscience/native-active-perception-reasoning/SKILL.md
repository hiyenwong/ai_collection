---
name: native-active-perception-reasoning
description: Native active perception methodology for omni-modal understanding using POMDP-based Observation-Thought-Action cycle, Agentic Supervised Fine-Tuning (ASFT), and TAURA turn-level credit assignment.
version: 1.0.0
tags: [active-perception, reasoning, POMDP, agentic-rl, video-understanding, multimodal]
activation_keywords: [active perception, POMDP, observation thought action, ASFT, TAURA, video understanding, turn-level entropy, test-time scaling, on-demand perception]
---

# Native Active Perception as Reasoning

## Overview

OmniAgent framework for native omni-modal understanding that formulates video understanding as a POMDP-based iterative Observation-Thought-Action cycle. Decouples reasoning complexity from raw video duration through on-demand perception.

## Core Methodology

### 1. POMDP Formulation
- **State**: Persistent textual memory (distilled audio-visual cues)
- **Action**: On-demand observation actions (seek, query, focus)
- **Observation**: Selective audio-visual cue extraction
- **Reward**: Query-answering accuracy + efficiency bonus

### 2. Observation-Thought-Action Cycle
```
while not terminated:
    # Thought: Analyze current memory state
    thought = analyze_memory(current_state, query)
    
    # Action: Select observation strategy
    action = select_action(thought, uncertainty)
    
    # Observation: Execute on-demand perception
    new_cue = execute_observation(action)
    
    # Memory Update: Distill into persistent text
    memory = update_memory(memory, new_cue)
```

### 3. Agentic Supervised Fine-Tuning (ASFT)
- **Best-of-N trajectory synthesis**
- **Dual-stage quality control**:
  1. Outcome verification (answer correctness)
  2. Process verification (trajectory efficiency)
- **Bootstrap native active perception** from expert demonstrations

### 4. TAURA: Turn-aware Adaptive Uncertainty Rescaled Advantage
```
# Turn-level entropy for credit assignment
for each turn t:
    entropy_t = compute_entropy(policy_t)
    
    # Rescale advantage based on uncertainty
    advantage_t = (reward_t - baseline) * rescale_factor(entropy_t)
    
    # Pivotal discovery turns get higher credit
    if is_pivotal_turn(entropy_t):
        advantage_t *= discovery_boost
```

**Key Insight**: High-entropy turns indicate exploration → boost credit assignment

### 5. Test-Time Scaling
- **Positive scaling**: Performance improves with more reasoning turns
- **Decoupling**: Complexity independent of video duration
- **On-demand**: Only observe what's needed for the query

## Implementation Pattern

```python
class OmniAgent:
    def __init__(self, vision_encoder, text_memory, policy_model):
        self.memory = PersistentTextMemory()
        self.policy = POMDPPolicy()
        
    def understand(self, video, query, max_turns=10):
        for turn in range(max_turns):
            # Thought phase
            thought = self.policy.think(self.memory.state, query)
            
            # Check if memory sufficient
            if thought.confidence > threshold:
                return self.answer(query, self.memory)
            
            # Action phase - on-demand observation
            action = self.policy.act(thought)
            cue = self.observe(video, action)
            
            # Memory update
            self.memory.distill(cue)
```

## Key Benefits

1. **Efficiency**: Memory cost decoupled from video duration
2. **Test-Time Scaling**: More turns → better performance
3. **Native**: No pre-scanning required
4. **Adaptive**: Entropy-guided credit assignment

## Use Cases

- Long video understanding (>10min)
- Omni-modal QA (audio + visual + text)
- Active perception agents
- On-demand inference optimization

## Performance

- 7B model beats 72B baseline (50.5% vs 47.3% on LVBench)
- VideoMME, LVBench state-of-the-art among open-source

## Reference

- Paper: "Native Active Perception as Reasoning for Omni-Modal Understanding" (arXiv:2606.19341v1)
- Authors: Zhenghao Xing et al. (2026-06-17)