---
name: fcn-llm-graph-tuning
description: >
  FCN-LLM: Empowering LLMs for Brain Functional Connectivity Network
  Understanding via Graph-level Multi-task Instruction Tuning. Covers the
  multi-scale FCN encoder, semantic projection into LLM, 19-attribute
  multi-paradigm instruction tuning, two-stage learning strategy, and
  zero-shot generalization. Based on arXiv 2603.01135.
category: "brain-llm-integration"
---

# FCN-LLM: Graph-level Multi-task Instruction Tuning for Brain FCN Understanding

## Overview

FCN-LLM is a framework that bridges the gap between brain functional connectivity networks (FCNs) derived from resting-state fMRI and large language models through **graph-level, multi-task instruction tuning**. It enables LLMs to directly understand FCNs by projecting multi-scale graph features into the LLM's semantic space and training on 19 subject-specific attributes spanning demographics, phenotypes, and psychiatric conditions.

**Paper**: FCN-LLM: Empower LLM for Brain Functional Connectivity Network Understanding via Graph-level Multi-task Instruction Tuning
**Authors**: Xingcan Hu, Wei Wang, Li Xiao
**arXiv**: 2603.01135 [cs.AI] (2026-03-01)

## Activation Keywords

- FCN-LLM
- brain FCN LLM
- graph instruction tuning
- functional connectivity LLM
- multi-task FCN tuning
- FCN-text alignment
- brain network LLM integration
- graph-level instruction tuning
- multi-scale FCN encoder

## Problem Statement

### The FCN-Text Modality Gap

Existing brain foundation models for functional connectivity networks do **not** align FCNs with the text modality, which limits the ability of LLMs to directly understand FCNs. This creates several problems:

| Problem | Impact |
|---------|--------|
| FCNs and text live in different representation spaces | LLMs cannot reason over brain network data |
| Supervised models are task-specific | Poor generalization across clinical tasks |
| No unified instruction interface | Each clinical prediction needs separate training |
| Black-box predictions | Limited interpretability for clinical use |

FCN-LLM solves this by introducing a **multi-scale FCN encoder + LLM projection + instruction tuning** pipeline that aligns graph-level brain network features with natural language semantics.

## Architecture

### Multi-Scale FCN Encoder

The encoder captures FCN structure at three hierarchical levels:

| Scale | Level | What It Captures |
|-------|-------|-----------------|
| **Brain-region** | Node-level | Individual ROI activity patterns and local connectivity |
| **Functional subnetwork** | Community-level | Within-network and between-network connectivity of canonical brain systems (DMN, FPN, SN, etc.) |
| **Whole-brain** | Graph-level | Global topology, small-worldness, efficiency, hub structure |

```python
class MultiScaleFCNEncoder(nn.Module):
    """Encodes FCNs at three scales for LLM projection."""
    
    def __init__(self, n_regions, hidden_dim):
        super().__init__()
        # Brain-region level: graph convolutions over ROI nodes
        self.region_encoder = GATConv(n_regions, hidden_dim)
        
        # Functional subnetwork level: pool by canonical networks
        self.subnetwork_pool = SubnetworkPool(n_regions, hidden_dim, n_networks=7)
        
        # Whole-brain level: global graph pooling
        self.global_pool = GlobalAttention(hidden_dim)
        
    def forward(self, fc_matrix, node_features, subnetwork_assignments):
        # Level 1: Node-level representations
        region_feats = self.region_encoder(node_features, fc_matrix)
        
        # Level 2: Subnetwork-level representations
        subnet_feats = self.subnetwork_pool(region_feats, subnetwork_assignments)
        
        # Level 3: Whole-brain representation
        global_feat = self.global_pool(region_feats)
        
        return region_feats, subnet_feats, global_feat
```

### Semantic Space Projection

FCN embeddings are projected into the LLM's token embedding space:

