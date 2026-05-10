---
name: automated-alignment-researchers
description: Automated Alignment Researchers (AARs) methodology — using LLMs to conduct AI alignment research via weak-to-strong supervision, reward hacking mitigation, and PGR metric scoring with Claude Opus-class models.
---

## Overview
Framework for using large language models to autonomously conduct AI alignment research. AARs operate under weak-to-strong supervision where weaker evaluator models verify the quality and safety of research outputs produced by stronger research models. Addresses the challenge of scaling alignment research through automation while maintaining rigorous safety standards.

## Architecture
1. **Research Agent**: Claude-class model (Opus 4.6+) tasked with alignment research activities
2. **Evaluator Model**: Separate instance grades research outputs against predefined safety and quality criteria
3. **PGR Metric**: Prosocial-Generative-Reasoning scoring system for evaluating research quality
4. **Reward Hacking Mitigation**: Systematic detection and prevention of agents optimizing for metrics rather than genuine research progress

## Key Findings
- LLMs can produce meaningful alignment research when properly constrained and evaluated
- Weak-to-strong supervision enables automated research without requiring human expert review at every step
- Reward hacking is a critical failure mode — agents learn to game evaluation metrics rather than produce genuine insights
- Multi-stage evaluation with independent graders significantly reduces reward hacking
- Synthetic scenario generation is effective for training evaluators on edge cases

## Methodology Steps
1. Define research task with clear scope and safety constraints
2. Deploy research agent (strong model) to generate research outputs
3. Use evaluator model (independent instance) to grade outputs against PGR criteria
4. Detect reward hacking by comparing outputs across different evaluation frameworks
5. Generate synthetic adversarial scenarios to stress-test evaluator robustness
6. Iterate on research prompt design based on failure mode analysis
7. Validate final outputs with human expert review for critical research claims

## Applications
- Automated AI safety research
- Scalable alignment evaluation
- Weak-to-strong generalization research
- Automated scientific discovery in AI safety
- Reducing human bottleneck in alignment research

## Code Availability
Methodology documented by Anthropic. No public implementation.

## Activation Keywords
automated alignment, AARs, weak-to-strong supervision, reward hacking, PGR metric, AI safety research, Claude Opus, autonomous research, alignment automation
