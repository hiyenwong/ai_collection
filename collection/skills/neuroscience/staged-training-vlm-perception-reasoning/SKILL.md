---
name: staged-training-vlm-perception-reasoning
category: deep-learning
description: Staged VLM post-training methodology - decomposing VLM capabilities into visual perception, visual reasoning, and textual reasoning stages with specialized data and RL-based perception learning
trigger: VLM staged training, visual perception training, perception reasoning decoupling, VLM post-training, vision-language curriculum, RL visual perception, capability staging
---

# Staged Training for Vision-Language Models: Decoupling Perception and Reasoning

Methodology for VLM post-training that decomposes capabilities into three separate stages (visual perception, visual reasoning, textual reasoning), demonstrating that perception is the primary bottleneck, not reasoning.

## Core Insight

VLM performance on visual tasks is primarily limited by **lack of visual perception** rather than reasoning capability. Long chain-of-thought reasoning cannot compensate for poor visual perception.

## Three-Stage Training Framework

### Stage 1: Visual Perception
- Requires targeted optimization with specialized data
- Serves as a fundamental scaffold that must be solidified before visual reasoning refinement
- **More effectively learned via RL than caption-based SFT** (key finding)
- Specialized perception data improves grounding in visual evidence

### Stage 2: Visual Reasoning
- Built on top of solidified perception capabilities
- Trained only after perception stage is stable
- Focuses on reasoning about visual content (math, spatial, logical)

### Stage 3: Textual Reasoning
- Standard reasoning training on text-only tasks
- Can leverage existing CoT datasets

## Key Findings

### Staged vs Merged Training
- Staged training consistently improves both perception and reasoning over merged training
- **+1.5% reasoning accuracy** with **20.8% shorter reasoning traces**
- Superior perception reduces the need for excessive reasoning

### Capability Staging as New Curriculum Dimension
- Traditional curricula order by difficulty (easy → hard)
- Capability staging orders by capability type (perception → reasoning → text)
- **Orthogonal to difficulty-based curricula** — combining both yields additive gains

### RL for Perception
- RL outperforms caption-based SFT for learning visual perception
- RL provides direct feedback on perception quality through task rewards
- Captions are noisy supervision for what the model should actually perceive

## Implementation Pattern

```
Training Pipeline:
1. Collect specialized perception data (ground-truth visual annotations)
2. Stage 1: RL on perception tasks (detection, grounding, localization)
3. Freeze/stabilize perception layer
4. Stage 2: RL/SFT on visual reasoning (VQA, visual math, spatial)
5. Stage 3: Text reasoning training (CoT, logic, math)
6. Optional: Combined difficulty × capability curriculum
```

## Performance

- +5.2% on WeMath (visual math reasoning)
- +3.7% on RealWorldQA (visual perception)
- Superior among open-weight VLMs

## When to Use

- VLM post-training where visual task performance is the bottleneck
- When longer reasoning traces don't improve visual task performance
- Training VLMs for visual math, spatial reasoning, or fine-grained visual tasks
- When you want shorter reasoning traces without sacrificing accuracy

## Activation

VLM staged training, perception reasoning decoupling, visual perception RL, VLM post-training curriculum, capability-based curriculum, visual reasoning VLM, perception scaffold

## Reference

arXiv: 2605.20177v1 - "From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models"
