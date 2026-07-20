---
name: brain-cliplm-semantic-compression-eeg
description: "Brain-CLIPLM semantic compression framework for EEG-to-text decoding. Two-stage methodology: semantic anchor recovery via contrastive learning + anchor-guided sentence reconstruction with retrieval-grounded LLM. Key principle: granularity matching - aligns decoding complexity with recoverable neural information scale. Use when: (1) EEG language decoding tasks, (2) brain-to-text translation, (3) neural signal semantic extraction, (4) cognitive state reconstruction from EEG, (5) sentence-level EEG decoding benchmarks (ZuCo), (6) semantic anchor-based neural decoding. Activation: EEG decoding, brain-to-text, semantic compression, neural anchor recovery, CLIP alignment, retrieval-grounded LLM, granularity matching, ZuCo benchmark."
metadata:
  arxiv_id: "2604.16370"
  published: "2026-04"
  authors: "Xiaoli Yang, Huiyuan Tian, Yurui Li, Jianyu Zhang, Shijian Li, Gang Pan"
  tags: [neuroscience, EEG, brain-decoding, semantic-compression, contrastive-learning, retrieval-grounded, LLM, granularity-matching, ZuCo]
license: Complete terms in LICENSE.txt
---

# Brain-CLIPLM: Semantic Compression for EEG-to-Text Decoding

## Overview

Brain-CLIPLM introduces a **semantic compression hypothesis** for EEG-to-text decoding: non-invasive EEG preserves recoverable **semantic anchors** rather than full lexical-syntactic sentence form. This framework decomposes EEG decoding into two stages, addressing the granularity mismatch between neural information scale and sentence complexity.

## Semantic Compression Hypothesis

### Core Principle: Granularity Matching

EEG signals (low SNR, ~100Hz, limited bandwidth) cannot directly encode full sentence structure. Instead, they preserve:
- **Semantic anchors** - ordered keyword-level evidence
- **Conceptual gist** - abstract meaning representation
- **Sentence-specific patterns** - distinguishable from language-model priors

**Key insight**: Direct sentence reconstruction is overly fine-grained relative to recoverable neural information. Decoding complexity must align with neural information scale.

### Two-Stage Decomposition

1. **Stage 1: Semantic Anchor Recovery**
   - Contrastive learning aligns word-level EEG evidence with fixed keyword vocabulary
   - Recover ordered semantic anchors (keywords representing sentence core meaning)
   - Granularity: word-level (~5-10 anchors per sentence)

2. **Stage 2: Anchor-Guided Sentence Reconstruction**
   - Retrieval-grounded LLM reconstructs sentence from anchors
   - Chain-of-thought reasoning prompts guide reconstruction
   - Preserves semantic fidelity while filling lexical-syntactic gaps

## Methodology

### Stage 1: Semantic Anchor Recovery

#### EEG Evidence Extraction

```python
# Extract EEG features for each word stimulus
eeg_features = extract_eeg_epochs(raw_eeg, word_timestamps)

# Apply contrastive learning
# Align EEG embeddings with keyword vocabulary embeddings
anchor_candidates = contrastive_alignment(
    eeg_features=eeg_features,
    vocabulary=vocabulary_embeddings,  # Fixed keyword vocab
    top_k=5  # Top-5 anchor candidates per position
)
```

#### Contrastive Alignment

- **Objective**: Maximize similarity between EEG evidence and correct keyword
- **Loss**: InfoNCE contrastive loss
- **Vocabulary**: Fixed set of keywords (domain-specific or general)
- **Output**: Ordered list of anchor candidates with confidence scores

#### Anchor Selection

```python
# Select anchors based on confidence and semantic coherence
selected_anchors = select_anchors(
    candidates=anchor_candidates,
    confidence_threshold=0.7,
    coherence_constraint=True  # Ensure anchors form coherent semantic structure
)
```

### Stage 2: Anchor-Guided Reconstruction

#### Retrieval-Grounded LLM

```python
# Construct anchor-guided prompt
prompt = construct_prompt(
    anchors=selected_anchors,
    reasoning_type="chain-of-thought",
    granularity="sentence-level",
    retrieval_corpus=sentence_database  # Reference sentences
)

# Generate sentence with LLM
reconstructed_sentence = llm_generate(prompt)
```

#### Chain-of-Thought Reasoning

Prompt structure:
1. **Anchor interpretation** - what each keyword represents
2. **Semantic synthesis** - how anchors combine into meaning
3. **Sentence generation** - express meaning in natural language
4. **Verification** - check consistency with anchor evidence

#### Retrieval Strategy

- Retrieve similar sentences from database based on anchor similarity
- Use retrieved sentences as style/structure references
- Combine retrieved patterns with anchor-specific content

## Implementation Guide

### Data Preparation

