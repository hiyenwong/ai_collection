---
name: ember-autonomous-cognitive-behaviour-learned-spiking
description: "EMBER: Autonomous cognitive behaviour from learned spiking neural network dynamics. Self-organizing SNN agents with intrinsic motivation, curiosity, and goal-directed behavior emerging from plastic recurrent connectivity without external reward shaping. Keywords: autonomous cognition, intrinsic motivation, SNN agents, emergent behavior, self-organization, curiosity-driven learning."
---

# EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics

> EMBER (Emergent Mind Through Biological Event-driven Responses) - self-organizing autonomous agents where complex cognitive behaviors emerge from learned spiking neural network dynamics through intrinsic motivation, curiosity, and plastic recurrent connectivity without external reward engineering.

## Metadata
- **Source**: arXiv:2604.12167v1
- **Authors**: [Authors from paper]
- **Published**: 2026-04-14
- **Category**: Neural and Evolutionary Computing (cs.NE), Artificial Intelligence (cs.AI)

## Core Methodology

### Key Innovation
EMBER presents a paradigm shift from **reward-engineered** to **self-organizing** autonomous agents. Rather than designing reward functions for specific behaviors, EMBER agents develop cognitive capabilities through:
- **Intrinsic Motivation**: Curiosity, novelty-seeking, and competence drives
- **Plastic Recurrent Connectivity**: Self-organizing RNN/SNN with local learning rules
- **Emergent Goal-Directedness**: Goals arise from internal state rather than external specification

### Technical Framework

**1. Intrinsic Motivation Architecture**

**Novelty-Based Motivation:**
```
R_novelty(s) = -log p(s | history)
```
High novelty reward for unexpected states.

**Competence-Based Motivation:**
```
R_competence(s, a) = ||s_target - s_actual|| - ||s_target - s_predicted||
```
Reward for successfully controlling outcomes.

**Information Gain Motivation:**
```
R_info = H(s_future) - H(s_future | a)
```
Reward for actions that reduce uncertainty.

**2. Spiking Recurrent Network with Plasticity**

**Recurrent SNN Structure:**
- Input neurons: Sensory encoding
- Recurrent excitatory pool: Working memory, sequence processing
- Inhibitory interneurons: Gain control, competition
- Motor output: Action selection

**Local Learning Rules:**
- Hebbian plasticity: "Neurons that fire together wire together"
- Homeostatic regulation: Maintains firing rate stability
- Meta-plasticity: Learning rate modulation by success

**3. Self-Organized Behavior Generation**

**Goal Emergence:**
- Goals as attractor states in recurrent dynamics
- No explicit goal encoding - goals are high-value internal states
- Goal switching through attractor basin hopping

**Action Selection:**
- Intrinsic motivation guides exploration
- Learned predictions guide exploitation
- Balance through uncertainty-weighted sampling

## Key Findings

### 1. Emergent Cognitive Behaviors
- **Foraging**: Agents self-organize efficient resource gathering
- **Tool Use**: Spontaneous discovery of environmental affordances
- **Social Behaviors**: Communication and coordination in multi-agent scenarios
- **Planning**: Multi-step action sequences emerge from predictive dynamics

### 2. Robustness to Environment Changes
- Adapts to novel environments without retraining
- Generalizes across task domains
- Resilient to sensor/actuator failures

### 3. Scalability
- Behavior complexity scales with network size
- Modular architecture enables hierarchical cognition
- Parallel exploration in multi-agent settings

## Implementation Guide

### Prerequisites
- Python 3.8+
- snnTorch or Norse for SNN simulation
- Gymnasium/OpenAI Gym for environments
- PyTorch for network components

### Step-by-Step Implementation

