---
name: llm-agent-externalization
description: "Design LLM agent systems using the externalization framework from cognitive artifacts theory (Norman). Covers memory externalization (state across time), skills externalization (procedural expertise), protocol externalization (interaction structure), and harness engineering (unification layer). Use when architecting multi-tool LLM agents, building agent frameworks, designing memory/skills/protocol systems, or unifying agent components. Keywords: agent externalization, cognitive artifacts, memory system, skill system, protocol system, harness engineering, agent architecture, Norman theory, LLM agent design, tool use patterns."
---

# LLM Agent Externalization Framework

Design LLM agent systems using the externalization paradigm: transform internal cognitive burdens into structured external artifacts. Grounded in Norman's cognitive artifacts theory (1991, 1993) and unified by Zhou et al. (arXiv: 2604.08224).

## Core Theory

**Externalization Principle**: Offload cognitive work from the LLM's internal context into structured external systems. Each system transforms a specific type of cognitive burden:

| System | Externalizes | Cognitive Burden | Artifact Type |
|--------|-------------|-----------------|---------------|
| Memory | State across time | Context window limits, forgetting | Records, embeddings, graphs |
| Skills | Procedural expertise | Prompt engineering, step planning | Tools, functions, modules |
| Protocols | Interaction structure | Coordination overhead, ambiguity | APIs, schemas, workflows |
| Harness | Integration complexity | Cross-system orchestration | Orchestrator, router, loop |

## 1. Memory Systems (Externalized State)

Memory transforms the LLM's transient context into persistent, searchable, and evolvable state.

### Memory Taxonomy

| Type | Timescale | Granularity | Storage | Use Case |
|------|-----------|-------------|---------|----------|
| Episodic | Session | Turn-level | Conversation log | Current task context |
| Semantic | Long-term | Fact-level | Vector DB / KG | Knowledge accumulation |
| Procedural | Permanent | Action-level | Skill registry | Learned behaviors |
| Meta | Cross-session | System-level | Config / prompt | Agent self-knowledge |

### Memory Operations

```
[Write] → Encode context → Store with metadata
[Read]  → Retrieve by query → Rank by relevance → Inject into context
[Update] → Detect staleness → Merge/replace → Version control
[Forget] → Prune low-value → Compress → Archive
```

### Design Patterns

**Pattern A: Hierarchical Memory**
```
Working Memory (in-context, immediate)
    ↓
Short-term Memory (session cache, recent turns)
    ↓
Long-term Memory (persistent DB, semantic index)
    ↓
Archive (cold storage, compressed summaries)
```

**Pattern B: Dual-Path Memory**
```
Fast Path: Semantic similarity → Top-k retrieval → Inject
Slow Path: Reasoning over memory → Graph traversal → Synthesize
```

**Pattern C: Memory-Aware Prompting**
- Dynamically adjust memory injection based on context budget
- Prioritize high-importance, high-recency entries
- Compress older memories into summaries before injection

### Pitfalls

- **Over-retrieval**: Injecting too many memories dilutes signal; cap at 5-10 entries
- **Stale memory**: Without TTL or decay, outdated facts cause errors
- **Memory bloat**: Unbounded growth degrades retrieval quality; implement pruning
- **Context fragmentation**: Disconnected memory shards lose coherence; maintain linkage

## 2. Skills Systems (Externalized Expertise)

Skills transform procedural knowledge—normally encoded in prompts—into executable, discoverable modules.

### Skill Architecture

```
Skill Registry
├── Discovery (search, list, match by description)
├── Selection (relevance scoring, context-aware ranking)
├── Execution (invoke with structured input/output)
└── Composition (chain, parallel, conditional)
```

### Skill Design Principles

1. **Single Responsibility**: Each skill solves one class of problem
2. **Structured I/O**: Define explicit input schemas and output contracts
3. **Self-Documenting**: Name, description, and usage examples enable LLM discovery
4. **Composable**: Skills chain via shared data formats, not implicit state

### Skill Lifecycle

```
Create → Register → Discover → Select → Execute → Evaluate → Update/Retire
```

### Design Patterns

