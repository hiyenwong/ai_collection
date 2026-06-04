---
name: prompt-optimization
description: "Universal prompt optimization skill that applies systematic techniques to improve prompt quality, clarity, and effectiveness for any AI agent."
---

# Prompt Optimization

## Description
A universal skill for optimizing prompts through systematic analysis, iterative refinement, and evidence-based improvement. Applicable to all agents and task types.

## Activation Keywords
- prompt optimization
- optimize prompt
- improve prompt
- prompt refinement
- prompt tuning
- prompt enhancement
- 优化 prompt

## Recommended Model
- **sonnet4.5** (Recommended for balanced reasoning and speed)
- **opus4.5** (For complex multi-step optimization)

## Tools Used
- exec: Run prompt tests and evaluations
- read: Analyze existing prompts and context
- write: Create optimized prompts and documentation

## Usage Patterns

### General Optimization
```
优化这个 prompt: [your prompt]
```

### Specific Technique Application
```
使用 [CoT/ToT/Few-shot] 优化这个 prompt
```

### Targeted Optimization
```
优化这个 prompt 以提高 [accuracy/consistency/clarity]
```

## Instructions for Agents

### Overview

Prompt optimization follows a systematic workflow:

```
┌─────────────────────────────────────────────────────────┐
│            Prompt Optimization Workflow                   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   ┌─────────────────┐       ┌─────────────────┐         │
│   │   Analyze       │──────▶│   Diagnose      │         │
│   │   (分析现状)     │       │   (诊断问题)    │         │
│   └─────────────────┘       └─────────────────┘         │
│          │                          │                    │
│          ▼                          ▼                    │
│   ┌─────────────────┐       ┌─────────────────┐         │
│   │   Refine        │──────▶│   Test          │         │
│   │   (优化改进)     │       │   (测试验证)    │         │
│   └─────────────────┘       └─────────────────┘         │
│          │                          │                    │
│          └──────────┬───────────────┘                    │
│                     ▼                                    │
│   ┌─────────────────────────────────────────────┐       │
│   │              Iterate & Document              │       │
│   │           (迭代并记录结果)                    │       │
│   └─────────────────────────────────────────────┘       │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Step 1: Analyze Current Prompt

**Goal:** Understand the prompt's current state and context

**Analysis Checklist:**

1. **Intent Clarity**
   ```markdown
   - What is the main task?
   - Is the objective clear?
   - Are there ambiguities?
   - Could it be misunderstood?
   ```

2. **Structure Assessment**
   ```markdown
   - Is the prompt well-organized?
   - Are instructions logically ordered?
   - Is there unnecessary complexity?
   - Is the output format specified?
   ```

3. **Content Evaluation**
   ```markdown
   - Are there examples?
   - Are constraints specified?
   - Is the context sufficient?
   - Are edge cases addressed?
   ```

4. **Performance Issues**
   ```markdown
   - Known failure modes
   - Inconsistency problems
   - Quality issues
   - Hallucination risk
   ```

### Step 2: Diagnose Problems

**Common Issues & Solutions:**

| Issue | Symptoms | Solution |
|-------|----------|----------|
| Unclear Intent | Off-topic outputs | Add explicit task statement |
| Missing Context | Inconsistent outputs | Add background information |
| No Examples | Variable quality | Add few-shot examples |
| Vague Constraints | Hallucination | Add explicit boundaries |
| No Output Format | Unstructured output | Specify exact format |
| Complex Task | Incomplete outputs | Break into steps |

**Diagnosis Process:**

```python
def diagnose_prompt(prompt, test_results):
    """Identify specific issues with a prompt."""
    issues = []
    
    # Check clarity
    if has_ambiguous_terms(prompt):
        issues.append({
            'type': 'clarity',
            'severity': 'high',
            'description': 'Ambiguous terms detected',
            'recommendation': 'Replace with specific terms'
        })
    
    # Check structure
    if not has_clear_structure(prompt):
        issues.append({
            'type': 'structure',
            'severity': 'medium',
            'description': 'Poor organization',
            'recommendation': 'Reorganize with clear sections'
        })
    
    # Check examples
    if not has_examples(prompt) and task_is_complex(prompt):
        issues.append({
            'type': 'examples',
            'severity': 'high',
            'description': 'No examples for complex task',
            'recommendation': 'Add 2-3 representative examples'
        })
    
    # Check constraints
    if has_hallucination_risk(prompt):
        issues.append({
            'type': 'constraints',
            'severity': 'critical',
            'description': 'Risk of hallucination',
            'recommendation': 'Add fact-checking constraints'
        })
    
    return issues
