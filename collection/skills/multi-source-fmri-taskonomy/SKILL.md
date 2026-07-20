---
name: multi-source-fmri-taskonomy
description: "Multi-source fMRI cognitive taskonomy framework using transfer learning across 23 HCP task states. Extends single-source to many-to-one task relations with Boolean Integer Programming for budget-constrained task allocation. Activation: fMRI taskonomy, cognitive tasks, transfer learning, multi-source, HCP, BIP."
tags: [neuroscience, fmri, transfer-learning, cognitive-tasks, brain-networks, integer-programming]
activation: fMRI taskonomy, cognitive tasks, transfer learning, multi-source transfer, HCP task states, Boolean Integer Programming, brain network analysis, masked fMRI reconstruction
---

## Overview

This skill implements multi-source fMRI cognitive taskonomy for quantifying transfer relations among task states across the Human Connectome Project (HCP). Extends single-source (one-to-one) transfer to many-to-one task relations with budget-constrained optimization. Based on arXiv:2606.26279v1.

## Core Concepts

### fMRI Cognitive Taskonomy
- **Definition**: Quantifying how cognitive tasks relate through shared and specialized neural processes
- **Method**: Masked fMRI reconstruction as common self-supervised objective
- **Scope**: 23 HCP task states (motor, working memory, language, social, etc.)

### Single-Source vs Multi-Source Transfer
- **Single-source**: One-to-one transfer from source task to target
- **Multi-source**: Many-to-one transfer combining multiple source tasks
- **Key Finding**: Many-to-one relations not fully captured by pairwise taskonomy alone

### Boolean Integer Programming (BIP)
- **Purpose**: Optimize budget-constrained task allocation
- **Objective**: Maximize transfer performance across supervision budgets
- **Finding**: Working-memory states (0-back, 2-back) repeatedly allocated highest priority despite not being strongest individual sources

## Methodology

### 1. Data Preparation
```python
import numpy as np
from sklearn.model_selection import train_test_split

# Load HCP fMRI data for 23 task states
tasks = load_hcp_tasks(['motor', 'working_memory', 'language', 'social', ...])
# Each task: shape (n_subjects, n_timepoints, n_voxels)

# Apply masking for self-supervised reconstruction
masked_data = apply_spatiotemporal_mask(tasks, mask_ratio=0.15)
```

### 2. Training Transfer Models
```python
from sklearn.linear_model import Ridge

def train_transfer_models(tasks, n_tasks=23):
    """Train 1,127 task-specific and transfer models."""
    models = {}

    for target_idx in range(n_tasks):
        target_task = tasks[target_idx]

        # Task-specific model (direct supervision)
        models[(target_idx, target_idx)] = train_model(target_task)

        # Transfer models (single-source)
        for source_idx in range(n_tasks):
            if source_idx != target_idx:
                source_task = tasks[source_idx]
                models[(source_idx, target_idx)] = train_transfer(
                    source_task, target_task
                )

    return models

def train_transfer(source_data, target_data):
    """Train model on source, fine-tune on target."""
    model = Ridge(alpha=1.0)
    model.fit(source_data.X, source_data.y)
    # Fine-tune on limited target data
    model.partial_fit(target_data.X[:100], target_data.y[:100])
    return model
```

### 3. Multi-Source Transfer
```python
def multi_source_transfer(sources, target, models):
    """Combine multiple source tasks for target prediction."""
    predictions = []
    for source_idx in sources:
        pred = models[(source_idx, target)].predict(target.X_test)
        predictions.append(pred)

    # Ensemble: weighted average based on single-source performance
    weights = compute_transfer_weights(sources, target, models)
    ensemble_pred = np.average(predictions, axis=0, weights=weights)

    return ensemble_pred
```

### 4. Boolean Integer Programming
```python
from scipy.optimize import milp, LinearConstraint, Bounds

def optimize_task_allocation(transfer_matrix, budget):
    """
    transfer_matrix: (n_tasks, n_tasks) transfer performance matrix
    budget: number of tasks to allocate direct supervision
    """
    n_tasks = transfer_matrix.shape[0]

    # Decision variables: x_i = 1 if task i gets direct supervision
    # Objective: maximize total transfer performance
    c = -transfer_matrix.sum(axis=1)  # negative for minimization

    # Constraint: sum(x) <= budget
    constraints = LinearConstraint(
        np.ones((1, n_tasks)),
        lb=0,
        ub=budget
    )

    # Binary variables
    integrality = np.ones(n_tasks)
    bounds = Bounds(0, 1)

    result = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    selected_tasks = np.where(result.x > 0.5)[0]
    return selected_tasks
```

