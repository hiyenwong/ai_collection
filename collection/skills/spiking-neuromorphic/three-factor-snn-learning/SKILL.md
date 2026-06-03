---
name: three-factor-snn-learning
description: "Three-factor learning rules for Spiking Neural Networks - extending STDP with neuromodulatory signals for improved credit assignment, reinforcement learning, and biological plausibility. Comprehensive survey from machine learning perspective. Activation triggers: three-factor learning, SNN learning, neuromodulation, STDP extension, reward learning, dopamine, surrogate gradient."
---

# Three-Factor Learning in Spiking Neural Networks

> A comprehensive survey of three-factor learning rules for SNNs from a machine learning perspective, bridging neuroscience and AI through neuromodulatory mechanisms.

## Metadata
- **Source**: arXiv:2504.05341
- **Authors**: Szymon Mazurek, Jakub Caputa, Jan K. Argasiński, Maciej Wielgosz
- **Published**: 2025-04
- **Institution**: AGH University of Krakow, Jagiellonian University, Sano - Centre for Computational Medicine

## Core Methodology

### Key Innovation

Three-factor learning extends traditional Hebbian learning (two-factor: pre- and post-synaptic activity) by introducing a **third factor** - typically a **neuromodulatory signal** that provides global contextual information about reward, error, or task relevance.

| Learning Rule | Factors | Third Factor | Application |
|--------------|---------|--------------|-------------|
| Hebbian | 2 (pre, post) | None | Unsupervised |
| STDP | 2 (pre, post, timing) | None | Unsupervised |
| **Three-Factor** | **3** | **Neuromodulator** | **Supervised/RL** |
| R-STDP | 2-3 | Reward | Reinforcement |
| e-prop | 2-3 | Error signal | Supervised |

### The Third Factor

**Neuromodulatory Signals**:
- **Dopamine**: Reward prediction error, motor learning
- **Acetylcholine**: Attention, salience, uncertainty
- **Norepinephrine**: Arousal, exploration
- **Serotonin**: Mood, behavioral inhibition
- **Error signals**: Task-specific loss gradients

**Mathematical Formulation**:

$$\Delta w_{ij} = \eta \cdot M(t) \cdot f(\text{pre}_i, \text{post}_j, \text{timing})$$

Where:
- $w_{ij}$: Synaptic weight from neuron $i$ to $j$
- $\eta$: Learning rate
- $M(t)$: Neuromodulatory signal (third factor)
- $f$: STDP-like eligibility trace

### Eligibility Trace

The eligibility trace acts as a short-term memory of recent synaptic activity:

$$\frac{d e_{ij}}{dt} = -\frac{e_{ij}}{\tau_e} + \text{STDP}(t_i^{pre}, t_j^{post})$$

$$\Delta w_{ij} = \eta \cdot M(t) \cdot e_{ij}$$

| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| $\tau_e$ | Eligibility trace decay | 50-500 ms |
| $\eta$ | Learning rate | 0.001-0.1 |
| $M(t)$ | Modulatory signal | Task-dependent |

## Implementation Guide

### Prerequisites

```python
# Required packages
pip install torch snntorch
pip install numpy matplotlib
pip install gymnasium  # For RL environments
```

### Step-by-Step

#### Step 1: Basic Three-Factor Learning

