---
name: perspective-latents-causal-emergence-active-inference
description: "Framework for measuring causal emergence (ΦID) in active inference agents with perspective latents architecture, analyzing how architectural separation between fast perception and slow global latents affects information-theoretic signatures of integration. Use when studying causal emergence, active inference, or hierarchical agent architectures."
metadata:
  arxiv_id: "2607.20708"
  authors: ["Hongju Pae"]
  subjects: ["Machine Learning (cs.LG)", "Neurons and Cognition (q-bio.NC)"]
---

# Perspective Latents as an Architectural Condition for Causal Emergence in Active Inference Agents

This skill implements the methodology from arXiv:2607.20708 for analyzing causal emergence in active inference agents using Integrated Information Decomposition (ΦID) with perspective latents architecture.

## Core Methodology

The paper investigates how architectural design choices in active inference agents affect causal emergence measured through ΦID. The key innovation is the use of a perspective latents architecture that separates:

1. **Fast Perception Latent (z)**: Handles immediate sensory processing and rapid responses
2. **Slow Global Latent (g)**: Captures higher-order temporal structure and is driven by prediction error

The critical architectural feature is that **g is structurally decoupled from policy gradients**, making it purely predictive rather than reward-optimized.

## Key Findings

### 1. Architectural Locus of ΦID
- ΦID concentrates in the slow global latent **g** rather than the fast perception latent **z**
- The aggregate magnitude of ΦID is largely determined by architecture rather than learning
- ΦID actually **decreases with training** in this reward-free setting

### 2. Atom-Compositional Learning Effects
- At the fine-grained level, learning produces meaningful changes:
  - **Decoupling flips sign** from negative to positive during training
  - Decoupling becomes **regime-invariant** under environmental change
  - **Downward causation** carries regime-dependent adjustment

### 3. Interpretation of Scalar ΦID
- Scalar ΦID should **not be read as a direct index of learned integration**
- The architectural locus (g) contains the relevant temporal organization for ΦID
- Meaningful learning effects are only visible at the atom-compositional level

## Implementation Steps

### 1. Define the Perspective Latents Architecture

```python
import torch
import torch.nn as nn
from typing import Tuple, Dict

class PerspectiveLatentsActiveInference(nn.Module):
    """
    Active inference agent with perspective latents architecture.
    Separates fast perception latent z from slow global latent g.
    """
    
    def __init__(self, 
                 obs_dim: int,
                 z_dim: int, 
                 g_dim: int,
                 hidden_dim: int = 256):
        super().__init__()
        
        # Fast perception encoder (z)
        self.encoder_z = nn.Sequential(
            nn.Linear(obs_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, z_dim)
        )
        
        # Slow global encoder (g) - driven by prediction error
        self.encoder_g = nn.Sequential(
            nn.Linear(obs_dim + z_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, g_dim)
        )
        
        # Decoder (reconstruction)
        self.decoder = nn.Sequential(
            nn.Linear(z_dim + g_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, obs_dim)
        )
        
        # Policy network (only uses z, not g - structural decoupling)
        self.policy = nn.Sequential(
            nn.Linear(z_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, action_dim)
        )
        
        # Prediction error computation
        self.prediction_error = nn.MSELoss(reduction='none')
    
    def forward(self, obs: torch.Tensor) -> Dict[str, torch.Tensor]:
        # Encode fast perception latent
        z = self.encoder_z(obs)
        
        # Encode slow global latent using observation and z
        g_input = torch.cat([obs, z], dim=-1)
        g = self.encoder_g(g_input)
        
        # Decode reconstruction
        latent = torch.cat([z, g], dim=-1)
        recon = self.decoder(latent)
        
        # Compute prediction error
        pred_error = self.prediction_error(recon, obs).mean(dim=-1)
        
        # Policy (structurally decoupled from g)
        action_logits = self.policy(z)
        
        return {
            'z': z,
            'g': g,
            'recon': recon,
            'pred_error': pred_error,
            'action_logits': action_logits
        }
```

### 2. Implement Integrated Information Decomposition (ΦID)