**Pattern A: Tool-Function Mapping**
```python
skill = {
    "name": "csv_analyzer",
    "description": "Analyze CSV data: summary stats, correlations, distributions",
    "input_schema": {"file_path": "str", "analysis_type": "enum[summary, correlation, distribution]"},
    "output_schema": {"result": "str", "charts": "list[ImageRef]", "insights": "list[str]"},
    "implementation": "scripts/csv_analyzer.py"
}
```

**Pattern B: Skill Hierarchy**
```
Domain Skills
├── Data Skills (load, transform, analyze, visualize)
├── Code Skills (generate, debug, refactor, test)
├── Research Skills (search, synthesize, cite, compare)
└── Communication Skills (summarize, translate, format, critique)
```

**Pattern C: Dynamic Skill Loading**
- Load only skills relevant to current task
- Lazy-load heavy skills on first use
- Cache recently-used skills in warm state

### Pitfalls

- **Skill bloat**: Too many registered skills increase selection overhead; maintain focused registries
- **Ambiguous descriptions**: Poor descriptions cause mis-selection; use concrete examples
- **Tight coupling**: Skills that depend on each other create fragile chains; use shared schemas
- **State leakage**: Skills mutating global state cause unpredictable behavior; enforce isolation

## 3. Protocol Systems (Externalized Interaction)

Protocols transform ad-hoc agent interactions into structured, verifiable, and reproducible exchanges.

### Protocol Layers

| Layer | Concern | Example |
|-------|---------|---------|
| Syntax | Message format | JSON schema, XML, protobuf |
| Semantics | Meaning of operations | CRUD verbs, intent types |
| Pragmatics | Context and state | Session IDs, turn counters |
| Meta-Protocol | Protocol about protocols | Negotiation, fallback, escalation |

### Protocol Design Patterns

**Pattern A: Request-Response Protocol**
```json
{
  "protocol_version": "1.0",
  "session_id": "sess_abc123",
  "turn": 3,
  "sender": "agent_orchestrator",
  "receiver": "skill_executor",
  "intent": "execute",
  "payload": {"skill_name": "csv_analyzer", "params": {"file": "data.csv"}},
  "constraints": {"timeout_ms": 30000, "max_retries": 2}
}
```

**Pattern B: Multi-Agent Handshake**
```
Agent A → Broadcast: "I need data analysis"
Agent B → Respond: "I can help, my capabilities: [list]"
Agent A → Select: "You're chosen. Here's the context"
Agent B → Execute: "Here are the results"
Agent A → Acknowledge: "Received, integrating"
```

**Pattern C: Error Recovery Protocol**
```
On failure:
  1. Classify error (transient vs. permanent)
  2. Retry with backoff (if transient)
  3. Escalate to supervisor (if permanent)
  4. Fallback to alternative skill (if available)
  5. Report to user (if all else fails)
```

### Pitfalls

- **Protocol drift**: Unversioned protocols cause silent incompatibilities; always version
- **Over-specification**: Too rigid protocols limit agent flexibility; allow extensibility
- **Missing error paths**: Protocols without failure handling cascade into system failures
- **Hidden assumptions**: Implicit protocol requirements cause integration bugs; document everything

## 4. Harness Engineering (Unification Layer)

The harness is the meta-system that coordinates memory, skills, and protocols into a coherent agent. It is the "operating system" for LLM agents.

### Harness Architecture

```
┌─────────────────────────────────────────┐
│              HARNESS LAYER               │
├──────────┬──────────┬───────────────────┤
│  Router  │ Planner  │    State Manager  │
├──────────┴──────────┴───────────────────┤
│          Execution Loop                  │
│  Input → Parse → Plan → Execute → Output │
├──────────┬──────────┬───────────────────┤
│  Memory  │  Skills  │    Protocols       │
│  System  │  System  │    System          │
└──────────┴──────────┴───────────────────┘
```

### Harness Components

**Router**: Directs incoming requests to appropriate skill/memory/protocol
- Intent classification → Skill matching → Confidence scoring
- Fallback: escalate to planner or human

**Planner**: Decomposes complex tasks into executable steps
- Task decomposition → Dependency resolution → Execution ordering
- Re-plan on failure or unexpected results