```

### Step 3: Apply Optimization Techniques

**Technique Selection Guide:**

```
Task Type                    → Recommended Technique
─────────────────────────────────────────────────────
Complex Reasoning           → Chain-of-Thought (CoT)
Multi-step Problems         → Decomposition
Decision Making             → Tree-of-Thought (ToT)
Pattern Matching            → Few-shot Examples
Quality Sensitive           → Self-Consistency
Error-Prone Tasks           → Verification Steps
Creative Tasks              → Style Guidelines
```

#### Technique 1: Chain-of-Thought (CoT)

**When to use:** Complex reasoning, math, logic problems

**Template:**
```
Let's think step by step:

1. [First step]
   - Analysis: ...
   - Reasoning: ...

2. [Second step]
   - Analysis: ...
   - Reasoning: ...

...

Therefore, the answer is: [Conclusion]
```

**Example Application:**

Before:
```
Solve: If John has 5 apples and gives 2 to Mary, then buys 3 more, how many does he have?
```

After:
```
Solve: If John has 5 apples and gives 2 to Mary, then buys 3 more, how many does he have?

Let's think step by step:

1. Initial state: John has 5 apples
2. First action: John gives 2 apples to Mary
   - Remaining: 5 - 2 = 3 apples
3. Second action: John buys 3 more apples
   - New total: 3 + 3 = 6 apples

Therefore, John now has 6 apples.
```

#### Technique 2: Few-Shot Learning

**When to use:** Pattern-based tasks, format-sensitive outputs

**Template:**
```
Task: [Task description]

Examples:
1. Input: [Example 1]
   Output: [Output 1]

2. Input: [Example 2]
   Output: [Output 2]

3. Input: [Example 3]
   Output: [Output 3]

Now solve:
Input: [New input]
Output:
```

**Example Application:**

Before:
```
Translate these sentences to formal English.
```

After:
```
Translate these sentences to formal English.

Examples:
1. Input: "can you help me?"
   Output: "Could you please assist me?"

2. Input: "I want to know"
   Output: "I would like to inquire"

3. Input: "it's not good"
   Output: "This is unsatisfactory"

Now translate:
Input: "you need to fix this"
Output:
```

#### Technique 3: Tree-of-Thought (ToT)

**When to use:** Decision making, multi-path reasoning

**Template:**
```
Let's explore multiple approaches:

Approach 1: [First approach]
- Considerations: ...
- Advantages: ...
- Disadvantages: ...
- Success probability: X%

Approach 2: [Second approach]
- Considerations: ...
- Advantages: ...
- Disadvantages: ...
- Success probability: X%

...

Best approach: [Selected approach]
Reasoning: [Why this is optimal]
```

#### Technique 4: Self-Consistency

**When to use:** High-stakes accuracy, validation needed

**Template:**
```
Generate 3 different solutions:

Solution A:
[First approach]

Solution B:
[Second approach]

Solution C:
[Third approach]

Analysis:
- Common elements: ...
- Differences: ...
- Most consistent: ...

Final answer: [Most reliable solution]
```

#### Technique 5: Structured Output

**When to use:** Format-specific requirements

**Template:**
```
Task: [Description]