**Step 1: Intrinsic Motivation Module**
```python
import torch
import torch.nn as nn
import numpy as np

class IntrinsicMotivationModule:
    """
    Compute intrinsic rewards for autonomous exploration
    """
    def __init__(self, state_dim, memory_size=10000, novelty_decay=0.99):
        self.state_dim = state_dim
        self.memory = []  # Buffer of experienced states
        self.memory_size = memory_size
        self.novelty_decay = novelty_decay
        
        # Forward model for prediction errors
        self.forward_model = self._build_forward_model()
        
        # State distribution model (for novelty)
        self.state_density = OnlineKernelDensity(state_dim)
    
    def _build_forward_model(self):
        """Build forward dynamics model"""
        return nn.Sequential(
            nn.Linear(self.state_dim + self.action_dim, 256),
            nn.ReLU(),
            nn.Linear(256, self.state_dim)
        )
    
    def compute_novelty(self, state):
        """
        Compute novelty reward as negative log likelihood
        
        Args:
            state: Current state (batch, state_dim)
        
        Returns:
            novelty: Scalar novelty score
        """
        # Estimate probability density
        prob = self.state_density.estimate(state)
        novelty = -torch.log(prob + 1e-10)
        
        return novelty
    
    def compute_prediction_error(self, state, action, next_state):
        """
        Compute prediction error for competence motivation
        
        Args:
            state: Current state
            action: Action taken
            next_state: Resulting state
        
        Returns:
            error: Prediction error (higher = more learning opportunity)
        """
        # Predict next state
        input_sa = torch.cat([state, action], dim=-1)
        predicted_next = self.forward_model(input_sa)
        
        # Prediction error
        error = torch.mean((next_state - predicted_next) ** 2, dim=-1)
        
        return error
    
    def compute_information_gain(self, state, action):
        """
        Estimate information gain from taking action
        
        Args:
            state: Current state
            action: Candidate action
        
        Returns:
            info_gain: Expected information gain
        """
        # Monte Carlo estimate of entropy reduction
        n_samples = 10
        entropies = []
        
        for _ in range(n_samples):
            # Sample predicted next states
            next_state = self.forward_model(torch.cat([state, action]))
            next_state += torch.randn_like(next_state) * 0.1  # Add noise
            
            # Estimate future entropy
            prob = self.state_density.estimate(next_state)
            entropy = -torch.log(prob + 1e-10)
            entropies.append(entropy)
        
        # Expected information gain
        info_gain = torch.mean(torch.stack(entropies))
        
        return info_gain
    
    def compute_intrinsic_reward(self, state, action, next_state):
        """
        Compute total intrinsic reward
        
        Args:
            state: Current state
            action: Action taken
            next_state: Next state
        
        Returns:
            reward: Intrinsic reward scalar
            components: Dict of reward components
        """
        # Novelty
        novelty = self.compute_novelty(next_state)
        
        # Prediction error (competence)
        pred_error = self.compute_prediction_error(state, action, next_state)
        
        # Information gain
        info_gain = self.compute_information_gain(state, action)
        
        # Combine (weights can be tuned)
        total_reward = novelty + 0.5 * pred_error + 0.3 * info_gain
        
        components = {
            'novelty': novelty.item(),
            'prediction_error': pred_error.item(),
            'information_gain': info_gain.item()
        }
        
        # Update memory
        self.update_memory(next_state)
        
        return total_reward, components
    
    def update_memory(self, state):
        """Update state memory"""
        self.memory.append(state.detach().cpu())
        if len(self.memory) > self.memory_size:
            self.memory.pop(0)
        
        # Update density estimator
        self.state_density.update(state)

class OnlineKernelDensity:
    """
    Online kernel density estimator for novelty computation
    """
    def __init__(self, dim, bandwidth=0.1):
        self.dim = dim
        self.bandwidth = bandwidth
        self.samples = []
        self.max_samples = 5000
    
    def update(self, sample):
        """Add new sample"""
        self.samples.append(sample.detach().cpu().numpy())
        if len(self.samples) > self.max_samples:
            self.samples = self.samples[-self.max_samples:]
    
    def estimate(self, query):
        """
        Estimate probability density at query point
        
        Args:
            query: (batch, dim) query points
        
        Returns:
            prob: (batch,) estimated probabilities
        """
        if len(self.samples) < 100:
            return torch.ones(query.shape[0], device=query.device) * 0.5
        
        query_np = query.detach().cpu().numpy()
        samples_np = np.array(self.samples)
        
        # Kernel density estimation
        probs = []
        for q in query_np:
            distances = np.linalg.norm(samples_np - q, axis=1)
            kernel_vals = np.exp(-distances**2 / (2 * self.bandwidth**2))
            prob = np.mean(kernel_vals)
            probs.append(prob)
        
        return torch.tensor(probs, device=query.device, dtype=torch.float32)
```

