---
skill_name: trajectory-geometry-transformer-representations
description: Neuroscience-inspired trajectory geometry framework for analyzing transformer representations across layers using computational neuroscience tools - trajectory length, curvature, semantic convergence, and attractor-like dynamics.
version: 1.0
last_updated: 2026-06-10
arxiv_id: 2606.09287v1
paper_title: "Trajectory Geometry of Transformer Representations Across Layers"
paper_url: https://arxiv.org/abs/2606.09287v1
authors: Vishal Pandey, Gopal Singh
published: 2026-06-08
categories: [cs.LG]
activation_keywords: [trajectory geometry, transformer interpretability, attractor dynamics, representation evolution, layerwise analysis, semantic convergence, computational neuroscience, probe-free interpretability, curvature analysis]
related_skills: [neuroscience-of-transformers, brain-inspired-snn-pattern-analysis, attractor-metadynamics-neural]
status: available
---

# Trajectory Geometry: Probe-Free Transformer Interpretability

## Overview

This framework recasts the transformer forward pass as a **discrete population trajectory** through a high-dimensional representation manifold, using geometric tools from computational neuroscience. It characterizes trajectory geometry through five metrics computed directly in ambient space, enabling **probe-free mechanistic interpretability** without requiring pre-specified feature probing.

## Core Innovation

### 1. Population Trajectory Perspective
- **Forward pass as trajectory**: Representations evolve as discrete points moving through representation manifold
- **Layer-wise evolution**: Each layer creates a step in the trajectory (discrete dynamics)
- **Geometric characterization**: Quantify trajectory shape/behavior directly in high-dimensional space
- **No probing required**: Analysis done in ambient space without feature detectors

### 2. Five Trajectory Geometry Metrics

#### (A) Trajectory Length
```
L = Σ_{l=0}^{L-1} ||h_{l+1} - h_l||

Measures total distance traveled through representation space
- Longer trajectories → more computational processing
- Shorter trajectories → more direct mapping
```

#### (B) Trajectory Curvature
```
κ_l = angle between (h_{l+1} - h_l) and (h_l - h_{l-1})

Curvature in radians (0 = straight, π = reversal)
- High curvature → computational complexity
- Low curvature → smooth progression
- Task-dependent: reasoning > lexical variation
```

#### (C) Semantic Convergence Index (CI)
```
CI = correlation of trajectory positions for semantically related prompts

Peak CI: 0.41--0.58 (p<0.001, Mann-Whitney U)
- High CI → attractor-like convergence
- Semantic clustering in middle-to-late layers
```

#### (D) Layerwise Cosine Similarity
```
cos_sim(l, l') = (h_l · h_l') / (||h_l|| ||h_l'||)

Reveals three-phase structure:
1. Encoding phase: Low similarity (rapid change)
2. Elaboration phase: Moderate similarity (processing)
3. Output preparation: High similarity (stabilization)
```

#### (E) Representational Stability
```
Stability = 1 / variance of representations across layers

Measures consistency of trajectory:
- High stability → converged representation
- Low stability → ongoing evolution
- Ambiguous tokens → bifurcation (low stability)
```

### 3. Three-Phase Universal Structure

**Discovery**: All transformer architectures (GPT-2, TinyLlama, Qwen2.5) show:
1. **Encoding Phase** (Early layers): Rapid representation change
2. **Elaboration Phase** (Middle layers): Semantic convergence, attractor-like dynamics
3. **Output Preparation Phase** (Late layers): Stabilization toward final output

## Key Findings

### Finding 1: Semantic Convergence (Attractor-Like Dynamics)
- **Peak CI**: 0.41--0.58 in middle-to-late layers
- **Statistical significance**: p<0.001 (Mann-Whitney U)
- **Interpretation**: Semantically related prompts converge to similar representations
- **Neuroscience analogy**: Attractor dynamics in recurrent networks

### Finding 2: Curvature Encodes Computational Complexity
- **Reasoning tasks**: Curvature 0.71--0.83 rad (high curvature)
- **Lexical variations**: Curvature 0.27--0.31 rad (low curvature)
- **Implication**: Curvature is computational complexity proxy
- **Task differentiation**: Geometry distinguishes task types

