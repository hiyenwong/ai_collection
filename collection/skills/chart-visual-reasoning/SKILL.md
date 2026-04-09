# SKILL.md - Chart-RL: RL for VLM Visual Reasoning

## Paper Reference
- **arXiv:** 2604.03157
- **Title:** Policy Optimization Reinforcement Learning for Enhanced Visual Reasoning in Chart Question Answering
- **Utility Score:** 0.85
- **Authors:** Amit Dhanda et al.
- **Conference:** KDD 2026
- **Date:** April 2026

## Core Insights

### Problem Addressed
VLMs struggle with Chart Question Answering (CQA):
- Imprecise numerical extraction
- Difficulty interpreting implicit visual relationships
- Inadequate attention for spatial relationships

### Solution: Chart-RL
- RL framework enhancing VLM chart understanding
- Feedback-driven policy optimization
- Adaptive reward functions
- LoRA-based parameter-efficient fine-tuning

### Key Result
**4B model beats 8B foundation model:**
- Qwen3-VL-4B-Instruct (RL): 0.634 accuracy
- Qwen3-VL-8B-Instruct (baseline): 0.580 accuracy
- Half the parameters, better performance

### Efficiency Gains
- Single GPU configuration (via LoRA)
- Inference latency: 31s → 9s (3.4x faster)

## Practical Applications

### Chart Understanding Pipeline
```markdown
1. Pre-train VLM on chart data
2. Apply RL fine-tuning with policy optimization
3. Use adaptive rewards for visual reasoning
4. Deploy with LoRA efficiency
```

### CQA Improvement Areas
- Numerical extraction precision
- Implicit relationship interpretation
- Spatial attention mechanisms

### Training Setup
- Parameter-efficient via LoRA
- Single GPU feasible
- Policy optimization framework

## Key Takeaways
- RL fine-tuning beats larger foundation models
- LoRA enables single-GPU deployment
- Latency reduction alongside accuracy gains
- VLMs need specialized reasoning training

## Benchmark
- ChartQAPro dataset
- Compared: open-source, proprietary, closed-source SOTA

## Further Reading
- Full paper: https://arxiv.org/abs/2604.03157
- PDF: https://arxiv.org/pdf/2604.03157
## Description
Framework from arXiv papers. See paper reference for details.
## Activation Keywords

- chart-visual-reasoning
- chart-visual-reasoning 技能
- chart-visual-reasoning skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply chart-visual-reasoning?

**Agent:** I'll help you understand and apply chart-visual-reasoning...

### Example 2: Advanced Application

**User:** What are the key considerations for chart-visual-reasoning?

**Agent:** Let me search for the latest research and best practices...
