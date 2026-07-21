---
name: vlms-human-alignment-natural-reading
description: "Research methodology comparing LLM and VLM alignment with human brain responses during natural reading. Uses controlled text-only evaluation to isolate multimodal training effects. Based on arXiv:2605.28818 (May 2026). Use when studying VLM vs LLM alignment, human brain-model comparison, natural reading fMRI, eye-tracking alignment, or visual semantic content effects on language models."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.28818"
  published: "2026-05-27"
  authors: "Jinzhou Wu, Zhengwu Ma, Jixing Li, Baoping Tang, Zitong Lu"
  categories: [cs.CL, q-bio.NC]
  tags: [vlm-llm-alignment, human-brain-alignment, natural-reading, fMRI, eye-tracking, visual-semantic-content, language-modeling, multimodal-pretraining, brain-model-comparison]
---

# VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading

**Source:** arXiv:2605.28818 [cs.CL], published 2026-05-27  
**Authors:** Jinzhou Wu, Zhengwu Ma, Jixing Li, Baoping Tang, Zitong Lu

## Description

This skill provides the methodology and findings from a controlled study comparing tightly matched LLM and Vision-Language Model (VLM) pairs under text-only conditions to isolate the effect of multimodal training history on human brain alignment during natural reading. The study evaluates model alignment using whole-cortex fMRI responses and synchronized eye-tracking saccades from human natural-reading experiments. The key finding: multimodal pretraining does not confer a uniform, global advantage in human alignment, suggesting language-internal representations remain the key factor for modeling human text processing.

---

## 1. Research Question

Large language models (LLMs) have become useful computational models of human language processing. A key question emerges: **Does vision-language learning make text representations more human-like during natural reading?**

### 1.1 Prior Work Context

Previous studies found:
- LLM representations correlate with human fMRI responses during language tasks
- VLMs show stronger brain alignment in some vision-related tasks
- But these studies often confounded multimodal training history with online visual input

### 1.2 The Challenge

Disentangling **multimodal training history** (what the model learned during pretraining) from:
- Online visual input (visual stimuli presented during evaluation)
- Cross-modal fusion (architectural differences enabling visual processing)

---

## 2. Methodology

### 2.1 Controlled Comparison Design

**Key innovation:** Strict text-only evaluation setting to isolate training history effects.

| Component | Design |
|-----------|--------|
| Model pairs | Tightly matched LLM-VLM pairs (same architecture, different pretraining) |
| Input modality | Text-only (no visual input during evaluation) |
| Task | Natural reading (reading sentences passively) |
| Human data | fMRI + eye-tracking during natural reading |
| Alignment metrics | Brain response correlation (fMRI), eye-movement similarity |

### 2.2 Model Selection

**Tightly matched pairs** ensure architectural equivalence:
- Same transformer architecture
- Same parameter count
- Same training corpus (text-only vs. text+vision)
- Only difference: multimodal pretraining history

**Example pairs:**
- LLM baseline vs. its VLM extension (e.g., LLaMA vs. LLaVA)
- Text-only pretraining vs. text+image pretraining

### 2.3 Human Data

**Natural-reading dataset characteristics:**
- Whole-cortex fMRI responses during sentence reading
- Synchronized eye-tracking (saccade patterns, fixation durations)
- Naturalistic stimuli (not artificial sentence lists)

**Advantages over traditional paradigms:**
- Ecological validity (natural reading behavior)
- Multi-modal brain data (visual cortex + language network)
- Eye movements capture processing dynamics

---

## 3. Alignment Metrics

### 3.1 fMRI Alignment

**Method:** Representational Similarity Analysis (RSA)

1. Extract model representations for each sentence/word
2. Compute Representational Dissimilarity Matrix (RDM) for model
3. Compute RDM for human fMRI responses (voxel patterns)
4. Correlate model RDM with human RDM across regions

**Brain regions evaluated:**
- Visual cortex (V1-V4)
- Language network (inferior frontal gyrus, temporal cortex)
- Semantic regions (angular gyrus, middle temporal gyrus)
- Whole-cortex patterns

### 3.2 Eye-Tracking Alignment

**Metrics:**
- Saccade pattern similarity (sequence of eye movements)
- Fixation duration correlation
- Regression probability (backward eye movements)
- Landing position distributions

**Why eye-tracking?**
- Captures online processing dynamics
- Reflects comprehension difficulty
- Shows attention allocation
- Complements fMRI temporal resolution

---

## 4. Key Findings

### 4.1 Main Result: No Global VLM Advantage

**Primary finding:** Multimodal pretraining does NOT confer a uniform, global advantage in human alignment during natural reading.

| Metric | LLM vs. VLM | Interpretation |
|--------|-------------|----------------|
| Overall fMRI alignment | Comparable | Language-internal representations dominate |
| Language network alignment | Similar | VLM training history doesn't improve core language processing |
| Eye-movement similarity | Comparable | Processing dynamics unaffected by visual training history |

**Implication:** Language-internal representations remain the key factor for modeling human text processing, not multimodal pretraining.

### 4.2 Selective VLM Advantage: Visual Semantic Content

**Secondary finding:** VLM advantage emerges selectively when sentences contain stronger visual semantic content.

