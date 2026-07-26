---
name: neurobridge-koopman-brain-dynamics
description: "NeuroBRIDGE: Behavior-conditioned Koopman dynamics with Riemannian alignment for brain network analysis. Uses Koopman operator theory with Riemannian geometry for dynamic functional connectivity modeling to predict substance use initiation risk. Activation: Koopman brain dynamics, behavior-conditioned Koopman, Riemannian alignment, dynamic connectivity, SUI prediction, adolescent brain."
---

# NeuroBRIDGE: Behavior-Conditioned Koopman Dynamics with Riemannian Alignment

> NeuroBRIDGE framework uses Koopman operator theory combined with Riemannian manifold alignment to model dynamic functional connectivity in adolescent brain networks for predicting substance use initiation (SUI) risk.

## Metadata
- **Source**: arXiv:2603.29960v1
- **Authors**: Neuroimaging research team
- **Published**: 2026-03-31
- **Category**: Computational Neuroscience, Brain Network Analysis

## Core Methodology

### Key Innovation
Traditional brain network analysis treats connectivity as static, missing temporal dynamics crucial for understanding risk. NeuroBRIDGE introduces a behavior-conditioned Koopman operator framework that:
1. Learns linear embeddings of nonlinear brain dynamics in a high-dimensional observable space
2. Uses Riemannian manifold alignment to account for individual differences in brain geometry
3. Conditions predictions on behavioral covariates (cognitive performance, substance use history)

### Technical Framework

#### Koopman Operator for Brain Dynamics
The Koopman operator K is an infinite-dimensional linear operator that acts on observables of a dynamical system:

```
K g(x) = g(F(x))
```

Where F is the nonlinear flow map and g are observable functions. For brain networks:
- **State**: Dynamic functional connectivity (DFC) matrices over time
- **Observables**: Deep neural network embeddings of DFC patterns
- **Eigenfunctions**: Learned via Extended Dynamic Mode Decomposition (EDMD)

#### Riemannian Manifold Alignment
Addresses individual differences in brain network geometry:
- **Manifold**: Space of symmetric positive definite (SPD) connectivity matrices
- **Metric**: Affine-invariant Riemannian metric on SPD manifold
- **Alignment**: Parallel transport of tangent vectors across subjects

```python
# Riemannian distance on SPD manifold
def riemannian_distance(S1, S2):
    """Affine-invariant metric between connectivity matrices"""
    S1_sqrt = matrix_sqrt(S1)
    S1_inv_sqrt = matrix_inv_sqrt(S1)
    M = S1_inv_sqrt @ S2 @ S1_inv_sqrt
    return np.linalg.norm(logm(M), 'fro')
```

#### Behavior-Conditioned Prediction
Integrates behavioral covariates b into the Koopman framework:

```
K(b) g(x_t) = g(x_{t+1})
```

The operator becomes behavior-dependent, allowing personalized predictions based on:
- Cognitive task performance
- Substance use history
- Demographic factors

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch or JAX for deep learning
- PyRiemann for Riemannian geometry on SPD manifolds
- Scikit-learn for baseline comparisons

### Step-by-Step

1. **Preprocess fMRI Data**
   ```python
   from nilearn import connectome
   # Extract time series from ROIs
   # Compute sliding-window connectivity
   ```

2. **Riemannian Alignment**
   ```python
   from pyriemann.utils.mean import mean_riemann
   from pyriemann.tangentspace import TangentSpace
   
   # Compute reference point (Riemannian mean)
   C_ref = mean_riemann(connectivity_matrices)
   
   # Project to tangent space
   ts = TangentSpace(metric='riemann')
   tangent_features = ts.fit_transform(connectivity_matrices)
   ```

3. **Koopman Operator Learning**
   ```python
   import torch
   import torch.nn as nn
   
   class KoopmanOperator(nn.Module):
       def __init__(self, obs_dim, behavior_dim):
           super().__init__()
           self.obs_encoder = nn.Sequential(
               nn.Linear(obs_dim, 256),
               nn.ReLU(),
               nn.Linear(256, 128)
           )
           self.behavior_encoder = nn.Sequential(
               nn.Linear(behavior_dim, 64),
               nn.ReLU()
           )
           # Conditioned Koopman matrix
           self.koopman_generator = nn.Linear(128 + 64, 128 * 128)
       
       def forward(self, x, b):
           obs = self.obs_encoder(x)
           beh = self.behavior_encoder(b)
           combined = torch.cat([obs, beh], dim=-1)
           K = self.koopman_generator(combined).view(-1, 128, 128)
           return K @ obs
   ```

