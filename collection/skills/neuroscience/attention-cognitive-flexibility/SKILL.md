---
name: attention-cognitive-flexibility
description: "Neural network model of attention mechanisms enabling cognitive flexibility - rapid task switching and generalization. Shows how structured attention underlies prefrontal cortex function and adaptive behavior. Activation: cognitive flexibility, attention mechanism, task switching, prefrontal cortex, neural network, cognitive control."
---

# Attention to Task Structure for Cognitive Flexibility

A neural network model demonstrating how attention mechanisms enable rapid task switching and generalization. The model shows that **structured attention**, rather than executive control alone, underlies cognitive flexibility.

## Core Concept

Cognitive flexibility is the ability to adapt behavior to changing task demands. Traditional models emphasize executive control, but this work shows that **attention to task structure** is the key mechanism.

## Key Insight

- **Structured attention** enables rapid reconfiguration of processing
- Task representations are encoded in attention patterns
- Generalization emerges from compositional attention structures

## Architecture

### 1. Task-Structured Attention Network

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TaskStructuredAttention(nn.Module):
    """
    Attention mechanism structured by task demands.
    
    Combines:
    - Stimulus-driven attention (bottom-up)
    - Task-guided attention (top-down)
    - Structured representations for compositionality
    """
    
    def __init__(
        self,
        input_dim: int = 100,
        hidden_dim: int = 256,
        n_tasks: int = 10,
        n_attention_heads: int = 8,
    ):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.n_tasks = n_tasks
        
        # Task embedding (learned task representations)
        self.task_embedding = nn.Embedding(n_tasks, hidden_dim)
        
        # Stimulus encoder
        self.stimulus_encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
        
        # Structured attention layers
        self.attention_layers = nn.ModuleList([
            StructuredAttentionLayer(
                hidden_dim=hidden_dim,
                n_heads=n_attention_heads,
            )
            for _ in range(4)
        ])
        
        # Task-specific output heads
        self.task_heads = nn.ModuleList([
            nn.Linear(hidden_dim, output_dim)
            for _ in range(n_tasks)
        ])
    
    def forward(self, stimulus, task_id):
        """
        Process stimulus according to task.
        
        Args:
            stimulus: [batch, input_dim]
            task_id: [batch] - task identifier
        """
        batch_size = stimulus.shape[0]
        
        # Encode stimulus
        stimulus_features = self.stimulus_encoder(stimulus)
        
        # Get task representation
        task_repr = self.task_embedding(task_id)  # [batch, hidden_dim]
        
        # Combine task and stimulus for structured attention
        # Task guides how attention is allocated
        combined = stimulus_features + task_repr
        
        # Apply structured attention layers
        features = combined
        attention_patterns = []
        
        for layer in self.attention_layers:
            features, attn = layer(features, task_repr)
            attention_patterns.append(attn)
        
        # Task-specific output
        outputs = []
        for i, tid in enumerate(task_id):
            output = self.task_heads[tid](features[i])
            outputs.append(output)
        
        outputs = torch.stack(outputs)
        
        return outputs, attention_patterns


