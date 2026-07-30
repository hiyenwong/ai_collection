---
name: neuroscience-domain-relevance-filtering
description: "Domain relevance filtering methodology for neuroscience paper selection in automated research workflows. Provides criteria for determining when arXiv papers are relevant to neuroscience, brain networks, neural dynamics, spiking neural networks, and computational neuroscience domains."
license: Complete terms in LICENSE.txt
---

# Neuroscience Domain Relevance Filtering

## Overview

This skill provides a systematic methodology for filtering arXiv papers to determine relevance to neuroscience research domains in automated workflows.

## Filtering Criteria

### Primary Categories (Highly Relevant)
- **q-bio.NC** (Neurons and Cognition) - Always relevant
- **cs.NE** (Neural and Evolutionary Computing) - Relevant if content relates to SNNs, brain networks, or neural computation

### Cross-listed Categories (Conditionally Relevant)
- **cs.LG** (Machine Learning) - Relevant if focused on brain-inspired ML, neural coding, or cognitive modeling
- **physics.bio-ph** (Biological Physics) - Relevant if addressing neural dynamics or brain biophysics
- **stat.AP** (Applications) - Relevant if applying statistical methods to neural data

### Exclude Categories (Generally Not Relevant)
- **cond-mat.stat-mech** (Statistical Mechanics) - Unless explicitly addressing neural systems
- **physics.flu-dyn** (Fluid Dynamics) - Not relevant to neuroscience
- **math.OC** (Optimization) - General optimization without neural context
- **eess.SY** (Systems and Control) - Unless specifically applied to neural systems

## Content-Based Filtering

### Read Abstracts and Apply These Rules:
1. **Include papers that mention**: neuroscience, brain network, neural dynamics, spiking neural network, computational neuroscience, neural coding, brain-computer interface, EEG, fMRI, MEG, neural oscillations, synaptic plasticity, neural computation
2. **Exclude papers focused on**: statistical mechanics, soft matter physics, Brownian motion, general optimization algorithms, molecular dynamics without neural context, pure mathematics without application

### Examples of Correct Filtering:
- **Included**: "State-Dependent Observation Noise Reintroduces Epistemic Value in Linear-Gaussian Active Inference" (arXiv:2607.20306) - addresses neural inference and active inference frameworks
- **Excluded**: "Optimal Finite-Time Control of Nonreciprocal Brownian Dimers" (arXiv:2607.20420) - focuses on statistical mechanics and Brownian motion, not neural systems

## Implementation in Automated Workflows

### Step-by-Step Process:
1. **Extract paper metadata** (title, abstract, categories, authors)
2. **Apply category filter** using the criteria above
3. **If category is ambiguous, apply content filter** by analyzing abstract keywords
4. **Only proceed with skill creation** for papers that pass both filters
5. **Log excluded papers** with reason for audit trail

### Code Pattern:
```python
def is_neuroscience_relevant(paper):
    # Check primary categories
    if 'q-bio.NC' in paper.categories:
        return True
    
    # Check cross-listed categories with content validation
    if 'cs.NE' in paper.categories:
        neuro_keywords = ['spiking', 'brain', 'neural network', 'neuron', 'synaptic']
        if any(kw in paper.abstract.lower() for kw in neuro_keywords):
            return True
    
    # Check abstract for neuroscience keywords regardless of category
    neuro_abstract_keywords = [
        'neuroscience', 'brain network', 'neural dynamics', 
        'spiking neural', 'computational neuroscience', 'neural coding',
        'brain-computer', 'EEG', 'fMRI', 'MEG', 'neural oscillation'
    ]
    if any(kw in paper.abstract.lower() for kw in neuro_abstract_keywords):
        return True
    
    return False
```

## Activation Keywords
- neuroscience domain filtering
- arxiv paper relevance
- automated research filtering
- brain network paper selection
- neural dynamics paper classification