---
name: attention-task-structure-cognitive-flexibility
description: Neural network model of attention mechanisms enabling cognitive flexibility through attention to task structure. Explores how neural systems dynamically reconfigure attention to handle multiple tasks and switch between cognitive demands.
version: 2.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [attention, cognitive-flexibility, task-switching, neural-networks, task-structure, prefrontal-cortex]
    source_paper: "Attention to task structure for cognitive flexibility (arXiv:2604.10923)"
    published: 2026-04-15
---

# Attention to Task Structure for Cognitive Flexibility

## Overview

A computational neuroscience methodology exploring how neural systems implement cognitive flexibility by attending to task structure. The model demonstrates how attentional mechanisms can dynamically reconfigure processing based on task demands, enabling flexible switching between different cognitive operations.

## Core Problem

Cognitive flexibility — the ability to adapt behavior to changing task demands — requires neural systems to dynamically attend to different aspects of task structure. Understanding how attention operates at the level of task rules and structures (rather than just stimuli) is crucial for modeling higher-order cognitive control.

## Key Mechanisms

### Task Structure Attention Model

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TaskStructureAttention(nn.Module):
    """
    Neural network model implementing attention to task structure
    for cognitive flexibility.
    """
    
    def __init__(self, input_dim=128, hidden_dim=256, 
                 num_tasks=4, num_rules=8, context_dim=64):
        super().__init__()
        self.num_tasks = num_tasks
        self.num_rules = num_rules
        self.context_dim = context_dim
        
        # Input encoding
        self.input_encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.GELU()
        )
        
        # Task structure representation
        self.task_structure = nn.Embedding(num_rules, hidden_dim)
        
        # Attention over task structure
        self.task_attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=8,
            batch_first=True
        )
        
        # Context gating for task switching
        self.context_gate = nn.Sequential(
            nn.Linear(context_dim + hidden_dim, hidden_dim),
            nn.Sigmoid()
        )
        
        # Output projection
        self.output_proj = nn.Linear(hidden_dim, num_tasks)
        
        # Working memory for task context
        self.task_context = nn.Parameter(torch.randn(1, num_tasks, hidden_dim))
    
    def attend_to_task_structure(self, input_repr, task_context):
        """
        Apply attention mechanism over task structure representations.
        
        Args:
            input_repr: [B, seq, hidden_dim] encoded input
            task_context: [B, num_tasks, hidden_dim] current task context
        Returns:
            attended: [B, seq, hidden_dim] task-structure attended representation
        """
        # Query from input, key/value from task structure
        attended, _ = self.task_attention(
            query=input_repr,
            key=task_context,
            value=task_context
        )
        return attended
    
    def switch_task(self, input_repr, new_task_id):
        """
        Switch attention to a different task structure.
        
        Args:
            input_repr: [B, seq, hidden_dim]
            new_task_id: [B] index of new task
        Returns:
            switched_repr: [B, seq, hidden_dim] with new task attention
        """
        # Retrieve new task structure
        task_struct = self.task_context[:, new_task_id, :]  # [B, hidden_dim]
        task_struct = task_struct.unsqueeze(1)  # [B, 1, hidden_dim]
        
        # Apply task-structure attention
        attended = self.attend_to_task_structure(input_repr, task_struct)
        
        # Gated combination
        gate = self.context_gate(
            torch.cat([input_repr, attended], dim=-1)
        )
        switched_repr = gate * attended + (1 - gate) * input_repr
        
        return switched_repr
    
    def forward(self, x, task_ids=None):
        """
        Forward pass with optional task switching.
        
        Args:
            x: [B, seq, input_dim] input sequence
            task_ids: optional [B] task indices for switching
        Returns:
            output: [B, num_tasks] task predictions
        """
        # Encode input
        h = self.input_encoder(x)
        
        if task_ids is not None:
            # Switch to specified task
            h = self.switch_task(h, task_ids)
        else:
            # Attend to current task context
            h = self.attend_to_task_structure(h, self.task_context)
        
        # Pool and classify
        h_pooled = h.mean(dim=1)
        output = self.output_proj(h_pooled)
        return output
```

### Cognitive Flexibility Metrics

```python
def compute_switch_cost(predictions, true_tasks, switch_indices):
    """
    Compute switch cost as performance degradation after task switches.
    """
    switch_perf = accuracy(predictions[switch_indices], true_tasks[switch_indices])
    repeat_mask = ~switch_indices
    repeat_perf = accuracy(predictions[repeat_mask], true_tasks[repeat_mask])
    return repeat_perf - switch_perf

def compute_attention_entropy(attention_weights):
    """
    Measure attentional focus via entropy of attention weights.
    Lower entropy = focused attention; Higher entropy = distributed attention (flexibility)
    """
    entropy = -torch.sum(attention_weights * torch.log(attention_weights + 1e-10), dim=-1)
    return entropy.mean()
```

## Key Findings

1. **Task Structure Attention**: Cognitive flexibility emerges from attentional mechanisms operating on task structure representations, not just stimulus features
2. **Dynamic Reconfiguration**: Neural systems rapidly reconfigure processing by shifting attention to different task rules
3. **Switch Costs**: Model reproduces human-like switch costs during task transitions
4. **Context Gating**: Gating mechanisms enable smooth transitions between task states

## Activation Keywords

- attention task structure cognitive flexibility
- task switching neural networks
- cognitive control attentional reconfiguration
- task rule attention prefrontal cortex
- 认知灵活性注意力机制
- 任务结构注意
- task-switching computational model
- cognitive control neural dynamics

## Applications

1. **Cognitive Modeling**: Simulate human task-switching behavior
2. **BCI**: Adaptive interfaces detecting and responding to task demands
3. **Clinical Assessment**: Measure cognitive flexibility in psychiatric conditions
4. **AI Systems**: Flexible AI adapting to changing task requirements

## References

- Attention to task structure for cognitive flexibility. arXiv:2604.10923, 2026-04-15.