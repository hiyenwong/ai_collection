---
name: vibe-calibration
description: "Vibe Calibration methodology for autonomous quantum processor bring-up using LLM skill orchestration. Distills expert tacit knowledge into reusable calibration skills for superconducting quantum processors. Use when designing autonomous calibration systems for quantum hardware, LLM-orchestrated experimental control, or skill-based bring-up workflows for complex scientific instruments. Triggers: quantum calibration, autonomous bring-up, LLM agent experiment, superconducting qubit, skill orchestration, quantum processor tuning, vibecoding calibration."
---

# Vibe Calibration

Methodology from arXiv:2606.22376v1 (Jun 21, 2026) — Autonomous Bring-up of a 112-Qubit Superconducting Quantum Processor by a Skill-Orchestrating Language Agent.

## Core Problem

Scaling superconducting quantum processors (>100 qubits) faces a calibration bottleneck: conventional scripts are brittle to anomalous signals, and expert judgment cannot keep pace with system scale.

## Key Innovation

Vibe Calibration uses **LLM agents to orchestrate reusable calibration skills**, distilling expert tacit knowledge into structured, composable workflows. The system achieved autonomous bring-up of a 112-qubit processor.

## Architecture

### 1. Skill Library
- Pre-defined calibration primitives (e.g., frequency find, Rabi calibration, Ramsey tuning)
- Each skill encapsulates: procedure, success criteria, failure recovery
- Skills are composable — higher-level skills chain lower-level ones

### 2. LLM Orchestrator
- LLM agent selects and sequences skills based on system state
- Interprets measurement data qualitatively (beyond threshold-based scripts)
- Adapts strategy when anomalies are detected
- Maintains calibration state across the full bring-up process

### 3. Closed-Loop Execution
```
Measure → LLM interprets → Select skill → Execute → Evaluate → Iterate
```

### 4. Knowledge Distillation
- Expert tacit knowledge → Structured skill descriptions
- Natural language skill specifications → Executable procedures
- Failure modes captured as skill-specific recovery strategies

## Key Principles
- **Skill-based modularity**: Decompose calibration into reusable, composable skills
- **LLM as interpreter**: Use LLMs to interpret qualitative measurement patterns
- **Tacit knowledge capture**: Encode expert intuition into structured skill descriptions
- **Adaptive sequencing**: Let the orchestrator decide skill order dynamically

## Application Domains
- Superconducting quantum processor calibration
- Any complex experimental system requiring expert tuning
- LLM-orchestrated scientific automation
- Skill-based autonomous experimental workflows

## Activation
Keywords: quantum calibration, autonomous bring-up, LLM agent experiment, superconducting qubit, skill orchestration, vibecoding, quantum processor tuning, autonomous experiment
