---
name: physics-informed-llm-pid-tuning
title: Physics-Informed LLM Framework for PID Tuning of Chemical Processes
version: 1.0.0
description: A physics-informed framework that uses Large Language Model agents for PID tuning of chemical processes, combining closed-loop response features, control-engineering diagnoses, and physics-informed reinforcement learning.
trigger_words:
  - "PID tuning"
  - "chemical process control"
  - "physics-informed LLM"
  - "control system optimization"
  - "process control"
categories:
  - systems-engineering
  - control-systems
  - ai-agents
  - chemical-engineering
paper_reference:
  arxiv_id: "2607.26594"
  title: "A Physics-Informed Framework for PID Tuning of Chemical Processes Using Large Language Model Agents"
  authors: ["Zhoupeng Shou", "Xiaodong Hong", "Congjing Ren", "Jingdai Wang", "Yongrong Yang", "Zuwei Liao"]
  date: "2026-07-29"
  url: "https://arxiv.org/abs/2607.26594"
---

# Physics-Informed LLM Framework for PID Tuning

## Overview
This skill implements a physics-informed framework for PID tuning of chemical processes using Large Language Model (LLM) agents. The approach formalizes the engineer-like workflow of observing responses, diagnosing deficiencies, adjusting gains, and validating results in an LLM-assisted framework.

## Core Methodology

### Hosted LLM Approach
For cloud-based LLMs (DeepSeek-V4-Flash, Qwen3.7-Plus):
1. **Input Features**: Provide closed-loop response features to the LLM
2. **Engineering Context**: Include control-engineering diagnoses and tuning preferences  
3. **Demonstrations**: Supply IMC (Internal Model Control)-based demonstrations as examples
4. **Iterative Correction**: Generate PID gains and iteratively correct under acceptance criteria
5. **Validation**: Apply common acceptance criteria for final validation

### Local Deployment Approach
For local small language models (Qwen3-0.6B):
1. **Supervised Fine-Tuning (SFT)**: Train with simulation-verified IMC targets
2. **Physics-Informed GRPO**: Apply group relative policy optimization with non-compensable stability and performance rewards
3. **Performance Metrics**: Focus on first-attempt reliability and stability margins

## Implementation Steps

### For Hosted LLMs
1. Collect closed-loop response data from the chemical process
2. Extract key features (overshoot, settling time, steady-state error, etc.)
3. Perform initial control-engineering diagnosis
4. Format input prompt with:
   - Process characteristics (FOPDT/SOPDT parameters)
   - Current performance metrics
   - Desired tuning objectives
   - IMC-based demonstration examples
5. Query hosted LLM for PID gain recommendations
6. Validate recommendations against safety and performance criteria
7. Iterate if necessary until acceptable performance is achieved

### For Local SLMs
1. Prepare training dataset with FOPDT/SOPDT test cases
2. Generate IMC targets through simulation verification
3. Perform supervised fine-tuning on the base model
4. Implement physics-informed reward function for GRPO:
   - Stability rewards (non-compensable)
   - Performance rewards (settling time, overshoot, etc.)
5. Train using group relative policy optimization
6. Deploy for real-time PID tuning recommendations

## Performance Benchmarks
- **Hosted LLMs**: 75-89% success rate on FOPDT cases, 77-79% on SOPDT cases
- **Local SLM (SFT only)**: 86.5% first-recommendation success rate  
- **Local SLM (SFT + PI-GRPO)**: 94.0% first-recommendation success rate

## Key Advantages
1. **Engineer-like Workflow**: Mimics human expert tuning process
2. **Physics-Informed**: Incorporates domain knowledge and physical constraints
3. **Flexible Deployment**: Works with both hosted and local models
4. **High Reliability**: Achieves >94% success rate with optimized local models
5. **Iterative Improvement**: Supports correction loops for suboptimal recommendations

## Use Cases
- Chemical process control systems
- Industrial automation PID tuning
- Process optimization in manufacturing
- Academic research in control theory
- Integration with existing DCS/SCADA systems

## Activation Conditions
Use this framework when:
- Tuning PID controllers for chemical processes
- Need to automate control system optimization
- Have access to closed-loop response data
- Require physics-informed AI solutions
- Working with FOPDT or SOPDT process models

## References
- Original paper: arXiv:2607.26594
- IMC (Internal Model Control) methodology
- Group Relative Policy Optimization (GRPO)
- First-Order Plus Dead Time (FOPDT) models
- Second-Order Plus Dead Time (SOPDT) models