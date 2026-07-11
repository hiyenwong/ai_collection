---
name: trustworthy-agents-framework
description: Five-principle framework for building and governing trustworthy AI agents. Covers human control, value alignment, secure interactions, transparency, and privacy in agent architecture design.
---

## Overview
Comprehensive framework for designing, deploying, and governing trustworthy AI agents. Establishes five core principles that must be satisfied for AI agents to be considered trustworthy: human control, value alignment, secure interactions, transparency, and privacy. Addresses prompt injection risks, tool-use security, and multi-agent coordination safety.

## Architecture
1. **Agent Model**: Core LLM with safety guardrails and constitutional constraints
2. **Agent Harness**: Execution environment managing tool access, state, and action logging
3. **Tools**: External APIs and functions with permission-based access control
4. **Environment**: Sandboxed execution context preventing unauthorized data access
5. **Agent Behavior Layers**:
   - Self-directed loop: plans, acts, observes, adjusts, repeats
   - Behavior depends on model + harness + tools + environment working together
6. **Five Core Principles**:
   - **Human Control**: Humans retain ultimate decision authority
     - Permission tiers: always allow, needs approval, block
     - Plan Mode: shows intended plan for review before execution
   - **Value Alignment**: Agent behavior consistent with human values
     - Training on ambiguous situations reinforces pausing over assuming
     - Constitution reinforces "raising concerns, seeking clarification, or declining to proceed"
   - **Secure Interactions**: Protection against prompt injection, tool misuse, data exfiltration
     - Multi-layer defenses: training, monitoring, red-teaming
   - **Transparency**: Agent actions and reasoning are auditable and explainable
   - **Privacy**: Agent respects data boundaries and minimizes information exposure

## Key Findings
- Prompt injection remains the highest-risk attack vector for agent deployment
- Agent behavior depends on all four layers (model, harness, tools, environment) working together
- Claude's rate of checking in roughly doubles on complex tasks vs simple tasks
- Tool-use security requires explicit permission models, not implicit trust
- Multi-agent systems introduce emergent risks not present in single-agent designs
- Open standards like MCP (Model Context Protocol, donated to Linux Foundation) improve interoperability but expand attack surface
- Auditability must be built into agent architecture, not bolted on after deployment

## Ecosystem Recommendations
1. **Benchmarks**: Rigorous, standardized ways to compare agent systems on prompt injection resistance and uncertainty surfacing
2. **Evidence Sharing**: Publishing how agents are used and where they struggle
3. **Open Standards**: Protocols like MCP (Model Context Protocol, donated to Linux Foundation) improve interoperability but expand attack surface

## Runtime Risk Management (Pre-Action Safety Layer)
See the **actuarial-runtime-ai-agents** skill for a mathematical framework that operationalizes the "Secure Interactions" principle at the action level:
- **Pre-action risk tolls**: Every side-effect-bearing action carries a counterfactual risk toll computed against a safe default, replacing post-hoc liability with pre-transaction underwriting
- **Budget gating theorem**: Translates risk tolerance into executed-action budget guarantees with high-probability bounds
- **No-splitting property**: Prevents agents from gaming the system by decomposing large actions into smaller sub-actions
- **Underwriting boundary design**: Determines the gaming-resistance of the entire system
This connects governance-level principles (human control, value alignment) to mathematical runtime guarantees on individual agent actions.

## Methodology Steps
1. **Threat Modeling**: Identify attack vectors specific to agent deployment context
2. **Principle Mapping**: Map each of the five trustworthiness principles to concrete implementation requirements
3. **Architecture Design**: Design agent model, harness, tools, and environment with security boundaries
4. **Access Control**: Implement least-privilege tool access with explicit permission grants
5. **Audit Logging**: Build comprehensive action and reasoning logging into agent harness
6. **Red Team Testing**: Systematically test for prompt injection, tool misuse, and data leakage
7. **Deployment Monitoring**: Continuously monitor agent behavior for drift from trustworthiness principles
8. **Incident Response**: Establish procedures for agent behavior rollback and human takeover

## Applications
- Enterprise AI agent deployment
- Multi-agent system governance
- Agent security assessment
- Tool-use safety design
- AI agent compliance and auditing
- Prompt injection defense

## Code Availability
Framework based on Anthropic research. MCP standard is open source.

## Activation Keywords
trustworthy agents, AI governance, prompt injection, human control, value alignment, secure interactions, agent transparency, agent privacy, MCP, agent security, multi-agent safety