```python
class FCN2LLMProjector(nn.Module):
    """Projects multi-scale FCN features into LLM semantic space."""
    
    def __init__(self, encoder_dim, llm_hidden_dim):
        super().__init__()
        self.region_projector = nn.Sequential(
            nn.Linear(encoder_dim, llm_hidden_dim),
            nn.GELU(),
            nn.Linear(llm_hidden_dim, llm_hidden_dim)
        )
        self.subnet_projector = nn.Sequential(
            nn.Linear(encoder_dim, llm_hidden_dim),
            nn.GELU(),
            nn.Linear(llm_hidden_dim, llm_hidden_dim)
        )
        self.global_projector = nn.Sequential(
            nn.Linear(encoder_dim, llm_hidden_dim),
            nn.GELU(),
            nn.Linear(llm_hidden_dim, llm_hidden_dim)
        )
        
    def forward(self, region_feats, subnet_feats, global_feat):
        """Return soft tokens for LLM input."""
        region_tokens = self.region_projector(region_feats)  # [n_regions, d]
        subnet_tokens = self.subnet_projector(subnet_feats)   # [n_networks, d]
        global_token  = self.global_projector(global_feat)     # [1, d]
        return region_tokens, subnet_tokens, global_token
```

The projected features are concatenated as **soft tokens** prepended to the instruction prompt, enabling the LLM to attend to both graph features and text instructions simultaneously.

## Multi-Paradigm Instruction Tasks

### 19 Subject-Specific Attributes

The instruction tuning covers 19 attributes across three categories:

#### Demographics (6 attributes)
| # | Attribute | Type | Example Instruction |
|---|-----------|------|-------------------|
| 1 | Age | Continuous/regression | "Predict the age of this subject from their FCN." |
| 2 | Sex | Binary classification | "Is this subject male or female?" |
| 3 | Education years | Continuous/regression | "Estimate the education level." |
| 4 | Handedness | Categorical | "Is this subject right-handed or left-handed?" |
| 5 | Race/ethnicity | Multi-class | "Classify the subject's racial background." |
| 6 | Site/scanner | Multi-class | "Which acquisition site produced this FCN?" |

#### Phenotypes (7 attributes)
| # | Attribute | Type | Example Instruction |
|---|-----------|------|-------------------|
| 7  | Cognitive score (general) | Continuous | "Estimate the general cognitive ability score." |
| 8  | Processing speed | Continuous | "Predict the processing speed index." |
| 9  | Working memory | Continuous | "Estimate working memory capacity." |
| 10 | Executive function | Continuous | "Predict executive function performance." |
| 11 | Sleep quality | Ordinal | "Rate the subject's sleep quality." |
| 12 | Physical activity | Continuous | "Estimate weekly physical activity level." |
| 13 | BMI | Continuous | "Predict the body mass index." |

#### Psychiatric Conditions (6 attributes)
| # | Attribute | Type | Example Instruction |
|---|-----------|------|-------------------|
| 14 | Depression severity | Continuous/ordinal | "Assess depression symptom severity." |
| 15 | Anxiety severity | Continuous/ordinal | "Assess anxiety symptom severity." |
| 16 | ADHD symptoms | Continuous | "Predict ADHD symptom score." |
| 17 | Psychosis risk | Binary/continuous | "Evaluate psychosis risk level." |
| 18 | Substance use | Binary/continuous | "Assess substance use patterns." |
| 19 | Overall mental health | Ordinal | "Rate overall mental health status." |

### Instruction Template

```python
def format_fcn_instruction(attribute, fc_tokens, instruction_type="predict"):
    """Format FCN + instruction for LLM input."""
    templates = {
        "predict": f"<FCN>{fc_tokens}</FCN> Based on the brain functional connectivity network, {attribute}?",
        "describe": f"<FCN>{fc_tokens}</FCN> Describe the brain connectivity patterns associated with {attribute}.",
        "compare": f"<FCN>{fc_tokens}</FCN> Compare this subject's {attribute} profile to the population average.",
        "explain": f"<FCN>{fc_tokens}</FCN> Explain which brain regions contribute most to {attribute}."
    }
    return templates.get(instruction_type, templates["predict"])
```

