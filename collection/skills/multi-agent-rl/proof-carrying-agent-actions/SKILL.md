---
name: proof-carrying-agent-actions
version: v1.0.0
last_updated: 2026-06-12
description: "Runtime governance framework for heterogeneous agent systems using action certificates. Model-agnostic governance centered on action proofs rather than vendor-native session records. From Anthropic research (arXiv:2606.04104)."
---

# Proof-Carrying Agent Actions

Framework for runtime-neutral governance of heterogeneous agent systems through action certificates.

## Purpose

Agent systems execute through runtimes with different control points (local coding tools, SDKs, managed platforms, API gateways). This makes it difficult to answer governance questions consistently: what action was authorized, under whose authority, and with what evidence after execution? PCAA solves this by centering on an action certificate rather than vendor-native session records.

## Core Framework

### Action Certificate Structure

Each agent action carries a proof that includes:

| Field | Description |
|-------|-------------|
| **Action Identity** | What action was performed (canonical representation) |
| **Authority Chain** | Who authorized it (user, system policy, delegation) |
| **Approval Semantics** | Under what conditions (explicit, implicit, scoped) |
| **Execution Evidence** | Proof that the action matched authorization |
| **Runtime Context** | Where it was executed (agnostic of specific platform) |

### Governance Model

1. **Authorization Layer**: Define what actions are permitted under which conditions
2. **Proof Generation**: Each action produces a certificate at execution time
3. **Proof Verification**: Independent verification that execution matched authorization
4. **Audit Trail**: Certificates form an immutable governance log

### Cross-Runtime Compatibility

The key insight is that a "publish data externally" action looks different in every runtime:
- **Local coding tool**: shell command
- **Framework SDK**: tool call
- **Managed platform**: hosted session transition
- **API gateway**: HTTP request

PCAA provides a canonical representation that works across all runtimes.

## Implementation Patterns

### Pattern 1: Action Canonicalization
```
1. Parse runtime-specific action representation
2. Map to canonical action type (read, write, execute, network)
3. Extract parameters and targets
4. Generate action fingerprint
```

### Pattern 2: Certificate Generation
```
1. Capture authorization context at decision time
2. Record action identity with parameters
3. Attach authority chain (who approved)
4. Compute execution evidence hash
5. Sign certificate with runtime key
```

### Pattern 3: Certificate Verification
```
1. Verify signature integrity
2. Check authorization chain validity
3. Compare execution evidence against authorization
4. Flag any deviations for review
5. Log verification result
```

## Activation Keywords
- proof-carrying agent actions
- agent governance framework
- runtime governance
- agent action certificate
- heterogeneous agent systems
- agent authorization proof
- 智能体治理
- 运行时治理
- agent audit trail

## Resources
- Paper: https://arxiv.org/abs/2606.04104
- Related: security-guardrails, spec-driven-agent-architecture, agent-integration-testing

## Notes
- Model-agnostic: works with any LLM or agent framework
- Designed for multi-runtime environments
- Certificates should be independently verifiable
- Authority chains support delegation and scoped permissions
