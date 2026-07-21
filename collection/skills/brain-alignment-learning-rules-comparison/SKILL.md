---
name: brain-alignment-learning-rules-comparison
description: "Comparative methodology for brain alignment across learning rules (BP, FA, PC, STDP). Key finding: single training epoch reduces V1 alignment by 25-90%. BP most destructive, PC and STDP preserve brain-like structure. Use when: brain alignment, representational similarity analysis, biologically plausible learning, visual cortex modeling, learning rule comparison. arXiv: 2605.30556"
---

## Brain Alignment Across Learning Rules

**Paper**: Supervised Training Rapidly Degrades Early Visual Cortex Alignment Across Biologically Plausible Learning Rules  
**arXiv**: 2605.30556  
**Authors**: Nils Leutenegger  
**Category**: cs.LG; q-bio.NC  
**Published**: 2026-05-28

## Core Findings

### The Paradox
Random, **untrained** neural networks consistently **match or exceed** trained networks in representational similarity to early visual cortex (V1). This challenges the assumption that learning improves brain alignment.

### Key Results

| Metric | Backpropagation | Feedback Alignment | Predictive Coding | STDP |
|--------|----------------|-------------------|-------------------|------|
| V1 alignment drop (Δr) | -0.080 | Moderate | ~-0.04 | ~-0.04 |
| Preservation of brain-like structure | Worst | Moderate | Best | Best |
| LOC alignment increase | Largest | Smaller | Small | Small |

1. **Single epoch of training reduces V1 alignment by 25-90%**, depending on learning rule
2. **Backpropagation** reduces V1 alignment most severely (Δr = -0.080)
3. **Predictive Coding and STDP** preserve substantially more brain-like structure (Δr ~ -0.04)
4. **Object-selective cortex (LOC)** shows opposite (but weaker) tendency — BP increases alignment during training

### Why This Happens
- **Untrained architectures** capture low-level visual statistics through **inductive biases alone** (architecture, connectivity patterns)
- **Global error signals** (BP) reshape early representations more aggressively
- **Local learning rules** (PC, STDP) better preserve brain-like structure because they operate locally without global optimization pressure

## Reusable Patterns

### Pattern 1: Inductive Bias First, Training Second
- Untrained networks encode meaningful visual statistics via architecture alone
- Design architectures with strong inductive biases before adding learning
- For brain-aligned models, prioritize architectural constraints over training objectives

### Pattern 2: Local vs Global Learning Rule Selection
- Use **local learning rules** (PC, STDP) when brain alignment is the goal
- Use **backpropagation** when task performance is the goal (accepts V1 misalignment)
- Consider **feedback alignment** as a middle ground

### Pattern 3: Multi-ROI Alignment Tracking
- Different brain regions respond differently to training
- V1 (early visual): alignment decreases with training
- LOC (object-selective): alignment may increase with training
- Track multiple ROIs simultaneously for comprehensive alignment assessment

### Pattern 4: RSA-Based Brain Alignment Measurement
- Use Representational Similarity Analysis (RSA) with Spearman correlations
- Compare model RDMs (Representational Dissimilarity Matrices) to brain RDMs
- Use standardized stimulus sets (e.g., THINGS database, 720 object images)
- Measure at multiple training checkpoints for temporal dynamics

## Implementation Guidance

1. For brain-aligned V1 models: Start with untrained architecture, apply minimal local learning
2. For task-oriented models with brain alignment: Use PC or STDP instead of BP for early layers
3. For evaluation: Track RSA alignment at 8+ checkpoints (epochs 0-40 minimum)
4. For stimulus design: Use diverse object databases (720+ images) with multiple subjects

## Connections to Existing Skills

- **predictive-coding-light**: PC learning rules — this paper validates PC for brain alignment
- **untrained-cnns-match-backprop-v1**: Untrained CNNs match backprop at V1 — direct confirmation
- **decoding-encoding-alignment-critique**: Brain-model alignment critique — complementary perspective
- **vlm-visual-cortex-alignment-robustness**: VLM visual cortex alignment — extends to training dynamics

## Pitfalls

- Do NOT assume training always improves brain alignment — it often degrades it in early visual areas
- The LOC trend is **weaker** than the V1 trend — do not over-interpret higher-level alignment improvements
- Results are specific to the THINGS database and 3 subjects — may not generalize to all stimuli/subjects
- The absolute alignment values matter more than relative changes — small Δr may still be significant
