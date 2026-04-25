"""
WTA Spiking Transformer Implementation
Example: Complete training and inference pipeline

Paper: Winner-Take-All Spiking Transformer for Language Modeling
arXiv: 2604.11321
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from typing import Optional, Tuple
import math


# =============================================================================
# Spiking Neuron Models
# =============================================================================

class T_LIF(nn.Module):
    """
    Ternary Leaky Integrate-and-Fire neuron
    Extends binary spikes {0,1} to ternary values {-α, 0, α}
    """
    def __init__(self, alpha: float = 1.0, beta: float = 0.5, v_reset: float = 0.0):
        super().__init__()
        self.alpha = alpha
        self.beta = beta
        self.v_reset = v_reset
        
    def forward(self, x: torch.Tensor, mem_prev: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, torch.Tensor]:
        batch_size = x.shape[0]
        device = x.device
        
        if mem_prev is None:
            mem_prev = torch.zeros(batch_size, *x.shape[1:], device=device)
        
        # Current integration
        u = mem_prev + x
        
        # Ternary spike generation
        s_pos = (u > self.alpha).float()
        s_neg = (u < -self.alpha).float()
        s = s_pos - s_neg  # {-1, 0, 1}
        
        # Membrane potential update
        spike_mask = (s != 0).float()
        mem = self.v_reset * spike_mask + self.beta * u * (1 - spike_mask)
        
        return s * self.alpha, mem


class NI_LIF(nn.Module):
    """
    Normalized Integer Leaky Integrate-and-Fire
    Uses integer training and spike inference for faster training
    """
    def __init__(self, D: int = 4, beta: float = 0.5):
        super().__init__()
        self.D = D  # Maximum quantized integer value
        self.beta = beta
        
    def forward(self, x: torch.Tensor, mem_prev: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, torch.Tensor]:
        batch_size = x.shape[0]
        device = x.device
        
        if mem_prev is None:
            mem_prev = torch.zeros(batch_size, *x.shape[1:], device=device)
        
        # Current integration
        u = mem_prev + x
        
        # Quantized spike generation
        s = torch.round(torch.clamp(u, 0, self.D)) / self.D
        
        # Membrane potential update
        mem = self.beta * (u - s * self.D)
        
        return s, mem


class SpikingNeuronLayer(nn.Module):
    """
    Wrapper for spiking neuron with time-step unrolling
    """
    def __init__(self, time_steps: int = 4, neuron_type: str = "ni_lif", **neuron_kwargs):
        super().__init__()
        self.time_steps = time_steps
        
        if neuron_type == "t_lif":
            self.neuron = T_LIF(**neuron_kwargs)
        elif neuron_type == "ni_lif":
            self.neuron = NI_LIF(**neuron_kwargs)
        else:
            raise ValueError(f"Unknown neuron type: {neuron_type}")
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input tensor [batch, seq_len, dim]
        Returns:
            spikes: [time_steps, batch, seq_len, dim]
        """
        batch_size, seq_len, dim = x.shape
        device = x.device
        
        spikes = []
        mem = None
        
        for t in range(self.time_steps):
            s, mem = self.neuron(x, mem)
            spikes.append(s)
        
        return torch.stack(spikes)  # [T, B, S, D]


# =============================================================================
# Winner-Take-All Mechanisms
# =============================================================================

def hard_wta(x: torch.Tensor, dim: int = -1) -> torch.Tensor:
    """
    Hard Winner-Take-All: Only the maximum value survives
    
    Args:
        x: Input tensor
        dim: Dimension to apply WTA
    Returns:
        One-hot encoded output
    """
    max_idx = torch.argmax(x, dim=dim, keepdim=True)
    output = torch.zeros_like(x)
    output.scatter_(dim, max_idx, 1.0)
    return output


