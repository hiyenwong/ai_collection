---
name: do-llm-generated-skills-make-better-ai-data-scientists-a-component-ablation
description: 'Product data scientists often ask LLM-based agents to help with recurring execution tasks such as cleaning data, writing SQL, choosing statistical tests, and formatting results. Reusable skill files a. Based on arXiv:2607.07504.'
---

# Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-Science Workflows

**arXiv**: 2607.07504 | **Authors**: Wei-Jung Huang | **Utility**: 0.87

## Overview

Product data scientists often ask LLM-based agents to help with recurring execution tasks such as cleaning data, writing SQL, choosing statistical tests, and formatting results. Reusable skill files are meant to avoid prompting from scratch by packaging guidance for a task family. Expert-written skills can encode high-quality guidance, but writing and maintaining them across many data-science task families creates a manual bottleneck. We ask whether LLM-generated skills offer a useful low-curation alternative: do they improve performance over the task prompt alone? We test this question across four lifecycle stages: data preparation, data extraction, statistical analysis, and reporting, using one generated skill per stage. We find no reliable improvement from full generated skills over No-Skill prompting. We then ask whether any part of the skill is useful by ablating different skill components. The main ablation covers 56 tasks, nine model configurations, and three providers, yielding 7,560 runs. Compared with prompting using the task alone, neither the full generated skill nor any ablated skill variant significantly improves performance; all p-values are at least 0.396, and the total spread across variants is only 1.2 pp. A supplemental token-matched control adds 1,512 runs and finds that Full skills perform similarly to task-irrelevant skill-formatted content. The results caution against using one LLM-generated skill per data-science workflow as a default single-shot prompting strategy.

## Key Contributions

1. Product data scientists often ask LLM-based agents to help with recurring execution tasks such as cleaning data, writing SQL, choosing statistical tests, and formatting results.
2. Reusable skill files are meant to avoid prompting from scratch by packaging guidance for a task family.
3. Expert-written skills can encode high-quality guidance, but writing and maintaining them across many data-science task families creates a manual bottleneck.
4. We ask whether LLM-generated skills offer a useful low-curation alternative: do they improve performance over the task prompt alone? We test this question across four lifecycle stages: data preparation, data extraction, statistical analysis, and reporting, using one generated skill per stage.

## Implementation Notes

- **Keywords**: llm, skill-library
- **Categories**: cs.AI
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm, skill-library.
