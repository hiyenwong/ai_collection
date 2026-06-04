---
name: sae-optimality-structures
description: Theory explaining how optimality conditions structure SAE (Sparse Autoencoder) dictionaries - hierarchical splitting, absorption, residuals, and dense antipodal features
version: 1.0
created: 2026-06-02
updated: 2026-06-02
authors:
  - William Dorrell
paper: arXiv:2606.02385
arxiv_url: https://arxiv.org/abs/2606.02385
doi: 10.48550/arXiv.2606.02385
categories:
  - neuroscience
  - machine-learning
  - interpretability
  - sparse-autoencoders
tags:
  - sae-optimality
  - sparse-autoencoders
  - interpretability
  - dictionary-learning
  - hierarchical-splitting
  - feature-absorption
activation:
  - sae theory
  - sparse autoencoder
  - feature splitting
  - dictionary learning
  - optimality analysis
  - interpretable features
related_skills:
  - neural-encoding-evaluation-ground-truth
  - representation-usefulness-philosophy-neuroscience
  - feature-visualization-brain-encoder
---

# SAE Optimality Structures

## Overview

**SAE Optimality Structures** provides a theoretical foundation for understanding what Sparse Autoencoders (SAEs) extract from neural representations. By analyzing local optimality conditions without assuming specific data-generating models, this theory explains observed SAE behaviors: hierarchical splitting, feature absorption, residual structure, and dense antipodal features.

**Key Contribution**: SAEs have empirical success in parsing neural representations into interpretable concepts, but lack theoretical grounding for what constitutes a "concept". This work derives constraints that any optimal SAE dictionary must satisfy, explaining phenomena through L1 regularization and nonnegativity interactions with data distributions.

**Use When**:
- Understanding SAE feature extraction mechanics
- Analyzing hierarchical splitting in learned dictionaries
- Debugging feature absorption phenomena
- Designing next-generation interpretable autoencoders
- Validating SAE-derived interpretations

## Core Concepts

### 1. Local Optimality Analysis Framework

**Definition**: Extends Gribonval & Schnass (2010) local optimality conditions to nonnegative joint optimization problem that vanilla SAEs approximate.

**Key Insight**: Instead of assuming sparse independent feature data models (which poorly approximate LLM representations), directly analyze what properties any optimal dictionary must satisfy.

**Mathematical Setup**:
```
Objective: minimize ||x - Dz||² + λ||z||₁
Subject to: z ≥ 0 (nonnegativity)
            D ≥ 0 (dictionary nonnegativity)

Where:
  x = input representation
  D = dictionary matrix (features)
  z = sparse code (activations)
  λ = L1 regularization strength
```

### 2. Optimality Constraints

**Constraint 1: Feature Distribution Relationship**
Optimal features must satisfy:
```
D_i ⟂ (X - DZ) Z_i^T ≥ λ|Z_i|  (for all features i)

Where:
  D_i = ith dictionary feature
  X = data matrix
  Z_i = ith feature's activation vector
  λ = regularization parameter
```

**Interpretation**: Features must be "just sparse enough" - activations balance reconstruction error and L1 penalty.

**Constraint 2: Nonnegativity Structure**
With nonnegativity, optimal solutions have:
```
D_ij = 0 iff feature i never activates for datapoint j
Z_ji > 0 iff feature i reconstructs j with positive contribution
```

**Implication**: Nonnegativity creates asymmetric feature structure, enabling hierarchical organization.

### 3. Observed Phenomena Explained

#### A. Hierarchical Splitting

**Phenomenon**: Features split into sub-features as dictionary size increases.

**Explanation from Optimality**:
```
As |D| increases:
1. Previously optimal single feature D_parent splits into D_child1, D_child2
2. Split condition: ||x - D_parent||² > ||x - D_child1||² + ||x - D_child2||² - λ(||z_child||₁ - ||z_parent||₁)
3. Split occurs when reconstruction gain exceeds sparsity penalty increase
```

**Visual Example**:
```
Parent feature (broad):    Child features (specialized):
D_parent = [0.3, 0.3]     D_child1 = [0.4, 0.1]  (specialized to dim1)
                          D_child2 = [0.1, 0.4]  (specialized to dim2)

Split when data has sub-clusters requiring specialized reconstruction
```

#### B. Feature Absorption

**Phenomenon**: Small features "absorbed" into larger features, disappearing from dictionary.

