---
name: feature-leakage-identifiability-entropy-models
description: Identifiability framework for direct-dependency entropy models of neural activity - diagnosing feature leakage in MaxEnt models, separating prediction from mechanism identification, state reweighting diagnostics
version: 1.0.0
author: arXiv:2606.01661 (Safaai & Sabatini, June 2026)
tags: [entropy-models, identifiability, feature-leakage, maxent, neural-computation, mechanism-recovery, hippocampus, ca1]
activation_keywords: [feature leakage, identifiability, entropy models, maxent, direct-dependency, mechanism recovery, state reweighting, conditional log-odds, temporal leakage, neural identifiability]
---

# Feature Leakage and Identifiability of Direct-Dependency Entropy Models

## Overview

Biological neurons receive thousands of synaptic inputs on branching, electrically excitable dendrites, yet population activity is often modeled with **direct input-output rules** where each input contributes independently to a scalar drive. This methodology studies what successful prediction by such models does, and does NOT, reveal about neural computation.

**Key Contribution**: Introduces diagnostics that separate **in-distribution prediction** from **recovery of the response rule**, revealing that entropy-explained fractions and raw coactivity predictions should be interpreted as predictions under the observed state distribution, NOT as evidence that mechanisms outside the direct model are absent or small.

**Core Problem**: MaxEnt models matching output rates and pairwise output-input coactivities can **absorb** omitted interaction, temporal, or hidden-state terms into fitted first-order parameters whenever they are correlated with included sufficient statistics. This is "feature leakage."

## Key Concepts

### 1. Information Projection Perspective

**Definition**: A restricted MaxEnt fit is an **information projection** - it matches sufficient statistics (rates and pairwise coactivities) but may absorb unmeasured mechanisms into first-order parameters.

**Mathematical Formulation**:
```
MaxEnt model: P(y|x) that maximizes entropy subject to:
  - Matching output rates: E[y] = observed
  - Matching pairwise coactivities: E[y_i x_j] = observed

The entropy explained is a prediction measure under P(x), NOT a mechanism test.
```

**Implication**: High entropy-explained fraction ≠ direct-dependency mechanism. It may simply mean unmeasured mechanisms correlate with measured statistics.

### 2. Feature Leakage Mechanism

**Definition**: Omitted higher-order interactions, temporal dynamics, or hidden states "leak" into first-order parameters through correlation with sufficient statistics.

**Explicit Form for Sparse Correlated Binary Inputs**:
```
Leakage has coskewness form:
  
Δθ_i = Σ_j,k λ_jk E[x_j x_k y_i]  (absorbed into first-order)

Where:
  θ_i = first-order parameter (direct input effect)
  λ_jk = second-order sufficient statistic coefficients
  x_j, x_k = input variables
  y_i = output variable
  
Higher-order interactions absorbed when correlated with pairwise statistics.
```

**Visualization**:
```
True mechanism: y = f(x₁, x₂, x₃) with interaction term x₁x₂
Measured: only pairwise coactivities (y,x₁), (y,x₂), (y,x₃)
Leakage: interaction effect x₁x₂ → absorbed into θ₁, θ₂
         if x₁x₂ correlates with x₁ or x₂ statistics
```

### 3. Diagnostics for Mechanism Recovery

#### A. State Reweighting

**Purpose**: Hold P(y|x) fixed while changing P(x) to test distribution-sensitivity.

**Method**:
```
Original distribution: P_empirical(x)
Reweighted distribution: P_balanced(x) - uniform weighting across input states

Compare entropy-explained under both:
  - If direct-dependency true: entropy-explained unchanged
  - If higher-order true: entropy-explained changes significantly
```

**Implementation**:
```python
def state_reweighting_diagnostic(y_data, x_data, model):
    """
    Test if predictions are distribution-sensitive
    
    Returns:
        - is_direct_dependency: bool
        - distribution_sensitivity: float
    """
    # Original empirical distribution
    entropy_empirical = compute_entropy_explained(y_data, x_data, model, weights='empirical')
    
    # Balanced reweighting (uniform across input states)
    balanced_weights = compute_balanced_weights(x_data)
    entropy_balanced = compute_entropy_explained(y_data, x_data, model, weights=balanced_weights)
    
    # Distribution sensitivity
    sensitivity = abs(entropy_empirical - entropy_balanced)
    
    # Direct-dependency if insensitive to distribution change
    is_direct = sensitivity < threshold
    
    return {
        'is_direct_dependency': is_direct,
        'entropy_empirical': entropy_empirical,
        'entropy_balanced': entropy_balanced,
        'distribution_sensitivity': sensitivity
    }
```

#### B. Conditional Log-Odds Contrasts

**Purpose**: Test local additivity of input effects.