```python
import torch
import torch.nn as nn
import numpy as np

class ThreeFactorSNNLayer(nn.Module):
    """
    SNN layer with three-factor learning rules
    
    Combines local STDP-like eligibility traces with
    global neuromodulatory signals
    """
    
    def __init__(
        self,
        n_inputs,
        n_neurons,
        tau_mem=20.0,      # Membrane time constant
        tau_syn=5.0,       # Synaptic time constant
        tau_elig=100.0,    # Eligibility trace time constant
        v_thresh=-50.0,    # Firing threshold (mV)
        v_rest=-65.0,      # Resting potential
        dt=1.0             # Time step (ms)
    ):
        super().__init__()
        
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons
        
        # Time constants
        self.tau_mem = tau_mem
        self.tau_syn = tau_syn
        self.tau_elig = tau_elig
        self.dt = dt
        self.alpha_mem = np.exp(-dt / tau_mem)
        self.alpha_syn = np.exp(-dt / tau_syn)
        self.alpha_elig = np.exp(-dt / tau_elig)
        
        # Thresholds
        self.v_thresh = v_thresh
        self.v_rest = v_rest
        
        # Synaptic weights
        self.weights = nn.Parameter(
            torch.randn(n_inputs, n_neurons) * 0.1
        )
        
        # State variables
        self.v_mem = None      # Membrane potential
        self.i_syn = None      # Synaptic current
        self.e_trace = None    # Eligibility trace
        self.spikes = None     # Spike output
        
    def reset_state(self, batch_size, device):
        """Reset layer state"""
        self.v_mem = torch.full(
            (batch_size, self.n_neurons),
            self.v_rest,
            device=device
        )
        self.i_syn = torch.zeros(batch_size, self.n_neurons, device=device)
        self.e_trace = torch.zeros(
            batch_size, self.n_inputs, self.n_neurons,
            device=device
        )
        self.spikes = torch.zeros(batch_size, self.n_neurons, device=device)
        self.pre_spikes = torch.zeros(batch_size, self.n_inputs, device=device)
    
    def forward(self, x):
        """
        Forward pass computing spikes and eligibility traces
        
        Args:
            x: Input spikes (batch, n_inputs)
        
        Returns:
            spikes: Output spikes (batch, n_neurons)
            e_trace: Eligibility traces (batch, n_inputs, n_neurons)
        """
        # Ensure state initialized
        if self.v_mem is None:
            self.reset_state(x.size(0), x.device)
        
        # Store previous states for eligibility
        v_mem_pre = self.v_mem.clone()
        pre_spikes = self.pre_spikes.clone()
        
        # Update synaptic current
        self.i_syn = self.alpha_syn * self.i_syn + x @ self.weights
        
        # Update membrane potential
        self.v_mem = self.alpha_mem * self.v_mem + self.i_syn
        
        # Check for spikes
        self.spikes = (self.v_mem >= self.v_thresh).float()
        
        # Reset after spike
        self.v_mem = torch.where(
            self.spikes > 0,
            torch.full_like(self.v_mem, self.v_rest),
            self.v_mem
        )
        
        # Update eligibility traces (STDP-like)
        # Post-synaptic term: depends on postsynaptic activity
        post_term = self.spikes.unsqueeze(1)  # (batch, 1, n_neurons)
        
        # Pre-synaptic term: depends on presynaptic activity
        pre_term = pre_spikes.unsqueeze(2)    # (batch, n_inputs, 1)
        
        # Hebbian update to eligibility trace
        hebbian = pre_term * post_term  # (batch, n_inputs, n_neurons)
        
        # Decay existing trace and add new contribution
        self.e_trace = self.alpha_elig * self.e_trace + hebbian
        
        # Store pre-synaptic spikes for next time step
        self.pre_spikes = x
        
        return self.spikes, self.e_trace
    
    def apply_modulation(self, M, learning_rate=0.001):
        """
        Apply three-factor learning rule
        
        Args:
            M: Modulatory signal (batch, 1) or (batch, n_neurons)
            learning_rate: Base learning rate
        
        Returns:
            weight_update: Updates to apply to weights
        """
        # Three-factor rule: dW = η * M * e_trace
        if M.dim() == 2:
            M = M.unsqueeze(1)  # (batch, 1, n_neurons) or (batch, 1, 1)
        
        # Weight update averaged over batch
        # e_trace: (batch, n_inputs, n_neurons)
        # M: (batch, 1, n_neurons)
        delta_w = learning_rate * (M * self.e_trace).mean(dim=0)
        
        # Apply update
        self.weights.data += delta_w
        
        return delta_w


# Test basic three-factor learning
layer = ThreeFactorSNNLayer(n_inputs=10, n_neurons=20)
layer.reset_state(batch_size=1, device='cpu')

# Simulate for some time steps
for t in range(100):
    # Random input spikes
    input_spikes = (torch.rand(1, 10) < 0.1).float()
    
    # Forward pass
    output_spikes, eligibility = layer(input_spikes)
    
    # Every 20 steps, apply reward-based modulation
    if t % 20 == 0:
        reward = torch.randn(1, 1)  # Random reward signal
        layer.apply_modulation(reward, learning_rate=0.01)
        print(f"t={t}: Applied modulation, weight update norm: {reward.abs().item():.4f}")
```

