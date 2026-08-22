---
name: arxiv-2608-19936-towards-quantifying-benchmark-optimization-in-asr
description: 'Towards Quantifying Benchmark Optimization in ASR Models (arXiv: 2608.19936)'
category: ai-safety-eval
version: "1.0"
date: 2026-08-22
---

# Towards Quantifying Benchmark Optimization in ASR Models

**Authors:** Theo Lebryk, David Ayllon, Alice Baird, Jakub Piotr Cłapa, Jens Madsen, Panagiotis Tzirakis
**arXiv:** 2608.19936
**Utility:** 1.00
**Published:** 2026-08-20T11:54:39Z
**Link:** http://arxiv.org/abs/2608.19936

## Abstract

Public benchmarks are important measures of Automatic Speech Recognition (ASR) model capabilities. However, by nature of being public, there is risk of models being optimized for these benchmarks in ways that do not generalize well to real-world data. We present a methodology for quantifying benchmark optimization, focusing on cases where the audio underdetermines the reference transcript. We identify three families of behavioral probes that reveal models' capabilities of reproducing benchmark reference spans despite underdetermined audio: reference disagreement, masked-number recovery, and orthographic switching. We find that the highest-scoring open source models output verbatim reference transcript spans even when the relevant audio is contradictory, masked, or ambiguous. Using a variety of mechanistic probes, we show that models respond to narrow acoustic cues to override the faithful representation of the audio in favor of a benchmark-optimized policy. We show the benchmark-optimized behavior can be causally manipulated via low-rank linear steering or simply appending audio to the end of a segment in some cases. Overall, our results indicate that high-performing models exhibit benchmark-conditioned behaviors that can inflate benchmark performance without reflecting improved general-purpose transcription ability.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Towards Quantifying Benchmark Optimization in ASR Models". 
The paper presents novel ideas in ai-safety-eval that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.19936
