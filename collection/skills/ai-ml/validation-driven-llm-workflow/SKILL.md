---
name: validation-driven-llm-workflow
description: "Validation-driven LLM workflow pattern - using verification loops to ensure LLM-generated outputs are correct. Extracted from 'Generating Statistical Charts with Validation-Driven LLM Workflows' (arXiv 2026-05-01). Applicable to code generation, data visualization, document generation, and any task requiring correctness guarantees."
category: "llm-patterns"
---

# Validation-Driven LLM Workflow

## Description
A reusable pattern for ensuring LLM-generated outputs meet correctness criteria through iterative verification loops. Instead of trusting LLM output directly, this pattern wraps generation in a validate-regenerate cycle until the output passes verification or reaches a maximum iteration limit.

## Activation Keywords
- validation-driven workflow
- verify LLM output
- LLM validation loop
- 验证驱动工作流
- LLM 验证循环
- generate with verification
- self-correcting generation

## Core Pattern

### Step 1: Define Validation Criteria
Before generation, establish clear, measurable validation criteria:
- **Syntax checks**: Code compiles, JSON parses, etc.
- **Semantic checks**: Output matches expected format, contains required fields
- **Execution checks**: Generated code runs without errors, produces expected results
- **Domain checks**: Statistical chart has correct axis labels, data matches source

### Step 2: Generate Initial Output
```
prompt = "Generate {task_description}"
output = llm.generate(prompt)
```

### Step 3: Validate Output
```
validation_result = validator.check(output)
if validation_result.passed:
    return output
else:
    feedback = validation_result.feedback
```

### Step 4: Regenerate with Feedback
```
improved_prompt = f"{original_prompt}\n\nPrevious attempt failed: {feedback}\nPlease fix these issues and regenerate."
output = llm.generate(improved_prompt)
```

### Step 5: Iterate with Limits
```
max_iterations = 3
for i in range(max_iterations):
    output = generate()
    result = validate(output)
    if result.passed:
        return output
    output = regenerate_with_feedback(result.feedback)
return best_output_so_far  # fallback
```

## Implementation Examples

### Code Generation
```python
def generate_validated_code(spec, max_retries=3):
    code = llm.generate(f"Write Python code: {spec}")
    for _ in range(max_retries):
        errors = run_syntax_check(code)
        if not errors:
            errors = run_unit_tests(code)
        if not errors:
            return code
        code = llm.generate(f"Fix these errors in the code:\n{errors}\n\nCode:\n{code}")
    return code
```

### Data Visualization
```python
def generate_validated_chart(data, chart_type, max_retries=3):
    spec = llm.generate(f"Create {chart_type} spec for this data: {data}")
    for _ in range(max_retries):
        chart = render_chart(spec, data)
        errors = validate_chart(chart)  # check axes, labels, data integrity
        if not errors:
            return chart
        spec = llm.generate(f"Fix chart issues: {errors}\n\nCurrent spec: {spec}")
    return chart
```

## Best Practices

1. **Make validators deterministic**: Use programmatic checks, not LLM-based validation (avoid LLM verifying LLM)
2. **Provide specific feedback**: Vague "this is wrong" feedback doesn't help; specify what failed and why
3. **Set reasonable iteration limits**: 3-5 retries is usually enough; more indicates a fundamental prompt issue
4. **Cache successful patterns**: When validation passes, save the prompt-output pair for future reference
5. **Graceful degradation**: Always return the best attempt, not just success/failure

## Error Handling

| Error | Recovery |
|-------|----------|
| Validator always fails | Review validation criteria - may be too strict or wrong |
| LLM produces same error repeatedly | Change the approach, not just the prompt |
| Timeout on validation | Set timeout limits for execution-based validators |
| Infinite regeneration loop | Hard cap iterations, return best result |

## Related Patterns

- **Constraint-Guided Execution**: Add constraints to the validation criteria
- **Self-Verification**: LLM verifies its own output (less reliable than external validators)
- **Test-Driven Development**: Write tests first, then generate code to pass them

## Resources

- Source paper: "Generating Statistical Charts with Validation-Driven LLM Workflows" (arXiv 2026-05-01)
- Related: "RunAgent: Interpreting Natural-Language Plans with Constraint-Guided Execution"