def topk_wta(x: torch.Tensor, k: int = 3, dim: int = -1) -> torch.Tensor:
    """
    Top-K Winner-Take-All: Top K values survive
    
    Args:
        x: Input tensor
        k: Number of winners
        dim: Dimension to apply WTA
    Returns:
        Binary mask with K 1s
    """
    _, indices = torch.topk(x, k, dim=dim)
    output = torch.zeros_like(x)
    output.scatter_(dim, indices, 1.0)
    return output


class SurrogateWTA(torch.autograd.Function):
    """
    Surrogate gradient for WTA layer
    Forward: Hard WTA
    Backward: Softmax gradient
    """
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        return hard_wta(input)
    
    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        # Use softmax gradient as surrogate
        softmax_probs = F.softmax(input, dim=-1)
        grad_input = grad_output * softmax_probs * (1 - softmax_probs)
        return grad_input


def apply_wta(x: torch.Tensor, training: bool = True, method: str = "hard") -> torch.Tensor:
    """
    Apply WTA with surrogate gradient during training
    
    Args:
        x: Input tensor
        training: Whether in training mode
        method: 'hard', 'topk', or 'sparsemax'
    """
    if method == "hard":
        if training:
            return SurrogateWTA.apply(x)
        else:
            return hard_wta(x)
    elif method == "topk":
        # Use topk with k=3 as default
        return topk_wta(x, k=3)
    else:
        raise ValueError(f"Unknown method: {method}")


# =============================================================================
# WTA Spiking Self-Attention
# =============================================================================

