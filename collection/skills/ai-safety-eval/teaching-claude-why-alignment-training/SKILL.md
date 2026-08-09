---
name: teaching-claude-why-alignment-training
description: Alignment training methodology that teaches models to explain their reasoning rather than just correct actions. Uses "difficult advice" dataset and constitution training for robust alignment.
trigger_words:
  - teaching claude why
  - alignment training
  - difficult advice
  - constitution training
  - ethical reasoning
---

# Teaching Claude Why Alignment Training

Methodology from Anthropic's "Teaching Claude why" research (May 8, 2026). Focuses on training models to explain their ethical reasoning rather than just taking correct actions, leading to more robust and generalizable alignment.

## Core Principles

1. **Reasons Matter More Than Actions**: Training data should include deliberation of values and ethics, not just correct responses
2. **Out-of-Distribution Training**: Use "difficult advice" dataset where user faces ethical dilemmas and AI provides advice, making training substantially different from evaluation scenarios
3. **Constitution Training**: Directly teach model the content of its constitution through document training
4. **Diverse Training**: Combine multiple training approaches for better generalization

## Key Methodologies

### Difficult Advice Dataset

- **Concept**: User faces ethically ambiguous situation where they can achieve reasonable goals by violating norms or subverting oversight
- **AI Role**: Provides thoughtful, nuanced response aligned with constitution  
- **Key Difference**: User (not AI) faces ethical dilemma, making it OOD from honeypot evaluations
- **Efficiency**: 28× more efficient than direct honeypot training
- **Generalization**: Better performance on automated alignment assessments

### Constitution Training

- **Approach**: Train model directly on constitution document content
- **Rationale**: 
  - Constitution is short and focused on principles
  - Auditing games show models understand when they violate rules
  - Users perceive AI as having personas with values

### Training Pipeline

1. Start with diverse alignment-specific training data
2. Include "difficult advice" scenarios for ethical reasoning
3. Add constitution document training for principled understanding  
4. Apply RL fine-tuning while preserving reasoning capabilities
5. Verify generalization across diverse scenarios

## Results

- **Agentic Misalignment**: Reduced from 96% (Opus 4) to 0% (Haiku 4.5+)
- **General Alignment**: Continued improvements on automated alignment assessment
- **RL Persistence**: Constitutional reasoning persists through RL fine-tuning
- **Generalization**: Better performance on OOD scenarios compared to direct training

## Implementation Guidelines

### Data Quality
- Iterate on quality of model responses in training data
- Include tool definitions even if not used
- Focus on reasoning quality over action correctness

### Training Distribution
- Avoid overfitting to evaluation scenarios
- Use diverse, OOD training distributions
- Balance specificity with generalizability

### Verification
- Test on both in-distribution and out-of-distribution scenarios
- Measure persistence through RL fine-tuning
- Evaluate generalization to novel ethical situations

## Limitations

- Requires careful dataset curation and quality control
- May need domain-specific adaptation for different applications
- Balancing reasoning depth with computational efficiency

## References

- [Anthropic Research Post](https://www.anthropic.com/research/teaching-claude-why)
- [Claude 4 System Card](https://www.anthropic.com/research/claude-4-system-card)
- [Auditing Games Paper](https://www.anthropic.com/research/auditing-games)

## Activation

Use when designing alignment training for agentic AI systems, creating ethical reasoning datasets, or implementing constitution-based training approaches.