# Agentic Reinforcement Learning for LLMs

## Description

Agentic RL transforms LLMs from passive sequence generators into autonomous, decision-making agents. This skill covers the paradigm shift from conventional LLM-RL (single-step MDPs) to Agentic RL (temporally extended POMDPs), including planning, tool use, memory, reasoning, self-improvement, and perception capabilities.

**Key Contributions:**
- Formalizes conceptual shift from LLM-RL to Agentic RL
- Two-fold taxonomy: agentic capabilities + task domains
- RL as mechanism for transforming static modules to adaptive behavior
- Consolidates 500+ works into practical compendium

## Tools Used

- read: Read agent state and environment observations
- exec: Execute actions in environment
- write: Store memories and plans
- browser: Access external tools and APIs
- memory_search: Retrieve relevant past experiences

## Instructions for Agents

### Core Agentic Capabilities

1. **Planning** - Generate and execute multi-step action sequences
2. **Tool Use** - Select and invoke appropriate tools
3. **Memory** - Store and retrieve relevant information
4. **Reasoning** - Chain-of-thought and decomposition
5. **Self-Improvement** - Learn from experience via RL
6. **Perception** - Process multi-modal inputs

### Key Paradigm Shift

| LLM-RL (Conventional) | Agentic RL |
|-----------------------|------------|
| Single-step MDP | Temporally extended POMDP |
| Passive generation | Autonomous decision-making |
| Static prompts | Dynamic environment interaction |
| No memory | Persistent memory |
| No planning | Multi-step planning |

### When to Use

- Multi-step reasoning tasks
- Environment interaction required
- Tool selection decisions
- Memory-dependent decisions
- Self-improvement loops

## Overview

**Source:** arXiv:2509.02547v4
**Utility:** 0.94
**Authors:** 23 authors from 14 institutions
**Scope:** 500+ works synthesized

## Activation Keywords

- agentic RL
- LLM reinforcement learning
- agent planning
- tool use RL
- LLM decision making

---

## Core Framework

### From MDP to POMDP

**LLM-RL (Single-step MDP):**
```
State (prompt) → Action (token) → Reward → Next State
```

**Agentic RL (POMDP):**
```
Observation → Belief State → Plan → Actions → Observations → ...
     ↓              ↓           ↓
   Memory       Reasoning    Tool Use
```

### Agentic Capabilities Taxonomy

| Capability | Description | RL Role |
|------------|-------------|---------|
| Planning | Multi-step action generation | Learn optimal plans |
| Tool Use | External API/tool selection | Learn tool policies |
| Memory | Information persistence | Learn what to store |
| Reasoning | Chain-of-thought | Learn reasoning strategies |
| Self-Improvement | Learning from experience | Meta-learning |
| Perception | Multi-modal processing | Learn representations |

---

## Implementation Patterns

### 1. Planning Agent

```python
class PlanningAgent:
    def __init__(self, llm, env):
        self.llm = llm
        self.env = env
    
    def plan(self, goal):
        # Generate high-level plan
        plan = self.llm.generate_plan(goal)
        
        # Execute with RL-learned policy
        for step in plan:
            action = self.policy(step)
            obs, reward = self.env.step(action)
            self.update_memory(obs, reward)
```

### 2. Tool-Using Agent

```python
class ToolUsingAgent:
    def __init__(self, tools, policy_network):
        self.tools = tools
        self.policy = policy_network
    
    def select_tool(self, context):
        # RL-learned tool selection
        tool_probs = self.policy(context)
        return self.tools[sample(tool_probs)]
    
    def execute(self, tool, inputs):
        return tool.execute(inputs)
```

### 3. Memory-Augmented Agent

```python
class MemoryAgent:
    def __init__(self, memory_size=1000):
        self.memory = []
        self.retrieval_policy = None  # RL-learned
    
    def store(self, observation, action, reward):
        # Learn what to remember
        if self.should_store(observation):
            self.memory.append((observation, action, reward))
    
    def retrieve(self, context):
        # RL-learned retrieval
        return self.retrieval_policy(context, self.memory)
```

---

## Key Applications

| Domain | Agentic RL Use |
|--------|----------------|
| Web Navigation | Multi-step browsing, form filling |
| Code Generation | Planning, testing, debugging loops |
| Game Playing | Strategic decision making |
| Robotics | Sensorimotor control |
| Research | Literature search, experiment design |

---

## Benchmarks

| Benchmark | Focus | Environment |
|-----------|-------|-------------|
| WebShop | E-commerce navigation | Web |
| ALFWorld | Household tasks | Embodied |
| ScienceWorld | Scientific reasoning | Text |
| InterCode | Code execution | Terminal |
| ToolBench | Tool use | API |

---

## Training Approaches

### 1. Policy Gradient Methods

```python
# PPO-style update for agentic behavior
def agentic_ppo_update(agent, trajectories):
    for traj in trajectories:
        returns = compute_returns(traj.rewards)
        advantages = returns - traj.values
        
        # Update policy
        ratio = new_prob / old_prob
        clip_ratio = torch.clamp(ratio, 1-eps, 1+eps)
        loss = -torch.min(ratio * advantages, clip_ratio * advantages)
```

### 2. Reward Shaping for Agents

```python
def agentic_reward(action, outcome, plan):
    reward = 0
    reward += outcome.success * 1.0      # Task completion
    reward += plan.efficiency * 0.1      # Plan quality
    reward += action.validity * 0.1      # Valid actions
    reward -= step_cost * 0.01           # Encourage efficiency
    return reward
```

---

## Open-Source Resources

### Environments
- OpenAI Gym
- RL4LMs
- AgentBench
- WebArena

### Frameworks
- LangChain
- AutoGPT
- BabyAGI
- MetaGPT

---

## Best Practices

1. **Start with clear objectives** - Define success metrics
2. **Design reward functions carefully** - Shape agent behavior
3. **Use curriculum learning** - Start simple, increase complexity
4. **Enable self-improvement** - Let agents learn from mistakes
5. **Monitor for reward hacking** - Agents may exploit loopholes

---

## Examples

### Example 1: Basic Application

**User:** I need to apply Agentic Reinforcement Learning for LLMs to my analysis.

**Agent:** I'll help you apply agentic-rl-llm-survey. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Multi-step reasoning tasks

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for agentic-rl-llm-survey?

**Agent:** Let me search for the latest research and best practices...

## References

- Paper: https://arxiv.org/abs/2509.02547
- DOI: https://doi.org/10.48550/arXiv.2509.02547
- TMLR: https://openreview.net/forum?id=RY19y2RI1O

---

**Created:** 2026-03-28
**Source:** arXiv:2509.02547v4 - "The Landscape of Agentic RL for LLMs"