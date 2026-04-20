---
name: brain-dit-fmri-foundation-model-v4
description: Brain-DiT universal multi-state fMRI foundation model with metadata-conditioned pretraining. Supports multi-state brain activity generation and decoding. Trigger words: brain dit, fmri foundation model, multi-state, metadata conditioned, diffusion transformer, fMRI generation.
---

# Brain-DiT: Universal Multi-state fMRI Foundation Model

## Paper Reference
- **arXiv**: [2604.12683v1](https://arxiv.org/abs/2604.12683)
- **Authors**: Junfeng Xia, Wenhao Ye, Xuanye Pan et al.
- **Published**: 2026-04-14
- **Citations**: 0

## Core Insight

A unified diffusion transformer (DiT) architecture pretrained on diverse fMRI datasets with metadata conditioning serves as a foundation model for brain activity across multiple cognitive states, enabling both generation and decoding without task-specific training.

## Key Mechanism

1. **Diffusion Transformer**: Denoising diffusion with transformer backbone
2. **Metadata Conditioning**: Subject demographics, scan parameters, task labels as conditioning
3. **Multi-state Support**: Single model handles resting-state, task-fMRI, naturalistic stimulation
4. **Cross-subject Generalization**: Learn subject-invariant brain dynamics

## Implementation Pattern

```python
import torch
import torch.nn as nn

class BrainDiT(nn.Module):
    def __init__(self, n_regions=200, hidden=512, n_heads=8, n_layers=12):
        super().__init__()
        self.time_embed = nn.Sequential(nn.Linear(1, hidden), nn.SiLU(), nn.Linear(hidden, hidden))
        self.metadata_embed = nn.Sequential(nn.Linear(128, hidden), nn.LayerNorm(hidden))
        enc_layer = nn.TransformerEncoderLayer(d_model=hidden, nhead=n_heads, dim_feedforward=hidden*4, batch_first=True)
        self.transformer = nn.TransformerEncoder(enc_layer, num_layers=n_layers)
        self.input_proj = nn.Linear(n_regions, hidden)
        self.output_proj = nn.Linear(hidden, n_regions)
    
    def forward(self, x_noisy, t, metadata=None):
        t_emb = self.time_embed(t.unsqueeze(-1).float() / 1000.0)
        if metadata is not None:
            m_emb = self.metadata_embed(metadata)
            condition = t_emb + m_emb
        else:
            condition = t_emb
        h = self.input_proj(x_noisy).unsqueeze(1)
        condition = condition.unsqueeze(1)
        combined = torch.cat([condition, h], dim=1)
        output = self.transformer(combined)
        return self.output_proj(output[:, -1, :])
```

## Applications

- fMRI data generation for augmentation
- Cross-subject brain activity prediction
- Multi-state brain decoding
- Clinical fMRI analysis with limited data

## Related Skills

- [[brain-dit-universal-multi-state]]
- [[brain-dit-fmri-foundation-model]]
- [[multimodal-brain-connectivity-gnn]]

## Activation Keywords

- "brain-dit-fmri-foundation-model-v4"
- "brain dit fmri foundation model v4"
- "use brain dit fmri foundation model v4"
- "brain dit fmri foundation model v4 help"
- "brain dit fmri foundation model v4 tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Brain Dit Fmri Foundation Model V4 usage
```
User: "Help me with brain dit fmri foundation model v4"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed brain dit fmri foundation model v4 assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
