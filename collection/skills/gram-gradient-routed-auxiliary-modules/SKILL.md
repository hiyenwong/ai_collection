---
name: gram-gradient-routed-auxiliary-modules
version: 1.0.0
description: GRAM (Gradient-Routed Auxiliary Modules) methodology for creating removable compartments for dual-use knowledge in AI models. Enables surgical control over model capabilities without affecting general performance.
tags: [safety, dual-use, knowledge-control, modular-training, gradient-routing]
trigger: When you need to control access to dual-use capabilities in AI models, create removable knowledge modules, or implement surgical capability control without retraining separate models.
---

# GRAM - Gradient-Routed Auxiliary Modules

## Overview
GRAM (Gradient-Routed Auxiliary Modules) is a training methodology that creates dedicated, removable compartments for dual-use knowledge in AI models. Instead of training separate filtered models for different deployment scenarios, GRAM enables a single model to be configured in multiple ways by adding extra neurons organized into modules, one per dual-use category.

## Core Concept
- **Modular Architecture**: Add extra neurons to every layer of a standard Transformer, divided into groups (modules) by dual-use category
- **Gradient Routing**: During training on dual-use data, only the relevant module updates while general-purpose weights are frozen
- **Knowledge Isolation**: Dual-use knowledge accumulates in dedicated modules rather than diffusing across the whole network
- **Surgical Removal**: Modules can be deleted post-training to remove specific capabilities without affecting general performance

## How GRAM Works

### Training Phase
1. **General Data**: Model learns normally across all weights when encountering general-purpose text
2. **Dual-Use Data**: When encountering dual-use category data (e.g., virology), only the relevant module updates
   - Model can **read** from general knowledge to make predictions
   - Only the **specific module** is allowed to **learn** from that text
   - General-purpose weights are temporarily frozen

### Post-Training Configuration
- **Module ON**: Keep module for trusted deployments requiring that capability
- **Module OFF**: Delete module to remove capability entirely
- **Multiple Categories**: With N dual-use categories, achieve 2^N different configurations from one training run

## Implementation Steps

### 1. Model Architecture Modification
```python
# Pseudocode for GRAM architecture
class GRAMTransformerLayer(nn.Module):
    def __init__(self, base_config, dual_use_categories):
        super().__init__()
        # Standard transformer components
        self.attention = MultiHeadAttention(base_config)
        self.mlp = MLP(base_config)
        
        # GRAM auxiliary modules - one per dual-use category
        self.aux_modules = nn.ModuleDict({
            category: nn.Linear(base_config.hidden_size, base_config.hidden_size)
            for category in dual_use_categories
        })
        
    def forward(self, x, active_categories=None):
        # Standard transformer forward pass
        x = self.attention(x) + x
        x = self.mlp(x) + x
        
        # Apply active auxiliary modules
        if active_categories:
            for category in active_categories:
                x = self.aux_modules[category](x) + x
                
        return x
```

### 2. Gradient Routing During Training
```python
# Pseudocode for gradient routing
def train_gram_step(model, batch, dual_use_classifier):
    # Classify batch content
    categories = dual_use_classifier.classify(batch.text)
    
    if categories:  # Dual-use content detected
        # Freeze general weights
        freeze_parameters(model.base_parameters())
        
        # Unfreeze only relevant modules
        for category in categories:
            unfreeze_parameters(model.aux_modules[category])
            
        # Forward and backward pass
        loss = compute_loss(model(batch))
        loss.backward()
        
        # Update only unfrozen parameters
        optimizer.step()
        
        # Restore all parameters to trainable
        unfreeze_all_parameters(model)
    else:  # General content
        # Standard training - all parameters update
        loss = compute_loss(model(batch))
        loss.backward()
        optimizer.step()
```

### 3. Module Management
```python
# Pseudocode for module operations
def configure_model_capabilities(model, enabled_categories):
    """Configure model by enabling/disabling modules"""
    model.active_categories = enabled_categories
    
def remove_module_permanently(model, category):
    """Permanently delete a module and its knowledge"""
    del model.aux_modules[category]
    
def export_configured_model(model, enabled_categories, path):
    """Export model with specific capabilities enabled"""
    configured_model = copy.deepcopy(model)
    configured_model.active_categories = enabled_categories
    save_model(configured_model, path)
```

