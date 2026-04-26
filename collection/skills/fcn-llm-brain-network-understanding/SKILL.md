---
name: fcn-llm-brain-network-understanding
description: "FCN-LLM framework for enabling Large Language Models to understand brain Functional Connectivity Networks through graph-level multi-task instruction tuning. Use for brain network analysis with LLMs, zero-shot FCN classification, neuroimaging interpretation, and cross-dataset generalization. Keywords: FCN-LLM, brain functional connectivity, LLM neuroimaging, graph instruction tuning."
---

# FCN-LLM: Brain Network Understanding with LLMs

Framework for empowering Large Language Models to understand brain Functional Connectivity Networks (FCNs) from resting-state fMRI through graph-level multi-task instruction tuning.

## Overview

Traditional brain FCN analysis uses specialized deep learning models limited to specific tasks. FCN-LLM bridges FCNs with text modality, enabling LLMs to directly interpret brain networks through natural language.

**Key Innovation:** Multi-scale FCN encoder projecting brain networks into LLM semantic space.

## Architecture

### 1. Multi-Scale FCN Encoder

Captures brain connectivity at three levels:

**Brain-Region Level:**
- Individual ROI (Region of Interest) features
- Local connectivity patterns
- Node-level embeddings

**Functional Subnetwork Level:**
- Module-level connectivity (e.g., default mode network)
- Subnetwork interactions
- Meso-scale organization

**Whole-Brain Level:**
- Global connectivity patterns
- Network topology features
- System-level properties

```python
class MultiScaleFCNEncoder(nn.Module):
    """Multi-scale FCN encoder for brain network analysis."""
    
    def __init__(self, n_rois=116, hidden_dim=512, embed_dim=768):
        super().__init__()
        
        # ROI-level encoder (GNN)
        self.roi_encoder = GCNConv(n_rois, hidden_dim)
        
        # Subnetwork-level (clustering-based)
        self.subnet_encoder = SubnetworkAggregator(hidden_dim)
        
        # Whole-brain level (readout)
        self.global_pool = GlobalAttentionPool(hidden_dim)
        
        # Projection to LLM space
        self.projection = nn.Sequential(
            nn.Linear(hidden_dim * 3, embed_dim),
            nn.LayerNorm(embed_dim),
            nn.GELU(),
            nn.Linear(embed_dim, embed_dim)
        )
    
    def forward(self, adj_matrix, roi_features):
        """
        Encode FCN at multiple scales.
        
        Args:
            adj_matrix: [batch, n_rois, n_rois] connectivity
            roi_features: [batch, n_rois, feature_dim]
        
        Returns:
            embedding: [batch, embed_dim] LLM-compatible embedding
        """
        # ROI level
        roi_emb = self.roi_encoder(roi_features, adj_matrix)
        
        # Subnetwork level
        subnet_emb = self.subnet_encoder(roi_emb, adj_matrix)
        
        # Whole-brain level
        global_emb = self.global_pool(roi_emb)
        
        # Concatenate and project
        multi_scale = torch.cat([roi_emb.mean(1), subnet_emb, global_emb], dim=-1)
        embedding = self.projection(multi_scale)
        
        return embedding
```

### 2. Instruction Task Design

**Multi-Paradigm Tasks (19 subject-specific attributes):**

**Demographics:**
- Age group classification
- Gender prediction
- Education level

**Phenotypes:**
- Cognitive performance
- Behavioral traits
- Clinical assessments

**Psychiatric Conditions:**
- Disease diagnosis (ADHD, ASD, etc.)
- Severity prediction
- Subtype classification

**Instruction Templates:**
```python
INSTRUCTION_TEMPLATES = {
    "age": "Analyze this brain functional connectivity network and predict the subject's age group.",
    "gender": "Examine the connectivity patterns in this brain network and determine the subject's gender.",
    "diagnosis": "Based on the functional connectivity patterns, does this subject show signs of {condition}?",
    "cognition": "Predict the cognitive performance level based on this brain network's connectivity structure."
}

def create_instruction_task(fcn_data, task_type, label):
    """Create instruction-tuning sample."""
    instruction = INSTRUCTION_TEMPLATES[task_type]
    
    # Encode FCN
    fcn_embedding = fcn_encoder(fcn_data)
    
    # Format for LLM
    return {
        "instruction": instruction,
        "input": "",  # FCN embedded in special tokens
        "fcn_embedding": fcn_embedding,
        "output": str(label)
    }
```

### 3. Multi-Stage Training Strategy

**Stage 1: FCN-LLM Alignment**
- Freeze LLM parameters
- Train only FCN encoder
- Goal: Project FCNs into LLM semantic space

**Stage 2: Joint Fine-tuning**
- Unfreeze LLM LoRA adapters
- End-to-end training
- Goal: Capture high-level semantic information

