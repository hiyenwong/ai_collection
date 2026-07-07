---
name: heterogeneous-neural-predictivity-lm
description: "Analysis framework for evaluating language model neural predictivity during naturalistic comprehension. Identifies heterogeneous brain-language alignment patterns across participants and brain regions, separating predictive usefulness from shared neural organization claims (arXiv: 2606.26880)"
metadata:
  arxiv_id: "2606.26880"
  authors: ["Xiao Jia"]
  published: "2026-06-25"
  source_url: "https://arxiv.org/abs/2606.26880"
  tags: ["neuroscience", "language models", "brain-language alignment", "naturalistic comprehension", "neural predictivity", "EEG", "MEG", "ECoG"]
  categories: ["cs.CL", "q-bio.NC", "cs.LG"]
  methodology: "Multi-dataset frozen LM analysis with controlled feature ablations and participant-level matching"
  datasets: ["Brain Treebank", "MEG-MASC", "Podcast ECoG"]
  models_tested: ["8 frozen language models", "blocked encoding models"]
  key_findings: "67/432 evaluable rows met controlled predictive criterion; participant-level advantages localized not uniform"
---

# Heterogeneous Neural Predictivity from Language Models

## Core Contribution

Demonstrates that language model representations can annotate neural activity during natural speech/text comprehension, but with critical caveats about interpretation.

## Methodology

### Multi-Dataset Framework
- Analyzed locked derived data from 3 datasets: Brain Treebank, MEG-MASC, Podcast ECoG
- Used 8 frozen language models with matched controls
- Controlled for temporal, nuisance, and representation-capacity confounds

### Evaluation Strategy
- Source-level summaries for held-out prediction
- Comparison against low-level baselines
- Feature ablations to test component-level sensitivity

### Control Conditions
- Brain-derived timing-linked controls
- Acoustic controls
- Implanted-signal controls
- Matched-capacity controls

## Key Findings

### Predictive Success
- 67 of 432 evaluable rows met controlled predictive-only criterion
- Positive held-out prediction widespread in source-level summaries
- Model-side feature ablations changed prediction scores in most evaluable rows

### Heterogeneity Pattern
- Participant-level matched-control advantages were **localized**, not uniform
- Response-profile and feature-specificity contrasts bounded interpretations
- Complete co-indexed integrated interpretation requires future jointly indexed coverage

## Critical Distinction

**Separates two claims:**
1. **Predictive usefulness**: LM features can predict neural activity ✓
2. **Shared organization**: LM features reveal neural computation mechanisms ✗ (not proven)

The framework explicitly distinguishes between using LMs as neural predictors vs. claiming they share neural computational principles.

## Implementation Guidance

### When to Use
- Evaluating LM neural predictivity in naturalistic settings
- Designing controlled brain-language alignment studies
- Interpreting heterogeneous alignment patterns across participants

### Methodology Steps
1. Select multiple frozen LMs across architecture families
2. Establish matched temporal and capacity controls
3. Test held-out prediction against low-level baselines
4. Perform feature ablations to verify component sensitivity
5. Analyze participant-level heterogeneity (don't assume uniform effects)
6. Separate predictive utility from mechanistic claims

### Pitfalls
- **Over-interpretation**: Predictive success ≠ shared computational mechanism
- **Uniformity assumption**: Effects are localized, not uniform across participants
- **Insufficient controls**: Must control for temporal, acoustic, and capacity confounds
- **Single-dataset claims**: Multi-dataset validation required for robust conclusions

## Applications

- Naturalistic neuroscience experimental design
- Brain-computer interface feature selection
- Language model evaluation for cognitive modeling
- Cross-participant neural pattern analysis

## Related Concepts

- Brain-language alignment
- Neural encoding models
- Naturalistic stimulus processing
- Frozen feature analysis
- Participant heterogeneity
