---
name: spatial-neighboring-scattering-transform
description: Spatial Neighboring Scattering Transform (SNST) — a wavelet-scattering-based cross-channel amplitude-coupling measure for EEG connectivity that captures amplitude-envelope and cross-frequency coupling, robust to volume conduction where phase-sync fails. Use when building EEG/fNIRS functional connectivity pipelines, comparing against PLI/wPLI, or extracting inter-regional amplitude-domain dependence.
---

# Spatial Neighboring Scattering Transform (SNST)

**Paper:** "Spatial Neighboring Scattering Transform: A Cross-Channel Amplitude Coupling Measure for EEG Connectivity" — Tawhid, Rafe, Priyom, Rahman. arXiv:2607.08855 (q-bio.NC, eess.SP, stat.AP), 2026-07-09.

## Why it matters
Standard EEG connectivity = **phase synchronization** (PLI, wPLI, coherence). Three problems:
1. **Volume conduction artifacts** — phase sync is contaminated by shared sources; PLI/wPLI mitigate but don't capture amplitude coupling.
2. **Amplitude-domain coupling discarded** — envelope correlations carry real inter-regional dependence invisible to phase methods.
3. **Single-frequency bias** — classic measures miss cross-frequency amplitude-modulation structure (e.g., slow rhythm gating fast coupling).

SNST extends the **wavelet scattering transform** (Mallat) to the **multichannel / spatial** setting, producing two descriptors:
- **First-order descriptor** → amplitude-envelope coupling between neighboring channels (consistent across subjects/conditions).
- **Second-order descriptor** → how that coupling is *modulated across frequency scales* (cross-frequency amplitude structure).

In the paper, on BCI IV-2a motor imagery: first-order SNST found significant central-parietal amplitude coupling reproduced in **all subjects** and **both imagery conditions**; second-order revealed the coupling is **periodically gated by slow rhythms**. PLI/wPLI under identical FDR correction found **negligible coupling with zero overlap** → amplitude-envelope coupling is a largely *distinct* connectivity signal.

## The method (recipe)
1. **Per-channel wavelet scattering**: for each EEG channel, compute scattering coefficients U[m](t) over a set of wavelet scales (Morlet/Gabor), yielding a time-series of scale-indexed representations.
2. **Spatial neighbor pooling**: define channel neighborhoods by spatial adjacency (electrode montage graph / Euclidean distance on scalp). For each channel, aggregate scattering coefficients over its neighbors → "spatial neighboring" representation.
3. **First-order descriptor**: amplitude-envelope coupling = correlation/coherence of the (Hilbert) amplitude envelopes between a channel's own scattering path and its neighbors' pooled path, across scales.
4. **Second-order descriptor**: compute modulation of the first-order coupling magnitude as a function of frequency scale (i.e., how envelope coupling at scale j depends on scale k) → reveals cross-frequency gating.
5. **Statistics**: bias-correct, control false discovery rate (FDR/BH), validation criterion = *spatial consistency of significant coupling across subjects* (not just per-subject p-values).

## When to use
- Multichannel EEG/fNIRS where amplitude-domain inter-regional dependence matters.
- As a **complement** to phase-sync (PLI/wPLI) — report both; expect low overlap.
- Cross-frequency coupling / rhythmic gating discovery.
- Anywhere volume conduction is a concern but you still want undirected connectivity.

## Pitfalls
- SNST is **undirected** and still shares some volume-conduction sensitivity at the envelope level — use spatial-neighbor *differencing* or source-localized input to reduce.
- Scale selection and wavelet Q-factor matter; validate descriptor stability across subjects.
- Not a causality measure (no directionality) — pair with Granger/DCM if direction needed.
- Compute cost scales with channels × scales; subsample scales for long recordings.

## Key references
- Mallat, "Group Invariant Scattering" (wavelet scattering foundations).
- PLI / wPLI (Stam, Nolte) — phase-sync baselines robust to volume conduction.
- BCI Competition IV-2a — motor imagery benchmark used in the paper.

## Activation
Triggers: EEG connectivity, amplitude coupling, wavelet scattering, volume conduction, PLI wPLI comparison, cross-frequency coupling, motor imagery connectivity, multichannel neural signal.
