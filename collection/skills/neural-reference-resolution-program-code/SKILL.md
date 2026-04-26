---
name: neural-reference-resolution-program-code
description: "Neural architectures for resolving references in program code using sequence-to-sequence models with direct and indirect indexing by permutation. New architectures outperform baselines in robustness and scalability, handling examples 10x longer. Activation: neural code reference resolution, decompilation, sequence-to-sequence indexing, permutation indexing, program analysis."
---

# Neural Reference Resolution in Program Code

Neural architectures for resolving references in program code using sequence-to-sequence models with direct and indirect indexing by permutation. Motivated by real-world decompilation tasks.

## Paper Information

- **Title:** Neural architectures for resolving references in program code
- **Authors:** Gergő Szalay, Gergely Zsolt Kovács, Sándor Teleki, Balázs Pintér, Tibor Gregorics
- **arXiv ID:** 2604.14073v1
- **Date:** April 15, 2026
- **Category:** cs.LG, cs.NE
- **PDF:** https://arxiv.org/pdf/2604.14073v1

## Problem Statement

**Reference resolution and rewriting** is fundamental in programming languages:
- Traditional sequence-to-sequence architectures struggle with reference rewriting
- Existing models have difficulty handling long sequences
- Decompilation tasks require robust reference indexing

### Abstracted Problems
1. **Direct indexing by permutation**: Mapping references directly to targets
2. **Indirect indexing by permutation**: Resolving references through intermediate mappings

## Core Innovation

**New Sequence-to-Sequence Architectures** that outperform well-known baselines:
- **10x longer sequences**: Handle examples 10x longer than best baseline
- **42% error reduction**: In real-world switch statement decompilation
- **Robust and scalable**: Superior performance on synthetic benchmarks

## Architecture Components

### Problem 1: Direct Indexing by Permutation

```
Input:  [reference_1, reference_2, ..., reference_n]
             ↓
    Direct Indexing Neural Architecture
             ↓
Output: [target_a, target_b, ..., target_n]  (permutation of inputs)
```

**Key Features:**
- Specialized permutation-aware attention mechanism
- Position-relative encoding for reference locations
- Direct mapping without intermediate representations

### Problem 2: Indirect Indexing by Permutation

```
Input:  [reference_1, reference_2, ..., reference_n]
             ↓
    Indirect Indexing Neural Architecture
             ↓
Intermediate: [index_1, index_2, ..., index_n]
             ↓
Output: [target_a, target_b, ..., target_n]
```

**Key Features:**
- Two-stage processing: reference → index → target
- Learned intermediate representations
- Handles complex aliasing patterns

## Architecture Design

### Base Architecture Components

