---
name: cortex-subcortex-memory-limited-learning
description: "Framework for functional dissociation between cortical and subcortical systems during learning under memory constraints - cortex supports general structure learning while subcortex specializes in reward-based learning"
author: arXiv:2606.00667 (Farrell & Toyoizumi, May 2026)
version: 1.0.0
created: 2026-06-03
last_updated: 2026-06-03
paper_source: arXiv:2606.00667v1
doi: https://doi.org/10.48550/arXiv.2606.00667
tags: [neuroscience, learning, cortex, subcortex, memory-constraint, model-based, model-free, decision-making]
activation_keywords:
  - cortex subcortex learning
  - memory constraint learning
  - model-based model-free
  - cortical memory limited
  - Farrell Toyoizumi
  - functional dissociation learning
---

# Cortex and Subcortex Memory-Constrained Learning Framework

## Overview

This skill provides a theoretical framework for understanding the functional dissociation between cortical and subcortical systems during learning under memory constraints. The framework demonstrates that when cortical memory resources are limited, the cortex supports general structure learning while subcortical circuits specialize in reward-based learning.

**arXiv ID**: 2606.00667
**Authors**: Matthew Farrell, Taro Toyoizumi
**Submission Date**: May 30, 2026
**DOI**: https://doi.org/10.48550/arXiv.2606.00667

## Key Insights

### 1. Memory-Constrained Model-Based Learning

**Core Hypothesis**:
- The brain integrates flexible, computationally expensive cortical processing with simpler, lower-cost subcortical mechanisms
- Memory constraints on cortical resources naturally give rise to different learning strategies
- Model-based (cortical) and model-free (subcortical) modules learn in tandem

**Memory Constraint Framework**:
```
Memory Budget M = {State Representations × Resolution × Temporal Depth}

When M < M_required:
  - Cortical system focuses on general structure
  - Subcortical system handles reward exploitation
```

### 2. Strategic Memory Allocation

**Key Finding**: When rewarded states change often, it's advantageous for the model-based module to focus memory resources on capturing general structure of the environment, rather than exploiting current rewards.

**Memory Allocation Strategies**:
1. **Exploitation-Focused**: Allocate memory to current high-reward states
2. **Structure-Focused**: Allocate memory to environmental structure regardless of current rewards
3. **Mixed Strategy**: Balance between exploitation and structure

**Optimal Strategy Selection**:
```python
def optimal_strategy(reward_change_rate, memory_budget):
    """
    Determine optimal memory allocation strategy
    
    Parameters:
    - reward_change_rate: Frequency of reward state changes
    - memory_budget: Available cortical memory resources
    
    Returns:
    - strategy: 'structure_focused' | 'exploitation_focused' | 'mixed'
    """
    if reward_change_rate > threshold:
        return 'structure_focused'
    elif memory_budget > M_threshold:
        return 'mixed'
    else:
        return 'exploitation_focused'
```

### 3. Functional Dissociation Model

**Cortical Role**:
- General structure learning
- Environmental model building
- Long-term strategy development
- Flexibility and adaptation

**Subcortical Role**:
- Reward-based learning
- Habit formation
- Fast decision execution
- Computational efficiency

**Interaction Dynamics**:
```
Cortex: Model-Based System
├── Builds environmental model
├── Limited memory resources (M_cortex)
├── Generalizes across contexts
└── Slow, flexible learning

Subcortex: Model-Free System
├── Reward prediction
├── Low computational cost
├── Context-specific habits
└── Fast, rigid learning

Interaction:
├── Cortex provides structural guidance
├── Subcortex executes reward-seeking
└── Memory constraint forces specialization
```

## Mathematical Framework

### Model-Based-Model-Free Integration

