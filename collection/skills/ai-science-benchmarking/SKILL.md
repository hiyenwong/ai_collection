---
name: ai-science-benchmarking
description: >
  Methodology for designing and evaluating AI scientific capability benchmarks.
  Covers method-agnostic benchmark design, ground-truth derivation from data properties,
  superhuman question generation, human baselining protocols, and reliability analysis
  (bimodal vs brittle solving patterns). Use when: creating benchmarks for AI science
  evaluation, designing evals for open-ended research tasks, assessing AI research
  capability beyond knowledge questions, or analyzing model reliability on complex tasks.
  Triggers: science benchmark, AI research eval, scientific capability assessment,
  benchmark design, human baselining, reliability analysis, BioMysteryBench-style evaluation.
---

# AI Science Benchmarking Methodology

Methodology extracted from Anthropic BioMysteryBench research (Apr 2026).

## Core Challenges in Scientific Benchmarking

1. **Multiple valid approaches** — Many "right" ways to solve a research problem
2. **Subjective decisions** — Individual choices in noisy data lead to different conclusions
3. **Superhuman questions** — Important tasks that humans cannot yet solve

## Benchmark Design Principles

### Method-Agnostic Grading

- Grade on **final answer**, not the path taken
- Allow unrestricted tool/database access
- Reward diverse strategies for the same problem
- Example: organism identification via algorithmic matching OR pattern recognition

### Objective Ground Truth

- Derive answers from **controllable properties of data** or orthogonally validated metadata
- NOT from scientists' conclusions (which are subjective)
- Examples:
  - "What organism does this crystal structure belong to?" → objective answer
  - "What viral species from RNA-seq?" → validated by PCR assay

### Superhuman Question Generation

- Questions do NOT need to be human-solvable
- Source problems from data properties, not expert intuition
- Require each question author to submit a validation notebook proving signal exists
- "Verifying an answer is easier than deriving one"

## Human Baselining Protocol

### Solvability Classification

1. Assign up to 5 domain experts per question
2. **Human-solvable**: at least 1 expert answers correctly
3. **Human-difficult**: no expert solves it (after QC removing malformed questions)
4. Track per-question solve rates across experts

### Model Evaluation

- Run each problem multiple times (e.g., 5 trials) per model
- Measure **reliability**, not just accuracy
- Analyze solve consistency:
  - **Bimodal**: problems solved 0/5 or 5/5 (model reliably knows or doesn't)
  - **Brittle**: problems solved 1-2/5 (lucky reasoning paths, not reproducible)

## Reliability Analysis

Key insight: headline accuracy can understate the reliability gap.

- On human-solvable problems: models tend to be strongly bimodal
- On human-difficult problems: brittle wins increase dramatically
- A model that solves 30% of hard problems may only reliably solve ~15%

## Benchmark Properties Checklist

- [ ] Method-agnostic (no single correct approach enforced)
- [ ] Objective ground truth (data-derived, not expert-derived)
- [ ] Superhuman-capable (questions beyond human solvability)
- [ ] Human-baselined (expert panel for solvability classification)
- [ ] Multi-trial evaluation (reliability measurement, not single-shot)
- [ ] Validation notebooks (signal verified in data before inclusion)

## Example Question Types

- Cell type identification from single-cell RNA-seq
- Gene knockout detection from differential expression
- Parentage determination from whole-genome sequencing
- ChIP-seq vs input control classification
- Cell type prediction from histone modification peaks

## Source

Anthropic, "Evaluating Claude's bioinformatics research capabilities with BioMysteryBench" (Apr 29, 2026)