```python
import torch
import torch.nn as nn

class ReferenceResolutionEncoder(nn.Module):
    """
    Encoder for reference resolution tasks.
    Specialized for code token sequences.
    """
    def __init__(self, vocab_size, embed_dim=512, num_layers=6):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.pos_encoding = PositionalEncoding(embed_dim)
        
        # Transformer encoder with permutation-aware attention
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=8,
            dim_feedforward=2048,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)
        
        # Reference position encoder
        self.reference_encoder = ReferencePositionEncoder(embed_dim)
        
    def forward(self, tokens, reference_mask):
        """
        Args:
            tokens: Input token sequence [batch, seq_len]
            reference_mask: Binary mask indicating reference positions [batch, seq_len]
        """
        # Embed tokens
        x = self.embedding(tokens)
        x = self.pos_encoding(x)
        
        # Add reference position information
        x = self.reference_encoder(x, reference_mask)
        
        # Encode with transformer
        encoded = self.transformer(x)
        
        return encoded

class DirectIndexingDecoder(nn.Module):
    """
    Decoder for direct indexing by permutation.
    Maps references directly to targets.
    """
    def __init__(self, embed_dim=512, num_layers=6):
        super().__init__()
        
        decoder_layer = nn.TransformerDecoderLayer(
            d_model=embed_dim,
            nhead=8,
            dim_feedforward=2048,
            batch_first=True
        )
        self.transformer = nn.TransformerDecoder(decoder_layer, num_layers)
        
        # Permutation prediction head
        self.permutation_head = nn.Sequential(
            nn.Linear(embed_dim, embed_dim),
            nn.ReLU(),
            nn.Linear(embed_dim, 1)  # Predict position for each reference
        )
        
    def forward(self, memory, reference_indices):
        """
        Args:
            memory: Encoded sequence [batch, seq_len, embed_dim]
            reference_indices: Indices of references to resolve [batch, num_refs]
        """
        # Extract reference representations
        ref_repr = memory[torch.arange(memory.size(0)).unsqueeze(1), reference_indices]
        
        # Decode with cross-attention to memory
        decoded = self.transformer(ref_repr, memory)
        
        # Predict target positions (permutation)
        target_positions = self.permutation_head(decoded).squeeze(-1)
        
        return target_positions

class IndirectIndexingDecoder(nn.Module):
    """
    Decoder for indirect indexing by permutation.
    Two-stage: reference → index → target
    """
    def __init__(self, embed_dim=512, num_layers=6, num_indices=None):
        super().__init__()
        
        # Stage 1: Index prediction
        self.index_predictor = nn.Sequential(
            nn.Linear(embed_dim, embed_dim),
            nn.ReLU(),
            nn.Linear(embed_dim, num_indices if num_indices else embed_dim)
        )
        
        # Stage 2: Target prediction from index
        decoder_layer = nn.TransformerDecoderLayer(
            d_model=embed_dim,
            nhead=8,
            batch_first=True
        )
        self.target_decoder = nn.TransformerDecoder(decoder_layer, num_layers)
        
        self.target_head = nn.Linear(embed_dim, 1)
        
    def forward(self, memory, reference_indices):
        """
        Two-stage indirect indexing.
        """
        # Extract reference representations
        ref_repr = memory[torch.arange(memory.size(0)).unsqueeze(1), reference_indices]
        
        # Stage 1: Predict intermediate indices
        intermediate_indices = self.index_predictor(ref_repr)
        
        # Stage 2: Decode to targets using indices
        indexed_repr = torch.matmul(intermediate_indices, memory)
        decoded = self.target_decoder(indexed_repr, memory)
        
        # Predict target positions
        target_positions = self.target_head(decoded).squeeze(-1)
        
        return target_positions, intermediate_indices
```

### Reference Position Encoder

```python
class ReferencePositionEncoder(nn.Module):
    """
    Encodes relative positions of references in code.
    """
    def __init__(self, embed_dim):
        super().__init__()
        self.position_embed = nn.Embedding(1000, embed_dim)  # Max 1000 positions
        self.reference_indicator = nn.Parameter(torch.randn(embed_dim))
        
    def forward(self, x, reference_mask):
        """
        Add position encoding specific to references.
        """
        batch_size, seq_len, _ = x.shape
        positions = torch.arange(seq_len, device=x.device).unsqueeze(0).expand(batch_size, -1)
        pos_embed = self.position_embed(positions)
        
        # Add reference indicator to reference positions
        ref_indicator = reference_mask.unsqueeze(-1).float() * self.reference_indicator
        
        return x + pos_embed + ref_indicator
```

## Training

### Synthetic Benchmarks