class WSSA(nn.Module):
    """
    WTA Spiking Self-Attention for Encoder-only models
    """
    def __init__(self, dim: int, num_heads: int = 8, time_steps: int = 4, 
                 wta_method: str = "hard"):
        super().__init__()
        assert dim % num_heads == 0, "dim must be divisible by num_heads"
        
        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = dim // num_heads
        self.time_steps = time_steps
        self.scale = self.head_dim ** -0.5
        self.wta_method = wta_method
        
        # Spiking neurons
        self.sn_input = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn_q = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn_k = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn_v = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn_out = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        
        # Linear projections
        self.q_proj = nn.Linear(dim, dim)
        self.k_proj = nn.Linear(dim, dim)
        self.v_proj = nn.Linear(dim, dim)
        self.out_proj = nn.Linear(dim, dim)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [batch, seq_len, dim]
        Returns:
            Output: [batch, seq_len, dim]
        """
        batch_size, seq_len, _ = x.shape
        
        # Spike encoding
        x_spikes = self.sn_input(x)  # [T, B, S, D]
        
        outputs = []
        for t in range(self.time_steps):
            x_t = x_spikes[t]
            
            # Generate Q, K, V
            Q = self.sn_q(x_t)[t]  # [B, S, D]
            K = self.sn_k(x_t)[t]
            V = self.sn_v(x_t)[t]
            
            # Apply linear projections
            Q = self.q_proj(Q)
            K = self.k_proj(K)
            V = self.v_proj(V)
            
            # Reshape for multi-head attention
            Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
            K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
            V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
            # [B, H, S, D_head]
            
            # Attention scores: Q @ K^T
            attn_scores = torch.matmul(Q, K.transpose(-2, -1)) * self.scale
            # [B, H, S, S]
            
            # Apply WTA
            attn_weights = apply_wta(
                attn_scores.view(-1, seq_len), 
                training=self.training,
                method=self.wta_method
            ).view(batch_size, self.num_heads, seq_len, seq_len)
            
            # Attention output: attn_weights @ V
            attn_out = torch.matmul(attn_weights, V)
            # [B, H, S, D_head]
            
            # Reshape and project
            attn_out = attn_out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.dim)
            out = self.out_proj(attn_out)
            
            outputs.append(out)
        
        # Aggregate over time
        return torch.stack(outputs).mean(dim=0)


class CWSSA(nn.Module):
    """
    Causal WTA Spiking Self-Attention for Decoder-only models
    Includes causal mask for autoregressive generation
    """
    def __init__(self, dim: int, num_heads: int = 8, time_steps: int = 4,
                 max_seq_len: int = 2048, wta_method: str = "hard"):
        super().__init__()
        assert dim % num_heads == 0
        
        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = dim // num_heads
        self.time_steps = time_steps
        self.scale = self.head_dim ** -0.5
        self.wta_method = wta_method
        
        # Spiking neurons
        self.sn_input = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn_q = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn_k = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn_v = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn_out = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        
        # Projections
        self.q_proj = nn.Linear(dim, dim)
        self.k_proj = nn.Linear(dim, dim)
        self.v_proj = nn.Linear(dim, dim)
        self.out_proj = nn.Linear(dim, dim)
        
        # Causal mask
        self.register_buffer(
            "causal_mask",
            torch.triu(torch.ones(max_seq_len, max_seq_len), diagonal=1).bool()
        )
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch_size, seq_len, _ = x.shape
        
        # Get causal mask
        mask = self.causal_mask[:seq_len, :seq_len]
        
        # Spike encoding
        x_spikes = self.sn_input(x)
        
        outputs = []
        for t in range(self.time_steps):
            x_t = x_spikes[t]
            
            # Generate Q, K, V
            Q = self.sn_q(x_t)[t]
            K = self.sn_k(x_t)[t]
            V = self.sn_v(x_t)[t]
            
            # Apply linear projections
            Q = self.q_proj(Q)
            K = self.k_proj(K)
            V = self.v_proj(V)
            
            # Reshape for multi-head
            Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
            K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
            V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
            
            # Attention scores with causal mask
            attn_scores = torch.matmul(Q, K.transpose(-2, -1)) * self.scale
            attn_scores = attn_scores.masked_fill(mask.unsqueeze(0).unsqueeze(0), float('-inf'))
            
            # Apply WTA with causal masking
            # First apply softmax for gradient flow in masked regions
            if self.training:
                attn_probs = F.softmax(attn_scores, dim=-1)
                attn_probs = attn_probs.masked_fill(mask.unsqueeze(0).unsqueeze(0), 0.0)
                
                # Forward: hard WTA
                flat_scores = attn_scores.view(-1, seq_len)
                hard_weights = hard_wta(flat_scores).view(
                    batch_size, self.num_heads, seq_len, seq_len
                )
                hard_weights = hard_weights.masked_fill(mask.unsqueeze(0).unsqueeze(0), 0.0)
                
                # Straight-through estimator
                attn_weights = hard_weights - attn_probs.detach() + attn_probs
            else:
                attn_weights = hard_wta(attn_scores.view(-1, seq_len)).view(
                    batch_size, self.num_heads, seq_len, seq_len
                )
                attn_weights = attn_weights.masked_fill(mask.unsqueeze(0).unsqueeze(0), 0.0)
            
            # Attention output
            attn_out = torch.matmul(attn_weights, V)
            attn_out = attn_out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.dim)
            
            out = self.out_proj(attn_out)
            outputs.append(out)
        
        # Aggregate over time
        return torch.stack(outputs).mean(dim=0)


# =============================================================================
# MLP and Transformer Blocks
# =============================================================================

class SpikeDrivenMLP(nn.Module):
    """
    Spike-driven MLP without floating-point multiplications in forward pass
    """
    def __init__(self, dim: int, hidden_dim: int, time_steps: int = 4):
        super().__init__()
        self.time_steps = time_steps
        
        self.fc1 = nn.Linear(dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, dim)
        
        self.sn1 = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        self.sn2 = SpikingNeuronLayer(time_steps, "ni_lif", D=4)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [batch, seq_len, dim]
        Returns:
            Output: [batch, seq_len, dim]
        """
        outputs = []
        for t in range(self.time_steps):
            # First layer
            h = self.fc1(x)
            h_spike = self.sn1(h.unsqueeze(0))[0]  # Hacky unroll
            
            # Second layer
            out = self.fc2(h_spike)
            out_spike = self.sn2(out.unsqueeze(0))[0]
            
            outputs.append(out_spike)
        
        return torch.stack(outputs).mean(dim=0)


