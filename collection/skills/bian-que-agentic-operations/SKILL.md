---
name: bian-que-agentic-operations
description: "Agentic framework for online system operations with Flexible Skill Arrangement. Use when designing LLM-based agents for system O&M, IT operations, DevOps automation, alert management, root cause analysis, or self-evolving agent systems. Activation triggers: system operations, O&M automation, agentic operations, skill arrangement, alert root cause analysis, self-evolving agents, release interception, proactive inspection, KuaiShou operations."
---

# Bian Que: Agentic Framework for Online System Operations

> An agentic framework with three contributions for operating large-scale online systems: unified operational paradigm, Flexible Skill Arrangement, and unified self-evolving mechanism. Deployed at KuaiShou with 75% alert reduction, 80% RCA accuracy, 50%+ MTTR reduction.

## Metadata
- **Source**: arXiv:2604.26805
- **Authors**: Bochao Liu, Zhipeng Qian, Yang Zhao, et al.
- **Published**: 2026-04-29
- **Code**: Available at GitHub

## Core Methodology

### Key Innovation 1: Unified Operational Paradigm

Abstract day-to-day O&M into three canonical patterns:

1. **Release Interception** - Monitor deployments, detect anomalies, gate releases before they reach production
2. **Proactive Inspection** - Systematically check system health, predict issues before they manifest
3. **Alert Root Cause Analysis** - Diagnose alert triggers, trace to root cause, recommend remediation

**Why this works**: Instead of treating each O&M task as unique, this taxonomy covers 90%+ of operational events with reusable patterns.

### Key Innovation 2: Flexible Skill Arrangement

Each **Skill** specifies:
- **Which data to retrieve**: metrics, logs, change events, traces
- **Which knowledge to apply**: handbook rules, practitioner experience, historical patterns
- **Context binding**: skills are scoped to specific business-module contexts

**Skill lifecycle**:
1. Skills can be **auto-generated** by LLMs from operational requirements
2. Skills can be **updated** via natural-language instructions from on-call engineers
3. Skills **compose** - multiple skills can be arranged for complex operational scenarios

**Critical insight**: The deployment bottleneck for LLM-based O&M agents is **not reasoning capability but orchestration** - selecting relevant data/knowledge for each event. Feeding all signals causes dilution and hallucination; manual curation is intractable.

### Key Innovation 3: Unified Self-Evolving Mechanism

One correction signal drives two parallel pathways:

1. **Case-Memory-to-Knowledge Distillation**: Historical incident cases are distilled into structured operational knowledge
2. **Targeted Skill Refinement**: Specific skills are refined based on correction signals

**Architecture**:
```
Operational Event → Skill Selection → Data/Knowledge Retrieval → LLM Reasoning → Action
                                                         ↓
                                                Correction Signal
                                                         ↓
                        ┌───────────────────────────────┴───────────────────────────────┐
                        ↓                                                               ↓
              Case-Memory-to-Knowledge                                    Targeted Skill Refinement
              Distillation Pipeline                                       (update skill definition)
```

## Implementation Guide

### Prerequisites
- LLM with tool-use capabilities
- Access to system metrics, logs, change events
- Knowledge base of operational procedures

### Step-by-Step

1. **Define Operational Taxonomy**
   - Catalog all O&M events into the three canonical patterns
   - For each pattern, identify common sub-scenarios

2. **Design Skills**
   - For each sub-scenario, create a skill specifying:
     - Required data sources (metrics, logs, traces, change events)
     - Required knowledge sources (runbooks, historical cases, expert rules)
     - Output format (diagnosis, remediation plan, escalation decision)

3. **Implement Skill Registry**
   - Skills stored as structured objects (JSON/YAML)
   - Skills indexed by business-module context and event type
   - Support for skill versioning and A/B testing

4. **Build Self-Evolution Loop**
   - Capture correction signals (human feedback, automated validation)
   - Store incident cases with resolution outcomes
   - Periodically distill cases into knowledge updates
   - Refine skills based on performance metrics

### Pitfalls
- **Signal dilution**: Feeding all operational data to the LLM causes hallucination. Skills must precisely scope data retrieval.
- **Cold start**: Initial skill generation may require human-in-the-loop. Start with high-value scenarios first.
- **Knowledge staleness**: Skills must be regularly validated against current system state.
- **Over-generalization**: Skills scoped too broadly lose precision; too narrow become unmaintainable.

## Applications
- IT operations automation (AIOps)
- Cloud infrastructure management
- E-commerce platform operations
- Microservice incident management
- DevOps workflow automation

## Related Skills
- agentic-behavioral-modeling
- agentic-fast-slow-planning
- logact-agentic-reliability
- emergent-systems-design