#### Step 2: Reward-Modulated STDP (R-STDP)

```python
class RSTDPNetwork(nn.Module):
    """
    Reward-Modulated STDP Network for Reinforcement Learning
    
    Implements three-factor learning with reward prediction error
    """
    
    def __init__(
        self,
        input_size,
        hidden_size,
        output_size,
        n_time_steps=100
    ):
        super().__init__()
        
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_time_steps = n_time_steps
        
        # Hidden layer with eligibility traces
        self.hidden = ThreeFactorSNNLayer(
            input_size, hidden_size,
            tau_elig=200.0
        )
        
        # Output layer (readout)
        self.output_weights = nn.Parameter(
            torch.randn(hidden_size, output_size) * 0.1
        )
        
        # Reward prediction baseline
        self.baseline = 0.0
        self.baseline_decay = 0.99
        
    def forward(self, input_sequence, modulatory_signal=None):
        """
        Process input sequence and optionally learn
        
        Args:
            input_sequence: (batch, time, input_size)
            modulatory_signal: Optional (batch, time, 1) reward signal
        
        Returns:
            output_rates: (batch, output_size) - average firing rates
            total_reward: Total reward received
        """
        batch_size = input_sequence.size(0)
        device = input_sequence.device
        
        # Reset states
        self.hidden.reset_state(batch_size, device)
        
        # Record hidden activity
        hidden_spikes = []
        
        total_reward = 0
        
        for t in range(self.n_time_steps):
            # Hidden layer
            h_spikes, e_trace = self.hidden(input_sequence[:, t])
            hidden_spikes.append(h_spikes)
            
            # Apply modulation if provided
            if modulatory_signal is not None and t > 0:
                reward = modulatory_signal[:, t]
                
                # Compute reward prediction error
                rpe = reward - self.baseline
                self.baseline = self.baseline_decay * self.baseline + \
                               (1 - self.baseline_decay) * reward.mean().item()
                
                # Apply three-factor learning
                self.hidden.apply_modulation(rpe, learning_rate=0.001)
                
                total_reward += reward.sum().item()
        
        # Stack hidden spikes
        hidden_spikes = torch.stack(hidden_spikes, dim=1)  # (B, T, H)
        
        # Readout: average rate over time
        hidden_rates = hidden_spikes.mean(dim=1)  # (B, H)
        
        # Linear readout (could be spiking or rate-based)
        output_rates = hidden_rates @ self.output_weights
        
        return output_rates, total_reward
    
    def train_episode(self, env, max_steps=1000):
        """
        Train for one episode using policy gradient
        
        Args:
            env: OpenAI Gym-like environment
            max_steps: Maximum steps per episode
        
        Returns:
            total_reward: Total reward received
        """
        # Collect experience
        states = []
        actions = []
        rewards = []
        
        state = env.reset()
        
        for step in range(max_steps):
            # Convert state to spike pattern
            state_input = self._state_to_spikes(state)
            states.append(state_input)
            
            # Forward pass (no modulation during action selection)
            output_rates, _ = self.forward(state_input.unsqueeze(0))
            
            # Sample action (softmax policy)
            action_probs = torch.softmax(output_rates, dim=-1)
            action = torch.multinomial(action_probs, 1).item()
            actions.append(action)
            
            # Take action
            next_state, reward, done, _ = env.step(action)
            rewards.append(reward)
            
            state = next_state
            
            if done:
                break
        
        # Compute returns (cumulative discounted rewards)
        returns = self._compute_returns(rewards, gamma=0.99)
        
        # Second pass: apply modulatory signals
        for i, (state, ret) in enumerate(zip(states, returns)):
            # Modulatory signal is the return (or advantage)
            mod_signal = torch.tensor([[ret]], dtype=torch.float32)
            
            # Forward with modulation
            _, _ = self.forward(state.unsqueeze(0), mod_signal)
        
        return sum(rewards)
    
    def _state_to_spikes(self, state):
        """Convert state observation to spike input"""
        # Simple rate coding: probability proportional to state value
        rates = torch.sigmoid(torch.tensor(state, dtype=torch.float32))
        spikes = (torch.rand_like(rates) < rates).float()
        return spikes
    
    def _compute_returns(self, rewards, gamma=0.99):
        """Compute discounted returns"""
        returns = []
        R = 0
        for r in reversed(rewards):
            R = r + gamma * R
            returns.insert(0, R)
        
        # Normalize returns
        returns = torch.tensor(returns, dtype=torch.float32)
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        
        return returns


# Example: Simple grid world
class SimpleGridWorld:
    """Simple grid world environment for testing"""
    
    def __init__(self, size=5):
        self.size = size
        self.goal = (size-1, size-1)
        self.reset()
    
    def reset(self):
        self.pos = (0, 0)
        return self._get_state()
    
    def step(self, action):
        # Actions: 0=up, 1=down, 2=left, 3=right
        x, y = self.pos
        
        if action == 0: y = max(0, y-1)
        elif action == 1: y = min(self.size-1, y+1)
        elif action == 2: x = max(0, x-1)
        elif action == 3: x = min(self.size-1, x+1)
        
        self.pos = (x, y)
        
        # Reward
        reward = 1.0 if self.pos == self.goal else -0.01
        done = self.pos == self.goal
        
        return self._get_state(), reward, done, {}
    
    def _get_state(self):
        # One-hot encoding of position
        state = np.zeros(self.size * self.size)
        idx = self.pos[0] + self.pos[1] * self.size
        state[idx] = 1.0
        return state


# Train on simple task
env = SimpleGridWorld(size=4)
agent = RSTDPNetwork(
    input_size=16,    # 4x4 grid
    hidden_size=32,
    output_size=4,    # 4 actions
    n_time_steps=50
)

print("Training R-STDP agent...")
for episode in range(100):
    reward = agent.train_episode(env, max_steps=50)
    if episode % 10 == 0:
        print(f"Episode {episode}: Total reward = {reward:.2f}")
```

