---
name: when-to-smell-in-stereo
description: "Stereo olfaction utility analysis framework - determines when dual nostril 'stereo' olfaction provides advantages over single nostril 'mono' olfaction based on odor concentration gradients and spatial correlation length scales. Use when analyzing animal olfactory navigation, odor trail tracking, or surface-based olfactory search strategies."
metadata:
  arxiv_id: "2607.20307"
  published: "2026-07-22"
  authors: "Sina Tootoonian, Andreas T. Schaefer"
  tags: [neuroscience, olfaction, stereo sensing, animal behavior, boundary layer]
license: Complete terms in LICENSE.txt
---

# When to Smell in Stereo

## Overview

This skill provides the theoretical framework from Tootoonian & Schaefer (2026) for determining when stereo olfaction (dual nostril sensing) provides advantages over mono olfaction (single nostril sensing) in animals.

The key insight is that stereo olfaction is advantageous under specific environmental conditions related to odor concentration gradients and spatial correlation structures in airflow.

## Core Principles

### When Stereo Olfaction is Advantageous

1. **Large relative changes in odor concentration**: When there are significant concentration differences between the two nostrils
2. **Large spatial length scales of correlations in air**: Particularly in boundary layers near surfaces where airflow is more structured
3. **Surface-based olfactory edge detection**: When animals are searching surfaces for odor trails or boundaries

### Mathematical Framework

The paper uses "back of the envelope" calculations to compare signal-to-noise ratios and information gain between stereo and mono olfaction strategies under different environmental conditions.

Key parameters include:
- Odor concentration gradient magnitude
- Spatial correlation length scale of turbulence
- Distance from surface (boundary layer effects)
- Nostril separation distance

## Applications

- **Animal behavior analysis**: Understanding when animals switch between stereo/mono olfaction strategies
- **Robotics**: Designing bio-inspired olfactory sensors for autonomous robots
- **Neuroscience**: Studying neural processing of bilateral olfactory inputs
- **Ecology**: Modeling odor-guided navigation in natural environments

## Methodology

### Analysis Steps

1. **Characterize the environment**: Determine odor concentration gradients and spatial correlation structure
2. **Assess boundary layer proximity**: Evaluate if the animal/robot is operating near surfaces
3. **Calculate expected concentration differences**: Estimate the differential signal between nostrils
4. **Compare information gain**: Determine if stereo sensing provides sufficient advantage to justify the neural processing cost

### Key Equations

The framework provides simple analytical expressions for:
- Expected concentration difference: ΔC ≈ (∂C/∂x) × d (where d is nostril separation)
- Signal-to-noise ratio improvement in stereo vs mono configurations
- Critical correlation length scale threshold for stereo advantage

## Pitfalls and Limitations

- **Assumes steady-state conditions**: May not apply to highly dynamic turbulent environments
- **Simplified geometry**: Real animal head geometries may affect results
- **Species-specific factors**: Neural processing capabilities vary across species
- **Behavioral context**: Animals may use stereo olfaction for reasons beyond pure information gain

## References

- **Primary Paper**: Tootoonian, S., & Schaefer, A. T. (2026). "When to Smell in Stereo." arXiv:2607.20307 [q-bio.NC]
- **Related Work**: Studies on stereo olfaction in moths, mice, and other mammals
- **Applications**: Bio-inspired robotics and sensor design literature

## Activation Keywords

- stereo olfaction
- dual nostril sensing  
- odor trail tracking
- olfactory navigation
- boundary layer olfaction
- when to smell in stereo
- arXiv:2607.20307