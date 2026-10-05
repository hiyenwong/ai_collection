---
name: arxiv-2610-02734v1-smp-syndrome-motif-projection-circuit-level-qec
description: "SMP: General hyperedge-based framework for circuit-level QEC — linear-complexity preprocessing, 77.8% failure reduction for color codes, works with Google Willow data"
tags: [arxiv, quantum, qec, decoding, hyperedge-faults, surface-code, color-code, google-willow]
arxiv_id: "2610.02734v1"
utility: 0.87
date_added: "2026-10-05"
---

# SMP: Syndrome Motif Projection for Circuit-Level Quantum Error Correction

**arXiv:** 2610.02734v1 | **Utility:** 0.87 | **Date:** 2026-10-05

## Abstract

SMP introduces a general framework for incorporating hyperedge information into matching-based decoding for circuit-level QEC. A hyperedge fault produces a characteristic local syndrome motif; observing such a motif provides evidence for the corresponding fault. SMP extracts this information with linear-complexity preprocessing while preserving the matching backend.

## Key Contributions

- **Hyperedge handling**: Addresses the major challenge of correlated multi-detection-event faults in circuit-level decoding
- **Linear-complexity preprocessing**: Lightweight front-end compatible with existing scalable matching decoders
- **Color code breakthrough**: SMP + Chromobius reduces logical failure probabilities by up to 77.8%
- **Gate circuit improvement**: 35.5% failure probability reduction for six-CNOT circuits
- **Validated on Google Willow**: Improves both standard and correlated matching on experimental surface code data

## Methods

1. **Syndrome motif**: Characteristic local pattern produced by hyperedge faults
2. **Motif detection**: Scans syndrome for matching patterns
3. **Weight update**: Maps motif evidence onto matching edge weights
4. **Backend-agnostic**: Works with any matching-based decoder (standard, correlated, Chromobius)

## Relevance

Practical, deployable improvement for QEC decoding. Unlike belief matching (which requires iterative inference on Tanner graph), SMP uses direct local updates — making it compatible with real-time decoding requirements. The 77.8% improvement for color codes is substantial. The fact that it works as a "plug-in" to existing decoders makes adoption straightforward. Important for anyone implementing fault-tolerant quantum computation.