### Finding 3: Trajectory Bifurcation for Ambiguous Tokens
- **Representational separation**: Up to 5.6x increase by final layer
- **Ambiguous tokens**: Trajectory bifurcation (multiple paths)
- **Unambiguous controls**: Single trajectory path (no bifurcation)
- **Interpretation**: Ambiguity creates competing representations

### Finding 4: Universal Three-Phase Structure
- **Architecture-independent**: Same structure in GPT-2, TinyLlama, Qwen2.5
- **Phase boundaries**: Consistent layer indices across models
- **Control validation**: Shuffled-layer/random-embedding removes phases

## Methodology Details

### 1. Trajectory Construction
```python
# For each prompt:
# 1. Extract layer-wise representations h_0, h_1, ..., h_L
# 2. Construct trajectory points in high-dimensional space
# 3. Compute geometric metrics between consecutive layers

trajectory = [h_0, h_1, h_2, ..., h_L]  # L = number of layers
```

### 2. Metric Computation Pipeline
```python
# Trajectory Length
L = sum([norm(h[l+1] - h[l]) for l in range(L-1)])

# Trajectory Curvature
curvature[l] = angle(h[l+1] - h[l], h[l] - h[l-1])

# Semantic Convergence Index
CI[l] = correlation(h_A[l], h_B[l])  # for semantically related prompts A, B

# Layerwise Cosine Similarity
cos_sim[l, l'] = dot(h[l], h[l']) / (norm(h[l]) * norm(h[l']))

# Representational Stability
stability = 1 / variance([h[l] for l in range(L)])
```

### 3. Control Experiments
- **Shuffled-layer control**: Randomize layer order → all effects vanish
- **Random-embedding control**: Use random vectors → no structure
- **Statistical tests**: Mann-Whitney U, permutation tests

## Practical Implementation

### Model-Agnostic Pipeline
```python
# 1. Load transformer model (any architecture)
# 2. Extract layer-wise representations for prompts
# 3. Compute five geometric metrics
# 4. Analyze trajectory patterns
# 5. Compare across task types, architectures

class TrajectoryGeometryAnalyzer:
    def extract_trajectory(self, model, prompt):
        # Get layer-wise hidden states
        with torch.no_grad():
            outputs = model(prompt, output_hidden_states=True)
            trajectory = outputs.hidden_states  # [layer_dim]
        return trajectory
    
    def compute_metrics(self, trajectory):
        metrics = {
            'length': self.compute_length(trajectory),
            'curvature': self.compute_curvature(trajectory),
            'stability': self.compute_stability(trajectory)
        }
        return metrics
    
    def semantic_convergence(self, traj_A, traj_B):
        # Compute CI for semantically related prompts
        CI = [correlation(traj_A[l], traj_B[l]) 
              for l in range(len(traj_A))]
        return CI
```

### Task Comparison Analysis
```python
# Compare reasoning vs lexical variation tasks
reasoning_trajectories = [extract_trajectory(model, p) 
                          for p in reasoning_prompts]
lexical_trajectories = [extract_trajectory(model, p) 
                        for p in lexical_prompts]

# Curvature comparison
reasoning_curvature = [compute_curvature(t) for t in reasoning_trajectories]
lexical_curvature = [compute_curvature(t) for t in lexical_trajectories]

# Statistical test
test_result = mann_whitney_u(reasoning_curvature, lexical_curvature)
# Result: reasoning curvature (0.71-0.83) > lexical (0.27-0.31), p<0.001
```

### Ambiguity Detection
```python
# Detect trajectory bifurcation for ambiguous tokens
ambiguous_trajectory = extract_trajectory(model, ambiguous_prompt)
unambiguous_trajectory = extract_trajectory(model, unambiguous_prompt)

# Compute representational separation across layers
separation[l] = norm(ambiguous_trajectory[l] - baseline[l]) / 
                norm(unambiguous_trajectory[l] - baseline[l])

# Result: separation up to 5.6x for ambiguous, ~1x for unambiguous
```

## Connection to Neuroscience

### Attractor Dynamics Analogy
- **Semantic convergence**: CI peaks → attractor-like convergence
- **Multiple attractors**: Different semantic clusters have distinct attractors
- **Basin of attraction**: Semantically related prompts converge to same attractor
- **Neuroscience parallel**: Similar to recurrent network attractor dynamics