```python
def train_fcn_llm_stage1(fcn_encoder, llm, dataloader):
    """Stage 1: Align FCN encoder with LLM."""
    optimizer = Adam(fcn_encoder.parameters(), lr=1e-4)
    
    for batch in dataloader:
        fcn_emb = fcn_encoder(batch['adj'], batch['features'])
        
        # Project through LLM embedding layer
        llm_inputs = prepare_llm_inputs(fcn_emb, batch['instruction'])
        outputs = llm(**llm_inputs, labels=batch['labels'])
        
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

def train_fcn_llm_stage2(fcn_encoder, llm, dataloader, lora_config):
    """Stage 2: Joint fine-tuning with LoRA."""
    # Apply LoRA to LLM
    llm = get_peft_model(llm, lora_config)
    
    optimizer = Adam([
        {'params': fcn_encoder.parameters()},
        {'params': llm.parameters(), 'lr': 1e-5}
    ], lr=1e-4)
    
    for batch in dataloader:
        fcn_emb = fcn_encoder(batch['adj'], batch['features'])
        llm_inputs = prepare_llm_inputs(fcn_emb, batch['instruction'])
        
        outputs = llm(**llm_inputs, labels=batch['labels'])
        
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
```

## Application Workflow

### 1. Data Preparation

```python
class FCNDataset:
    """Prepare FCN data for LLM training."""
    
    def __init__(self, connectivity_matrices, metadata):
        self.connectivity = connectivity_matrices  # [N, n_rois, n_rois]
        self.metadata = metadata  # Demographics, phenotypes, etc.
    
    def __getitem__(self, idx):
        adj = self.connectivity[idx]
        
        # Extract features (e.g., degree, centrality)
        features = extract_graph_features(adj)
        
        # Create tasks
        tasks = {
            'age_group': self.metadata['age_group'][idx],
            'gender': self.metadata['gender'][idx],
            'diagnosis': self.metadata['diagnosis'][idx],
        }
        
        return {'adj': adj, 'features': features, 'tasks': tasks}
```

### 2. Zero-Shot Inference

```python
def zero_shot_predict(fcn_llm, fcn_data, query):
    """
    Perform zero-shot prediction on new FCN data.
    
    Args:
        fcn_llm: Trained FCN-LLM model
        fcn_data: New brain connectivity network
        query: Natural language query about the network
    
    Returns:
        prediction: LLM's response
    """
    fcn_llm.eval()
    
    with torch.no_grad():
        # Encode FCN
        fcn_emb = fcn_llm.encoder(fcn_data['adj'], fcn_data['features'])
        
        # Create prompt
        prompt = f"{query}\n<FCN_EMBEDDING>{fcn_emb}</FCN_EMBEDDING>"
        
        # Generate response
        inputs = fcn_llm.tokenizer(prompt, return_tensors='pt')
        outputs = fcn_llm.generate(**inputs, max_new_tokens=100)
        
        prediction = fcn_llm.tokenizer.decode(outputs[0])
    
    return prediction
```

### 3. Cross-Dataset Generalization

```python
def evaluate_zero_shot_generalization(fcn_llm, unseen_datasets):
    """
    Evaluate on unseen datasets from different sites.
    
    Key finding: FCN-LLM achieves strong zero-shot generalization
    outperforming conventional supervised and foundation models.
    """
    results = {}
    
    for dataset_name, data in unseen_datasets.items():
        predictions = []
        ground_truth = []
        
        for sample in data:
            pred = zero_shot_predict(fcn_llm, sample['fcn'], sample['query'])
            predictions.append(pred)
            ground_truth.append(sample['label'])
        
        results[dataset_name] = compute_metrics(predictions, ground_truth)
    
    return results
```

## Key Results

**Performance:**
- Strong zero-shot generalization on unseen datasets
- Outperforms conventional supervised models
- Beats brain foundation models on cross-site evaluation

**Advantages:**
- Flexible natural language interface
- Interpretable predictions
- Multi-task capability
- Cross-dataset robustness

## Activation Keywords

- FCN-LLM
- brain functional connectivity
- LLM neuroimaging
- graph instruction tuning
- zero-shot brain network
- multi-scale brain encoding

## Tools Used

- PyTorch Geometric for GNN components
- Transformers library for LLM integration
- PEFT for LoRA fine-tuning
- Nilearn for fMRI preprocessing

## References

Hu, X., Wang, W., & Xiao, L. (2026). FCN-LLM: Empower LLM for Brain Functional Connectivity Network Understanding via Graph-level Multi-task Instruction Tuning. arXiv:2603.01135.

## Related Skills

- brain-connectivity-analysis
- fmri-preprocessing
- graph-neural-networks
- llm-fine-tuning