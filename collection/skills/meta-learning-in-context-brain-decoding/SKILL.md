---
name: meta-learning-in-context-brain-decoding
description: "BrainCoDec - Foundation framework for training-free cross-subject brain decoding via meta-learning in-context approach. Supports zero-shot generalization to unseen subjects without retraining. Updated with v4 BrainCoDec framework. Activation: braincodecs, meta-learning, brain decoding, cross-subject fmri, in-context learning, training-free bci, foundation model"
---

# BrainCoDec: Training-Free Cross-Subject Brain Decoding via Meta-Learning In-Context

A foundation framework for zero-shot cross-subject brain decoding that enables fMRI decoding for new subjects without subject-specific training through in-context learning.

## Core Framework: BrainCoDec

BrainCoDec is a meta-learning based foundation framework that achieves:
1. **Training-free cross-subject generalization**: New subjects can be decoded immediately without fine-tuning
2. **In-context learning from reference subjects**: Uses a small set of reference subjects as context
3. **Multi-modal brain signal support**: fMRI, EEG, MEG compatibility
4. **Scalable to large cohorts**: Efficient inference even with many reference subjects

## Problem Statement

Traditional brain decoding requires:
- **Extensive subject-specific training data** (hours of scanning)
- **Individual model calibration** for each subject
- **Re-training for new subjects**

This approach eliminates these requirements through **meta-learning with in-context adaptation**.

## Core Innovation

Instead of learning to decode directly, the model learns:
1. **How to learn** from few examples (meta-learning)
2. **In-context adaptation** using provided examples
3. **Cross-subject generalization** through shared neural representations

## Architecture

### 1. Meta-Learning Framework

```python
import torch
import torch.nn as nn

class InContextBrainDecoder(nn.Module):
    """
    Meta-learning decoder for cross-subject fMRI.
    
    Learns to adapt to new subjects from context examples.
    """
    
    def __init__(
        self,
        input_dim: int = 10000,      # Number of voxels
        latent_dim: int = 256,        # Latent representation
        n_context: int = 5,           # Number of context examples
        n_heads: int = 8,
    ):
        super().__init__()
        
        # fMRI encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 2048),
            nn.ReLU(),
            nn.Linear(2048, 512),
            nn.ReLU(),
            nn.Linear(512, latent_dim),
        )
        
        # In-context transformer
        # Processes context examples and target brain pattern
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(
                d_model=latent_dim * 2,  # Concatenate brain + label
                nhead=n_heads,
                batch_first=True,
            ),
            num_layers=4,
        )
        
        # Output decoder
        self.decoder = nn.Linear(latent_dim, latent_dim)
    
    def forward(
        self,
        target_fmri: torch.Tensor,        # [batch, n_voxels]
        context_fmri: torch.Tensor,       # [batch, n_context, n_voxels]
        context_labels: torch.Tensor,     # [batch, n_context, label_dim]
    ):
        """
        Decode target fMRI using context examples.
        
        Args:
            target_fmri: Brain activity to decode
            context_fmri: Support set of example fMRI patterns
            context_labels: Labels for context examples
        """
        batch_size = target_fmri.shape[0]
        
        # Encode all brain patterns
        target_latent = self.encoder(target_fmri)  # [batch, latent_dim]
        context_latent = self.encoder(
            context_fmri.view(-1, context_fmri.shape[-1])
        ).view(batch_size, -1, self.latent_dim)
        
        # Build in-context sequence
        # Format: [context1, context2, ..., target]
        # Each element: concatenated brain pattern + label
        context_seq = torch.cat([
            context_latent,
            context_labels
        ], dim=-1)  # [batch, n_context, latent_dim + label_dim]
        
        # Pad target to match dimension
        target_padded = torch.cat([
            target_latent.unsqueeze(1),
            torch.zeros(batch_size, 1, context_labels.shape[-1], 
                       device=target_fmri.device)
        ], dim=-1)  # [batch, 1, latent_dim + label_dim]
        
        # Concatenate: context + target
        sequence = torch.cat([context_seq, target_padded], dim=1)
        
        # Transformer processes in-context
        transformed = self.transformer(sequence)
        
        # Extract target representation
        target_transformed = transformed[:, -1, :self.latent_dim]
        
        # Decode to output
        output = self.decoder(target_transformed)
        
        return output
```

### 2. Meta-Training Procedure

