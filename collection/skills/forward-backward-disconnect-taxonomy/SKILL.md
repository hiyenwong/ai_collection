---
name: forward-backward-disconnect-taxonomy
description: "Forward-backward disconnect taxonomy for neural computation."
metadata:
  arxiv_id: "2608.19995"
  published: "2026-08-20"
  authors: "Hadi Al Mubasher, Mariette Awad"
  tags: [neural-computation, credit-assignment, state-dynamics, biological-grounding, taxonomy, forward-backward-disconnect]
license: Complete terms in LICENSE.txt
---

# Forward-Backward Disconnect Taxonomy

## Overview

This skill implements the methodology from "The Forward-Backward Disconnect: State Dynamics, Credit Assignment, and Biological Grounding in Neural Computation" (arXiv:2608.19995), which identifies and analyzes a fundamental asymmetry in neural computation. While forward dynamics have diversified across multiple state-dynamics classes (static, recurrent, attention-based, state-space, continuous-time, implicit, spiking), scalable credit assignment mechanisms remain concentrated around backpropagation and its variants.

The framework provides a three-axis taxonomy for analyzing neural model families: state-dynamics structure, credit-assignment mechanism, and biological grounding (split into separate forward and learning dimensions). The atomic unit of analysis is the architecture-learning configuration rather than the architecture name alone.

## Key Contributions

- **Taxonomy Framework**: Three coupled axes organize neural computation models systematically
- **Forward-Backward Disconnect**: Names and characterizes the asymmetry between diversified forward dynamics and concentrated credit assignment
- **Configuration-Level Analysis**: Treats architecture-learning pairs as atomic units rather than architectures in isolation
- **Biological Grounding Separation**: Distinguishes forward biological grounding from learning biological grounding
- **Substrate Alignment**: Connects algorithmic taxonomy to computational substrate requirements
- **Empirical Audit**: Comprehensive survey of 32 representative configurations across neural model families

## Methodology

### Three-Axis Taxonomy

**Axis 1: State-Dynamics Structure**
- **Static**: Memoryless input-output maps (MLP, CNN, ResNet)
- **Discrete-time/Sequence**: Explicit recurrence or sequence-level computation (RNN, LSTM, Transformer, SSM)
- **Continuous-time**: Differential equation-based evolution (Neural ODE, Liquid RNN)
- **Implicit**: Equilibrium-based computation (Modern Hopfield, DEQ, Implicit Layers)
- **Hybrid Event-driven**: Spiking networks with discrete spike timing (SNN)

**Axis 2: Credit-Assignment Mechanism**
- **Global Gradient**: Backpropagation, BPTT, adjoint methods
- **Approximate/Implicit Gradient**: Surrogate gradients, synthetic gradients, predictive coding approximations
- **Local Plasticity**: Hebbian rules, STDP, dendrite-local learning
- **Energy/Unsupervised**: Contrastive divergence, equilibrium propagation, energy minimization

**Axis 3: Biological Grounding**
- **Forward Grounding**: How well forward dynamics match biological neural computation
- **Learning Grounding**: How well credit assignment matches biological synaptic plasticity
- **Grounding Tiers**: Strong (mechanistic), Functional (analogy), Weak (metaphorical)

### Configuration Classification Protocol

To classify a new architecture-learning configuration:

1. **Identify State Variable**: Determine the mathematical form of internal state evolution
2. **Map to State-Dynamics Class**: Assign to one of five state-dynamics categories
3. **Identify Credit Assignment**: Determine the learning mechanism used for parameter updates
4. **Map to Credit-Assignment Class**: Assign to appropriate credit-assignment category
5. **Assess Biological Grounding**: Evaluate both forward and learning grounding independently
6. **Document Rationale**: Record placement decisions with supporting evidence

### Analysis Workflow

1. **Literature Survey**: Systematic search across databases (ACM, IEEE, arXiv) with temporal windows
2. **Configuration Identification**: Extract architecture-learning pairs from representative papers
3. **Taxonomic Placement**: Apply classification protocol to each configuration
4. **Pattern Analysis**: Identify cross-family structural patterns and asymmetries
5. **Gap Identification**: Flag underrepresented combinations as research opportunities

