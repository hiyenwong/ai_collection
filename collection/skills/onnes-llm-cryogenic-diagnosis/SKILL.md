---
name: onnes-llm-cryogenic-diagnosis
description: "Physics-grounded digital twin + multi-agent LLM simulator for cryogenic fault diagnosis in quantum computing infrastructure. Use when analyzing dilution refrigerator fault diagnosis, multi-agent LLM operations for quantum hardware, digital twin simulators for quantum systems, or cryogenic infrastructure monitoring."
---

# Onnes LLM Cryogenic Diagnosis

## Overview
Methodology from arXiv:2607.05805 (July 2026) for using physics-grounded digital twin simulators combined with multi-agent LLM systems for fault diagnosis in quantum computing cryogenic infrastructure.

## Core Architecture
1. **Physics-Grounded Digital Twin**: Forward physics model of dilution refrigerator with learned noise fingerprint from real operational logs
2. **Multi-Agent LLM Operations Layer**: Zero-shot LLM panel for fault detection and classification
3. **Hybrid Fault Classes**: Engineered fault classes that separate on flow/pressure when overlapping on temperature

## Key Results
- Zero-shot LLM panel matches supervised ML classifier on detection (no significant difference)
- Classification accuracy raised from 0.685 to 0.990 with few-shot demonstrations (6 labeled examples)
- Self-consistency voting improves classification without parameter updates
- Real-hardware validation: 6.4% false-alarm rate, 100% recall on injected physics faults
- Confidence gate suppresses pre-onset false alarms

## Implementation Pattern
1. Build forward physics model of target system
2. Learn noise/correlation fingerprint from operational logs
3. Define fault classes with overlapping symptoms on different axes
4. Deploy zero-shot LLM panel for initial detection
5. Add curated contrastive few-shot demonstrations for classification
6. Implement self-consistency voting for reliability
7. Add confidence gate for false-alarm suppression
8. Validate on real hardware telemetry

## Activation
dilution refrigerator, cryogenic fault diagnosis, quantum computing infrastructure, digital twin quantum, multi-agent LLM operations, Onnes, physics-grounded simulator, fault classification, BlueFors logs