**State Manager**: Maintains execution context across components
- Track active skills, memory state, protocol sessions
- Checkpoint/restore for long-running tasks

### Execution Loop Patterns

**Pattern A: ReAct-style Loop**
```python
while not task_complete:
    thought = plan(current_state, goal)
    action = select_skill(thought)
    observation = execute(action)
    update_state(observation)
```

**Pattern B: Hierarchical Planning**
```
Top-level: decompose task into subgoals
Mid-level: plan skill sequences for each subgoal
Low-level: execute individual skill invocations
```

**Pattern C: Reflective Loop**
```
Act → Observe → Reflect → Re-plan → Act (improved)
```

### Design Principles

1. **Separation of Concerns**: Harness orchestrates; skills execute; memory stores; protocols communicate
2. **Observability**: Log all decisions, skill calls, memory accesses for debugging
3. **Graceful Degradation**: When a component fails, fall back to simpler alternatives
4. **Bounded Context**: Each component has clear responsibility boundaries

## Practical Implementation

### Quick Start: Minimal Agent

```python
class ExternalizedAgent:
    def __init__(self, llm, memory, skill_registry, protocol):
        self.llm = llm
        self.memory = memory
        self.skills = skill_registry
        self.protocol = protocol
    
    def run(self, user_input):
        # 1. Retrieve relevant memory
        context = self.memory.retrieve(user_input)
        
        # 2. Plan with LLM
        plan = self.llm.plan(user_input, context)
        
        # 3. Select and execute skills
        for step in plan.steps:
            skill = self.skills.select(step.intent)
            result = self.protocol.execute(skill, step.params)
            self.memory.write(step, result)
        
        # 4. Synthesize response
        return self.llm.synthesize(user_input, self.memory.read_recent())
```

### Integration Checklist

- [ ] Memory: persistent store with retrieval, update, and pruning
- [ ] Skills: registry with structured I/O, discovery, and isolation
- [ ] Protocols: versioned message format with error handling
- [ ] Harness: execution loop with planning, routing, and state tracking
- [ ] Observability: logging, metrics, and debugging interfaces
- [ ] Testing: unit tests for skills, integration tests for harness

## Best Practices Summary

| Principle | Do | Don't |
|-----------|----|-------|
| Memory | Prune aggressively, version entries | Inject everything, forget to expire |
| Skills | Keep focused, document well | Create mega-tools, vague descriptions |
| Protocols | Version, handle errors | Implicit assumptions, no failure paths |
| Harness | Separate concerns, observe everything | Monolithic design, blind execution |
| General | Start minimal, iterate based on usage | Over-engineer upfront, ignore user patterns |

## Applications

- Multi-tool LLM agent design (coding assistants, research agents)
- Enterprise agent platforms (customer service, data analysis)
- Multi-agent collaboration systems (agent swarms, role-based agents)
- Agent framework evaluation and comparison
- Cognitive architecture design for AI systems

## Related Skills

- `agent-memory-framework`: Memory-augmented agents with RL optimization
- `agent-memory-management`: Memory lifecycle and retrieval patterns
- `agent-collaboration-protocol`: Multi-agent interaction patterns
- `skill-creator`: Guide for creating effective skills
- `skill-extractor`: Extract skill patterns from conversations

## References

- **Externalization in LLM Agents** (arXiv: 2604.08224) — Zhou et al., April 2026. Shanghai Jiao Tong University, Sun Yat-Sen University, CMU, OPPO.
- **Cognitive Artifacts** (Norman, 1991, 1993) — Foundation theory for externalizing cognitive work into designed artifacts.
- **ReAct** (Yao et al., 2022) — Reasoning and acting loop for LLM agents.
- **Toolformer** (Schick et al., 2023) — LLMs that learn to use tools.

## Notes

- The externalization framework provides a principled vocabulary for agent design decisions
- Each externalization axis (memory, skills, protocols) can be designed independently and integrated via the harness
- The harness layer is where most agent frameworks differentiate—the choice of execution loop, routing strategy, and state management defines agent behavior
- Start with minimal externalization; add complexity only when the cognitive burden justifies it
