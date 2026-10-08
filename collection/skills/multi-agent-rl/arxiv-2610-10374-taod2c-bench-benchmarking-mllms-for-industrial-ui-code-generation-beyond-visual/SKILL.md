---
name: arxiv-2610-10374-taod2c-bench-benchmarking-mllms-for-industrial-ui-code-generation-beyond-visual
description: 'TaoD2C-Bench: Benchmarking MLLMs for Industrial UI Code Generation Beyond Visual Fidelity (arXiv: 2610.10374)'
metadata:
  {
    "arxiv_id": "2610.10374",
    "utility": 1.0,
    "title": "TaoD2C-Bench: Benchmarking MLLMs for Industrial UI Code Generation Beyond Visual Fidelity",
    "authors": "Chengwei Shi, Yunnong Chen, Tingting Zhou, Qiang Lu, Shiyu Yue...",
    "url": "https://arxiv.org/abs/2610.10374v1",
    "categories": ["cs.SE", "cs.AI"],
    "published": "2026-10-07"
  }
---

# TaoD2C-Bench: Benchmarking MLLMs for Industrial UI Code Generation Beyond Visual Fidelity

**arXiv ID:** 2610.10374
**Authors:** Chengwei Shi, Yunnong Chen, Tingting Zhou, Qiang Lu, Shiyu Yue...
**URL:** https://arxiv.org/abs/2610.10374v1
**Utility Score:** 1.00
**Published:** 2026-10-07
**Categories:** cs.SE, cs.AI

## Summary

A key challenge for multimodal large language models (MLLMs) is moving beyond visual recognition to constraint-aware cross-modal reasoning. This involves combining visual cues with information from other modalities to understand elements' relationships under domain-specific rules. This challenge is acutely evident in industrial design-to-code (D2C), which converts user interface (UI) designs into code and requires MLLMs to connect design images with disorganized layer metadata, infer component and layout implementation requirements, and realize them in code under target-library constraints. However, these capabilities remain insufficiently evaluated in realistic industrial settings. To fill this gap, we present TaoD2C-Bench, a benchmark for evaluating MLLMs' ability to generate UI code that satisfies implementation requirements in industrial applications. The TaoD2C dataset consists of 2,861 production designs from 17 commercial platforms with 97,652 expert annotations across four categories: Component, Group, Alignment, and Position. These annotations distinguish required constraints from permitted implementation choices. TaoD2C-Bench defines three tasks: end-to-end UI code generation, requirement inference, and requirement realization. Evaluating eight MLLMs reveals substantial gaps in generating UI code that satisfies implementation requirements, alongside distinct performance profiles in inference and realization. We further show that MLLMs' visual reconstruction ability does not necessarily imply an ability to generate code that meets these requirements. We release TaoD2C to support research on industrial UI code generation.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10374v1