Output format:
```
[Field 1]: [Description]
[Field 2]: [Description]
[Field 3]: [Description]
```

Constraints:
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]
```

### Step 4: Test & Validate

**Testing Framework:**

```python
def test_optimized_prompt(prompt, test_cases):
    """Test optimized prompt with diverse inputs."""
    results = {
        'passed': 0,
        'failed': 0,
        'issues': []
    }
    
    for test in test_cases:
        output = run_prompt(prompt, test.input)
        
        # Evaluate output
        evaluation = evaluate_output(
            output,
            test.expected,
            criteria=['accuracy', 'completeness', 'format']
        )
        
        if evaluation.passes_threshold(threshold=0.8):
            results['passed'] += 1
        else:
            results['failed'] += 1
            results['issues'].append({
                'input': test.input,
                'output': output,
                'expected': test.expected,
                'evaluation': evaluation
            })
    
    return {
        'success_rate': results['passed'] / len(test_cases),
        'details': results
    }
```

**Test Case Design:**

```markdown
## Test Cases for Prompt Optimization

### Normal Cases
- Typical inputs
- Expected behavior
- Standard complexity

### Edge Cases
- Boundary conditions
- Unusual inputs
- Missing information

### Failure Cases
- Known problematic inputs
- Ambiguous requests
- Conflicting constraints

### Stress Cases
- Long inputs
- Complex requirements
- Multiple constraints
```

### Step 5: Iterate & Document

**Iteration Process:**

1. **Compare Results**
   ```markdown
   Version 1 → Version 2 Changes:
   - Added: [What was added]
   - Modified: [What was changed]
   - Removed: [What was removed]
   
   Performance Impact:
   - Accuracy: 75% → 85% (+10%)
   - Consistency: 70% → 90% (+20%)
   - Format Compliance: 80% → 95% (+15%)
   ```

2. **Document Learnings**
   ```markdown
   ## Optimization Log
   
   ### Date: [Date]
   ### Prompt: [Prompt name/version]
   
   Issues Identified:
   - [Issue 1]
   - [Issue 2]
   
   Solutions Applied:
   - [Solution 1] → Result: [Outcome]
   - [Solution 2] → Result: [Outcome]
   
   Key Learnings:
   - [Learning 1]
   - [Learning 2]
   ```

3. **Track Versions**
   ```python
   class PromptVersion:
       def __init__(self, prompt, version, changes, metrics):
           self.prompt = prompt
           self.version = version
           self.changes = changes
           self.metrics = metrics
           self.timestamp = datetime.now()
       
       def is_better_than(self, other_version):
           return self.metrics['overall'] > other_version.metrics['overall']
   ```

## Optimization Checklist

### Before Optimization
- [ ] Understand the task and success criteria
- [ ] Identify known issues and failure modes
- [ ] Gather test cases
- [ ] Set baseline metrics

### During Optimization
- [ ] Apply appropriate technique(s)
- [ ] Test with diverse inputs
- [ ] Measure performance
- [ ] Document changes

### After Optimization
- [ ] Compare against baseline
- [ ] Document learnings
- [ ] Archive previous versions
- [ ] Plan for future iterations

## Common Optimization Patterns

### Pattern 1: Clarity Enhancement

```python
def enhance_clarity(prompt):
    """Improve prompt clarity."""
    # Add explicit task statement
    if not has_task_statement(prompt):
        prompt = add_task_statement(prompt)
    
    # Replace vague terms
    vague_terms = identify_vague_terms(prompt)
    for term in vague_terms:
        specific = get_specific_alternative(term)
        prompt = prompt.replace(term, specific)
    
    # Add structure
    prompt = add_section_headers(prompt)
    
    return prompt
