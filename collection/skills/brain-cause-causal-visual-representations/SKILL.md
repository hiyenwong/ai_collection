---
name: brain-cause-causal-visual-representations
description: "BrainCause methodology for discovering and causally validating visual representations in the human brain using generative models, counterfactual stimulus synthesis, and fMRI encoding models. Use when: (1) studying causal vs correlational brain representations, (2) designing controlled fMRI experiments with counterfactual stimuli, (3) validating whether brain regions truly represent specific visual concepts beyond activation-based localization, or (4) applying generative AI to neuroscience brain mapping."
arxiv_id: "2605.23895"
published: "2026-05-22"
authors: "Yuval Golbari, Navve Wasserman, Matias Cosarinsky, Roman Beliy, Aude Oliva, Antonio Torralba, Michal Irani, Tamar Rott Shaham"
tags: [causal-representation, fmri-encoding, generative-models, counterfactual-stimuli, brain-mapping, visual-neuroscience, functional-localization]
---

# BrainCause: Causal Visual Representation Discovery in the Human Brain

## Core Concept

BrainCause is an automated framework that combines **generative image models** with **image-to-fMRI encoding models** to synthesize controlled stimuli and validate neural representations through **targeted causal testing**. It moves beyond traditional activation-based functional localization to establish whether brain regions genuinely **represent** visual concepts rather than merely responding to correlated cues.

## Key Insights

1. **Activation ≠ Representation**: Strong activation alone does not establish that a brain region represents a concept — responses may be driven by correlated visual or semantic cues. Without causal validation, a large fraction of functional localizations would be false positives.

2. **Counterfactual Causal Testing**: BrainCause constructs three types of controlled stimuli:
   - **Concept images**: Strong exemplars of the target concept
   - **Counterfactual edits**: Images where the target concept is removed while preserving other content
   - **Correlated distractor images**: Images with candidate confounds that correlate with the target concept

3. **Image-to-fMRI Encoding**: Uses a predictive encoding model to estimate brain responses to synthetic stimuli, enabling large-scale causal testing without requiring new fMRI scans for every hypothesis.

4. **Automated Experiment Proposal**: Returns validated candidate representations and proposes follow-up fMRI experiments for further testing.

## Methodology

### Stimulus Construction Pipeline
1. Define target visual concept (e.g., "faces", "places", "body parts")
2. Generate concept exemplars using generative models
3. Create counterfactual versions that remove the target concept
4. Generate correlated distractor stimuli

### Validation Procedure
1. Feed synthetic stimuli through image-to-fMRI encoding model
2. Search for voxels/regions responding specifically to target concept
3. Control for correlated alternatives via comparison conditions
4. Return validated candidate representations

### Recovery Validation
- Successfully recovers **known functional localizations** (e.g., FFA for faces, PPA for places)
- Identifies **new candidate representations** across dozens of concepts
- Validated on both **predicted fMRI** (via encoding model) and **measured fMRI** data

## Applications

- **Neuroscience**: Mapping the causal basis of visual concept representations in human cortex
- **fMRI experiment design**: Generating hypothesis-driven stimulus sets for targeted validation
- **Brain-AI alignment**: Understanding which features drive neural responses vs. truly encoded representations
- **Cognitive neuroscience**: Disentangling correlated visual/semantic confounds from genuine concept selectivity

## Activation Keywords
- brain-cause, causal-representation, counterfactual-fmri, functional-localization, activation-vs-representation, generative-fmri, brain-encoding, visual-concept-validation, stimulus-synthesis, fmri-experiment-design
