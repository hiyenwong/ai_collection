---
name: spec-driven-agent-architecture
description: "Workflow and architecture patterns for building robust AI agents using Specs, Contracts, and Repository patterns."
category: "devops"
---

# Spec-Driven Agent Architecture

Build robust AI agent systems using **Spec-Driven Development**, **Contract Enforcement**, and **Pluggable Repositories**.

## Workflow

1.  **Define Spec**: Create YAML specification in `specs/` (e.g., `specs/agents/`, `specs/schemas/`).
2.  **Define Contract**: Create Python contract in `contracts/` (Preconditions, Postconditions, Invariants).
3.  **Implement**: Build code following Repository Pattern (Abstract Base Class -> Concrete Implementation).
4.  **Validate**: Ensure implementation passes `eval/` tests.
5.  **Commit**: Task-level commit (No `git add .`).

## Core Architecture Components

### 1. Orchestrator (The Brain)
-   Loads Agent Specs from YAML.
-   Manages execution flow (State Machine / Pipeline).
-   Enforces Contracts before and after execution.
-   Integrates with Knowledge Service.

### 2. Agent Network Topology
The system runs four agents in a directed pipeline with feedback loops:

```
              Research (Tier 1)
            findings/  │ \context (indirect)
              ↓        │  \
    Planning (Tier 2)  →──→ Build (Tier 3)
       task plan  ↓    \    ↓ output
                  \     \   ↓
                   ───→ Eval (Tier 4)
                        ↑      │
                  retry ↺──────┘  (failed → re-plan / rebuild)
```

- **Research**: `web_search`, `file_read`, `github_search`. Outputs findings + sources with confidence ratings. Escalates on 3 empty searches, all-low confidence, or knowledge gap beyond scope.
- **Planning**: `file_read`. Outputs phased plans with deliverables, dependencies, risks. Escalates on insufficient research, ambiguous vision, or missing dependency info.
- **Build**: `file_read`, `file_write`, `shell_exec`, `test_runner`. Outputs code + tests. Escalates on contract failure, dependency install failure, or out-of-scope modification.
- **Eval**: `file_read`. Scores outputs against rubric, checks contracts. Escalates on missing spec, unparseable output, or inconsistent scoring (>0.3 delta on same input).

**Spec-to-topology**: Agent specs in `specs/agents/*.yaml` define roles, tools, escalation conditions. The orchestrator loads all specs to reconstruct the network at runtime.

### 3. Knowledge Service (The Data Layer)
-   **Repository Pattern**: Define `KnowledgeRepository` interface. Implementations for SQLite, Postgres, etc.
-   **Separation of Concerns**: Persistent Knowledge (Facts, Entities) vs. Runtime Memory (Tasks, Sessions).
-   **Self-Validation**: The Knowledge Base maintains `entity_specs` and validates entities *before* insertion.
    -   *Example*: "Concepts must have min_confidence > 0.8", "Decisions must have 'approved' tag".

### 3. Contract Validator (The Enforcer)
-   Checks `preconditions` (input validity).
-   Checks `postconditions` (output correctness).
-   Checks `invariants` (global rules, e.g., no secrets).

### 4. Agent Runtime (Tool-Use Loop)
Each Agent inherits `BaseAgent` which implements a **ReAct-style tool-use loop**:

```
Agent.execute()
  → pre-condition check
  → build_messages(with tool defs injected per role)
  → _tool_use_loop():
      LLM response → parse_tool_calls() (JSON or XML format)
        → has tool calls?
          YES → execute_all() via ToolRegistry → inject results → loop
          NO  → extract JSON → return final answer
  → post-condition check → return AgentResult
```

- **Tool parsing**: Supports `{"tool_calls": [...]}` JSON format AND `<tool_call name="..." args='...' />` XML format.
- **Safety guard**: `MAX_TOOL_ITERATIONS = 5` prevents infinite loops.
- **Role-based tool access**: `ToolRegistry.get_for_role(role)` filters tools by `allowed_roles`.
- **Prompt injection**: `build_tool_definitions(role)` auto-injects available tools into the system prompt.

### 5. Multi-LLM Provider (ModelRouter)
- `OpenAICompatibleProvider` handles all OpenAI-compatible APIs (智谱 GLM, Kimi, 阿里 Qwen, OpenAI) via `openai` SDK with different `base_url`.
- `ClaudeCLIRunner` for local `claude --print` CLI (fallback, no API key needed).
- **Fallback chain**: `zhipu → kimi → dashscope → claude_cli` — try in order, skip unavailable, stop on first success.
- **No liteLLM**: Build own `OpenAICompatibleProvider` instead — lighter, more controllable.

### 6. Agent Documentation (AGENT.md + soul.md)
Each agent directory contains:
- **`AGENT.md`**: Contract-facing spec — role, purpose, model strategy, tools, output contract, guidelines (MUST/MUST_NOT), escalation conditions.
- **`soul.md`**: Identity document — philosophical identity, values, workflow, boundaries. Written in first person. Defines "what makes me this agent" and "what I will never do".

## Design Rules

