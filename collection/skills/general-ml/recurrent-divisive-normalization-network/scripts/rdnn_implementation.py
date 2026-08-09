import torch
import torch.nn as nn
import torch.nn.functional as F

class RecurrentDivisiveNormalizationNetwork(nn.Module):
    """
    Recurrent Divisive Normalization Network (RDNN) implementation.
    
    This implements the core RDNN architecture from Gu et al. (2026)
    for continuous working memory with low-rank slow manifolds.
    """
    
    def __init__(self, input_size, hidden_size, output_size, alpha=0.1, 
                 activation='tanh', orthogonal_init=True):
        """
        Initialize RDNN.
        
        Args:
            input_size (int): Size of input features
            hidden_size (int): Size of hidden state
            output_size (int): Size of output features  
            alpha (float): Divisive normalization strength (default: 0.1)
            activation (str): Activation function ('tanh' or 'relu')
            orthogonal_init (bool): Whether to use orthogonal initialization
        """
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.alpha = alpha
        
        # Recurrent and input weight matrices
        self.W_h = nn.Parameter(torch.randn(hidden_size, hidden_size))
        self.W_x = nn.Parameter(torch.randn(hidden_size, input_size))
        self.W_out = nn.Parameter(torch.randn(output_size, hidden_size))
        
        # Bias terms
        self.b_h = nn.Parameter(torch.zeros(hidden_size))
        self.b_out = nn.Parameter(torch.zeros(output_size))
        
        # Activation function
        if activation == 'tanh':
            self.activation = torch.tanh
        elif activation == 'relu':
            self.activation = F.relu
        else:
            raise ValueError(f"Unsupported activation: {activation}")
            
        # Initialize weights
        if orthogonal_init:
            nn.init.orthogonal_(self.W_h)
            nn.init.xavier_uniform_(self.W_x)
            nn.init.xavier_uniform_(self.W_out)
        else:
            nn.init.xavier_uniform_(self.W_h)
            nn.init.xavier_uniform_(self.W_x)
            nn.init.xavier_uniform_(self.W_out)
    
    def forward_step(self, x_t, h_prev):
        """
        Single forward step of RDNN.
        
        Args:
            x_t (Tensor): Input at time t, shape (batch_size, input_size)
            h_prev (Tensor): Previous hidden state, shape (batch_size, hidden_size)
            
        Returns:
            h_t (Tensor): Current hidden state, shape (batch_size, hidden_size)
            y_t (Tensor): Current output, shape (batch_size, output_size)
        """
        # Compute pre-activation hidden state
        h_pre = torch.matmul(h_prev, self.W_h.t()) + torch.matmul(x_t, self.W_x.t()) + self.b_h
        
        # Apply activation function
        h_activated = self.activation(h_pre)
        
        # Apply divisive normalization
        # L1 norm along hidden dimension
        l1_norm = torch.sum(torch.abs(h_activated), dim=-1, keepdim=True)
        h_t = h_activated / (1.0 + self.alpha * l1_norm)
        
        # Compute output
        y_t = torch.matmul(h_t, self.W_out.t()) + self.b_out
        
        return h_t, y_t
    
    def forward(self, x_seq, h0=None):
        """
        Forward pass through sequence.
        
        Args:
            x_seq (Tensor): Input sequence, shape (seq_len, batch_size, input_size)
            h0 (Tensor): Initial hidden state, shape (batch_size, hidden_size)
            
        Returns:
            outputs (Tensor): Output sequence, shape (seq_len, batch_size, output_size)
            hidden_states (Tensor): Hidden states, shape (seq_len, batch_size, hidden_size)
        """
        seq_len, batch_size = x_seq.shape[0], x_seq.shape[1]
        
        if h0 is None:
            h0 = torch.zeros(batch_size, self.hidden_size, device=x_seq.device)
        
        outputs = []
        hidden_states = []
        h_t = h0
        
        for t in range(seq_len):
            h_t, y_t = self.forward_step(x_seq[t], h_t)
            outputs.append(y_t)
            hidden_states.append(h_t)
        
        outputs = torch.stack(outputs, dim=0)
        hidden_states = torch.stack(hidden_states, dim=0)
        
        return outputs, hidden_states
    
    def compute_effective_rank(self, hidden_states):
        """
        Compute effective rank of hidden state covariance matrix.
        
        Args:
            hidden_states (Tensor): Hidden states, shape (seq_len, batch_size, hidden_size)
            
        Returns:
            effective_rank (float): Effective rank of the hidden state manifold
        """
        # Reshape to (total_timesteps, hidden_size)
        h_flat = hidden_states.view(-1, self.hidden_size)
        
        # Compute covariance matrix
        h_centered = h_flat - h_flat.mean(dim=0, keepdim=True)
        cov_matrix = torch.matmul(h_centered.t(), h_centered) / (h_flat.shape[0] - 1)
        
        # Compute singular values
        s = torch.svd(cov_matrix, compute_uv=False).S
        s = s[s > 1e-10]  # Remove near-zero singular values
        
        if len(s) == 0:
            return 0.0
            
        # Normalize singular values to form probability distribution
        p = s / s.sum()
        
        # Compute entropy and effective rank
        entropy = -torch.sum(p * torch.log(p + 1e-10))
        effective_rank = torch.exp(entropy).item()
        
        return effective_rank


def create_continuous_memory_task(seq_len=50, delay_len=20, batch_size=32, input_dim=1, output_dim=1):
    """
    Create a continuous working memory task.
    
    Task: Store a continuous value during a delay period and reproduce it at the end.
    
    Args:
        seq_len (int): Total sequence length
        delay_len (int): Delay period length  
        batch_size (int): Batch size
        input_dim (int): Input dimension
        output_dim (int): Output dimension
        
    Returns:
        inputs (Tensor): Input sequence
        targets (Tensor): Target sequence  
        mask (Tensor): Loss mask (1 during output period, 0 otherwise)
    """
    # Initialize sequences
    inputs = torch.zeros(seq_len, batch_size, input_dim)
    targets = torch.zeros(seq_len, batch_size, output_dim)
    mask = torch.zeros(seq_len, batch_size, output_dim)
    
    # Generate random continuous values to remember
    values_to_remember = torch.randn(batch_size, output_dim)
    
    # Input: present value at beginning of sequence
    inputs[0] = values_to_remember
    
    # Target: reproduce value at end of sequence
    targets[-1] = values_to_remember
    mask[-1] = 1.0  # Only compute loss at final timestep
    
    return inputs, targets, mask


# Example usage
if __name__ == "__main__":
    # Create model
    model = RecurrentDivisiveNormalizationNetwork(
        input_size=1, 
        hidden_size=64, 
        output_size=1, 
        alpha=0.1,
        activation='tanh'
    )
    
    # Create task data
    inputs, targets, mask = create_continuous_memory_task(
        seq_len=100, 
        delay_len=80, 
        batch_size=16
    )
    
    # Forward pass
    outputs, hidden_states = model(inputs)
    
    # Compute effective rank
    eff_rank = model.compute_effective_rank(hidden_states)
    print(f"Effective rank: {eff_rank:.2f}")
    
    # Compute loss (only at final timestep)
    loss = torch.mean(mask * (outputs - targets) ** 2)
    print(f"Loss: {loss.item():.4f}")