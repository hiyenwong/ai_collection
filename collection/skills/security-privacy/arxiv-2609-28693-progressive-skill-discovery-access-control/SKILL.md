---
name: arxiv-2609-28693-progressive-skill-discovery-access-control
description: 'Research paper: Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery.'
metadata:
  openclaw:
    emoji: "🔐"
    tags: ["research", "arxiv", "security-privacy", "access-control", "mcp", "governance", "llm-agent", "tool-use"]
---

# Progressive Skill Discovery as Access Control for Tool-Using LLM Agents

**arXiv ID:** 2609.28693
**Authors:** Michael Stettler, Benjamin Girardet, Jonas Canton, Nicolas Corod
**Categories:** cs.AI, cs.CR, cs.MA, eess.SY
**Utility Score:** 0.85

## Abstract

Large Language Model (LLM) agents struggle to scale safely when exposed to vast enterprise toolsets. Providing an agent with access to every internal tool leads to oversized context windows, degraded tool selection, and severe governance vulnerabilities—as system policies defined purely in prompts remain probabilistic advice rather than hard constraints. Existing mitigations, such as multi-agent domain delegation, decentralize audit logs and fail to guarantee policy compliance across sessions. We introduce skilder, a framework that packages capabilities into roles: bundles of skills, tools, and instructions, together with the limits that bound them. An agent begins with a minimal role catalog, learns the roles a task requires, and receives each role's skills, instructions, and tools through a single MCP server. Because tools reach the agent only inside learned skills, the same server enforces the scope of what was learned deterministically. We evaluate skilder against flat-context tool selection and multi-agent orchestration across 13 tasks using six models (10 runs each). Our results show that, when models completed discovery and issued a governed call, the skilder simulated authorization layer enforced governance boundaries: no unauthorized tool call or parameter violation (e.g., a spending-limit breach) executed. Aggregate task pass rates also reflect whether each model followed the discovery protocol and satisfied response-quality checks; those misses are not authorization failures. Furthermore, by allowing agents to dynamically acquire cross-role capabilities mid-task, skilder preserves problem-solving flexibility while providing hard system-level enforcement.

## Key Contributions

1. **Role-Based Capability Packaging**: Introduces skilder framework that packages capabilities into roles (skills + tools + instructions + limits)
2. **Progressive Discovery**: Agents start with minimal role catalog and progressively discover needed capabilities
3. **MCP-Based Enforcement**: Single MCP server delivers tools only inside learned skills, enforcing scope deterministically
4. **Zero Authorization Violations**: Across 13 tasks with 6 models (10 runs each), no unauthorized tool call or parameter violation executed
5. **Cross-Role Flexibility**: Agents can dynamically acquire cross-role capabilities mid-task while maintaining governance

## Relevance to AI Systems

- **Agent Security**: Addresses critical governance challenge of LLM agents with access to large toolsets
- **MCP Integration**: Demonstrates MCP server as both capability delivery and enforcement mechanism
- **Enterprise Applicability**: Directly applicable to enterprise deployments requiring strict access control
- **Structural Governance**: Moves beyond prompt-based policies to hard system-level enforcement