class StructuredAttentionLayer(nn.Module):
    """
    Attention layer with task-structured constraints.
    """
    
    def __init__(self, hidden_dim, n_heads=8):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.n_heads = n_heads
        self.head_dim = hidden_dim // n_heads
        
        # Multi-head attention
        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim)
        self.out_proj = nn.Linear(hidden_dim, hidden_dim)
        
        # Task structure modulation
        self.task_gate = nn.Linear(hidden_dim, n_heads)
    
    def forward(self, x, task_repr):
        """
        Apply attention modulated by task structure.
        """
        batch_size = x.shape[0]
        
        # Compute Q, K, V
        Q = self.q_proj(x).view(batch_size, -1, self.n_heads, self.head_dim)
        K = self.k_proj(x).view(batch_size, -1, self.n_heads, self.head_dim)
        V = self.v_proj(x).view(batch_size, -1, self.n_heads, self.head_dim)
        
        # Task-based gating of attention heads
        task_gates = torch.sigmoid(self.task_gate(task_repr))  # [batch, n_heads]
        
        # Attention scores
        scores = torch.einsum('bqhd,bkhd->bhqk', Q, K) / np.sqrt(self.head_dim)
        attn = F.softmax(scores, dim=-1)
        
        # Apply task gates
        attn = attn * task_gates.unsqueeze(1).unsqueeze(-1)
        attn = attn / (attn.sum(dim=-1, keepdim=True) + 1e-8)
        
        # Apply attention
        out = torch.einsum('bhqk,bkhd->bqhd', attn, V)
        out = out.reshape(batch_size, -1, self.hidden_dim)
        out = self.out_proj(out)
        
        return out, attn
```

### 2. Cognitive Flexibility Mechanism

```python
class CognitiveFlexibilityModule(nn.Module):
    """
    Implements flexible switching between tasks.
    
    Uses attention-based task switching rather than
    complete network reconfiguration.
    """
    
    def __init__(self, hidden_dim, n_tasks):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.n_tasks = n_tasks
        
        # Task switching attention
        self.switch_attention = nn.MultiheadAttention(
            hidden_dim, num_heads=8, batch_first=True
        )
        
        # Task conflict resolution
        self.conflict_gate = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.Sigmoid(),
        )
        
        # Adaptive learning rates per task
        self.task_lr = nn.Parameter(torch.ones(n_tasks) * 0.01)
    
    def switch_task(self, current_state, new_task_id, task_cache):
        """
        Rapidly switch to new task.
        
        Uses attention to retrieve and apply new task structure.
        """
        # Retrieve cached task representation
        new_task_repr = task_cache[new_task_id]
        
        # Attention-based task switching
        switched_state, _ = self.switch_attention(
            query=current_state.unsqueeze(1),
            key=new_task_repr.unsqueeze(1),
            value=new_task_repr.unsqueeze(1),
        )
        
        return switched_state.squeeze(1)
    
    def resolve_conflict(self, task_a_repr, task_b_repr, current_input):
        """
        Resolve conflict between competing task demands.
        """
        # Combine task representations
        combined = torch.cat([task_a_repr, task_b_repr], dim=-1)
        
        # Gating mechanism for conflict resolution
        gate = self.conflict_gate(combined)
        
        # Blend task representations based on input
        resolved = gate * task_a_repr + (1 - gate) * task_b_repr
        
        return resolved
```

## Task Representation Learning

### Compositional Task Structure

```python
class CompositionalTaskLearner:
    """
    Learn task representations as compositions of primitive operations.
    
    Enables generalization to novel task combinations.
    """
    
    def __init__(self, n_primitives, hidden_dim):
        self.n_primitives = n_primitives
        self.hidden_dim = hidden_dim
        
        # Primitive operation embeddings
        self.primitives = nn.Embedding(n_primitives, hidden_dim)
        
        # Composition network
        self.composition_net = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
        )
    
    def compose_task(self, primitive_ids, composition_structure):
        """
        Compose task from primitives.
        
        Args:
            primitive_ids: List of primitive operation IDs
            composition_structure: How to combine them (tree structure)
        """
        primitive_reprs = self.primitives(primitive_ids)
        
        # Compose according to structure
        if composition_structure == 'sequential':
            task_repr = self.compose_sequential(primitive_reprs)
        elif composition_structure == 'parallel':
            task_repr = self.compose_parallel(primitive_reprs)
        elif composition_structure == 'hierarchical':
            task_repr = self.compose_hierarchical(primitive_reprs)
        
        return task_repr
    
    def compose_sequential(self, primitive_reprs):
        """Sequential composition: A → B → C"""
        result = primitive_reprs[0]
        for i in range(1, len(primitive_reprs)):
            result = self.composition_net(
                torch.cat([result, primitive_reprs[i]], dim=-1)
            )
        return result
    
    def compose_parallel(self, primitive_reprs):
        """Parallel composition: A + B + C"""
        return torch.sum(primitive_reprs, dim=0)
    
    def compose_hierarchical(self, primitive_reprs):
        """Hierarchical composition: (A → B) + C"""
        # First compose some primitives
        intermediate = self.compose_sequential(primitive_reprs[:2])
        # Then combine with remaining
        return self.composition_net(
            torch.cat([intermediate, primitive_reprs[2]], dim=-1)
        )