**Visual semantic content indicators:**
- Concrete nouns (object names, colors, shapes)
- Spatial descriptions (locations, layouts)
- Visual properties (brightness, texture)
- Scene descriptions

**Converging evidence from both modalities:**
- fMRI: Higher correlation in visual cortex for visually rich sentences
- Eye-tracking: Similar fixation patterns for visually semantic sentences

**Mechanism hypothesis:**
- Multimodal pretraining grounds abstract text representations in visual experience
- Visual grounding helps when text evokes mental imagery
- No advantage when text is purely abstract/language-specific

### 4.3 Regional Differences

| Brain region | LLM-VLM comparison | Visual semantic effect |
|--------------|--------------------|------------------------|
| Visual cortex (V1-V4) | VLM modestly better for visual content | Strong visual semantic advantage |
| Language network (IFG, temporal) | No difference | No visual semantic effect |
| Semantic regions (AG, MTG) | Mixed | Weak visual semantic effect |
| Whole cortex | No global difference | Regional selective effects |

---

## 5. Experimental Details

### 5.1 Sentence Selection

**Visual semantic content quantification:**
- Human ratings of "imagability" (how easily the sentence evokes a mental image)
- Word concreteness scores (concrete nouns = high visual content)
- Scene description frequency (location/object mentions)

**Controlled sentence categories:**
- High visual semantic: Scene descriptions, concrete objects
- Low visual semantic: Abstract concepts, theoretical statements
- Mixed: Balanced visual and abstract content

### 5.2 Text-Only Evaluation Protocol

**Strict text-only setting:**
- Models receive only text input (no images)
- VLMs evaluated without their vision encoder active
- Ensures only training history differs, not online architecture

**Why text-only?**
- Isolate training history effect
- Remove confound of cross-modal fusion during evaluation
- Test whether visual grounding improves language representations

---

## 6. Implications

### 6.1 For Brain-Model Alignment Research

**Methodological implications:**
1. **Controlled comparisons essential:** Tight architectural matching needed to isolate training effects
2. **Text-only evaluation informative:** Removes confounds of online multimodal processing
3. **Selective effects matter:** Global metrics may miss important regional/condition-specific differences

**Future directions:**
- Study other modalities (audio, sensorimotor) with controlled designs
- Investigate multimodal training dynamics (what visual features transfer to language?)
- Test other language tasks (comprehension, generation, dialogue)

### 6.2 For VLM Development

**Design implications:**
1. **Language core remains critical:** Improve language representations first, then add modality
2. **Visual grounding selective:** Expect advantages only for visually semantic content
3. **Domain-specific tuning:** Optimize visual grounding for specific applications (scene descriptions, embodied AI)

**Potential improvements:**
- Ground language representations in specific visual domains
- Balance abstract vs. visual semantic content in pretraining
- Design architectures that selectively activate visual grounding when beneficial

### 6.3 For Cognitive Neuroscience

**Theoretical implications:**
1. **Language modality independence:** Core language processing may be modality-independent
2. **Visual imagery role:** Visual semantic content triggers mental imagery, engaging visual cortex
3. **Brain region specialization:** Language network vs. visual cortex functional dissociation

**Hypothesis testing:**
- Does visual cortex activation during reading reflect mental imagery?
- Are abstract and concrete concepts processed differently?
- How does multimodal experience shape language representations in development?

---

## 7. Activation Keywords

- VLM vs LLM alignment, vision-language model brain alignment
- human brain model comparison, brain-model alignment
- natural reading fMRI, reading comprehension fMRI
- eye-tracking alignment, saccade pattern similarity
- visual semantic content, concreteness effect
- multimodal pretraining effects, visual grounding
- text-only evaluation, controlled comparison design
- representational similarity analysis RSA
- language network, visual cortex activation
- abstract vs concrete concepts, imagery-evoking sentences

---

## 8. Related Skills

- `vlm-visual-cortex-alignment-robustness`: VLM robustness through early visual cortex alignment — complementary finding
- `backpropagation-brain-hierarchy-misalignment`: Backpropagation gradient vs. brain hierarchy — related alignment methodology
- `brain-llm-alignment-training-data`: Brain-LLM alignment driven by training language — related training effect study
- `representation-steering`: LLM representation steering and activation patching — related technique for improving alignment

---

## References

- Wu, J., Ma, Z., Li, J., Tang, B., & Lu, Z. (2026). VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading. arXiv:2605.28818 [cs.CL].
- Schrimpf, M., et al. (2021). The neural architecture of language: Integrative modeling converges on current views of human language processing. Neuron.
- Wang, S., et al. (2022). On the utility of multimodal representations in language models. arXiv preprint.
- Kumar, S., et al. (2022). Brain-like representational organization emerges in deep neural networks trained for natural language processing. Nature Communications.

---

## Notes

- This study uses a controlled text-only evaluation setting, which is a methodological innovation for isolating training history effects
- The selective VLM advantage for visual semantic content suggests visual grounding is not uniformly beneficial
- The study uses both fMRI (spatial resolution) and eye-tracking (temporal resolution) for converging evidence
- Tightly matched LLM-VLM pairs are essential — architectural differences could confound results
- The findings challenge assumptions that multimodal pretraining universally improves language model alignment with human brains

*Last updated: 2026-05-29*