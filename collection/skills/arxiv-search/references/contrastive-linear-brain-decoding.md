# Contrastive-Linear Brain Decoding — fMRI Linearization Hypothesis

arXiv:2606.19081 — "Retrieval-Based Brain Decoding by Alignment, not Complexity"
Ciferri, Ferrante, Toschi (q-bio.NC; cs.HC), Jun 2026

## Core Finding

Despite neural computations being highly nonlinear at the microscale, **fMRI measurements effectively linearize observable representations** through spatiotemporal averaging and noise smoothing. This has major implications for methodology selection:

### Key Implications

1. **Linear contrastive decoders** consistently outperform ridge regression AND standard nonlinear alternatives for fMRI-to-embedding mapping
2. **Training objective choice** (contrastive vs. MSE) matters more than architectural complexity
3. **Results generalize** across images, text, and sound modalities
4. **Contrastive objectives** are biologically plausible candidates to reverse the brain loss function

### Methodology

```
fMRI activity → foundation model embedding space (CLIP, LM, audio)
                ↓
        linear contrastive decoder
                ↓
    retrieve via nearest neighbor in embedding space
```

### When to Apply

- When building brain decoders from fMRI data → **start with linear contrastive**, not complex nonlinear models
- When mapping neural representations to foundation model spaces
- When the goal is retrieval/reconstruction rather than regression
- Cross-modal decoding (images, text, audio from same neural data)

### Contrast with Existing Methods

| Method | Performance | Why |
|--------|------------|-----|
| Linear contrastive | Best | Objective matches brain organization |
| Ridge regression (linear) | Worse | MSE ≠ alignment objective |
| Nonlinear models | Worse | fMRI linearization makes complexity wasteful |

### Theoretical Connection

This connects to the high-dimensional vector theory of concepts: the brain organizes concepts as vectors where semantic meaning is captured by directions and relative angles. Contrastive objectives optimize for relative positioning, which aligns with this organization.

### Related Pattern

- `bipartite-oscillator-synchronization` (2606.20345): macroscopic dynamics emerge from microscopic complexity via averaging effects — same principle, different domain (oscillator sync vs. fMRI decoding)
