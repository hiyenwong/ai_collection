---
name: activity-dependent-epidemic-spreading-alzheimers
description: "Epidemic spreading with activity predicts Alzheimer's."
metadata:
  arxiv_id: "2608.12647"
  published: "2026-08-12"
  authors: "Christoffer G. Alexandersen, Suman S. Kulkarni, Jessica T. Davis, Sebastian N. Roemer-Cassiano, Nicolai Franzmeier, Dani S Bassett"
  tags: [alzheimers, epidemic-modeling, brain-networks, neuronal-activity, tau-propagation]
license: Complete terms in LICENSE.txt
---

# Activity-dependent Epidemic Spreading for Alzheimer's Disease Progression

## Overview

This methodology couples neuronal activity processes to susceptible-infected-susceptible (SIS) dynamics to model how pathological proteins propagate through brain networks in Alzheimer's disease. The framework accounts for how neuronal firing promotes protein transmission, providing more accurate predictions of disease progression than structural connectivity alone.

## Key Contributions

1. **Activity-dependent epidemic threshold**: Neuronal activity shifts the epidemic threshold that determines whether small pathological seeds can grow
2. **Dominant network mode redirection**: Activity redirects spreading by mixing structural network modes  
3. **Multiscale decomposition**: Separates contributions from regional mean activity and within-region activity variation
4. **Clinical validation**: Uses longitudinal PET data with glucose metabolism as neuronal activity proxy and tau accumulation as disease progression marker

## When to Use This Skill

Use this methodology when:
- Modeling neurodegenerative disease progression on brain networks
- Need to incorporate neuronal activity into epidemic spreading models
- Predicting spatial patterns of pathological protein accumulation
- Analyzing Alzheimer's disease progression using PET imaging data
- Studying activity-modulating therapies to slow pathological spread

## Methodology

### Core Framework
The model couples a general node-activity process to SIS dynamics:
- **Epidemic threshold**: Determines if pathological seeds can grow
- **Network modes**: Determine where growth begins  
- **Activity coupling**: Neuronal firing modifies transmission rates

### Theoretical Analysis
- Derive approximations showing how neuronal activity shifts epidemic threshold
- Show how activity redirects spreading by mixing structural network modes
- For multiscale networks, decompose changes into regional mean vs. within-region variation contributions

### Validation Approach
1. **Synthetic networks**: Validate theoretical results with stochastic simulations
2. **Human data**: Use longitudinal PET with:
   - Glucose metabolism → neuronal activity proxy
   - Tau accumulation → disease progression measure
3. **Model comparison**: Compare activity-enhanced model vs. structural connectivity-only model

## Implementation Steps

1. **Network construction**: Build multiscale brain network from structural connectivity data
2. **Activity measurement**: Obtain neuronal activity data (e.g., glucose metabolism from PET)
3. **Parameter estimation**: Calibrate epidemic parameters using baseline pathology data
4. **Simulation**: Run activity-dependent SIS dynamics to predict progression
5. **Validation**: Compare predictions against longitudinal tau accumulation data

## Pitfalls and Considerations

- **Activity heterogeneity**: Brain imaging may not resolve fine-grained activity variation
- **Network resolution**: Multiscale structure must be properly captured in the network model
- **Parameter sensitivity**: Epidemic threshold is sensitive to activity scaling factors
- **Temporal alignment**: Activity and pathology measurements must be temporally aligned

## Applications

- **Therapeutic targeting**: Identify regions where activity modulation could slow spread
- **Progression prediction**: Forecast individual-specific disease trajectories
- **Biomarker development**: Validate neuronal activity as predictor of pathological spread
- **Network medicine**: Understand how network topology influences disease vulnerability

## References

- Original paper: arXiv:2608.12647 [q-bio.NC]
- Related work: Network neuroscience, epidemic theory, neurodegenerative disease modeling
- Clinical data: Longitudinal PET studies with glucose metabolism and tau imaging

## Activation Keywords

- alzheimer's disease
- epidemic spreading  
- brain networks
- neuronal activity
- tau propagation
- pathological protein transmission
- activity-dependent modeling
- multiscale brain networks