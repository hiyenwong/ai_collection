---
name: autogenesis-a-self-evolving-agent-protocol
description: 'Research paper: Autogenesis: A Self-Evolving Agent Protocol'
metadata:
  source: arXiv
  arxiv_id: 2604.15034
  published: 2026-04-16
  utility_score: 1.0
  keywords: multi-agent, self-evolving, memory, long horizon, tool, tools, planning, benchmark
---

# Autogenesis: A Self-Evolving Agent Protocol

**arXiv ID:** 2604.15034  
**Published:** 2026-04-16  
**Utility Score:** 1.0  
**URL:** http://arxiv.org/abs/2604.15034

## Authors
Wentao Zhang

## Categories
cs.AI

## Abstract
Recent advances in LLM based agent systems have shown promise in tackling complex, long horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under specify cross entity lifecycle and context management, version tracking, and evolution safe update interfaces, which encourages monolithic compositions and brittle glue code. We introduce \textbf{\textsc{Autogenesis Protocol (AGP)}}, a self evolution protocol that decouples what evolves from how evolution occurs. Its Resource Substrate Protocol Layer (RSPL) models prompts, agents, tools, environments, and memory as protocol registered resources\footnote{Unless otherwise specified, resources refer to instances of the five RSPL entity types: \emph{prompt}, \emph{agent}, \emph{tool}, \emph{environment}, \emph{memory} with agent \emph{outputs}.} with explicit state, lifecycle, and versioned interfaces. Its Self Evolution Protocol Layer (SEPL) specifies a closed loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback. Building on \textbf{\textsc{AGP}}, we present \textbf{\textsc{Autogenesis System (AGS)}}, a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. We evaluate \textbf{\textsc{AGS}} on multiple challenging benchmarks that require long horizon planning and tool use across heterogeneous resources. The results demonstrate consistent improvements over strong baselines, supporting the effectiveness of agent resource management and closed loop self evolution.

## Matched Keywords
multi-agent, self-evolving, memory, long horizon, tool, tools, planning, benchmark

## Relevance to AI Agents
This paper is highly relevant to AI agent systems research with focus on:
- multi-agent, self-evolving, memory, long horizon, tool

## Quick Reference
```bash
# View paper
open http://arxiv.org/abs/2604.15034

# Download PDF
open http://arxiv.org/pdf/2604.15034.pdf
```

---
*Auto-generated from arXiv on 2026-04-17*