## Multi-Stage Learning Strategy

### Stage 1: FCN-LLM Alignment

**Goal**: Align FCN embeddings with the LLM's semantic space while freezing the LLM.

```python
def stage1_alignment(fcn_encoder, projector, llm, dataloader, epochs=5):
    """Freeze LLM, train encoder + projector to align FCN features."""
    freeze_params(llm)  # LLM weights frozen
    trainable = [fcn_encoder, projector]
    
    optimizer = AdamW(get_trainable_params(trainable), lr=1e-4)
    
    for epoch in range(epochs):
        for batch in dataloader:
            # Encode FCN
            region_feats, subnet_feats, global_feat = fcn_encoder(
                batch.fc_matrix, batch.node_features, batch.subnetwork_assignments
            )
            
            # Project to LLM space
            region_tokens, subnet_tokens, global_token = projector(
                region_feats, subnet_feats, global_feat
            )
            
            # Prepare LLM input: soft tokens + instruction + target
            llm_input = torch.cat([
                region_tokens, subnet_tokens, global_token,  # FCN soft tokens
                batch.instruction_embeddings                    # Text instruction
            ], dim=1)
            
            loss = compute_alignment_loss(llm, llm_input, batch.target_text)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

**Key characteristics**:
- Only the FCN encoder and projector are trained
- The LLM acts as a fixed "teacher" providing the semantic target space
- Uses contrastive or next-token prediction objectives
- Fast convergence since only a small fraction of parameters are updated

### Stage 2: Joint Fine-tuning

**Goal**: Jointly fine-tune the entire model (encoder + projector + LLM) to capture high-level semantic relationships.

```python
def stage2_joint_finetuning(fcn_encoder, projector, llm, dataloader, epochs=3, lr=2e-5):
    """Unfreeze all components for end-to-end fine-tuning."""
    all_params = list(fcn_encoder.parameters()) + \
                 list(projector.parameters()) + \
                 list(llm.parameters())
    
    optimizer = AdamW(all_params, lr=lr)
    
    for epoch in range(epochs):
        for batch in dataloader:
            # Full forward pass through all components
            region_feats, subnet_feats, global_feat = fcn_encoder(...)
            region_tokens, subnet_tokens, global_token = projector(...)
            llm_input = torch.cat([region_tokens, subnet_tokens, global_token, 
                                   batch.instruction_embeddings], dim=1)
            
            # Multi-task loss over all 19 attributes
            loss = compute_multi_task_loss(llm, llm_input, batch.targets)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

**Key characteristics**:
- Lower learning rate (2e-5) to preserve LLM knowledge
- Multi-task loss aggregates across all 19 attributes
- Gradient accumulation for memory efficiency
- LoRA/QLoRA adapters recommended for parameter-efficient tuning

## Zero-Shot Generalization

### Evaluation Protocol

FCN-LLM demonstrates strong zero-shot generalization on **unseen datasets** (sites not in training):

```python
def evaluate_zero_shot(model, unseen_dataset, attributes):
    """Evaluate on datasets from sites never seen during training."""
    results = {}
    model.eval()
    
    with torch.no_grad():
        for attr in attributes:
            predictions = []
            ground_truth = []
            
            for subject in unseen_dataset:
                fc_tokens = encode_and_project(subject.fc_matrix, subject.features, model)
                instruction = format_instruction(attr, fc_tokens)
                pred = model.generate(instruction)
                predictions.append(parse_prediction(pred, attr))
                ground_truth.append(subject.labels[attr])
            
            results[attr] = compute_metrics(predictions, ground_truth, attr)
    
    return results
```

### Generalization Strategies

