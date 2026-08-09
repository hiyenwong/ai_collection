---
name: sparse-weight-decomposition-circuit-extraction
description: Sparse Weight Decomposition (SWD) for efficient circuit extraction from pretrained transformers. Reparameterizes linear projections by factorizing weight matrices into two sparse factors with shared intermediate coordinates as circuit units.
trigger_words:
  - sparse weight decomposition
  - swd
  - circuit extraction
  - mechanistic interpretability
  - transformer interpretability
---

# Sparse Weight Decomposition (SWD) for Efficient Circuit Extraction

## Overview
Sparse Weight Decomposition (SWD) addresses the challenge that dense pretrained transformers do not naturally expose interpretable units for circuit extraction. SWD reparameterizes pretrained linear projections by factorizing each weight matrix into two sparse factors whose shared intermediate coordinates serve as individually addressable circuit units.

## Key Advantages Over Existing Approaches
- **No Separate Training**: Unlike methods that train auxiliary sparse representations, SWD works directly on pretrained models
- **Minimal Data Usage**: Uses less than 1% of the data required by Transcoder and other strong baselines
- **Zero-Data Variant**: Features a zero-data variant enabling broader mechanistic interpretability analysis
- **High Fidelity**: Matches held-out fidelity of strong baselines while being more data-efficient
- **Fewer Units**: Achieves same circuit sufficiency and necessity targets with fewer active read/write edges and selected units

## Technical Implementation

### Weight Matrix Factorization
For a weight matrix W ∈ ℝ^(m×n), SWD factorizes it as:
```
W ≈ A × B
```
Where:
- A ∈ ℝ^(m×k) is sparse (input-to-intermediate projection)
- B ∈ ℝ^(k×n) is sparse (intermediate-to-output projection)  
- k is the number of circuit units (intermediate coordinates)
- The shared intermediate coordinates serve as interpretable circuit units

### Sparsity Constraints
- Both factors A and B are constrained to be sparse
- Sparsity patterns can be learned or predefined based on domain knowledge
- The intermediate dimension k controls the granularity of circuit units

### Full-Model Replacement
- SWD can replace all attention and MLP weight matrices in a transformer
- After factorization, nonzero factor values can be fine-tuned to maintain performance
- Enables comprehensive circuit analysis across the entire model

## Implementation Guidelines

### For Circuit Extraction Workflows
1. **Matrix Selection**: Identify target linear projections (attention heads, MLP layers, etc.)
2. **Factorization**: Apply SWD to factorize each weight matrix into sparse factors
3. **Unit Scoring**: Score intermediate circuit units based on their contribution to model outputs
4. **Selection**: Select top-k units based on scoring criteria
5. **Ablation**: Perform ablation studies to validate circuit sufficiency and necessity

### Code Implementation
```python
class SparseWeightDecomposition(nn.Module):
    def __init__(self, input_dim, output_dim, num_units, sparsity_level=0.1):
        super().__init__()
        self.num_units = num_units
        # Sparse input-to-units projection
        self.A = SparseLinear(input_dim, num_units, sparsity=sparsity_level)
        # Sparse units-to-output projection  
        self.B = SparseLinear(num_units, output_dim, sparsity=sparsity_level)
    
    def forward(self, x):
        # x -> units -> output
        units = self.A(x)
        output = self.B(units)
        return output, units  # Return units for circuit analysis
    
    def factorize_from_pretrained(self, pretrained_weight):
        # Initialize A and B to approximate pretrained_weight
        # Can use SVD, NMF, or other matrix factorization methods
        # Then apply sparsity constraints
        pass
```

### Zero-Data Variant
For scenarios where no data is available:
- Use structural properties of the weight matrix for factorization
- Apply regularization to encourage meaningful unit structure
- Enable per-step analysis without requiring training data

## Use Cases
- **Mechanistic Interpretability**: Analyzing internal mechanisms of pretrained transformers
- **Circuit Discovery**: Identifying interpretable computational units in large models
- **Model Compression**: Sparse factorization can also serve compression purposes
- **Per-Step Analysis**: Zero-data variant enables analysis of individual inference steps
- **Cross-Model Analysis**: Apply consistent circuit extraction across different model families (GPT-2, Qwen, etc.)

## Evaluation Metrics
- **Held-out Fidelity**: Reconstruction accuracy on unseen data
- **Circuit Sufficiency**: Performance when using only selected circuit units
- **Circuit Necessity**: Performance degradation when ablating selected units
- **Unit Efficiency**: Number of active units needed to achieve target performance
- **Edge Efficiency**: Number of active read/write edges in the circuit

## Supported Models
- GPT-2 family
- Qwen2.5 
- Qwen3.5-27B
- Other transformer architectures with linear projections

## References
- arXiv:2608.03913 - Sparse Weight Decomposition for Efficient Circuit Extraction

## Activation
Use when performing mechanistic interpretability analysis on pretrained transformers and needing efficient, data-minimal circuit extraction without training separate replacement networks.