```

## Training for Cognitive Flexibility

### Meta-Learning Task Switching

```python
class MetaLearningTrainer:
    """
    Meta-train for rapid task switching.
    """
    
    def __init__(self, model, n_tasks):
        self.model = model
        self.n_tasks = n_tasks
    
    def sample_meta_task(self):
        """
        Sample a sequence of tasks for meta-learning.
        """
        # Random sequence of 3-5 tasks
        sequence_length = np.random.randint(3, 6)
        task_sequence = np.random.randint(0, self.n_tasks, sequence_length)
        
        return task_sequence
    
    def meta_training_step(self, task_sequence, stimuli):
        """
        Train on task sequence to learn flexible switching.
        """
        total_loss = 0
        hidden_state = None
        
        for i, (task_id, stimulus) in enumerate(zip(task_sequence, stimuli)):
            # Forward pass
            output, hidden_state = self.model(
                stimulus, task_id, hidden_state
            )
            
            # Task-specific loss
            loss = self.compute_task_loss(output, task_id)
            
            # Add switching cost (encourages fast switching)
            if i > 0:
                switch_penalty = self.compute_switch_penalty(
                    hidden_state, task_id, task_sequence[i-1]
                )
                loss += 0.1 * switch_penalty
            
            total_loss += loss
        
        return total_loss / len(task_sequence)
    
    def compute_switch_penalty(self, hidden_state, current_task, previous_task):
        """
        Penalize slow task switching.
        
        Measures how different the hidden state is from
        expected state for current task.
        """
        expected_state = self.model.get_expected_state(current_task)
        distance = torch.norm(hidden_state - expected_state)
        return distance
```

## Biological Plausibility

### Prefrontal Cortex Implementation

```python
class PFCModel(nn.Module):
    """
    Model of prefrontal cortex function in cognitive flexibility.
    """
    
    def __init__(self, hidden_dim, n_tasks):
        super().__init__()
        
        # Lateral PFC: Task rule maintenance
        self.lateral_pfc = nn.LSTM(
            input_size=hidden_dim,
            hidden_size=hidden_dim,
            num_layers=2,
        )
        
        # Medial PFC: Conflict monitoring
        self.medial_pfc = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
            nn.Sigmoid(),
        )
        
        # Orbital PFC: Reward/outcome evaluation
        self.orbital_pfc = nn.Linear(hidden_dim, 1)
        
        # Connectivity to other regions
        self.parietal_proj = nn.Linear(hidden_dim, hidden_dim)
        self.striatum_proj = nn.Linear(hidden_dim, hidden_dim)
    
    def forward(self, sensory_input, current_task, reward_history):
        """
        Process through PFC modules.
        """
        # Lateral PFC maintains task rules
        task_context, _ = self.lateral_pfc(sensory_input)
        
        # Medial PFC monitors conflict
        conflict = self.medial_pfc(
            torch.cat([task_context, sensory_input], dim=-1)
        )
        
        # Orbital PFC evaluates outcomes
        expected_reward = self.orbital_pfc(task_context)
        
        # Project to action regions
        parietal_signal = self.parietal_proj(task_context)
        striatum_signal = self.striatum_proj(task_context)
        
        return {
            'task_context': task_context,
            'conflict': conflict,
            'expected_reward': expected_reward,
            'parietal': parietal_signal,
            'striatum': striatum_signal,
        }