-   **CLAUDE.md Compliance**: Before starting any phase, audit `CLAUDE.md` and ensure all actions conform to the project constitution.
-   **Task-Level Commits**: Commit immediately after task completion. Message format: `<type>(<scope>): <description>`. Never `git add .`.
-   **Documentation**: Log design decisions in `DESIGN_LOG.md` and `ADR-NNN.md`.
-   **Pluggability**: Use abstract base classes for storage and external integrations.
    -   See: [Knowledge Base Pattern](references/knowledge-base-pattern.md).

## Reference Files

- **[Knowledge Base Pattern](references/knowledge-base-pattern.md)**: Detailed implementation of Repository Pattern + Spec Enforcement.
- **[E2E Testing Patterns](references/e2e-testing-patterns.md)**: Agent contract preconditions cheat sheet, mock LLM patterns, common pitfalls (type mismatches, hook enums, pipeline completion behavior, trace isolation).
- **[Tool Authoring Pattern](references/tool-authoring-pattern.md)**: How to create new tools for the agent system (ToolHandler pattern, project management integration, local-first fallback).
- **[ai_collection Structure](references/ai-collection-structure.md)**: Canonical project layout for skill/agent package collections.

## Pitfalls

-   **Mixing Memory Types**: Do not store transient runtime state (like task progress) in the persistent Knowledge Base.
-   **Ignoring Specs**: If a Spec exists, the implementation *must* follow it. If the Spec is wrong, update the Spec first.
-   **Silent Failures**: The Orchestrator must explicitly handle failures (e.g., write to `memory/blocked/`) rather than ignoring them.
-   **E2E Test Context Requirements**: Each agent role has strict contract preconditions — research needs `query` + `available_sources`, planning needs `vision` (string) + `research_refs` (list), build needs `plan` (dict) + `task_id`, eval needs `spec_path` + `target_output`. See [references/e2e-testing-patterns.md](references/e2e-testing-patterns.md) for full cheat sheet and common pitfalls (hook enums are lowercase, PipelineExecutor may complete even when all steps fail, TraceCollector uses `.super_factory/data/traces` by default).

## Tool Authoring Pattern

All tools in `super_factory/tools/` must follow the `ToolHandler` class pattern:

```python
from tools.base import ToolHandler, ToolResult
from tools.registry import tool

@tool(
    "tool_name",
    "Brief description of what the tool does",
    allowed_roles={"research", "planning", "build", "eval", "orchestrator"},
    parameters_schema={
        "type": "object",
        "properties": {
            "param1": {"type": "string", "description": "..." },
        },
        "required": ["param1"],
    },
)
class MyToolHandler(ToolHandler):
    def execute(self, params: dict[str, Any]) -> ToolResult:
        # Implementation
        return ToolResult(success=True, data={...})
```

**Critical rules:**
- Tools MUST be classes inheriting from `ToolHandler`, NOT standalone functions
- The `@tool` decorator auto-registers the tool in the global registry
- `allowed_roles` controls which agents can access the tool
- Return `ToolResult(success=True/False, data=.../error=...)`

## Project Management Integration

When adding new capabilities (tools) to the agent system:

1. **Create the tool** in `tools/<name>.py` following the `ToolHandler` pattern
2. **Update `prompt_builder.py`** to inject tool instructions into system prompts
3. **Update all `AGENT.md` files** (`agents/*/AGENT.md`) to document the new tool and workflow
4. **Initialize data** (e.g., `.projects/tasks.json`) if the tool requires state
5. **Test**: Verify tool registration and run full test suite

### Local-First Fallback Pattern

When external services (GitHub API, etc.) require auth that can't be automated:
- Implement local storage first (JSON files in `.projects/`)
- Provide a sync function that attempts external API and gracefully falls back
- Agents use local tools immediately; sync happens when auth is granted
- Document the auth requirement as a "Blocked" task in the project system

See: [Tool Authoring Pattern](references/tool-authoring-pattern.md)
-   **`.gitignore` build/ rule**: A `build/` entry in `.gitignore` will match `agents/build/` — use `git add -f` to force-add files in agent subdirectories.
-   **opencode run unreliable for delegation**: `opencode run` with kimi-k2.5 hung for 3+ hours with zero output on super_factory tasks. When opencode fails, write code directly — it's faster and more reliable.
-   **Orchestrator ClaudeRunner replacement**: When replacing `ClaudeRunner` with `ModelRouter`, existing tests that mock `orchestrator.base.ClaudeRunner.run` must be updated to mock `agents.core.llm_provider.ModelRouter.chat`. Also update `call_args[0][0]` → `call_args.kwargs.get('messages', [])` since the new API uses keyword args.
-   **Pre-condition check location**: `Orchestrator.execute_agent()` must include its own pre-condition check (in addition to `BaseAgent.execute()`), because the orchestrator is called directly by the pipeline executor and may bypass the agent's execute method.
-   **Agent soul.md structure**: Each agent's soul.md should be written in first person, defining: Identity, What Makes Me [Role], My Values (with quotes), My Workflow (ASCII diagram), My Boundaries (with ✅/❌ list).