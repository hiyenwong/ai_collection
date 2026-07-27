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

This skill provides the implementation framework for the Nimbus Personalizer system described in arXiv:2607.22397. The core innovation is a trunk-agnostic API that enables BCI applications to integrate once and support multiple frozen EEG encoder architectures without requiring separate personalization stacks for each model.

## Core Architecture

The Nimbus Personalizer follows a three-tier architecture:

1. **Contract Encode Layer**: Standardized input encoding interface that normalizes EEG data across different trunk requirements
2. **Bayesian Head**: Lightweight adaptive head that performs subject-specific calibration using Bayesian inference
3. **BrainState (Optional)**: Affine mid-tier transformation layer for additional capacity when embedding space allows

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

## Usage Patterns

### For BCI Application Developers
```python
# Initialize personalizer once
personalizer = NimbusPersonalizer(trunk_type="conformer")

# Apply to any subject/session
calibrated_output = personalizer.calibrate(eeg_data, subject_id)

# Switch trunks without changing integration
personalizer.set_trunk("reve")  # Now uses REVE foundation model
```

### For EEG Trunk Developers  
```python
# Implement trunk interface
class MyEEGTrunk(TrunkInterface):
    def get_input_spec(self): return {"channels": 64, "samples": 1000}
    def get_embedding_capacity(self): return True  # Supports BrainState
    def forward(self, x): return self.model(x)
```

## Performance Considerations

- **Calibration-only mode**: Achieves 89-94% of fine-tune accuracy with 100x faster adaptation
- **BrainState mode**: Recovers 95-98% of fine-tune accuracy with 10x faster adaptation  
- **Clean data requirement**: Calibration-only holds in 12/18 experimental cells when data quality is sufficient
- **Confidence intervals**: Subject-level bootstrap provides reliability metrics for production deployment

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