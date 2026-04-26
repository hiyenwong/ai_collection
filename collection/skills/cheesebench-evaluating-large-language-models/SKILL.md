---
name: cheesebench-evaluating-large-language-models
description: "We introduce CheeseBench, a benchmark that evaluates large language models (LLMs) on nine classical behavioral neuroscience paradigms (Morris water maze, Barnes maze, T-maze, radial arm maze, star maz. Activation: rodent behavior paradigms, LLM evaluation, ODE complexity"
version: 1.0.0
metadata:
  hermes:
    source_paper: "CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms (arXiv:2604.10825v1)"
    tags: [behavior, behavioral, cognitive, learning, neuroscience, paradigm]
---

# CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms

## Paper Reference

- **Title**: CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms
- **Authors**: Zacharie Bugaud
- **arXiv**: 2604.10825v1
- **Published**: 2026-04-12
- **Categories**: cs.AI
- **PDF**: https://arxiv.org/abs/2604.10825

## Overview

We introduce CheeseBench, a benchmark that evaluates large language models (LLMs) on nine classical behavioral neuroscience paradigms (Morris water maze, Barnes maze, T-maze, radial arm maze, star maze, operant chamber, shuttle box, conditioned place preference, and delayed non-match to sample), spanning six cognitive dimensions. Each task is grounded in peer-reviewed rodent protocols with approximate animal baselines. The agent receives a unified system prompt with no task-specific instructions and must discover goals purely from ASCII text observations and reward signals, much like a rodent placed into an unfamiliar apparatus. We evaluate six open-weight LLMs (3B to 72B parameters) on text-based ASCII renderings and compare against both a random baseline and a graph-based reinforcement l

## Core Concepts

1. **Behavioral Neuroscience Paradigms**: Classic rodent behavioral tests as LLM evaluation tasks
2. **Cross-Species Evaluation**: Bridging animal behavior research with AI evaluation
3. **Cognitive Task Benchmarking**: Systematic assessment of LLM capabilities through behavioral paradigms
4. **Spatial Memory & Navigation**: Evaluating spatial reasoning through maze-like tasks

## Core Paradigms Covered

| Task | Cognitive Domain | What it Tests |
|------|-----------------|---------------|
| Morris Water Maze | Spatial learning | Navigation & memory |
| T-Maze | Working memory | Alternation behavior |
| Radial Arm Maze | Spatial reference memory | Memory capacity |
| Open Field | Anxiety & exploration | Risk assessment |
| Elevated Plus Maze | Anxiety | Risk-reward tradeoff |
| Fear Conditioning | Associative learning | Memory formation |
| Object Recognition | Recognition memory | Novelty detection |
| Barnes Maze | Spatial learning | Escape motivation |
| Social Interaction | Social behavior | Social cognition |

## Implementation Pattern

```python
class CheeseBenchTask:
    """Base class for rodent behavioral paradigm tasks."""
    
    def __init__(self, name, domain, description):
        self.name = name
        self.domain = domain
        self.description = description
    
    def evaluate_llm(self, llm_response, ground_truth):
        raise NotImplementedError

class MorrisWaterMaze(CheeseBenchTask):
    """Spatial navigation and learning task."""
    
    def __init__(self):
        super().__init__(
            name="Morris Water Maze",
            domain="Spatial Learning",
            description="Navigate to hidden platform using spatial cues"
        )
    
    def generate_prompt(self, session_num=1):
        return ("Imagine you are in a circular pool. "
                "Find a hidden platform using spatial landmarks. "
                "Session: " + str(session_num))
```

## Applications

- LLM cognitive capability evaluation
- Cross-modal behavioral benchmarking
- AI safety assessment through behavioral paradigms
- Comparative cognitive science

## Limitations

- Based on abstract analysis; full paper may contain additional details
- Implementations are illustrative; refer to paper for production code
- Domain-specific parameters need empirical tuning

## References

- Zacharie Bugaud (2026). "CheeseBench: Evaluating Large Language Models on Rodent Behavioral Neuroscience Paradigms." arXiv:2604.10825v1.
- Full paper: https://arxiv.org/pdf/2604.10825.pdf

## Activation Keywords

- behavior, behavioral, cognitive, learning, neuroscience, paradigm, rodent
