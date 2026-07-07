---
name: llm-autonomous-physics-discovery
description: "Autonomous LLM agent methodology for computational physics discovery using progressive local search, knowledge accumulation from successful/failed attempts, and interpretable exploration trajectories. Covers PhyNex framework for scorable scientific tasks with domain-specific tools enforcing physical consistency. Activation: LLM autonomous discovery, physics agent, progressive local search, computational physics agent, PhyNex, automated physics optimization, 大语言模型物理发现, 自主科学发现代理"
metadata:
  arxiv_id: "2606.14266"
  published: "2026-06-12"
  authors: "Hang Lin, Chongwen Liu, Gang Yan"
  tags: [LLM, autonomous-discovery, computational-physics, agent, optimization]
---

# LLM Autonomous Physics Discovery

## Description

PhyNex: autonomous LLM agent framework for computational physics discovery. Combines LLM-guided progressive local search with domain-specific tools enforcing physical consistency, accumulating knowledge from both successful and failed attempts.

## Activation Keywords
- LLM autonomous discovery
- physics agent
- progressive local search
- computational physics agent
- PhyNex
- automated physics optimization
- 大语言模型物理发现
- 自主科学发现代理
- scientific discovery agent
- LLM-guided exploration

## Core Methodology

### Problem
Scientific discovery in computational physics involves optimizing quantitatively evaluable objectives subject to physical constraints, but researchers spend substantial effort on iterative refinement of methods.

### PhyNex Framework

1. **Exploration**: Systematically explore solution space of scorable scientific tasks
2. **LLM-guided search**: Use LLMs to propose method modifications and parameter adjustments
3. **Domain tools**: Enforce physical consistency through computational tools
4. **Knowledge accumulation**: Learn from both successful and failed attempts
5. **Interpretable trajectories**: Reveal which algorithmic components drive improvements

### Validated Applications
| Task | Improvement | Metric |
|------|------------|--------|
| Dielectric spectra prediction | +3.8% | Spectral similarity |
| Max-Cut heuristics | +15.0% | Normalized mean cut |
| Quantum battery charging | +5.9% | Ergotropy at 80k checkpoint |

## Usage Patterns

### Pattern 1: Automated Algorithm Design
When optimizing computational physics algorithms:
1. Define scorable objective function with physical constraints
2. Set up LLM agent with domain-specific tool access
3. Run progressive local search with knowledge accumulation
4. Analyze exploration trajectories for interpretable insights

### Pattern 2: Method Discovery
When discovering new approaches for scientific problems:
1. Frame problem as optimization with quantitative metrics
2. Provide LLM with prior knowledge and constraints
3. Allow agent to explore methodological search space
4. Extract reusable knowledge from successful attempts

## Instructions for Agents

### Step 1: Define Scientific Task
- Quantifiable objective function (e.g., spectral similarity, ergotropy)
- Physical constraints (e.g., conservation laws, boundary conditions)
- Evaluation protocol with reproducible metrics

### Step 2: Set Up Agent Framework
- LLM with domain knowledge context
- Domain-specific computational tools
- Progressive local search mechanism
- Knowledge storage for attempt history

### Step 3: Run Exploration
- Agent proposes method modifications
- Execute with physical consistency checks
- Score and record results
- Accumulate knowledge from successes and failures

### Step 4: Analyze Results
- Extract interpretable exploration trajectories
- Identify which components drove improvements
- Document reusable knowledge for future tasks

## Error Handling
### Physical Constraint Violation
If agent proposes physically invalid solutions:
- Enforce constraints via domain tools
- Reject and record failed attempts as knowledge
- Guide agent toward valid search regions

### Convergence Failure
If agent cannot improve beyond baseline:
- Expand search space exploration
- Provide additional domain priors
- Reset with different initial configurations

## References
- arXiv: 2606.14266v1
- Validated on: dielectric spectra, Max-Cut heuristics, quantum batteries
