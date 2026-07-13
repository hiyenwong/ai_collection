---
name: neural-code-language-interpretability
description: "Natural language hypothesis generation and verification for single-neuron selectivity. Combines vision-language models, neural digital twins, and text-to-image generation to automatically characterize what individual neurons encode across the visual hierarchy. Use for neuron interpretability, automated neuroscience discovery, digital twin validation, language-based neural characterization, closed-loop hypothesis testing."
---

# Neural Code Language Interpretability (NCLI)

Automated characterization of single-neuron selectivity through natural language, combining digital twins, vision-language models, and generative testing in a closed-loop framework.

**Paper**: "Letting the Neural Code Speak: Automated Characterization of Monkey Visual Neurons through Human Language"
**Authors**: Vedang Lad, Katrin Franke, Tamar Rott Shaham, Surya Ganguli, Andreas S. Tolias, Sophia Sanborn, Nikos Karantzas
**arXiv**: [2605.12485](https://arxiv.org/abs/2605.12485) (May 12, 2026)

## Core Insight

Natural language can serve as a compact, interpretable coordinate system for neural selectivity — replacing mathematical models (like Gabor functions in V1) with semantic descriptions that generalize across the visual hierarchy.

## Three-Stage Framework

### Stage 1: Translate (Image → Text)

Convert images into detailed, reconstruction-faithful captions:
- **Input**: Natural images (grayscale for V1, RGB for V4)
- **Model**: Gemini 3.0 Pro (dense captioning)
- **Key instruction**: Prioritize visually grounded details sufficient for reconstruction (colors, textures, spatial relations, lighting) — NOT semantic summarization
- **Validation**: Regenerate images from captions using text-to-image model (Imagen 4.0), measure cosine similarity in DINOv3 embedding space
- **Quality check**: Matched reconstruction similarity >> random pairing similarity

### Stage 2: Semantic Hypothesis (Text → Hypothesis)

Distill extreme responses into concise, testable descriptions:
- Use functional digital twin (neuron-specific readout on pretrained CNN backbone) to screen ~1.2M ImageNet images
- Identify **Most Activating Images (MAIs)** and **Least Activating Images (LAIs)** for each neuron
- Select top/bottom 15 images per neuron
- Feed their dense captions to LLM to produce:
  - **Excitatory hypothesis**: What features drive the neuron
  - **Suppressive hypothesis**: What features suppress the neuron (only for non-sparse neurons with baseline activity)
  - Dimensions of invariance
  - Spatial properties (orientation, scale)
- **Sparsity threshold**: Neurons with response distribution skewness < 2 are "non-sparse" (suppressible)
- Results span visual hierarchy: V1 = oriented edges, spatial frequency; V4 = conjunctions of form, color, texture

### Stage 3: Verification (Hypothesis → Image → Response)

Closed-loop generative testing:
1. LLM expands hypothesis into multiple diverse text prompts
2. Text-to-image model synthesizes novel stimuli from prompts
3. Digital twin predicts neural responses to generated images
4. **Spatial optimization**: Affine transformations (rotation, scale, translation) to find best receptive field alignment
5. **Control**: Same spatial optimization on random images (controls for spatial-only effects)

**Success criterion**: Generated images drive neuron to extreme percentiles of natural image response distribution

## Key Results

| Metric | V1 | V4 |
|--------|-----|-----|
| Activating hypothesis success rate (>95th percentile) | >96% | >96% |
| Suppressing hypothesis success rate (<5th percentile) | 56% | 97.6% |
| Random image baseline | ~10% | ~10% |

- V4 suppression is highly describable in language (97.6%), V1 suppression is not (56%)
- Suggests linguistic expressibility limits for sub-lexical properties in early visual cortex
- Representation Similarity Analysis (RSA) shows partial alignment between: neural activity ↔ DINOv3 visual embeddings ↔ Qwen 0.6B language embeddings
- Vision embeddings most aligned with neural activity
- Information lost in text bottleneck is recovered when hypotheses are rendered back to images → linguistic compression is lossy but semantically faithful

## Implementation Details

### Digital Twin Architecture
- Neuron-specific readout layers on top of pretrained CNN backbone
- Trained on single-neuron spiking data from natural image fixation experiments
- Predicts responses with high accuracy → enables in-silico screening at scale

### Image Dataset
- 1.2 million ImageNet images
- V1: grayscale stimuli (experimental protocol)
- V4: full-color stimuli
- Screened through digital twin to identify extreme-response sets

### Language Models Used
- **Captioning**: Gemini 3.0 Pro
- **Hypothesis generation**: Gemini 3.0 Pro (single-pass, no iterative refinement against neural data)
- **Text-to-image**: Imagen 4.0
- **Language embeddings for RSA**: Qwen 0.6B

### Spatial Optimization
- Systematic search over: rotation, scale, translation
- Two-stage: semantic generation → spatial optimization
- Separates contribution of feature content from spatial arrangement

## Applications

### For Neuroscience Research
- Automated neuron characterization at scale (438 V1 + 205 V4 neurons demonstrated)
- Hypothesis generation for higher visual areas where no mathematical framework exists
- Population-level analysis of neural code geometry across modalities
- Bridging predictive accuracy and mechanistic understanding

### For AI Interpretability
- Extends to artificial neural networks (CNNs, ViTs)
- Closed-loop validation distinguishes from correlational methods
- Language as a universal coordinate system for unit selectivity

### For Agentic Scientific Discovery
- Framework enables autonomous hypothesis generation and testing
- Combines generative models with neural digital twins
- Moves toward automated, interpretable neuroscience

## Limitations

1. **Single-pass hypothesis generation**: Not iteratively refined against neural responses
2. **Language expressibility limits**: V1 suppression poorly captured (56% vs 97.6% in V4)
3. **Weaker criterion than equivalence**: Success means extreme tail activation, not full equivalence to original MAIs/LAIs
4. **Spatial positioning**: Vision-language models unreliable at specifying feature location/scale/orientation in receptive field
5. **Requires high-quality digital twin**: Prediction accuracy is prerequisite
6. **Preprint status**: Not yet peer-reviewed

## Related Methods

- Network Dissection (Bau et al., 2017): Manual concept labeling
- CLIP-based neuron labeling: Correlational, not closed-loop
- Activation maximization: Pixel-space, not interpretable
- LLM-based LLM unit description (Bills et al., 2023): For language model internals
- Agentically-driven hypothesis generation (Rott Shaham et al., 2024): Extended here to biological neurons

## Activation Keywords

- neural code interpretability
- neuron characterization
- digital twin neuroscience
- language-based neural analysis
- closed-loop hypothesis testing
- automated neuroscience
- semantic hypothesis generation
- visual cortex neuron selectivity
- V1 V4 neuron encoding
- neural digital twin
- language-brain alignment
- representation similarity analysis
