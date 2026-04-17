# Implementation Patterns: WTA Spiking Transformer for Language Modeling

## 1. Winner-Take-All Spiking Self-Attention (WSSA)

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Optional

class WTAAttention(nn.Module):
    """Winner-Take-All attention mechanism — softmax-free spike-driven attention.
    
    Instead of computing softmax(QK^T/sqrt(d))V, WTA selects top-k competing
    attention weights per query, zeroing out the rest. This produces sparse,
    spike-like attention patterns suitable for neuromorphic deployment.
    """
    def __init__(self, dim: int, num_heads: int = 8, k_ratio: float = 0.25):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = dim // num_heads
        self.scale = self.head_dim ** -0.5
        self.k_ratio = k_ratio  # fraction of winners to keep
        
        self.q_proj = nn.Linear(dim, dim)
        self.k_proj = nn.Linear(dim, dim)
        self.v_proj = nn.Linear(dim, dim)
        self.out_proj = nn.Linear(dim, dim)
        
    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor,
                mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """WTA-based attention without softmax.
        
        Args:
            q, k, v: (B, L, D) query, key, value
            mask: optional (B, L, L) attention mask
            
        Returns:
            (B, L, D) output
        """
        B, L, D = q.shape
        H = self.num_heads
        d = self.head_dim
        
        # Linear projections and reshape to heads
        Q = self.q_proj(q).view(B, L, H, d).transpose(1, 2)  # (B, H, L, d)
        K = self.k_proj(k).view(B, L, H, d).transpose(1, 2)
        V = self.v_proj(v).view(B, L, H, d).transpose(1, 2)
        
        # Attention scores
        scores = torch.matmul(Q, K.transpose(-2, -1)) * self.scale  # (B, H, L, L)
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        
        # WTA selection: keep top-k scores per query, zero the rest
        k_winners = max(1, int(self.k_ratio * L))
        
        # Create WTA mask: top-k per row, rest masked to zero
        topk_values, topk_indices = scores.topk(k_winners, dim=-1)
        wta_mask = torch.zeros_like(scores)
        wta_mask.scatter_(-1, topk_indices, 1.0)
        
        # Apply WTA: zero out non-winners, keep winners unnormalized
        sparse_scores = scores * wta_mask
        
        # Compute attention output (no softmax — raw weighted sum of winners)
        attn_output = torch.matmul(sparse_scores, V)  # (B, H, L, d)
        
        # Reshape and project
        attn_output = attn_output.transpose(1, 2).contiguous().view(B, L, D)
        return self.out_proj(attn_output)
```

## 2. Causal WTA Spiking Self-Attention (CWSSA)

```python
class CausalWTAAttention(WTAAttention):
    """Causal WTA attention for autoregressive/decoder-only language modeling.
    
    Extends WTA with causal masking: each token only attends to itself
    and preceding tokens. WTA competition happens within the causal window.
    """
    def __init__(self, dim: int, num_heads: int = 8, k_ratio: float = 0.25):
        super().__init__(dim, num_heads, k_ratio)
        
    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        """Causal WTA attention with triangular mask.
        
        Args:
            q, k, v: (B, L, D) for decoder sequence
            
        Returns:
            (B, L, D) output
        """
        B, L, D = q.shape
        H = self.num_heads
        d = self.head_dim
        
        Q = self.q_proj(q).view(B, L, H, d).transpose(1, 2)
        K = self.k_proj(k).view(B, L, H, d).transpose(1, 2)
        V = self.v_proj(v).view(B, L, H, d).transpose(1, 2)
        
        scores = torch.matmul(Q, K.transpose(-2, -1)) * self.scale
        
        # Causal mask: upper triangle = -inf
        causal_mask = torch.tril(torch.ones(L, L, device=q.device, dtype=torch.bool))
        causal_mask = causal_mask.unsqueeze(0).unsqueeze(0)  # (1, 1, L, L)
        scores = scores.masked_fill(~causal_mask, float('-inf'))
        
        # WTA within causal window: k_winners from allowed positions only
        k_winners = max(1, int(self.k_ratio * L))
        
        topk_values, topk_indices = scores.topk(k_winners, dim=-1)
        wta_mask = torch.zeros_like(scores)
        wta_mask.scatter_(-1, topk_indices, 1.0)
        
        sparse_scores = scores * wta_mask
        attn_output = torch.matmul(sparse_scores, V)
        
        attn_output = attn_output.transpose(1, 2).contiguous().view(B, L, D)
        return self.out_proj(attn_output)
