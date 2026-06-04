# Tool Authoring Pattern for super_factory

## ToolHandler Class Pattern

Every tool in `super_factory/tools/` must be a class inheriting from `ToolHandler`:

```python
from __future__ import annotations

from typing import Any

from tools.base import ToolHandler, ToolResult
from tools.registry import tool

@tool(
    "tool_name",                              # Unique tool name (snake_case)
    "Brief description of what the tool does", # Shown in agent prompts
    allowed_roles={"research", "build"},       # Which agent roles can use it
    is_dangerous=False,                        # True for file_write, shell_exec
    parameters_schema={                        # JSON Schema for validation
        "type": "object",
        "properties": {
            "param1": {"type": "string", "description": "First parameter"},
            "param2": {"type": "integer", "description": "Second parameter", "default": 0},
        },
        "required": ["param1"],
    },
)
class MyToolHandler(ToolHandler):
    """Implementation of the tool_name tool."""

    def execute(self, params: dict[str, Any]) -> ToolResult:
        param1 = params.get("param1", "")
        if not param1:
            return ToolResult(success=False, error="param1 is required")

        # ... implementation ...

        return ToolResult(success=True, data={"result": "value"})
```

## Common Mistakes

### ❌ Don't: Use standalone functions

```python
# WRONG - This won't be registered
def my_tool(param1: str) -> str:
    return f"Result: {param1}"
```

### ❌ Don't: Forget to import ToolHandler

```python
# WRONG - Will fail at runtime
@tool("name", "desc")
class MyTool:  # Missing ToolHandler inheritance
    def execute(self, params): ...
```

### ✅ Do: Return ToolResult with proper structure

```python
return ToolResult(success=True, data={"key": "value"})  # Success
return ToolResult(success=False, error="Something went wrong")  # Failure
```

## Adding New Tools to the Agent System

When creating a new tool, follow this checklist:

### 1. Create the Tool File

```bash
# tools/my_tool.py
from tools.base import ToolHandler, ToolResult
from tools.registry import tool

@tool(...)
class MyToolHandler(ToolHandler):
    def execute(self, params): ...
```

### 2. Update prompt_builder.py

Add instructions for using the tool in `TOOL_USE_INSTRUCTIONS`:

```python
TOOL_USE_INSTRUCTIONS = """
...
## My Tool Category
Use `my_tool` when you need to...
"""
```

### 3. Update All AGENT.md Files

For each agent that should use the tool, add to `agents/<role>/AGENT.md`:

```markdown
## Tools

| Tool | 用途 |
|------|------|
| `my_tool` | Description of what it does |

### Workflow
1. When to use the tool
2. Expected output
3. Error handling
```

### 4. Initialize State (if needed)

If the tool requires persistent state:

```bash
mkdir -p .my_tool/
echo '{"initialized": true}' > .my_tool/state.json
```

### 5. Test Registration

```python
import tools.file_ops  # Import to trigger registration
import tools.my_tool

from tools.registry import get_registry

registry = get_registry()
tool_def = registry.get("my_tool")
assert tool_def is not None, "Tool not registered!"
```

### 6. Run Full Test Suite

```bash
cd ~/ai_github/super_factory && python -m pytest tests/ -q
```

## Project Management Tool Example

The `tools/project_manager.py` demonstrates a complete implementation with:
- 5 tools (create, query, update, list, sync)
- Local JSON storage in `.projects/tasks.json`
- GitHub sync with graceful fallback
- All agents can access project tools

## Local-First Fallback Pattern

When external APIs require interactive auth:

```python
def sync_to_external() -> ToolResult:
    # 1. Try external API
    try:
        result = call_external_api()
        if "INSUFFICIENT_SCOPES" in result:
            return ToolResult(
                success=False,
                error="Auth required. Run: `gh auth refresh --scopes 'project'`"
            )
        return ToolResult(success=True, data={"synced": True})
    except Exception:
        # 2. Fall back to local storage
        return ToolResult(
            success=True,
            data={"message": "Saved locally. Sync when auth is granted."}
        )
```

This pattern ensures agents can work immediately while external integration is pending.