### Trajectory Curvature as Complexity
- **High curvature**: Sharp turns → complex computation (reasoning)
- **Low curvature**: Smooth paths → simpler mapping (lexical)
- **Neural correlate**: Neural trajectory curvature correlates with task difficulty
- **Interpretation**: Geometry encodes computational complexity

### Bifurcation and Ambiguity
- **Trajectory splitting**: Ambiguous tokens → multiple trajectory paths
- **Competing representations**: Ambiguity creates competing attractors
- **Neuroscience analogy**: Neural bifurcation for ambiguous stimuli
- **Resolution**: Late layers resolve ambiguity (choose path)

### Three-Phase Structure
- **Encoding**: Rapid change → sensory processing (early visual cortex)
- **Elaboration**: Semantic convergence → recurrent processing (higher cortex)
- **Output preparation**: Stabilization → motor/action output (output layers)

## Experimental Validation

### Model Coverage
- **GPT-2**: Standard transformer baseline
- **TinyLlama**: Efficient transformer variant
- **Qwen2.5**: Multilingual transformer
- **Result**: Universal structure across all architectures

### Prompt Families
- **Reasoning tasks**: Math problems, logical inference
- **Lexical variations**: Synonym substitutions, paraphrases
- **Ambiguous tokens**: Words with multiple meanings
- **Control prompts**: Random/shuffled prompts

### Statistical Validation
- **Semantic convergence**: p<0.001 (Mann-Whitney U)
- **Curvature difference**: p<0.001 (reasoning > lexical)
- **Bifurcation detection**: 5.6x separation (ambiguous vs unambiguous)
- **Control validation**: All effects vanish in shuffled/random controls

## Applications

### 1. Mechanistic Interpretability
- **Probe-free analysis**: No need for feature detectors
- **Task understanding**: Geometry reveals computational nature
- **Model comparison**: Compare architectures via trajectory patterns
- **Debugging**: Identify anomalous trajectory behavior

### 2. Model Architecture Design
- **Layer optimization**: Identify efficient layer structures
- **Phase tuning**: Adjust phase boundaries for specific tasks
- **Convergence enhancement**: Design for semantic attractor formation
- **Curvature control**: Architecture choices affect trajectory geometry

### 3. Ambiguity Detection
- **Real-time monitoring**: Detect bifurcation during inference
- **Resolution tracking**: Monitor ambiguity resolution across layers
- **Failure prediction**: Unresolved bifurcation → prediction errors
- **Intervention**: Early detection enables intervention strategies

### 4. Task Classification
- **Geometry-based classification**: Curvature, length → task type
- **Complexity estimation**: High curvature → complex task
- **Semantic grouping**: CI clustering → semantic categories
- **Prompt optimization**: Minimize trajectory complexity for efficiency

## Limitations

### Current Limitations
1. **Ambient space analysis**: No explicit low-dimensional manifold
2. **Static geometry**: Doesn't capture temporal dynamics within layers
3. **Prompt dependency**: Trajectory geometry varies across prompts
4. **Layer discretization**: Continuous dynamics approximated as discrete

### Future Extensions
- **Manifold learning**: Combine with explicit manifold extraction
- **Continuous dynamics**: Model within-layer evolution
- **Prompt normalization**: Standardize geometry across prompt diversity
- **Temporal analysis**: Time-resolved trajectory evolution

## Technical Specifications

### Representation Extraction
- **Layer-wise hidden states**: Extract from transformer.hidden_states
- **Position**: Use final token position for trajectory
- **Normalization**: Optional L2 normalization before metric computation

### Metric Definitions (Mathematical)
```
Trajectory Length:
L = Σ_{l=0}^{L-1} ||h_{l+1} - h_l||_2

Curvature:
κ_l = arccos( (Δh_l · Δh_{l-1}) / (||Δh_l|| ||Δh_{l-1}||) )
where Δh_l = h_{l+1} - h_l

Semantic Convergence Index:
CI_l = corr(h_A[l], h_B[l])

Representational Stability:
S = 1 / (Σ_l ||h_l - mean(h)||^2 / L)
```

### Statistical Tests
- **Mann-Whitney U**: Non-parametric comparison
- **Permutation tests**: Significance validation
- **Bootstrap**: Confidence intervals for metrics

