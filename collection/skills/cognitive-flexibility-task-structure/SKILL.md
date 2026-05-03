---
name: cognitive-flexibility-task-structure
description: Neural network model of attention to task structure enabling cognitive flexibility. Studies how neural networks learn to attend to relevant task dimensions and switch between task rules. Combines attention mechanisms with structured task representations to model cognitive control. Use when building neural models of cognitive flexibility, studying task switching in neural networks, implementing attention-based rule learning, or analyzing prefrontal cortex-like computation in artificial networks. Triggers: cognitive flexibility, task structure, task switching, attention task, rule learning neural, cognitive control, prefrontal model.
---

# Attention to Task Structure for Cognitive Flexibility

## Core Concept

Cognitive flexibility — the ability to switch between different task rules or mental sets — emerges from neural networks that learn to attend to relevant task structure. This skill provides methodology for building and analyzing such models.

## Key Mechanisms

### 1. Task Structure Representation

Tasks are decomposed into structural components:
- **Input dimensions**: What features are available
- **Rule set**: Which mapping from inputs to outputs applies
- **Context signal**: External or internal cue indicating current rule

### 2. Attention-Based Rule Selection

The network learns a gating mechanism:

```
attention_weights = softmax(W_context · h_context + W_rule · h_rule)
output = Σ_i attention_weights[i] · f_i(input)
```

Where f_i represents different input-output mappings (rules).

### 3. Meta-Learning for Rule Acquisition

Rules are acquired through meta-learning:

```
θ_rule ← θ_rule - α · ∇_θ L_task(θ, context)
```

The network updates its rule-specific parameters based on task context, enabling rapid adaptation.

## Implementation Architecture

### Core Model

```python
import torch
import torch.nn as nn

class CognitiveFlexibilityModel(nn.Module):
    """Neural network with attention-based task structure."""
    
    def __init__(self, input_dim, hidden_dim, n_rules, output_dim):
        super().__init__()
        self.n_rules = n_rules
        
        # Rule-specific processing modules
        self.rule_modules = nn.ModuleList([
            nn.Sequential(
                nn.Linear(input_dim, hidden_dim),
                nn.ReLU(),
                nn.Linear(hidden_dim, output_dim)
            ) for _ in range(n_rules)
        ])
        
        # Context encoder
        self.context_encoder = nn.Linear(input_dim, hidden_dim)
        
        # Attention over rules
        self.rule_attention = nn.Linear(hidden_dim, n_rules)
        
    def forward(self, x, context):
        """x: input, context: task context cue"""
        # Encode context
        ctx_repr = torch.relu(self.context_encoder(context))
        
        # Compute attention weights over rules
        attn_weights = torch.softmax(self.rule_attention(ctx_repr), dim=-1)
        
        # Weighted combination of rule outputs
        rule_outputs = torch.stack([
            rule(x) for rule in self.rule_modules
        ], dim=-1)  # (batch, output_dim, n_rules)
        
        output = torch.sum(rule_outputs * attn_weights.unsqueeze(1), dim=-1)
        return output, attn_weights
```

### Training with Meta-Learning

```python
def meta_train_step(model, task_batch, context, lr_inner=0.01):
    """Inner loop: adapt to a specific task rule."""
    # Clone model for task-specific adaptation
    adapted = clone_model(model)
    
    # Fast adaptation
    loss = compute_loss(adapted, task_batch, context)
    adapted.fast_adapt(loss, lr=lr_inner)
    
    # Meta-gradient
    meta_loss = compute_loss(adapted, task_batch, context)
    return meta_loss

def task_switch_eval(model, old_context, new_context, test_data):
    """Evaluate ability to switch between task rules."""
    # Measure switch cost: performance drop when context changes
    _, old_attn = model(test_data.x, old_context)
    _, new_attn = model(test_data.x, new_context)
    
    switch_cost = torch.norm(old_attn - new_attn)
    return switch_cost
```

## Analysis Methods

### Measuring Cognitive Flexibility

1. **Switch Cost**: Performance degradation when switching rules
   ```
   switch_cost = accuracy(task_A after B) - accuracy(task_A after A)
   ```

2. **Rule Abstraction**: How well learned rules generalize to new inputs
   ```
   abstraction_score = accuracy(new_inputs, known_rule)
   ```

3. **Attention Alignment**: Correlation between attention weights and ground-truth rule relevance
   ```
   alignment = cosine_similarity(attn_weights, rule_relevance)
   ```

### Visualization

```python
def plot_attention_dynamics(model, context_sequence, input_stream):
    """Plot how attention shifts across rules over time."""
    attn_weights = []
    for ctx in context_sequence:
        _, attn = model(input_stream, ctx)
        attn_weights.append(attn.detach().cpu().numpy())
    
    plt.imshow(np.array(attn_weights).T, aspect='auto')
    plt.xlabel('Time Step')
    plt.ylabel('Rule')
    plt.title('Attention Dynamics Across Task Switches')
```

## Experimental Paradigms

| Paradigm | Description | Key Metric |
|----------|-------------|------------|
| Task switching | Alternate between 2+ rules | Switch cost, reaction time |
| Rule abstraction | Apply learned rule to novel inputs | Generalization accuracy |
| Context learning | Learn context cues from data | Context inference accuracy |
| Interference | Competing rules active simultaneously | Conflict resolution rate |

## Applications

- **Cognitive modeling**: Understanding prefrontal cortex function
- **Continual learning**: Networks that adapt to new tasks without forgetting
- **Multi-task learning**: Shared representations with task-specific routing
- **Adaptive AI**: Systems that flexibly switch strategies based on context

## Activation Keywords

- cognitive flexibility
- task structure
- task switching
- attention task
- rule learning neural
- cognitive control
- prefrontal model
- 认知灵活性
- 任务切换
- 规则学习

## Tools Used

- `read` - Read research papers and model implementations
- `write` - Save model configurations and analysis results
- `exec` - Run neural network training scripts for cognitive flexibility models

## Instructions for Agents

Follow these steps when helping users implement cognitive flexibility models:

1. **Identify the task structure**: Determine the rules, input dimensions, and context signals
2. **Build the attention model**: Implement the attention-based rule selection mechanism
3. **Train with meta-learning**: Apply the meta-learning approach for rule acquisition
4. **Analyze flexibility**: Measure switch cost, generalization, and interference

## Examples

### Example 1: Task Switching Model

```
User: "构建任务切换的神经网络模型"

Execute:
1. Define the task structure with multiple rules
2. Build the attention-based rule selection mechanism
3. Train with meta-learning for rule acquisition
4. Analyze switch cost and flexibility metrics
```

### Example 2: Cognitive Control Analysis

```
User: "分析认知控制中的注意力动态"

Execute:
1. Load the trained cognitive flexibility model
2. Extract attention weights across task switches
3. Visualize attention dynamics
4. Quantify rule selection accuracy and reaction time
```
