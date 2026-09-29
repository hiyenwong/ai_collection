---
name: periodically-modulated-traveling-waves
description: Traveling wave propagation failure in IF networks with periodic coupling modulation. Use when modeling wave speed in inhomogeneous neural tissue.
category: ai_collection
version: "1.0.0"
source: arXiv:2609.33006
source_title: "Periodically modulated traveling waves in integrate-and-fire networks: recursive speed law and propagation failure"
authors: "Jie Nissel, Ricardo Erazo-Toscano, Rosahn Bhattarai, Marius Osan, Mandeep Chauhan, Remus Osan"
published: 2026-09-26
categories: "cond-mat.stat-mech; cond-mat.dis-nn; nlin.PS; q-bio.NC"
trigger_words:
  - traveling wave propagation failure
  - periodic coupling modulation
  - integrate-and-fire wave speed
  - trough bottleneck speed
  - homogenization breakdown neural media
  - fold bifurcation wave
---

# Periodically Modulated Traveling Waves in Integrate-and-Fire Networks

## Overview
Methodology from arXiv:2609.33006 (Nissel, Erazo-Toscano, Bhattarai, Osan, Chauhan, Osan; submitted 2026-09-26).
The paper analyzes traveling waves of activity in a 1-D integrate-and-fire (IF) network (each neuron fires once, exponential coupling) where the synaptic coupling carries a **periodic spatial modulation** $K(x) = \epsilon k(\omega x)$. The key result: the full firing-map dynamics reduce **exactly** to a scalar ODE for the wave speed, whose slow- and fast-modulation limits admit closed-form failure boundaries. Counter-intuitively, homogenization/averaging **fails** in both limits.

## The Reduced Speed Law
Differentiating the firing map twice annihilates the spatial integral (memorylessness of the exponential kernel), yielding an exact local law:

$$a(x) = -\frac{(c-c_1)(c-c_2)}{\sigma} + B\,c\,K(x), \quad B = \frac{g_{syn}}{2V_T \tau_1}$$

with homogeneous speeds:
$$c_{1,2} = \frac{\sigma}{2}\left[(B-\beta) \mp \sqrt{(B-\beta)^2 - \frac{4}{\tau_1 \tau_2}}\right], \quad \beta = \frac{\tau_1+\tau_2}{\tau_1 \tau_2}$$

$c_1$ = slow/unstable branch, $c_2$ = fast/stable branch. Wave dynamics = 1-D flow in space $x$ pushed by modulation $\epsilon k(\omega x)$. Relaxation length $\ell = \sigma c_2/(c_2-c_1)$; the ratio $\ell/\lambda$ ($\lambda = 2\pi/\omega$) splits the two regimes.

**Default parameter set** (all numbers below): $\tau_1=1, \tau_2=2, \sigma=1, V_T=1, g_{syn}=10$ → $B=5$, $c_1 = 0.1492$, $c_2 = 3.3508$.

## Core Results

### 1. Slow limit (large λ): trough-controlled failure floor
The speed tracks the instantaneous stable equilibrium adiabatically; failure occurs when the two local equilibria collide in a **saddle-node at the trough** ($k = -1$):

$$\epsilon_0 = \frac{(\sqrt{c_2}-\sqrt{c_1})^2}{\sigma B} = 1 - \frac{g_{min}}{g}, \quad g_{min} = \frac{2V_T(\sqrt{\tau_1}+\sqrt{\tau_2})^2}{\tau_2}$$

The bottleneck speed is $c^* = \sqrt{c_1 c_2} = \sigma/\sqrt{\tau_1\tau_2}$ — strictly **above** the homogeneous unstable speed $c_1$ (contrast with rate models where the front speed vanishes at failure). Failure is set by the modulation's **extreme** (deepest trough), not by its spatial mean. For every shape normalized to $\min k = -1$, the floor is identical.

### 2. Fast limit (small λ): profile-controlled linear slope
The speed splits into slow mean $C(x)$ + fast ripple $\xi(x) = a\sin\omega x$ with $a = B\epsilon/\omega$. Averaging leaves a homogenized equation whose restoring term is the **full** period average of $1/c$, a Stieltjes transform of the ripple's sojourn (occupation) density $\rho(\xi)$:

$$S(C) = \int \frac{\rho(\xi)}{C+\xi} d\xi$$

Cosine (arcsine $\rho$) → $S = (C^2-a^2)^{-1/2}$; square (uniform $\rho$) → $S = \mathrm{arctanh}(a/C)/a$. Critical ripple amplitude from saddle-node of averaged drift:

