# Fourier Analysis of Amplitude-Embedded VQCs

Source: arXiv:2606.14206 (Kang, Sevior, Usman, 2026-06-12)

## Core Contribution
Develops Fourier analysis framework for VQCs with **non-linear data embedding**, particularly amplitude encoding. Prior work only covered angle-embedded VQCs in noiseless settings.

## Key Results

### Domain Sensitivity
- Subtle differences in input feature domains within amplitude embedding affect **zero-frequency Fourier coefficient** expressivity
- This is distinct from angle embedding where domain effects are well-understood

### Weingarten Calculus Derivation
Under 2-design assumption for unitary ensemble:
- **Mean** of Fourier coefficients concentrated at zero
- **Variance** scales exponentially decaying with multi-dimensional frequency magnitude
- Provides rigorous expressivity bounds in frequency domain

### Noise Suppression
For noise channels with unitary Kraus operators {p_k}:
- Variance suppressed by factor `(Σ p_k²)^Q < 1`
- Q = number of channel instances applied
- Noise exponentially degrades expressivity with circuit depth

## Practical Implications
- Amplitude encoding expressivity is more constrained than angle encoding due to domain effects
- Fourier variance scaling predicts barren plateau onset depth
- Noise-aware training must account for expressivity degradation
- Weingarten calculus provides analytical alternative to empirical BP detection

## Comparison to Angle Embedding
| Property | Angle Embedding | Amplitude Embedding |
|----------|----------------|-------------------|
| Domain sensitivity | Well-studied | Subtle, affects zero-frequency |
| Noise effect | Known | Suppressed by (Σ p_k²)^Q |
| Frequency spectrum | Polynomial | Exponentially decaying |
| Barren plateau | Parameter-count driven | Frequency-magnitude driven |

## Related
- `fourier-analysis-qnn-nonlinear-embedding` skill (detailed standalone)
- `qml-feature-encoding` skill (encoding strategy selection)
- `qml-expressivity-separation` skill (expressivity theory)
