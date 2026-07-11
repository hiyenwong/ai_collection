---
name: agent-integration-testing
description: "Integration testing patterns for autonomous agent frameworks — mocking LLM routers, verifying tool-use loops, contract validation, and fallback chains. Applies to super_factory and similar spec-driven agent architectures."
trigger: "Writing or extending tests for agent code that uses LLM routing, tool-use loops, or contract validation."
---

## Scope

Integration tests for agent systems that sit **between** unit tests (mocked routers) and E2E tests (real pipelines). Focus is on verifying `BaseAgent`/`GenericAgent` correctly integrate with `ModelRouter`, handle tool-use loops, and enforce contract pre/post conditions.

## Test Structure

Organize into 7 sections:

1. **ModelRouter Injection** — router=None acceptance, mock injection, call argument verification, real router construction
2. **Model Hint Pass-Through** — verify `_get_model_hint()` correctly forwards model config to router (not hardcoded)
3. **Tool-Use Loop** — no-tool-call direct answer, one-turn tool+answer, multi-turn chains (3+), error injection, max iterations
4. **GenericAgent** — role property, mock router execution, subclass override hooks
5. **Fallback Chain** — single provider failure, all-provider failure
6. **Contract Validation** — precondition blocks, postcondition fails, **both pass happy path**
7. **Edge Cases** — router=None graceful failure, nested JSON extraction depth limits, tool execution exception injection

## Patterns

### Mock Router Setup

```python
mock_router = MagicMock()
mock_router.chat.return_value = '{"result": "ok"}'
# or side_effect for multi-turn:
mock_router.chat.side_effect = [tool_call_response, final_answer]
```

### Verifying Message Structure

```python
call_args = mock_router.chat.call_args
messages = call_args.kwargs.get("messages")  # kwargs, NOT args
assert messages[0]["role"] == "system"
assert messages[1]["role"] == "user"
```

### Tool-Use Loop Verification

```python
# After 2 turns, verify tool results were injected:
second_msgs = mock_router.chat.call_args_list[1].kwargs.get("messages")
assert len(second_msgs) == 4  # system + user + assistant + user(results)
assert second_msgs[2]["role"] == "assistant"
assert "Tool Execution Results" in second_msgs[3]["content"]
```

### Contract Validation Mocking

```python
mock_contract = MagicMock()
agent._contract_validator.validate = mock_validate
agent._load_contract = lambda: mock_contract
```

## Pitfalls

### Pitfall 1 — call_args.args vs call_args.kwargs

The router's `chat()` method is called with keyword arguments (`messages=...`), not positional args. Using `call_args.args[0]` raises `IndexError`. Always use `call_args.kwargs.get("messages")`.

### Pitfall 2 — Max iterations returns "success" for parseable JSON

When `MAX_TOOL_ITERATIONS` is reached, `_tool_use_loop` tries `_extract_json()` on the last raw output. If it parses as JSON (even if it is a `tool_calls` structure), the result is `"success"`. It only returns `"failed"` when the output is genuinely unparseable. Test assertions must match this behavior.

### Pitfall 3 — Tool registry must be loaded

Integration tests that exercise tool execution must import tool modules (`import tools.file_ops`, etc.) at the top so `@tool` decorators register themselves. Without this, all tool calls return "Tool not found".

### Pitfall 4 — AgentContext requires config

The `AgentContext` constructor requires a `config=AgentExecConfig()` parameter. Omitting it causes subtle failures.

### Pitfall 5 — `_get_model_hint()` must not be hardcoded

A common bug: `_get_model_hint(model)` has two branches but both return `"default"`, making the `model` parameter dead code. The fix is `return model if model else "default"`. Always test this with `model="kimi-k2.5"` in `AgentExecConfig` and assert the router receives `model_hint="kimi-k2.5"`.

### Pitfall 6 — `ToolResult.data` vs `result.output`

`tools/base.py` defines `ToolResult` with fields `success`, `data`, and `error`. Code that references `result.output` will raise `AttributeError` at runtime. Always use `result.data` when mapping `ToolResult` to `ToolCallResult`.

### Pitfall 7 — Patch `execute_all` at `agents.base`, not `agents.core.tool_executor`

When mocking `execute_all` in integration tests, the import path matters. `base.py` does `from agents.core.tool_executor import execute_all`, so the patch target must be `agents.base.execute_all`, not `agents.core.tool_executor.execute_all`.

### Pitfall 8 — Nested JSON extraction max_depth=3

`_extract_json` handles double/triple-encoded JSON strings via recursive `try_parse` with `max_depth=3`. Double-encoded (1 reparse) and triple-encoded (2 reparses) succeed. Quadruple (3) is at the boundary. Quintuple (4) exceeds the limit. Test assertions must count depth correctly: `depth > max_depth` raises.

## Verification
## Verification

Run the integration test file plus existing tests together:
```bash
cd /path/to/super_factory
python -m pytest tests/test_base_agent_integration.py tests/test_base_agent.py tests/test_orchestrator.py -v --tb=short
```

All integration tests should pass. Existing test failures in unrelated modules (e.g., `test_llm_provider.py` with stale config assertions) are not integration test failures.

## Known Bugs Reference

See `references/base-agent-bugs-found.md` for documented bugs discovered during test expansion, including `_get_model_hint()` dead code, `ToolResult.output` vs `.data` field mismatch, and `router=None` crash design gap.