$$C^*(c_1+c_2-C^*)^3 = (c_1 c_2)^2, \quad a_c^2 = C^{*2} - \frac{c_1 c_2}{c_1+c_2-C^*}$$

Failure boundary **linear in ω**: $\epsilon_f(\omega) \simeq (a_c/B)\,\omega$.

### 3. Shape-independent perturbation recursion
Expanding $c = c_2 + \sum_n \epsilon^n h_n(x)$, only $h_1$ is forced directly by $K$ (damped low-pass response, attenuation $1/\sqrt{\gamma^2+(k\sigma\omega)^2}$, phase lag $\delta_k = \arctan(k\sigma\omega/\gamma)$, $\gamma = (c_2-c_1)/c_2$). Every higher order is forced only by products of lower orders through the same linear operator:

$$\sigma h_n' - \lambda_0 h_n = -c_1 c_2 \tilde{P}_n, \quad \tilde{P}_n = \sum_{j\ge 2} \frac{(-1)^j}{c_2^j} \sum_{m_1+\cdots+m_j=n} h_{m_1}\cdots h_{m_j}$$

Harmonic support fixed order-by-order ($S_n$ = even/odd harmonics up to $n$). Series analytic in $\epsilon$; in the quasi-static cosine limit, **radius of convergence = failure amplitude $\epsilon_0$**.

### 4. Two distinct failure observables (do not conflate)
- **Fold** $\epsilon_{fold}(\omega)$: stable + unstable periodic profiles merge and disappear (Floquet continuation, neutral multiplier).
- **Launch threshold** $\epsilon_{launch}(\omega)$: particular launch from $c(0)=c_2$ collapses within finite horizon. Differs from fold by ≤ ~4%, either direction (basin effect below, finite-horizon effect above). Under forcing, $c_1$ is **not** a separatrix — trajectories can dip below $c_1$ on a crest and recover.

### 5. Homogenization breaks down — with explicit error budget
The weak-ripple truncation $\langle 1/c \rangle \approx C^{-1}(1+a^2/2C^2)$ predicts slope $a_H/B$ with $a_H = \sqrt{2G^*/(c_1c_2)}$. At default coupling this overshoots the true slope by **2.5×** (1.41 vs 0.568), because at the boundary the ripple is **O(1)**: $a_c/C^* = 0.93$, within 7% of the expansion's breakdown. Error spans 3 orders of magnitude across coupling range (0.1% accurate near homogeneous onset $g_{min}$ where ripple is small; 2.5× off at $g=10$). The truncated theory also misses the slow-limit plateau entirely (predicts $\epsilon_f \to 0$ as $\omega \to 0$; true value = finite floor 0.42).

### 6. Compact interpolation (whole-range boundary)
$$\epsilon_f(\omega) \approx \sqrt{\epsilon_0^2 + (m_\infty \omega)^2}, \quad m_\infty = a_c/B$$

Max error 6.6% over $0.05 \le \omega \le 20$ vs computed fold. Refined form adds slow slope $m_1 = \sigma\sqrt{c_1c_2}\epsilon_0/2B$ correction → max error 2.1%.

### 7. Shape comparison (cosine / triangle / square)
| Shape | $\rho(\xi)$ | $S(C)$ | hi-ω slope | trough power p | slow approach |
|---|---|---|---|---|---|
| cosine (smooth) | arcsine | $(C^2-a^2)^{-1/2}$ | 0.568 | 2 | $\omega^1$ |
| triangle (kinked) | parabolic | arctan+arctanh | 0.717 | 1 | $\omega^{2/3}$ |
| square (flat trough) | uniform | arctanh(a/C)/a | 0.390 | ∞ | $\omega^2$ |

Fast limit probes the **value distribution** of the integrated profile (sojourn density); slow limit probes the **local trough geometry** (power $p$ → approach exponent $2p/(p+2)$). The two limits are independent probes of modulation shape.

### 8. Piecewise-constant (square) case: exact solution
Alternating ±ε blocks of length λ: per-phase quadratics $c^2 - s_\pm c + c_1c_2 = 0$ with $s_\pm = c_1+c_2 \pm \sigma B\epsilon$. Period-closure conditions (both phase integrals = λ) give 2×2 transcendental system for speed-band endpoints $(c_0, c_f)$; closed form via partial fractions (Eq. 14–15). Failure = loss of admissible $(c_0,c_f)$ pair at a fold; complex negative-phase roots alone do NOT imply failure (positive phase catches the speed in time).

