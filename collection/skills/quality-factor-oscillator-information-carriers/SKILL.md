---
name: quality-factor-oscillator-information-carriers
description: "Quality-factor screen for biological oscillator carriers."
metadata:
  arxiv_id: "2608.10560"
  published: "2026-08-12"
  authors: "Eran Kopel"
  tags: [biological oscillators, information carriers, quality factor, neural rhythms, spectral distinguishability, coherence time]
license: Complete terms in LICENSE.txt
---

# Quality-Factor Screen for Biological Oscillator Information Carriers

## Overview

This methodology provides a universal framework for evaluating how many distinguishable labels a biological oscillator can carry as an information carrier. The core insight is that **spectral distinguishability alone bounds the number of labels by the quality factor**: 

**M ≤ Q = 2πντ**

Where:
- M = number of distinguishable labels
- Q = quality factor  
- ν = frequency (Hz)
- τ = coherence time (seconds)

This relationship follows from the fundamental connection between linewidth and coherence time, making it independent of substrate, mechanism, or position on quantum effects in biology.

## Key Principles

### 1. Universal Quality Factor Bound
The quality factor Q provides a substrate-independent upper bound on information capacity. This allows fair comparison across diverse proposed carriers:
- Collective vibrational modes
- Endogenous electromagnetic fields  
- Microtubule excitations
- Oscillatory phase codes

### 2. Spectral Distinguishability Criterion
A carrier must have sufficient spectral resolution to distinguish between different labels. The linewidth (Δν) must be narrow enough relative to the carrier frequency:

**Q = ν/Δν = 2πντ**

Low Q values indicate poor spectral distinguishability.

### 3. Metabolic Power Constraint
Independent metabolic power bounds must also be satisfied. High-frequency carriers often exceed feasible metabolic power by 5-9 orders of magnitude.

### 4. Two-Sided Persistence Window
Valid information carriers must satisfy both:
- **Readable**: Labels can be detected/received
- **Rewritable**: Labels can be modified/updated

## Application Workflow

### Step 1: Calculate Quality Factor
For any proposed oscillator, determine:
1. Carrier frequency (ν) - from experimental measurements or theoretical models
2. Coherence time (τ) - from linewidth measurements or decay constants
3. Compute Q = 2πντ

### Step 2: Apply Spectral Screening
- **Q ≥ 1**: Potentially viable carrier (can distinguish at least 1 label from baseline)
- **Q < 1**: Fundamentally limited (linewidth exceeds carrier frequency)

*Example from paper*: 30 GHz intracolumnar microwave field → Q = 0.19 (fails screening)

### Step 3: Check Metabolic Feasibility
Calculate required metabolic power and compare to biological constraints:
- Neuronal ATP consumption rates
- Mitochondrial energy production limits
- Tissue-specific metabolic budgets

### Step 4: Validate Persistence Window
Ensure the carrier supports both reading and writing operations within biological timescales.

### Step 5: Comprehensive Screening
Apply all six criteria from the original framework:
1. Spectral distinguishability (Q factor)
2. Metabolic power feasibility  
3. Readability (detection possible)
4. Rewritability (modification possible)
5. Geometric compatibility (no forbidden cavity requirements)
6. Temporal persistence (sufficient coherence for processing)

## Practical Implementation

### Reference Implementation
The paper provides a reference implementation and verification suite:
- DOI: https://doi.org/10.5281/zenodo.21837368
- Extends: https://doi.org/10.5281/zenodo.21837082

### Screening Results
When applied to eleven proposed carriers, only **low-frequency neural rhythms** pass all criteria. High-frequency molecular carriers fail due to brevity (short coherence times), not fragility as previously assumed.

## Use Cases

### When to Apply This Framework
- Evaluating new proposals for neural information carriers
- Comparing competing theories of brain information processing  
- Assessing feasibility of quantum biological mechanisms
- Designing experiments to test information carrier hypotheses
- Reviewing literature on neural coding schemes

### Activation Keywords
- quality factor biological oscillators
- information carrier screening
- spectral distinguishability neuroscience  
- coherence time neural rhythms
- oscillator information capacity
- biological information processing limits

## Pitfalls and Limitations

### Common Misconceptions
1. **Fragility vs. Brevity**: High-frequency carriers fail due to short coherence times (brevity), not environmental fragility
2. **Cavity Requirements**: Driven emitters require resonant cavities for narrow linewidths, but many proposed geometries forbid them
3. **Metabolic Overestimation**: Power requirements are often underestimated by orders of magnitude

### Implementation Challenges
- Accurate coherence time measurement in biological systems
- Distinguishing intrinsic vs. extrinsic decoherence sources  
- Accounting for collective vs. individual oscillator behavior
- Handling non-stationary biological environments

## References

- Original Paper: [arXiv:2608.10560](https://arxiv.org/abs/2608.10560)
- Reference Implementation: https://doi.org/10.5281/zenodo.21837368
- Extended Framework: https://doi.org/10.5281/zenodo.21837082

## Verification

To validate this methodology:
1. Reproduce the Q = 0.19 calculation for 30 GHz microwave field
2. Apply the framework to known neural rhythm frequencies (delta, theta, alpha, beta, gamma)
3. Verify metabolic power calculations for high-frequency proposals
4. Test the two-sided persistence window requirement on candidate carriers