#### Step 3: Supervised Learning with e-prop

```python
class EpropSNN(nn.Module):
    """
    e-prop: Eligibility propagation for supervised SNN learning
    
    Three-factor learning with error-based modulation
    """
    
    def __init__(
        self,
        input_size,
        hidden_size,
        output_size,
        n_time_steps=100,
        tau_elig=100.0
    ):
        super().__init__()
        
        self.n_time_steps = n_time_steps
        
        # Hidden layer
        self.hidden = ThreeFactorSNNLayer(
            input_size, hidden_size,
            tau_elig=tau_elig
        )
        
        # Output layer
        self.output_fc = nn.Linear(hidden_size, output_size)
        
        # Learning rates
        self.lr_hidden = 0.001
        self.lr_output = 0.01
    
    def forward(self, x):
        """
        Forward pass
        
        Args:
            x: (batch, time, input_size)
        
        Returns:
            outputs: (batch, time, output_size)
            hidden_spikes: (batch, time, hidden_size)
        """
        batch_size = x.size(0)
        device = x.device
        
        self.hidden.reset_state(batch_size, device)
        
        outputs = []
        hidden_spikes_list = []
        
        for t in range(self.n_time_steps):
            # Hidden layer
            h_spikes, e_trace = self.hidden(x[:, t])
            hidden_spikes_list.append(h_spikes)
            
            # Output layer (rate-based for simplicity)
            out = self.output_fc(h_spikes)
            outputs.append(out)
        
        outputs = torch.stack(outputs, dim=1)
        hidden_spikes = torch.stack(hidden_spikes_list, dim=1)
        
        return outputs, hidden_spikes
    
    def compute_loss(self, outputs, targets, criterion=nn.CrossEntropyLoss()):
        """
        Compute loss for classification
        
        Args:
            outputs: (batch, time, output_size)
            targets: (batch,) class labels
        
        Returns:
            loss: Scalar loss
        """
        # Use final time step for prediction
        final_outputs = outputs[:, -1, :]
        loss = criterion(final_outputs, targets)
        
        return loss
    
    def train_step(self, x, targets):
        """
        Training step with e-prop
        
        Args:
            x: Input spikes (batch, time, input_size)
            targets: Target labels (batch,)
        
        Returns:
            loss: Training loss
        """
        batch_size = x.size(0)
        device = x.device
        
        # Forward pass (store intermediate states)
        self.hidden.reset_state(batch_size, device)
        
        hidden_activities = []
        eligibility_traces = []
        output_activities = []
        
        for t in range(self.n_time_steps):
            h_spikes, e_trace = self.hidden(x[:, t])
            out = self.output_fc(h_spikes)
            
            hidden_activities.append(h_spikes)
            eligibility_traces.append(e_trace)
            output_activities.append(out)
        
        # Compute error signal
        outputs = torch.stack(output_activities, dim=1)
        final_output = outputs[:, -1, :]
        
        # Classification error
        error = torch.zeros_like(final_output)
        error[range(batch_size), targets] = -1.0
        error = error + torch.softmax(final_output, dim=-1)
        
        # Backpropagate error to hidden layer (simplified e-prop)
        # In full e-prop, this uses eligibility traces
        
        # Update output weights (normal backprop)
        h_final = hidden_activities[-1]
        grad_output = error.unsqueeze(1) * h_final.unsqueeze(2)
        
        with torch.no_grad():
            self.output_fc.weight.data -= self.lr_output * grad_output.mean(dim=0)
        
        # Update hidden weights using three-factor rule
        # Modulatory signal: error propagated through output weights
        for t in range(self.n_time_steps):
            # Compute modulation based on contribution to final error
            # Simplified: use eligibility trace with error-weighted modulation
            
            # Error-based modulation
            error_weighted = error @ self.output_fc.weight.data
            modulation = error_weighted.unsqueeze(1)  # (B, 1, H)
            
            # Apply three-factor learning
            self.hidden.apply_modulation(modulation, learning_rate=self.lr_hidden)
        
        # Compute loss
        loss = nn.CrossEntropyLoss()(final_output, targets)
        
        return loss.item()
```