## Usage Examples

### Example 1: Compare Task Types
```python
# Analyze reasoning vs lexical variation
analyzer = TrajectoryGeometryAnalyzer()

# Extract trajectories
reasoning_traj = [analyzer.extract_trajectory(model, p) 
                  for p in reasoning_prompts]
lexical_traj = [analyzer.extract_trajectory(model, p) 
                for p in lexical_prompts]

# Compute metrics
reasoning_metrics = [analyzer.compute_metrics(t) for t in reasoning_traj]
lexical_metrics = [analyzer.compute_metrics(t) for t in lexical_traj]

# Compare curvature
print(f"Reasoning curvature: {np.mean([m['curvature'] for m in reasoning_metrics])}")
print(f"Lexical curvature: {np.mean([m['curvature'] for m in lexical_metrics])}")

# Result: Reasoning (0.71-0.83) > Lexical (0.27-0.31), p<0.001
```

### Example 2: Detect Ambiguity
```python
# Monitor trajectory bifurcation for ambiguous token
ambiguous_prompt = "The bank of the river"  # "bank" is ambiguous
unambiguous_prompt = "The river bank"  # clear meaning

amb_traj = analyzer.extract_trajectory(model, ambiguous_prompt)
unamb_traj = analyzer.extract_trajectory(model, unambiguous_prompt)

# Compute separation across layers
separation = [norm(amb_traj[l] - baseline[l]) / 
              norm(unamb_traj[l] - baseline[l]) 
              for l in range(len(amb_traj))]

# Check for bifurcation (separation > threshold)
if max(separation) > 5.0:
    print("Ambiguity detected: trajectory bifurcation observed")
```

### Example 3: Semantic Convergence Analysis
```python
# Analyze semantic convergence for related prompts
prompt_A = "The cat sat on the mat"
prompt_B = "A feline rested on the rug"  # semantic variant

traj_A = analyzer.extract_trajectory(model, prompt_A)
traj_B = analyzer.extract_trajectory(model, prompt_B)

# Compute CI across layers
CI = analyzer.semantic_convergence(traj_A, traj_B)

# Find peak convergence
peak_layer = np.argmax(CI)
peak_CI = CI[peak_layer]

print(f"Peak semantic convergence at layer {peak_layer}: CI={peak_CI}")
# Result: Peak CI 0.41-0.58 in middle-to-late layers, p<0.001
```

### Example 4: Three-Phase Identification
```python
# Identify encoding, elaboration, output phases
trajectory = analyzer.extract_trajectory(model, prompt)

# Compute layerwise cosine similarity
cos_sim = [cosine_similarity(trajectory[l], trajectory[0]) 
           for l in range(len(trajectory))]

# Detect phase boundaries (similarity gradient changes)
phase_boundaries = analyzer.detect_phase_boundaries(cos_sim)

print(f"Encoding phase: layers 0-{phase_boundaries[0]}")
print(f"Elaboration phase: layers {phase_boundaries[0]}-{phase_boundaries[1]}")
print(f"Output preparation: layers {phase_boundaries[1]}-L")
```

## Key Takeaways

1. **Probe-free interpretability**: Direct geometric analysis in ambient space
2. **Universal structure**: Three-phase organization across architectures
3. **Semantic convergence**: Attractor-like dynamics in transformers
4. **Curvature → complexity**: Geometry encodes task computational nature
5. **Ambiguity detection**: Trajectory bifurcation reveals competing representations

## Summary

Trajectory geometry provides a **neuroscience-inspired, probe-free framework** for transformer interpretability that:
- **Characterizes evolution**: Representation progression through manifold
- **Reveals structure**: Universal three-phase organization
- **Detects complexity**: Curvature distinguishes task types
- **Identifies semantics**: Convergence index shows attractor-like dynamics
- **Monitors ambiguity**: Bifurcation reveals competing representations

This methodology enables **mechanistic interpretability without probing**, using geometric tools from computational neuroscience to understand transformer computation.

---

**Activation**: trajectory geometry, transformer interpretability, attractor dynamics, representation evolution, layerwise analysis, semantic convergence, computational neuroscience, probe-free interpretability, curvature analysis, three-phase structure, trajectory bifurcation