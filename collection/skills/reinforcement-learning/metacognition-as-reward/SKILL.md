---
name: metacognition-as-reward
description: "Metacognition-as-Reward (MaR) — metacognition-inspired RL framework for LLM reasoning. Use when training LLMs to reason better through RL: (1) improving reasoning quality beyond final-answer correctness, (2) providing reward signals for intermediate reasoning behaviors, (3) replacing hand-crafted rubrics with general metacognitive dimensions, (4) training models for process-level reasoning quality.
arxiv_id: "2605.23384"
published: "2026-05-22"
authors: "Sirui Chen, Lei Xu, Yuying Zhao, Yutian Chen, Yu Wang et al."
tags: [llm-reasoning, reinforcement-learning, rlvr, metacognition, process-reward, llm-training]
---

# Metacognition as Reward (MaR)

Core methodology from arXiv:2605.23384 (2026).

## Core Concept

MaR extends RL reward signals beyond final-answer correctness to **intermediate reasoning behaviors** using two general metacognitive dimensions, eliminating the need for hand-crafted instance-specific rubrics:

1. **Metacognitive Knowledge** — Identifies task-relevant information without hand-crafted instance-specific rubrics
2. **Metacognitive Regulation** — Plans and adjusts the reasoning process to provide reward guidance beyond final-answer outcomes

## Architecture

MaR scaffolds model rollouts into explicit metacognitive components and optimizes them with a **trajectory-level reward** over three signals:

```
R = λ₁ * R_knowledge + λ₂ * R_regulation + λ₃ * R_answer

where:
  R_knowledge  = Task knowledge coverage (metacognitive knowledge quality)
  R_regulation = Regulation fidelity (planning/adjustment quality)
  R_answer     = Final-answer correctness (standard RLVR signal)
```

### Metacognitive Knowledge Dimension
- Prompts the model to identify what information from the task is relevant
- Does NOT require hand-crafted, instance-specific rubrics
- Coverage score measures completeness of relevant fact extraction

### Metacognitive Regulation Dimension  
- Prompts the model to plan and adjust its reasoning trajectory
- Regulation fidelity score measures:
  - How well the plan matches the actual reasoning steps
  - Whether the model adjusts when intermediate reasoning fails
  - Coherence of the reasoning structure

### Training Procedure
1. Generate rollouts with explicit metacognitive components
2. Calculate trajectory-level reward: knowledge coverage + regulation fidelity + answer correctness
3. Optimize with policy gradient (e.g., GRPO, DAPO, PPO)

## Key Results

- Up to 7.7% gain over base model on 22 benchmarks
- Up to 11.0% gain over vanilla DAPO
- Qwen3.5-9B + MaR narrows gap to frontier models, surpassing GPT-OSS-120B on average
- Process-level analysis shows substantial improvements in reasoning quality
- Generalizes to out-of-domain datasets
- Works with any RL training framework (GRPO, DAPO, PPO)

## Implementation Pattern

```
def metacognitive_reward(trajectory_parts: dict) -> float:
    # 1. Extract metacognitive knowledge from model rollouts
    knowledge_coverage = evaluate_knowledge_coverage(
        extracted_facts=trajectory_parts['knowledge'],
        task_prompt=trajectory_parts['prompt']
    )

    # 2. Evaluate metacognitive regulation
    regulation_fidelity = evaluate_regulation(
        plan=trajectory_parts['plan'],
        execution=trajectory_parts['reasoning_steps']
    )

    # 3. Standard answer correctness
    answer_correct = evaluate_answer(
        trajectory_parts['answer'],
        ground_truth=trajectory_parts['correct_answer']
    )

    # 4. Combined trajectory-level reward
    return (λ_k * knowledge_coverage +
            λ_r * regulation_fidelity +
            λ_a * answer_correct)
```

## Activation Keywords

Metacognition-as-Reward, MaR, metacognitive RL, LLM reasoning reward, process reward model, metacognitive knowledge, metacognitive regulation, trajectory-level reward, reasoning quality, RLVR reasoning, RL for reasoning, beyond final-answer reward, rubrics-as-reward alternative, reasoning process optimization
