# Bugs Found During BaseAgent Integration Test Expansion

## Bug 1: `_get_model_hint()` Dead Code

**File:** `agents/base.py`, line 167-170

```python
def _get_model_hint(self, model: str | None) -> str:
    if model:
        return "default"
    return "default"  # both branches return the same value
```

**Impact:** The `model` parameter from `context.config` is completely ignored. All LLM calls route with hint `"default"` regardless of user config.

**Fix:**
```python
def _get_model_hint(self, model: str | None) -> str:
    return model if model else "default"
```

## Bug 2: `ToolResult.output` → `ToolResult.data`

**File:** `agents/core/tool_executor.py`, line 80

```python
output=json.dumps(result.output, ensure_ascii=False) if result.output else "",
```

`ToolResult` (defined in `tools/base.py`) has fields: `success`, `data`, `error`. There is no `output` field.

**Impact:** Any real tool execution that returns data will raise `AttributeError: 'ToolResult' object has no attribute 'output'`, causing the tool-use loop to inject an exception message instead of actual tool output.

**Fix:**
```python
output=json.dumps(result.data, ensure_ascii=False) if result.data else "",
```

## Bug 3: `router=None` Crash (Design Gap)

**File:** `agents/base.py`, line 131

```python
raw_output = self._router.chat(...)  # AttributeError if router is None
```

**Impact:** If `BaseAgent` is constructed with `router=None` (which the constructor allows) and `execute()` is called, it crashes with `AttributeError: 'NoneType' object has no attribute 'chat'`. The outer try/except catches this but returns a generic error message.

**Status:** Not yet fixed. The current behavior (captured as "failed" status) is acceptable for now, but a cleaner approach would validate router presence in `__init__` or `execute()` early.
