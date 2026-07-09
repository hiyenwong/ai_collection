---
name: gram-dual-use-knowledge-control
description: Gradient-Routed Auxiliary Modules (GRAM) methodology for surgical control of dual-use knowledge in AI models. Enables removable knowledge compartments without retraining separate models.
tags: [ai-safety, knowledge-control, dual-use, gradient-routing, transformer-architecture]
created: 2026-07-09
source: https://www.anthropic.com/research/off-switch-dual-use
---

# GRAM: Gradient-Routed Auxiliary Modules for Dual-Use Knowledge Control

## Overview

GRAM (Gradient-Routed Auxiliary Modules) is a method for surgically controlling access to dual-use knowledge in AI models. It enables a single model to have removable knowledge compartments, allowing different capability configurations without training separate models.

## Core Methodology

### Architecture Design

1. **Auxiliary Module Addition**
   - Add extra neurons to every layer of a standard Transformer
   - These neurons form dedicated compartments for each category of dual-use knowledge
   - Modules are architecturally isolated from main processing pathways

2. **Gradient Routing During Training**
   - When learning from dual-use data, update ONLY the auxiliary modules
   - Main model weights remain unchanged for dual-use knowledge
   - Creates clean separation between general capabilities and restricted knowledge

3. **Removable Knowledge Compartments**
   - Each dual-use category gets its own removable module
   - Modules can be added/removed post-training without affecting base model
   - Enables one model → many capability configurations

## Key Benefits

- **Cost Efficiency**: Train once, deploy many configurations
- **Surgical Control**: Remove specific knowledge without affecting other capabilities
- **Flexibility**: Different deployments can have different capability sets
- **Preserves Performance**: Main model unaffected by dual-use knowledge additions/removals

## Implementation Considerations

### When to Use GRAM

- Multiple deployment scenarios requiring different capability sets
- Dual-use knowledge that needs surgical removal (e.g., biosecurity, cybersecurity)
- Cost-prohibitive to train separate models for each configuration
- Need to balance: limiting access, enabling trusted users, preserving performance

### Limitations

- Preliminary research (not yet applied to production models at Anthropic)
- Adds architectural complexity
- Requires careful gradient routing during training
- Effectiveness depends on clean separation of knowledge domains

## Use Cases

1. **Biosecurity**: Remove pathogen design knowledge for general deployment, retain for vetted research labs
2. **Cybersecurity**: Remove exploit knowledge for public models, retain for security teams
3. **Chemical/Biological Weapons**: Surgical removal of WMD-related knowledge
4. **Regulatory Compliance**: Different regional deployments with different capability sets

## Comparison to Alternatives

| Method | Pros | Cons |
|--------|------|------|
| **Filtering pretraining data** | Simple | Blunt instrument, expensive (need separate models) |
| **Refusal training + classifiers** | Easy to implement | Doesn't change underlying knowledge, jailbreakable |
| **GRAM** | Surgical, flexible, cost-efficient | More complex, preliminary research |

## Technical Details

- **Architecture**: Standard Transformer + auxiliary neurons per layer
- **Training**: Gradient routing isolates dual-use updates to auxiliary modules
- **Inference**: Modules can be physically removed or zeroed out
- **Overhead**: Minimal impact on main model performance

## Activation Triggers

Use this skill when working on:
- AI safety and knowledge control
- Dual-use capability management
- Model deployment with varying capability requirements
- Regulatory compliance for AI systems
- Surgical capability removal without retraining

## Related Concepts

- Knowledge compartmentalization
- Gradient routing
- Modular neural networks
- AI safety and alignment
- Dual-use technology governance
