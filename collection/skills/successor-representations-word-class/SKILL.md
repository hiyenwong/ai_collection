---
name: successor-representations-word-class
description: >-
  First systematic application of Successor Representations (SRs) from
  reinforcement learning to natural language. Trains deep residual network on
  WikiText-103 to predict future word distributions; structured language
  representations (noun/verb/adjective categories) emerge spontaneously without
  explicit linguistic supervision. Establishes bridge between RL, linguistics,
  and cognitive neuroscience. Based on arXiv:2605.24585 (May 2026). Use when
  studying successor representations in language, emergent syntactic categories,
  predictive sequence learning in the brain, RL-inspired NLP, or cognitive
  neuroscience of language acquisition.
metadata:
  arxiv_id: "2605.24585"
  published: "2026-05-23"
  authors: "Mathis Immertreu, Achim Schilling, Thomas Kinfe, Patrick Krauss"
  categories: [cs.CL, q-bio.NC]
  tags: [successor-representations, reinforcement-learning, language-modeling, emergent-syntax, part-of-speech, predictive-coding, cognitive-neuroscience, wikitext, temporal-horizon, unsupervised-linguistics]
---

# Word Class Representations Spontaneously Emerge from Successor Representations Trained on Natural Language

**Source:** arXiv: [2605.24585](https://arxiv.org/abs/2605.24585) (May 2026)
**Authors:** Mathis Immertreu, Achim Schilling, Thomas Kinfe, Patrick Krauss

---

## 1. Overview

This paper transfers Successor Representations (SRs) — a core idea from reinforcement learning — to natural language processing. Instead of predicting the next token (standard language modeling), SRs predict the expected discounted distribution of future words across multiple temporal horizons. This reveals that syntactic categories (nouns, verbs, adjectives) emerge spontaneously without any explicit linguistic supervision.

**Core finding:** Predictive sequence learning alone is sufficient for syntactic categories to emerge — they need not be explicitly encoded.

---

## 2. Methodology

### 2.1 Successor Representations for Language

Standard language models predict the **immediate next token**:
```
P(w_{t+1} | w_1, ..., w_t)
```

Successor Representations predict the **discounted future distribution**:
```
SR(w) = E[ Σ γ^k · 1{w_{t+k+1}=w} | w_1, ..., w_t ]
```

Where:
- γ is the discount factor controlling predictive horizon
- k indexes future time steps
- 1{w=w'} is the indicator for word identity

### 2.2 Training Setup

| Component | Detail |
|-----------|--------|
| Dataset | WikiText-103 (103M tokens, 20K vocabulary) |
| Model | Deep residual neural network |
| Optimization | KL divergence for probability distributions |
| Horizons | Multiple temporal discount factors |
| Supervision | No explicit linguistic labels |

### 2.3 Emergent Structure

After training, the learned embedding space develops:

1. **Part-of-speech organization**: Nouns, verbs, adjectives become separable through unsupervised clustering
2. **Horizon-dependent structure**: Short horizons → strongest syntactic structure; longer horizons → broader contextual/semantic information
3. **Lexical substructure**: Coherent subclasses within major word categories at finer resolutions

---

## 3. Key Results

### 3.1 Spontaneous Syntactic Organization

Without any part-of-speech labels, the SR-learned representations form clear geometric clusters corresponding to syntactic categories:

- **Nouns** cluster together in embedding space
- **Verbs** form separate regions
- **Adjectives** occupy distinct areas
- Unsupervised clustering recovers these categories

### 3.2 Predictive Horizon Effects

| Horizon Length | Emerging Structure |
|----------------|-------------------|
| Short (γ ≈ 0) | Strongest syntactic organization |
| Medium | Blend of syntactic and semantic |
| Long | Dominantly semantic/contextual |

### 3.3 Conceptual Bridge

This work establishes connections between:
- **Reinforcement learning**: Successor representation framework
- **Linguistics**: Emergent syntactic categories from predictive learning
- **Cognitive neuroscience**: Neural mechanisms of language acquisition may involve predictive sequence learning

---

## 4. Implications

### 4.1 For Computational Neuroscience

- Provides a normative account of how the brain might learn syntactic categories without innate linguistic knowledge
- Suggests predictive coding frameworks (common in neuroscience) naturally give rise to linguistic structure
- Multiple timescales of prediction (short vs long horizons) may correspond to different neural circuits

### 4.2 For NLP

- Successor representations offer an alternative to next-token prediction for representation learning
- Representations capture long-range transition structure beyond surface statistics
- Interpretable emergent structure without explicit supervision

### 4.3 For Cognitive Science

- Supports usage-based theories of language acquisition
- Syntactic categories may be emergent properties of predictive learning
- Bridges statistical learning and symbolic linguistic representations

---

## 5. Activation

- successor-representations
- emergent-syntax-pos
- predictive-sequence-learning
- sr-language-modeling
- unsupervised-linguistics
- cognitive-neuroscience-language
- temporal-horizon-representations
- wikitext-successor
