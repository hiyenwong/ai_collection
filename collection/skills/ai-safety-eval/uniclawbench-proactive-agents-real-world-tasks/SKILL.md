---
name: uniclawbench-proactive-agents-real-world-tasks
description: "Capability-driven benchmark for evaluating proactive agents in dynamic real-world settings. UniClawBench evaluates five foundational capabilities (Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, Cross-Platform Coordination) across 400 bilingual tasks in live Docker containers with closed-loop evaluation. Activation: proactive agents, real-world benchmark, agent evaluation, capability-driven, multimodal agents, closed-loop evaluation."
metadata:
  arxiv_id: "2607.08768"
  published: "2026-07-09"
  authors: "Zhekai Chen, Chengqi Duan, Kaiyue Sun, Bohao Li, Yuqing Wang"
  tags: [proactive-agents, real-world-benchmark, agent-evaluation, capability-driven, multimodal-agents]
---

# UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

## Overview

The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. UniClawBench is the first capability-driven benchmark designed to evaluate proactive agents in dynamic, real-world settings, addressing limitations of existing benchmarks that rely on sandboxed environments and single-turn evaluation paradigms.

## Key Innovations

### Capability-Driven Task Taxonomy
- Five foundational model capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, and Cross-Platform Coordination
- Disentangles model capabilities from framework-level design choices
- Enables identification of root causes of agent failures

### Live Docker Container Evaluation
- Tasks executed in live Docker containers rather than static pre-recorded answers
- Fine-grained, step-by-step completion checkpoints
- Realistic multi-turn human feedback simulation

### Closed-Loop Evaluation Strategy
- Executor agent performs tasks
- Hidden supervisor agent evaluates
- User agent simulates human feedback
- Prevents grading criteria leakage

## Methodology

1. **Capability Taxonomy**: Design 400 bilingual tasks across five capability dimensions
2. **Live Environment**: Deploy tasks in Docker containers with real system state
3. **Closed-Loop**: Multi-agent evaluation simulating real user interaction
4. **Framework Comparison**: Evaluate state-of-the-art models under multiple agent frameworks

## Implications

- Framework design and base model capabilities jointly shape real-world performance
- Capability-driven benchmarks enable targeted improvement of agent systems
- Live evaluation reveals failure modes invisible to static benchmarks
- Supports the growing field of proactive agent deployment

## Pitfalls

- Docker container setup may limit scalability for very large evaluations
- Bilingual tasks may introduce language-specific biases
- Framework comparison depends on framework maturity and optimization
- Closed-loop evaluation complexity may increase evaluation cost

## Activation Keywords

proactive agents, real-world benchmark, agent evaluation, capability-driven, multimodal agents, closed-loop evaluation, Docker benchmark, agent frameworks, UniClawBench

## Paper Reference

arXiv:2607.08768 - "UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks" (Jul 2026)
