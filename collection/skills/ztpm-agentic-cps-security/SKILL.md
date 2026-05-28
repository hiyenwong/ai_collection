---
name: ztpm-agentic-cps-security
description: Zero Trust Policy Model (ZTPM) for Agentic Cyber-Physical Systems security enforcement at physical actuation boundary
version: 1.0.0
author: Tharindu Ranathunga, Kavishka Fernando, Susan Rea
arxiv_id: 2605.25653
date_created: 2026-05-28
activation_keywords:
  - agentic CPS
  - zero trust policy
  - robot security
  - multi-agent systems
  - physical actuation boundary
  - LFM security
  - industrial robot control
tags:
  - cyber-physical systems
  - security
  - multi-agent systems
  - zero trust
  - robotics
  - distributed systems
  - control systems
---

# ZTPM: Zero Trust Policy Model for Agentic Cyber-Physical Systems

## Overview

ZTPM (Zero Trust Policy Model) is a security framework designed for agentic cyber-physical systems where multi-agent systems powered by Large Foundation Models (LFMs) control industrial robots through natural language commands.

## Problem Statement

- Multi-agent systems using LFMs increasingly control industrial robots via natural language
- Security failures in these systems produce **physical consequences**
- Five attack classes specific to agentic CPS identified:
  1. **Command injection attacks** - malicious natural language commands
  2. **Agent hijacking** - unauthorized control of agent behavior
  3. **Physical parameter manipulation** - altering actuation parameters
  4. **Model dependency exploitation** - exploiting LFM vulnerabilities
  5. **Cross-agent interference** - disrupting agent coordination

## Core Methodology: ZTPM Framework

### 1. Policy Primitives (25 Typed Primitives)

ZTPM comprises **25 typed policy primitives** across **five enforcement domains**:

#### Enforcement Domains:
1. **Command Validation Domain**
   - Primitive types: command-origin, command-syntax, command-semantic, command-intent
   - Enforces natural language command verification

2. **Agent Behavior Domain**
   - Primitive types: agent-state, agent-permission, agent-capability, agent-delegation
   - Controls agent autonomy and delegation chains

3. **Physical Actuation Domain**
   - Primitive types: actuation-limit, actuation-speed, actuation-force, actuation-range, actuation-zone
   - Enforces physical safety boundaries

4. **Model Interface Domain**
   - Primitive types: model-query-limit, model-response-validation, model-fallback, model-version
   - Governs LFM interaction policies

5. **Cross-Agent Coordination Domain**
   - Primitive types: coordination-protocol, agent-communication, task-assignment, conflict-resolution, synchronization
   - Regulates multi-agent collaboration

### 2. Physical Impact Tiers (Runtime Policy Dimension)

Physical Impact Tiers classify the severity of potential physical consequences:

- **Tier 0**: Information-level impact (no physical consequences)
- **Tier 1**: Minor physical impact (sub-threshold actuations)
- **Tier 2**: Moderate physical impact (within operational bounds)
- **Tier 3**: Major physical impact (approaching safety limits)
- **Tier 4**: Critical physical impact (potential harm/damage)

**Key Insight**: Tier classification enables **policy-level enforcement at physical actuation boundary** rather than relying solely on model behavior.

### 3. Implementation Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Natural Language Command Input                          │
└─────────────────────┬───────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────┐
│  ZTPM Policy Engine                                      │
│  ├─ Command Validation Domain (Primitives: 4)           │
│  ├─ Agent Behavior Domain (Primitives: 4)               │
│  ├─ Physical Actuation Domain (Primitives: 5)           │
│  ├─ Model Interface Domain (Primitives: 4)              │
│  ├─ Cross-Agent Coordination Domain (Primitives: 8)     │
│  └─ Physical Impact Tier Assessment                      │
└─────────────────────┬───────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────┐
│  Physical Actuation Boundary Enforcement                 │
│  ├─ Tier-based policy activation                         │
│  ├─ Parameter validation                                 │
│  ├─ Safety constraint enforcement                        │
│  └─ Fallback mechanisms                                  │
└─────────────────────┬───────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────┐
│  Industrial Robot (UR3e) Actuation                       │
└─────────────────────────────────────────────────────────┘
```

### 4. Key Empirical Findings

From 60 execution traces on two LFM backends:
- **Actuation parameter selection is model-dependent**
- **Parameter selection is non-deterministic** (same command → different parameters)
- **Physical actuation boundary requires policy-level enforcement** (not model-level)

### 5. Deployment Case Study: Cobot-Claw

Cobot-Claw is a **deployed four-agent system** for UR3e robotic arm control:
- Agent 1: Natural language command parser
- Agent 2: Task decomposition planner
- Agent 3: Motion trajectory generator
- Agent 4: Physical actuation controller

ZTPM prevents security failures from cascading across agent chain to physical consequences.

## Implementation Patterns

### Pattern 1: Tier-Based Policy Activation

```python
def enforce_tier_based_policy(command, tier_level):
    """
    Activate policy primitives based on Physical Impact Tier.
    
    Args:
        command: Natural language command
        tier_level: Physical Impact Tier (0-4)
    
    Returns:
        Policy enforcement decision
    """
    policy_primitives = select_primitives_by_tier(tier_level)
    
    # Tier 0: Minimal enforcement
    if tier_level == 0:
        enforce_domain('command_validation', ['command-origin', 'command-syntax'])
    
    # Tier 1-2: Standard enforcement
    elif tier_level in [1, 2]:
        enforce_domain('command_validation', all_primitives)
        enforce_domain('agent_behavior', ['agent-permission', 'agent-capability'])
    
    # Tier 3: Enhanced enforcement
    elif tier_level == 3:
        enforce_all_domains()
        enforce_domain('physical_actuation', ['actuation-limit', 'actuation-zone'])
    
    # Tier 4: Critical enforcement
    elif tier_level == 4:
        enforce_all_domains()
        enforce_domain('physical_actuation', all_primitives)
        require_human_approval()
    
    return validate_actuation_parameters()