class WESpikingformerBlock(nn.Module):
    """
    WE-Spikingformer Block (Encoder-only)
    """
    def __init__(self, dim: int, num_heads: int, mlp_ratio: float = 4.0, 
                 time_steps: int = 4, wta_method: str = "hard"):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)
        self.attn = WSSA(dim, num_heads, time_steps, wta_method)
        self.norm2 = nn.LayerNorm(dim)
        
        mlp_hidden = int(dim * mlp_ratio)
        self.mlp = SpikeDrivenMLP(dim, mlp_hidden, time_steps)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Self-attention with residual
        x = x + self.attn(self.norm1(x))
        # MLP with residual
        x = x + self.mlp(self.norm2(x))
        return x


class WDSpikingformerBlock(nn.Module):
    """
    WD-Spikingformer Block (Decoder-only)
    """
    def __init__(self, dim: int, num_heads: int, mlp_ratio: float = 4.0,
                 time_steps: int = 4, max_seq_len: int = 2048, wta_method: str = "hard"):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)
        self.attn = CWSSA(dim, num_heads, time_steps, max_seq_len, wta_method)
        self.norm2 = nn.LayerNorm(dim)
        
        mlp_hidden = int(dim * mlp_ratio)
        self.mlp = SpikeDrivenMLP(dim, mlp_hidden, time_steps)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.attn(self.norm1(x))
        x = x + self.mlp(self.norm2(x))
        return x


# =============================================================================
# Complete Models
# =============================================================================

class WESpikingformer(nn.Module):
    """
    WTA-based Encoder-only Spiking Transformer for Masked Language Modeling
    """
    def __init__(self, vocab_size: int, dim: int = 768, depth: int = 12,
                 num_heads: int = 12, max_seq_len: int = 512, 
                 time_steps: int = 4, mlp_ratio: float = 4.0,
                 wta_method: str = "hard"):
        super().__init__()
        
        self.token_embed = nn.Embedding(vocab_size, dim)
        self.pos_embed = nn.Embedding(max_seq_len, dim)
        
        self.blocks = nn.ModuleList([
            WESpikingformerBlock(dim, num_heads, mlp_ratio, time_steps, wta_method)
            for _ in range(depth)
        ])
        
        self.norm = nn.LayerNorm(dim)
        self.head = nn.Linear(dim, vocab_size)
        
        self._init_weights()
        
    def _init_weights(self):
        """Initialize weights"""
        nn.init.normal_(self.token_embed.weight, std=0.02)
        nn.init.normal_(self.pos_embed.weight, std=0.02)
        
    def forward(self, input_ids: torch.Tensor, 
                labels: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, ...]:
        batch_size, seq_len = input_ids.shape
        device = input_ids.device
        
        # Embeddings
        positions = torch.arange(seq_len, device=device).unsqueeze(0).expand(batch_size, -1)
        x = self.token_embed(input_ids) + self.pos_embed(positions)
        
        # Transformer blocks
        for block in self.blocks:
            x = block(x)
        
        x = self.norm(x)
        logits = self.head(x)
        
        if labels is not None:
            loss = F.cross_entropy(
                logits.view(-1, logits.size(-1)),
                labels.view(-1),
                ignore_index=-100
            )
            return loss, logits
        
        return logits


