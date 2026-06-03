---
name: bio-mystery-bench
description: BioMysteryBench methodology for benchmarking LLM bioinformatics research capabilities on real-world, open-ended problems. Addresses three key challenges in scientific benchmarking: (1) multiple valid approaches to the same problem, (2) subjective research decisions in noisy datasets, (3) unsolved biological questions. Use when: evaluating AI scientific capabilities, designing research benchmarks, bioinformatics evaluation, agentic science assessment, or measuring AI performance on open-ended research tasks.
---

# BioMysteryBench: Benchmarking AI Bioinformatics Research

## The Challenge of Scientific Benchmarks

Three properties make biological research especially hard to benchmark:

### 1. Multiple Valid Approaches
- Same research question can be tackled via GWAS, microbiome sequencing, etc.
- Approach depends on expertise, resources, and research taste
- BixBench handles this by grading conclusions, not methods
- Tradeoff: conclusions reflect subjective choices made along the way

### 2. Subjective Decisions Lead to Different Conclusions
- Small analysis differences can flip conclusions in noisy biological datasets
- Example: metformin response prediction — three studies, three different answers
- SciGym avoids this by using simulated biology with ground-truth
- Tradeoff: unclear if simulated performance tracks real-data performance

### 3. Unsolved Problems
- Most impactful tasks are ones humans haven't solved yet
- Cannot use expert intuition as ground-truth
- Solution: ground benchmarks in experimental measurements
  - ProteinGym: mutation fitness via Deep Mutational Scanning
  - CASP: protein folding against unpublished crystal structures

## Benchmarking Strategy

**BioMysteryBench approach**:
- Tasks Claude with analysis of real-world biological datasets
- Evaluates creative solutions to open-ended problems
- Grounds evaluation in verifiable biological outcomes

## Key Findings

- Claude's biological capabilities improve rapidly across generations
- Current models perform on par with human experts
- Latest generations solved problems that human expert panels could not
- Models sometimes used very different strategies than humans

## Benchmark Design Principles for Scientific Tasks

1. **Ground in data, not just expert opinion** — use experimental measurements as ground-truth
2. **Allow multiple solution paths** — grade on correctness, not methodology
3. **Include unsolved problems** — test where models could surpass human capability
4. **Handle ambiguity gracefully** — noisy real-world data should be part of the evaluation
5. **Compare to human baselines** — include expert panels for comparison

## Comparison with Other Benchmarks

| Benchmark | Tests | Limitation |
|-----------|-------|------------|
| MMLU-Pro | Expert knowledge | Self-contained Q&A only |
| GPQA | Graduate-level questions | Google-proof but still Q&A |
| LAB-Bench | Biology knowledge work | Reading figures, protocols |
| BLADE | Dataset analysis | Checks if steps match human |
| BixBench | Biological datasets | Grades conclusions (subjective grader) |
| SciGym | Simulated lab | Simulated, not real data |
| BioMysteryBench | Real-world open problems | Novel approach |
