---
name: self-supervised-local-learning-hierarchy
description: "Biologically plausible local self-supervised learning rules that learn hidden hierarchical data structure as efficiently as supervised backprop. Demonstrates that Direct Feedback Alignment (DFA) methods fail on hierarchical tasks due to input-specific masking. Use for biologically plausible learning algorithms, local plasticity rules, self-supervised representation learning."
arxiv_id: "2605.18557"
paper_title: "Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data"
authors: "Ariane Delrocq, Wu S. Zihan, Guillaume Bellec, Wulfram Gerstner"
publication_date: "2026-05-18"
category: "Neuroscience Research"
---

# Self-Supervised Local Learning Rules

**arXiv**: 2605.18557  
**Date**: 2026-05-18  
**Authors**: Ariane Delrocq, Wu S. Zihan, Guillaume Bellec, Wulfram Gerstner  

## Overview

This paper investigates biologically plausible learning algorithms on the Random Hierarchy Model (RHM), an artificial dataset designed to study how deep neural networks learn intrinsic hierarchical structure from high-dimensional data. The key finding is that local self-supervised learning rules (contrastive and non-contrastive) can match the data efficiency of supervised backpropagation, while Direct Feedback Alignment (DFA) methods fail on hierarchical tasks.

## Key Findings

- **Local self-supervised learning rules** using layerwise contrastive or non-contrastive loss functions solve RHM tasks as efficiently as backpropagation
- **DFA and its variants fail** on hierarchical tasks due to missing input-specific masking — a critical nonlinearity in backprop that enables learning of complex hierarchical structure
- **Compatibility with cortical plasticity**: Layerwise loss functions enable local learning rules consistent with known synaptic plasticity mechanisms in cortex

## Methodological Details

- **Random Hierarchy Model (RHM)**: A controlled synthetic dataset with known hierarchical structure that allows precise measurement of representation learning
- **Two classes of local rules tested**:
  1. Direct feedback signal approaches (DFA variants) — approximate error propagation from output
  2. Layerwise self-supervised loss functions — contrastive and non-contrastive objectives

## Significance

This work reveals a fundamental limitation of DFA methods and demonstrates that local self-supervised learning offers a biologically plausible alternative to backpropagation that does not sacrifice data efficiency. The findings provide strong constraints on theories of cortical learning and suggest that the brain may use layer-local objective functions rather than explicit error feedback.

## Activation Keywords

- local learning rules
- biologically plausible learning
- self-supervised representation learning
- Random Hierarchy Model
- Direct Feedback Alignment failure
- local plasticity
