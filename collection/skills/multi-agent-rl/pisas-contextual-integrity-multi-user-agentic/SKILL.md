---
name: pisas-contextual-integrity-multi-user-agentic
description: "Benchmarking contextual integrity in multi-user agentic systems. As LLM agents evolve into shared organizational infrastructure, new privacy risks emerge from inter-agent messages, shared memory, and cross-user information exposure. Activation: contextual integrity, multi-user agents, privacy benchmark, agentic privacy, inter-agent communication, shared memory privacy."
metadata:
  arxiv_id: "2607.05318"
  published: "2026-07-06"
  authors: "Shubham Gupta, Nazanin Mohammadi Sepahvand, Abhinav Kumar, Cem Subakan, Spandana Gella, Pierre-André Noël, Perouz Taslakian, Eugene Bagdasarian, Valentina Zantedeschi"
  tags: [contextual-integrity, multi-user-agents, privacy, benchmark, inter-agent-communication, shared-memory]
---

# PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems

## Overview

As LLM agents evolve from single-user assistants into shared organizational infrastructure, new privacy risks emerge: inappropriate information may not only be exposed through outputs for external recipients, but also internally across users through inter-agent messages, shared memory and agents. This paper introduces PiSAs, a benchmark for evaluating contextual integrity in multi-user agentic systems.

## Key Problem

### Multi-User Privacy Risks in Agentic Systems
- **Inter-agent message leakage**: Agents sharing information with other agents serving different users
- **Shared memory exposure**: Common memory stores accessible across user contexts
- **Contextual integrity violations**: Information appropriate in one context may be inappropriate in another
- **Internal vs external risks**: Privacy violations can occur internally (across users) not just externally

### Contextual Integrity Framework
- Based on contextual integrity theory: information flow norms depend on context, sender, recipient, and information type
- Agents must respect contextual boundaries when processing and sharing information
- Multi-user settings introduce complex information flow constraints

## Benchmark Design

1. **Multi-User Scenarios**: Agents serving different users with overlapping but distinct information access
2. **Privacy Violation Detection**: Measures for detecting contextual integrity violations
3. **Inter-Agent Communication**: Tests for information leakage through agent-to-agent messages
4. **Shared Memory Access**: Evaluates privacy preservation in shared memory architectures

## Implications

- New privacy paradigm needed for multi-user agentic AI systems
- Contextual integrity as a framework for designing privacy-preserving agent architectures
- Benchmark enables systematic evaluation of privacy risks in deployed multi-user agents
- Organizational deployments of LLM agents need context-aware information flow controls

## Pitfalls

- Contextual integrity norms are domain-specific and may not generalize
- Benchmark scenarios may not capture all real-world privacy failure modes
- Trade-off between privacy and agent utility/efficiency
- Dynamic context boundaries are hard to define in practice

## Activation Keywords

contextual integrity, multi-user agents, privacy benchmark, agentic privacy, inter-agent communication, shared memory privacy, organizational agents, information flow norms, PiSAs

## Paper Reference

arXiv:2607.05318 - "PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems" (Jul 2026)
