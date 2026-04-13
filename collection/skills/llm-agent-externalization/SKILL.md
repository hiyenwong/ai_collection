---
name: llm-agent-externalization
description: "Externalization in LLM Agents - unified review of memory, skills, protocols and harness engineering. Agent capabilities externalized into cognitive artifacts for reliability and composability. Use for: agent architecture, LLM agent design, externalized memory, agent skills, agent protocols, cognitive artifacts. Activation: agent externalization, LLM agent architecture, agent memory externalization, agent skills, agent harness, cognitive artifacts."
---

# Externalization in LLM Agents

Unified review of how LLM agents externalize capabilities into memory stores, reusable skills, interaction protocols, and harness engineering.

## Overview

Large language model (LLM) agents are increasingly built less by changing model weights than by reorganizing the runtime around them. Capabilities that earlier systems expected the model to recover internally are now **externalized** into:

1. **Memory Stores**: Persistent external memory
2. **Reusable Skills**: Composable capability modules
3. **Interaction Protocols**: Structured communication patterns
4. **Harness Engineering**: Runtime infrastructure

Drawing on the idea of **cognitive artifacts**, this framework argues that agent infrastructure transforms hard cognitive tasks into tractable engineering problems.

## Core Concepts

### Cognitive Artifacts

**Definition**: External representations that support cognitive processes.

```
Internal Cognition (Model Weights) → External Artifacts (Runtime)

Examples:
- Mental arithmetic → Calculator (external computation)
- Memory recall → Notes/Database (external storage)
- Planning → Calendar/Project management (external organization)
```

### The Externalization Shift

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT ARCHITECTURE EVOLUTION                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   EARLY AGENTS              →           MODERN AGENTS           │
│   (Model-Centric)                       (Externalization-Centric)│
│                                                                  │
│   ┌──────────────┐                      ┌──────────────┐        │
│   │   LLM Core   │                      │   LLM Core   │        │
│   │              │                      │   (Thin)     │        │
│   │  All logic   │                      │              │        │
│   │  All memory  │                      └──────┬───────┘        │
│   │  All skills  │                             │                │
│   └──────────────┘              ┌──────────────┼──────────────┐ │
│                                 │              │              │ │
│                          ┌──────┴──────┐ ┌────┴────┐ ┌──────┴┐│
│                          │   Memory    │ │ Skills  │ │Harness││
│                          │   Store     │ │ Module  │ │Engine ││
│                          └─────────────┘ └─────────┘ └───────┘│
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Four Pillars of Externalization

### 1. Memory Stores

**Purpose**: Extend limited context window with persistent external memory.

```
Types of External Memory:
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Working Memory          Short-term storage during task     │
│  │                                                          │
│  ├── Context Window      Model's native attention           │
│  └── Scratchpad          Temporary computation space        │
│                                                             │
│  Reference Memory        Long-term knowledge storage        │
│  │                                                          │
│  ├── Vector Store        Semantic search (RAG)              │
│  ├── Knowledge Graph     Structured relationships           │
│  └── Document Cache      Raw text retrieval                 │
│                                                             │
│  Episodic Memory         Past interactions and experiences  │
│  │                                                          │
│  ├── Conversation History Previous turns                    │
│  ├── Session State       Current task context               │
│  └── User Profile        Preferences and patterns           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Key Insight**: Memory externalization converts "recall from weights" (hard) to "retrieve from store" (tractable).

### 2. Reusable Skills

**Purpose**: Package capabilities as composable, testable modules.

```
Skill Structure:
┌─────────────────────────────────────────────────────────────┐
│  Skill: Code Execution                                       │
├─────────────────────────────────────────────────────────────┤
│  Interface:                                                  │
│    - Input: code (str), language (str)                       │
│    - Output: result (dict)                                   │
│    - Errors: TimeoutError, SyntaxError, SecurityError        │
│                                                              │
│  Implementation:                                             │
│    - Sandbox environment                                     │
│    - Resource limits (CPU, memory, time)                     │
│    - Security policies                                       │
│                                                              │
│  Examples:                                                   │
│    - execute_python("print('hello')")                        │
│    - execute_bash("ls -la")                                  │
│                                                              │
│  Tests:                                                      │
│    - Unit tests for each language                            │
│    - Security test cases                                     │
│    - Performance benchmarks                                  │
└─────────────────────────────────────────────────────────────┘
```

**Benefits**:
- **Composability**: Skills combine into workflows
- **Testability**: Each skill independently verified
- **Reusability**: Use across different agents
- **Observability**: Clear boundaries for monitoring

### 3. Interaction Protocols

**Purpose**: Structure communication between agents and with users.

```
Protocol Layers:
┌─────────────────────────────────────────────────────────────┐
│  Application Layer    Task-specific protocols               │
│  │                                                          │
│  ├── Tool Use         Structured function calling           │
│  ├── Planning         Goal decomposition protocols          │
│  └── Collaboration    Multi-agent coordination              │
│                                                             │
│  Session Layer        Conversation management               │
│  │                                                          │
│  ├── Turn-taking      Who speaks when                       │
│  ├── Context passing  State transfer between turns          │
│  └── Clarification    Ambiguity resolution                  │
│                                                             │
│  Transport Layer      Message delivery                      │
│  │                                                          │
│  ├── Schema           Structured message formats            │
│  ├── Validation       Input/output checking                 │
│  └── Error handling   Recovery from failures                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Example - Tool Use Protocol**:
```python
# Structured tool invocation
{
    "thought": "I need to search for information",
    "action": "web_search",
    "arguments": {"query": "latest AI research"},
    "expected_result": "list of papers"
}

# Structured response
{
    "observation": "Found 5 papers...",
    "result": [...],
    "status": "success"
}
```

