---
name: omniqec-ai-scientist-quantum-error-correction
description: OmniQEC methodology for discovering practical quantum error-correcting codes using an AI scientist framework with LLM orchestrator and slow-fast synergistic workflow.
---

# OmniQEC: Discovering Practical Quantum Error-Correcting Codes by an AI Scientist

## Overview
OmniQEC is an efficient AI scientist framework for discovering quantum error-correcting (QEC) codes suited to deployment on modern quantum processors. It formulates QEC design as an iterative discovery process where an orchestrator (implemented by advanced LLMs) coordinates code generation, code-level screening, syndrome extraction synthesis, and decoder-based circuit evaluation.

## Core Methodology

### Slow-Fast Synergistic Workflow
- **Fast loop**: Explores candidates using inexpensive code-level proxies
- **Slow loop**: Performs physically grounded circuit-level evaluation and feeds evidence back into the search

### Key Components
1. **Code Generation**: Creates candidate QEC codes from various construction families
2. **Code-Level Screening**: Filters candidates based on structural properties
3. **Syndrome Extraction Synthesis**: Designs hardware-efficient syndrome measurement circuits
4. **Decoder-Based Circuit Evaluation**: Tests logical performance under realistic noise models

## Applications
- Discovery of qLDPC codes that outperform existing benchmarks (BB codes)
- Hardware-friendly QEC implementations for practical quantum computing
- Co-design of codes, circuits, and decoders for optimal performance

## Activation Keywords
quantum error correction, QEC, qLDPC, AI scientist, LLM-assisted discovery, code-circuit-decoder co-design

## References
- arXiv:2607.25865 [quant-ph]
- Authors: Ge Yan, Shanchuan Li, Pengyue Ma, Qixin Zhang, Pingchuan Ma, Jianping Wang, Min-Hsiu Hsieh, Yuxuan Du
- Submitted: 28 Jul 2026