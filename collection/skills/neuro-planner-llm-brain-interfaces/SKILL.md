---
title: LLM-Assisted Brain Stimulation Planning (Neuro-Planner)
description: LLM-assisted transcranial electrical stimulation (tES) montage design using iterative reasoning. Applies LLM chain-of-thought reasoning to propose, simulate, evaluate, and refine brain stimulation montages with FEM-based E-field simulation feedback loop.
activation: brain stimulation planning, LLM tES, montage optimization, tDCS design, transcranial stimulation, computational neuromodulation, Neuro-Planner
categories: ["neuroscience", "brain-stimulation", "LLM", "neuromodulation", "clinical"]
trigger_keywords: ["LLM brain stimulation", "tES montage", "transcranial electrical stimulation", "tDCS optimization", "tACS design", "FEM E-field", "computational neuromodulation", "brain stimulation planning", "neuro-planner", "CoT stimulation"]
related_skills: 
source_paper: Neuro-Planner: Leveraging LLM Iterative Reasoning to Propose Brain Stimulation Montages
source_url: https://arxiv.org/abs/2604.14951
created: 2026-04-19
version: 1.0
name: neuro-planner-llm-brain-interfaces
---


# Neuro-Planner: LLM-Assisted Brain Stimulation Planning

## Overview

Neuro-Planner uses Large Language Models as reasoning engines for designing transcranial electrical stimulation (tES) montages. Through iterative chain-of-thought reasoning combined with FEM-based E-field simulation feedback, the system proposes, evaluates, and refines electrode placements for targeted brain stimulation.

## When to Use

- Designing personalized tES/tDCS/tACS stimulation protocols
- Computational neuromodulation research
- Brain stimulation protocol optimization
- Clinical trial planning for transcranial stimulation
- Non-invasive BCI enhancement

## Core Methodology

### Iterative Reasoning Loop

```
┌─────────────────────────────────────────────────────┐
│  1. Prompt Construction                              │
│     - Define target ROI (e.g., DLPFC, M1)            │
│     - Specify desired E-field properties             │
│     - Include safety constraints                     │
├─────────────────────────────────────────────────────┤
│  2. LLM Montage Generation                           │
│     - Zero-shot CoT: LLM reasons from first          │
│       principles about electrode placement           │
│     - Few-shot CoT: Provide examples of good         │
│       montages as context                            │
│     - Multi-prompt: Generate diverse candidates      │
├─────────────────────────────────────────────────────┤
│  3. FEM E-Field Simulation                           │
│     - Run SimNIBS or equivalent FEM simulation       │
│     - Compute E-field distribution in brain          │
│     - Extract target and off-target metrics          │
├─────────────────────────────────────────────────────┤
│  4. Evaluation & Scoring                             │
│     - E-field strength at target ROI                 │
│     - Focality (concentration at target)             │
│     - Off-target exposure minimization               │
│     - Safety compliance check                        │
├─────────────────────────────────────────────────────┤
│  5. Iterative Refinement                             │
│     - Feed simulation results back to LLM            │
│     - LLM analyzes what worked/didn't work           │
│     - Generate improved montage proposal             │
│     - Repeat until convergence or max iterations     │
└─────────────────────────────────────────────────────┘
```

### Prompt Design Strategies

**Zero-shot CoT Prompt:**
```
"You are a neuroscientist designing a tDCS montage. The target ROI
is [DLPFC]. Design an electrode montage that maximizes E-field
strength at the target while minimizing off-target exposure.
Think step by step about:
1. Electrode positions (10-20 system)
2. Current direction and magnitude
3. Expected E-field distribution
4. Safety constraints (< 2mA, current density limits)"
```

**Few-shot CoT Prompt:**
```
"Example 1:
Target: Primary Motor Cortex (M1)
Good montage: Anode at C3, Cathode at Fp2
Reasoning: C3 is directly over left M1, Fp2 provides
good return path avoiding target region...

Now design a montage for [TARGET]:"
```

### Evaluation Metrics

| Metric | Description | Target Value |
|--------|-------------|--------------|
| E-Field Strength | Mean electric field in target ROI | > 0.3 V/m |
| Focality | Ratio of target to total brain E-field | > 0.6 |
| Off-Target Ratio | E-field outside ROI / Total E-field | < 0.4 |
| Safety Score | Compliance with tES guidelines | 1.0 (pass) |

## Implementation Guidelines

### Required Components
1. **LLM Engine:** Any capable LLM with chain-of-thought reasoning
2. **FEM Simulator:** SimNIBS, ROAST, or custom FEM solver
3. **Head Model:** Subject-specific or template (MNI)
4. **Safety Checker:** tES safety guideline validator

### Python Implementation Pattern
```python
class NeuroPlanner:
    def __init__(self, llm_client, fem_solver, head_model):
        self.llm = llm_client
        self.fem = fem_solver
        self.head = head_model

    def plan(self, target_roi, n_iterations=5):
        prompt = self._build_prompt(target_roi)
        best_montage = None
        best_score = -1

        for i in range(n_iterations):
            # LLM proposes montage
            montage = self._llm_propose(prompt, previous_results)
            # Simulate E-field
            efield = self.fem.simulate(montage, self.head)
            # Evaluate
            score = self._evaluate(efield, target_roi)
            # Refine
            if score > best_score:
                best_score = score
                best_montage = montage
            prompt = self._refine_prompt(prompt, montage, score)

        return best_montage, best_score
```

## Applications

- **Depression Treatment:** Optimize tDCS targeting DLPFC
- **Motor Rehabilitation:** Design stimulation for M1/PMC
- **Cognitive Enhancement:** Prefrontal cortex targeting
- **Pain Management:** Motor cortex stimulation protocols
- **Research:** Systematic exploration of montage space

## Pitfalls

1. **LLM Hallucination:** LLM may propose physically impossible montages. Always validate with FEM simulation.
2. **Template vs. Individual:** Template head models may not reflect individual anatomy. Use subject-specific models when available.
3. **Safety Violations:** LLM may not fully understand current density limits. Always run safety verification.
4. **Convergence Issues:** Iterative refinement may not converge. Set maximum iterations and fallback to best-so-far.
5. **Prompt Sensitivity:** Results depend heavily on prompt design. Use systematic prompt engineering.
6. **Limited E-Field Knowledge:** LLM training data may contain outdated or incorrect tES knowledge. Ground truth must come from simulation.

## Safety Considerations

- Maximum current: ≤ 2 mA for tDCS
- Current density: ≤ 0.28 mA/cm² at electrodes
- Duration: ≤ 30 minutes per session
- Contraindications: History of seizures, metal implants, pregnancy
- Always verify against current tES safety guidelines (e.g., Bikson et al., 2016)

## Future Directions

- Integration with real-time fMRI/EEG for closed-loop stimulation
- Multi-target optimization for network-level modulation
- Personalized protocols based on individual brain anatomy
- Automated safety verification pipeline
- Clinical validation through controlled trials


## Activation Keywords

- neuro-planner-llm-brain-interfaces
- neuro planner llm
- neuro planner llm brain interfaces


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Neuro Planner Llm Brain Interfaces

**Agent:** Neuro Planner Llm Brain Interfaces 是关于...