```

### Pattern 2: Physical Actuation Boundary Enforcement

```python
def enforce_actuation_boundary(parameters, tier_level):
    """
    Enforce safety constraints at physical actuation boundary.
    
    Args:
        parameters: Actuation parameters from LFM
        tier_level: Physical Impact Tier
    
    Returns:
        Safe parameters or rejection
    """
    # Validate parameters against physical constraints
    constraints = get_physical_constraints(tier_level)
    
    for param in parameters:
        if param['type'] in ['speed', 'force', 'range']:
            if param['value'] > constraints[param['type']]:
                # Apply fallback or reject
                return apply_fallback_policy(param, constraints)
    
    return parameters
```

### Pattern 3: Multi-Agent Coordination Enforcement

```python
def enforce_coordination_policy(agent_chain):
    """
    Enforce cross-agent coordination primitives.
    
    Args:
        agent_chain: Sequence of agents processing command
    
    Returns:
        Coordination validation result
    """
    primitives = [
        'coordination-protocol',
        'agent-communication',
        'task-assignment',
        'conflict-resolution',
        'synchronization'
    ]
    
    for i, agent in enumerate(agent_chain):
        # Validate agent permission to communicate with next agent
        if not validate_agent_delegation(agent, agent_chain[i+1]):
            return reject_command('Invalid agent delegation chain')
        
        # Validate task assignment permissions
        if not validate_task_assignment_permission(agent):
            return reject_command('Unauthorized task assignment')
    
    return approve_coordination_chain()
```

## Technical Implementation Details

### 1. Primitive Type Definitions

Each primitive has:
- **Type**: (command, agent, actuation, model, coordination)
- **Scope**: (domain-specific, cross-domain)
- **Enforcement Level**: (validation, constraint, fallback)
- **Tier Requirement**: (0-4)

### 2. Policy Engine Architecture

**Components**:
1. **Policy Registry** - stores all primitive definitions
2. **Tier Classifier** - assesses physical impact tier
3. **Primitive Selector** - activates primitives by tier
4. **Enforcement Engine** - applies policy decisions
5. **Fallback Manager** - handles policy violations

### 3. Integration with LFM Backends

- Monitor LFM parameter selection variability
- Detect non-deterministic parameter generation
- Apply policy-level constraints regardless of model behavior
- Implement fallback mechanisms for parameter rejection

## When to Use This Skill

Use ZTPM when:
- Designing security for agentic CPS systems
- Multi-agent systems control physical devices via LFMs
- Need to enforce security at physical actuation boundary
- Addressing non-deterministic LFM parameter selection
- Implementing tiered security policies
- Protecting industrial robots from malicious commands

## Related Skills

- `agent-security-framework` - general agent security patterns
- `cps-resilience-roadmap` - CPS resilience design
- `distributed-quantum-control-systems` - distributed control patterns
- `systems-engineering-apr2026` - recent systems engineering patterns

## References

- arXiv:2605.25653 - Original paper
- Cobot-Claw deployment system
- UR3e robotic arm specifications
- LFM security frameworks

## Pitfalls & Lessons Learned

### Pitfall 1: Model-Level Enforcement Insufficient

**Problem**: Relying on LFM output validation alone is insufficient due to:
- Non-deterministic parameter selection
- Model-dependent behavior variability
- Incomplete coverage of attack classes

**Solution**: Implement **policy-level enforcement at physical actuation boundary** regardless of model behavior.

### Pitfall 2: Tier Underestimation

**Problem**: Underestimating physical impact tier leads to insufficient policy activation.

**Solution**: Use conservative tier estimation, default to Tier 3 for uncertain commands, require human approval for Tier 4.

### Pitfall 3: Agent Chain Vulnerability

**Problem**: Single compromised agent can cascade failure through multi-agent chain.

**Solution**: Enforce **cross-agent coordination primitives** at each agent transition, validate delegation chains.

## Verification Steps

1. Test all 25 primitives against command validation
2. Verify tier-based policy activation
3. Validate physical actuation boundary enforcement
4. Test fallback mechanisms for parameter rejection
5. Simulate all 5 attack classes
6. Validate agent chain coordination
7. Measure non-deterministic parameter selection variability

## Future Research Directions

1. Automated tier classification from natural language commands
2. Learning-based policy primitive optimization
3. Cross-modal enforcement (vision + language + actuation)
4. Real-time policy adaptation
5. Formal verification of ZTPM policies