---
name: stp-stabilizes-goal-conditioned-dynamics
description: "短时程突触可塑性(STP)稳定目标条件化动力学方法论。研究STP如何在PFC储水池模型中支持多步目标导向行动规划，通过动态调节有效连接保持目标信息。Activation: STP, goal-conditioned dynamics, PFC reservoir, action planning, 突触可塑性, 目标导向行为."
---

# STP Stabilizes Goal-Conditioned Dynamics

**Paper:** arXiv:2606.03481 (Submitted: 2026-06-02)
**Authors:** Jin Nakamura, Yuichi Katori
**Categories:** q-bio.NC, cs.NE

## Core Innovation

**Short-Term Synaptic Plasticity (STP) stabilizes goal information as action-relevant, goal-conditioned dynamics** in prefrontal cortex (PFC) reservoir models for multistep goal-directed action planning.

### Key Finding

- **Without STP:** Success drops from 75.8% → 49.5% under noise
- **With STP:** Success remains stable: 91.8% → 89.2% (Cohen's dz=1.31)
- STP preserves goal information as **goal-conditioned dynamics** available at later action opportunities

## Neuroscience Mechanism

### PFC Goal Maintenance Problem

```python
"""
PFC Challenge:
- Maintain goal information over behavioral timescales
- Preserve in action-usable form (not just readable)
- Support delayed execution (delay period → action)

Traditional View:
- Recurrent circuits maintain information
- Issue: How to keep goal information "action-relevant"?

This Paper's Answer:
- STP provides dynamic modulation of goal-dependent connectivity
- Creates time-varying, goal-specific effective connectivity patterns
"""
```

### STP Mechanism

```python
class ShortTermSynapticPlasticity:
    """
    STP implementation in reservoir model
    
    Parameters:
    - U: utilization factor (release probability)
    - D: depression time constant
    - F: facilitation time constant
    
    Key dynamics:
    - Facilitation: Increases release probability with activity
    - Depression: Decreases available resources with activity
    """
    
    def __init__(self, U, D, F):
        self.U = U  # Utilization factor (0-1)
        self.D = D  # Depression time constant (ms)
        self.F = F  # Facilitation time constant (ms)
        self.x = 1.0  # Available resources
        self.u = U    # Current utilization
    
    def update(self, spike, dt):
        """STP dynamics update"""
        if spike:
            # Spike-triggered update
            self.u = self.u + self.U * (1 - self.u)  # Facilitation
            self.x = self.x - self.u * self.x         # Depression
        
        # Recovery dynamics
        self.u = self.u - self.u * dt / self.F  # Facilitation recovery
        self.x = self.x + (1 - self.x) * dt / self.D  # Resource recovery
        
        return self.u * self.x  # Effective synaptic weight
```

## Methodology Framework

### 1. PFC-Inspired Reservoir Model

```python
class PFCReservoirWithSTP:
    """
    Reservoir computing model with STP
    
    Architecture:
    - Input layer: Goal encoding
    - Reservoir: Recurrent network with STP synapses
    - Readout: Basal ganglia-inspired TD learning
    """
    
    def __init__(self, N_neurons, STP_config):
        self.N = N_neurons
        
        # Recurrent weights with STP
        self.W_rec = np.random.randn(N, N) * g / np.sqrt(N)
        self.stp = [ShortTermSynapticPlasticity(**STP_config) 
                    for _ in range(N*N)]
        
        # Input weights
        self.W_in = np.random.randn(N, goal_dim)
        
        # Readout (action values)
        self.W_out = np.zeros((num_actions, N))
    
    def forward(self, goal_input, delay_steps):
        """Forward pass through delay period"""
        
        # Initialize reservoir state
        r = np.zeros(self.N)
        
        # Encode goal
        r = np.dot(self.W_in, goal_input)
        
        # Evolve through delay period (STP active)
        for t in range(delay_steps):
            # Apply STP-modulated recurrent weights
            W_eff = self.compute_effective_weights()
            
            # Reservoir update
            dr = -r + np.dot(W_eff, r) + noise
            r = r + dt * dr
        
        # Read out action values
        action_values = np.dot(self.W_out, r)
        
        return action_values, r, W_eff
```

### 2. Goal-Conditioned Dynamics Analysis

```python
def analyze_goal_conditioned_dynamics(model, goals, noise_level):
    """
    Analyze how STP creates goal-specific dynamics
    
    Metrics:
    1. Goal decoding accuracy during delay
    2. State-space separability across goals
    3. Action-value difference (action relevance)
    4. Effective connectivity patterns
    """
    
    results = {
        'goal_decoding': [],
        'state_separability': [],
        'action_value_diff': [],
        'effective_connectivity': []
    }
    
    for goal in goals:
        # Run model with/without noise
        action_values, state, W_eff = model.forward(goal, delay)
        
        # 1. Goal decoding (linear readout)
        decoded_goal = linear_decoder(state)
        results['goal_decoding'].append(accuracy(decoded, goal))
        
        # 2. State-space separability
        separability = compute_separability(states_across_goals)
        results['state_separability'].append(separability)
        
        # 3. Action-value difference (relevance measure)
        av_diff = np.max(action_values) - np.min(action_values)
        results['action_value_diff'].append(av_diff)
        
        # 4. Effective connectivity patterning
        pattern = compute_pattern(W_eff)
        results['effective_connectivity'].append(pattern)
    
    return results
```

### 3. Control Experiments

```python
def run_controls(model):
    """
    Key control experiments from paper
    
    1. Gain-matched control: Fixed recurrent scaling
       - Tests if STP effect is just scaling
    
    2. STP-state perturbation: Freeze STP dynamics
       - Tests online vs offline STP
    
    3. Time constant grid search
       - Identify facilitation-dominant range
    """
    
    # Control 1: Gain-matched
    model_no_stp_matched = create_gain_matched_model(model)
    success_matched = evaluate(model_no_stp_matched, noise=True)
    
    # Control 2: STP freeze
    model_stp_frozen = freeze_stp_dynamics(model)
    success_frozen = evaluate(model_stp_frozen, noise=True)
    
    # Control 3: Grid search
    best_tau = grid_search_STP_time_constants(
        tau_range=(50, 500),  # ms
        metric='success_rate'
    )
    
    return {
        'gain_matched_success': success_matched,
        'stp_frozen_success': success_frozen,
        'optimal_tau': best_tau
    }
```

## Key Results

### 1. Robustness Under Noise

| Model | Clean | Noise | Drop |
|-------|-------|-------|------|
| No STP | 75.8% | 49.5% | -26.3% |
| With STP | 91.8% | 89.2% | -2.6% |

**Interpretation:** STP provides dramatic noise robustness (Cohen's dz=1.31)

### 2. Goal Decoding vs Action Relevance

```python
"""
Key distinction:
- Goal decoding: High in both models (STP not needed for readability)
- Action relevance: Only preserved with STP under noise

STP transforms goal representation from:
  "Readable" → "Action-relevant" (goal-conditioned dynamics)
"""
```

### 3. Effective Connectivity Dynamics

```python
"""
Without STP: Time-invariant connectivity
With STP: Goal-specific patterning increases toward action time

Pattern:
- Early delay: Weak goal-specific pattern
- Late delay: Strong goal-specific pattern (action-ready)

Interpretation: STP creates "task-state-conditioned" connectivity
"""
```

### 4. Optimal STP Parameters

```python
optimal_config = {
    'tau_facilitation': 200-400,  # ms (facilitation-dominant)
    'tau_depression': 500-800,    # ms
    'U_utilization': 0.2-0.4     # Low baseline
}

# Grid search found facilitation-dominant range yields highest success
```

## Implementation Guide

### Step 1: Build PFC Reservoir

```python
# Initialize reservoir
reservoir = PFCReservoirWithSTP(
    N_neurons=1000,
    STP_config={'U': 0.3, 'D': 600, 'F': 300}
)

# Goal encoding (e.g., 3 goals)
goal_encoder = GoalEncoder(num_goals=3, encoding_dim=100)
```

### Step 2: Train TD Readout

```python
# Basal ganglia-inspired TD learning
td_learner = TDReadoutLearner(
    reservoir=reservoir,
    num_actions=4,
    discount_factor=0.9
)

# Training loop
for episode in range(num_episodes):
    goal = select_goal()
    state = reservoir.encode_goal(goal)
    
    for step in range(delay_steps):
        action_values = td_learner.predict(state)
        action = select_action(action_values)
        
        # Execute and get reward
        reward = execute_action(action, goal)
        
        # TD update
        td_learner.update(state, action, reward)
```

### Step 3: Evaluate Robustness

```python
# Test under different noise levels
noise_levels = [0.0, 0.01, 0.05, 0.1]

for noise in noise_levels:
    success_rate = evaluate_task_performance(
        model, 
        noise_std=noise,
        num_trials=100
    )
    print(f"Noise {noise}: Success {success_rate:.1f}%")
```

## Applications

### 1. Cognitive Modeling

```python
# Model goal maintenance in PFC
pfc_model = PFCReservoirWithSTP(N=500)

# Simulate working memory tasks
task = GoalDirectedTask(delay=5.0, num_goals=3)
performance = evaluate(pfc_model, task, noise=True)
```

### 2. Neural Network Design

```python
# Incorporate STP in RNN architectures
class RNNWithSTP(nn.Module):
    """Modern RNN with STP-like adaptive weights"""
    
    def __init__(self, hidden_dim):
        self.hidden_dim = hidden_dim
        self.stp_module = AdaptiveWeightModule(
            facilitation_tau=300,
            depression_tau=600
        )
    
    def forward(self, x, h_prev):
        # STP-modulated recurrent weights
        W_eff = self.stp_module.get_effective_weights()
        h = torch.tanh(W_eff @ h_prev + self.W_in @ x)
        return h, W_eff
```

### 3. Robotics & Planning

```python
# Goal-directed action planning with STP stability
planner = STPReservoirPlanner(
    goal_dim=10,
    action_dim=4
)

# Robust planning under uncertainty
plan = planner.plan(goal_state, uncertainty_level=0.05)
```

## Key Insights

### 1. STP Functional Role

```markdown
- NOT just weight scaling (gain-matched control disproves)
- NOT offline static modulation (STP freeze control disproves)
- IS online, history-dependent synaptic modulation
- Creates time-varying, goal-specific connectivity patterns
```

### 2. Goal-Conditioned Dynamics

```markdown
Goal representation types:
1. Linear readable (decodable) - Both models have this
2. Action-relevant (usable for action selection) - Only with STP

STP transforms: Readable → Action-relevant
```

### 3. Temporal Structure

```markdown
Effective connectivity evolution:
- Without STP: Flat (time-invariant)
- With STP: Increases toward action opportunity
- Pattern: Task-state-conditioned (goal × time interaction)
```

## Limitations & Future Directions

1. **Model Simplification**
   - Reservoir vs detailed PFC circuit
   - Need more biologically realistic synapse models

2. **Task Specificity**
   - Multistep delay task only
   - Test on more complex planning tasks

3. **Neural Validation**
   - Computational model predictions
   - Need experimental validation in real PFC

## References

- Tsodyks-Markram STP model (1997)
- PFC working memory literature
- Reservoir computing theory
- Basal ganglia TD learning

## Activation Keywords

- STP, short-term synaptic plasticity
- Goal-conditioned dynamics
- PFC reservoir model
- Goal-directed action planning
- 突触可塑性, 目标导向行为
- Working memory stability
- Noise robustness
- Effective connectivity dynamics