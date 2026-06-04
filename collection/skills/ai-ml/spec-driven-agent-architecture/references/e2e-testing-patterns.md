# E2E Integration Testing Patterns for Contract-Driven Agent Systems

## Context
When testing multi-agent pipeline systems (Spec → Contract → Agent → Eval), each agent role has strict contract preconditions that must be satisfied in the test context before LLM execution begins.

## Agent Contract Preconditions Cheat Sheet

| Agent | Required Context Fields | Notes |
|---|---|---|
| **research** | `query` (non-empty string), `available_sources` (list), `knowledge_sources_consulted` (list) | Blocks on empty query |
| **planning** | `vision` (non-empty string), AND (`research_refs` as list OR `knowledge_sources` as list) | Vision is a string, research_refs must be a list |
| **build** | `plan` (non-empty dict), `task_id` (non-empty string) | plan_tasks optional (only checked if present) |
| **eval** | `spec_path` (non-empty string), `target_output` (not None) | spec_path is a filepath string |

## Common Pitfalls

### 1. Type Mismatch in Mock Context
- `research_refs` must be a `list` (not a string). Passing a string causes `len(refs) > 0` check to pass (since len of string > 0) but the contract logic may still fail downstream.
- `plan` must be a `dict` (not a list). The contract checks `bool(plan)`.
- `vision` must be a non-empty string. Empty string or None fails precondition.

### 2. Hook Enum Values Are Lowercase
HookPoint enum values are lowercase strings like `pipeline_start`, `agent_post_execute`, `pipeline_end`. Do not assert on uppercase `PIPELINE_START`.

### 3. PipelineExecutor Doesn't Always Stop on First Failure
The PipelineExecutor continues processing independent steps. When all steps fail with the same error (e.g., LLM unavailable), the pipeline may still report `status == "completed"` if the execution flow completes without raising `PipelineExecutionError`. Test for per-step `step_results[step].status == "failed"` instead of only checking pipeline state.

### 4. TraceCollector Uses Default Directory
The Orchestrator's TraceCollector defaults to `.super_factory/data/traces`. In tests, replace with a `tmp_path` directory to isolate test artifacts.

### 5. Memory Store Files Should Be Gitignored
Runtime memory store files (`memory/store/*.json`) change every execution and should be in `.gitignore`. The `_index.json` is also a runtime file and should be ignored.

## Test Structure Pattern

```python
class TestFullPipelineEndToEnd:
    """Test complete Research → Planning → Build → Eval chain."""
    
    def test_happy_path(self, orchestrator):
        # Each agent executed through real Orchestrator with mocked LLM
        # Verify contract preconditions, postconditions, context passing
        pass

class TestPipelineExecutorIntegration:
    """Test PipelineExecutor with real Orchestrator."""
    
    def test_default_pipeline_execution(self, orchestrator):
        # Full DAG execution via PipelineExecutor.run()
        pass

class TestHookLifecycleE2E:
    """Verify hook events fire at correct lifecycle points."""
    pass

class TestTraceCollectionEndToEnd:
    """Verify trace persistence to disk."""
    pass
```

## Mock LLM Response Pattern

```python
def mock_chat(messages, model_hint=None):
    """Route mock responses based on call order."""
    responses = [RESEARCH_JSON, PLANNING_JSON, BUILD_JSON, EVAL_JSON]
    idx = call_counter["n"]
    call_counter["n"] += 1
    return responses[idx % len(responses)]
```

Each mock response must satisfy the corresponding agent's contract postconditions (e.g., research needs ≥3 sources with url/path, build needs tests_passed=True, coverage ≥0.8, etc.).
