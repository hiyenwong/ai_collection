---
name: agent-safety-layer
description: Runtime safety and observability layer for local AI agents. Intercepts every proposed agent action before execution, evaluates against declarative policy, requires human approval for sensitive operations, and records complete audit trails. Use when building safe local AI agents, implementing action interception, designing agent guardrails, or creating policy enforcement for autonomous systems. Covers AgentWall methodology (arXiv: 2605.16265).
---

# Agent Safety Layer

Runtime safety pattern for local AI agents based on the AgentWall architecture (arXiv: 2605.16265).

## Core Concept

Intercept every proposed agent action **before** it reaches the host environment. Evaluate against a declarative policy. Require human approval for sensitive operations. Record complete execution trail.

## Architecture

```
Agent → Action Proposal → Policy Interceptor → [ALLOW / BLOCK / ASK] → Host Environment
                                                      ↓
                                                Audit Trail (replay)
```

### Policy Model

Define explicit rules for action categories:

```yaml
policies:
  filesystem:
    read: allow                    # Read-only: always allow
    write: ask                     # Modifications: require approval
    delete: block                  # Destructive: always block
  shell:
    read: allow                    # ls, cat, grep: allow
    install: ask                   # pip install, brew: ask
    sudo: block                    # Privileged: block
    network: ask                   # curl, wget: ask
  api:
    read: allow                    # GET requests: allow
    write: ask                     # POST/PUT: require approval
    admin: block                   # Destructive API calls: block
```

### Interception Points

1. **Before execution**: Intercept at the tool-call boundary
2. **Policy evaluation**: Match action against declarative rules
3. **Decision**: ALLOW (pass through), BLOCK (deny + explain), ASK (pause for approval)
4. **Audit**: Log action, decision, and outcome for replay

### Key Design Principles

- **Explicit over implicit**: Every action must have a defined policy rule
- **Least privilege**: Default to ASK or BLOCK; explicitly ALLOW known-safe operations
- **Full provenance**: Every decision is logged with timestamp, agent ID, action details, and policy match
- **Sub-millisecond overhead**: Policy matching should not bottleneck agent throughput
- **Cross-platform**: Works with MCP proxy pattern, supporting Claude Desktop, Cursor, Claude Code, etc.

### Threat Model

Protect against:
- Agent executing unintended destructive commands
- Adversarial prompt injection leading to unsafe actions
- Credential leakage through agent tool calls
- Unintended filesystem or API modifications

### Implementation Patterns

#### Pattern 1: MCP Proxy
Wrap the Model Context Protocol server. Intercept all tool calls:
```
Client → Agent → [Proxy] → MCP Server
                 ↑
           Policy check + audit
```

#### Pattern 2: Native Plugin
Implement as a plugin in the agent framework:
- Register hook before each tool execution
- Run policy check in hook
- Return early if blocked

### Evaluation

92.9% policy enforcement accuracy with sub-millisecond overhead across 14 benchmark tests. Key metrics:
- Enforcement accuracy (blocked/allowed correctly)
- False positive rate (legitimate actions incorrectly blocked)
- Latency overhead per action
- Audit trail completeness
