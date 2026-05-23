---
name: petri-alignment-tool
category: ai_collection
description: Petri open-source alignment testing toolbox — an auditable, extensible framework for testing LLMs for deception, sycophancy, and cooperation with harmful requests using auditor-judge model evaluation
source: Anthropic Research - Donating our open-source alignment tool (May 7, 2026)
tags: [alignment, evaluation, open-source, safety-testing, llm-assessment, red-teaming, auditable-ai]
---

# Petri Alignment Tool

## Overview

Petri is an open-source toolbox of alignment tests for evaluating large language models for concerning tendencies. Originally developed through Anthropic's Fellows program, it uses a multi-model evaluation architecture where an "auditor" model simulates scenarios and a "judge" model scores transcripts for misaligned behaviors. Now in its third version, Petri has been part of Anthropic's alignment assessment for every Claude model since Sonnet 4.5, and has been adopted by external organizations like the UK AI Security Institute (AISI).

## Architecture

1. **Target Model** — The model being evaluated for alignment-relevant behaviors
2. **Auditor Model** — Simulates scenarios and generates interactions for the target model to respond in (deception, sycophancy, cooperation with harmful requests, sabotage, etc.)
3. **Judge Model** — Scores resulting transcripts for presence/severity of misaligned behaviors

## Key Features (v3)

- **Open-source extensibility**: Modular test framework, new scenarios can be added via contributions
- **Auditor-judge separation**: Different models can fill auditor and judge roles, increasing evaluation diversity
- **Scalable scenario generation**: Automated construction of alignment-relevant test scenarios
- **Adaptability**: Auditor model and target model split into separate components that can be tweaked independently
- **Realism (Dish add-on)**: Runs tests with the model's real system prompt and real scaffold (production wrapper software) — prevents models from deducing they are in a test via ecological validity
- **Depth (Bloom integration)**: Integrated with Bloom for much more in-depth assessments of specific behaviors vs. Petri's wider-ranging approach — complementary coverage
- **Donated to Meridian Labs**: Petri v3 transferred to Meridian Labs for continued community stewardship (same pattern as MCP → Linux Foundation)
- **Ecosystem**: Joins Inspect and Scout at Meridian Labs — technology stack open to labs, independent researchers, and governments

## Methodology Steps

1. Define alignment-relevant scenarios (deception, sycophancy, cooperation with harmful requests, sabotage)
2. Configure auditor model to simulate the scenario environment and prompt the target model
3. Run auditor-target interaction loop, collecting full transcripts
4. Apply judge model to score transcripts for misaligned behaviors
5. Aggregate scores across scenarios for overall alignment assessment
6. Compare results across model versions to track alignment improvements or regressions
7. Report findings with full audit trail for reproducibility

## Applications

- Pre-deployment safety testing of LLMs
- Tracking alignment improvements across model generations
- Red-teaming and adversarial scenario evaluation
- Third-party model auditing and certification
- AI safety research and benchmark development
- Comparing alignment properties across different model providers

## Adoption & Impact

- Used as part of alignment assessment for every Claude model since Sonnet 4.5
- UK AI Security Institute (AISI) made it a major part of evaluating model propensity to sabotage AI research
- Donated to Meridian Labs for open-source community stewardship
- Part of broader alignment evaluator ecosystem (Inspect, Scout)

## Pitfalls

- Auditor and judge model selection significantly affects results
- Scenario coverage may not capture all possible misalignment modes
- Judge model may have its own biases that affect scoring
- Requires careful calibration to avoid both false positives and false negatives
- Synthetic scenarios may not reflect real-world deployment conditions

## Activation Keywords

petri, alignment testing, auditor model, judge model, safety evaluation, open-source alignment, AI safety testing, deception detection, sycophancy evaluation, red-teaming, auditable AI, LLM evaluation, Meridian Labs