**ZuCo Benchmark (Zurich Cognitive Language Processing)**:
- EEG recordings during sentence reading
- Word-level timestamps synchronized with EEG
- Sentence-level labels for evaluation

```python
# Load ZuCo dataset
zuco_data = load_zuco_benchmark()
# Structure: {sentence_id: {eeg, words, timestamps, label}}
```

### Model Architecture

**Stage 1 Model**:
- EEG encoder: CNN + transformer (extract word-level features)
- Contrastive projector: MLP (align EEG to vocabulary space)
- Keyword vocabulary: Pre-trained embeddings (CLIP, word2vec)

**Stage 2 Model**:
- LLM backbone: GPT, Claude, or retrieval-augmented model
- Retrieval corpus: Sentence database with semantic indexing
- Prompt template: Chain-of-thought structure

### Evaluation Metrics

**Sentence Retrieval Accuracy**:
- Top-5: 67.6% (Brain-CLIPLM)
- Top-25: 85.0% (Brain-CLIPLM)

**Permutation Test**:
- Verify EEG-derived anchors carry sentence-specific information
- Compare against language-model priors alone
- Significant difference indicates neural evidence contribution

### Anchor Granularity Analysis

```python
# Test different anchor numbers
for num_anchors in [3, 5, 7, 10]:
    anchors = select_top_k_anchors(evidence, k=num_anchors)
    sentence = reconstruct_with_anchors(anchors)
    accuracy = evaluate_retrieval(sentence, ground_truth)
    # Result: Intermediate granularity (5-7 anchors) performs best
```

**Key finding**: Peak performance at intermediate anchor granularity - balances information preservation and reconstruction flexibility.

## Key Results

### Performance on ZuCo

- **Top-5 retrieval**: 67.6% accuracy
- **Top-25 retrieval**: 85.0% accuracy
- **Best granularity**: 5-7 anchors per sentence

### Semantic Anchor Validity

**Permutation test result**:
- EEG-derived anchors significantly better than random anchors
- Anchors carry sentence-specific information beyond language-model priors
- Validates semantic compression hypothesis

### Granularity Matching Principle

Evidence:
- Too few anchors (3): Under-constrained, poor reconstruction
- Too many anchors (10): Over-constrained, noise dominates
- Intermediate anchors (5-7): Optimal balance

## Pitfalls

### Common Mistakes

1. **Direct sentence reconstruction**
   - **Problem**: Attempting full lexical-syntactic decoding from EEG
   - **Why fails**: EEG bandwidth insufficient for fine-grained encoding
   - **Fix**: Use semantic compression + anchor-guided reconstruction

2. **Ignoring granularity matching**
   - **Problem**: Fixed anchor count regardless of sentence complexity
   - **Why fails**: Mismatch between neural info scale and decoding complexity
   - **Fix**: Adaptive anchor selection based on EEG evidence strength

3. **Skipping retrieval grounding**
   - **Problem**: Pure LLM generation without reference corpus
   - **Why fails**: LLM hallucinates beyond anchor evidence
   - **Fix**: Retrieval-grounded generation with anchor similarity matching

4. **No permutation validation**
   - **Problem**: Not verifying EEG contribution vs language priors
   - **Why fails**: Cannot distinguish neural evidence from LLM knowledge
   - **Fix**: Permutation test comparing EEG anchors to random/null anchors

5. **Mismatched vocabulary**
   - **Problem**: Keyword vocabulary not covering sentence domain
   - **Why fails**: Cannot recover domain-specific anchors
   - **Fix**: Domain-adaptive vocabulary expansion or general vocab with fallback

### EEG Processing Pitfalls

1. **Temporal misalignment**
   - Word timestamps must match EEG epochs precisely
   - Use stimulus synchronization markers

2. **Noise contamination**
   - Apply bandpass filtering (0.5-50Hz typical)
   - Artifact removal (ICA, regression)

3. **Subject variability**
   - Individual differences in EEG patterns
   - Consider subject-specific calibration or adaptation

### LLM Generation Pitfalls

1. **Over-generation**
   - LLM adds information beyond anchors
   - Use strict anchor-guided prompts

2. **Under-generation**
   - LLM fails to synthesize anchor meaning
   - Add semantic reasoning steps in prompt

3. **Retrieval bias**
   - Retrieved sentences dominate output
   - Balance anchor evidence with retrieval patterns

## Activation Keywords

**Core concepts**: EEG decoding, semantic compression, anchor recovery, granularity matching

**Task triggers**: brain-to-text, neural decoding, EEG language processing, semantic reconstruction

**Method triggers**: CLIP alignment, contrastive learning, retrieval-grounded LLM, chain-of-thought reasoning

**Benchmark**: ZuCo, EEG sentence decoding, semantic anchor recovery

## Related Skills

- EEG decoding methodologies
- Contrastive learning frameworks
- Retrieval-augmented generation
- Brain-computer interfaces
- Neural signal processing