```

## Evaluation

### Flexibility Metrics

```python
class FlexibilityMetrics:
    """Metrics for cognitive flexibility."""
    
    @staticmethod
    def task_switch_cost(model, task_a_data, task_b_data, n_trials=100):
        """
        Measure cost of switching between tasks.
        
        Compare performance on:
        - Repeat trials (same task)
        - Switch trials (different task)
        """
        repeat_times = []
        switch_times = []
        
        for trial in range(n_trials):
            # Measure time to criterion on task A
            time_a = model.time_to_criterion(task_a_data)
            
            if trial % 2 == 0:
                # Repeat: Task A again
                time_next = model.time_to_criterion(task_a_data)
                repeat_times.append(time_next)
            else:
                # Switch: Task B
                time_b = model.time_to_criterion(task_b_data)
                switch_times.append(time_b)
        
        switch_cost = np.mean(switch_times) - np.mean(repeat_times)
        return switch_cost
    
    @staticmethod
    def generalization_score(model, trained_tasks, novel_task):
        """
        Measure generalization to novel task.
        """
        # Zero-shot performance
        zero_shot = model.evaluate(novel_task, adapt=False)
        
        # Few-shot adaptation
        few_shot = model.evaluate(novel_task, adapt=True, n_examples=5)
        
        return {
            'zero_shot': zero_shot,
            'few_shot': few_shot,
            'adaptation_gain': few_shot - zero_shot,
        }
    
    @staticmethod
    def attention_reconfiguration_speed(model, task_transitions):
        """
        Measure how quickly attention reconfigures.
        """
        reconfiguration_times = []
        
        for old_task, new_task in task_transitions:
            # Track attention patterns
            attention_traces = []
            
            for t in range(100):  # 100 timesteps
                _, attention = model.forward(dummy_input, new_task)
                attention_traces.append(attention)
                
                # Check if attention has stabilized
                if t > 0 and attention_converged(attention_traces[-2:]):
                    reconfiguration_times.append(t)
                    break
        
        return np.mean(reconfiguration_times)
```

## Applications

### 1. Adaptive AI Systems

```python
class AdaptiveAgent:
    """
    AI agent with cognitive flexibility.
    """
    
    def __init__(self, flexibility_model):
        self.model = flexibility_model
        self.task_history = []
    
    def act(self, observation, current_goal):
        """
        Act flexibly based on current goal.
        """
        # Detect if goal has changed
        if current_goal != self.current_goal:
            # Rapidly switch task structure
            self.model.switch_task(current_goal)
        
        # Act according to current task
        action = self.model(observation, current_goal)
        
        return action
```

### 2. Cognitive Training

```python
def generate_flexibility_training(tasks, difficulty_progression):
    """
    Generate training curriculum for flexibility.
    """
    curriculum = []
    
    # Stage 1: Single tasks
    for task in tasks[:3]:
        curriculum.append([task] * 20)  # 20 trials each
    
    # Stage 2: Alternating (A-B-A-B)
    curriculum.append([tasks[0], tasks[1]] * 10)
    
    # Stage 3: Random switching
    curriculum.append(np.random.choice(tasks[:3], 40))
    
    # Stage 4: Multi-step tasks
    curriculum.append([
        [tasks[0], tasks[1]],  # Composite task
        [tasks[1], tasks[2]],
    ])
    
    return curriculum
```

## References

- Zhang, X. K., Senoussi, M., Verguts, T. (2026). Attention to task structure for cognitive flexibility. arXiv:2604.13281
- Monsell (2003). Task switching
- Koechlin & Summerfield (2007). An information theoretical approach to prefrontal executive function

## Activation Keywords

- cognitive flexibility
- attention mechanism
- task switching
- prefrontal cortex model
- neural network cognitive control
- structured attention
- compositional task learning