```

## 3. Spiking Feed-Forward Network

```python
class SpikingActivation(torch.autograd.Function):
    """Differentiable spiking activation for training.
    
    Forward: binary spike (1 if input > 0, else 0)
    Backward: surrogate gradient for BPTT
    """
    @staticmethod
    def forward(ctx, x, threshold=0.5, width=1.0):
        ctx.save_for_backward(x)
        ctx.threshold = threshold
        ctx.width = width
        return (x > threshold).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        x, = ctx.saved_tensors
        # Surrogate gradient: smooth sigmoid derivative
        grad = grad_output * torch.exp(-ctx.width * (x - ctx.threshold).abs())
        return grad

class SpikingFFN(nn.Module):
    """Spiking feed-forward network replacing ReLU/GeGLU in transformers.
    
    Uses spiking activation between linear layers for energy efficiency.
    """
    def __init__(self, dim: int, hidden_dim: int = None, dropout: float = 0.1):
        super().__init__()
        hidden_dim = hidden_dim or dim * 4
        self.fc1 = nn.Linear(dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, dim)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.fc1(x)
        h = SpikingActivation.apply(h)  # spiking nonlinearity
        h = self.dropout(h)
        h = self.fc2(h)
        return h
```

## 4. WE-Spikingformer (Encoder-only for MLM)

```python
class SpikingTransformerBlock(nn.Module):
    """Single spiking transformer block with WTA attention + spiking FFN."""
    def __init__(self, dim: int, num_heads: int, mlp_ratio: float = 4.0,
                 dropout: float = 0.1, k_ratio: float = 0.25,
                 causal: bool = False):
        super().__init__()
        AttnClass = CausalWTAAttention if causal else WTAAttention
        self.attn = AttnClass(dim, num_heads, k_ratio=k_ratio)
        self.norm1 = nn.LayerNorm(dim)
        self.norm2 = nn.LayerNorm(dim)
        self.ffn = SpikingFFN(dim, int(dim * mlp_ratio), dropout)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Attention with residual
        x = x + self.dropout(self.attn(self.norm1(x), self.norm1(x), self.norm1(x)))
        # FFN with residual
        x = x + self.dropout(self.ffn(self.norm2(x)))
        return x