## Method Recipe (how to apply)

1. Compute $B, \beta$ from network parameters → get $c_1, c_2$ (Eq. 4).
2. For slow modulation check: is $\epsilon < \epsilon_0 = (\sqrt{c_2}-\sqrt{c_1})^2/(\sigma B)$? If yes, wave survives at ANY wavelength (below floor).
3. For fast modulation: compute $a_c$ (Eq. 33), compare $a = B\epsilon/\omega$ against $a_c$. Or use the blend $\epsilon_f(\omega) \approx \sqrt{\epsilon_0^2 + (m_\infty\omega)^2}$ for the whole range.
4. For exact boundary at given $(\epsilon, \omega)$: integrate the scalar ODE (Eq. 19) or use harmonic balance (Sec. IV B 5) — fold = saddle-node of projected algebraic equations.
5. Never use spatial-mean-only or weak-ripple homogenization to predict failure: it misses the plateau and misestimates the slope (up to 2.5×).

## Biological Significance
Cortical tissue is heterogeneous (ocular-dominance columns, barrel structure of somatosensory cortex, columnar visual cortex). In this model:
- Waves crossing periodic structure get speed-modulated with phase lag $\delta_1 = \arctan(\sigma\omega/\gamma)$ — speed profiles constrain connectivity only via a noise-sensitive **inverse problem**: $k(\omega x) = [\sigma c' + c - (c_1+c_2) + c_1 c_2/c]/(\sigma B \epsilon)$.
- Slowly varying waves are blocked **where coupling is weakest** (deepest trough), at finite bottleneck speed $\sqrt{c_1 c_2} > c_1$.
- Seizure fronts / spreading depression propagate through heterogeneous cortex — extreme-controlled failure law suggests where pathological waves **stall**.
- Rate vs IF descriptions agree on wave speed but **diverge on the failure criterion** (rate: front speed → 0; IF: bottleneck lost at strictly positive $c^*$).

## Scope & Caveats
- $\epsilon \le 1$ keeps coupling excitatory (neural model proper, covers plateau + boundary up to $\omega \approx 1.6$); $\epsilon > 1$ (sign-changing) is a model extension with hypothesized biological counterpart.
- Each neuron fires **once** (first-spike/leading-edge); repeated spiking not addressed.
- Exponential kernel essential for memoryless reduction; finite-support kernels give window-delayed dynamics, no scalar law.
- Single-scale kernels only; multiscale kernels may carry >2 candidate speeds.
- The two limits (trough vs sojourn-density) are **asymptotic**; interpolation is empirical (no uniform bound claimed).

## Key Equations Summary
| Quantity | Formula | Regime |
|---|---|---|
| Speed branches | $c_{1,2} = \frac{\sigma}{2}[(B-\beta) \mp \sqrt{(B-\beta)^2 - 4/\tau_1\tau_2}]$ | homogeneous |
| Slow failure floor | $\epsilon_0 = (\sqrt{c_2}-\sqrt{c_1})^2/\sigma B = 1 - g_{min}/g$ | $\omega \to 0$ |
| Bottleneck speed | $c^* = \sqrt{c_1 c_2} = \sigma/\sqrt{\tau_1\tau_2}$ | trough saddle-node |
| Fast slope | $\epsilon_f \simeq (a_c/B)\omega$, $a_c^2 = C^{*2} - c_1c_2/(c_1+c_2-C^*)$ | $\omega \to \infty$ |
| Blend | $\epsilon_f \approx \sqrt{\epsilon_0^2 + (m_\infty \omega)^2}$ | all $\omega$ (6.6% err) |
| First-order response | $h_1 = A_1\cos(\omega x + \phi_1)$, $A_1 = \sigma B/\sqrt{\gamma^2+(\sigma\omega)^2}$ | small $\epsilon$ |

## Related Papers
- Zhang & Osan, Phys. Rev. E 93, 052228 (2016) — homogeneous exponential-kernel precursor [1]
- Ermentrout, J. Comput. Neurosci. 5:191 (1998); Bressloff, J. Math. Biol. 40:169 (2000) — foundational IF wave analysis
- Coombes & Laing, interface method for pulsating fronts (closest prior analysis)
- Bressloff; Kilpatrick–Folias–Bressloff — inhomogeneous neural media homogenization