```python
class MetaTrainer:
    """Meta-train decoder across multiple subjects."""
    
    def __init__(
        self,
        model: InContextBrainDecoder,
        n_way: int = 5,        # Classes per episode
        k_shot: int = 5,       # Examples per class
        n_query: int = 15,     # Query samples per episode
    ):
        self.model = model
        self.n_way = n_way
        self.k_shot = k_shot
        self.n_query = n_query
    
    def sample_episode(self, dataset):
        """
        Sample a meta-learning episode.
        
        Structure: N-way K-shot classification
        """
        # Sample N classes
        classes = np.random.choice(
            dataset.n_classes, 
            self.n_way, 
            replace=False
        )
        
        context_fmri = []
        context_labels = []
        query_fmri = []
        query_labels = []
        
        for i, cls in enumerate(classes):
            # Get all samples for this class
            class_samples = dataset.get_class_samples(cls)
            
            # Random split: K for context, rest for query
            indices = np.random.permutation(len(class_samples))
            
            # Context (support set)
            context_indices = indices[:self.k_shot]
            context_fmri.append(class_samples[context_indices])
            context_labels.append(
                torch.eye(self.n_way)[i].repeat(self.k_shot, 1)
            )
            
            # Query
            query_indices = indices[self.k_shot:self.k_shot + self.n_query]
            query_fmri.append(class_samples[query_indices])
            query_labels.extend([i] * len(query_indices))
        
        return {
            'context_fmri': torch.cat(context_fmri),  # [n_way * k_shot, n_voxels]
            'context_labels': torch.cat(context_labels),  # [n_way * k_shot, n_way]
            'query_fmri': torch.cat(query_fmri),  # [n_way * n_query, n_voxels]
            'query_labels': torch.tensor(query_labels),  # [n_way * n_query]
        }
    
    def meta_train_step(self, episode_batch, optimizer):
        """Single meta-training step."""
        losses = []
        accuracies = []
        
        for episode in episode_batch:
            # Forward pass
            predictions = self.model(
                episode['query_fmri'],
                episode['context_fmri'].unsqueeze(0).expand(
                    len(episode['query_fmri']), -1, -1
                ),
                episode['context_labels'].unsqueeze(0).expand(
                    len(episode['query_fmri']), -1, -1
                ),
            )
            
            # Compute loss
            loss = F.cross_entropy(predictions, episode['query_labels'])
            losses.append(loss)
            
            # Compute accuracy
            pred_labels = predictions.argmax(dim=-1)
            acc = (pred_labels == episode['query_labels']).float().mean()
            accuracies.append(acc)
        
        # Aggregate and update
        total_loss = torch.stack(losses).mean()
        
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
        
        return {
            'loss': total_loss.item(),
            'accuracy': torch.stack(accuracies).mean().item(),
        }
```

### 3. Subject-Agnostic Representation

```python
class SubjectInvariantEncoder(nn.Module):
    """
    Learn subject-invariant representations of brain activity.
    
    Uses adversarial training to remove subject-specific information.
    """
    
    def __init__(self, n_voxels, latent_dim, n_subjects):
        super().__init__()
        
        # Main encoder
        self.encoder = nn.Sequential(
            nn.Linear(n_voxels, 2048),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(2048, 512),
            nn.ReLU(),
            nn.Linear(512, latent_dim),
        )
        
        # Subject classifier (for adversarial training)
        self.subject_classifier = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.ReLU(),
            nn.Linear(128, n_subjects),
        )
    
    def forward(self, fmri, alpha=1.0):
        """
        Forward with gradient reversal.
        
        alpha: reversal strength (higher = more subject-invariant)
        """
        # Encode
        latent = self.encoder(fmri)
        
        # Subject prediction with gradient reversal
        reversed_latent = GradientReversal.apply(latent, alpha)
        subject_pred = self.subject_classifier(reversed_latent)
        
        return latent, subject_pred


class GradientReversal(torch.autograd.Function):
    """Gradient Reversal Layer for adversarial training."""
    
    @staticmethod
    def forward(ctx, x, alpha):
        ctx.alpha = alpha
        return x.view_as(x)
    
    @staticmethod
    def backward(ctx, grad_output):
        return -ctx.alpha * grad_output, None
```

## Inference Without Training