**Step 2: Recurrent SNN with Plastic Connectivity**
```python
import snntorch as snn
from snntorch import surrogate

class PlasticRecurrentSNN(nn.Module):
    """
    Recurrent SNN with biologically plausible plasticity
    """
    def __init__(self, input_size, hidden_size, output_size, 
                 recurrent_size=256, beta=0.9):
        super().__init__()
        
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.recurrent_size = recurrent_size
        
        # Input encoding
        self.input_encoder = nn.Linear(input_size, recurrent_size)
        
        # Recurrent layer with excitatory and inhibitory populations
        self.rec_exc = snn.Leaky(beta=beta, init_hidden=True)
        self.rec_inh = snn.Leaky(beta=beta, init_hidden=True)
        
        # Recurrent weights (plastic)
        self.w_ee = nn.Parameter(torch.randn(recurrent_size, recurrent_size) * 0.01)
        self.w_ei = nn.Parameter(torch.randn(recurrent_size, recurrent_size) * 0.01)
        self.w_ie = nn.Parameter(torch.randn(recurrent_size, recurrent_size) * 0.01)
        
        # Output readout
        self.readout = nn.Linear(recurrent_size, output_size)
        
        # Surrogate gradient
        self.surrogate = surrogate.fast_sigmoid(slope=25)
        
        # Plasticity parameters
        self.A_plus = 0.01
        self.A_minus = 0.01
        self.tau_stdp = 20.0
    
    def forward(self, x, time_steps=100, return_spikes=True):
        """
        Forward pass through recurrent SNN
        
        Args:
            x: Input (batch, input_features)
            time_steps: Number of simulation steps
            return_spikes: Return full spike trains
        
        Returns:
            output: Action logits
            spikes: Spike trains (if return_spikes=True)
        """
        batch_size = x.shape[0]
        
        # Encode input to initial activity
        input_current = self.input_encoder(x)
        
        # Initialize states
        mem_exc = self.rec_exc.init_leaky()
        mem_inh = self.rec_inh.init_leaky()
        
        # Activity recording
        spikes_exc = []
        spikes_inh = []
        
        for t in range(time_steps):
            # Recurrent input
            if t == 0:
                rec_input_exc = input_current
            else:
                prev_exc = spikes_exc[-1] if spikes_exc else torch.zeros_like(mem_exc)
                prev_inh = spikes_inh[-1] if spikes_inh else torch.zeros_like(mem_inh)
                
                rec_input_exc = (torch.matmul(prev_exc, self.w_ee.t()) - 
                                torch.matmul(prev_inh, self.w_ie.t()) +
                                input_current)
            
            # Excitatory population
            spk_exc, mem_exc = self.rec_exc(rec_input_exc, mem_exc)
            
            # Inhibitory population (driven by excitatory activity)
            inh_input = torch.matmul(spk_exc, self.w_ei.t())
            spk_inh, mem_inh = self.rec_inh(inh_input, mem_inh)
            
            spikes_exc.append(spk_exc)
            spikes_inh.append(spk_inh)
        
        # Stack spikes
        spike_trains_exc = torch.stack(spikes_exc, dim=1)  # (batch, time, neurons)
        spike_trains_inh = torch.stack(spikes_inh, dim=1)
        
        # Readout (rate coding)
        rates = spike_trains_exc.mean(dim=1)  # (batch, neurons)
        output = self.readout(rates)
        
        if return_spikes:
            return output, (spike_trains_exc, spike_trains_inh)
        return output
    
    def apply_stdp(self, spike_trains, reward_signal):
        """
        Apply reward-modulated STDP to recurrent weights
        
        Args:
            spike_trains: (batch, time, neurons) spike trains
            reward_signal: Scalar reward value
        """
        batch_size, time_steps, n_neurons = spike_trains.shape
        
        # Compute STDP update for each pair
        with torch.no_grad():
            for b in range(batch_size):
                for i in range(n_neurons):
                    for j in range(n_neurons):
                        if i == j:
                            continue
                        
                        # Get spike times
                        times_i = torch.where(spike_trains[b, :, i] > 0)[0].float()
                        times_j = torch.where(spike_trains[b, :, j] > 0)[0].float()
                        
                        if len(times_i) == 0 or len(times_j) == 0:
                            continue
                        
                        # Compute STDP window
                        delta_t = times_i.unsqueeze(1) - times_j.unsqueeze(0)
                        
                        # STDP kernel
                        if delta_t > 0:
                            dw = self.A_plus * torch.exp(-delta_t / self.tau_stdp)
                        else:
                            dw = -self.A_minus * torch.exp(delta_t / self.tau_stdp)
                        
                        # Apply reward modulation
                        self.w_ee.data[i, j] += reward_signal * dw.mean()
            
            # Keep weights positive
            self.w_ee.data = torch.clamp(self.w_ee.data, min=0)
            self.w_ei.data = torch.clamp(self.w_ei.data, min=0)
            self.w_ie.data = torch.clamp(self.w_ie.data, min=0)
```

