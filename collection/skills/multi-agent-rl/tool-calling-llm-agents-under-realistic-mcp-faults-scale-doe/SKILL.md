---
name: tool-calling-llm-agents-under-realistic-mcp-faults-scale-doe
description: "Tool-Calling LLM Agents Under Realistic MCP Faults: Scale ..."
category: multi-agent-rl
tags: [cs.SE, cs.AI]
source: arxiv
paper_id: 2610.32555v1
utility: 0.85
---

# Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance

**arXiv ID:** 2610.32555v1
**URL:** http://arxiv.org/abs/2610.32555v1
**Published:** 2026-10-23T12:35:51Z
**Categories:** cs.SE, cs.AI
**Utility Score:** 0.85

## Abstract

LLM agents increasingly rely on external tools exposed via the Model Context Protocol (MCP), yet current benchmarks assume tools respond correctly and on time, leaving agent resilience to realistic tool failures untested. We introduce MCP-Injector, a drop-in, protocol-aware fault-injection middleware that interposes on the MCP tool-call path with controlled persistence (permanent, transient, intermittent) and seedable schedules. Its fault model is calibrated to the observed incident distribution (failure mode x persistence) of the public MCP ecosystem, mined from 57,240 issue and pull-request threads across 1,774 open-source MCP repositories. In a 1,350-cell experiment crossing two backbone sizes (20B, 120B), three agent stacks (custom multi-round plan-and-execute, OpenAI Agents SDK, LangChain), and three fault injection conditions, we find that faults drawn from this permanent-heavy stress profile cause severe quality degradation (task-completion score falls by 60%, from 8.08 to 3.23 

## Key Contributions

- Paper from arXiv in categories: cs.SE, cs.AI
- High utility score (0.85) indicates relevance to AI/ML research
- Published: 2026-10-23T12:35:51Z

## Related Skills

This paper relates to the `multi-agent-rl` category based on keyword analysis.