## Applications

### Research Planning and Positioning
- **Gap Analysis**: Identify underexplored architecture-learning-substrate combinations
- **Research Prioritization**: Focus on combinations that address current limitations
- **Literature Organization**: Systematically categorize existing work for comprehensive understanding

### Model Selection and Design
- **Trade-off Analysis**: Understand scalability vs. biological plausibility trade-offs
- **Architecture-Learning Co-design**: Design compatible forward-backward pairs
- **Substrate Alignment**: Match algorithmic choices to hardware capabilities

### Educational and Diagnostic Use
- **Conceptual Clarity**: Provide clear framework for understanding neural computation landscape
- **Diagnostic Constraint**: Use biology as constraint rather than metaphor to expose preserved/discarded mechanisms
- **Historical Context**: Understand evolution of neural computation through taxonomic lens

## Implementation Guidelines

### Literature Review Process
1. **Define Search Scope**: Set temporal windows (foundational, representative, recent high-impact)
2. **Apply Boolean Queries**: Use taxonomy-aligned search strings across multiple databases
3. **Screen for Relevance**: Filter by state-dynamics and credit-assignment relevance
4. **Extract Configurations**: Identify architecture-learning pairs from selected papers
5. **Classify Systematically**: Apply taxonomy to each configuration with documented rationale

### Configuration Analysis
1. **State-Dynamics Assessment**: Analyze mathematical form of state evolution
2. **Credit-Assignment Characterization**: Determine learning mechanism properties
3. **Biological Grounding Evaluation**: Assess both forward and learning biological correspondence
4. **Scalability Documentation**: Record demonstrated scaling capabilities and limitations
5. **Substrate Considerations**: Note hardware alignment and computational requirements

### Pattern Synthesis
1. **Cross-Family Comparison**: Compare configurations across state-dynamics classes
2. **Asymmetry Quantification**: Measure concentration of credit assignment mechanisms
3. **Gap Identification**: Flag sparse regions in joint taxonomy space
4. **Research Implications**: Derive priorities from identified gaps and patterns
5. **Validation**: Cross-check findings with empirical evidence and scaling claims

## Pitfalls and Limitations

### Classification Challenges
- **Ambiguous Placements**: Some configurations may fit multiple categories
- **Evolving Definitions**: Taxonomy boundaries may shift with new developments
- **Scope Limitations**: Framework excludes certain model families (GNNs, KANs, diffusion models)

### Interpretation Caveats
- **Descriptive vs. Prescriptive**: Taxonomy describes observed patterns, not optimal designs
- **Coverage Bias**: English-language, indexed works may be overrepresented
- **Recency Effects**: Recent developments may appear more significant than warranted

### Practical Constraints
- **Implementation Complexity**: Full taxonomic analysis requires significant expertise
- **Dynamic Field**: Rapid evolution may outpace systematic classification efforts
- **Interdisciplinary Gaps**: Requires knowledge across neuroscience, ML, and systems engineering

## Activation Keywords

- forward-backward disconnect
- neural computation taxonomy
- state-dynamics structure
- credit assignment mechanisms
- biological grounding neural models
- architecture-learning configuration
- neural model families analysis

## References

- Al Mubasher, H., & Awad, M. (2026). The Forward-Backward Disconnect: State Dynamics, Credit Assignment, and Biological Grounding in Neural Computation. arXiv:2608.19995
- Maass, W. (1997). Networks of spiking neurons: The third generation of neural network models. Neural Networks
- Lillicrap, T. P., et al. (2020). Backpropagation and the brain. Nature Reviews Neuroscience
- Neftci, E. O., et al. (2019). Surrogate gradient learning in spiking neural networks. arXiv:1901.09948
- Whittington, J. C. R., & Bogacz, R. (2019). Theories of error back-propagation in the brain. Trends in Cognitive Sciences