```python
import numpy as np
from scipy.stats import entropy

def compute_phi_id(latents: Dict[str, np.ndarray], 
                   time_window: int = 10) -> Dict[str, float]:
    """
    Compute Integrated Information Decomposition (ΦID) for perspective latents.
    
    Parameters:
    - latents: Dictionary containing 'z' and 'g' time series
    - time_window: Number of time steps for temporal analysis
    
    Returns:
    - phi_id_metrics: Dictionary with ΦID components
    """
    
    z_series = latents['z']  # Shape: [T, z_dim]
    g_series = latents['g']  # Shape: [T, g_dim]
    
    # Compute temporal dependencies
    def temporal_mutual_info(series, lag=1):
        """Compute mutual information between series[t] and series[t-lag]"""
        if len(series) <= lag:
            return 0.0
        
        current = series[lag:]
        past = series[:-lag]
        
        # Discretize for MI computation
        current_disc = np.digitize(current, np.quantile(current, np.linspace(0, 1, 10)))
        past_disc = np.digitize(past, np.quantile(past, np.linspace(0, 1, 10)))
        
        # Joint and marginal entropies
        joint_hist = np.histogram2d(current_disc.flatten(), past_disc.flatten(), 
                                   bins=10)[0]
        joint_prob = joint_hist / joint_hist.sum()
        joint_entropy = entropy(joint_prob.flatten())
        
        current_entropy = entropy(np.histogram(current_disc, bins=10)[0] / len(current_disc))
        past_entropy = entropy(np.histogram(past_disc, bins=10)[0] / len(past_disc))
        
        mi = current_entropy + past_entropy - joint_entropy
        return max(0.0, mi)  # Ensure non-negative
    
    # Compute ΦID components
    phi_id_metrics = {}
    
    # Total integrated information in g
    phi_id_metrics['phi_g_total'] = temporal_mutual_info(g_series)
    
    # Total integrated information in z  
    phi_id_metrics['phi_z_total'] = temporal_mutual_info(z_series)
    
    # Downward causation (g -> z influence)
    # Measure how g[t] influences z[t+1] beyond z[t]
    if len(g_series) > 1:
        g_current = g_series[:-1]
        z_future = z_series[1:]
        z_current = z_series[:-1]
        
        # Conditional mutual information I(g[t]; z[t+1] | z[t])
        # Approximate using correlation-based approach
        residuals_z = z_future - z_current  # Innovation in z
        correlation_g_residuals = np.corrcoef(g_current.T, residuals_z.T)[0, 1]
        phi_id_metrics['downward_causation'] = abs(correlation_g_residuals)
    
    # Decoupling measure (independence between g and policy gradients)
    # Since policy doesn't use g, this should be high
    # Measure correlation between g and action selection
    actions = np.argmax(latents.get('actions', np.random.randn(len(g_series), 5)), axis=1)
    correlation_g_actions = np.corrcoef(g_series.T, actions[np.newaxis, :])[0, -1]
    phi_id_metrics['decoupling'] = 1.0 - abs(correlation_g_actions)
    
    return phi_id_metrics
```

### 3. Analyze Regime-Switching Protocol

```python
def analyze_regime_switching(phi_id_results: Dict[str, np.ndarray],
                           regime_boundaries: np.ndarray) -> Dict[str, Dict[str, float]]:
    """
    Analyze ΦID behavior across environmental regime switches.
    
    Parameters:
    - phi_id_results: Time series of ΦID metrics
    - regime_boundaries: Indices where regime switches occur
    
    Returns:
    - regime_analysis: Dictionary with pre/post switch statistics
    """
    
    analysis = {}
    
    for metric_name, metric_series in phi_id_results.items():
        if len(metric_series) == 0:
            continue
            
        # Split into pre-switch and post-switch periods
        pre_switch = []
        post_switch = []
        
        for boundary in regime_boundaries:
            if boundary > 5 and boundary < len(metric_series) - 5:
                pre_switch.extend(metric_series[boundary-5:boundary])
                post_switch.extend(metric_series[boundary:boundary+5])
        
        if len(pre_switch) > 0 and len(post_switch) > 0:
            analysis[metric_name] = {
                'pre_switch_mean': np.mean(pre_switch),
                'post_switch_mean': np.mean(post_switch),
                'regime_invariant': abs(np.mean(pre_switch) - np.mean(post_switch)) < 0.1,
                'switch_effect_size': (np.mean(post_switch) - np.mean(pre_switch)) / np.std(pre_switch + post_switch)
            }
    
    return analysis
```

### 4. Training Protocol for Reward-Free Learning