4. **Training with Behavior Conditioning**
   ```python
   def train_step(model, dfc_sequence, behavior, target):
       # DFC: dynamic functional connectivity over time
       # behavior: subject-specific covariates
       predictions = []
       state = dfc_sequence[0]
       
       for t in range(len(dfc_sequence) - 1):
           state = model(state, behavior)
           predictions.append(state)
       
       loss = prediction_loss(predictions, dfc_sequence[1:])
       loss.backward()
       optimizer.step()
   ```

### Code Example: Complete Pipeline
```python
class NeuroBRIDGE:
    """
    Behavior-conditioned Koopman dynamics for brain network analysis
    """
    def __init__(self, n_rois=264, behavior_dim=10, latent_dim=128):
        self.n_rois = n_rois
        self.behavior_dim = behavior_dim
        self.latent_dim = latent_dim
        
        # Observable encoder (connectivity -> latent)
        self.obs_encoder = self._build_encoder(
            input_dim=n_rois * (n_rois - 1) // 2,  # upper triangle
            output_dim=latent_dim
        )
        
        # Behavior encoder
        self.behavior_encoder = nn.Sequential(
            nn.Linear(behavior_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32)
        )
        
        # Conditioned Koopman operator
        self.koopman_net = nn.Sequential(
            nn.Linear(latent_dim + 32, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim * latent_dim)
        )
    
    def forward(self, connectivity_seq, behavior):
        """
        connectivity_seq: [batch, time, n_rois, n_rois]
        behavior: [batch, behavior_dim]
        """
        batch_size, seq_len = connectivity_seq.shape[:2]
        
        # Encode connectivity to observables
        obs = self._vectorize_connectivity(connectivity_seq)
        obs = self.obs_encoder(obs)  # [batch*time, latent_dim]
        obs = obs.view(batch_size, seq_len, self.latent_dim)
        
        # Encode behavior
        beh = self.behavior_encoder(behavior)  # [batch, 32]
        
        # Predict next states using conditioned Koopman
        predictions = []
        state = obs[:, 0, :]
        
        for t in range(seq_len - 1):
            # Concatenate state and behavior
            conditioned = torch.cat([state, beh], dim=-1)
            K = self.koopman_net(conditioned).view(-1, self.latent_dim, self.latent_dim)
            state = (K @ state.unsqueeze(-1)).squeeze(-1)
            predictions.append(state)
        
        return torch.stack(predictions, dim=1)
    
    def predict_risk(self, connectivity_seq, behavior, horizon=6):
        """Predict SUI risk at future time horizon (months)"""
        future_states = self.forward(connectivity_seq, behavior)
        # Use final predicted state for classification
        risk_score = self.risk_classifier(future_states[:, -1, :])
        return risk_score
```

## Applications
- **Substance Use Initiation Prediction**: Early identification of at-risk adolescents
- **Dynamic Connectivity Analysis**: Understanding temporal brain network changes
- **Personalized Intervention**: Behavior-specific recommendations based on brain dynamics
- **Longitudinal Studies**: Tracking developmental trajectories in brain networks

## Pitfalls
- **Computational Cost**: Koopman operator learning requires significant GPU resources
- **Temporal Resolution**: Sliding-window connectivity assumes quasi-stationarity
- **Interpretability**: Deep Koopman embeddings may lack biological interpretability
- **Data Requirements**: Needs longitudinal fMRI data with behavioral assessments

## Related Skills
- kuramoto-brain-network
- geometric-brain-dynamics-mapping
- brain-connectivity-analysis
- functional-connectome-fingerprint

## References
```bibtex
@article{neurobridge2026,
  title={NeuroBRIDGE: Behavior-Conditioned Koopman Dynamics with Riemannian Alignment for Adolescent Brain Networks},
  author={[Authors]},
  journal={arXiv preprint arXiv:2603.29960},
  year={2026}
}
```