**Method**:
```
For direct-dependency: 
  log P(y=1|x) - log P(y=0|x) = Σ_i θ_i x_i  (additive in inputs)

Diagnostic: compute log-odds for different x combinations
  - If additive: log-odds differences match θ predictions
  - If interaction present: systematic deviations
```

**Implementation**:
```python
def conditional_log_odds_diagnostic(y_data, x_data, model_params):
    """
    Test local additivity of input effects
    
    Returns:
        - is_additive: bool
        - interaction_detected: bool
    """
    log_odds_contrasts = []
    
    # Compute log-odds for different input configurations
    for x_config in generate_input_configs(x_data):
        P_y1 = model_predict_probability(y=1, x=x_config, params=model_params)
        P_y0 = 1 - P_y1
        
        log_odds = np.log(P_y1 / P_y0)
        
        # Compare with additive prediction
        additive_prediction = sum(model_params.theta_i * x_config[i] for i in range(len(x_config)))
        
        deviation = log_odds - additive_prediction
        log_odds_contrasts.append(deviation)
    
    # Systematic deviations indicate interactions
    interaction_detected = np.std(log_odds_contrasts) > threshold
    
    return {
        'is_additive': not interaction_detected,
        'interaction_detected': interaction_detected,
        'contrast_deviations': log_odds_contrasts
    }
```

#### C. Temporal Leakage Controls

**Purpose**: Prevent sampling-induced temporal correlation from masking true mechanisms.

**Method**:
```
Temporal leakage: consecutive samples correlated → 
  pairwise statistics absorb temporal structure

Control: 
  - Subsample to reduce temporal correlation
  - Use independent samples for fitting vs. testing
```

**Implementation**:
```python
def temporal_leakage_control(data, sampling_interval):
    """
    Prevent temporal correlation from masking mechanisms
    
    Returns:
        - leakage_reduced_data: subsampled data
        - temporal_correlation: measure of remaining correlation
    """
    # Original temporal correlation
    original_corr = compute_temporal_correlation(data)
    
    # Subsample to reduce correlation
    subsampled_indices = subsample_with_interval(data, sampling_interval)
    leakage_reduced_data = data[subsampled_indices]
    
    # Reduced correlation
    reduced_corr = compute_temporal_correlation(leakage_reduced_data)
    
    return {
        'leakage_reduced_data': leakage_reduced_data,
        'original_temporal_correlation': original_corr,
        'reduced_temporal_correlation': reduced_corr,
        'improvement': original_corr - reduced_corr
    }
```

## Ground Truth Simulations

### Simulation Protocol

**Purpose**: Validate diagnostics distinguish direct-dependency from higher-order mechanisms.

**Setup**:
```
1. Generate data from known ground-truth:
   - Direct-dependency: y = f(x₁ + x₂ + x₃)
   - Higher-order: y = f(x₁ + x₂ + x₃ + x₁x₂ + x₁x₃x₂)

2. Fit MaxEnt model matching rates and pairwise coactivities

3. Apply diagnostics:
   - Entropy explained
   - Raw coactivity prediction
   - State reweighting
   - Conditional log-odds
   - Temporal leakage control

4. Compare diagnostic outcomes for true vs. false mechanisms
```

**Results**:
```
Purely higher-order responses:
  ✓ Pass first-order entropy tests (under leakage-prone sampling)
  ✓ Pass raw coactivity tests
  ✗ FAIL state reweighting (become distribution-sensitive)
  ✗ FAIL log-odds contrasts (interaction deviations)

Conclusion: Diagnostics correctly classify after reweighting
```

## Application to CA1 Hippocampal Data

### Experimental Results

**Data**: Selected, leakage-enriched local tables from CA1 hippocampal recordings.

**Analysis**:
```python
def analyze_ca1_identifiability(ca1_data):
    """
    Apply identifiability diagnostics to CA1 recordings
    
    Returns:
        - fraction_direct: proportion of tables with direct-dependency
        - fraction_leaked: proportion with absorbed higher-order
    """
    results = []
    
    for table in ca1_data.tables:
        # Original analysis (leakage-prone)
        empirical_direct = test_direct_dependency(table, weights='empirical')
        
        # Reweighted analysis (leakage-reduced)
        balanced_direct = test_direct_dependency(table, weights='balanced')
        
        # Classification
        if empirical_direct and balanced_direct:
            classification = 'true_direct'
        elif empirical_direct and not balanced_direct:
            classification = 'leaked_higher-order'
        else:
            classification = 'no_direct'
        
        results.append({
            'table_id': table.id,
            'empirical_entropy_explained': empirical_direct.entropy_explained,
            'balanced_entropy_explained': balanced_direct.entropy_explained,
            'classification': classification
        })
    
    # Aggregate
    true_direct = sum(1 for r in results if r['classification'] == 'true_direct')
    leaked = sum(1 for r in results if r['classification'] == 'leaked_higher-order')
    
    return {
        'fraction_true_direct': true_direct / len(results),
        'fraction_leaked_higher_order': leaked / len(results),
        'detailed_results': results
    }
```

