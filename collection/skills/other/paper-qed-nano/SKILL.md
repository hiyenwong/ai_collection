---
name: skill.md---qed-nano-small-model-mathematical-reaso
description: Skill for AI agent capabilities
---

# SKILL.md - QED-Nano: Small Model Mathematical Reasoning

## Paper Reference
- **arXiv ID**: 2604.04898
- **Title**: Teaching a Tiny Model to Prove Hard Theorems
- **Authors**: Yuxiao Qu et al.
- **Date**: April 2026
- **URL**: https://arxiv.org/abs/2604.04898

## Utility Score
**0.92** - High utility for practical AI engineering

## Core Insight
Small models (4B parameters) can achieve competitive Olympiad-level mathematical proof performance with the right training pipeline, challenging the assumption that reasoning requires massive models.

## Key Methods
### Three-Stage Training Recipe
1. **Supervised Fine-Tuning (SFT)**: Distill proof-writing styles from DeepSeek-Math-V2
2. **Reinforcement Learning (RL)**: Rubric-based reward optimization
3. **Reasoning Cache**: Decompose long proofs into iterative summarize-and-refine cycles for stronger test-time reasoning

### Performance
- Surpasses larger open models (Nomos-1, GPT-OSS-120B)
- Approaches proprietary models (Gemini 3 Pro) at fraction of inference cost

## When to Apply
- When training small models for reasoning tasks
- For cost-efficient inference on mathematical/proof-based tasks
- When designing test-time compute strategies

## Practical Applications
1. **Model Training**: Use the three-stage recipe for small model reasoning
2. **Inference Cost Reduction**: Deploy QED-Nano instead of larger models for math tasks
3. **Reasoning Cache Pattern**: Implement summarize-and-refine cycles for complex problems

## Key Takeaways
- **Model size ≠ reasoning quality** - training methodology matters more
- **Test-time compute** via reasoning cache is highly effective
- **Distillation + RL** is a winning combination for specialized reasoning

## Resources
- QED-Nano model (4B)
- QED-Nano-SFT model
- FineProofs-SFT dataset
- FineProofs-RL dataset
- Training and evaluation code (all released)

## Related Techniques
- Rubric-based RL rewards for structured reasoning
- Proof-style distillation from larger models
- Iterative refinement at inference time

## Tags
`small-models` `reasoning` `mathematics` `rl-training` `distillation` `inference-optimization` `proof-generation`

## Activation Keywords

- "paper-qed-nano"
- "paper qed nano"
- "use paper qed nano"
- "paper qed nano help"
- "paper qed nano tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Paper Qed Nano usage
```
User: "Help me with paper qed nano"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed paper qed nano assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
