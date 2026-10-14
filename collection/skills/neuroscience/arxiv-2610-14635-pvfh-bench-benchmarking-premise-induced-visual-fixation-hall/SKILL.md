---
name: arxiv-2610-14635-pvfh-bench-benchmarking-premise-induced-visual-fixation-hall
description: 'PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Visio (arXiv: 2610.14635)'
metadata:
  {
    "arxiv_id": "2610.14635",
    "utility": 1.0,
    "title": "PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.14635"
  }
---

# PVFH-Bench: Benchmarking Premise-Induced Visual Fixation Hallucinations in Vision-Language Models

**arXiv ID:** 2610.14635
**URL:** https://arxiv.org/abs/2610.14635
**Utility Score:** 1.00

## Abstract

Large Vision-Language Models (LVLMs) have achieved remarkable progress across a wide range of multimodal tasks. However, object hallucination remains a persistent challenge, undermining model reliability in applications such as visual question answering, embodied agents, and human-AI decision support systems. In this paper, inspired by cognitive science studies on perceptual bias, we investigate a new failure mode termed Premise-Induced Visual Fixation Hallucination (PVFH). Specifically, PVFH refers to a premise-induced reasoning error in which models become anchored to visually confusable evidence, accept a false textual premise, and subsequently generate responses about an absent yet visually plausible object. To systematically study this phenomenon, we introduce PVFH-Bench, a benchmark that automatically constructs visually confusable but absent targets and pairs the core hallucination setting with diagnostic subsets to trace how models move from object recognition to Premise-Induced Visual Fixation Hallucination. Experimental results on 10 state-of-the-art LVLMs demonstrate that all evaluated models are highly vulnerable to Premise-Induced Visual Fixation Hallucination. Moreover, we find that explicit chain-of-thought reasoning can further exacerbate this failure mode by encouraging models to overinterpret weak visual cues as supporting evidence for hallucinated objects.

## Key Topics

benchmark, vision, multimodal, ppo, embodied

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.14635
