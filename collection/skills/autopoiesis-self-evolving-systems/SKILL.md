---
name: autopoiesis-self-evolving-systems
description: "Self-evolving system design paradigm inspired by autopoiesis. Use when designing systems that need continuous online policy evolution, LLM-driven program synthesis, autonomous adaptation to runtime dynamics, or self-modifying code architectures. Keywords: autopoiesis, self-evolving, policy evolution, online synthesis, runtime adaptation, living code."
---

# Autopoiesis: Self-Evolving System Paradigm

Self-evolving systems that continuously rewrite their own policies during deployment, shifting from static human-engineered designs to LLM-driven online evolution.

## Core Concept

**Autopoiesis** (from biology: self-creation/maintenance) applied to computing systems. Policies become "living code" that evolves throughout deployment, not static artifacts designed before deployment.

## Key Components

### 1. LLM-Driven Program Synthesis Workflow

- Evolve serving policies with respect to real-time observed dynamics
- Policies reflect optimal decisions in navigating multi-dimensional trade-off spaces
- Use LLMs as policy synthesizers, not just policy executors

### 2. Continuous Online Evolution

- Observe real-world system behavior
- Rewrite policy code as runtime trade-offs shift
- Transform policy design from one-time offline to ongoing system component

### 3. Runtime Trade-off Navigation

Key trade-offs in dynamic environments:
- Scheduling overhead vs. execution efficiency
- Rescheduling frequency vs. reconfiguration overhead
- Workload fluctuations vs. elastic cluster autoscaling

Optimal balance is workload-specific and shifts continuously.

## Design Pattern

```
Traditional: [Human Design] → [Static Policy] → [Deployment] → [Fixed Execution]
Autopoiesis: [Initial Policy] → [Deployment] → [Observation] → [LLM Synthesis] → [Policy Rewrite] → [Loop]
```

## Implementation Principles

1. **Policy as Code Artifact**: Policies are executable programs, not configuration files
2. **Observation-Driven Evolution**: Evolution triggered by runtime metrics, not manual intervention
3. **Synthesis vs. Learning**: LLM generates new code, not just adjusts parameters
4. **Safe Evolution**: Policies must maintain correctness constraints during evolution

## Application Domains

- LLM serving systems (workload fluctuation handling)
- Distributed system scheduling
- Cloud resource management
- Adaptive control systems
- Any system with volatile runtime dynamics

## Key Results

- Up to 53% improvement over static policies
- Average 34% improvement over state-of-the-art
- Handles severe runtime dynamics autonomously

## Design Questions

When designing self-evolving systems:

1. What policies need to evolve? (scheduling, routing, allocation)
2. What runtime metrics drive evolution? (latency, throughput, utilization)
3. What constraints must evolution respect? (safety, correctness, fairness)
4. How fast should evolution occur? (real-time, periodic, triggered)

## Related Concepts

- **Autopoiesis in Biology**: Systems that produce and maintain themselves
- **Meta-programming**: Programs that modify programs
- **Adaptive control**: Systems that adjust parameters online
- **Evolutionary algorithms**: Population-based optimization

## References

- arXiv:2604.07144v1 - "Autopoiesis: A Self-Evolving System Paradigm for LLM Serving Under Runtime Dynamics"
- Original biological concept: Maturana & Varela (1973)

## Activation Keywords

- autopoiesis
- self-evolving
- policy evolution
- online synthesis
- runtime adaptation
- living code

## Tools Used

- read
- write

## Instructions for Agents

Use this skill to design self-evolving systems that continuously rewrite their own policies. Follow the autopoiesis paradigm: observe runtime dynamics → synthesize updated policy with LLM → deploy new policy → repeat.

## Examples

User: Help me with Autopoiesis Self Evolving Systems
Agent: [Activates autopoiesis-self-evolving-systems skill and follows the instructions above]
