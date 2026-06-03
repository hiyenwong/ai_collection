---
name: effort-cognitive-cost-llm-alignment
description: Investigates whether Large Reasoning Model (LRM) chain-of-thought reasoning effort (inference-time compute budget) aligns with human cognitive costs. Finds that cognitive cost alignment between LRMs and humans is a training-time achievement, robust to inference-time perturbations, supporting compiled rather than online accounts of LRM problem-solving.
source: "arXiv: 2605.16938v1"
arxiv_id: "2605.16938"
authors: "Yueqing Hu, Tianhong Wang"
published: "2026-05-16"
category: "cs.CL, cs.AI, q-bio.NC"
---

# Effort as Ceiling, Not Dial: Reasoning Budget Does Not Modulate Cognitive Cost Alignment

## Overview

Large Reasoning Models (LRMs) generate chain-of-thought traces whose length tracks human reaction times across cognitive tasks. But does this alignment reflect genuine computational structure or just surface verbosity? This paper tests whether alignment varies with inference-time reasoning effort across multiple models, effort levels, and tasks.

## Key Contributions

1. **Invariant Alignment**: Within-task and cross-task alignment between LRM token counts and human RTs remains invariant across three effort levels (Bayes Factors lean toward null, mean alignment near-identical across conditions).

2. **Effort as Ceiling, Not Dial**: The effort parameter sets an **upper budget** on generation rather than driving real-time allocation — the allocation policy is crystallized at training time.

3. **Scale Improves Match**: Arithmetic complexity contrasts show token allocation tracks fine-grained, format-dependent human difficulty patterns, with model scale improving the match.

4. **Compiled vs. Online Account**: Cognitive cost alignment supports a **compiled** (training-time) rather than **online** (inference-time) account of LRM problem-solving.

## Methodology

### Experiment Design

- **Models tested**: GPT-OSS-20B and GPT-OSS-120B
- **Effort levels**: 3 inference-time compute budgets
- **Tasks**: 6 reasoning tasks spanning cognitive domains
- **Analysis**: Bayes Factors for null hypothesis testing across within-task and cross-task conditions

### Key Metrics

- **Token count vs. Human RT alignment**: Measured across effort conditions
- **Arithmetic complexity contrasts**: Format-dependent difficulty patterns (e.g., symbolic vs. numeric)
- **Manipulation check**: Verified that the effort parameter functions as a budget ceiling

### Statistical Framework

- Bayes Factors used to test null hypothesis of no alignment modulation
- Cross-task and within-task alignment invariance tested systematically
- Numerical near-identity across conditions demonstrated

## Key Results

1. **Primary finding**: LRM-human cost alignment does NOT vary with inference effort — effort is a ceiling, not a dial
2. **Training-time crystallization**: The allocation policy is fixed during training, not dynamically re-allocated at inference
3. **Scale benefits**: Larger models (120B) show better fine-grained alignment with human difficulty patterns
4. **Format effects**: Token allocation tracks format-dependent difficulty (symbolic vs. numeric arithmetic)

## Implications

### For Neuroscience / Cognitive Science

- Supports **compiled cognition** models over online resource allocation models in AI systems
- Suggests that human-like reasoning patterns in LLMs emerge from training dynamics, not explicit inference-time control
- Provides experimental framework for testing alignment between artificial and human cognitive architectures

### For AI Safety / Alignment

- Inference-time compute controls may not affect the *nature* of alignment with human cognition
- Safety interventions targeting inference-time reasoning may need to address training-time crystallized patterns

## Activation

Cognitive cost alignment, LRM reasoning budget, chain-of-thought, reaction time alignment, compiled cognition, cognitive modeling, human-AI alignment

## Related Skills

- [[vlm-lam-brain-alignment]] - Brain alignment of VLM/LAM during gameplay
- [[computational-neuroscience-in-llm-era]] - Computational neuroscience in LLM era
- [[naturalistic-computational-cognitive-science]] - Naturalistic computational cognitive science

## References

- Hu, Y. & Wang, T. (2026). Effort as Ceiling, Not Dial: Reasoning Budget Does Not Modulate Cognitive Cost Alignment Between Humans and Large Reasoning Models. arXiv:2605.16938v1 [cs.CL, cs.AI, q-bio.NC].
