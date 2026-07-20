---
name: brain-llm-alignment-training-data
description: "Brain-LLM alignment is driven by training-language dominance, not an inherent property of English. Tests with fMRI from 112 participants across English, Chinese, French and 7 LLMs (English-dominant, Chinese-dominant, multilingual). Baichuan2-7B reverses alignment gradient entirely; typological distance independently affects alignment degradation in syntax regions (IFG). Accepted at CoNLL 2026. Activation: brain-LLM alignment, cross-linguistic brain encoding, training data dominance, multilingual fMRI, typological alignment."
arxiv_id: "2605.23032"
published: "2026-05-21"
authors: "Dongxin Guo, Jikun Wu, Siu Ming Yiu"
tags: [brain-llm-alignment, cross-linguistic, fmri, neurolinguistics, training-data-dominance, computational-neuroscience]
---

# Brain-LLM Alignment Tracks Training Data, Not Typology

> This paper shows that the apparent "English advantage" in brain-LLM alignment is an artifact of training data composition. Using fMRI from 112 participants across three languages (English, Chinese, French) and 7 LLMs, it demonstrates that training-language dominance, not English per se, drives alignment patterns.

**Source**: arXiv: [2605.23032](https://arxiv.org/abs/2605.23032) | Accepted at CoNLL 2026

## Core Methodology

### Key Innovation
Brain-LLM alignment is well-established in English, but the brain's language network is neuroanatomically universal. This paper asks: does alignment generalize cross-linguistically, and what governs the variation? It provides the first systematic cross-linguistic test of brain-LLM alignment.

### Technical Framework

1. **fMRI Dataset**: Le Petit Prince corpus with 112 participants across English, Chinese, and French
2. **LLM Suite**: 7 models spanning English-dominant (LLaMA-2-7B, GPT-2 XL), Chinese-dominant (Baichuan2-7B), and multilingual (mT5, BLOOM, XLM-R) architectures
3. **Encoding Model**: Ridge regression encoding models predicting fMRI responses from LLM layer activations
4. **Training-Language Dominance Analysis**: Compare alignment gradients between architecture-matched English-dominant (LLaMA-2-7B) and Chinese-dominant (Baichuan2-7B) models
5. **Typological Distance Analysis**: Quantify how formal typological distance between languages independently affects alignment degradation
6. **Brain Region Analysis**: Decompose alignment by brain regions — syntax-associated IFG vs. lexico-semantic PTL
7. **Tokenization Analysis**: Measure how tokenization fertility (tokens per word) affects cross-linguistic optimal encoding layer shifts

### Key Results

- **Training-language dominance drives alignment**: Baichuan2-7B (Chinese-dominant, architecture-matched to LLaMA-2-7B) reverses the alignment gradient entirely — aligns best with Chinese brains and worst with English
- **Typological distance independently covaries** with alignment degradation across all models
- **Syntax regions (IFG) show** steeper typological gradients than lexico-semantic regions (PTL)
- **Tokenization fertility** accounts for ~60% of the cross-linguistic shift in optimal encoding layer
- **The "English advantage"** is an artifact of training data composition, not an inherent property of the English language

## Applications

- **Cross-linguistic neuroscience**: Study how language processing in the brain depends on model training vs. inherent language structure
- **LLM evaluation for brain alignment**: Evaluate which models are best for predicting brain responses across different languages
- **Neurolinguistic theory**: Understand the interplay between training data, typology, and neural language processing
- **Multilingual model design**: Inform multilingual model development by understanding how training data composition affects brain-relevant representations

## Related Skills

- sparse-autoencoder-brain-llm-topography
- brain-llm-key-neurons-grammar
- fcn-llm-brain-network-understanding
- computational-linguistics-brain-perspective
