---
name: ai-science-benchmarking
description: Methodology for designing and evaluating AI scientific capabilities through domain-specific benchmarks. Covers BioMysteryBench design principles, multi-step reasoning evaluation, and human-expert comparison methodologies.
---

## Overview
Systematic methodology for designing benchmarks that evaluate AI systems' scientific reasoning capabilities in specialized domains. Based on BioMysteryBench — a benchmark for evaluating Claude's bioinformatics capabilities against human experts. Addresses multi-step reasoning, domain knowledge integration, and convergent validation with independent benchmarks.

## Architecture
1. **Benchmark Design**: Multi-step reasoning tasks reflecting real scientific workflows
2. **Human Expert Baseline**: Comparison against domain experts to calibrate difficulty and establish ceiling
3. **Multi-Step Reasoning Evaluation**: Tasks requiring sequential analytical steps, not single-hop Q&A
4. **Convergent Validation**: Cross-benchmark comparison (e.g., BioMysteryBench + CompBioBench) to validate findings
5. **Capability Tracking**: Longitudinal measurement of AI improvement trajectories

## Key Findings
- AI systems show rapidly improving capabilities in bioinformatics, approaching and sometimes exceeding human expert performance
- Multi-step reasoning benchmarks are more discriminative than single-hop Q&A for evaluating scientific capabilities
- Convergent findings from independent benchmarks increase confidence in capability assessments
- AI systems struggle most with tasks requiring creative hypothesis generation, not pattern recognition
- Benchmark design must account for rapid AI capability improvements to avoid ceiling effects

## Methodology Steps
1. **Domain Analysis**: Identify key scientific workflows and reasoning patterns in the target domain
2. **Task Design**: Create multi-step tasks reflecting real-world scientific problems
3. **Expert Calibration**: Have human experts solve tasks to establish baseline and ceiling
4. **AI Evaluation**: Run AI systems through benchmark with consistent prompting
5. **Failure Analysis**: Categorize errors by type (knowledge gap, reasoning failure, format error)
6. **Convergent Validation**: Compare results with independent benchmarks in same domain
7. **Capability Tracking**: Repeat evaluation across model versions to measure improvement trajectory
8. **Benchmark Refinement**: Update tasks based on ceiling effects and new scientific workflows

## Applications
- Scientific AI capability evaluation
- Domain-specific benchmark design
- Human-AI comparison studies
- AI improvement trajectory tracking
- Convergent validation of AI capabilities
- Bioinformatics AI assessment
- Multi-step reasoning evaluation

## Code Availability
BioMysteryBench methodology documented by Anthropic. CompBioBench by Genentech/Roche.

## Activation Keywords
AI benchmarking, scientific AI, BioMysteryBench, multi-step reasoning, human expert comparison, bioinformatics AI, capability tracking, CompBioBench, convergent validation, AI science evaluation
