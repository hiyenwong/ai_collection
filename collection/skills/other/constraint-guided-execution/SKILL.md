---
name: constraint-guided-execution
description: "Constraint-guided execution pattern for interpreting natural language plans. Extracted from 'RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution' (arXiv 2026-05-05). Applicable to agent task planning, workflow automation, and any system that needs to execute plans under constraints."
category: "agent-patterns"
---

# Constraint-Guided Execution

## Description
A pattern for converting natural language plans into executable actions while respecting hard and soft constraints. The system parses plans into structured instructions, extracts constraint conditions (time, resources, dependencies, ordering), and executes within a constraint satisfaction framework that dynamically adapts when constraints change.

## Activation Keywords
- constraint-guided execution
- natural language plan execution
- plan interpretation
- 约束引导执行
- 自然语言计划执行
- agent task planning
- constrained workflow

## Core Pattern

### Step 1: Parse Natural Language Plan
```
Input: "First deploy the database migration, then run the data validation, 
        but only if the migration succeeds. If validation fails, rollback."

Parsed:
- Actions: [deploy_migration, run_validation, rollback]
- Dependencies: validation -> migration (success)
- Conditions: rollback IF validation_fail
- Constraints: ordering (migration before validation)
```

### Step 2: Extract Constraints
Identify constraint types:
- **Ordering constraints**: Action A must happen before Action B
- **Conditional constraints**: Action B only if condition C is met
- **Resource constraints**: Action A requires resource R
- **Time constraints**: Action A must complete within time T
- **Success/failure constraints**: On failure of A, do B

### Step 3: Build Execution Graph
```
graph = DependencyGraph()
for action in parsed_plan.actions:
    graph.add_node(action)
for dep in parsed_plan.dependencies:
    graph.add_edge(dep.from_action, dep.to_action, condition=dep.condition)
```

### Step 4: Execute with Constraint Checking
```
def execute_plan(graph):
    ready = graph.get_ready_actions()  # no unmet dependencies
    results = {}
    while ready:
        action = ready.pop()
        if not check_constraints(action, results):
            continue  # skip, constraints not met
        result = execute(action)
        results[action] = result
        # trigger conditional actions
        for dependent in graph.get_dependents(action):
            if dependent.condition.evaluate(result):
                ready.add(dependent)
        # trigger fallback actions on failure
        if result.failed:
            for fallback in graph.get_fallbacks(action):
                ready.add(fallback)
    return results
```

### Step 5: Dynamic Adaptation
When constraints change during execution:
- **Resource unavailable**: Re-plan with alternative resources
- **Timeout**: Skip or defer the action
- **New dependency discovered**: Add to graph, re-evaluate readiness
- **Action fails**: Execute fallback path, notify upstream

## Implementation Example

```python
class ConstraintGuidedExecutor:
    def __init__(self, plan_text):
        self.actions = self.parse_actions(plan_text)
        self.constraints = self.extract_constraints(plan_text)
        self.graph = self.build_execution_graph()
        self.results = {}
    
    def execute(self):
        while self.graph.has_pending():
            ready = self.graph.get_ready(self.results)
            for action in ready:
                if self.check_preconditions(action):
                    result = self.run_action(action)
                    self.results[action] = result
                    self.handle_result(action, result)
        return self.results
    
    def handle_result(self, action, result):
        if result.success:
            self.enable_dependents(action)
        else:
            self.trigger_fallbacks(action)
            self.notify_upstream(action, result.error)
```

## Best Practices

1. **Fail fast**: Detect constraint violations before execution, not during
2. **Provide rollback**: Every destructive action should have a defined rollback path
3. **Log execution trace**: Record which actions ran, in what order, with what results
4. **Support partial execution**: If some actions fail, continue with independent actions
5. **Make constraints explicit**: Don't hide constraints in action logic; declare them upfront

## Error Handling

| Scenario | Response |
|----------|----------|
| Circular dependency detected | Reject plan, report cycle to user |
| Constraint conflict | Report conflicting constraints, ask for resolution |
| Action timeout | Mark as failed, trigger fallback if defined |
| Resource exhausted | Queue action, retry when resource available |
| Unknown action | Return error with available action suggestions |

## Related Patterns

- **Validation-Driven LLM Workflow**: Validate plan correctness before execution
- **Test-Driven Development**: Write constraints as tests before implementing actions
- **State Machine**: Model execution states explicitly for complex workflows

## Resources

- Source paper: "RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution" (arXiv 2026-05-05)
- Related: "Generating Statistical Charts with Validation-Driven LLM Workflows"
