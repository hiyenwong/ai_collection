---
name: decoding-encoding-alignment-critique
description: >
  Critical analysis framework for brain-model alignment methods (RSA, encoding, decoding).
  Exposes theoretical limitations of representational similarity analysis and encoding models,
  including representational collapse, feature confounding, and stimulus-set dependency.
  Use when: (1) evaluating brain-model alignment methodologies, (2) designing RSA studies,
  (3) interpreting encoding/decoding results, (4) selecting appropriate alignment metrics,
  (5) reviewing neuroscience-AI alignment papers, (6) avoiding alignment pitfalls.
  Trigger words: RSA critique, encoding model limitations, representational similarity pitfalls,
  brain-model alignment, representational collapse, feature confounding, alignment validity,
  stimulus-set dependency, cross-decoding, transformation alignment.
---

# Decoding-Encoding-Alignment Critique

Critical framework for evaluating and interpreting brain-model alignment methods.

## Core Thesis

Standard alignment metrics (RSA, encoding models, linear decoding) have systematic blind spots
that can produce misleading conclusions about brain-AI similarity.

## Key Limitations Exposed

### 1. Representational Collapse

**Problem**: RSA can report high similarity when both representations are degenerate/collapsed.
Two uninformative representations can have high RSM correlation.

**Detection**: Check representational dimensionality (participation ratio, intrinsic dimension).
Compare against low-dimensional baselines.

### 2. Feature Confounding

**Problem**: Encoding models can achieve high performance by capturing low-level confounds
(pixel statistics, image size, contrast) rather than semantic representations.

**Detection**: 
- Control for low-level features in encoding design matrices
- Cross-validate across stimulus sets with different low-level statistics
- Compare against pixel-level baselines

### 3. Stimulus-Set Dependency

**Problem**: Alignment scores vary dramatically with stimulus selection.
Results may not generalize beyond the specific stimulus set used.

**Detection**:
- Test on multiple diverse stimulus sets
- Report cross-stimulus-set generalization
- Use cross-decoding between stimulus categories

### 4. Linear Probing Artifacts

**Problem**: High linear decoding accuracy does not imply the model uses the same
representations as the brain — it only proves the information is linearly extractable.

**Detection**: 
- Compare linear vs. nonlinear probe performance
- Analyze representational geometry, not just decoding accuracy
- Use probing with matched capacity constraints

## Recommended Evaluation Protocol

1. **Multi-metric assessment**: Never rely on a single alignment metric
2. **Dimensionality matching**: Compare representations at matched dimensionalities
3. **Cross-stimulus validation**: Test generalization across stimulus distributions
4. **Null model comparison**: Always include trivial baselines (pixel features, random projections)
5. **Transformation analysis**: Use NVS (see brain-dnn-transformation-alignment) to verify
   that representations transform similarly, not just match statically

## Common Pitfalls in Alignment Studies

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| RSA inflation | High RSM correlation with degenerate RSMs | Check RSM condition number |
| Encoding overfitting | High R² on test set but poor generalization | Cross-validate across stimulus sets |
| Decoding ceiling | Near-perfect decoding from both brain and model | Use matched-capacity probes |
| Category confound | Alignment driven by coarse categories, not fine structure | Control for category structure |

## Relationship to NVS

The Naturality Violation Score (NVS) from `brain-dnn-transformation-alignment` addresses
several of these limitations by testing transformation preservation rather than static similarity.

## Practical Checklist for Paper Reviews

- [ ] Does the paper report representational dimensionality?
- [ ] Are results robust across stimulus sets?
- [ ] Are low-level confounds controlled?
- [ ] Are trivial baselines included?
- [ ] Is transformation preservation tested (beyond static RSA)?
- [ ] Is statistical significance properly assessed (permutation tests)?

## arXiv Reference

- Paper: "Critique of Representational Similarity Analysis and Encoding Models"
- ID: arXiv:2605.05907v1
- Category: q-bio.NC
