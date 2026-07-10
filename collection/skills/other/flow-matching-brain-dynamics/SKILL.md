---
name: flow-matching-brain-dynamics
description: "Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics — compositional conditional generation of neural time series using continuous normalizing flows, enabling zero-shot generalization to novel experimental conditions"
tags: [flow-matching, neural-dynamics, brain-dynamics, generative-models, in-context-learning, out-of-distribution, continuous-normalizing-flows, neural-time-series]
related_skills: [dysco-multiview-latent-dynamics-extraction, autoregressive-flow-matching-neural-dynamics]
activation: ["flow matching brain", "in-context priors", "neural time series generation", "conditional generation neural", "zero-shot brain dynamics", "continuous normalizing flows", "compositional conditioning", "out-of-distribution neural"]
---

# Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics

**arXiv**: 2606.11833v1

**Authors**: Sam Gijsen, Michał Łukomski, Marc-André Schulz, et al.

**Publication**: 18 days ago

## Core Contribution

First framework for **compositional conditional generation** of neural time series using flow matching, enabling **zero-shot generalization** to novel experimental conditions by combining categorical and continuous conditioning modalities.

## Methodology

### Flow Matching for Neural Time Series

**Flow matching** learns continuous normalizing flows (CNFs) that transform simple noise distributions into complex neural dynamics:

1. **Continuous Normalizing Flows**: Learn vector fields that map base distribution (Gaussian) to target distribution (neural time series)
2. **Conditional Generation**: Condition on experimental variables (task, stimulus, subject) for controlled generation
3. **Compositional Conditioning**: Combine multiple conditioning sources (categorical + continuous) for flexible generation

### In-Context Priors for Zero-Shot Generalization

Key innovation: **In-context learning** enables generation for unseen conditions:

- **Context Encoder**: Encodes few-shot examples of target condition
- **Prior Network**: Learns distribution over conditions from context
- **Zero-Shot Generation**: Generate samples for completely novel conditions using only context examples

### Architecture

```
Input: Noise z ~ N(0,I) + Context examples {x_i, c_i}
  |
Context Encoder: f({x_i, c_i}) -> context embedding e
  |
Prior Network: g(e) -> prior distribution p(c_new|e)
  |
Conditional Flow: h(z, c_new, e) -> generated neural time series
  |
Output: Synthetic brain dynamics for novel condition c_new
```

## Key Innovations

### 1. Compositional Conditioning
- **Categorical conditions**: Task type, stimulus category, brain region
- **Continuous conditions**: Behavioral variables, reaction time, confidence
- **Composition**: Combine conditions multiplicatively for complex scenarios

### 2. Zero-Shot Generalization
- **No fine-tuning required**: Generate for unseen subjects/tasks using only context
- **Few-shot context**: 5-10 examples sufficient for good generalization
- **Distributional shift**: Handles out-of-distribution conditions gracefully

### 3. Continuous-Time Dynamics
- **Neural ODEs**: Model continuous-time neural dynamics
- **Irregular sampling**: Handle variable inter-sample intervals
- **Temporal smoothness**: Generate smooth trajectories respecting biological constraints

## Applications

### 1. Data Augmentation
- Generate synthetic training data for rare conditions
- Augment underrepresented subjects/tasks
- Balance datasets for classification

### 2. Hypothesis Testing
- Simulate "what-if" scenarios
- Test predictions about unobserved conditions
- Generate counterfactual neural dynamics

### 3. Transfer Learning
- Pre-train on large dataset
- Zero-shot adapt to new experimental setup
- Reduce data collection burden

### 4. Clinical Applications
- Generate pathological dynamics for rare conditions
- Simulate treatment effects
- Personalize models with few patient examples

## Implementation Pattern

### Flow Matching Training

```python
import torch
from torchdiffeq import odeint

class ConditionalFlowMatching:
    def __init__(self, input_dim, context_dim):
        self.vector_field = VectorFieldNetwork(input_dim, context_dim)
    
    def forward(self, t, z, context):
        # ODE: dz/dt = v(z, t, context)
        return self.vector_field(z, t, context)
    
    def generate(self, context, num_samples=100):
        # Generate samples via ODE integration
        z0 = torch.randn(num_samples, input_dim)
        trajectory = odeint(
            lambda t, z: self.forward(t, z, context),
            z0,
            t=torch.linspace(0, 1, 100)
        )
        return trajectory[-1]  # Final samples
```

### In-Context Prior

```python
class InContextPrior:
    def __init__(self, embedding_dim, context_dim):
        self.context_encoder = TransformerEncoder(embedding_dim)
        self.prior_network = PriorMLP(embedding_dim, context_dim)
    
    def forward(self, context_examples):
        # context_examples: list of (x_i, c_i) pairs
        embeddings = [self.context_encoder(x_i) for x_i in context_examples]
        context_embedding = torch.mean(torch.stack(embeddings), dim=0)
        c_new = self.prior_network(context_embedding)
        return c_new
```

## Experimental Results

### Datasets
- **EEG motor imagery**: 9 subjects, 4 task conditions
- **fMRI visual stimulation**: 12 subjects, 6 stimulus categories
- **MEG auditory**: 8 subjects, continuous attention modulation

### Results
- **Zero-shot FID**: 15.2 vs. 23.7 for conditional GAN baseline
- **Few-shot adaptation**: 5 examples gives 92% of fully supervised performance
- **Compositional generation**: Successfully combine task + subject + behavior

## Advantages Over Alternatives

| Method | Zero-Shot | Compositional | Continuous-Time | Sample Quality |
|--------|-----------|---------------|-----------------|----------------|
| GAN | No | No | No | Medium |
| VAE | No | Partial | No | Low |
| Diffusion | Partial | No | Yes | High |
| **Flow Matching** | **Yes** | **Yes** | **Yes** | **High** |

## Pitfalls

- **ODE integration cost**: Slow for long sequences (100+ steps); use adaptive solvers
- **Context quality**: Poor context examples lead to poor generation
- **Distribution coverage**: Context must span relevant condition space
- **Memory**: Store full trajectory for training; use checkpointing for long sequences

## Related Skills

- [[autoregressive-flow-matching-neural-dynamics]] - AFM framework for neural dynamics
- [[dysco-multiview-latent-dynamics-extraction]] - Latent dynamics extraction
- [[flow-matching-in-context-priors-brain-dynamics]] - Related flow matching work

## References

1. Gijsen, S., Łukomski, M., Schulz, M.-A., et al. (2026). Flow Matching with In-Context Priors for Out-of-Distribution Brain Dynamics. arXiv:2606.11833v1
2. Lipman, Y., et al. (2023). Flow Matching for Generative Modeling. ICLR 2023.