**Explanation**:
```
Absorption occurs when:
1. Feature D_small has low activation rate |Z_small|/n < threshold
2. Its reconstruction contribution is covered by D_large
3. Removing D_small improves objective: λ|Z_small| > ||X - DZ||² contribution

Absorption condition:
||D_small * Z_small||² < λ||Z_small||₁
```

**Interpretation**: L1 penalty "kills" rarely-used features, consolidating them into frequently-activated ones.

#### C. Residual Structure

**Phenomenon**: Reconstruction residuals have non-random structure, not pure noise.

**Explanation**:
```
Residual R = X - DZ satisfies:
1. R ⟂ D (orthogonal to dictionary)
2. ||R||² > λ for non-absorbed features
3. R has interpretable structure: components not captured by current features

Residual analysis reveals:
- Missing feature directions
- Feature interactions not modeled
- Hierarchical organization gaps
```

**Implication**: Residuals guide where new features should be added.

#### D. Dense Antipodal Features

**Phenomenon**: Some features appear dense (high activation) yet interpretable.

**Explanation**:
```
Antipodal pairs: D_a ≈ -D_b (but nonnegativity constraint forces both positive)

For data x = αD_a + βD_b + noise:
Optimal encoding: z_a = α, z_b = β (both dense)

Why interpretable?
1. D_a and D_b represent opposite directions in semantic space
2. High activation = strong presence of that semantic direction
3. Dense ≠ uninterpretable if direction is meaningful
```

**Example in LLM representations**:
```
D_positive_sentiment: activates for happy, joy, good (dense)
D_negative_sentiment: activates for sad, anger, bad (dense)
Both interpretable despite high activation frequency
```

## Implementation Methodology

### Phase 1: Optimality Analysis

#### Step 1: Compute Local Optimality Conditions
```python
def check_local_optimality(D, Z, X, lambda_reg):
    """
    Verify if current (D, Z) satisfies local optimality conditions
    
    Returns:
        - is_optimal: bool
        - violation_details: dict of constraint violations
    """
    # Constraint 1: Feature distribution
    reconstruction_error = X - D @ Z
    feature_constraints = {}
    
    for i in range(D.shape[1]):
        # Check: D_i ⟂ (X - DZ) Z_i^T ≥ λ|Z_i|
        gradient_Di = reconstruction_error @ Z[i]
        penalty_term = lambda_reg * np.abs(Z[i]).sum()
        
        feature_constraints[i] = {
            'gradient_norm': np.linalg.norm(gradient_Di),
            'penalty': penalty_term,
            'satisfied': np.linalg.norm(gradient_Di) >= penalty_term
        }
    
    # Constraint 2: Nonnegativity
    nonneg_D = (D >= 0).all()
    nonneg_Z = (Z >= 0).all()
    
    is_optimal = all(c['satisfied'] for c in feature_constraints.values()) and nonneg_D and nonneg_Z
    
    return {
        'is_optimal': is_optimal,
        'feature_constraints': feature_constraints,
        'nonnegativity_satisfied': {'D': nonneg_D, 'Z': nonneg_Z}
    }
```

#### Step 2: Detect Hierarchical Splitting
```python
def detect_feature_splitting(D_large, D_small, Z_large, Z_small, X, lambda_reg):
    """
    Analyze if features in D_small are splits of D_large features
    
    Split detection criteria:
    1. Child features reconstruct better than parent
    2. Sparsity penalty increase is compensated
    3. Child features specialize on sub-clusters
    """
    splits_detected = []
    
    for parent_idx in range(D_large.shape[1]):
        D_parent = D_large[:, parent_idx]
        
        # Find potential children (similar direction, more specialized)
        potential_children = []
        for child_idx in range(D_small.shape[1]):
            D_child = D_small[:, child_idx]
            
            # Similarity measure
            similarity = cosine_similarity(D_parent, D_child)
            if similarity > 0.7:  # High similarity threshold
                potential_children.append(child_idx)
        
        if len(potential_children) >= 2:
            # Check split condition
            children_features = D_small[:, potential_children]
            children_codes = Z_small[potential_children]
            
            # Reconstruction comparison
            parent_reconstruction = D_parent @ Z_large[parent_idx]
            children_reconstruction = children_features @ children_codes
            
            parent_error = np.linalg.norm(X - parent_reconstruction)
            children_error = np.linalg.norm(X - children_reconstruction)
            
            # Sparsity penalty comparison
            parent_penalty = lambda_reg * np.abs(Z_large[parent_idx]).sum()
            children_penalty = lambda_reg * np.abs(children_codes).sum()
            
            # Split beneficial?
            split_beneficial = (parent_error - children_error) > (children_penalty - parent_penalty)
            
            if split_beneficial:
                splits_detected.append({
                    'parent_idx': parent_idx,
                    'child_indices': potential_children,
                    'reconstruction_gain': parent_error - children_error,
                    'sparsity_cost': children_penalty - parent_penalty,
                    'net_benefit': (parent_error - children_error) - (children_penalty - parent_penalty)
                })
    
    return splits_detected
```