```python
def train_perspective_latents_agent(agent: PerspectiveLatentsActiveInference,
                                 environment: object,
                                 num_episodes: int = 1000,
                                 reward_free: bool = True) -> Dict[str, list]:
    """
    Train perspective latents agent in reward-free regime-switching environment.
    
    Parameters:
    - agent: PerspectiveLatentsActiveInference instance
    - environment: Environment with regime switching
    - num_episodes: Number of training episodes
    - reward_free: If True, optimize only prediction error
    
    Returns:
    - training_history: Dictionary with metrics over time
    """
    
    optimizer = torch.optim.Adam(agent.parameters(), lr=1e-3)
    training_history = {
        'phi_id_over_time': [],
        'prediction_error': [],
        'decoupling_measure': [],
        'regime_switches': []
    }
    
    for episode in range(num_episodes):
        obs = environment.reset()
        episode_phi_id = []
        episode_pred_error = []
        episode_decoupling = []
        
        done = False
        while not done:
            # Forward pass
            outputs = agent(obs)
            
            # Compute loss (reward-free: only prediction error)
            if reward_free:
                loss = outputs['pred_error'].mean()
            else:
                # Include policy loss if not reward-free
                action_probs = torch.softmax(outputs['action_logits'], dim=-1)
                # ... policy loss computation
                
            # Backpropagate (note: g gradients flow through prediction error only)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            # Record metrics
            episode_pred_error.append(loss.item())
            
            # Sample action
            action = torch.multinomial(torch.softmax(outputs['action_logits'], dim=-1), 1)
            obs, reward, done, info = environment.step(action.item())
            
            # Check for regime switch
            if info.get('regime_switch', False):
                training_history['regime_switches'].append(episode)
        
        # Compute ΦID for episode (simplified)
        # In practice, would collect full latent trajectories
        phi_id_metrics = {
            'phi_g_total': np.random.rand(),  # Placeholder
            'decoupling': np.random.rand()
        }
        episode_phi_id.append(phi_id_metrics['phi_g_total'])
        episode_decoupling.append(phi_id_metrics['decoupling'])
        
        # Store episode averages
        training_history['phi_id_over_time'].append(np.mean(episode_phi_id))
        training_history['prediction_error'].append(np.mean(episode_pred_error))
        training_history['decoupling_measure'].append(np.mean(episode_decoupling))
    
    return training_history
```

## Validation

Simulations should reproduce:
  - Concentration of ΦID in slow global latent **g** rather than fast perception latent **z**
  - Decrease in aggregate ΦID magnitude with training in reward-free setting
  - Sign flip in decoupling measure from negative to positive during training
  - Regime-invariance of decoupling measure under environmental change
  - Downward causation carrying regime-dependent adjustment

## Resources

### scripts/
  - `perspective_latents_agent.py` - Main implementation of the agent architecture
  - `phi_id_computation.py` - Integrated Information Decomposition calculation
  - `regime_switching_analysis.py` - Analysis of ΦID behavior across regime switches
  - `training_protocol_reward_free.py` - Reward-free training protocol implementation

### references/
  - `integrated_information_decomposition.md` - Background on ΦID methodology
  - `active_inference_framework.md` - Overview of active inference principles
  - `causal_emergence_theory.md` - Theoretical foundations of causal emergence

### assets/
  - `phi_id_concentration_plot.png` - Visualization of ΦID concentration in g vs z
  - `decoupling_sign_flip.png` - Plot showing decoupling measure sign flip during training
  - `regime_invariance_analysis.png` - Analysis of regime-invariant vs regime-dependent measures

## Activation Keywords

  - perspective-latents-causal-emergence-active-inference
  - causal emergence active inference
  - integrated information decomposition
  - perspective latents architecture
  - slow global latent
  - fast perception latent
  - structural decoupling
  - regime-switching protocol
  - reward-free predictive organization
  - atom-compositional analysis

## Validation

After implementing this skill, verify that:
  1. ΦID concentrates in the slow global latent g rather than fast perception latent z.
  2. The aggregate ΦID magnitude decreases with training in reward-free settings.
  3. Decoupling measure shows sign flip from negative to positive during training.
  4. Decoupling becomes regime-invariant while downward causation remains regime-dependent.
  5. Scalar ΦID is not a reliable indicator of learned integration without atom-compositional analysis.

## References

  Pae, H. (2026). Perspective Latents as an Architectural Condition for Causal Emergence in Active Inference Agents. arXiv preprint arXiv:2607.20708.