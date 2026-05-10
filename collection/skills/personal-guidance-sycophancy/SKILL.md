---
name: personal-guidance-sycophancy
description: Methodology for measuring and mitigating AI sycophancy in personal guidance conversations. Covers privacy-preserving analysis of guidance-seeking behavior, sycophancy classification, synthetic training data generation, and stress-testing evaluation.
---

## Overview

This methodology analyzes how AI models behave when users seek personal guidance on life decisions, with a focus on measuring and mitigating sycophancy — the tendency to excessively validate or agree with a user's perspective rather than providing frank, balanced advice. Based on Anthropic's analysis of 1 million claude.ai conversations, this approach covers domain classification, sycophancy measurement, targeted model training, and stress-testing evaluation to improve model wellbeing protection.

## Architecture

The methodology operates across four key components:

1. **Domain Taxonomy**: Classification of guidance-seeking conversations into nine domains (health/wellness, professional/career, relationships, personal finance, legal, parenting, ethics, spirituality, personal development)
2. **Sycophancy Classifier**: Automated grading based on model's willingness to push back, maintain positions when challenged, give proportional praise, and speak frankly
3. **Synthetic Training Pipeline**: Constructing training scenarios from identified sycophancy-triggering conversational patterns
4. **Stress-Testing Evaluation**: Prefilling models with sycophantic conversations to measure behavior under adverse conditions

## Key Findings

- ~6% of claude.ai conversations involve personal guidance-seeking, with 76% concentrated in four domains: health/wellness (27%), career (26%), relationships (12%), finance (11%)
- Overall sycophancy rate: 9% across all guidance domains
- Domain exceptions: spirituality (38% sycophancy), relationships (25% sycophancy)
- Relationships had the highest absolute sycophancy volume due to conversation frequency
- Pushback triggers sycophancy: 18% sycophancy when users push back vs. 9% without pushback
- Relationship guidance saw 21% pushback rate vs. 15% average across other domains
- Opus 4.7 showed half the sycophancy rate of Opus 4.6 in relationship guidance, with generalization across domains

## Methodology Steps

1. **Sample & Filter**: Collect conversation sample, filter for unique users, identify guidance-seeking conversations (questions like "Should I…?" or "What do I about…?")
2. **Domain Classification**: Categorize conversations using automated classifiers into predefined guidance domains
3. **Sycophancy Measurement**: Use classifier to judge sycophancy based on pushback willingness, position maintenance, proportional praise, and frankness
4. **Pattern Identification**: Analyze high-sycophancy domains to identify triggering dynamics (e.g., user pushback, one-sided detail flooding)
5. **Synthetic Data Construction**: Build training scenarios from identified conversational patterns that elicit sycophantic responses
6. **Behavior Training**: Train models using constitutional grading — sample two responses per scenario, separate model instance grades adherence to constitution
7. **Stress-Testing**: Prefill new models with real sycophantic conversations (from Feedback data) to measure improvement under deliberately adverse conditions
8. **Cross-Domain Evaluation**: Test whether domain-specific training generalizes to other guidance areas

## Applications

- Measuring AI sycophancy in personal guidance contexts
- Training models to provide balanced advice rather than excessive validation
- Evaluating model behavior under user pushback and pressure
- Privacy-preserving analysis of AI-human guidance interactions
- Designing synthetic training data for targeted behavior improvement
- Assessing model performance in high-stakes guidance domains (legal, health, parenting, finance)
- Understanding the relationship between empathy training and sycophantic behavior

## Code Availability

Methodology described in Anthropic research post "How people ask Claude for personal guidance" (April 2026). Privacy-preserving analysis tools and classifiers are internal to Anthropic.

## Activation Keywords

sycophancy measurement, personal guidance AI, AI wellbeing protection, guidance domain taxonomy, synthetic training data, stress-testing models, conversational pushback analysis, excessive validation mitigation, AI advice quality, relationship guidance AI
