---
name: complex-valued-dark-signals-brain-dynamics
description: "Use when modeling brain dynamics as complex fields."
---

# Complex-Valued Dark Signals for Brain Network Dynamics

**Source**: arXiv:2509.24715 — "Dark Signals in the Brain: Augment Brain Network Dynamics to the Complex-valued Field"

## Core Idea

Observed brain signals (fMRI, EEG) are low-dimensional, indirect projections of neural dynamics in a high-dimensional unobservable space. Hamiltonian mechanics teaches that adding a dimension of conjugate momenta makes conservative dynamics more compact and elegant. Analogously: augment the observed signal x(t) (generalized coordinate) with a latent "dark signal" p(t) playing the role of conjugate momentum, lifting the dynamics to a **complex-valued field** z(t) = x(t) + i·p(t). The **Hilbert transform** is the optimal lifter within this framework (it minimizes fitting error), yielding a **Schrödinger-like equation** governing complex-valued augmented brain dynamics:

i·∂ψ/∂t = H·ψ  (whole-brain Hamiltonian, ψ complex-valued field over regions)

## Methodology

1. **Lift real signals to the complex field**
   - Observed: x_r(t) per brain region r (fMRI BOLD, EEG source signals).
   - Augment with dark signal: z_r(t) = x_r(t) + i·p_r(t), where p_r = Hilbert transform of x_r (analytic signal construction). The Hilbert transform is provably the optimal augmentation within the Hamiltonian fitting framework.
2. **Fit a complex-valued (Schrödinger-like) dynamical model**
   - Linear regime: ψ(t+Δt) = e^{-iHΔt}ψ(t); fit H by least squares over the complex field. Stability: H Hermitian ⇒ norm-preserving flow; non-Hermitian generalizations capture dissipation/nonequilibrium regimes.
   - Nonlinear regime: add a nonlinear potential V(ψ) or use a complex-valued neural ODE; compare real-valued vs complex-valued counterparts on identical data.
3. **Validate against the real-valued baseline**
   - Short-horizon prediction in the linear regime: correlation improves 0.12 → 0.82.
   - Nonlinear/nonequilibrium fits: 0.47 → 0.88.
4. **Extract structure from H**
   - Structure-function coupling: entries of H correlate with structural connectivity better than real-valued fits.
   - Hierarchical intrinsic timescales: eigenvalue spectrum |λ_j| of H recovers the hierarchy of neural timescales.
   - Directed effective connectivity: Im/Re structure of H entries gives directed influence (r→s), varying systematically with age, and reconfiguring from rest to task via **global rescaling plus targeted rewiring**.

## What the Dark-Signal Framework Buys You

- **Phase-space completeness**: a real-valued first-order model sees only half the phase space; the conjugate-momentum dimension restores second-order (oscillatory) structure without extra observed data.
- **Prediction**: dramatic short-horizon gains in both linear and nonlinear regimes.
- **Interpretability**: Hamiltonian structure gives principled directed connectivity and timescale hierarchy.
- **Rest→task reconfiguration** decomposes into a scalar global rescaling plus sparse targeted rewiring — a compact description of task-state transitions.

## Use When
- Modeling brain dynamics as Hamiltonian / neural ODE / complex-valued systems
- Building generative models of fMRI/EEG dynamics where real-valued models underpredict oscillations
- Extracting directed effective connectivity that varies with age or task
- Preprocessing oscillatory neural signals for downstream decoding (analytic signal = standard in EEG/MEG phase analyses, here given a Hamiltonian justification)

## Pitfalls
- The dark signals are **latent momenta, not measured data** — do not interpret them as hidden neural recordings; they are the conjugate-momentum completion of the observed coordinate.
- Hilbert transform assumes narrowband/analytic structure; for broadband signals apply per frequency band or filter first.
- Hermitian H conserves norm; real brain dynamics is dissipative — allow mild non-Hermiticity when modeling nonequilibrium regimes, and report both.
- Complex-valued fit improvement alone is not evidence of quantum effects in the brain — this is classical Hamiltonian mechanics in a complexified representation.

## Quick Reference

```python
import numpy as np
from scipy.signal import hilbert

# 1. Lift: analytic signal (x + i*HT[x])
z = hilbert(x, axis=0)               # x: (T, R) real signals over R regions

# 2. Linear complex fit: z(t+1) ≈ U z(t), U ≈ exp(-i H Δt)
U = np.linalg.lstsq(z[:-1], z[1:], rcond=None)[0]
# Recover Hermitian H (project U to unitary first for stability)
from scipy.linalg import logm
u, s, vh = np.linalg.svd(U)
U_unitary = u @ vh
H = 1j * logm(U_unitary) / dt   # i dψ/dt = H ψ  ⇒  U = exp(-i H dt)
H_herm = (H + H.conj().T) / 2

# 3. Directed effective connectivity: |H_rs| with sign of Im(H_rs)
dec = np.abs(H_herm)
timescales = 1.0 / np.abs(np.linalg.eigvals(H_herm) + 1e-12)
```