**Key Finding**: **~50% of tables** that appear first-order under empirical weights become distribution-sensitive under balanced reweighting. This is **far above matched additive-surrogate null**, indicating widespread feature leakage in CA1 data.

### Implications for Neuroscience

1. **Prediction ≠ Mechanism**: Good prediction under empirical distribution does not validate direct-dependency mechanism.

2. **Common Leakage**: Many neural responses appear first-order but absorb higher-order interactions.

3. **Diagnostic Necessity**: State reweighting essential before mechanism claims.

## Implementation Framework

### Complete Identifiability Pipeline

```python
class EntropyModelIdentifiabilityAnalyzer:
    """
    Complete pipeline for diagnosing feature leakage in MaxEnt models
    """
    
    def __init__(self, data, model_class='MaxEnt'):
        self.data = data
        self.model_class = model_class
        self.diagnostics = {}
    
    def full_analysis(self):
        """
        Run all diagnostics and classify mechanism
        
        Returns:
            - mechanism_type: 'direct-dependency' | 'higher-order' | 'mixed'
            - confidence: float
            - diagnostics: dict of test results
        """
        # 1. Fit MaxEnt model
        model = self.fit_maxent_model(self.data)
        
        # 2. Original entropy-explained
        self.diagnostics['entropy_explained_empirical'] = self.compute_entropy_explained(
            self.data, model, weights='empirical'
        )
        
        # 3. State reweighting
        reweight_result = state_reweighting_diagnostic(
            self.data.outputs, self.data.inputs, model
        )
        self.diagnostics['state_reweighting'] = reweight_result
        
        # 4. Conditional log-odds
        log_odds_result = conditional_log_odds_diagnostic(
            self.data.outputs, self.data.inputs, model.params
        )
        self.diagnostics['log_odds_contrasts'] = log_odds_result
        
        # 5. Temporal leakage
        temporal_result = temporal_leakage_control(self.data, sampling_interval=10)
        self.diagnostics['temporal_leakage'] = temporal_result
        
        # 6. Classification
        if reweight_result['is_direct_dependency'] and log_odds_result['is_additive']:
            mechanism_type = 'direct-dependency'
            confidence = 0.9
        elif not reweight_result['is_direct_dependency'] and log_odds_result['interaction_detected']:
            mechanism_type = 'higher-order'
            confidence = 0.8
        else:
            mechanism_type = 'mixed'
            confidence = 0.5
        
        return {
            'mechanism_type': mechanism_type,
            'confidence': confidence,
            'diagnostics': self.diagnostics,
            'recommendations': self.generate_recommendations()
        }
    
    def fit_maxent_model(self, data):
        """
        Fit MaxEnt model matching rates and pairwise coactivities
        """
        from sklearn.linear_model import LogisticRegression
        
        # MaxEnt with pairwise constraints
        # (implementation depends on specific MaxEnt solver)
        model = MaxEntDirectDependency(
            n_inputs=data.inputs.shape[1],
            n_outputs=data.outputs.shape[1]
        )
        
        model.fit(data.inputs, data.outputs)
        
        return model
    
    def generate_recommendations(self):
        """
        Provide recommendations based on diagnostic outcomes
        """
        recommendations = []
        
        if not self.diagnostics['state_reweighting']['is_direct_dependency']:
            recommendations.append(
                "CRITICAL: High distribution-sensitivity detected. "
                "Do NOT claim direct-dependency mechanism. "
                "Higher-order interactions likely absorbed into first-order params."
            )
        
        if self.diagnostics['log_odds_contrasts']['interaction_detected']:
            recommendations.append(
                "WARNING: Systematic log-odds deviations. "
                "Interaction terms present but not modeled. "
                "Extend model with pairwise or higher-order terms."
            )
        
        if self.diagnostics['temporal_leakage']['original_temporal_correlation'] > 0.3:
            recommendations.append(
                "INFO: High temporal correlation in data. "
                "Use subsampled data for mechanism claims. "
                "Temporal structure may leak into pairwise statistics."
            )
        
        return recommendations
```

## Pitfalls & Misinterpretations

### Pitfall 1: High Entropy-Explained = Direct Mechanism

**Common Misinterpretation**: "Entropy-explained fraction 90% → direct-dependency mechanism confirmed."