### 4. Harness Engineering

**Purpose**: Runtime infrastructure that makes externalized components reliable.

```
Harness Components:
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  Orchestration                                               │
│  ├── Workflow engine         Execute skill sequences        │
│  ├── State machine           Manage agent lifecycle         │
│  └── Event handling          React to triggers              │
│                                                             │
│  Resilience                                                  │
│  ├── Retry logic             Handle transient failures      │
│  ├── Circuit breakers        Prevent cascade failures       │
│  └── Fallbacks               Graceful degradation           │
│                                                             │
│  Observability                                               │
│  ├── Logging                 Record actions and decisions   │
│  ├── Metrics                 Performance measurement        │
│  └── Tracing                 End-to-end request tracking    │
│                                                             │
│  Security                                                    │
│  ├── Sandboxing              Isolate untrusted code         │
│  ├── Policy enforcement      Apply safety constraints       │
│  └── Audit logging           Compliance tracking            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Design Principles

### 1. Separation of Concerns

```
Model Responsibility          Runtime Responsibility
─────────────────────         ─────────────────────
Pattern matching              State management
Text generation               Tool orchestration
Reasoning (in-context)        Long-term memory
Language understanding        Protocol enforcement
```

### 2. Composability

```
Small Skills → Workflows → Complex Tasks

Example:
  read_file → analyze_content → write_summary
  
  [Skill]     [Skill]          [Skill]
     │            │                │
     └────────────┴────────────────┘
                  │
            [Workflow: Document Analysis]
```

### 3. Testability

```
Externalized Component:
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│   Input     │─────→│  Component  │─────→│   Output    │
│  (known)    │      │  (isolated) │      │ (verifiable)│
└─────────────┘      └─────────────┘      └─────────────┘

Can test:
- Unit tests for each skill
- Integration tests for workflows
- Property-based tests for protocols
```

### 4. Observability

```
Externalized systems enable:
- Clear input/output boundaries
- Explicit state transitions
- Measurable performance
- Debuggable failures
```

## Implementation Patterns

### Pattern 1: Memory-Augmented Agent

```python
class MemoryAugmentedAgent:
    def __init__(self, llm, memory_store):
        self.llm = llm
        self.memory = memory_store
    
    def run(self, task):
        # 1. Retrieve relevant context
        context = self.memory.retrieve(task)
        
        # 2. Augment prompt
        prompt = f"Context: {context}\nTask: {task}"
        
        # 3. Generate with LLM
        response = self.llm.generate(prompt)
        
        # 4. Store interaction
        self.memory.store(task, response)
        
        return response
```

### Pattern 2: Skill-Based Agent

```python
class SkillBasedAgent:
    def __init__(self, llm, skills):
        self.llm = llm
        self.skills = {s.name: s for s in skills}
    
    def execute(self, intent):
        # 1. Select skill
        skill_name = self.select_skill(intent)
        skill = self.skills[skill_name]
        
        # 2. Extract parameters
        params = self.extract_params(intent, skill)
        
        # 3. Execute skill
        result = skill.execute(**params)
        
        return result
```

### Pattern 3: Protocol-Driven Agent

```python
class ProtocolDrivenAgent:
    def __init__(self, llm, protocol):
        self.llm = llm
        self.protocol = protocol
        self.state = "idle"
    
    def interact(self, message):
        # 1. Validate message against protocol
        if not self.protocol.validate(message, self.state):
            return self.protocol.error_response()
        
        # 2. Process message
        response = self.llm.generate(message)
        
        # 3. Update state
        self.state = self.protocol.next_state(self.state, message)
        
        return response
```

## Comparison: Internal vs External

| Aspect | Internal (Model-Centric) | External (Runtime-Centric) |
|--------|-------------------------|---------------------------|
| Memory | Context window only | Unlimited external stores |
| Skills | Prompt engineering | Composable modules |
| Reliability | Best effort | Guaranteed by harness |
| Testing | End-to-end only | Unit + integration |
| Observability | Black box | White box |
| Updates | Retrain model | Update runtime |
| Cost | Inference only | Infrastructure + inference |

## Practical Implications

### For Agent Developers

1. **Design for externalization from the start**
2. **Invest in harness engineering**
3. **Build composable skills**
4. **Implement clear protocols**

### For System Architects

1. **Separate model and runtime concerns**
2. **Design observable boundaries**
3. **Plan for failure modes**
4. **Consider operational costs**

### For Researchers

1. **Study externalization patterns**
2. **Develop new harness components**
3. **Create skill libraries**
4. **Design standard protocols**

## References

- **Paper**: "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering" by Zhou et al. (arXiv:2604.08224v1, 2026)
- **Authors**: Chenyu Zhou, Huacan Chai, Wenteng Chen, et al.
- **Categories**: cs.SE (Software Engineering), cs.MA (Multi-Agent Systems)

## Related Skills

- **logact-agentic-reliability**: Shared log architecture for agent reliability
- **psi-shared-state-architecture**: PSI shared-state for personal AI agents
- **agent-memory-framework**: Memory-augmented AI agents
- **skill-creator**: Creating effective agent skills

## Activation Keywords

- agent externalization
- LLM agent architecture
- agent memory externalization
- agent skills
- agent harness
- cognitive artifacts
- agent runtime
- externalized capabilities
- agent infrastructure
- composable agents


## Tools Used

- `exec`
- `read`
- `write`


## Instructions for Agents

1. **理解需求**：分析用户请求的具体场景
2. **选择方法**：根据上下文选择合适的技术方案
3. **执行操作**：按照技能描述实施具体步骤
4. **验证结果**：检查结果是否符合预期


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...