class WESpikingformer(nn.Module):
    """WE-Spikingformer: Encoder-only spiking transformer for masked language modeling.
    
    Architecture:
    - Embedding → Position Encoding → N Spiking Transformer Blocks → LM Head
    - Each block uses WSSA (bidirectional WTA attention) + spiking FFN
    - Trained with MLM objective (masked token prediction)
    """
    def __init__(self, vocab_size: int, dim: int = 768, num_heads: int = 12,
                 num_layers: int = 12, max_seq_len: int = 512,
                 dropout: float = 0.1, k_ratio: float = 0.25):
        super().__init__()
        self.token_embed = nn.Embedding(vocab_size, dim)
        self.pos_embed = nn.Embedding(max_seq_len, dim)
        self.dropout = nn.Dropout(dropout)
        
        self.blocks = nn.ModuleList([
            SpikingTransformerBlock(dim, num_heads, dropout=dropout,
                                   k_ratio=k_ratio, causal=False)
            for _ in range(num_layers)
        ])
        
        self.norm = nn.LayerNorm(dim)
        self.lm_head = nn.Linear(dim, vocab_size, bias=False)
        self.lm_head.weight = self.token_embed.weight  # tied embeddings
        
    def forward(self, input_ids: torch.Tensor, mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        """Forward pass for masked language modeling.
        
        Args:
            input_ids: (B, L) token IDs (with [MASK] tokens)
            mask: (B, L) attention mask (1 = visible, 0 = masked out)
            
        Returns:
            logits: (B, L, vocab_size) token prediction logits
        """
        B, L = input_ids.shape
        positions = torch.arange(L, device=input_ids.device).unsqueeze(0).expand(B, -1)
        
        h = self.token_embed(input_ids) + self.pos_embed(positions)
        h = self.dropout(h)
        
        for block in self.blocks:
            h = block(h)
        
        h = self.norm(h)
        logits = self.lm_head(h)
        return logits
    
    def mlm_loss(self, input_ids: torch.Tensor, labels: torch.Tensor,
                 attention_mask: torch.Tensor) -> torch.Tensor:
        """Compute masked language modeling loss.
        
        Only compute loss on masked positions (labels != -100).
        """
        logits = self.forward(input_ids, attention_mask)
        loss_fn = nn.CrossEntropyLoss(ignore_index=-100)
        return loss_fn(logits.view(-1, logits.size(-1)), labels.view(-1))
```

## 5. WD-Spikingformer (Decoder-only for CLM)

```python
class WDSpikingformer(nn.Module):
    """WD-Spikingformer: Decoder-only spiking transformer for causal language modeling.
    
    Architecture:
    - Embedding → Position Encoding → N Causal Spiking Transformer Blocks → LM Head
    - Each block uses CWSSA (causal WTA attention) + spiking FFN
    - Trained with CLM objective (next token prediction)
    """
    def __init__(self, vocab_size: int, dim: int = 768, num_heads: int = 12,
                 num_layers: int = 12, max_seq_len: int = 1024,
                 dropout: float = 0.1, k_ratio: float = 0.25):
        super().__init__()
        self.token_embed = nn.Embedding(vocab_size, dim)
        self.pos_embed = nn.Embedding(max_seq_len, dim)
        self.dropout = nn.Dropout(dropout)
        
        self.blocks = nn.ModuleList([
            SpikingTransformerBlock(dim, num_heads, dropout=dropout,
                                   k_ratio=k_ratio, causal=True)
            for _ in range(num_layers)
        ])
        
        self.norm = nn.LayerNorm(dim)
        self.lm_head = nn.Linear(dim, vocab_size, bias=False)
        self.lm_head.weight = self.token_embed.weight
        
    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        """Forward pass for causal language modeling.
        
        Args:
            input_ids: (B, L) token IDs
            
        Returns:
            logits: (B, L, vocab_size) next-token prediction logits
        """
        B, L = input_ids.shape
        positions = torch.arange(L, device=input_ids.device).unsqueeze(0).expand(B, -1)
        
        h = self.token_embed(input_ids) + self.pos_embed(positions)
        h = self.dropout(h)
        
        for block in self.blocks:
            h = block(h)
        
        h = self.norm(h)
        logits = self.lm_head(h)
        return logits
    
    def clm_loss(self, input_ids: torch.Tensor) -> torch.Tensor:
        """Compute causal language modeling loss (next token prediction).
        
        Shift: predict token[i+1] from token[:i].
        """
        logits = self.forward(input_ids[:, :-1])
        labels = input_ids[:, 1:]
        loss_fn = nn.CrossEntropyLoss()
        return loss_fn(logits.view(-1, logits.size(-1)), labels.view(-1))
```

## 6. Training Pipeline for NLP Tasks

```python
def train_mlm(model: WESpikingformer,
              train_dataloader: torch.utils.data.DataLoader,
              n_epochs: int = 10,
              lr: float = 5e-5,
              mask_prob: float = 0.15) -> list[float]:
    """Train WE-Spikingformer on masked language modeling.
    
    Args:
        model: WESpikingformer
        train_dataloader: yields (input_ids, attention_mask, labels)
        mask_prob: probability of masking each token
    """
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.01)
    losses = []
    
    for epoch in range(n_epochs):
        model.train()
        epoch_loss = 0.0
        
        for batch in train_dataloader:
            input_ids, attention_mask, labels = batch
            
            # Apply random masking
            masked_input = apply_mlm_mask(input_ids, mask_prob)
            
            loss = model.mlm_loss(masked_input, labels, attention_mask)
            
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            
            epoch_loss += loss.item()
        
        avg_loss = epoch_loss / len(train_dataloader)
        losses.append(avg_loss)
        
    return losses

