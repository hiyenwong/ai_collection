---
name: agentic-configuration-management-acm
description: "ACM framework for governed agentic systems configuration."
metadata:
  arxiv_id: "2608.11166"
  authors: "Audrey Quessada-Vial"
  published: "2026-08-11"
  subjects: "Software Engineering (cs.SE)"
  title: "Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems"
license: Complete terms in LICENSE.txt
---

# Agentic Configuration Management (ACM)

## Overview

Agentic Configuration Management (ACM) is a framework-independent governance and configuration reference model for heterogeneous agentic systems. It addresses the challenge that existing LLMOps and AgentOps platforms support orchestration and observability but lack a common configuration-governance model for representing and governing these systems as coherent, versioned configurations.

## Core Components

### 1. Typed and Independently Versioned Agentic Configuration Items (ACIs)
- Each component (agents, prompts, tools, models, skills, composite subsystems, policies, workflows) is represented as a typed ACI
- ACIs are independently versioned to enable granular evolution tracking
- Types provide semantic meaning and validation constraints

### 2. Immutable Revisions and Baselines
- Configuration states are captured as immutable revisions
- Baselines group related revisions for coordinated deployment
- Enables reproducible system states and rollback capabilities

### 3. Explicit Configuration-Runtime Separation
- Clear boundary between configuration specification and runtime execution
- Prevents configuration drift and ensures auditability
- Runtime provenance captures actual execution against intended configuration

### 4. Lifecycle and Assurance Semantics
- Formal lifecycle states (proposed, validated, deployed, deprecated)
- Assurance levels tied to validation and testing requirements
- Governance gates control transitions between lifecycle states

### 5. Dependency-Aware Impact Propagation
- Dependencies between ACIs are explicitly modeled
- Changes propagate through dependency graph with monotone propagation over finite lattice
- Guarantees convergence, termination, and uniqueness of least fixed point above initial impact valuation

### 6. Canonical Configuration Graph
- Heterogeneous native configurations are normalized through semantic projection
- Common governance semantics operate on the canonical graph
- Enables interoperability across different execution frameworks

## Implementation Patterns

### Semantic Projection Adapters
- Create adapters for each target framework (LangGraph, CrewAI, OpenAI Agents SDK)
- Map framework-specific constructs to canonical ACI types
- Preserve semantic equivalence during projection

### Impact Propagation Algorithm
- Implement monotone propagation over finite lattice structure
- Start from initial impact valuation (changed ACIs)
- Iteratively propagate impacts until fixed point convergence
- Track affected components for change management

### Runtime Provenance Collection
- Instrument runtime to capture actual execution details
- Correlate runtime events with configuration specifications
- Enable traceability from runtime behavior back to configuration intent

## Usage Workflow

1. **Define ACI Types**: Identify and define types for all system components
2. **Create Initial Configuration**: Author ACIs and establish baseline
3. **Project to Target Framework**: Use semantic projection adapter for target runtime
4. **Deploy and Monitor**: Deploy projected configuration and collect provenance
5. **Manage Changes**: Apply changes to ACIs, propagate impacts, validate, and deploy new baseline

## Evaluation Results

The reference implementation demonstrates:
- Governance-equivalent ACM representations across LangGraph, CrewAI, and OpenAI Agents SDK
- Reproducible governance outcomes after projection
- Convergence, termination, and uniqueness properties for impact propagation
- Support for reproducibility, auditability, dependency analysis, and interoperability

## Activation Keywords
- agentic configuration management
- ACM framework
- governed agentic systems
- configuration governance
- heterogeneous agents
- semantic projection
- impact propagation
- configuration graph
- LLMOps governance
- AgentOps governance

## References
- Original paper: https://arxiv.org/abs/2608.11166
- Reference implementation: Available in Python with adapters for LangGraph, CrewAI, and OpenAI Agents SDK
- Formal appendices: Included in original paper (77 pages total)