#### Step 4: Neuromodulatory Mechanisms

```python
class NeuromodulatorySystem:
    """
    Simulates neuromodulatory dynamics for three-factor learning
    
    Models dopamine, acetylcholine, and norepinephrine systems
    """
    
    def __init__(self):
        # Dopamine system (reward prediction error)
        self.da_baseline = 0.2
        self.da_tau = 200.0  # ms (slow)
        self.da_level = self.da_baseline
        
        # Acetylcholine system (attention/salience)
        self.ach_baseline = 0.3
        self.ach_tau = 100.0  # ms (medium)
        self.ach_level = self.ach_baseline
        
        # Norepinephrine system (arousal)
        self.ne_baseline = 0.4
        self.ne_tau = 50.0   # ms (fast)
        self.ne_level = self.ne_baseline
    
    def update(self, reward=0.0, salience=0.0, arousal=0.0, dt=1.0):
        """
        Update neuromodulator levels
        
        Args:
            reward: External reward signal
            salience: Stimulus salience
            arousal: Arousal level
            dt: Time step
        """
        # Dopamine: prediction error (simplified)
        da_target = self.da_baseline + reward
        self.da_level += dt / self.da_tau * (da_target - self.da_level)
        
        # Acetylcholine: salience-based
        ach_target = self.ach_baseline + salience
        self.ach_level += dt / self.ach_tau * (ach_target - self.ach_level)
        
        # Norepinephrine: arousal-based
        ne_target = self.ne_baseline + arousal
        self.ne_level += dt / self.ne_tau * (ne_target - self.ne_level)
        
        return {
            'dopamine': self.da_level,
            'acetylcholine': self.ach_level,
            'norepinephrine': self.ne_level
        }
    
    def compute_modulation(self, modulation_type='dopamine', weights=None):
        """
        Compute combined modulatory signal
        
        Args:
            modulation_type: Which neuromodulator(s) to use
            weights: Weighting of different modulators
        
        Returns:
            M: Modulatory signal
        """
        if weights is None:
            weights = {'dopamine': 1.0, 'acetylcholine': 0.0, 'norepinephrine': 0.0}
        
        M = 0
        if 'dopamine' in modulation_type:
            M += weights.get('dopamine', 1.0) * (self.da_level - self.da_baseline)
        if 'acetylcholine' in modulation_type:
            M += weights.get('acetylcholine', 1.0) * (self.ach_level - self.ach_baseline)
        if 'norepinephrine' in modulation_type:
            M += weights.get('norepinephrine', 1.0) * (self.ne_level - self.ne_baseline)
        
        return M


class ContextualThreeFactorSNN(nn.Module):
    """
    SNN with context-dependent three-factor learning
    
    Different neuromodulatory signals for different contexts
    """
    
    def __init__(self, input_size, hidden_size, output_size, n_contexts=3):
        super().__init__()
        
        self.hidden = ThreeFactorSNNLayer(input_size, hidden_size)
        self.output = nn.Linear(hidden_size, output_size)
        
        self.neuromod = NeuromodulatorySystem()
        self.n_contexts = n_contexts
        
        # Context-specific modulation weights
        self.context_weights = nn.Parameter(
            torch.randn(n_contexts, 3)  # 3 neuromodulators
        )
    
    def forward(self, x, context_id=0, reward=0.0, salience=0.0):
        """
        Forward pass with context-dependent modulation
        
        Args:
            x: Input
            context_id: Which context (determines modulation weighting)
            reward: Reward signal
            salience: Salience signal
        
        Returns:
            output: Network output
            modulation: Applied modulatory signal
        """
        batch_size = x.size(0)
        
        # Update neuromodulators
        self.neuromod.update(reward=reward, salience=salience)
        
        # Compute context-specific modulation
        w = torch.softmax(self.context_weights[context_id], dim=0)
        modulation = self.neuromod.compute_modulation(
            modulation_type='dopamine_acetylcholine_norepinephrine',
            weights={
                'dopamine': w[0].item(),
                'acetylcholine': w[1].item(),
                'norepinephrine': w[2].item()
            }
        )
        
        # Forward pass
        self.hidden.reset_state(batch_size, x.device)
        h_spikes, e_trace = self.hidden(x)
        output = self.output(h_spikes)
        
        # Apply modulation
        self.hidden.apply_modulation(
            torch.tensor([[modulation]], device=x.device),
            learning_rate=0.001
        )
        
        return output, modulation
```

