---
name: semantic-navigation-embedding-trajectories---chara
description: Skill for AI agent capabilities
---

# semantic-navigation-embedding-trajectories - Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space

## Description

This framework represents human concept production as navigation through embedding space. Using transformer text embedding models, it constructs semantic trajectories and extracts geometric/dynamical metrics (distance, entropy, velocity, acceleration) to quantify semantic representation search as movement in a geometric space.

**Source:** arXiv:2602.05971v1
**Utility:** 0.91
**Accepted:** ICLR 2026

## Activation Keywords

- semantic navigation
- embedding trajectories
- concept production
- semantic representation
- cumulative embeddings
- semantic geometry
- verbal fluency analysis

## Core Concepts

### 1. Framework Overview

```
Concept Production → Cumulative Embeddings → Trajectory Analysis → Geometric/Dynamical Metrics
```

**Key insight:** Human semantic search is navigation through a structured knowledge space.

### 2. Trajectory Metrics

| Metric | Description | Interpretation |
|--------|-------------|----------------|
| **Distance to next** | Distance between consecutive concepts | Semantic jump size |
| **Distance to centroid** | Distance from trajectory center | Semantic exploration radius |
| **Entropy** | Distribution of embedding positions | Semantic diversity |
| **Velocity** | Speed of semantic movement | Concept production rate |
| **Acceleration** | Change in velocity | Semantic search dynamics |

### 3. Applications

- **Clinical research:** Distinguishing neurodegenerative groups
- **Cross-linguistic analysis:** Property listing in Italian/German
- **Verbal fluency:** Swear word generation analysis
- **AI cognition:** Assessing artificial semantic representation

## Step-by-Step Instructions

### 1. Construct Cumulative Embeddings

```python
import numpy as np
from sentence_transformers import SentenceTransformer

class SemanticTrajectory:
    """Semantic navigation trajectory analyzer."""
    
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.encoder = SentenceTransformer(model_name)
    
    def build_cumulative_trajectory(self, concepts):
        """
        Build cumulative embedding trajectory.
        
        Args:
            concepts: List of concepts produced by participant
        
        Returns:
            trajectory: Array of cumulative embeddings
        """
        trajectory = []
        cumulative_context = ""
        
        for concept in concepts:
            # Add to cumulative context
            cumulative_context += f" {concept}"
            
            # Get embedding
            embedding = self.encoder.encode(cumulative_context.strip())
            trajectory.append(embedding)
        
        return np.array(trajectory)
    
    def build_non_cumulative_trajectory(self, concepts):
        """
        Build non-cumulative embedding trajectory (for short sequences).
        """
        embeddings = [self.encoder.encode(c) for c in concepts]
        return np.array(embeddings)
```

### 2. Compute Geometric Metrics

```python
def compute_distance_to_next(trajectory):
    """Distance between consecutive embeddings."""
    distances = []
    for i in range(len(trajectory) - 1):
        dist = np.linalg.norm(trajectory[i+1] - trajectory[i])
        distances.append(dist)
    return np.array(distances)

def compute_distance_to_centroid(trajectory):
    """Distance from trajectory centroid."""
    centroid = np.mean(trajectory, axis=0)
    distances = [np.linalg.norm(e - centroid) for e in trajectory]
    return np.array(distances)

def compute_entropy(trajectory, bins=20):
    """Entropy of embedding distribution."""
    from scipy.stats import entropy
    
    # Project to 1D (first principal component)
    from sklearn.decomposition import PCA
    pca = PCA(n_components=1)
    projected = pca.fit_transform(trajectory).flatten()
    
    # Compute histogram
    hist, _ = np.histogram(projected, bins=bins, density=True)
    
    return entropy(hist + 1e-10)  # Avoid zero bins
```

### 3. Compute Dynamical Metrics

```python
def compute_velocity(trajectory, time_steps=None):
    """Velocity of semantic movement."""
    if time_steps is None:
        time_steps = np.arange(len(trajectory))
    
    # Discrete velocity: embedding difference per time step
    velocity = []
    for i in range(len(trajectory) - 1):
        vel = (trajectory[i+1] - trajectory[i]) / (time_steps[i+1] - time_steps[i])
        velocity.append(vel)
    
    return np.array(velocity)

def compute_acceleration(trajectory, time_steps=None):
    """Acceleration of semantic movement."""
    if time_steps is None:
        time_steps = np.arange(len(trajectory))
    
    velocity = compute_velocity(trajectory, time_steps)
    
    # Discrete acceleration
    acceleration = []
    for i in range(len(velocity) - 1):
        acc = (velocity[i+1] - velocity[i]) / (time_steps[i+2] - time_steps[i+1])
        acceleration.append(acc)
    
    return np.array(acceleration)

def compute_speed(velocity):
    """Speed (magnitude of velocity)."""
    return np.linalg.norm(velocity, axis=1)
```

### 4. Analyze Participant Trajectories