**Correction**: 
```
High entropy-explained means:
  ✓ Good prediction under empirical distribution P_empirical(x)
  ✗ NOT evidence that higher-order mechanisms absent

Reason: Absorption/leakage can give high prediction 
        even with strong higher-order interactions
```

**Diagnostic Required**: State reweighting to test distribution-sensitivity.

### Pitfall 2: Raw Coactivity Prediction = Mechanism Test

**Common Misinterpretation**: "Coactivity prediction accurate → mechanism recovered."

**Correction**:
```
Coactivity prediction tests:
  E[y_i x_j] under P_empirical(x)

This is in-distribution prediction, NOT mechanism identification.
Mechanism test requires: hold P(y|x) fixed, change P(x)
```

**Diagnostic Required**: Balanced reweighting across input states.

### Pitfall 3: Leakage-Free Sampling Guarantees Identifiability

**Problem**: Even without temporal leakage, **correlation leakage** can occur.

**Solution**:
```
Temporal leakage: consecutive samples correlated
Correlation leakage: input variables correlated

Both cause absorption: higher-order statistics leak into first-order

Diagnostic: state reweighting handles both
```

### Pitfall 4: Model Comparison Solves Identifiability

**Problem**: Comparing direct vs. higher-order models on same data does not solve identifiability.

**Reason**: Both models can fit equally well under empirical distribution if higher-order terms correlate with pairwise statistics.

**Solution**: Test on **different distributions** (state reweighting) to distinguish.

## Applications

### Application 1: Neural Mechanism Validation

**Context**: Validate direct-dependency mechanism claims in neural data.

**Workflow**:
```python
# Step 1: Fit MaxEnt model
model = MaxEntDirectDependency()
model.fit(neural_inputs, neural_outputs)

# Step 2: Compute entropy-explained
entropy_explained = model.explained_fraction()

# Step 3: CRITICAL - Apply identifiability diagnostics
analyzer = EntropyModelIdentifiabilityAnalyzer(neural_data)
result = analyzer.full_analysis()

# Step 4: Interpret result
if result['mechanism_type'] == 'direct-dependency':
    print("Direct-dependency mechanism validated with high confidence")
elif result['mechanism_type'] == 'higher-order':
    print("WARNING: Higher-order interactions absorbed. Direct-dependency false.")
else:
    print("Mixed mechanism. Further investigation needed.")
```

### Application 2: Dendritic Computation Studies

**Context**: Study if dendritic branching creates higher-order interactions vs. direct summation.

**Application**:
```
Hypothesis: Dendritic filtering creates interactions beyond direct summation

Test:
  1. Record dendritic inputs and outputs
  2. Fit direct-dependency MaxEnt
  3. Apply state reweighting diagnostic
  
Interpretation:
  - If distribution-sensitive: dendritic filtering creates interactions
  - If distribution-insensitive: direct summation sufficient
```

### Application 3: Network Control Theory

**Context**: Control neural networks via input perturbation. Need true mechanism to design control.

**Relevance**:
```
Direct-dependency mechanism:
  Control: linear input perturbation → predictable output change

Higher-order mechanism:
  Control: linear perturbation unpredictable (interaction effects)
  
Identifiability diagnostic essential before control design.
```

## Key Takeaways

### Theoretical Summary

1. **Information projection**: MaxEnt models project onto sufficient statistics, potentially absorbing unmeasured mechanisms.

2. **Feature leakage**: Higher-order interactions leak into first-order parameters through correlation with pairwise statistics.

3. **Coskewness form**: Leakage has explicit mathematical expression for sparse binary inputs.

4. **Distribution-sensitivity**: True mechanism test requires changing input distribution while holding P(y|x) fixed.

### Practical Implications

1. **Prediction ≠ Mechanism**: Good prediction under empirical distribution does not validate mechanism.

2. **Diagnostic necessity**: State reweighting, log-odds contrasts, temporal controls essential.

3. **CA1 evidence**: ~50% of apparent first-order responses are leaked higher-order.

### Future Directions

1. **General leakage theory**: Extend beyond binary sparse inputs.

2. **Multi-output interactions**: Interactions across outputs, not just inputs.

3. **Temporal identifiability**: Mechanism recovery in streaming data.

## References

- **Primary**: arXiv:2606.01661 - Safaai & Sabatini (2026)
- **MaxEnt theory**: Jaynes (1957), Schneidman et al. (2006)
- **Identifiability**: Gribonval (2011), trait identifiability
- **Hippocampal coding**: O'Keefe & Dostrovsky (1971), place cells

## Activation

Trigger when:
- Analyzing neural data with entropy models
- Validating direct-dependency mechanism claims
- Diagnosing feature leakage in MaxEnt fits
- Studying dendritic computation mechanisms
- Keywords: feature leakage, identifiability, entropy models, mechanism recovery, state reweighting