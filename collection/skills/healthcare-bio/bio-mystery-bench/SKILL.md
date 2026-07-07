---
name: bio-mystery-bench
description: BioMysteryBench methodology for evaluating AI bioinformatics research capabilities. Tasks models with analyzing real-world biological datasets using method-agnostic, ground-truth-verified questions that allow superhuman evaluation.
---

## Overview

BioMysteryBench is a bioinformatics benchmark developed by Anthropic that evaluates AI models' ability to conduct professional-level scientific research. Unlike traditional benchmarks that use multiple-choice questions, BioMysteryBench tasks models with analyzing messy, real-world biological data to answer open-ended research questions with objectively verifiable answers. The benchmark consists of 99 questions spanning DNA/RNA sequencing, proteomics, and metabolomics, allowing for creative, method-agnostic problem solving while maintaining ground-truth evaluation.

## Architecture

BioMysteryBench has a tetrad of unique properties:

1. **Method-agnostic**: Models have unrestricted access to downloading tools and databases, graded on final answer rather than path taken
2. **Ground-truth answers**: Answers derived from controllable data properties or orthogonally validated metadata, not subjective scientist conclusions
3. **Superhuman question generation**: Questions sourced from controllable data properties without requiring humans to be able to solve them
4. **Validation notebooks**: Each question author submits a validation notebook proving the signal exists in the data

## Key Findings

- Frontier models (Claude Opus 4.6, Mythos Preview) perform on par with human domain experts on human-solvable problems
- Models solved significant fractions of human-difficult problems (Mythos Preview: 30% solve rate)
- Claude uses two primary strategies: vast knowledge base combining with live analysis, and multi-method convergence under uncertainty
- Model performance is strongly bimodal on human-solvable tasks (reliable retrieval), but shows "brittle wins" on difficult tasks (lucky reasoning paths)
- Models are improving across generations and outperforming panels of five domain experts on some tasks

## Methodology Steps

1. **Question Design**: Domain experts gather real datasets and create questions based on objective, controllable properties of the data
2. **Validation**: Each question requires a validation notebook demonstrating the signal exists in the data
3. **Execution Environment**: Models run in containers with canonical bioinformatics tools, pip/conda access, and database permissions (NCBI, Ensembl)
4. **Human Baselining**: Up to five domain experts attempt each question; questions solved by at least one human are classified as "human-solvable"
5. **Model Evaluation**: Each model attempts every problem five times; accuracy averaged across trials
6. **Reliability Analysis**: Per-problem solve counts categorized (0/5 through 5/5) to distinguish reliable solutions from brittle wins
7. **Strategy Analysis**: Model transcripts analyzed to identify reasoning patterns and compare with human approaches

## Applications

- Evaluating AI capabilities in bioinformatics and computational biology
- Benchmarking model improvements across generations for scientific reasoning
- Understanding AI vs. human problem-solving strategies in biology
- Identifying research areas where AI can outperform human experts
- Designing method-agnostic evaluations for open-ended scientific tasks
- Assessing model reliability vs. accuracy distinction on hard problems

## Code Availability

BioMysteryBench is accessible for researchers interested in understanding model performance on difficult verifiable computational biology tasks.

## Activation Keywords

BioMysteryBench, bioinformatics benchmark, AI for science, computational biology evaluation, agentic science benchmark, biological data analysis, method-agnostic evaluation, superhuman benchmarking, ground-truth science evaluation, model reliability analysis