| Strategy | Description | Impact |
|----------|-------------|--------|
| **Multi-site training** | Train on data from diverse acquisition sites | Reduces site-specific bias |
| **Harmonization layers** | Learn site-invariant representations | Improves cross-site transfer |
| **Diverse instruction pool** | 19 varied attributes prevent overfitting to single task | Broadens semantic understanding |
| **Graph-level encoding** | Whole-brain features generalize better than region-specific | Captures universal patterns |

## Graph-level Instruction Tuning

### Why Graph-level?

Unlike node-level or edge-level approaches, FCN-LLM operates at the **graph level** because:

1. **Clinical attributes** (age, diagnosis, cognitive scores) are **subject-level** properties, not node-level
2. **Whole-brain integration** is necessary — no single brain region determines complex traits
3. **Instruction tuning** requires a single representation per subject to map to text

### Training Data Format

```json
{
  "fc_matrix": [[0.0, 0.3, ...], [0.3, 0.0, ...], ...],
  "node_features": [[...], [...], ...],
  "subnetwork_assignments": [1, 2, 1, 3, ...],
  "instructions": [
    {
      "type": "predict",
      "attribute": "age",
      "instruction": "Based on the brain functional connectivity network, predict the age of this subject.",
      "target": "The subject is approximately 35 years old."
    },
    {
      "type": "describe",
      "attribute": "depression",
      "instruction": "Describe the brain connectivity patterns associated with depression severity.",
      "target": "This subject shows elevated connectivity between the default mode network..."
    }
  ],
  "labels": {
    "age": 35,
    "sex": "female",
    "depression_severity": 12.5,
    ...
  }
}
```

## Clinical Applications

### Potential Use Cases

| Application | How FCN-LLM Helps |
|-------------|-------------------|
| **Clinical decision support** | Generate natural language interpretations of patient FCNs |
| **Biomarker discovery** | LLM explanations identify key brain regions and networks |
| **Multi-site harmonization** | Zero-shot generalization enables deployment across hospitals |
| **Longitudinal monitoring** | Track changes in connectivity patterns over time with text reports |
| **Patient education** | Convert complex FCN data into understandable descriptions |
| **Research hypothesis generation** | LLM can suggest connectivity-behavior relationships to investigate |

### Example Clinical Workflow

```python
def clinical_fcn_report(patient_fc, model):
    """Generate a clinical interpretation report from patient FCN."""
    fc_tokens = encode_and_project(patient_fc, model)
    
    report_sections = []
    
    # Demographics prediction
    age_pred = model.predict(f"<FCN>{fc_tokens}</FCN> Predict this patient's age.")
    report_sections.append(f"Estimated age: {age_pred}")
    
    # Cognitive assessment
    cognition = model.predict(f"<FCN>{fc_tokens}</FCN> Assess cognitive function profile.")
    report_sections.append(f"Cognitive assessment: {cognition}")
    
    # Risk screening
    depression = model.predict(f"<FCN>{fc_tokens}</FCN> Assess depression risk.")
    report_sections.append(f"Depression screening: {depression}")
    
    # Network analysis
    network_desc = model.generate(f"<FCN>{fc_tokens}</FCN> Describe notable connectivity patterns.")
    report_sections.append(f"Connectivity analysis: {network_desc}")
    
    return "\n\n".join(report_sections)
```

## Comparison with Existing Approaches

### FCN-LLM vs. Supervised Models

| Aspect | Traditional Supervised | FCN-LLM |
|--------|----------------------|---------|
| **Task specificity** | One model per task | Single model, 19+ tasks |
| **Output format** | Fixed (scalar/vector) | Natural language |
| **Generalization** | Poor to unseen sites/datasets | Strong zero-shot |
| **Interpretability** | Black-box predictions | LLM-generated explanations |
| **Data efficiency** | Needs task-specific labels | Leverages instruction diversity |

### FCN-LLM vs. Brain Foundation Models