**Step 3: Autonomous Agent**
```python
class EMBERAgent:
    """
    EMBER autonomous agent with self-organized behavior
    """
    def __init__(self, state_dim, action_dim, env, 
                 network_size=256, learning_rate=0.001):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.env = env
        
        # Intrinsic motivation
        self.motivation = IntrinsicMotivationModule(state_dim)
        
        # Spiking network
        self.network = PlasticRecurrentSNN(
            state_dim, network_size, action_dim, network_size
        )
        
        # Optimizer for network weights
        self.optimizer = torch.optim.Adam(
            self.network.parameters(), lr=learning_rate
        )
        
        # Experience buffer
        self.buffer = []
        self.buffer_size = 10000
    
    def select_action(self, state, epsilon=0.1):
        """
        Select action using network output
        
        Args:
            state: Current state
            epsilon: Exploration rate
        
        Returns:
            action: Selected action
        """
        state_t = torch.FloatTensor(state).unsqueeze(0)
        
        if np.random.random() < epsilon:
            # Random exploration
            return self.env.action_space.sample()
        
        with torch.no_grad():
            action_logits, _ = self.network(state_t)
            action_probs = torch.softmax(action_logits, dim=-1)
            action = torch.multinomial(action_probs, 1).item()
        
        return action
    
    def train_step(self, batch_size=32):
        """
        Training step with intrinsic motivation
        
        Args:
            batch_size: Number of transitions to sample
        
        Returns:
            loss: Training loss
        """
        if len(self.buffer) < batch_size:
            return None
        
        # Sample batch
        batch = np.random.choice(self.buffer, batch_size, replace=False)
        
        states = torch.FloatTensor([t[0] for t in batch])
        actions = torch.LongTensor([t[1] for t in batch])
        next_states = torch.FloatTensor([t[2] for t in batch])
        
        # Compute intrinsic rewards
        intrinsic_rewards = []
        for s, a, ns in zip(states, actions, next_states):
            a_onehot = torch.zeros(self.action_dim)
            a_onehot[a] = 1
            r, _ = self.motivation.compute_intrinsic_reward(
                s.unsqueeze(0), a_onehot.unsqueeze(0), ns.unsqueeze(0)
            )
            intrinsic_rewards.append(r)
        
        intrinsic_rewards = torch.stack(intrinsic_rewards)
        
        # Forward pass
        action_logits, (spikes_exc, spikes_inh) = self.network(states)
        
        # Policy gradient loss
        action_probs = torch.softmax(action_logits, dim=-1)
        selected_probs = action_probs.gather(1, actions.unsqueeze(1))
        
        loss = -(torch.log(selected_probs) * intrinsic_rewards.detach()).mean()
        
        # Backward pass
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        # Apply STDP with intrinsic reward
        self.network.apply_stdp(spikes_exc, intrinsic_rewards.mean().item())
        
        return loss.item()
    
    def run_episode(self, max_steps=1000, render=False):
        """
        Run one episode
        
        Args:
            max_steps: Maximum episode length
            render: Whether to render environment
        
        Returns:
            total_reward: Sum of intrinsic rewards
            episode_length: Number of steps
        """
        state = self.env.reset()
        total_intrinsic_reward = 0
        
        for step in range(max_steps):
            if render:
                self.env.render()
            
            # Select action
            action = self.select_action(state)
            
            # Take action
            next_state, env_reward, done, info = self.env.step(action)
            
            # Compute intrinsic reward
            state_t = torch.FloatTensor(state).unsqueeze(0)
            next_state_t = torch.FloatTensor(next_state).unsqueeze(0)
            action_t = torch.zeros(self.action_dim)
            action_t[action] = 1
            
            intrinsic_r, components = self.motivation.compute_intrinsic_reward(
                state_t, action_t.unsqueeze(0), next_state_t
            )
            
            total_intrinsic_reward += intrinsic_r.item()
            
            # Store transition
            self.buffer.append((state, action, next_state))
            if len(self.buffer) > self.buffer_size:
                self.buffer.pop(0)
            
            # Train
            if step % 4 == 0:
                self.train_step()
            
            state = next_state
            
            if done:
                break
        
        return total_intrinsic_reward, step + 1
    
    def train(self, n_episodes=1000, eval_interval=100):
        """
        Train agent for multiple episodes
        
        Args:
            n_episodes: Number of training episodes
            eval_interval: Episodes between evaluations
        """
        for episode in range(n_episodes):
            # Training episode
            reward, length = self.run_episode()
            
            if episode % 10 == 0:
                print(f"Episode {episode}: Intrinsic Reward={reward:.2f}, Length={length}")
            
            # Evaluation
            if episode % eval_interval == 0:
                eval_reward, eval_length = self.evaluate()
                print(f"  [Eval] Reward={eval_reward:.2f}, Length={eval_length}")
    
    def evaluate(self, n_episodes=5):
        """
        Evaluate agent performance
        
        Args:
            n_episodes: Number of evaluation episodes
        
        Returns:
            avg_reward: Average intrinsic reward
            avg_length: Average episode length
        """
        rewards = []
        lengths = []
        
        for _ in range(n_episodes):
            r, l = self.run_episode(render=False)
            rewards.append(r)
            lengths.append(l)
        
        return np.mean(rewards), np.mean(lengths)
```

