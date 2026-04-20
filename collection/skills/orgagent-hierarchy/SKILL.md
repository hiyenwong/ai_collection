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

## Activation Keywords

- "orgagent-hierarchy"
- "orgagent hierarchy"
- "use orgagent hierarchy"
- "orgagent hierarchy help"
- "orgagent hierarchy tool"

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

### Basic Orgagent Hierarchy usage
```
User: "Help me with orgagent hierarchy"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed orgagent hierarchy assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