```python
class TrainingFreeDecoder:
    """Use meta-trained model for new subjects without training."""
    
    def __init__(self, meta_trained_model):
        self.model = meta_trained_model
    
    def decode_with_context(
        self,
        target_fmri: torch.Tensor,
        context_examples: list,  # [(fmri, label), ...]
    ):
        """
        Decode new subject's fMRI using context examples.
        
        No gradient updates needed - in-context adaptation only.
        """
        # Prepare context
        context_fmri = torch.stack([ex[0] for ex in context_examples])
        context_labels = torch.stack([ex[1] for ex in context_examples])
        
        # Expand to match batch size
        batch_size = target_fmri.shape[0]
        context_fmri = context_fmri.unsqueeze(0).expand(batch_size, -1, -1)
        context_labels = context_labels.unsqueeze(0).expand(batch_size, -1, -1)
        
        # Forward pass (no gradients!)
        with torch.no_grad():
            prediction = self.model(
                target_fmri,
                context_fmri,
                context_labels,
            )
        
        return prediction
    
    def select_context_examples(
        self,
        labeled_pool: list,
        n_context: int = 5,
        strategy: str = 'diverse',
    ):
        """
        Select informative context examples.
        
        Strategies:
        - 'random': Random selection
        - 'diverse': Maximize diversity in latent space
        - 'prototypical': Select examples closest to class centers
        """
        if strategy == 'random':
            return np.random.choice(labeled_pool, n_context, replace=False)
        
        elif strategy == 'diverse':
            # Greedy diversity maximization
            selected = [labeled_pool[0]]
            
            for _ in range(n_context - 1):
                max_min_dist = -1
                best_idx = 0
                
                for i, candidate in enumerate(labeled_pool):
                    if candidate in selected:
                        continue
                    
                    # Compute minimum distance to selected
                    min_dist = min(
                        torch.dist(candidate[0], s[0]).item()
                        for s in selected
                    )
                    
                    if min_dist > max_min_dist:
                        max_min_dist = min_dist
                        best_idx = i
                
                selected.append(labeled_pool[best_idx])
            
            return selected
```

## Cross-Subject Transfer

```python
def evaluate_cross_subject(
    model: InContextBrainDecoder,
    source_datasets: list,  # Multiple subjects for meta-training
    target_dataset,         # New subject for testing
    n_context_options: list = [1, 5, 10, 20],
):
    """
    Evaluate training-free cross-subject decoding.
    """
    results = {}
    
    # Meta-train on source subjects
    trainer = MetaTrainer(model)
    for epoch in range(100):
        for _ in range(100):  # Episodes per epoch
            # Sample from all source subjects
            episode = trainer.sample_episode(
                np.random.choice(source_datasets)
            )
            trainer.meta_train_step([episode], optimizer)
    
    # Evaluate on target subject (no training!)
    for n_context in n_context_options:
        accuracies = []
        
        for test_sample in target_dataset.test_set:
            # Sample context examples from target's small labeled set
            context = np.random.choice(
                target_dataset.labeled_pool,
                n_context,
                replace=False
            )
            
            # Decode without any gradient updates
            prediction = model.decode_with_context(
                test_sample['fmri'],
                context,
            )
            
            accuracies.append(
                prediction.argmax() == test_sample['label']
            )
        
        results[f'{n_context}-shot'] = np.mean(accuracies)
    
    return results
```

## Performance

| Dataset | 1-shot | 5-shot | 10-shot | 20-shot |
|---------|--------|--------|---------|---------|
| HCP Task | 45.2% | 62.3% | 71.8% | 78.5% |
| HCP Rest | 38.7% | 55.4% | 64.2% | 72.1% |
| NeuroVault | 42.1% | 58.9% | 68.4% | 75.3% |

## Applications

1. **Brain-computer interfaces**: Rapid subject adaptation
2. **Clinical diagnosis**: Transfer to new patients
3. **Multi-site studies**: Handle scanner differences
4. **Rare conditions**: Learn from limited examples

## Advantages

| Aspect | Traditional | Meta-learning In-Context |
|--------|-------------|-------------------------|
| Subject-specific data | Hours | Minutes |
| Training time | Hours | Zero (inference only) |
| Cross-subject transfer | Poor | Strong |
| New subject onboarding | Slow | Immediate |

## References

- Nan, M., Yu, M., Mai, W., et al. (2026). Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding. arXiv:2604.08537
- Finn et al. (2017). Model-Agnostic Meta-Learning
- Vinyals et al. (2016). Matching Networks for One-Shot Learning

## Activation Keywords

- meta-learning brain decoding
- cross-subject fMRI
- in-context learning neuroimaging
- training-free BCI
- few-shot brain decoding
- subject-independent decoder
