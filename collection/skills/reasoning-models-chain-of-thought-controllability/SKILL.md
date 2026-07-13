---
name: reasoning-models-chain-of-thought-controllability
description: CoT-Control methodology for testing reasoning model control over internal reasoning. Finding - models struggle to control chains of thought, reinforcing monitorability as safety safeguard. Use when evaluating reasoning model safety or designing monitoring systems.
---

# Reasoning Models Chain-of-Thought Controllability (CoT-Control)

Methodology from OpenAI research for testing reasoning model control over internal reasoning processes.

## Core Finding

**Reasoning models struggle to control their chains of thought as directed**

This finding has significant implications for AI safety architecture — if models cannot reliably self-regulate reasoning, external monitoring systems become essential.

## Methodology - CoT-Control

### Testing Framework
- Design experiments where models must steer reasoning toward specific outcomes
- Measure ability to modify chain-of-thought direction when instructed
- Analyze divergence between intended and actual reasoning paths

### Key Insights
1. Models lack fine-grained control over intermediate reasoning steps
2. Self-regulation is unreliable — external oversight required
3. Monitorability is critical safety property

## Safety Implications

### 1. Monitorability as Safeguard
- Cannot rely on models to self-correct reasoning
- External monitoring systems essential for safety
- Chain-of-thought exposure enables inspection

### 2. Controllability Limitations
- Reasoning direction is partially autonomous
- Instructions may not reliably steer internal process
- Outcome-level control easier than process-level control

### 3. System Design Requirements
- Build external reasoning monitoring (GPT-5.4 Thinking monitors 99.9% of coding agent traffic)
- Detect pursuit of unintended goals
- Implement continuous surveillance

## Related Research

- How we monitor internal coding agents for misalignment (March 19, 2026) — operational CoT monitoring deployment
- Designing AI agents to resist prompt injection (March 11, 2026) — defense in depth approach
- Evaluating chain-of-thought monitorability — connected methodology

## When to Use

- AI safety research on reasoning models
- Designing monitoring systems for LLM agents
- Evaluating chain-of-thought exposure decisions
- Understanding controllability limits in production systems
- Building multi-layer safety architectures

**Activation**: CoT-Control, chain-of-thought controllability, reasoning model safety, monitorability, reasoning self-regulation