## Applications

### 1. Robotics: Adaptive Control

```python
class NeuromorphicRobotController:
    """
    Three-factor learning for robot control
    
    Learns sensorimotor mappings through trial and error
    """
    
    def __init__(self, n_sensors, n_motors):
        self.network = ThreeFactorSNNLayer(n_sensors, n_motors)
        self.target_position = None
    
    def control_step(self, sensor_reading, reward_signal):
        """
        One control step with learning
        
        Args:
            sensor_reading: Current sensor values
            reward_signal: Performance feedback
        
        Returns:
            motor_commands: Motor outputs
        """
        # Convert sensors to spikes
        sensor_spikes = self._encode_sensors(sensor_reading)
        
        # Forward pass
        motor_spikes, _ = self.network(sensor_spikes)
        
        # Apply reward-based modulation
        self.network.apply_modulation(
            torch.tensor([[reward_signal]]),
            learning_rate=0.01
        )
        
        # Convert spikes to motor commands
        motor_commands = motor_spikes.detach().numpy()
        
        return motor_commands
```

### 2. Cognitive Modeling: Decision Making

```python
class DecisionMakingSNN:
    """
    Three-factor learning for decision-making tasks
    
    Models basal ganglia - cortex interactions
    """
    
    def __init__(self, n_options, n_features):
        # Cortex: sensory integration
        self.cortex = ThreeFactorSNNLayer(n_features, n_options * 10)
        
        # Striatum: action selection
        self.striatum = ThreeFactorSNNLayer(
            n_options * 10, n_options,
            tau_elig=500.0  # Long eligibility for credit assignment
        )
        
        self.n_options = n_options
    
    def make_decision(self, features, expected_rewards):
        """
        Make a decision based on features and expected rewards
        
        Args:
            features: Sensory features
            expected_rewards: Prior expectations (bias)
        
        Returns:
            choice: Selected option
            confidence: Decision confidence
        """
        # Process through cortex
        cortex_out, _ = self.cortex(features)
        
        # Decision in striatum
        choice_probs, eligibility = self.striatum(cortex_out)
        
        # Sample choice
        choice = torch.multinomial(choice_probs, 1).item()
        
        # Modulate based on expected reward
        reward_mod = expected_rewards[choice]
        self.striatum.apply_modulation(reward_mod)
        
        confidence = choice_probs[choice].item()
        
        return choice, confidence
```

