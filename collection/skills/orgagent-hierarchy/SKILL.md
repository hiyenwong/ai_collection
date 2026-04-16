---
name: orgagent-hierarchy
description: Company-style hierarchical multi-agent organization framework. Use when building multi-agent systems, designing agent coordination architectures, optimizing agent token consumption, or discussing multi-agent organizational structures. Triggers on "multi-agent organization", "agent hierarchy", "OrgAgent", "company-style agents", or "agent coordination".
---

# OrgAgent: Hierarchical Multi-Agent Organization

Key findings from "OrgAgent: Organize Your Multi-Agent System like a Company" (arXiv:2604.01020) by Wang et al.

## Framework Architecture

Three-layer company-style hierarchy:

### Governance Layer
- Planning and resource allocation
- Strategic decision-making

### Execution Layer  
- Task solving and review
- Actual work execution

### Compliance Layer
- Final answer control
- Quality verification

## Key Results

Performance improvements on GPT-OSS-120B:
- **+102.73%** performance over flat multi-agent on SQuAD 2.0
- **-74.52%** token consumption reduction

Benefits most when tasks require:
- Stable skill assignment
- Controlled information flow
- Layered verification

## When to Use Hierarchy

Hierarchy outperforms flat structures when:
- Complex reasoning tasks
- Tasks benefit from skill specialization
- Need controlled information propagation
- Verification is critical

## Implementation Guidance

1. Define clear layer boundaries
2. Assign agents to appropriate layers based on capabilities
3. Establish communication protocols between layers
4. Monitor token consumption vs performance trade-offs

## Reference

arXiv:2604.01020 - "OrgAgent: Organize Your Multi-Agent System like a Company" by Yiru Wang et al.
Submitted: April 1, 2026