def apply_mlm_mask(input_ids: torch.Tensor, mask_prob: float,
                   mask_token_id: int = 100,
                   vocab_size: int = 30522) -> torch.Tensor:
    """Apply MLM-style random masking: 80% mask, 10% random, 10% keep."""
    masked = input_ids.clone()
    mask = torch.rand_like(input_ids, dtype=torch.float) < mask_prob
    
    # 80% → mask token, 10% → random token, 10% → keep original
    rand = torch.rand_like(input_ids, dtype=torch.float)
    
    # Mask
    mask_80 = mask & (rand < 0.8)
    masked[mask_80] = mask_token_id
    
    # Random replace
    rand_10 = mask & ((rand >= 0.8) & (rand < 0.9))
    masked[rand_10] = torch.randint(0, vocab_size, (rand_10.sum(),), device=input_ids.device)
    
    # Labels: -100 for non-masked, original token for masked
    labels = input_ids.clone()
    labels[~mask] = -100
    
    return masked

def train_clm(model: WDSpikingformer,
              train_dataloader: torch.utils.data.DataLoader,
              n_epochs: int = 10,
              lr: float = 5e-5) -> list[float]:
    """Train WD-Spikingformer on causal language modeling."""
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.01)
    losses = []
    
    for epoch in range(n_epochs):
        model.train()
        epoch_loss = 0.0
        
        for batch in train_dataloader:
            input_ids = batch
            
            loss = model.clm_loss(input_ids)
            
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            
            epoch_loss += loss.item()
        
        avg_loss = epoch_loss / len(train_dataloader)
        losses.append(avg_loss)
        
    return losses
```

## 7. Energy Efficiency Analysis

```python
def estimate_spike_sparsity(model: nn.Module, sample_input: torch.Tensor) -> dict:
    """Estimate energy efficiency by measuring spike sparsity across layers.
    
    WTA spiking transformers achieve energy savings through:
    1. Sparse attention (only k/N connections active per token)
    2. Binary spike activations (0 or 1, no multiply for zero inputs)
    3. Event-driven computation (only active neurons consume energy)
    """
    spike_counts = {}
    
    # Hook into spiking activations to count spikes
    def hook_fn(name):
        def hook(module, input, output):
            spike_counts[name] = output.mean().item()
        return hook
    
    handles = []
    for name, module in model.named_modules():
        if isinstance(module, SpikingFFN):
            handles.append(module.register_forward_hook(hook_fn(name)))
    
    with torch.no_grad():
        _ = model(sample_input)
    
    for h in handles:
        h.remove()
    
    return {
        'spike_rates': spike_counts,
        'avg_sparsity': sum(spike_counts.values()) / max(len(spike_counts), 1),
    }

def compare_energy_cost(softmax_attn_flops: int, wta_attn_flops: int,
                        seq_len: int, k_ratio: float = 0.25) -> dict:
    """Compare energy cost of softmax vs WTA attention.
    
    Softmax attention: O(L^2 * d) — full quadratic computation
    WTA attention: O(L * k * d) where k = k_ratio * L — sparse computation
    """
    k = int(k_ratio * seq_len)
    
    return {
        'softmax_flops': softmax_attn_flops,
        'wta_flops': wta_attn_flops,
        'reduction_factor': softmax_attn_flops / max(wta_attn_flops, 1),
        'sparse_connections': f"{k_ratio*100:.0f}% of connections active",
    }
```