## Applications

### 1. Autonomous Robotics
- Self-motivated exploration robots
- Adaptive navigation without task specification
- Lifelong learning agents

### 2. Artificial Life Simulation
- Virtual creatures with emergent behavior
- Ecosystems with self-organized interactions
- Evolutionary robotics

### 3. Cognitive Neuroscience Models
- Study of intrinsic motivation in biological systems
- Computational models of curiosity
- Goal-directed behavior emergence

### 4. Educational AI
- Self-motivated learning systems
- Adaptive tutoring agents
- Curiosity-driven knowledge acquisition

## Pitfalls

### 1. Exploration-Exploitation Balance
- **Issue**: Pure intrinsic motivation can lead to endless exploration
- **Mitigation**: Gradually shift to external rewards or competence-based goals

### 2. Emergence Unpredictability
- **Issue**: Behaviors may not align with designer intentions
- **Mitigation**: Constrain environment, provide safe exploration spaces

### 3. Computational Cost
- **Issue**: Kernel density estimation is expensive
- **Mitigation**: Use approximate methods, limit memory size

### 4. Local Minima in Motivation
- **Issue**: Agent may get stuck in locally interesting patterns
- **Mitigation**: Multiple motivation sources, meta-learning

## Related Skills
- intrinsic-motivation-rl
- self-organizing-transformer
- neuromodulated-synaptic-plasticity
- brain-inspired-snn-pattern-analysis

## References
```bibtex
@article{2026ember,
  title={EMBER: Autonomous Cognitive Behaviour from Learned Spiking Neural Network Dynamics},
  journal={arXiv preprint arXiv:2604.12167},
  year={2026}
}
```
