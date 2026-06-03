---
name: llm-brain-alignment-creative-thinking
description: >
  Research skill based on the paper "Large Language Models Align with the Human Brain
  during Creative Thinking" (arXiv:2604.03480). Covers LLM-brain representational
  alignment during divergent thinking using fMRI, default mode network (DMN) involvement,
  executive control regions, layer-wise alignment patterns, and scaling properties.
  Activation keywords: creative thinking, LLM-brain alignment, fMRI, divergent thinking,
  DMN, default mode network, executive control, representational similarity analysis,
  RSA, model scaling, neural alignment, cognitive neuroscience, AI-brain comparison.
---

# LLMs Align with Human Brain during Creative Thinking

**Paper:** Large Language Models Align with the Human Brain during Creative Thinking
**Authors:** Mete Ismayilzada, Simone A. Luchini, Abdulkadir Gokce, Badr AlKhamissi et al.
**Published:** 2026-04-03
**arXiv:** [2604.03480](https://arxiv.org/abs/2604.03480)
**Categories:** q-bio.NC, cs.AI, cs.CL

---

## Summary

This paper investigates whether and how internal representations of large language models (LLMs) align with human neural activity measured via fMRI during creative (divergent) thinking tasks. It represents a pioneering effort to bridge computational AI creativity research with cognitive neuroscience, using representational similarity analysis (RSA) to systematically compare LLM hidden-layer activations with brain responses.

---

## Research Methodology

### Paradigm
- Participants underwent **fMRI scanning** while performing **divergent thinking tasks** (e.g., alternate uses task, creative story generation) and **analytical/control thinking tasks**.
- Brain activity was recorded during both **idea generation** and **idea elaboration** phases.

### LLM Representation Extraction
- Multiple LLMs of varying sizes and architectures were used to process the same stimuli presented to human participants.
- **Hidden-layer activations** were extracted for each token/stimulus across all layers of each model.

### Representational Similarity Analysis (RSA)
- Representational Dissimilarity Matrices (RDMs) were constructed from:
  - **Brain data:** fMRI voxel patterns across conditions within regions of interest (ROIs).
  - **LLM data:** Activation patterns across layers for each stimulus.
- RSA compared the structure of LLM RDMs with brain RDMs to quantify alignment.
- Alignment was assessed **layer-wise** (across model depth) and **region-wise** (across brain areas).

---

## Key Findings

### 1. Significant LLM-Brain Alignment During Creative Thinking
- LLM internal representations, particularly in **middle-to-upper layers**, significantly correlate with human brain activity during creative idea generation.
- This alignment is not uniform across the brain — it is concentrated in specific functional networks.

### 2. Stronger Alignment for Creative vs. Analytical Thinking
- Alignment between LLMs and the brain is **significantly stronger for divergent/creative thinking** tasks compared to analytical/convergent thinking tasks.
- This suggests LLMs capture something specific about the neural representations underlying creative cognition, beyond general language processing.

### 3. Scaling Properties
- **Alignment scales with model size:** Larger LLMs show stronger brain alignment during creative thinking.
- This scaling effect mirrors findings in language-only tasks (e.g., Caucheteux & King, 2022) but is specifically amplified for creative contexts.
- The relationship between model scale and brain alignment suggests that as LLMs improve in creative task performance, their internal representations become more brain-like.

### 4. Layer-Wise Alignment Profile
- Lower layers (primarily syntactic/lexical processing) show moderate alignment with sensory and language regions.
- **Middle-to-upper layers** show the strongest alignment with higher-order cognitive regions involved in creative thinking.
- This is consistent with a hierarchical processing interpretation where deeper layers capture more abstract, conceptual representations.

---

## Brain Regions Involved

### Default Mode Network (DMN)
- **Core finding:** Strong LLM-brain alignment in DMN regions during creative thinking.
- Key DMN subregions showing alignment:
  - **Medial Prefrontal Cortex (mPFC):** Involved in self-referential and imaginative processing.
  - **Posterior Cingulate Cortex (PCC):** Involved in internally-directed cognition and memory retrieval.
  - **Angular Gyrus:** Associated with semantic integration and creative idea combination.
- The DMN is reliably engaged during divergent thinking and creative cognition, and LLM representations capture this engagement pattern.

### Executive Control Network
- Alignment also observed in executive control regions:
  - **Dorsolateral Prefrontal Cortex (dlPFC):** Cognitive control, working memory, and idea evaluation.
  - **Anterior Cingulate Cortex (ACC):** Conflict monitoring and cognitive flexibility.
- These regions are thought to guide and constrain the creative search process, and their alignment with LLMs suggests models may implicitly represent similar control processes.

### Language Network
- Moderate alignment in classical language areas (left inferior frontal gyrus, superior temporal gyrus) — expected given the language-based nature of both tasks and models.

---

## Implications

1. **For Cognitive Neuroscience:** LLMs can serve as computational models for studying the neural basis of creativity, offering a novel tool for generating and testing hypotheses about creative cognition.

2. **For AI Research:** Brain alignment during creative tasks may serve as an additional metric for evaluating the sophistication and human-likeness of AI-generated creative output.

3. **For Understanding Creativity:** The finding that alignment scales with model size and is stronger for creative tasks supports the view that creativity involves specialized neural computations that emerge in more capable language models.

4. **Brain-Inspired AI:** Understanding which brain regions and networks align with LLM representations could inform the design of architectures better suited for creative tasks.

---

## Methodological Details

| Aspect | Details |
|--------|---------|
| **Imaging** | fMRI (functional magnetic resonance imaging) |
| **Analysis Method** | Representational Similarity Analysis (RSA) |
| **LLM Layers Analyzed** | All layers, with focus on middle-to-upper layers |
| **Task Types** | Divergent thinking (creative) vs. convergent/analytical thinking |
| **Brain Networks** | DMN, Executive Control Network, Language Network |
| **Scaling Test** | Multiple model sizes compared |

---

## Related Concepts & Search Terms

- Divergent thinking, convergent thinking, alternate uses task (AUT)
- Representational Similarity Analysis (RSA), brain encoding models
- Default Mode Network (DMN), executive control network, salience network
- LLM layer analysis, model scaling laws, brain-like representations
- Creative cognition, associative thinking, remote associations
- NeuroAI, cognitive computational neuroscience, model-brain alignment
- fMRI, voxel-wise analysis, regions of interest (ROI)

---

## Citation

```bibtex
@article{ismayilzada2026llm,
  title={Large Language Models Align with the Human Brain during Creative Thinking},
  author={Ismayilzada, Mete and Luchini, Simone A. and Gokce, Abdulkadir and AlKhamissi, Badr and others},
  journal={arXiv preprint arXiv:2604.03480},
  year={2026}
}
```