## Testing and Validation Framework

### 1. Capability Isolation Testing
- **Module ON vs OFF**: Compare performance on dual-use tasks with module enabled vs disabled
- **General Performance**: Verify no degradation on non-dual-use tasks when modules are removed
- **Knowledge Recovery Resistance**: Test if removed knowledge can be recovered through fine-tuning

### 2. Scaling Validation
- **Model Size**: Test GRAM effectiveness across different model scales (50M to 5B+ parameters)
- **Category Count**: Validate with increasing numbers of dual-use categories
- **Compute Costs**: Measure training overhead and inference impact

### 3. Real-World Scenario Testing
- **Domain-Specific Evaluation**: Test on realistic dual-use domains (virology, cybersecurity, nuclear physics)
- **Downstream Task Performance**: Evaluate on actual applications rather than just next-token prediction
- **Adversarial Robustness**: Test resistance to attempts to bypass module removal

## Key Results from Anthropic Research

### Performance Metrics
- **Capability Removal**: Deleting modules removes capabilities as effectively as never training on that data
- **General Performance**: No degradation on general tasks when modules are removed
- **Recovery Resistance**: GRAM resists knowledge recovery better than post-hoc unlearning techniques
- **Scaling Benefits**: Gap between "module on" and "module off" widens as models get larger

### Experimental Domains
- **Synthetic**: Children's stories tagged by topic (proof of concept)
- **Realistic**: Web text, code, and scientific papers with four dual-use domains:
  - Virology
  - Cybersecurity  
  - Nuclear physics
  - Specialized programming language (proxy for dual-use code)

## Limitations and Considerations

### Current Limitations
- **Entanglement Challenge**: Some dual-use capabilities may be too entangled with general knowledge for clean separation
- **Frontier Scale**: Not yet tested at frontier model scale or in production pipelines
- **Evaluation Scope**: Current evaluations focus on next-token prediction rather than downstream tasks
- **Implementation Complexity**: Requires modifications to training infrastructure

### Practical Considerations
- **Category Definition**: Careful definition of dual-use categories is crucial
- **Data Classification**: Need reliable dual-use content classifier for training
- **Module Sizing**: Determine appropriate module capacity for each category
- **Training Overhead**: Additional computational cost during training phase

## Use Cases and Applications

### 1. Safety-Critical Deployments
- **Biosecurity Labs**: Enable virology module only for vetted researchers
- **Cybersecurity Teams**: Activate security module for authorized penetration testing
- **Nuclear Facilities**: Restrict nuclear physics knowledge to approved personnel

### 2. Regulatory Compliance
- **Geographic Restrictions**: Enable/disable capabilities based on local regulations
- **Industry Requirements**: Tailor model capabilities to specific industry compliance needs
- **Customer Segmentation**: Provide different capability sets to different customer tiers

### 3. Research and Development
- **Capability Analysis**: Study how specific knowledge affects model behavior
- **Ablation Studies**: Systematically remove capabilities to understand their contribution
- **Transfer Learning**: Share general knowledge while controlling specialized capabilities

## Key Activation Words
- **Safety**: dual-use knowledge control, capability removal, surgical safety
- **Training**: gradient routing, auxiliary modules, modular training
- **Deployment**: configurable models, removable capabilities, multi-tenant AI

## References
- Anthropic & AE Studio (2026). "An off switch for dual-use knowledge in AI models"
- Previous work on dual-use knowledge confinement in model weights
- Data filtering approaches for CBRN weapons information

## Example Implementation Pipeline

### Phase 1: Setup and Architecture
1. Define dual-use categories for your domain
2. Modify model architecture to include auxiliary modules
3. Implement dual-use content classifier
4. Set up gradient routing infrastructure

### Phase 2: Training
1. Train on mixed dataset (general + dual-use content)
2. Apply gradient routing during dual-use content processing
3. Monitor module specialization and knowledge isolation
4. Validate general performance preservation

### Phase 3: Configuration and Deployment
1. Create configuration profiles for different deployment scenarios
2. Test capability removal effectiveness
3. Validate resistance to knowledge recovery attacks
4. Deploy configured models to appropriate environments

GRAM represents a significant advance in AI safety by enabling precise, surgical control over model capabilities without the prohibitive cost of training multiple separate models.