```

### Pattern 2: Example Augmentation

```python
def add_examples(prompt, task_type):
    """Add relevant examples to prompt."""
    examples = generate_examples(task_type, count=3)
    
    example_section = "\nExamples:\n"
    for i, example in enumerate(examples, 1):
        example_section += f"\n{i}. Input: {example.input}\n"
        example_section += f"   Output: {example.output}\n"
    
    return insert_before(prompt, "Now solve:", example_section)
```

### Pattern 3: Constraint Addition

```python
def add_constraints(prompt, risk_areas):
    """Add constraints to prevent issues."""
    constraints = []
    
    if 'hallucination' in risk_areas:
        constraints.append("- Only use provided information")
        constraints.append("- State if information is unknown")
    
    if 'format' in risk_areas:
        constraints.append("- Follow exact output format specified")
    
    if 'safety' in risk_areas:
        constraints.append("- Refuse harmful requests")
    
    constraint_section = "\nConstraints:\n" + "\n".join(constraints)
    
    return prompt + constraint_section
```

## Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Accuracy | > 85% | Correct outputs / Total outputs |
| Consistency | > 90% | Same input → same output |
| Format Compliance | > 95% | Correctly formatted outputs |
| Clarity Score | > 8/10 | Human evaluation |
| Iteration Efficiency | < 3 iterations | Average to reach target |

## Best Practices

1. **Start Simple**: Begin with clear instructions before adding complexity
2. **Test Early**: Test after each significant change
3. **Measure Objectively**: Use quantitative metrics when possible
4. **Document Everything**: Track all changes and their impacts
5. **Iterate Systematically**: Change one element at a time
6. **Know When to Stop**: Don't over-optimize for marginal gains
7. **Maintain Versions**: Keep previous versions for rollback

## Limitations

- Cannot fix fundamentally impossible tasks
- May require multiple iterations for complex prompts
- Quality depends on test case coverage
- Some optimizations are model-specific
- May not generalize to all edge cases

## Examples

### Example 1: Code Generation Prompt

**Before:**
```
Write a function to sort a list.
```

**After:**
```
Write a Python function to sort a list of integers in ascending order.

Requirements:
- Function name: sort_list
- Input: List[int]
- Output: List[int] (sorted)
- Time complexity: O(n log n)

Example:
Input: [3, 1, 4, 1, 5, 9, 2, 6]
Output: [1, 1, 2, 3, 4, 5, 6, 9]

Constraints:
- Handle empty list (return [])
- Handle single element (return as-is)
- Include type hints
- Add docstring

Output format:
```python
def sort_list(numbers: List[int]) -> List[int]:
    """Sort a list of integers in ascending order."""
    # Your implementation
```
```

### Example 2: Analysis Prompt

**Before:**
```
Analyze this text.
```

**After:**
```
Analyze the sentiment and key themes in the following text.

Text: [INPUT TEXT]

Analysis format:

1. Sentiment: [Positive/Negative/Neutral]
   - Confidence: [0-100%]
   - Key indicators: [List phrases]

2. Key Themes:
   - Theme 1: [Description with evidence]
   - Theme 2: [Description with evidence]
   - Theme 3: [Description with evidence]

3. Summary: [2-3 sentences]

Constraints:
- Base analysis on text content only
- Provide specific evidence for claims
- Acknowledge uncertainty if present
```

## Resources

- **CoT Paper**: https://arxiv.org/abs/2201.11903
- **ToT Paper**: https://arxiv.org/abs/2305.10601
- **Few-Shot Learning**: https://arxiv.org/abs/2005.14165
- **Prompt Engineering Guide**: https://www.promptingguide.ai

## Related Skills
- self-challenge: Challenge prompt capabilities
- meta-cognitive-reflection: Reflect on prompt performance
- ice-review: Review optimization impact

## Notes

- Prompt optimization is iterative - don't expect perfection in one attempt
- Different tasks may require different optimization approaches
- Always test with real inputs, not just idealized cases
- Balance complexity with clarity - sometimes simpler is better
- Monitor performance in production, not just in testing