**Standard MB-MF Framework**:
- Model-based: $V_{MB}(s) = \max_a Q_{MB}(s,a)$ with transition model $T(s'|s,a)$
- Model-free: $V_{MF}(s)$ learned via RL without transition model
- Weighted combination: $V(s) = \omega V_{MB}(s) + (1-\omega) V_{MF}(s)$

**Memory-Constrained Extension**:
```python
class MemoryConstrainedMBMF:
    def __init__(self, memory_budget, reward_change_rate):
        self.memory_budget = memory_budget
        self.reward_change_rate = reward_change_rate
        
    def allocate_memory(self, states, rewards):
        """
        Allocate limited memory to states
        
        Key insight: Under high reward change rate,
        allocate memory to structural states, not high-reward states
        """
        if self.reward_change_rate > threshold:
            # Structure-focused allocation
            memory_states = identify_structural_states(states)
        else:
            # Exploitation-focused allocation
            memory_states = identify_high_reward_states(states, rewards)
            
        return memory_states[:self.memory_budget]
```

### Memory Constraint Parameterization

**Memory Budget Measurement**:
```
M_cortex = N_states × Resolution × Temporal_window

Where:
- N_states: Number of representable states
- Resolution: Granularity of state representation  
- Temporal_window: Depth of temporal predictions
```

**Constraint Impact**:
- When $M_{required} > M_{cortex}$: Specialization emerges
- When $M_{required} \leq M_{cortex}$: Flexible integration possible

## Experimental Validation

### Hypotheses Testable in Experimental Data

**H1: Cortical Generalization Under Constraint**
- Cortex represents environmental structure rather than specific reward contingencies
- Test: Examine cortical representations across reward schedule changes

**H2: Subcortical Reward Specialization**
- Subcortical activity correlates with current reward values
- Test: Compare subcortical responses to reward changes vs. structural changes

**H3: Memory Constraint Effects**
- Memory limitation forces functional dissociation
- Test: Manipulate memory demands and observe cortical-subcortical balance

**H4: Reward Change Rate Interaction**
- High reward change rates shift cortical focus to structure
- Test: Compare learning across different reward stability conditions

### Neural Signature Predictions

**Cortical Activity Patterns**:
- Stable across reward contingencies
- Correlated with structural features (transitions, state topology)
- Higher in novel/restructured environments

**Subcortical Activity Patterns**:
- Tracks current reward values
- Rapid updates with reward changes
- Higher in stable reward environments

**fMRI/EEG Markers**:
```
Cortical markers:
├── Prefrontal cortex: Environmental model building
├── Hippocampus: Structural memory encoding
└── Posterior parietal: State space representation

Subcortical markers:
├── Striatum: Reward prediction
├── Amygdala: Reward value encoding
└── Dopaminergic system: Reward learning signals
```

## Implementation Guidelines

### 1. Computational Model Implementation

```python
import numpy as np

class MemoryConstrainedLearningModel:
    """
    Implementation of cortex-subcortex learning framework
    """
    
    def __init__(self, n_states, n_actions, memory_budget, 
                 reward_change_rate=0.1):
        self.n_states = n_states
        self.n_actions = n_actions
        self.memory_budget = memory_budget
        self.reward_change_rate = reward_change_rate
        
        # Model-based (cortical) system
        self.mb_transition_model = {}
        self.mb_memory_states = set()
        
        # Model-free (subcortical) system  
        self.mf_q_values = np.zeros((n_states, n_actions))
        
    def update_mb_memory(self, states_visited):
        """
        Update cortical memory allocation
        
        Strategy depends on reward change rate:
        - High change: Store structural states
        - Low change: Store high-reward states
        """
        if self.reward_change_rate > 0.5:
            # Structure-focused: states with high transition variability
            structural_states = self.identify_structural_states(states_visited)
            self.mb_memory_states.update(structural_states)
        else:
            # Exploitation-focused: states with high average reward
            reward_states = self.identify_reward_states(states_visited)
            self.mb_memory_states.update(reward_states)
            
        # Enforce memory budget
        if len(self.mb_memory_states) > self.memory_budget:
            self.mb_memory_states = set(list(self.mb_memory_states)[:self.memory_budget])
            
    def identify_structural_states(self, states):
        """
        Identify states important for environmental structure
        
        Criteria:
        - High branching factor (many possible next states)
        - Transition uncertainty
        - Central position in state graph
        """
        structural_scores = {}
        for s in states:
            branching = len(self.mb_transition_model.get(s, {}))
            uncertainty = self.compute_transition_uncertainty(s)
            centrality = self.compute_state_centrality(s, states)
            
            structural_scores[s] = branching + uncertainty + centrality
            
        return sorted(structural_scores.keys(), 
                      key=lambda x: structural_scores[x], reverse=True)
        
    def compute_mb_value(self, state):
        """
        Compute model-based value with memory constraint
        
        Only uses stored transition model for memory states
        """
        if state in self.mb_memory_states:
            # Full model-based computation
            return self.full_mb_value(state)
        else:
            # Reduced model-based or rely on model-free
            return self.reduced_mb_value(state)
            
    def update_mf_values(self, state, action, reward, next_state):
        """
        Update model-free (subcortical) Q-values
        
        Standard RL update without memory constraints
        """
        td_error = reward + self.gamma * max(self.mf_q_values[next_state]) - \
                   self.mf_q_values[state, action]
        self.mf_q_values[state, action] += self.alpha * td_error
        
    def decide_action(self, state):
        """
        Combine MB and MF systems weighted by memory availability
        """
        mb_value = self.compute_mb_value(state)
        mf_value = self.mf_q_values[state]
        
        # Weight depends on memory state inclusion
        weight_mb = 1.0 if state in self.mb_memory_states else 0.3
        
        combined_value = weight_mb * mb_value + (1 - weight_mb) * mf_value
        
        return np.argmax(combined_value)
```

### 2. Experimental Analysis Framework

```python
def analyze_cortical_subcortical_dissociation(neural_data, behavioral_data):
    """
    Analyze neural data for cortical-subcortical dissociation
    
    Parameters:
    - neural_data: fMRI/EEG recordings with region labels
    - behavioral_data: Learning trajectories, reward schedules
    
    Returns:
    - dissociation_score: Evidence for functional separation
    """
    
    # Extract cortical vs subcortical activity
    cortical_activity = neural_data.filter_regions(['PFC', 'HC', 'PPC'])
    subcortical_activity = neural_data.filter_regions(['striatum', 'amygdala'])
    
    # Test cortical stability across reward changes
    reward_stability_score = test_cortical_stability(
        cortical_activity, behavioral_data.reward_changes
    )
    
    # Test subcortical reward tracking
    reward_tracking_score = test_subcortical_reward_correlation(
        subcortical_activity, behavioral_data.rewards
    )
    
    # Compute dissociation index
    dissociation_score = reward_stability_score * reward_tracking_score
    
    return {
        'dissociation_score': dissociation_score,
        'cortical_stability': reward_stability_score,
        'subcortical_reward_tracking': reward_tracking_score
    }
```

## Key Applications

### 1. Understanding Brain Learning Mechanisms

- Explains why cortical and subcortical systems have distinct roles
- Provides computational framework for memory-constrained learning
- Predicts neural activity patterns under different reward schedules

### 2. AI/ML Memory-Constrained Systems

- Design hybrid systems with limited memory budgets
- Optimize memory allocation strategies
- Combine model-based and model-free learning efficiently

### 3. Clinical Implications

- Parkinson's disease: Subcortical dysfunction effects
- Memory disorders: Cortical constraint impacts
- Addiction: Reward system specialization

### 4. NeuroAI Architecture Design

```python
class MemoryConstrainedNeuroAI:
    """
    NeuroAI architecture implementing cortex-subcortex framework
    """
    
    def __init__(self, memory_budget):
        self.cortical_module = CorticalModule(memory_budget)
        self.subcortical_module = SubcorticalModule()
        
    def learn(self, environment):
        """
        Learning with memory-constrained cortical + unlimited subcortical
        """
        for episode in environment:
            # Cortical: Build structure model with limited memory
            self.cortical_module.update_structure(episode)
            
            # Subcortical: Learn reward associations
            self.subcortical_module.update_rewards(episode)
            
            # Combine for decision
            action = self.combine_modules(episode.state)
```

## Theoretical Extensions

### 1. Multi-Level Memory Constraints

**Hierarchical Memory Budgets**:
```
L1 (Primary Cortex): Highest resolution, smallest budget
L2 (Secondary Cortex): Medium resolution, medium budget  
L3 (Association Cortex): Low resolution, large budget

Each level specializes in different structural features
```

### 2. Dynamic Memory Reallocation

**Adaptive Strategy**:
- Memory allocation can shift based on environmental demands
- Rapid reward changes → structure focus
- Stable rewards → exploitation focus

### 3. Developmental Trajectories

**Memory Budget Growth**:
- Early development: Limited cortical memory, heavy subcortical reliance
- Maturation: Growing cortical memory enables flexible integration
- Aging: Memory decline may revert to subcortical dominance

## Experimental Design Recommendations

### Task Design

**Task Parameters**:
```
Essential variables:
├── Reward change rate (λ): 0.1, 0.5, 1.0 per episode
├── State space complexity (N): 10, 50, 100 states
├── Memory demands (M_required vs M_available)
└── Transition structure variability (T_var)
```

**Recommended Tasks**:
1. Two-step task with varying reward stability
2. Maze navigation with changing reward locations
3. Probabilistic reversal learning

### Neural Recording

**Recommended Methods**:
- fMRI: Whole-brain cortical and subcortical activity
- EEG: Temporal dynamics of cortical processes
- Electrophysiology: Striatal dopamine signals, cortical representations

**Analysis Metrics**:
```python
metrics = {
    'cortical_stability_index': 'Correlation of cortical activity across reward changes',
    'subcortical_reward_index': 'Correlation of subcortical activity with reward value',
    'memory_utilization': 'Number of states in cortical representation',
    'learning_efficiency': 'Performance per memory unit'
}
```

## Connections to Other Frameworks

### Related Skills

- [[agent-memory-framework]]: AI memory architecture
- [[neural-digital-twins-bci]]: Brain-computer interfaces
- [[model-based-model-free-learning]]: Standard MB-MF framework
- [[cortico-cerebellar-modularity-rnn]]: Cortico-cerebellar interactions
- [[hippocampal-entorhinal-world-model]]: Structure learning systems

### Theoretical Connections

**Reinforcement Learning Theory**:
- Dyna architectures: Model-based + model-free integration
- Prioritized sweeping: Memory allocation strategies
- Experience replay: Subcortical-like learning

**Neuroscience Frameworks**:
- Habit vs goal-directed behavior
- Model-free vs model-based decision making
- Cortical vs striatal learning systems

## Pitfalls and Considerations

### Common Mistakes

1. **Over-generalizing dissociation**: Framework applies under memory constraints, not universally
2. **Ignoring memory dynamics**: Memory allocation strategy depends on reward change rate
3. **Simplistic cortical-subcortical mapping**: Real systems have complex interactions beyond this model

### Limitations

1. Model is theoretical; experimental validation ongoing
2. Memory budget quantification is simplified
3. Real cortical-subcortical interactions more complex

### Best Practices

1. **Parameter Estimation**:
   - Estimate memory budget empirically from neural capacity
   - Measure reward change rate from behavioral data
   
2. **Model Comparison**:
   - Compare with standard MB-MF models
   - Test predictions in memory-manipulated experiments
   
3. **Neural Validation**:
   - Use multi-region recordings to test dissociation
   - Compare cortical stability vs subcortical reward tracking

## Future Directions

### Open Questions

1. How does memory budget vary across individuals?
2. Can memory reallocation be dynamically controlled?
3. What triggers transition from structure-focused to exploitation-focused?

### Research Extensions

1. **Computational**: Implement in deep RL architectures
2. **Neural**: Test predictions in animal learning experiments
3. **Clinical**: Apply to understanding learning disorders

## References

### Primary Source
- arXiv:2606.00667 - Farrell & Toyoizumi (2026)

### Related Literature
- Daw et al. (2011): Model-based vs model-free arbitration
- Keramati et al. (2011): Speed-accuracy tradeoff in MB-MF
- Kool et al. (2018): Cognitive resource demands in MB learning

---

## Summary

This framework provides a theoretical foundation for functional dissociation between cortical and subcortical learning systems under memory constraints. Key prediction: cortex specializes in general structure learning while subcortex handles reward-based learning when cortical memory is limited. Testable through neural recordings comparing cortical stability and subcortical reward tracking.

**Activation Keywords**: cortex subcortex learning, memory constraint learning, model-based model-free, Farrell Toyoizumi, functional dissociation learning