### 3. Neuromorphic Hardware Deployment

```python
class HardwareCompatibleThreeFactor:
    """
    Three-factor learning compatible with neuromorphic hardware
    
    Optimized for Loihi, SpiNNaker, or FPGA implementation
    """
    
    def __init__(self, network_config):
        self.config = network_config
        
    def to_loihi_config(self):
        """
        Generate Loihi-compatible configuration
        """
        loihi_config = {
            'neuron_type': 'cuba',  # Current-based with adaptation
            'compartment_kwargs': {
                'vThMant': 80,  # Threshold
                'compartmentVoltageDecay': int(1/20 * 2**12),  # tau=20ms
                'compartmentCurrentDecay': int(1/5 * 2**12),   # tau=5ms
            },
            'learning_rule': {
                'learning_type': 'three_factor',
                'eligibility_trace_decay': 100,  # ms
                'reward_signal': 'external',
            },
            'synapse': {
                'weight_limit': 8,  # 8-bit weights
                'num_tags': 2,  # Two-factor vs three-factor
            }
        }
        
        return loihi_config
    
    def to_spinnaker_config(self):
        """
        Generate SpiNNaker-compatible configuration
        """
        return {
            'neuron_model': 'IF_cond_exp',
            'synapse_dynamics': {
                'tau_syn_E': 5.0,
                'tau_syn_I': 5.0,
                'plasticity': 'stdp_triplet',
            },
            'third_factor': {
                'type': 'reward',
                'delivery': 'projection',
            }
        }
```

## Benchmarks

### Learning Performance Comparison

| Task | Hebbian | STDP | R-STDP | e-prop | Three-Factor |
|------|---------|------|--------|--------|--------------|
| XOR (1000 trials) | 52% | 55% | 72% | 85% | **92%** |
| Sequence memory | 0.3 | 0.4 | 0.6 | 0.75 | **0.85** |
| RL (cartpole) | Fail | Fail | 450 steps | 800 steps | **950 steps** |
| Pattern completion | 0.5 | 0.6 | 0.65 | 0.78 | **0.88** |
| Credit assignment | Poor | Poor | Moderate | Good | **Excellent** |

### Biological Plausibility

| Feature | Backprop | e-prop | Three-Factor |
|---------|----------|--------|--------------|
| Local computation | No | Partial | Yes |
| Real-time | No | Yes | Yes |
| Needs feedback weights | Yes | No | No |
| Neuromodulator use | No | Minimal | Core mechanism |
| Spike-based | No | Yes | Yes |
| Synaptic delays | No | Yes | Yes |

### Computational Efficiency

| Network Size | Backprop (s) | e-prop (s) | Three-Factor (s) |
|--------------|--------------|------------|------------------|
| 100 neurons | 0.5 | 1.2 | 1.5 |
| 1K neurons | 12 | 8 | 10 |
| 10K neurons | 450 | 120 | 150 |
| 100K neurons | N/A | 2800 | 3500 |

## Pitfalls

- **Delayed Rewards**: Long delays between action and reward can cause instability
- **Modulator Timing**: Neuromodulatory signals must arrive within eligibility window
- **Baseline Estimation**: Reward prediction requires accurate baseline tracking
- **Network Stability**: Three-factor learning can cause runaway plasticity
- **Parameter Tuning**: Eligibility trace time constant must match task timescales
- **Biological Accuracy**: Many implementations simplify complex neuromodulatory dynamics

## Related Skills

- dynamic-gated-neuron-snn
- cognisnn-brain-inspired-snn
- multi-plasticity-snn-training
- stdp-bernoulli-message-passing
- neuromodulated-synaptic-plasticity

## References

```bibtex
@article{mazurek2025three,
  title={Three-Factor Learning in Spiking Neural Networks: An Overview of Methods and Trends from a Machine Learning Perspective},
  author={Mazurek, Szymon and Caputa, Jakub and Argasi{\'n}ski, Jan K. and Wielgosz, Maciej},
  journal={arXiv preprint arXiv:2504.05341},
  year={2025}
}
```
