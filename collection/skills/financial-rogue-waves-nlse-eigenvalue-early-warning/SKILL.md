---
name: financial-rogue-waves-nlse-eigenvalue-early-warning
description: Detect rogue-wave onset in volatility via NLSE eigenvalues.
category: ai_collection
---

# Financial Rogue Waves: NLSE Eigenvalue-Gradient Early Warning

**Source**: Hayward, Lennon & Biancalana, "Real-time identification of the onset of financial rogue waves" (arXiv:2606.31475, q-fin.ST, v4 2026-10-15).

## Core Idea

Transfer the optics/hydrodynamics rogue-wave framework to financial volatility indices (VIX/VXO/VSTOXX). The squared envelope of the volatility series, taken as a Kerr-shaped potential `U = -|psi|^2` in a discretized linear Schrodinger operator, develops Anderson-localized low eigenstates as an extreme peak approaches. The **numerical gradient of |minimum eigenvalue|** over a rolling window spikes reliably at the onset of extreme events.

## Method Pipeline

1. **Envelope extraction**: FFT-filter the raw index (drop Fourier peaks below the 92.5th percentile; use 95th in real-time mode), Hilbert transform to get the analytic signal, take absolute value = envelope wave. Mirror the signal at the end in real-time mode to avoid end-point artifacts.
2. **Rogue-wave labeling**: `scipy.find_peaks` prominences on the envelope; SWH = mean of top-third prominences; extreme peaks = prominence > 2 or 2.5 x SWH.
3. **Eigen-operator**: within window L (=80 trading days), build the tridiagonal matrix from finite-difference second derivative `-1/2 d^2/dt^2 + U(t)`, `U = -|psi|^2` (normalized envelope, one trading day = 1 time unit). Solve the eigensystem each day.
4. **Indicator**: numerical gradient of |lambda_min| across the last 10 windows; warning indicator = (max gradient in 10 days) x (count of gradient > 50). Reliability threshold: VIX 300 (VXO 700, VSTOXX 300), calibrated in-sample only.
5. **Real-time discipline**: envelope computed ONLY up to the last datapoint (no future data, no leakage); poor fits early in the series are expected and excluded.

## Key Results

- VIX: detects all major peaks but 2018 (too-fast 2-day rise); 2008 Lehman warning 3 days after the collapse, 18 trading days before the VIX envelope peak. Precision 84% (>2.5 SWH), 94% excluding late signals.
- Out-of-sample: VXO 87.5% and VSTOXX 87.5% major-peak detection (7/8 each); precision 63-70% full, 66-86% excluding late.
- Supporting analogies: Omori-law aftershock relaxation, long-tailed prominence distributions (as for ocean wave heights), Anderson-localization narrowing of min-eigenvector width within 5 days of a peak.
- vs LPPL+AI crash classifiers: those reach about 50.9% precision; this method trades "no signal most days" for reliable onset spikes.

## Pitfalls

- Distribution overlap: skewness/kurtosis/min-eigenvector-width shifts are NOT standalone predictors (overlapping distributions far from peaks); only the eigenvalue gradient is actionable.
- Must process the envelope (NOT the raw series) — raw noise kills the signal. The squared envelope matters (weaker nonlinearity fails).
- Parameters (L=80, cutoffs, thresholds) via repeated in-sample trials; the threshold is system-specific — no general rule yet.
- Marks regime-change onset, not prediction: it fires once the cascade begins resolving, not before.
- Feedback risk: widespread use could itself move volatility.

## Reuse

- Any extreme-event early warning on smoothed (enveloped) fat-tailed series: volatility indices, spread indicators, physical rogue-wave sensors.
- General recipe — squared envelope as potential in a linear operator, track the gradient of the extremal eigenvalue — is a cheap (LxL eigen-solve per day) leading-indicator construction.

## Metadata

- arxiv_id: 2606.31475
- published: 2026-06-30 (v4 2026-10-15)
- authors: Rosie Hayward, Orla Lennon, Fabio Biancalana
- tags: [rogue-waves, nlse, extreme-events, volatility, early-warning, econophysics]
