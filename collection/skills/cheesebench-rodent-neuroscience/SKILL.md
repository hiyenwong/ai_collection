---
name: cheesebench-rodent-neuroscience
description: "CheeseBench benchmark for evaluating LLMs on classical rodent behavioral neuroscience paradigms. Includes 9 tasks covering water maze, T-maze, Morris water maze, and other established behavioral tests. Cross-paradigm evaluation for neuroscience AI systems."
version: 1.0.0
metadata:
  hermes:
    source_paper: "CheeseBench: Evaluating LLMs on Rodent Behavioral Neuroscience (arXiv:2604.13661)"
    tags: [neuroscience, benchmark, llm-evaluation, rodent, behavioral, paradigm]
---

# CheeseBench: Rodent Neuroscience LLM Evaluation

## Overview

Comprehensive benchmark evaluating LLMs on classical rodent behavioral neuroscience paradigms. Contains 9 tasks covering established behavioral tests (water maze, T-maze, open field, fear conditioning, etc.) for systematic evaluation of neuroscience AI systems.

## Benchmark Structure

| Task | Paradigm | Evaluation |
|------|----------|-----------|
| 1 | Water Maze | Spatial learning/memory |
| 2 | T-Maze | Working memory |
| 3 | Open Field | Locomotor activity |
| 4 | Fear Conditioning | Associative learning |
| 5 | Morris Water Maze | Spatial reference memory |
| 6 | Elevated Plus Maze | Anxiety-like behavior |
| 7 | Social Interaction | Social behavior |
| 8 | Novel Object Recognition | Recognition memory |
| 9 | Forced Swim | Behavioral despair |

## Usage

```python
def run_cheesebench(model, task_id=None):
    """Evaluate model on CheeseBench tasks."""
    if task_id:
        return evaluate_single_task(model, task_id)
    return evaluate_all_tasks(model)

# Tasks probe understanding of:
# - Experimental design in neuroscience
# - Behavioral interpretation
# - Statistical analysis
# - Translational relevance
```

## Applications

- **Neuroscience AI evaluation**: Benchmark domain-specific reasoning
- **LLM capability assessment**: Test scientific reasoning in neuroscience
- **Educational tools**: Validate AI teaching assistants for neuroscience
- **Research assistance**: Evaluate AI support for experimental design

## References

- Original paper: arXiv:2604.13661v1
- Published: 2026-04-15

## Activation Keywords

- "cheesebench-rodent-neuroscience"
- "cheesebench rodent neuroscience"
- "use cheesebench rodent neuroscience"
- "cheesebench rodent neuroscience help"
- "cheesebench rodent neuroscience tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Cheesebench Rodent Neuroscience usage
```
User: "Help me with cheesebench rodent neuroscience"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed cheesebench rodent neuroscience assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
