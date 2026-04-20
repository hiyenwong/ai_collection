---
name: autonomous-evolution-of-eda-tools-multi-agent-self
description: 'Research paper: Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC'
metadata:
  source: arXiv
  arxiv_id: 2604.15082
  published: 2026-04-16
  utility_score: 1.0
  keywords: multi-agent, self-evolving, tool, tools, benchmark, evaluation, autonomous
---

# Autonomous Evolution of EDA Tools: Multi-Agent Self-Evolved ABC

**arXiv ID:** 2604.15082  
**Published:** 2026-04-16  
**Utility Score:** 1.0  
**URL:** http://arxiv.org/abs/2604.15082

## Authors
Cunxi Yu, Haoxing Ren

## Categories
cs.AR, cs.AI

## Abstract
This paper introduces the first \emph{self-evolving} logic synthesis framework, which leverages Large Language Model (LLM) agents to autonomously improve the source code of \textsc{ABC}, the widely adopted logic synthesis system. Our framework operates on the \emph{entire integrated ABC codebase}, and the output repository preserves its single-binary execution model and command interface. In the initial evolution cycle, we bootstrap the system using existing prior open-source synthesis components, covering flow tuning, logic minimization, and technology mapping, but without manually injecting new heuristics. On top of this foundation, a team of LLM-based agents iteratively rewrites and evolves specific sub-components of ABC following our ``programming guidance`` prompts under a unified correctness and QoR-driven evaluation loop. Each evolution cycle proposes code modifications, compiles the integrated binary, validates correctness, and evaluates quality-of-results (QoR) on \emph{multi-suite benchmarks including ISCAS~85/89/99, VTR, EPFL, and IWLS~2005}. Through continuous feedback, the system discovers optimizations beyond human-designed heuristics, effectively \emph{learning new synthesis strategies} that enhance QoR. We detail the architecture of this self-improving system, its integration with \textsc{ABC}, and results demonstrating that the framework can autonomously and progressively improve EDA tool at full million-line scale.

## Matched Keywords
multi-agent, self-evolving, tool, tools, benchmark, evaluation, autonomous

## Relevance to AI Agents
This paper is highly relevant to AI agent systems research with focus on:
- multi-agent, self-evolving, tool, tools, benchmark

## Quick Reference
```bash
# View paper
open http://arxiv.org/abs/2604.15082

# Download PDF
open http://arxiv.org/pdf/2604.15082.pdf
```

---
*Auto-generated from arXiv on 2026-04-17*

## Activation Keywords

- "autonomous-evolution-of-eda-tools-multi-agent-self"
- "autonomous evolution of eda tools multi agent self"
- "use autonomous evolution of eda tools multi agent self"
- "autonomous evolution of eda tools multi agent self help"
- "autonomous evolution of eda tools multi agent self tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Autonomous Evolution Of Eda Tools Multi Agent Self usage
```
User: "Help me with autonomous evolution of eda tools multi agent self"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed autonomous evolution of eda tools multi agent self assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