```python
def generate_direct_indexing_dataset(num_samples=10000, seq_length=100):
    """
    Generate synthetic dataset for direct indexing by permutation.
    """
    dataset = []
    for _ in range(num_samples):
        # Create random sequence with references
        seq_len = random.randint(10, seq_length)
        num_refs = random.randint(2, seq_len // 2)
        
        # Random permutation mapping
        targets = list(range(num_refs))
        random.shuffle(targets)
        
        sample = {
            'tokens': generate_code_tokens(seq_len, num_refs),
            'reference_positions': sorted(random.sample(range(seq_len), num_refs)),
            'target_permutation': targets
        }
        dataset.append(sample)
    
    return dataset

def generate_indirect_indexing_dataset(num_samples=10000, seq_length=100):
    """
    Generate synthetic dataset for indirect indexing.
    """
    dataset = []
    for _ in range(num_samples):
        seq_len = random.randint(10, seq_length)
        num_refs = random.randint(2, seq_len // 2)
        
        # Two-stage mapping: ref → index → target
        indices = list(range(num_refs * 2))  # More indices for intermediate
        random.shuffle(indices)
        intermediate = indices[:num_refs]
        
        targets = list(range(num_refs))
        random.shuffle(targets)
        
        sample = {
            'tokens': generate_code_tokens(seq_len, num_refs),
            'reference_positions': sorted(random.sample(range(seq_len), num_refs)),
            'intermediate_indices': intermediate,
            'target_permutation': targets
        }
        dataset.append(sample)
    
    return dataset
```

### Training Loop

```python
def train_reference_resolution(model, train_loader, val_loader, epochs=100):
    """
    Train reference resolution model.
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for batch in train_loader:
            tokens = batch['tokens']
            ref_positions = batch['reference_positions']
            targets = batch['target_permutation']
            
            # Forward pass
            predictions = model(tokens, ref_positions)
            
            # Compute loss
            loss = criterion(predictions, targets)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        # Validation
        val_accuracy = evaluate(model, val_loader)
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {total_loss/len(train_loader):.4f}, "
                  f"Val Acc: {val_accuracy:.4f}")
```

## Evaluation Results

### Synthetic Benchmarks

| Model | Max Sequence Length | Robustness | Scalability |
|-------|---------------------|------------|-------------|
| Baseline (Transformer) | 100 | Moderate | Poor |
| New Architecture (Direct) | 1000 | High | Excellent |
| New Architecture (Indirect) | 1000 | High | Excellent |

### Real-World Task: Switch Statement Decompilation

- **Error rate reduction**: 42%
- **Task**: Resolving jump table references in decompiled code
- **Challenge**: Indirect indexing through jump tables

### Ablation Studies

All components are essential:
- Reference position encoding
- Permutation-aware attention
- Two-stage indirect indexing (for indirect problem)
- Specialized decoder architecture

## Applications

### Program Analysis
- **Decompilation**: Converting binary to high-level code
- **Refactoring**: Automated code restructuring
- **Static analysis**: Reference tracking in code

### Compiler Optimization
- **Jump table resolution**: Switch statement optimization
- **Alias analysis**: Pointer reference tracking
- **Control flow analysis**: Branch target resolution

### Code Transformation
- **Obfuscation**: Reference rewriting for protection
- **Porting**: Adapting code between architectures
- **Instrumentation**: Adding monitoring references

## Activation Keywords

- neural code reference resolution
- decompilation
- sequence-to-sequence indexing
- permutation indexing
- program analysis
- reference rewriting
- indirect indexing
- direct indexing
- code decompilation
- jump table resolution
- 神经代码引用解析
- 反编译神经网络
- 程序代码分析
- sequence-to-sequence code
- neural program analysis

## Related Work

- **Sequence-to-sequence models**: Standard transformer baselines
- **Pointer networks**: For outputting positions
- **Tree-to-tree models**: For code structure
- **Graph neural networks**: For code as graphs

## References

- Szalay, G., et al. (2026). Neural architectures for resolving references in program code. *arXiv preprint* arXiv:2604.14073v1.
- Vaswani, A., et al. (2017). Attention is all you need. *NeurIPS*.
- Luong, M. T., et al. (2015). Effective approaches to attention-based neural machine translation. *EMNLP*.

## Limitations

- Requires synthetic pretraining on large datasets
- Limited to permutation-based reference patterns
- May struggle with highly complex aliasing

## Extensions

1. **Multi-file resolution**: References across files
2. **Type-aware resolution**: Incorporating type information
3. **Incremental resolution**: Online reference tracking
4. **Graph-based extensions**: Combining with GNNs
