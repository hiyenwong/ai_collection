---
name: magnet-brain-structure-function-gnn
description: Multi-Scale Adaptive Graph Network (MAGNet) for learning structural-functional brain representations. Models structure-function coupling for cognitive insight.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [brain-network, structure-function, graph-attention, cognitive-insight, gnn, neuroimaging]
    source_paper: "Learning Structural-Functional Brain Representations through Multi-Scale Adaptive Graph Attention for Cognitive Insight (arXiv:2603.29967v1)"
---

# MAGNet: Multi-Scale Adaptive Graph for Brain Structure-Function

## Overview
MAGNet (Multi-scale Adaptive Graph Network) learns joint structural-functional brain representations through adaptive graph attention. By modeling how structural connectivity constrains and enables functional dynamics across multiple spatial scales, the framework provides cognitive insights into brain organization.

## Core Concepts

### Multi-Scale Architecture
- **Local Scale**: Regional connectivity patterns within brain modules
- **Mesoscale**: Inter-module connectivity and hub regions
- **Global Scale**: Whole-brain integration and small-world topology

### Adaptive Graph Attention
- Attention weights adapt based on both structural and functional features
- Learns which structural connections are most relevant for functional prediction
- Dynamic re-weighting across scales

### Structure-Function Coupling
- Structural connectome (from DTI) as graph scaffold
- Functional connectome (from fMRI) as node dynamics
- Coupling strength varies by region and cognitive state

## Implementation Pattern
```python
class MAGNet(nn.Module):
    def __init__(self, n_regions, n_scales=3, hidden_dim=128):
        super().__init__()
        self.scales = nn.ModuleList([
            ScaleAttention(n_regions, hidden_dim, scale_factor=2**i)
            for i in range(n_scales)
        ])
        self.fusion = nn.Linear(hidden_dim * n_scales, hidden_dim)
        self.decoder = nn.Linear(hidden_dim, n_regions)
    
    def forward(self, structural_conn, functional_signals):
        scale_features = []
        for scale_module in self.scales:
            feat = scale_module(structural_conn, functional_signals)
            scale_features.append(feat)
        fused = torch.cat(scale_features, dim=-1)
        fused = self.fusion(fused).relu()
        return self.decoder(fused)
```

## Applications
- Brain structure-function coupling analysis
- Cognitive trait prediction from neuroimaging
- Brain network biomarker discovery
- Personalized neuroscience

## Activation Keywords
- structure-function brain coupling, multi-scale brain network, adaptive graph attention brain, MAGNet brain model, structural connectome analysis, 脑结构功能耦合, 多尺度脑网络

## References
- Learning Structural-Functional Brain Representations through Multi-Scale Adaptive Graph Attention for Cognitive Insight
- Authors: Badhan Mazumder, Sir-Lord Wiafe, Aline Kotoski, Vince D. Calhoun, Dong Hye Ye
- Published: 2026-03-31
- arXiv: https://arxiv.org/abs/2603.29967v1

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

### Basic Magnet Brain Structure Function Gnn usage
```
User: "Help me with magnet brain structure function gnn"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed magnet brain structure function gnn assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
