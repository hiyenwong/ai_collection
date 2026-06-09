---
name: quantum-annealing-xai
description: "Quantum annealing-based feature selection for interpretable AI in Convolutional Neural Networks. Uses constrained optimization to select most important feature maps contributing to predictions, providing explainable AI with improved class disentanglement. Use when implementing XAI for CNNs, quantum annealing feature selection, or model interpretation via quantum computing."
---

# Quantum Annealing Feature Selection for Interpretable CNNs

Research methodology from arXiv:2604.25649 (April 2026) - Venturelli et al.

## Core Idea

Interpret CNN predictions by **selecting the most important feature maps** using quantum annealing. This approach improves class disentanglement - making model decision boundaries more distinct and reasoning more transparent compared to gradient-based methods like GradCAM/GradCAM++.

## Problem Formulation

### Feature Map Selection as Combinatorial Optimization

Given:
- A trained CNN with L convolutional layers
- Each layer l produces F_l feature maps: {f_1, f_2, ..., f_Fl}
- For a specific input x, identify subset S of feature maps that maximize prediction confidence

**Combinatorial Problem**: 
- Search space: 2^F (all subsets of feature maps)
- Objective: Maximize importance while minimizing redundancy
- Constraint: Selected features must be coherent (spatially correlated)

## Methodology

### Step 1: Feature Importance Scoring

```python
def compute_feature_importance(model, input_x, target_class):
    """
    Compute importance score for each feature map
    """
    importances = {}
    activations = forward_pass_with_hooks(model, input_x)
    
    for layer_name, feature_maps in activations.items():
        for idx, fm in enumerate(feature_maps):
            # Gradient-based importance
            score = compute_gradcam_score(fm, target_class)
            
            # Spatial coherence
            coherence = compute_spatial_coherence(fm)
            
            importances[f"{layer_name}_{idx}"] = {
                'score': score,
                'coherence': coherence,
                'spatial_extent': fm.shape
            }
    
    return importances
```

### Step 2: QUBO Formulation

Encode feature selection as Quadratic Unconstrained Binary Optimization (QUBO):

```
minimize: H(x) = Σ_i h_i x_i + Σ_{i<j} J_{ij} x_i x_j

where:
- x_i ∈ {0,1}: binary variable (1 if feature i is selected)
- h_i: linear term (negative importance score)
- J_{ij}: quadratic term (redundancy penalty)
```

**Linear Terms**:
```python
h_i = -α * importance_score[i] + β * computational_cost[i]
```

**Quadratic Terms**:
```python
J_{ij} = γ * redundancy(i, j) - δ * spatial_correlation(i, j)
```

### Step 3: Quantum Annealing Solution

```python
def solve_feature_selection_qubo(h, J, num_reads=1000):
    """
    Solve QUBO using quantum annealing (D-Wave API)
    """
    from dwave.system import DWaveSampler, EmbeddingComposite
    
    # Build BQM
    bqm = dimod.BinaryQuadraticModel.from_ising(h, J)
    
    # Quantum annealing
    sampler = EmbeddingComposite(DWaveSampler())
    response = sampler.sample(bqm, num_reads=num_reads)
    
    # Extract best solution
    best_solution = response.first.sample
    selected_features = [i for i, v in best_solution.items() if v == 1]
    
    return selected_features, response
```

### Step 4: Explanation Generation

```python
def generate_explanation(selected_features, feature_importances):
    """
    Create interpretable explanation from selected features
    """
    explanation = {
        'selected_count': len(selected_features),
        'top_features': sorted(
            [(f, feature_importances[f]['score']) 
             for f in selected_features],
            key=lambda x: x[1], reverse=True
        )[:5],
        'spatial_regions': extract_spatial_regions(selected_features),
        'layer_distribution': analyze_layer_distribution(selected_features)
    }
    return explanation
```

## Key Advantages

### 1. Class Disentanglement

Quantum annealing finds globally optimal feature subsets:
- **GradCAM**: Local gradient-based (may miss global optimum)
- **This Method**: Global optimization via quantum search
- **Result**: More distinct class decision boundaries

### 2. Feature Coherence

Enforces spatial and semantic coherence:
- Adjacent pixels in same feature map correlated
- Cross-layer feature dependencies modeled
- Natural image structure preserved

### 3. Interpretability Metrics

Quantitative evaluation:
- **Localization accuracy**: IoU with ground truth
- **Class sensitivity**: Change in prediction with feature removal
- **Faithfulness**: Correlation with model behavior

## Implementation

### Requirements

```python
# Classical preprocessing
numpy, torch, opencv-python

# Quantum annealing
dwave-ocean-sdk

# Visualization
matplotlib, seaborn
```

### Complete Pipeline

```python
class QuantumXAIExplainer:
    def __init__(self, cnn_model, quantum_sampler=None):
        self.model = cnn_model
        self.sampler = quantum_sampler or self._init_sampler()
    
    def explain(self, input_image, target_class, 
                num_features=10, alpha=1.0, beta=0.1):
        """
        Generate explanation for model prediction
        """
        # 1. Extract activations
        activations = self._get_activations(input_image)
        
        # 2. Compute importance scores
        importances = self._score_features(activations, target_class)
        
        # 3. Build QUBO
        h, J = self._build_qubo(importances, num_features, alpha, beta)
        
        # 4. Solve with quantum annealing
        selected = self._solve_qubo(h, J)
        
        # 5. Generate explanation
        explanation = self._create_explanation(
            selected, importances, input_image.shape
        )
        
        return explanation
    
    def visualize(self, explanation, input_image):
        """
        Create visualization of selected features
        """
        overlay = self._create_heatmap(explanation['spatial_regions'])
        return self._blend_with_image(input_image, overlay)
```

## Comparison with SOTA

| Method | Optimization | Coherence | Speed | Interpretability |
|--------|-------------|-----------|-------|------------------|
| GradCAM | Local (gradient) | Implicit | Fast | Medium |
| GradCAM++ | Local (gradient) | Implicit | Fast | Medium |
| **This Method** | **Global (quantum)** | **Explicit** | **Annealing time** | **High** |
| SHAP | Global (sampling) | Implicit | Slow | High |
| LIME | Local (perturbation) | Implicit | Medium | Medium |

## Error Analysis

### Energy Gap Analysis

The quantum annealing behavior analyzed via:
1. **Minimum energy gap**: During computation
2. **Success probability**: P(correct solution)

```python
def analyze_annealing_performance(response):
    """
    Analyze quantum annealing quality metrics
    """
    energies = [sample.energy for sample in response.record]
    
    metrics = {
        'min_energy': min(energies),
        'ground_state_degeneracy': energies.count(min(energies)),
        'success_probability': energies.count(min(energies)) / len(energies),
        'energy_gap': min(set(energies)) - min(energies) if len(set(energies)) > 1 else 0
    }
    
    return metrics
```

## Applications

- **Medical Imaging**: Explainable diagnosis from CNN predictions
- **Autonomous Vehicles**: Interpretable object detection
- **Financial Systems**: Explainable fraud detection
- **Safety-Critical Systems**: Model verification and validation

## Tools Used

- `exec`: Python for CNN processing and QUBO solving
- `read`: Load trained CNN models
- `write`: Save explanations and visualizations

## References

- **Primary Paper**: arXiv:2604.25649 - "Towards interpretable AI with quantum annealing feature selection"
- **D-Wave**: dwavesys.com/docs
- **GradCAM**: Selvaraju et al. (2017) ICCV

## Related Skills

- quantum-tensor-train-surrogates
- quantum-ml-research
- quantum-annealing
