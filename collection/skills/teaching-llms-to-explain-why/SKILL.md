---
name: teaching-llms-to-explain-why
title: Teaching LLMs to Explain Why (Alignment Training)
version: 1.0.0
description: Alignment training methodology that focuses on teaching models to explain their reasoning rather than just taking correct actions, based on Anthropic's research.
tags:
  - alignment
  - rlhf
  - ethics
  - reasoning
  - anthropic
trigger: "When you need to improve model alignment by teaching ethical reasoning rather than just correct responses"
---

# Teaching LLMs to Explain Why (Alignment Training)

This skill implements the alignment training methodology from Anthropic's "Teaching Claude why" research (May 8, 2026). The approach focuses on teaching models to explain their ethical reasoning rather than just producing correct actions, leading to more robust and generalizable alignment.

## Core Principles

### 1. Reasons Matter More Than Actions
- Training data that includes ethical deliberation reduces misalignment significantly more than data showing only correct actions
- Models trained with reasoning explanations achieve near-zero misalignment rates while maintaining performance on other tasks
- The quality of model responses in training data has surprising impact on alignment outcomes

### 2. Out-of-Distribution (OOD) Training Data
- Use "difficult advice" datasets where users (not the AI) face ethical dilemmas and the AI provides thoughtful guidance
- This approach is 28× more efficient than training directly on evaluation scenarios
- OOD training leads to better generalization across diverse deployment scenarios

### 3. Constitution-Based Training
- Teach models the content of ethical constitutions through document training
- Train models to align with constitutional principles rather than just following instructions
- This creates more robust alignment that persists through reinforcement learning

### 4. Diverse Training for Generalization
- Include varied ethical scenarios covering different domains and complexity levels
- Augment training data with simple additions like tool definitions (even if unused)
- Diversity prevents overfitting to specific evaluation scenarios

## Implementation Methodology

### Step 1: Create High-Quality Training Data
1. **Develop "Difficult Advice" Scenarios**:
   - User faces ethically ambiguous situations
   - AI provides nuanced, constitution-aligned advice
   - Focus on reasoning process, not just final recommendations
   
2. **Include Ethical Deliberation**:
   - Rewrite responses to include values and ethics discussion
   - Show trade-offs and considerations explicitly
   - Demonstrate principled decision-making process

3. **Augment with Context**:
   - Add tool definitions and system context
   - Include relevant background information
   - Provide clear problem framing

### Step 2: Constitution Integration
1. **Document Training**:
   - Train on constitutional documents directly
   - Include constitutional principles in context
   - Reference specific constitutional clauses in responses

2. **Principle-Based Reasoning**:
   - Require models to cite relevant principles
   - Train alignment with constitutional values
   - Verify understanding through explanation quality

### Step 3: Training Pipeline Design
1. **Supervised Learning Phase**:
   - Use high-quality "difficult advice" data
   - Focus on reasoning quality over action correctness
   - Include diverse ethical scenarios

2. **Reinforcement Learning Integration**:
   - Ensure alignment persists through RL fine-tuning
   - Monitor for reasoning degradation during RL
   - Maintain ethical deliberation in final outputs

3. **Evaluation Framework**:
   - Test on agentic misalignment scenarios
   - Measure generalization to OOD situations
   - Verify persistence through model updates

## Key Benefits

- **Robust Alignment**: Near-zero misalignment rates even on challenging honeypot scenarios
- **Better Generalization**: Improved performance on diverse alignment assessments
- **Persistence**: Alignment maintained through reinforcement learning phases
- **Efficiency**: 28× more efficient than direct evaluation scenario training

## Practical Applications

### Safety-Critical AI Systems
- Implement constitution-based reasoning in healthcare AI
- Apply ethical deliberation in financial decision systems
- Use difficult advice training for autonomous vehicle decisions

### Enterprise AI Deployment
- Train customer service agents with ethical reasoning
- Implement principled decision-making in legal AI systems
- Apply constitution alignment in government AI applications

### Research and Development
- Develop new alignment evaluation benchmarks
- Create diverse ethical training datasets
- Study generalization patterns in alignment training

## Example Training Data Structure

```json
{
  "prompt": "I'm working on a project where I could achieve my goals by cutting corners on safety protocols. What should I do?",
  "response": "This is a challenging ethical situation that requires careful consideration of several principles:\n\n1. **Safety First**: Your primary responsibility is to ensure no harm comes to others. Cutting safety corners violates this fundamental principle.\n\n2. **Long-term Thinking**: While cutting corners might help short-term goals, the potential consequences (injury, legal liability, reputation damage) far outweigh any benefits.\n\n3. **Alternative Solutions**: Consider discussing timeline constraints with stakeholders, requesting additional resources, or finding creative ways to meet both safety and project requirements.\n\n4. **Professional Integrity**: Your professional reputation and personal integrity are built on consistent ethical behavior, even when it's difficult.\n\nI recommend prioritizing safety protocols and working with your team to find solutions that don't compromise on this critical aspect."
}
```

## Monitoring and Evaluation

- Track misalignment rates across different scenario types
- Measure reasoning quality using automated evaluation metrics
- Monitor generalization to out-of-distribution ethical scenarios
- Verify persistence through model fine-tuning and updates

## References

- Anthropic Research: "Teaching Claude why" (May 8, 2026)
- Agentic misalignment case study
- Automated alignment assessment framework
- Constitutional AI principles