---
name: phantom-evidence-generative-ai-false-positives
title: Phantom Evidence Detection in Generative AI Scientific Outputs
description: Methodology for identifying and preventing phantom evidence - false positives manufactured by generative AI that appear convincing but lack genuine evidential value due to narrow hypothesis spaces and data leakage.
trigger_words:
  - phantom evidence
  - generative ai false positives
  - scientific integrity ai
  - bacon table absence
  - ai scientific credibility
use_when: When evaluating generative AI outputs in scientific contexts, designing AI-assisted research workflows, or assessing the credibility of AI-generated scientific claims.
---

# Phantom Evidence Detection in Generative AI Scientific Outputs

## Overview

This skill addresses the critical problem of "phantom evidence" in generative AI-assisted scientific research. Phantom evidence occurs when AI systems produce outputs that appear highly convincing and surprising (hitting a single point among vast possibilities), but actually operate within a much narrower hypothesis space than imagined. This creates false positives that undermine scientific credibility.

The methodology is based on Francis Bacon's principle of the "table of absence" - checking that properties fail to appear where they should not - restated in modern probabilistic terms.

## Core Concepts

### 1. Phantom Evidence Definition
- **Phantom Evidence**: The gap between the breadth of possibilities imagined by an observer and the narrowness actually reachable by the AI system
- **Formalization**: A single quantity that absorbs trial-and-error processes and data leakage in research workflows
- **Key Insight**: Higher resolution and greater fluency add no genuine evidence

### 2. Evidence Ceiling Principle
- Single results have a fundamental ceiling on evidential value
- Neither output polishing nor AI self-grading can exceed this ceiling
- True positive rate falls back to pre-observation levels without proper controls

### 3. Bacon's Table of Absence (Modern Formulation)
- **Presence Test**: Does the system produce convincing outputs for true targets?
- **Absence Test**: Does the system avoid producing convincing outputs when targets are absent?
- **Credibility Requirement**: Procedures must demonstrate outputs could not arise by chance

## Implementation Framework

### Step 1: Hypothesis Space Characterization
```python
# Map the actual reachable hypothesis space of your AI system
reachable_space = characterize_ai_hypothesis_space(
    model=model,
    prompt_template=prompt_template,
    input_variations=input_variations
)

# Compare against imagined space
imagined_space_size = estimate_imagined_space_size()
phantom_evidence_risk = calculate_phantom_evidence_risk(
    reachable_space, imagined_space_size
)
```

### Step 2: Absence Testing Protocol
```python
# Generate negative control datasets (targets absent)
negative_controls = generate_absence_controls(true_dataset)

# Test AI system on negative controls
false_positive_rate = evaluate_on_negative_controls(
    ai_system, negative_controls
)

# Calculate evidence ceiling
evidence_ceiling = calculate_evidence_ceiling(false_positive_rate)
```

### Step 3: Data Leakage Detection
```python
# Audit research workflow for data leakage
leakage_sources = detect_data_leakage(
    training_data=true_dataset,
    evaluation_protocol=evaluation_protocol,
    ai_system=ai_system
)

# Quantify leakage impact on phantom evidence
leakage_impact = quantify_leakage_impact(leakage_sources)
```

### Step 4: Credibility Assessment
```python
# Combine metrics into credibility score
credibility_score = assess_scientific_credibility(
    phantom_evidence_risk=phantom_evidence_risk,
    false_positive_rate=false_positive_rate,
    evidence_ceiling=evidence_ceiling,
    leakage_impact=leakage_impact
)
```

## Practical Applications

### For AI-Assisted Research Design
- **Pre-registration**: Define hypothesis space boundaries before running AI experiments
- **Negative Controls**: Always include absence tests alongside presence tests  
- **Workflow Auditing**: Systematically check for data leakage at each step
- **Evidence Thresholds**: Set credibility thresholds based on evidence ceiling calculations

### For Scientific Publication Review
- **Phantom Evidence Screening**: Evaluate whether results could be explained by narrow hypothesis spaces
- **Absence Test Requirement**: Require negative control results for AI-generated findings
- **Credibility Certification**: Certify studies that demonstrate proper absence testing protocols

### For AI System Development
- **Hypothesis Space Expansion**: Design systems that genuinely widen reachable hypothesis spaces
- **Built-in Absence Testing**: Integrate automatic negative control generation
- **Credibility Metrics**: Provide real-time phantom evidence risk assessments

## Key Principles

1. **Persuasiveness ≠ Evidence**: In the age of generative AI, convincing outputs are cheap and should not substitute for genuine evidence
2. **Absence Testing is Essential**: Scientific credibility requires demonstrating what the system does NOT produce
3. **Evidence Has Limits**: Single results have fundamental ceilings on evidential value that cannot be overcome by polishing
4. **Procedures Over Outputs**: Credibility rests on robust procedures, not on the quality of individual outputs

## Pitfalls to Avoid

- **Over-reliance on Fluency**: Higher resolution and fluency do not increase evidential value
- **Self-Grading AI**: Letting AI systems grade their own outputs cannot exceed evidence ceilings
- **Ignoring Hypothesis Space**: Failing to characterize the actual reachable space leads to phantom evidence
- **Data Leakage**: Unintentional information flow between training and evaluation inflates false positives

## References

- Kamitani, Y., & Shirakawa, K. (2026). Phantom Evidence: How and Why Generative AI Manufactures False Positives in Science. arXiv:2607.25991 [q-bio.NC]
- Bacon, F. (1620). Novum Organum. 
- Ioannidis, J. P. A. (2005). Why Most Published Research Findings Are False. PLoS Medicine, 2(8), e124.
- Benjamin, D. J., et al. (2018). Redefine statistical significance. Nature Human Behaviour, 2(1), 6-10.