## Key Results

### Single-Source Transfer Patterns
- **Motor paradigm**: Strong within-paradigm transfer (motor→motor)
- **Cross-paradigm**: Limited transfer from motor to non-motor targets
- **Implication**: Shared sensorimotor execution system with effector-specific representations

### Multi-Source Transfer
- **Composition-dependent**: Performance depends on source set composition
- **Beyond pairwise**: Many-to-one relations exceed sum of pairwise transfers
- **Synergistic effects**: Some source combinations outperform individual sources

### BIP Optimization Results
- **Working memory priority**: 0-back and 2-back tasks repeatedly selected
- **Paradox**: Not the strongest individual sources, but optimal under budget constraints
- **Explanation**: Integration of perceptual, attentional, and executive processes

## Practical Usage

### When to Use
- Analyzing cognitive task relationships in fMRI data
- Optimizing fMRI study design under budget constraints
- Understanding shared vs specialized neural processes
- Building transfer learning models for cognitive tasks

### Workflow
1. **Collect fMRI data**: Multiple task states from HCP or similar dataset
2. **Preprocess**: Standard fMRI preprocessing (motion correction, normalization)
3. **Apply masking**: Spatiotemporal masking for self-supervised learning
4. **Train models**: Task-specific and transfer models
5. **Compute transfer matrix**: Quantify pairwise transfer performance
6. **Optimize allocation**: Use BIP to find optimal supervision budget allocation
7. **Validate**: Test on held-out tasks or new datasets

### Common Pitfalls
- **Ignoring multi-source effects**: Pairwise transfer underestimates many-to-one relations
- **Overfitting transfer models**: Use regularization (Ridge, Lasso)
- **Neglecting task heterogeneity**: Different tasks may require different preprocessing
- **Budget misallocation**: BIP optimization reveals non-obvious priorities

## Validation

### Transfer Performance Metrics
```python
def evaluate_transfer(models, tasks):
    """Evaluate single-source and multi-source transfer."""
    metrics = {}

    for target_idx in range(len(tasks)):
        # Single-source
        single_scores = []
        for source_idx in range(len(tasks)):
            if source_idx != target_idx:
                score = models[(source_idx, target_idx)].score(
                    tasks[target_idx].X_test,
                    tasks[target_idx].y_test
                )
                single_scores.append(score)
        metrics[f'task_{target_idx}_single'] = np.mean(single_scores)

        # Multi-source (all other tasks)
        sources = [i for i in range(len(tasks)) if i != target_idx]
        multi_pred = multi_source_transfer(sources, target_idx, models)
        multi_score = r2_score(tasks[target_idx].y_test, multi_pred)
        metrics[f'task_{target_idx}_multi'] = multi_score

    return metrics
```

### Statistical Validation
- **Bootstrap resampling**: Estimate confidence intervals on transfer scores
- **Permutation testing**: Test significance of multi-source vs single-source gains
- **Cross-validation**: Ensure robustness to train/test splits

## Extensions

### Beyond HCP
- Apply to other datasets (UK Biobank, ABCD, local collections)
- Cross-dataset transfer learning

### Temporal Dynamics
- Time-resolved taskonomy: how task relations change over time
- Dynamic functional connectivity integration

### Clinical Applications
- Transfer learning for patient populations with limited data
- Optimizing clinical fMRI protocols

## References

- Paper: arXiv:2606.26279v1 "Beyond Single-Source Cognitive Taskonomy: Multi-Source Task Relations through fMRI Transfer Learning"
- Key insight: Multi-source transfer reveals synergistic effects beyond pairwise relations
- Method: Boolean Integer Programming for budget-constrained task allocation
- Dataset: 23 HCP task states, 1,127 models trained

## Activation Triggers

Use this skill when:
- Analyzing cognitive task relationships in fMRI
- Optimizing fMRI study design or data collection
- Building transfer learning models for brain data
- Studying shared vs specialized neural processes
- Working with HCP or similar multi-task fMRI datasets