```python
def analyze_semantic_navigation(concepts, model_name='all-MiniLM-L6-v2'):
    """
    Full analysis of semantic navigation.
    
    Args:
        concepts: List of concepts produced by participant
        model_name: Embedding model
    
    Returns:
        metrics: Dictionary of all metrics
    """
    analyzer = SemanticTrajectory(model_name)
    
    # Choose trajectory type based on length
    if len(concepts) >= 10:
        trajectory = analyzer.build_cumulative_trajectory(concepts)
        trajectory_type = "cumulative"
    else:
        trajectory = analyzer.build_non_cumulative_trajectory(concepts)
        trajectory_type = "non-cumulative"
    
    # Compute all metrics
    metrics = {
        'trajectory_type': trajectory_type,
        'length': len(concepts),
        'distance_to_next': compute_distance_to_next(trajectory),
        'distance_to_centroid': compute_distance_to_centroid(trajectory),
        'entropy': compute_entropy(trajectory),
        'velocity': compute_velocity(trajectory),
        'acceleration': compute_acceleration(trajectory),
        'mean_speed': np.mean(compute_speed(compute_velocity(trajectory)))
    }
    
    return metrics
```

### 5. Compare Groups

```python
def compare_groups(group1_concepts, group2_concepts, model_name='all-MiniLM-L6-v2'):
    """
    Compare semantic navigation between two groups.
    
    Args:
        group1_concepts: List of concept lists for group 1
        group2_concepts: List of concept lists for group 2
    
    Returns:
        comparison: Statistical comparison of metrics
    """
    from scipy.stats import mannwhitneyu
    
    # Analyze each participant
    group1_metrics = [analyze_semantic_navigation(c, model_name) for c in group1_concepts]
    group2_metrics = [analyze_semantic_navigation(c, model_name) for c in group2_concepts]
    
    # Compare key metrics
    comparison = {}
    
    for metric_name in ['entropy', 'mean_speed']:
        g1_values = [m[metric_name] for m in group1_metrics]
        g2_values = [m[metric_name] for m in group2_metrics]
        
        stat, pvalue = mannwhitneyu(g1_values, g2_values)
        comparison[metric_name] = {
            'group1_mean': np.mean(g1_values),
            'group2_mean': np.mean(g2_values),
            'statistic': stat,
            'p_value': pvalue
        }
    
    return comparison
```

## Tools Used

- `sentence_transformers` - Embedding models
- `numpy` - Numerical computations
- `scipy.stats` - Statistical tests
- `sklearn.decomposition.PCA` - Dimensionality reduction
- `exec` - Run analysis scripts
- `read` - Load concept data

## Example Use Cases

### 1. Verbal Fluency Analysis

```python
# Analyze patient's verbal fluency
patient_concepts = ["apple", "banana", "cherry", "date", "elderberry"]
metrics = analyze_semantic_navigation(patient_concepts)

print(f"Entropy: {metrics['entropy']:.2f}")
print(f"Mean speed: {metrics['mean_speed']:.4f}")
print(f"Trajectory type: {metrics['trajectory_type']}")
```

### 2. Clinical Group Comparison

```python
# Compare neurodegenerative vs control
neurodegenerative = [["cat", "dog", "bird"], ["car", "bus", "train"]]
control = [["cat", "dog", "bird", "fish", "horse"], ["car", "bus", "train", "plane", "boat"]]

comparison = compare_groups(neurodegenerative, control)

for metric, results in comparison.items():
    print(f"{metric}:")
    print(f"  Neuro: {results['group1_mean']:.3f}")
    print(f"  Control: {results['group2_mean']:.3f}")
    print(f"  p-value: {results['p_value']:.4f}")
```

### 3. Cross-Linguistic Analysis

```python
# Compare semantic navigation in different languages
italian_concepts = ["cane", "gatto", "uccello"]
german_concepts = ["hund", "katze", "vogel"]

italian_metrics = analyze_semantic_navigation(italian_concepts)
german_metrics = analyze_semantic_navigation(german_concepts)

print(f"Italian entropy: {italian_metrics['entropy']:.2f}")
print(f"German entropy: {german_metrics['entropy']:.2f}")
```

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Construct Cumulative Embeddings

## Examples

### Example 1: Basic Application

**User:** I need to apply semantic-navigation-embedding-trajectories - Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space to my analysis.

**Agent:** I'll help you apply semantic-navigation-embedding-trajectories. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for semantic-navigation-embedding-trajectories?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `functional-connectome-fingerprint` - Functional connectivity analysis
- `brain-network-joint-embedding` - Brain network embedding
- `task-aware-brain-connectivity` - Task-based brain connectivity

## References

- Carvalho, R.D.M.C. (2026). "Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space" arXiv:2602.05971v1 [cs.CL]
- Accepted to ICLR 2026

---

**Created:** 2026-03-29 15:05
**Author:** Aerial (from arXiv:2602.05971v1)