#!/usr/bin/env python3
"""
CogniSNN Implementation

Reference implementation of Cognition-aware Spiking Neural Networks 
with Random Graph Architecture.

Paper: "CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, 
and Dynamic-Configurability with Random Graph Architectures in 
Spiking Neural Networks" (arXiv:2512.11743)
"""

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List
from collections import defaultdict
import networkx as nx


class SurrogateGradient(torch.autograd.Function):
    """
    Surrogate gradient for spike function.
    Backward pass uses continuous approximation.
    """
    
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        return (input > 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        # Derivative of fast sigmoid
        grad_input = grad_output / (1.0 + np.pi * torch.abs(input))**2
        return grad_input


spike_activation = SurrogateGradient.apply


class LIFNeuron(nn.Module):
    """
    Leaky Integrate-and-Fire neuron with learnable parameters.
    """
    
    def __init__(self, tau=20.0, v_th=1.0, v_rest=0.0, tau_ref=2.0):
        super().__init__()
        self.tau = nn.Parameter(torch.tensor(tau))
        self.v_th = v_th
        self.v_rest = v_rest
        self.tau_ref = tau_ref
        
    def forward(self, current, state):
        """
        Forward pass of LIF neuron.
        
        Args:
            current: Input current [batch, n_neurons]
            state: Dictionary with 'v' (voltage) and 'ref' (refractory)
            
        Returns:
            spike: Output spikes
            new_state: Updated state
        """
        v_prev = state['v']
        ref_prev = state['ref']
        
        # Refractory period handling
        v_decayed = torch.where(
            ref_prev > 0,
            torch.full_like(v_prev, self.v_rest),
            v_prev
        )
        
        # Membrane integration
        dv = (v_decayed - self.v_rest + current) / self.tau
        v_new = v_decayed + dv - self.v_th * state.get('spike', torch.zeros_like(v_prev))
        
        # Spike generation
        spike = spike_activation(v_new)
        
        # Update refractory period
        ref_new = torch.clamp(ref_prev - 1 + spike * self.tau_ref, min=0)
        
        new_state = {
            'v': v_new * (1 - spike) + self.v_rest * spike,
            'ref': ref_new,
            'spike': spike
        }
        
        return spike, new_state


class RandomGraphTopology:
    """
    Generates and manages random graph topology for SNN.
    """
    
    def __init__(self, n_neurons: int, connection_prob: float = 0.1,
                 small_world_rewiring: float = 0.3):
        self.n_neurons = n_neurons
        self.connection_prob = connection_prob
        self.small_world_rewiring = small_world_rewiring
        self.graph = self._generate_graph()
        
    def _generate_graph(self) -> nx.Graph:
        """Generate small-world random graph."""
        # Start with ring lattice
        k = int(self.connection_prob * self.n_neurons)
        G = nx.watts_strogatz_graph(
            self.n_neurons, 
            k, 
            self.small_world_rewiring
        )
        return G
    
    def get_adjacency_matrix(self) -> np.ndarray:
        """Get adjacency matrix representation."""
        return nx.to_numpy_array(self.graph)
    
    def add_neuron(self, connect_to_k: int = 5):
        """Dynamically add neuron to graph."""
        new_id = self.n_neurons
        self.graph.add_node(new_id)
        
        # Connect to k nearest neighbors (small-world property)
        existing = list(range(self.n_neurons))
        neighbors = np.random.choice(existing, size=connect_to_k, replace=False)
        
        for neighbor in neighbors:
            self.graph.add_edge(new_id, neighbor)
        
        self.n_neurons += 1
        return new_id
    
    def get_neighbors(self, neuron_id: int) -> List[int]:
        """Get neighboring neurons."""
        return list(self.graph.neighbors(neuron_id))


class SpikingResidualBlock(nn.Module):
    """
    Pure spiking residual block for deep SNN pathways.
    """
    
    def __init__(self, in_features, out_features, alpha_init=1.0):
        super().__init__()
        self.in_features = in_features
        self.out_features = out_features
        
        # Spiking layers
        self.fc = nn.Linear(in_features, out_features)
        self.bn = nn.BatchNorm1d(out_features)
        
        # Residual scaling
        self.alpha = nn.Parameter(torch.tensor(alpha_init))
        
        # Adaptive pooling for dimension matching
        if in_features != out_features:
            self.pool = nn.Linear(in_features, out_features, bias=False)
        else:
            self.pool = nn.Identity()
    
    def forward(self, x, lif_states):
        """
        Forward with spiking activation.
        
        Args:
            x: Input [batch, time, features] or [batch, features]
            lif_states: LIF neuron states
        """
        residual = self.pool(x)
        
        # Spiking transformation
        current = self.fc(x)
        if len(current.shape) == 3:  # [batch, time, features]
            current = current.transpose(1, 2)
            current = self.bn(current)
            current = current.transpose(1, 2)
        else:
            current = self.bn(current)
        
        # Generate spikes (simplified - no time dimension handling)
        spike = spike_activation(current)
        
        # Residual connection
        out = spike + self.alpha * residual
        
        return out, lif_states


class CogniSNN(nn.Module):
    """
    Cognition-aware Spiking Neural Network.
    """
    
    def __init__(self, input_size, hidden_size, output_size,
                 n_neurons=1000, connection_prob=0.1):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Random graph topology
        self.topology = RandomGraphTopology(n_neurons, connection_prob)
        adj_matrix = self.topology.get_adjacency_matrix()
        
        # Spiking neurons
        self.neurons = nn.ModuleList([
            LIFNeuron() for _ in range(n_neurons)
        ])
        
        # Synaptic weights (masked by adjacency)
        self.register_buffer('adj_mask', torch.from_numpy(adj_matrix).float())
        self.weights = nn.Parameter(torch.randn(n_neurons, n_neurons) * 0.01)
        
        # Input/output projections
        self.input_proj = nn.Linear(input_size, n_neurons)
        self.output_proj = nn.Linear(n_neurons, output_size)
        
        # Residual blocks
        self.residual_blocks = nn.ModuleList([
            SpikingResidualBlock(n_neurons, n_neurons)
            for _ in range(3)
        ])
        
        # Key pathway tracking for continual learning
        self.key_pathway_mask = None
        self.fisher_information = None
        
    def forward(self, x, timesteps=10):
        """
        Forward pass through network.
        
        Args:
            x: Input [batch, input_size]
            timesteps: Number of simulation timesteps
            
        Returns:
            output: Network output
            spike_history: Record of network activity
        """
        batch_size = x.size(0)
        n_neurons = len(self.neurons)
        
        # Initialize states
        states = [{
            'v': torch.zeros(batch_size, 1),
            'ref': torch.zeros(batch_size, 1),
            'spike': torch.zeros(batch_size, 1)
        } for _ in range(n_neurons)]
        
        spike_history = []
        
        # Input projection
        input_current = self.input_proj(x)  # [batch, n_neurons]
        
        for t in range(timesteps):
            # Compute synaptic currents
            spikes = torch.cat([s['spike'] for s in states], dim=1)  # [batch, n_neurons]
            masked_weights = self.weights * self.adj_mask
            synaptic_input = spikes @ masked_weights.t()  # [batch, n_neurons]
            
            total_current = input_current + synaptic_input
            
            # Update neurons
            new_spikes = []
            for i, neuron in enumerate(self.neurons):
                spike, states[i] = neuron(
                    total_current[:, i:i+1], 
                    states[i]
                )
                new_spikes.append(spike)
            
            spike_history.append(torch.cat(new_spikes, dim=1))
        
        # Output from last timestep
        final_spikes = spike_history[-1]
        output = self.output_proj(final_spikes)
        
        return output, spike_history
    
    def identify_key_pathways(self, dataloader, num_batches=10):
        """
        Identify key pathways using Fisher Information.
        
        Args:
            dataloader: Data for computing importance
            num_batches: Number of batches to use
        """
        self.eval()
        fisher = defaultdict(float)
        
        for i, (data, target) in enumerate(dataloader):
            if i >= num_batches:
                break
            
            self.zero_grad()
            output, _ = self(data)
            loss = F.cross_entropy(output, target)
            loss.backward()
            
            # Accumulate squared gradients
            for name, param in self.named_parameters():
                if param.grad is not None:
                    fisher[name] += param.grad.data ** 2
        
        # Normalize
        for name in fisher:
            fisher[name] /= num_batches
        
        # Create key pathway mask (top 10% important)
        self.fisher_information = fisher
        
        all_fisher = torch.cat([f.flatten() for f in fisher.values()])
        threshold = torch.quantile(all_fisher, 0.9)
        
        self.key_pathway_mask = {
            name: (f > threshold).float()
            for name, f in fisher.items()
        }
    
    def apply_kplwf_loss(self, new_loss, replay_loss, lambda_replay=1.0):
        """
        Apply Key Pathway-based Learning without Forgetting loss.
        
        Args:
            new_loss: Loss on new task
            replay_loss: Loss on replay data
            lambda_replay: Weight for replay loss
            
        Returns:
            Combined loss
        """
        if self.key_pathway_mask is None:
            return new_loss + lambda_replay * replay_loss
        
        # Compute gradients separately
        new_loss.backward(retain_graph=True)
        new_grads = {
            name: param.grad.clone() if param.grad is not None else None
            for name, param in self.named_parameters()
        }
        
        self.zero_grad()
        replay_loss.backward()
        replay_grads = {
            name: param.grad.clone() if param.grad is not None else None
            for name, param in self.named_parameters()
        }
        
        # Combine with masking
        for name, param in self.named_parameters():
            if new_grads[name] is not None:
                # New task gradients only on non-key pathways
                masked_new = new_grads[name] * (1 - self.key_pathway_mask.get(name, 1))
                # Replay gradients only on key pathways  
                masked_replay = replay_grads.get(name, 0) * self.key_pathway_mask.get(name, 0)
                param.grad = masked_new + lambda_replay * masked_replay
        
        return new_loss + lambda_replay * replay_loss
    
    def dynamic_growth(self, activity_threshold=0.5, correlation_threshold=0.8):
        """
        Dynamic Growth Learning: Add neurons and synapses based on activity.
        
        Args:
            activity_threshold: Threshold for adding new neuron
            correlation_threshold: Threshold for adding new synapse
        """
        # This is a simplified version
        # In practice, would analyze activity patterns over time
        
        # Check if new neuron needed
        avg_activity = self.fisher_information.get('weights', torch.tensor([0])).mean()
        
        if avg_activity > activity_threshold:
            # Add new neuron
            new_id = self.topology.add_neuron(connect_to_k=5)
            
            # Initialize new neuron
            new_neuron = LIFNeuron()
            self.neurons.append(new_neuron)
            
            # Expand weight matrix
            new_weights = torch.randn(len(self.neurons), len(self.neurons)) * 0.01
            new_weights[:self.weights.size(0), :self.weights.size(1)] = self.weights.data
            self.weights = nn.Parameter(new_weights)
            
            # Update adjacency mask
            new_adj = self.topology.get_adjacency_matrix()
            self.register_buffer('adj_mask', torch.from_numpy(new_adj).float())
            
            return new_id
        
        return None


class CogniSNNTrainer:
    """
    Trainer for CogniSNN with continual learning support.
    """
    
    def __init__(self, model, optimizer, device='cpu'):
        self.model = model.to(device)
        self.optimizer = optimizer
        self.device = device
        self.task_history = []
        
    def train_task(self, dataloader, num_epochs, task_id):
        """
        Train on a specific task.
        
        Args:
            dataloader: Data for current task
            num_epochs: Training epochs
            task_id: Task identifier
        """
        self.model.train()
        
        # Identify key pathways from previous tasks
        if len(self.task_history) > 0:
            self.model.identify_key_pathways(dataloader)
        
        for epoch in range(num_epochs):
            total_loss = 0
            
            for data, target in dataloader:
                data, target = data.to(self.device), target.to(self.device)
                
                self.optimizer.zero_grad()
                
                # Forward pass
                output, _ = self.model(data)
                new_loss = F.cross_entropy(output, target)
                
                # Apply KP-LwF if not first task
                if len(self.task_history) > 0:
                    # Generate replay data (simplified)
                    replay_data, replay_target = self._get_replay_data()
                    replay_output, _ = self.model(replay_data)
                    replay_loss = F.cross_entropy(replay_output, replay_target)
                    loss = self.model.apply_kplwf_loss(new_loss, replay_loss)
                else:
                    loss = new_loss
                
                loss.backward()
                self.optimizer.step()
                
                total_loss += loss.item()
            
            print(f"Task {task_id}, Epoch {epoch+1}/{num_epochs}, "
                  f"Loss: {total_loss/len(dataloader):.4f}")
        
        self.task_history.append(task_id)
    
    def _get_replay_data(self):
        """Get replay data from previous tasks (simplified)."""
        # In practice, would use stored exemplars or generative replay
        return (torch.randn(32, self.model.input_size).to(self.device),
                torch.randint(0, self.model.output_size, (32,)).to(self.device))
    
    def evaluate(self, dataloader):
        """Evaluate model performance."""
        self.model.eval()
        correct = 0
        total = 0
        
        with torch.no_grad():
            for data, target in dataloader:
                data, target = data.to(self.device), target.to(self.device)
                output, _ = self.model(data)
                _, predicted = output.max(1)
                total += target.size(0)
                correct += predicted.eq(target).sum().item()
        
        accuracy = 100. * correct / total
        return accuracy


def example_usage():
    """Example usage of CogniSNN."""
    print("CogniSNN Example")
    print("=" * 50)
    
    # Model configuration
    input_size = 784  # e.g., MNIST
    hidden_size = 1000
    output_size = 10
    
    # Create model
    model = CogniSNN(
        input_size=input_size,
        hidden_size=hidden_size,
        output_size=output_size,
        n_neurons=500,
        connection_prob=0.1
    )
    
    print("\nModel created:")
    print(f"  Neurons: {len(model.neurons)}")
    print(f"  Connections: {model.adj_mask.sum().item():.0f}")
    print(f"  Parameters: {sum(p.numel() for p in model.parameters()):,}")
    
    # Test forward pass
    test_input = torch.randn(4, input_size)
    output, spikes = model(test_input, timesteps=10)
    
    print("\nTest forward pass:")
    print(f"  Input: {test_input.shape}")
    print(f"  Output: {output.shape}")
    print(f"  Spike activity: {sum(s.sum().item() for s in spikes):.0f} spikes")


if __name__ == "__main__":
    example_usage()