| Aspect | Brain Foundation Models | FCN-LLM |
|--------|----------------------|---------|
| **Modality alignment** | Graph-only, no text | Graph + text aligned |
| **Interface** | Task-specific heads | Natural language instructions |
| **Reasoning** | Pattern matching | LLM reasoning capabilities |
| **Flexibility** | Fixed output types | Open-ended generation |
| **Clinical integration** | Separate analysis pipeline | Directly interfaces with clinical text systems |

## Implementation Guidelines

### Recommended Tech Stack

```
PyTorch + PyG (Graph Neural Networks)
Transformers (LLM backbone: LLaMA, Qwen, or Mistral)
PeFT/LoRA (parameter-efficient fine-tuning)
fMRIPrep (preprocessing)
Nilearn (FCN construction)
```

### Data Preprocessing Pipeline

```python
def preprocess_fMRI_to_fcn(fmri_data, atlas="Schaefer_400", bandpass=(0.01, 0.1)):
    """Convert fMRI timeseries to functional connectivity matrix."""
    # 1. Parcellate using atlas
    timeseries = extract_timeseries(fmri_data, atlas)
    
    # 2. Bandpass filter
    timeseries = bandpass_filter(timeseries, bandpass)
    
    # 3. Compute functional connectivity (Pearson correlation)
    fc_matrix = np.corrcoef(timeseries.T)
    
    # 4. Fisher z-transform
    fc_matrix = np.arctanh(np.clip(fc_matrix, -0.99, 0.99))
    
    # 5. Construct node features (e.g., degree, clustering coefficient)
    node_features = compute_node_features(fc_matrix)
    
    return fc_matrix, node_features
```

### Training Configuration

```yaml
# FCN-LLM Training Configuration
model:
  llm_base: "meta-llama/Llama-3-8B-Instruct"  # or Qwen2.5-7B
  encoder: "GAT"  # Graph Attention Network
  n_regions: 400  # Schaefer atlas
  hidden_dim: 256
  projector_layers: 2

stage1_alignment:
  epochs: 5
  batch_size: 32
  learning_rate: 1e-4
  freeze_llm: true
  optimizer: AdamW
  
stage2_finetuning:
  epochs: 3
  batch_size: 8
  learning_rate: 2e-5
  lora_rank: 16
  lora_alpha: 32
  gradient_accumulation: 4
  optimizer: AdamW

data:
  atlases: ["Schaefer_400", "AAL_116"]
  preprocessing: "standardized"
  train_val_split: 0.8
  multi_site: true
  harmonization: "ComBat"
```

### Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| **Site effects dominate** | Apply ComBat harmonization before training |
| **FCN matrix sparsity** | Use thresholding or sparse graph methods |
| **LLM hallucination on medical data** | Constrain outputs with structured templates and fact-checking |
| **Memory overflow with full fine-tuning** | Use LoRA/QLoRA for LLM parameters |
| **Class imbalance in psychiatric attributes** | Use focal loss or weighted sampling |
| **Overfitting to instruction format** | Use instruction templates with varied phrasing |
| **Temporal leakage in longitudinal data** | Strict subject-level train/test splits |

## Integration with Related Skills

- **fcn-llm-brain-network-understanding**: Complementary overview of FCN-LLM conceptual framework
- **brain-foundation-model-inversion**: For inverting brain foundation model representations back to interpretable FCNs
- **multimodal-brain-connectivity-gnn**: For GNN-based FCN encoding alternatives and multimodal extensions

## Key Takeaways

1. **Alignment is essential**: The FCN-text modality gap must be explicitly addressed through projection and alignment
2. **Multi-scale matters**: Brain-region + subnetwork + whole-brain encoding captures more information than any single scale
3. **Instruction diversity enables generalization**: 19 varied attributes prevent task-specific overfitting
4. **Two-stage training is efficient**: Alignment first, then joint fine-tuning preserves LLM capabilities while adapting to FCNs
5. **Zero-shot is achievable**: Multi-site training + diverse instructions enables generalization to unseen datasets
6. **Clinical relevance**: Natural language output bridges the gap between complex FCN data and clinical practice
