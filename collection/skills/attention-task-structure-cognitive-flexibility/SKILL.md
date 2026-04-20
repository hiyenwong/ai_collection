---
name: attention-task-structure-cognitive-flexibility
description: Neural network model of attention mechanisms enabling cognitive flexibility - retaining prior knowledge while transferring to new tasks
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [attention, cognitive-flexibility, task-structure, transfer-learning]
    source_paper: "Attention to task structure for cognitive flexibility (arXiv:2604.13281)"
    authors: "Xiaoyu K. Zhang, Mehdi Senoussi, Tom Verguts"
    published: "2026-04-14"
    category: "neuroscience"
---

# Attention to Task Structure for Cognitive Flexibility

## Overview
Neural network model of attention mechanisms enabling cognitive flexibility -- retaining prior knowledge while transferring to new tasks. Important for understanding how brains and AI systems manage task switching.

## Key Concepts

### Task Structure Attention
- Attending to abstract task rules
- Flexible reconfiguration of processing
- Knowledge retention during transfer

## Implementation Pattern

```python
import numpy as np

class TaskFlexibleNetwork:
    def __init__(self, input_dim, hidden_dim, n_tasks):
        self.W_shared = np.random.randn(hidden_dim, input_dim) * 0.1
        self.W_task = np.random.randn(n_tasks, hidden_dim, hidden_dim) * 0.1
        self.task_attention = np.ones(n_tasks) / n_tasks

    def attend_task(self, task_id):
        self.task_attention = np.zeros(len(self.task_attention))
        self.task_attention[task_id] = 1.0

    def forward(self, x, task_id):
        h = np.tanh(self.W_shared @ x)
        # Task-specific transformation
        W = np.sum(self.W_task * self.task_attention[:, None, None], axis=0)
        out = W @ h
        return out
```

## Applications
- Continual learning
- Multi-task AI systems
- Cognitive flexibility research

## References
- Attention to task structure for cognitive flexibility
- Authors: Xiaoyu K. Zhang, Mehdi Senoussi, Tom Verguts
- arXiv: 2604.13281 (2026-04-14)

## Activation
- cognitive flexibility
- task structure attention
- transfer learning
- 认知灵活性
- 任务结构注意

## Activation Keywords

- "attention-task-structure-cognitive-flexibility"
- "attention task structure cognitive flexibility"
- "use attention task structure cognitive flexibility"
- "attention task structure cognitive flexibility help"
- "attention task structure cognitive flexibility tool"

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

### Basic Attention Task Structure Cognitive Flexibility usage
```
User: "Help me with attention task structure cognitive flexibility"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed attention task structure cognitive flexibility assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