#### Step 3: Analyze Residual Structure
```python
def analyze_residual_structure(D, Z, X):
    """
    Analyze reconstruction residual structure to find missing features
    
    Key analyses:
    1. Residual magnitude per dimension
    2. Residual clustering (potential new feature directions)
    3. Residual-feature orthogonality verification
    """
    residual = X - D @ Z
    
    # 1. Magnitude per dimension
    residual_magnitude = np.linalg.norm(residual, axis=0)
    high_residual_dims = np.where(residual_magnitude > residual_magnitude.mean())[0]
    
    # 2. Clustering analysis (PCA on residuals)
    from sklearn.decomposition import PCA
    pca = PCA(n_components=10)
    residual_components = pca.fit_transform(residual.T)
    
    # Check if residual components are orthogonal to D
    residual_directions = pca.components_
    orthogonal_to_D = []
    for direction in residual_directions:
        orthogonality = np.abs(D.T @ direction).max()
        if orthogonality < 0.1:  # Nearly orthogonal
            orthogonal_to_D.append(direction)
    
    # 3. Potential new features
    potential_new_features = {
        'residual_magnitude': residual_magnitude,
        'high_residual_dims': high_residual_dims,
        'residual_components': residual_components,
        'orthogonal_directions': orthogonal_to_D,
        'suggested_features': len(orthogonal_to_D)
    }
    
    return potential_new_features
```

### Phase 2: Large-Dictionary Convex Problem

#### Step 1: Construct Convex Relaxation
```python
def construct_large_dictionary_problem(X, n_atoms, lambda_reg):
    """
    Construct convex problem for large dictionary limit
    
    Key insight: As |D| → n_datapoints, problem becomes convex
    (atom-per-datapoint limit)
    """
    n_samples, n_features = X.shape
    
    # Convex relaxation: each datapoint gets dedicated atom
    # Objective becomes: minimize ||X - DZ||² + λ||Z||₁
    # with Z diagonal (one atom per point)
    
    # This simplifies to per-point optimization:
    convex_solution = {}
    
    for i in range(n_samples):
        x_i = X[i]
        
        # Optimal atom for x_i: D_i = x_i (reconstruction perfect)
        # Optimal code: z_i = 1 if ||x_i||² > λ, else 0
        
        if np.linalg.norm(x_i) ** 2 > lambda_reg:
            convex_solution[i] = {
                'atom': x_i,
                'code': 1.0,
                'active': True
            }
        else:
            convex_solution[i] = {
                'atom': np.zeros(n_features),
                'code': 0.0,
                'active': False
            }
    
    # Active atoms count
    n_active = sum(s['active'] for s in convex_solution.values())
    
    return {
        'solution': convex_solution,
        'n_active_atoms': n_active,
        'sparsity': n_active / n_samples,
        'convex_limit': True
    }
```

