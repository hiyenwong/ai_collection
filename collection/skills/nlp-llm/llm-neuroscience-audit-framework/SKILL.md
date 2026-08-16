---
name: llm-neuroscience-audit-framework
description: "Cross-family LLM-neuroscience audit framework."
metadata:
  arxiv_id: "2608.08159"
  published: "2026-08-08"
  authors: "Yuqi Wu, Shengming Zhao, Jie Chen"
  tags: [neuroscience, llm, ai-neuroscience, concept-steering, measurement-confounds, cross-family-audit]
license: Complete terms in LICENSE.txt
---

# LLM Neuroscience Audit Framework

This skill provides a comprehensive framework for auditing neuroscience-inspired claims in Large Language Models (LLMs) using rigorous, comparable measurements across multiple model families.

## Core Methodology

The framework addresses the main constraint in AI neuroscience: **lack of comparable measurements and adequate controls** rather than lack of phenomena. It audits four representative neuroscience-inspired paradigms:

1. **Causal steerability of concept directions**
2. **Linear geographic world map decoding**  
3. **Number magnitude encoding patterns**
4. **Language-specific structure localization**

## Implementation Guidelines

### 1. Cross-Family Model Selection
- Test across **17 models from 5 families** spanning **0.6B to 72B parameters**
- Include the **Qwen3 series** for scale trend analysis
- Ensure diverse architectural approaches (dense vs MoE, different training regimes)

### 2. Concept Steering Audit Protocol
**Critical confounds to control:**
- **Raw activation units**: Use residual-norm-comparable interventions instead of raw units
- **Readout metric**: Standardize across models  
- **Operating point**: Use held-out operating-point selection
- **Layer and coefficient**: Avoid fixed layer/coefficient assumptions

**Validation procedure:**
- With proper controls, concept steering remains significant at every scale
- No significant trend across Qwen3 series (confidence interval allows moderate positive slope)
- Raw pipeline shows false emergent capability pattern

### 3. Geographic World Map Validation
- A linear geographic world map is **consistently decodable** in every tested checkpoint up to 72B
- Use consistent stimuli and decoding methodology across all models
- Validate with held-out geographic locations

### 4. Number Magnitude Analysis  
- Number magnitude is **strongly encoded** across scales
- **Selection criterion determines neuron appearance**: bell-shaped vs monotonic responses depend on how neurons are selected
- Report selection methodology transparently

### 5. Language-Specific Structure Testing
- Language-specific structure is **localizable** but sensitive to attribution methods
- **Cross-lingual asymmetry direction reverses** under different attribution methods
- Always test multiple attribution approaches

## Best Practices

### Measurement Calibration
- **Never rely on single-model results** - always compare across families
- **Standardize intervention magnitudes** using residual norm comparability
- **Use held-out data** for operating point selection
- **Report confidence intervals** for all trend analyses

### Control Experiments
- Implement **uncalibrated baseline** (raw units, fixed layer/coefficient) to demonstrate confound effects
- Test **multiple attribution methods** for language structure claims  
- Validate findings with **different selection criteria** for neuron analysis

### Reporting Standards
- Release **protocol, stimuli, and code** publicly
- Document **all measurement choices** and their sensitivity
- Distinguish between **model properties** vs **measurement artifacts**

## Activation Keywords

- `llm neuroscience audit`
- `concept steering validation`  
- `cross-family model comparison`
- `measurement confounds llm`
- `neuroscience parallels llm`
- `ai neuroscience methodology`

## References

- **Original Paper**: Wu, Y., Zhao, S., & Chen, J. (2026). When Is a Steerable Concept Representation Real? Measurement Confounds in a Cross-Family Audit of Neuroscience Parallels in LLMs. arXiv:2608.08159
- **Protocol Repository**: Check for released code and stimuli from authors
- **Related Skills**: `llm-concept-neurons-control`, `llm-explanations-brain-alignment`, `brain-llm-alignment-training-data`

## Pitfalls to Avoid

1. **Single-model bias**: Claims based on one model family may reflect measurement choices rather than model properties
2. **Uncalibrated interventions**: Raw activation units create false scale trends
3. **Fixed operating points**: Can overestimate or underestimate effects
4. **Attribution method dependence**: Language structure findings reverse with different methods
5. **Selection criterion sensitivity**: Neuron response patterns depend on how they're selected

## Verification Steps

✅ Audit spans multiple model families (≥3)  
✅ Uses residual-norm-comparable interventions  
✅ Implements held-out operating point selection  
✅ Tests multiple attribution methods  
✅ Reports confidence intervals for trends  
✅ Releases protocol and code publicly