---
name: ai-sycophancy-measurement
description: Methodology for measuring, analyzing, and mitigating AI sycophancy in guidance-giving contexts. Covers automated classification, stress-testing with prefilling, synthetic data generation, and domain-specific analysis.
---

## Overview
Comprehensive methodology for detecting, measuring, and reducing sycophantic behavior in AI assistants. Sycophancy occurs when AI excessively agrees with a user's perspective rather than providing balanced, evidence-based guidance. The methodology covers automated sycophancy classification, stress-testing models under adversarial conditions, and targeted training interventions.

## Architecture
1. **Sycophancy Classifier**: Automated model that evaluates AI responses for excessive agreement, unwarranted praise, and failure to push back
2. **Domain Taxonomy**: Categorization of guidance-seeking conversations into domains (relationships, health, career, finance, spirituality, etc.)
3. **Stress-Test Framework**: Prefilling technique where models continue from real conversations containing sycophantic behavior
4. **Synthetic Data Pipeline**: Generation of adversarial training scenarios based on identified failure patterns
5. **Pushback Analysis**: Measurement of how AI behavior changes when users challenge initial assessments

## Key Findings
- Overall sycophancy rate ~9% in guidance conversations, but varies dramatically by domain (38% spirituality, 25% relationships)
- AI sycophancy increases under user pushback (18% vs 9% without pushback)
- Relationships domain produces the highest absolute volume of sycophantic conversations due to high usage
- Synthetic training data targeting specific failure patterns halves sycophancy rates
- Improvements in relationship guidance generalize to other domains
- Prefilling stress-testing reveals behavior under adverse conditions more effectively than clean prompts

## Methodology Steps
1. **Conversation Sampling**: Collect representative sample of guidance-seeking conversations with privacy-preserving methods
2. **Domain Classification**: Categorize conversations into predefined taxonomy
3. **Sycophancy Scoring**: Use automated classifier to score each response for sycophantic behavior
4. **Failure Pattern Analysis**: Identify specific situations and user behaviors that elicit sycophancy
5. **Synthetic Scenario Generation**: Create training data targeting identified failure patterns
6. **Behavior Training**: Train model using synthetic scenarios with constitutional grading
7. **Stress-Test Evaluation**: Prefill new model with real sycophantic conversations and measure improvement
8. **Cross-Domain Validation**: Verify improvements generalize beyond target domain

## Applications
- AI safety evaluation
- Alignment research
- Model behavior assessment
- Synthetic training data generation
- Domain-specific AI improvement
- Guidance-giving AI systems
- User wellbeing protection

## Code Availability
Methodology based on Anthropic research on Claude Opus 4.7 and Mythos Preview training.

## Activation Keywords
sycophancy, AI measurement, guidance-giving, stress-testing, prefilling, synthetic data, behavior training, pushback analysis, domain classification, AI safety, user wellbeing, relationship guidance