#### Step 2: Explore Wide Atom Limit
```python
def explore_wide_atom_limit(X, lambda_reg_values):
    """
    Explore behavior as n_atoms → ∞ (wide dictionary limit)
    
    Phenomena to observe:
    1. Sparsity saturation
    2. Feature specialization
    3. Hierarchical depth
    """
    results = {}
    
    for lambda_reg in lambda_reg_values:
        # Large dictionary convex solution
        convex_sol = construct_large_dictionary_problem(X, X.shape[0], lambda_reg)
        
        # Compute properties
        results[lambda_reg] = {
            'active_ratio': convex_sol['sparsity'],
            'avg_feature_norm': np.mean([
                np.linalg.norm(s['atom']) for s in convex_sol['solution'].values() 
                if s['active']
            ]),
            'feature_specialization': compute_specialization_metric(convex_sol),
            'hierarchical_depth': estimate_hierarchy_depth(convex_sol)
        }
    
    return results

def compute_specialization_metric(convex_solution):
    """
    Measure how specialized features are (vs. general/broad)
    
    Specialization = low overlap between features
    """
    active_atoms = [s['atom'] for s in convex_solution['solution'].values() if s['active']]
    
    if len(active_atoms) < 2:
        return 0.0
    
    # Compute pairwise cosine similarity
    from sklearn.metrics.pairwise import cosine_similarity
    similarity_matrix = cosine_similarity(active_atoms)
    
    # Specialization = 1 - mean similarity (excluding self-similarity)
    n = len(active_atoms)
    mean_similarity = (similarity_matrix.sum() - n) / (n * (n - 1))
    
    return 1 - mean_similarity

def estimate_hierarchy_depth(convex_solution):
    """
    Estimate hierarchical tree depth from feature structure
    
    Approximation: clustering depth of active atoms
    """
    active_atoms = [s['atom'] for s in convex_solution['solution'].values() if s['active']]
    
    if len(active_atoms) < 10:
        return 1
    
    # Hierarchical clustering
    from sklearn.cluster import AgglomerativeClustering
    clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0.3)
    labels = clustering.fit_predict(active_atoms)
    
    # Depth = max cluster level
    return clustering.n_clusters_
```

### Phase 3: Validation & Interpretation

#### Step 1: Validate SAE Behaviors
```python
def validate_sae_phenomena(D, Z, X, lambda_reg):
    """
    Validate if observed SAE behaviors match optimality theory predictions
    
    Checks:
    1. Hierarchical splitting matches data sub-clusters
    2. Absorbed features were low-activation
    3. Residuals have interpretable structure
    4. Dense features are antipodal pairs
    """
    validation_results = {}
    
    # 1. Splitting validation
    splits = detect_feature_splitting(D[:, :D.shape[1]//2], D, Z[:D.shape[1]//2], Z, X, lambda_reg)
    validation_results['splitting'] = {
        'n_splits': len(splits),
        'avg_reconstruction_gain': np.mean([s['reconstruction_gain'] for s in splits]) if splits else 0,
        'matches_subclusters': verify_subcluster_match(splits, X)
    }
    
    # 2. Absorption validation
    activation_rates = np.abs(Z).sum(axis=1) / X.shape[0]
    low_activation_features = np.where(activation_rates < 0.05)[0]
    
    validation_results['absorption'] = {
        'n_low_activation': len(low_activation_features),
        'absorption_candidates': low_activation_features,
        'would_be_absorbed': [
            idx for idx in low_activation_features
            if np.linalg.norm(D[:, idx] @ Z[idx]) ** 2 < lambda_reg * np.abs(Z[idx]).sum()
        ]
    }
    
    # 3. Residual structure validation
    residual_analysis = analyze_residual_structure(D, Z, X)
    validation_results['residual'] = {
        'has_structure': len(residual_analysis['orthogonal_directions']) > 0,
        'n_potential_features': residual_analysis['suggested_features'],
        'interpretable': check_interpretability(residual_analysis['orthogonal_directions'])
    }
    
    # 4. Dense antipodal features
    dense_features = np.where(activation_rates > 0.3)[0]
    antipodal_pairs = find_antipodal_pairs(D[:, dense_features])
    
    validation_results['antipodal'] = {
        'n_dense': len(dense_features),
        'n_antipodal_pairs': len(antipodal_pairs),
        'pairs': antipodal_pairs
    }
    
    return validation_results

def find_antipodal_pairs(D_subset, similarity_threshold=-0.7):
    """
    Find features that are antipodal (opposite directions)
    """
    pairs = []
    n = D_subset.shape[1]
    
    for i in range(n):
        for j in range(i+1, n):
            similarity = cosine_similarity(D_subset[:, i], D_subset[:, j])
            if similarity < similarity_threshold:  # Negative = antipodal
                pairs.append((i, j, similarity))
    
    return pairs

def check_interpretability(directions):
    """
    Heuristic: interpretable directions have low entropy activation patterns
    """
    if not directions:
        return False
    
    # Simplified: assume interpretable if directions cluster well
    from sklearn.cluster import KMeans
    try:
        kmeans = KMeans(n_clusters=min(5, len(directions)))
        labels = kmeans.fit_predict(directions)
        
        # Low cluster variance = interpretable
        silhouette = silhouette_score(directions, labels)
        return silhouette > 0.5
    except:
        return False
```

## Technical Pitfalls