class WDSpikingformer(nn.Module):
    """
    WTA-based Decoder-only Spiking Transformer for Causal Language Modeling
    """
    def __init__(self, vocab_size: int, dim: int = 1024, depth: int = 24,
                 num_heads: int = 16, max_seq_len: int = 2048,
                 time_steps: int = 4, mlp_ratio: float = 4.0,
                 wta_method: str = "hard"):
        super().__init__()
        
        self.token_embed = nn.Embedding(vocab_size, dim)
        self.pos_embed = nn.Embedding(max_seq_len, dim)
        
        self.blocks = nn.ModuleList([
            WDSpikingformerBlock(dim, num_heads, mlp_ratio, time_steps, max_seq_len, wta_method)
            for _ in range(depth)
        ])
        
        self.norm = nn.LayerNorm(dim)
        self.head = nn.Linear(dim, vocab_size)
        
        self._init_weights()
        
    def _init_weights(self):
        nn.init.normal_(self.token_embed.weight, std=0.02)
        nn.init.normal_(self.pos_embed.weight, std=0.02)
        
    def forward(self, input_ids: torch.Tensor,
                labels: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, ...]:
        batch_size, seq_len = input_ids.shape
        device = input_ids.device
        
        positions = torch.arange(seq_len, device=device).unsqueeze(0).expand(batch_size, -1)
        x = self.token_embed(input_ids) + self.pos_embed(positions)
        
        for block in self.blocks:
            x = block(x)
        
        x = self.norm(x)
        logits = self.head(x)
        
        if labels is not None:
            # Causal LM loss - shift by 1
            shift_logits = logits[..., :-1, :].contiguous()
            shift_labels = labels[..., 1:].contiguous()
            loss = F.cross_entropy(
                shift_logits.view(-1, shift_logits.size(-1)),
                shift_labels.view(-1),
                ignore_index=-100
            )
            return loss, logits
        
        return logits
    
    @torch.no_grad()
    def generate(self, input_ids: torch.Tensor, max_new_tokens: int = 100,
                 temperature: float = 1.0, top_k: Optional[int] = None) -> torch.Tensor:
        """
        Autoregressive generation
        """
        for _ in range(max_new_tokens):
            logits = self.forward(input_ids)
            next_token_logits = logits[:, -1, :] / temperature
            
            # Optional top-k sampling
            if top_k is not None:
                v, _ = torch.topk(next_token_logits, top_k)
                next_token_logits[next_token_logits < v[:, [-1]]] = float('-inf')
            
            # Sample next token
            probs = F.softmax(next_token_logits, dim=-1)
            next_token = torch.multinomial(probs, num_samples=1)
            
            input_ids = torch.cat([input_ids, next_token], dim=-1)
        
        return input_ids


# =============================================================================
# Energy Calculation
# =============================================================================

def calculate_energy_consumption(model: nn.Module, input_shape: Tuple[int, ...],
                                  firing_rates: Optional[dict] = None,
                                  time_steps: int = 4) -> float:
    """
    Calculate theoretical energy consumption in millijoules
    
    Args:
        model: SNN model
        input_shape: (batch, seq_len, dim)
        firing_rates: Dict of layer names to firing rates (default: 0.1)
        time_steps: Number of simulation time steps
    
    Returns:
        Energy in mJ
    """
    E_MAC = 4.6e-12  # 4.6 pJ per MAC
    E_AC = 0.9e-12   # 0.9 pJ per AC
    
    if firing_rates is None:
        firing_rates = {}
    
    total_energy = 0.0
    total_ops = 0
    
    for name, module in model.named_modules():
        if isinstance(module, nn.Linear):
            in_features = module.in_features
            out_features = module.out_features
            
            # For SNN: MAC -> AC with firing rate
            fr = firing_rates.get(name, 0.1)
            ops = in_features * out_features
            
            # SNN uses AC operations
            energy = ops * E_AC * fr * time_steps
            total_energy += energy
            total_ops += ops
    
    # Convert to millijoules
    return total_energy * 1000


# =============================================================================
# Example Usage
# =============================================================================

