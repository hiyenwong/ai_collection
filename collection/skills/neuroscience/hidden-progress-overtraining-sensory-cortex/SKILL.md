---
name: hidden-progress-overtraining-sensory-cortex
description: "Hidden progress during overtraining in sensory cortex networks — discovering that overtrained neural networks continue learning useful representations even after apparent performance plateau, with implications for neuroscience and deep learning theory. Activation: overtraining, sensory cortex, hidden progress, learning plateau, groove, deep learning theory, representational change, network training dynamics."
---

# Hidden Progress During Overtraining in Sensory Cortex Networks

> Reveals that neural networks trained on sensory tasks continue developing useful internal representations even after behavioral performance plateaus — a "hidden progress" phenomenon with implications for understanding cortical overtraining and learning plateaus.

## Metadata
- **Source**: arXiv:2411.03541
- **Authors**: Tanishq Kumar, Grace W. Lindsay
- **Published**: 2024-11-05
- **Categories**: cs.LG, q-bio.NC

## Core Methodology

### Key Innovation
Demonstrates that overtrained neural networks on sensory classification tasks show "hidden progress" — internal representations continue evolving meaningfully even when accuracy has saturated. This parallels sensory cortex overtraining phenomena and challenges the assumption that performance plateau means learning has stopped.

### Technical Framework
1. **Overtraining Setup**: Train CNNs and RNNs on visual/auditory classification tasks well beyond convergence
2. **Behavioral Plateau**: Observe that accuracy saturates (e.g., 99%+ accuracy reached early)
3. **Hidden Progress Metrics**: Track representations during overtraining phase:
   - **Linear probes**: Fit linear classifiers to intermediate representations → probe accuracy continues improving
   - **Representational similarity analysis (RSA)**: Representations continue drifting toward brain-like patterns
   - **Adversarial robustness**: Overtrained networks become more adversarially robust
   - **Feature selectivity**: Neurons become sharper in their feature tuning
4. **Groove Phase**: Term for the extended learning period where hidden progress occurs
5. **Brain Alignment**: Overtrained networks often better match neural data from sensory cortex

### Implementation Guide

#### Prerequisites
- Deep learning training dynamics
- Representational analysis (RSA, linear probes, CCA)
- Sensory neuroscience (visual/auditory cortex)
- Adversarial robustness evaluation

#### Step-by-Step
1. **Train network** on sensory task (e.g., image classification) for 5-10x normal epochs
2. **Track behavioral metrics**: Accuracy, loss (will plateau early)
3. **Track representational metrics** at each epoch:
   - Linear probe accuracy on penultimate layer features
   - RSA correlation with brain recordings (if available)
   - Adversarial accuracy (PGD attack)
4. **Identify groove phase**: Epochs where behavior is stable but representations change
5. **Quantify hidden progress**: Δ(linear probe), Δ(adversarial robustness), Δ(RSA)
6. **Compare**: Early-stopped vs. overtrained representations on transfer tasks

### Code Example
```python
import torch
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy.stats import spearmanr

def track_hidden_progress(model, train_loader, test_loader, 
                          brain_rdm=None, n_epochs=200):
    """Track behavioral and representational progress during overtraining."""
    records = []
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    for epoch in range(n_epochs):
        # Standard training
        model.train()
        for x, y in train_loader:
            loss = torch.nn.functional.cross_entropy(model(x), y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        # Behavioral metrics
        acc = evaluate_accuracy(model, test_loader)
        
        # Hidden progress metrics
        features, labels = extract_features(model, test_loader)
        
        # Linear probe: can a linear classifier do better?
        probe_acc = linear_probe_accuracy(features, labels)
        
        # Adversarial robustness
        adv_acc = adversarial_accuracy(model, test_loader, eps=0.03)
        
        # Representational similarity (if brain data available)
        rsa_corr = 0.0
        if brain_rdm is not None:
            model_rdm = compute_rdm(features)
            rsa_corr = spearmanr(model_rdm.flatten(), 
                                  brain_rdm.flatten())[0]
        
        records.append({
            'epoch': epoch,
            'accuracy': acc,
            'loss': loss.item(),
            'probe_accuracy': probe_acc,
            'adversarial_accuracy': adv_acc,
            'rsa_correlation': rsa_corr
        })
        
        # Detect groove phase
        if epoch > 50 and acc > 0.99:
            print(f"Epoch {epoch}: Groove phase - acc={acc:.4f}, "
                  f"probe={probe_acc:.4f}, adv={adv_acc:.4f}")
    
    return records

def linear_probe_accuracy(features, labels):
    """Fit linear probe and return accuracy."""
    clf = LogisticRegression(max_iter=1000)
    clf.fit(features, labels)
    return clf.score(features, labels)

def compute_rdm(features):
    """Compute representational dissimilarity matrix."""
    # Pairwise correlation distance
    corr = np.corrcoef(features)
    return 1 - corr
```

## Applications
- **Deep Learning Theory**: Understand what happens during extended training beyond convergence
- **Neuroscience of Learning**: Model cortical overtraining and perceptual learning plateaus
- **Brain-Model Alignment**: Overtrained models may better match brain data
- **Transfer Learning**: Hidden progress representations may transfer better
- **Training Best Practices**: Rethink early stopping criteria

## Pitfalls
- Overtraining is computationally expensive (5-10x normal epochs)
- Not all tasks show hidden progress — depends on task complexity and architecture
- Overfitting risk: overtrained models may overfit to training distribution
- Brain alignment improvements may not generalize across all brain regions

## Related Skills
- computational-neuroscience-in-llm-era
- neural-code-dynamics-analysis
- untrained-cnns-match-backpropagation-at-v1
- representation-use-usability-framework
- feedforward-dynamics-stimulus-encoding