### Pitfall 1: Nonnegativity Violations
**Problem**: Standard SAE implementations allow negative activations
**Solution**: Enforce strict nonnegativity via projection
```python
# Correct approach
def enforce_nonnegativity(Z):
    """Project activations to nonnegative space"""
    return np.maximum(Z, 0)

# In training loop
Z = enforce_nonnegativity(Z)
D = enforce_nonnegativity(D)
```

### Pitfall 2: L1 Regularization Scaling
**Problem**: λ not scaled to data magnitude → incorrect sparsity
**Solution**: Normalize λ relative to ||X||²
```python
# Correct scaling
lambda_reg = lambda_base * np.mean(np.linalg.norm(X, axis=1) ** 2)

# Or use adaptive λ
lambda_adaptive = lambda_base * reconstruction_error_norm
```

### Pitfall 3: Splitting Misinterpretation
**Problem**: Splitting detected but features not semantically related
**Solution**: Verify split corresponds to data substructure
```python
def verify_semantic_split(parent_feature, child_features, X):
    """Check if children partition parent's semantic region"""
    # Compute data points activating parent
    parent_activating = np.where(Z_parent > threshold)[0]
    
    # Check children partition this set
    child1_activating = np.where(Z_child1 > threshold)[0]
    child2_activating = np.where(Z_child2 > threshold)[0]
    
    # Partition criterion
    partition_quality = (
        len(set(parent_activating) - set(child1_activating) - set(child2_activating)) < 
        0.1 * len(parent_activating)
    )
    
    return partition_quality
```

### Pitfall 4: Residual Overinterpretation
**Problem**: Treating all residual structure as meaningful
**Solution**: Filter residuals by magnitude threshold
```python
def filter_meaningful_residuals(residual, threshold_ratio=0.5):
    """Keep only residuals above significance threshold"""
    residual_norm = np.linalg.norm(residual, axis=1)
    threshold = threshold_ratio * residual_norm.mean()
    
    meaningful_residuals = residual[residual_norm > threshold]
    
    return meaningful_residuals
```

## Applications

### Application 1: SAE Interpretability Validation
**Context**: Verify SAE-derived interpretations are principled

**Implementation**:
```python
class SAEInterpretabilityValidator:
    """
    Validate SAE interpretations using optimality theory
    
    Checks:
    1. Features satisfy optimality constraints
    2. Phenomena match theoretical predictions
    3. Interpretations reflect data structure
    """
    def validate_sae(self, D, Z, X, lambda_reg):
        # Optimality check
        optimality = check_local_optimality(D, Z, X, lambda_reg)
        
        # Phenomena validation
        phenomena = validate_sae_phenomena(D, Z, X, lambda_reg)
        
        # Interpretation quality score
        quality_score = self.compute_quality_score(optimality, phenomena)
        
        return {
            'is_principled': optimality['is_optimal'],
            'phenomena_match': all([
                phenomena['splitting']['matches_subclusters'],
                phenomena['residual']['has_structure'],
                len(phenomena['antipodal']['pairs']) > 0
            ]),
            'quality_score': quality_score,
            'recommendations': self.generate_recommendations(optimality, phenomena)
        }
    
    def compute_quality_score(self, optimality, phenomena):
        """Aggregate quality metrics"""
        score = 0
        
        if optimality['is_optimal']:
            score += 0.4
        
        if phenomena['splitting']['matches_subclusters']:
            score += 0.2
        
        if phenomena['residual']['has_structure']:
            score += 0.2
        
        if phenomena['antipodal']['n_antipodal_pairs'] > 0:
            score += 0.2
        
        return score
```

### Application 2: Next-Generation SAE Design
**Context**: Design interpretable autoencoders with principled foundations

