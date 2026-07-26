"""
Template for Event-based GRU implementation
Based on: Event-based Neural Decoding for Neuroprosthetic Motor Control (arXiv:2607.11445v1)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class EventBasedGRUCell(nn.Module):
    """
    Event-based GRU Cell that processes spike events asynchronously.
    Only computes updates when spikes arrive (event-driven computation).
    """
    
    def __init__(self, input_size, hidden_size, bias=True):
        super(EventBasedGRUCell, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.bias = bias
        
        # Gates: update gate (z), reset gate (r), candidate activation (h)
        self.weight_ih = nn.Parameter(torch.Tensor(3 * hidden_size, input_size))
        self.weight_hh = nn.Parameter(torch.Tensor(3 * hidden_size, hidden_size))
        if bias:
            self.bias_ih = nn.Parameter(torch.Tensor(3 * hidden_size))
            self.bias_hh = nn.Parameter(torch.Tensor(3 * hidden_size))
        else:
            self.register_parameter('bias_ih', None)
            self.register_parameter('bias_hh', None)
        
        self.reset_parameters()
    
    def reset_parameters(self):
        """Initialize weights using Xavier uniform distribution"""
        stdv = 1.0 / (self.hidden_size ** 0.5)
        for weight in self.parameters():
            weight.data.uniform_(-stdv, stdv)
    
    def forward(self, event_input, hidden_state, event_mask=None):
        """
        Forward pass for event-based GRU.
        
        Args:
            event_input: Tensor of shape (batch, seq_len, input_size) - event features
            hidden_state: Tensor of shape (batch, hidden_size) - previous hidden state
            event_mask: Binary tensor of shape (batch, seq_len) indicating event presence
                       (1 = event present, 0 = no event). If None, treats all timesteps as events.
        
        Returns:
            output: Tensor of shape (batch, seq_len, hidden_size) - hidden states for each timestep
            final_hidden: Tensor of shape (batch, hidden_size) - final hidden state
        """
        batch_size, seq_len, _ = event_input.size()
        
        if event_mask is None:
            event_mask = torch.ones(batch_size, seq_len, device=event_input.device)
        
        # Initialize output tensor
        output = []
        
        # Process each timestep
        h_t = hidden_state  # Initial hidden state
        
        for t in range(seq_len):
            # Check if event occurred at this timestep
            event_occurred = event_mask[:, t] > 0
            
            if event_occurred.any():
                # Get input for events that occurred
                x_t = event_input[:, t, :]  # (batch, input_size)
                
                # Compute gates
                # Window the weights for efficient computation
                gates = torch.mm(x_t, self.weight_ih.t()) + torch.mm(h_t, self.weight_hh.t())
                if self.bias:
                    gates += self.bias_ih + self.bias_hh
                
                # Split into reset, update, and candidate gates
                r_t, z_t, n_t = gates.chunk(3, dim=1)
                
                # Apply activations
                r_t = torch.sigmoid(r_t)  # Reset gate
                z_t = torch.sigmoid(z_t)  # Update gate
                n_t = torch.tanh(r_t * n_t)  # Candidate activation
                
                # Compute new hidden state
                h_t = (1 - z_t) * n_t + z_t * h_t
            # If no event, hidden state remains unchanged (h_t = h_t)
            
            output.append(h_t)
        
        # Stack outputs
        output = torch.stack(output, dim=1)  # (batch, seq_len, hidden_size)
        
        return output, h_t


class EventBasedGRU(nn.Module):
    """
    Multi-layer Event-based GRU for processing neural event sequences.
    """
    
    def __init__(self, input_size, hidden_size, num_layers=1, batch_first=True, dropout=0):
        super(EventBasedGRU, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.batch_first = batch_first
        self.dropout = dropout
        
        # Create layers
        self.layers = nn.ModuleList()
        for i in range(num_layers):
            layer_input_size = input_size if i == 0 else hidden_size
            self.layers.append(EventBasedGRUCell(layer_input_size, hidden_size))
        
        self.dropout_layer = nn.Dropout(dropout) if dropout > 0 else None
    
    def forward(self, event_input, event_mask=None, hidden_state=None):
        """
        Forward pass through the Event-based GRU.
        
        Args:
            event_input: Tensor of shape (batch, seq_len, input_size) if batch_first=True
            event_mask: Binary tensor of shape (batch, seq_len) indicating event presence
            hidden_state: Initial hidden state (num_layers, batch, hidden_size) or None
            
        Returns:
            output: Tensor of shape (batch, seq_len, hidden_size) if batch_first=True
            hidden_n: Final hidden state (num_layers, batch, hidden_size)
        """
        if not self.batch_first:
            # Convert to batch_first for processing
            event_input = event_input.transpose(0, 1)
            if event_mask is not None:
                event_mask = event_mask.transpose(event_mask.transpose(0, 1)
        
        batch_size, seq_len, _ = event_input.size()
        
        # Initialize hidden state if not provided
        if hidden_state is None:
            h_n = torch.zeros(self.num_layers, batch_size, self.hidden_size, 
                             device=event_input.device)
        else:
            h_n = hidden_state
        
        # Process through each layer
        layer_input = event_input
        layer_outputs = []
        
        for layer_idx, layer in enumerate(self.layers):
            # Get current layer's hidden state
            h_t = h_n[layer_idx]  # (batch, hidden_size)
            
            # Forward pass through layer
            layer_output, h_t_new = layer(layer_input, h_t, event_mask)
            
            # Apply dropout between layers (except last layer)
            if self.dropout_layer is not None and layer_idx < self.num_layers - 1:
                layer_output = self.dropout_layer(layer_output)
            
            # Update hidden state
            h_n[layer_idx] = h_t_new
            
            # Prepare input for next layer
            layer_input = layer_output
        
        # Final output
        output = layer_output
        
        if not self.batch_first:
            # Convert back to seq_first
            output = output.transpose(0, 1)
            h_n = h_n  # Already in (num_layers, batch, hidden_size)
        
        return output, h_n


# Example usage function
def create_event_based_decoder(input_dim, hidden_dim, output_dim, num_layers=2):
    """
    Create a complete event-based decoding model for motor control.
    
    Args:
        input_dim: Dimension of event features (timestamp, amplitude, channel_id, etc.)
        hidden_dim: Hidden dimension of GRU layers
        output_dim: Output dimension (e.g., 2 for velocity x,y; 3 for position x,y,z)
        num_layers: Number of GRU layers
    
    Returns:
        model: Complete decoding model
    """
    class EventBasedDecoder(nn.Module):
        def __init__(self):
            super(EventBasedDecoder, self).__init__()
            self.gru = EventBasedGRU(input_dim, hidden_dim, num_layers, batch_first=True)
            self.fc = nn.Linear(hidden_dim, output_dim)
            # Optional: add a final activation depending on output type
            # For continuous control: no activation (raw output)
            # For classification: softmax or sigmoid
            
        def forward(self, event_input, event_mask=None):
            """
            Decode neural events to motor commands.
            
            Args:
                event_input: Event features (batch, seq_len, input_dim)
                event_mask: Event presence mask (batch, seq_len)
                
            Returns:
                decoded_output: Predicted motor commands (batch, seq_len, output_dim)
            """
            # Process through GRU
            gru_output, _ = self.gru(event_input, event_mask)
            
            # Final projection to output space
            output = self.fc(gru_output)
            
            return output
    
    return EventBasedDecoder()


# Surrogate gradient functions for training spiking neurons
def surrogate_grad_sigmoid(x, alpha=1.0):
    """
    Fast sigmoid surrogate gradient for spike function.
    sigma'(x) = alpha * sigmoid(alpha * x) * (1 - sigmoid(alpha * x))
    """
    sig = torch.sigmoid(alpha * x)
    return alpha * sig * (1 - sig)


def surrogate_grad_arctan(x, alpha=1.0):
    """
    Arctan surrogate gradient.
    d/dx atan(alpha * x) = alpha / (1 + (alpha * x)^2)
    """
    return alpha / (1 + (alpha * x) ** 2)


def surrogate_grad_piecewise_linear(x):
    """
    Piecewise linear surrogate gradient.
    f'(x) = 1 - |x| for |x| <= 1, 0 otherwise
    """
    return torch.clamp(1.0 - torch.abs(x), min=0.0)


# Sparsity regularization functions
def l1_sparsity_loss(spike_rates, target_rate=0.02):
    """
    L1 sparsity loss to encourage low firing rates.
    
    Args:
        spike_rates: Average firing rates per neuron (batch, num_neurons)
        target_rate: Target firing rate (e.g., 0.02 for 2% sparsity)
    
    Returns:
        scalar loss value
    """
    return torch.mean(torch.abs(spike_rates - target_rate))


def kl_sparsity_loss(logits, target_prob=0.05):
    """
    KL divergence sparsity loss (more principled than L1).
    
    Args:
        logits: Raw network outputs before activation
        target_prob: Target activation probability
    
    Returns:
        scalar loss value
    """
    # Convert to probabilities
    probs = torch.sigmoid(logits)
    # KL divergence: p * log(p/q) + (1-p) * log((1-p)/(1-q))
    kl = target_prob * torch.log(target_prob / (probs + 1e-8)) + \
         (1 - target_prob) * torch.log((1 - target_prob) / (1 - probs + 1e-8))
    return torch.mean(kl)


if __name__ == "__main__":
    # Example usage
    print("Creating event-based GRU decoder...")
    
    # Example parameters for neural decoding
    input_dim = 3  # [timestamp, amplitude, channel_id]
    hidden_dim = 64
    output_dim = 2  # [velocity_x, velocity_y] or [position_x, position_y]
    num_layers = 2
    
    # Create model
    model = create_event_based_decoder(input_dim, hidden_dim, output_dim, num_layers)
    print(f"Model created: {model}")
    
    # Example forward pass
    batch_size = 16
    seq_len = 100  # 100 time bins (e.g., 1 second at 100Hz binning)
    
    # Simulate event data
    event_input = torch.randn(batch_size, seq_len, input_dim)
    # Create sparse event mask (average 5% event rate)
    event_mask = (torch.rand(batch_size, seq_len) < 0.05).float()
    
    # Forward pass
    with torch.no_grad():
        output = model(event_input, event_mask)
        print(f"Input shape: {event_input.shape}")
        print(f"Event mask sum (total events): {event_mask.sum().item()}")
        print(f"Output shape: {output.shape}")
        print(f"Output range: [{output.min():.3f}, {output.max():.3f}]")
    
    print("\nImplementation complete!")
    print("To use in training:")
    print("1. Replace surrogate gradient in loss.backward() call")
    print("2. Add sparsity regularization to loss function")
    print("3. Deploy to neuromorphic hardware for event-driven inference")