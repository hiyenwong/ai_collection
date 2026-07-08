---
name: "EEG Cortical Speech Tracking for Subjective Cognitive Decline"
description: "Research methodology and findings on using EEG cortical tracking strength (CTS) as a neural marker for early-stage cognitive decline. Combines speech encoding models with linguistic feature analysis to detect subjective cognitive decline (SCD). Use when: studying EEG speech processing, cognitive decline biomarkers, neural tracking of naturalistic speech, or linguistic feature encoding in aging populations."
metadata:
  arxiv_id: "2509.21277"
  published: "2025-09-25"
  authors: "Matthew King-Hang Ma, Yun Feng, Cloris Pui-Hang Li, Manson Cheuk-Man Fong"
  keywords: ["EEG", "cortical speech tracking", "subjective cognitive decline", "dementia risk", "speech encoding model", "linguistic features"]
  category: "q-bio.NC"
---

# EEG Cortical Speech Tracking for Subjective Cognitive Decline (SCD)

## Overview

This skill documents the methodology and key findings from arXiv:2509.21277, which investigates how self-perceived cognitive worsening shapes neural dynamics during naturalistic speech perception, and identifies cortical tracking strength (CTS) as a potential neural marker for early-stage cognitive decline.

## Background

**Subjective Cognitive Decline (SCD)** doubles dementia risk. This study explores how self-perceived cognitive decline affects neural processing of naturalistic speech with varying prosodic contexts.

## Methodology

### Experimental Design
- **Participants**: 60 cognitively normal older adults
- **Stimuli**: Speech samples with four expressive styles:
  - Scrambled (low-level acoustic)
  - Descriptive (prosodically flat)
  - Dialogue (natural conversational)
  - Exciting (high prosodic variation)

### Speech Encoding Models
Three speech representation layers mapped to EEG:
1. **Acoustic features** (low-level)
2. **Subsyllabic segmentation** (linguistic unit boundaries)
3. **Phonotactic features** (probability of sound sequences)

### Analysis
- **Cortical Tracking Strength (CTS)**: Correlation between speech features and EEG signals
- **Comparison**: Linguistic vs. acoustic feature tracking
- **Correlation**: CTS with SCD severity scores

## Key Findings

### 1. Linguistic Features Outperform Acoustic
Subsyllabic linguistic feature models showed stronger CTS than acoustic models across all participants.

### 2. SCD-Related Neural Markers
Greater SCD severity associated with weaker CTS for:
- **Subsyllabic linguistic features** (but NOT acoustic features)
- **Prosodically flat speech** (scrambled and descriptive styles)

### 3. Specificity of Impairment
- Linguistic processing impaired in SCD
- Basic acoustic processing preserved
- Prosodic variation modulates the effect

## Implications

### Clinical Biomarker
**CTS of higher-level linguistic features during prosodically flat speech** may serve as an early neural marker for cognitive decline before clinical symptoms emerge.

### Theoretical Insights
- Linguistic (not acoustic) processing vulnerable in early cognitive decline
- Prosodic context can compensate or exacerbate processing deficits
- Natural speech paradigms reveal subtle neural changes

## Methodology Applications

### When to Apply
- Studying early dementia biomarkers
- Investigating speech processing in aging
- Developing neural markers for cognitive screening
- Analyzing naturalistic speech perception

### Key Technical Components
1. **Encoding models**: Map speech features → EEG
2. **Linguistic feature extraction**: Subsyllabic segmentation
3. **Prosodic manipulation**: Control speech expressiveness
4. **CTS computation**: Cross-correlation with lag optimization

### Experimental Considerations
- Use naturalistic speech (not isolated syllables)
- Include multiple prosodic conditions
- Control for hearing ability and attention
- Account for linguistic background

## Related Research Areas

- EEG speech tracking
- Cognitive decline biomarkers
- Naturalistic neuroscience
- Linguistic processing in aging
- Neural encoding models

## Limitations and Future Directions

### Current Limitations
- Cross-sectional design (causality unclear)
- Cognitive normal participants (clinical validation needed)
- Single language (Mandarin Chinese)

### Future Work
- Longitudinal studies tracking CTS changes
- Clinical populations (MCI, dementia)
- Multi-language validation
- Integration with other biomarkers (MRI, CSF)

## Citation

```
Ma, M. K.-H., Feng, Y., Li, C. P.-H., & Fong, M. C.-M. (2025). More than a feeling: 
Expressive style influences cortical speech tracking in subjective cognitive decline. 
arXiv preprint arXiv:2509.21277.
```

## Keywords for Activation

EEG, cortical speech tracking, subjective cognitive decline, SCD, dementia biomarker, speech encoding model, linguistic features, prosody, naturalistic speech, neural tracking, cognitive aging
