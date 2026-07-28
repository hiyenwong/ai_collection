---
name: universal-bci-personalization-api
description: "Universal BCI Personalization API for trunk-agnostic EEG foundation model integration. Provides one contract encode to Bayesian head to BrainState architecture that works across heterogeneous frozen EEG trunks without per-architecture personalization stacks. Use when implementing BCI systems that need to support multiple EEG encoder architectures (EEGNet, Shallow, Deep, Conformer, ATCNet, REVE) with a single personalization interface."
metadata:
  arxiv_id: "2607.22397"
  published: "2026-07-24"
  authors: "Nimbus Personalizer Team"
  tags: [bci, eeg, foundation-models, personalization, trunk-agnostic, brain-computer-interface]
license: Complete terms in LICENSE.txt
---

# Universal BCI Personalization API

## Overview

The Universal BCI Personalization API (Nimbus Personalizer) provides a trunk-agnostic contract that enables personalization across heterogeneous frozen EEG encoders without requiring per-model fine-tune defaults. This solves the scalability problem of proliferating frozen EEG encoders by providing one integration surface that works across both classical trunks and foundation model encoders.

**Core contribution**: The trunk-agnostic API surface—not the ML novelty of LDA-on-embeddings—that allows OEMs to integrate once and swap trunks without standing up new personalization stacks per architecture.

## Architecture

The Nimbus Personalizer follows a three-component contract:

1. **Encoder Boundary**: Any frozen mapping from trials to embedding rows Z ∈ R^(n×d)
   - Callable functions, sklearn transformers, or torch module methods
   - Adapters exist for BrainDecode-style trunks including foundation encoders like REVE
   
2. **Bayesian Head**: Default is LDA; QDA and Softmax are interchangeable alternatives
   - Modular design keeps heads as interchangeable parameters rather than hardcoded
   - LDA serves as safe default; head optimality is dataset- and stress-dependent
   
3. **App State**: Structured prediction object called BrainState containing:
   - Primary intent hypothesis
   - Normalized predictive uncertainty (empirically calibrated under shift)
   - Ranked alternatives suitable for downstream decision presets

## Key Benefits

- **Trunk Agnosticism**: Single integration point supports heterogeneous frozen trunks (EEGNet, Shallow, Deep, Conformer, ATCNet, REVE)
- **Cost Efficiency**: Orders of magnitude less adaptation wall time compared to fine-tuning or PEFT
- **Scalability**: OEMs integrate once and can swap trunks without changing personalization logic
- **Performance Recovery**: Recovers much of the fine-tune accuracy gain while maintaining calibration-only simplicity

## Implementation Workflow

### Step 1: Trunk Integration Setup
```python
# Define trunk-agnostic interface
class TrunkAgnosticPersonalizer:
    def __init__(self, trunk_config):
        self.contract_encoder = ContractEncoder(trunk_config.input_shape)
        self.bayesian_head = BayesianHead(num_classes=trunk_config.num_classes)
        self.brainstate = BrainState() if trunk_config.has_capacity else None
```

### Step 2: Contract Encoding
The contract encoder normalizes input EEG data to match the expected format of any trunk:
- Handles different sampling rates
- Normalizes channel configurations  
- Applies standardized preprocessing pipeline

### Step 3: Bayesian Head Calibration
The Bayesian head performs lightweight subject-specific adaptation:
- Uses LDA-on-embeddings as baseline approach
- Applies calibration only when data quality is sufficient (clean data detection)
- Maintains confidence intervals for reliability assessment

### Step 4: Optional BrainState Enhancement
When the trunk embedding has sufficient capacity, the BrainState affine transformation provides additional adaptation capability:
- Learned affine transformation in embedding space
- Optional component based on trunk capacity assessment
- Provides mid-point between calibration-only and full fine-tuning

## When to Use This Skill

Use when implementing BCI personalization systems that need to support multiple frozen EEG encoder architectures without per-model personalization pipelines. This skill is particularly valuable for:

- OEM integrators building BCI platforms supporting diverse encoder backends
- Researchers comparing personalization approaches across encoder families  
- Systems requiring scalable personalization without fine-tune/PEFT overhead per model
- Applications needing calibrated uncertainty for downstream decision making

## Empirical Validation

The same Personalizer surface runs successfully on:
- **Five classical trunks**: {EEGNet, Shallow, Deep, Conformer, ATCNet}
- **Four MI datasets**: 18 evaluation cells total
- **Foundation encoder**: REVE under the same surface without redesign

Key findings:
- Where embedding capacity exists, head adaptation is cheap mid-point vs warm-start FT/PEFT
- Calibration-only holds in 12/18 cells (clean already wins)
- Strict ordinal escalation is conditional (5/18), not the product headline
- Expected calibration error improves significantly under severe shift (BNCI 0.22→0.10, Zhou 0.27→0.09)

## Implementation Guidelines

### For Integrators

1. **Supply frozen encode function**: Provide callable that maps trials to embedding rows
2. **Choose head type**: LDA (default), QDA, or Softmax based on dataset characteristics  
3. **Configure escalation logic**: Use companion work [Musienko, 2026] for control layer decisions on when to spend labels or escalate

### For Downstream Consumers

- **Use BrainState fields**: Treat intent + uncertainty as inputs to observe–allocate–adapt loops
- **Do not specify allocation rules**: The public core exposes calibrated signals; control logic remains separate layer
- **Leverage uncertainty**: BrainState confidence field is empirically calibrated signal for controller action

## Pitfalls and Limitations

- **Exploratory results**: All findings are based on subject-level bootstrap without confirmatory statistical tests
- **Data quality dependency**: Performance gains require sufficient clean data for calibration
- **Capacity assessment**: Not all trunks benefit from BrainState - assess embedding capacity first
- **Companion work needed**: Decision logic for when to escalate to full adaptation is covered in separate control layer work

## Activation Keywords

- universal bci personalization
- trunk-agnostic eeg
- nimbus personalizer  
- frozen eeg trunks
- bci foundation models
- eeg encoder api
- heterogeneous bci integration

## References

- Original Paper: https://arxiv.org/abs/2607.22397
- Companion Control Layer: Forthcoming work on adaptation escalation decision logic
- Supported Trunks: EEGNet, Shallow, Deep, Conformer, ATCNet, REVE
- Experimental Datasets: Four MI datasets across 18 experimental cells