**Implementation**:
```python
class PrincipledSAE(nn.Module):
    """
    SAE designed based on optimality theory insights
    
    Improvements:
    1. Enforced nonnegativity
    2. Adaptive L1 regularization
    3. Residual monitoring for feature expansion
    """
    def __init__(self, input_dim, n_features, lambda_base=0.1):
        super().__init__()
        self.encoder = nn.Linear(input_dim, n_features)
        self.decoder = nn.Linear(n_features, input_dim, bias=False)
        
        self.lambda_base = lambda_base
        self.n_features = n_features
        
        # Track residuals for expansion decisions
        self.residual_history = []
    
    def forward(self, x):
        # Encode with ReLU (nonnegativity)
        z = F.relu(self.encoder(x))
        
        # Decode (dictionary reconstruction)
        reconstruction = self.decoder(z)
        
        # Residual tracking
        residual = x - reconstruction
        self.residual_history.append(residual.detach())
        
        return reconstruction, z
    
    def compute_loss(self, x, reconstruction, z):
        # Adaptive lambda based on reconstruction error
        recon_error = torch.norm(x - reconstruction, dim=1).mean()
        lambda_reg = self.lambda_base * recon_error
        
        # L1 regularization
        l1_penalty = lambda_reg * torch.norm(z, p=1, dim=1).mean()
        
        # Total loss
        loss = torch.norm(x - reconstruction, dim=1).mean() + l1_penalty
        
        return loss, lambda_reg
    
    def should_expand_features(self):
        """Decide if more features needed based on residual structure"""
        if len(self.residual_history) < 100:
            return False
        
        recent_residuals = torch.stack(self.residual_history[-100:])
        residual_norms = torch.norm(recent_residuals, dim=1)
        
        # Expansion criterion: residuals consistently large
        mean_residual_norm = residual_norms.mean()
        input_norm = torch.norm(self.residual_history[0], dim=1).mean()
        
        return mean_residual_norm > 0.3 * input_norm
```

### Application 3: Feature Attribution Analysis
**Context**: Attribute model decisions to SAE-derived concepts

**Implementation**:
```python
def attribute_to_features(model_output, D, Z, feature_names):
    """
    Attribute model output to SAE features with principled validation
    
    Uses optimality theory to ensure attributions are meaningful
    """
    # Verify features satisfy optimality
    optimality_check = verify_feature_optimality(D, Z)
    
    if not optimality_check['satisfied']:
        print("Warning: Features not optimal, attributions may be unreliable")
    
    # Compute attribution scores
    attribution_scores = {}
    
    for i, feature_name in enumerate(feature_names):
        # Attribution = feature activation × feature direction alignment
        activation = Z[i]
        feature_direction = D[:, i]
        
        # Alignment with output
        output_direction = compute_output_gradient_direction(model_output)
        alignment = cosine_similarity(feature_direction, output_direction)
        
        # Combined attribution
        attribution_scores[feature_name] = {
            'activation': activation,
            'alignment': alignment,
            'contribution': activation * alignment,
            'is_dense': activation > 0.3,
            'is_interpretable': optimality_check['feature_constraints'][i]['satisfied']
        }
    
    return attribution_scores
```

## Key Takeaways

### Theoretical Highlights
1. **Novel framework**: Optimality analysis without data-generating model assumptions
2. **Unified explanation**: Single theory explains multiple SAE phenomena
3. **Actionable insights**: Constraints guide next-generation SAE design

### Practical Implications
1. **Interpretability validation**: Check if SAE interpretations are principled
2. **Architecture design**: Inform feature expansion decisions
3. **Debugging SAEs**: Understand splitting, absorption, residual behaviors

### Future Directions
1. **Quantitative predictions**: Derive precise splitting thresholds
2. **Multi-layer SAEs**: Extend theory to hierarchical dictionaries
3. **Dynamic dictionaries**: Optimality for streaming/non-stationary data

## References

1. **Primary Paper**: Dorrell, W. (2026). "How Optimality Structures Sparse Dictionaries". arXiv:2606.02385
2. **Gribonval & Schnass** (2010): "Local optimality analysis" foundation
3. **Olshausen & Field** (1996): "Sparse coding in V1" original inspiration
4. **Anthropic SAE work**: Practical applications in LLM interpretability
5. **Dictionary learning theory**: Classical sparse coding literature

## Code Examples

See `scripts/` directory for:
- `optimality_analysis.py` - Constraint verification
- `splitting_detector.py` - Hierarchical splitting detection
- `residual_analyzer.py` - Missing feature identification
- `principled_sae.py` - Next-generation SAE implementation
- `interpretability_validator.py` - Validation framework

## Related Skills

- **neural-encoding-evaluation-ground-truth**: Evaluating encoding models
- **sae-brain-llm-topography**: SAE applications in brain-LLM alignment
- **feature-visualization-brain-encoder**: Feature visualization techniques
- **representation-usefulness-philosophy-neuroscience**: Interpretability philosophy

---
**Created**: 2026-06-02 (arXiv:2606.02385)
**Last Updated**: 2026-06-02
**Maintainer**: Cron Job - Neuroscience Research