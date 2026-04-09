---
name: agentic-portfolio
description: 'Design multi-agent architectures for complex workflows using specialized agent roles, critique/vote mechanisms, and meta-agent self-improvement. Use when building multi-agent systems with 10+ specialized agents, implementing agent oversight pipelines, or creating self-improving agent workflows. Based on arXiv:2604.02279 - The Self Driving Portfolio: Agentic Architecture for Institutional Asset Management.'
---

# Agentic Architecture for Complex Workflows

Design multi-agent pipelines with specialized roles, voting, and self-improvement.

## Architecture Pattern

From "The Self Driving Portfolio" paper (50 specialized agents):

### 1. Specialized Agent Roles

Assign domain-specific roles:
- **Analyst agents**: Produce domain-specific assumptions
- **Constructor agents**: Apply competing methods (20+ methods)
- **Critic agents**: Evaluate and critique outputs
- **Voting agents**: Aggregate and select best approaches
- **Researcher agent**: Propose novel methods not yet represented
- **Meta-agent**: Compare forecasts vs. realized outcomes, rewrite agent code/prompts

### 2. Pipeline Structure

```
Input → Analysts → Constructors → Critics → Voters → Output
         ↓           ↓            ↓        ↓
      [Researcher proposes new methods]
         ↓
      [Meta-agent: compare forecasts vs. actuals → improve agents]
```

### 3. Governance by Policy Document

Key insight: **Investment Policy Statement** guides human portfolio managers → same document can constrain autonomous agents.

Any complex workflow can use similar governance:
- Define policy/guidelines document
- All agents operate within policy constraints
- Policy becomes the oversight mechanism

## Multi-Agent Coordination Patterns

### Critique and Vote Cycle

```python
# Each agent produces output
outputs = [agent_i.produce(context) for agent_i in constructors]

# Critic agents evaluate
critiques = [critic_j.evaluate(outputs) for critic_j in critics]

# Voting agents aggregate
best_output = voter.aggregate(critiques, outputs)
```

### Self-Improvement Loop

```python
# Meta-agent compares past forecasts vs. realized outcomes
comparison = meta_agent.compare(past_forecasts, realized_returns)

# Rewrite agent code/prompts based on gap
improved_agents = meta_agent.improve(agents, comparison)
```

## Key Design Principles

1. **Specialization**: Each agent has narrow, well-defined role
2. **Competition**: Multiple agents apply different methods, best selected
3. **Critique**: Independent evaluation before selection
4. **Voting**: Democratic aggregation of evaluations
5. **Self-improvement**: Meta-agent learns from outcomes
6. **Policy governance**: Document constrains all agent behavior

## When to Apply

- Complex workflows requiring multiple domain perspectives
- Tasks with many valid approaches (need competition)
- Systems needing self-improvement from feedback
- Workflows that humans oversee via policy documents
- Building robust multi-agent pipelines

## Scale Considerations

- 10-50 specialized agents for complex domains
- Multiple constructor agents for competing methods
- Independent critics for objective evaluation
- Single meta-agent for improvement coordination

## Benefits

- Shifts operator role from execution to oversight
- Leverages diverse expertise through specialization
- Self-improvement from outcome feedback
- Policy document provides human oversight interface

## Paper Reference

arXiv:2604.02279 - "The Self Driving Portfolio: Agentic Architecture for Institutional Asset Management" (Apr 2026)
## Activation Keywords

- agentic-portfolio
- agentic-portfolio 技能
- agentic-portfolio skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Specialization

### Step 2: Competition

### Step 3: Critique

### Step 4: Voting

### Step 5: Self-improvement

## Examples

### Example 1: Basic Application

**User:** I need to apply Agentic Architecture for Complex Workflows to my analysis.

**Agent:** I'll help you apply agentic-portfolio. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for agentic-portfolio?

**Agent:** Let me search for the latest research and best practices...