def demo_we_spikingformer():
    """Demonstrate WE-Spikingformer usage"""
    print("=" * 60)
    print("WE-Spikingformer Demo (Masked Language Modeling)")
    print("=" * 60)
    
    # Model configuration
    vocab_size = 30522  # BERT vocab size
    batch_size = 2
    seq_len = 128
    
    # Create model
    model = WESpikingformer(
        vocab_size=vocab_size,
        dim=768,
        depth=12,
        num_heads=12,
        max_seq_len=512,
        time_steps=4,
        wta_method="hard"
    )
    
    # Dummy input
    input_ids = torch.randint(0, vocab_size, (batch_size, seq_len))
    labels = torch.randint(0, vocab_size, (batch_size, seq_len))
    
    # Forward pass
    loss, logits = model(input_ids, labels)
    
    print(f"Input shape: {input_ids.shape}")
    print(f"Output logits shape: {logits.shape}")
    print(f"Loss: {loss.item():.4f}")
    
    # Energy calculation
    energy = calculate_energy_consumption(
        model, 
        (batch_size, seq_len, 768),
        firing_rates={'fc1': 0.12, 'fc2': 0.15},
        time_steps=4
    )
    print(f"Estimated energy: {energy:.2f} mJ")
    
    # Count parameters
    num_params = sum(p.numel() for p in model.parameters())
    print(f"Total parameters: {num_params / 1e6:.2f}M")
    
    return model


def demo_wd_spikingformer():
    """Demonstrate WD-Spikingformer usage"""
    print("\n" + "=" * 60)
    print("WD-Spikingformer Demo (Causal Language Modeling)")
    print("=" * 60)
    
    # Model configuration
    vocab_size = 50257  # GPT-2 vocab size
    batch_size = 2
    seq_len = 64
    
    # Create model (0.4B parameters)
    model = WDSpikingformer(
        vocab_size=vocab_size,
        dim=1024,
        depth=24,
        num_heads=16,
        max_seq_len=2048,
        time_steps=4,
        wta_method="hard"
    )
    
    # Dummy input
    input_ids = torch.randint(0, vocab_size, (batch_size, seq_len))
    labels = torch.randint(0, vocab_size, (batch_size, seq_len))
    
    # Forward pass
    loss, logits = model(input_ids, labels)
    
    print(f"Input shape: {input_ids.shape}")
    print(f"Output logits shape: {logits.shape}")
    print(f"Loss: {loss.item():.4f}")
    
    # Energy calculation
    energy = calculate_energy_consumption(
        model,
        (batch_size, seq_len, 1024),
        firing_rates={'fc1': 0.10, 'fc2': 0.12},
        time_steps=4
    )
    print(f"Estimated energy: {energy:.2f} mJ")
    
    # Count parameters
    num_params = sum(p.numel() for p in model.parameters())
    print(f"Total parameters: {num_params / 1e6:.2f}M")
    
    # Generation example
    print("\nGeneration example:")
    prompt = torch.randint(0, vocab_size, (1, 10))
    generated = model.generate(prompt, max_new_tokens=20, temperature=1.0)
    print(f"Prompt length: {prompt.shape[1]}")
    print(f"Generated length: {generated.shape[1]}")
    
    return model


def demo_training_step():
    """Demonstrate a single training step"""
    print("\n" + "=" * 60)
    print("Training Step Demo")
    print("=" * 60)
    
    vocab_size = 1000
    model = WESpikingformer(
        vocab_size=vocab_size,
        dim=256,
        depth=4,
        num_heads=8,
        max_seq_len=128,
        time_steps=2  # Faster for demo
    )
    
    # Optimizer
    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-4, weight_decay=0.01)
    
    # Dummy batch
    batch_size = 4
    seq_len = 32
    input_ids = torch.randint(0, vocab_size, (batch_size, seq_len))
    labels = torch.randint(0, vocab_size, (batch_size, seq_len))
    
    # Training step
    model.train()
    optimizer.zero_grad()
    
    loss, logits = model(input_ids, labels)
    loss.backward()
    
    # Clip gradients
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    
    optimizer.step()
    
    print(f"Batch size: {batch_size}")
    print(f"Sequence length: {seq_len}")
    print(f"Loss: {loss.item():.4f}")
    print("Training step completed successfully!")


if __name__ == "__main__":
    # Run demos
    we_model = demo_we_spikingformer()
    wd_model = demo_wd_spikingformer()
    demo_training_step()
    
    print("\n" + "=" * 60)
    print("All demos completed successfully!")
    print("=" * 60)
