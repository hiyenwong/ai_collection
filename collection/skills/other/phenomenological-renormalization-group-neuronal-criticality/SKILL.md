---
name: phenomenological-renormalization-group-neuronal-criticality
description: "Phenomenological Renormalization Group (PRG) validation methodology for detecting criticality in neuronal models. Validates PRG coarse-graining on excitable cellular automata and stochastic E/I LIF networks, introduces adaptive ISI-based time binning to eliminate spurious criticality signatures. Use for brain criticality analysis, avalanche dynamics, renormalization group neuroscience, scale-invariant neural activity. Activation: PRG, renormalization group, critical brain, neuronal criticality, avalanche, scale invariance, coarse graining, adaptive binning, non-gaussianity"
metadata:
  arxiv_id: "2506.14053"
  published: "2026-06-16"
  revised: "2026-07-01"
  authors: ["Kaio F. R. Nascimento", "Daniel M. Castro", "Gustavo G. Cambrainha", "Mauro Copelli"]
  tags: [neuroscience, criticality, renormalization-group, neuronal-avalanche, computational-neuroscience, brain-criticality]
license: Complete terms in LICENSE.txt
---

# Phenomenological Renormalization Group in Neuronal Models Near Criticality

## Core Contribution

First systematic computational validation of the Phenomenological Renormalization Group (PRG) method for detecting criticality in neuronal systems. The PRG procedure was originally proposed as a model-independent tool for detecting scale invariance in brain data, but its reliability had never been validated against ground-truth neuronal models with known critical points.

**Key finding**: PRG detects genuine scaling behavior only within a narrow vicinity of the critical point, reinforcing interpretations from experimental data. Fixed time binning can produce spurious signatures of criticality; an adaptive ISI-based binning procedure solves this.

## Theoretical Framework

### Phenomenological Renormalization Group (PRG)

The PRG applies Kadanoff-style coarse-graining to neuronal activity data via two complementary approaches:

#### 1. Momentum-Space Coarse Graining (PCA-based)

Starting from the covariance matrix of binary spike trains:
```
C_ij = <phi_i * phi_j> - <phi_i><phi_j>
```
where `phi_i(t)` is the binary spike vector (0=silence, 1=spike) of neuron i.

Eigenvalues `lambda_1 > lambda_2 > ... > lambda_N` and eigenvectors `u_{mu,i}` of C define the coarse-graining. At each RG step, project activity onto dominant eigenmodes:
```
psi_i = sum_j u_{1,i} * phi_j  (project onto leading eigenvector)
```
Iteratively decimate by keeping top N/2^k neurons sorted by eigenvector weight.

**Criticality proxy**: The distribution of normalized coarse-grained activity `psi` transitions from Gaussian (trivial/non-critical) to non-Gaussian (heavy-tailed) near criticality. Measure via:
- **Kurtosis**: `kappa = <psi^4>/<psi^2>^2` (peaks at criticality)
- **KL divergence** from Gaussian: `KL(P(psi) || N(0,1))` (peaks sharply at critical point)
- **Skewness**, **5th standardized moment** (alternative non-Gaussianity measures)

#### 2. Real-Space Coarse Graining (Network Decimation)

Correlation-based network decimation: at each step, identify the pair of most correlated neurons, merge them into a single "block" (sum their spike trains), recalculate correlations, repeat.

**Mean-variance exponent** `alpha`: Plot `Var(psi)` vs number of remaining units N' on log-log scale. A power-law scaling `Var ~ N'^alpha` with `alpha > 0` indicates non-trivial scale invariance.

### Neuronal Models Used for Validation

#### Model 1: Excitable Cellular Automaton
- N=10^4 neurons on random network with K neighbors each
- n discrete states: s=0 (resting), s=1 (excited/spiking), s=2...n-1 (refractory)
- Transition probability p from resting to excited when a neighbor spikes
- **Control parameter**: sigma (driving rate) — critical point at sigma=sigma_c
- Refractory progression is deterministic once excited

#### Model 2: Stochastic E/I Leaky Integrate-and-Fire
- Excitatory + inhibitory neurons, all-to-all connectivity
- Membrane potential evolution:
```
V_i^{E/I}(t+1) = [mu * V_i^{E/I}(t) + I_e + (J/N) * sum(X_j^E) - (gJ/N) * sum(X_j^I)] * (1 - X_i^{E/I}(t))
```
- **Control parameter**: g (E/I ratio) — critical point at g approx 1.5
- Stochastic spike when V exceeds threshold, then reset

## Adaptive Time Binning (Key Innovation)

**Problem**: Fixed time bins cause spurious results:
- Small bins in subcritical regime → sparse data → PRG falsely detects heavy tails
- Large bins in supercritical regime → temporal averaging → spurious non-Gaussianity

**Solution**: Data-driven adaptive binning proportional to average interspike interval:
```
Delta_t = f * <ISI>
```
where `<ISI> = (1/N_prg) * sum_j <ISI>_j` is the population-averaged mean ISI, and f is a single scaling factor (f~0.15-0.26).

**Benefits**:
- Eliminates spurious criticality signatures far from the critical point
- Makes results robust across dynamical phases with different activity levels
- Only one free parameter (f) instead of arbitrary bin size
- Validated on both models AND experimental rat V1 data

## Key Results

### 1. Narrow Critical Window
PRG reliably detects criticality only within ~5% of the critical control parameter value. KL divergence peaks sharply at criticality; exponent alpha peaks more gradually. This narrow window validates PRG results in experimental data as genuine critical signatures.

### 2. Spurious Signatures with Fixed Binning
Fixed bins produce false positives: subcritical data with small bins shows heavy-tailed distributions indistinguishable from critical behavior. Shuffled controls cannot always distinguish these artifacts.

### 3. Adaptive Binning Robustness
With adaptive binning (f~0.15-0.26), the critical signature appears as a narrow vertical ridge in the (control parameter, f) parameter space, centered at the critical point. The ridge persists across a broad band of f values, confirming robustness.

### 4. System Size Scaling
KL divergence at criticality grows systematically with system size N. Extrapolating `1/N -> 0` shows stronger deviations from Gaussianity in the thermodynamic limit.

### 5. Experimental Validation
Applied adaptive binning to rat V1 spiking data (9 animals, urethane-anesthetized). Results consistent with model predictions: spurious correlations at very small f, convergence at moderate f.

## Methodology Workflow

1. **Simulate/Record**: Obtain binary spike trains phi_i(t) from N neurons (typical N_prg=256 subsampled for PRG)
2. **Adaptive Binning**: Calculate `<ISI>`, set `Delta_t = f * <ISI>` (f~0.15-0.26)
3. **Build Covariance Matrix**: `C_ij = <phi_i phi_j> - <phi_i><phi_j>` over time windows
4. **Momentum-Space RG**: Eigendecompose C, project onto leading eigenmode, iterate decimation
5. **Measure Non-Gaussianity**: Calculate KL divergence, kurtosis, skewness of coarse-grained activity
6. **Shuffled Control**: Time-shuffle spikes per neuron, repeat PRG, compare
7. **Real-Space RG** (optional): Correlation-based decimation, extract alpha exponent
8. **Sweep Control Parameter**: Plot non-Gaussianity vs control parameter to locate critical point

## Pitfalls

### Fixed time binning produces spurious criticality
The most common error in PRG analysis. Fixed bins mismatched to activity density create heavy-tailed distributions that mimic critical behavior. **Always use adaptive ISI-based binning**.

### Single time window insufficient
PRG results vary across time windows even for identical parameters due to stochastic fluctuations. Average over multiple windows and report variance.

### Shuffled controls are necessary but not sufficient
Shuffling destroys temporal correlations but preserves marginal statistics. Some spurious effects survive shuffling. Compare KL divergence of data AND shuffled data relative to Gaussian (`Delta_KL = KL_data - KL_shuffled`).

### Subsampling affects results
Experimental recordings observe only a small fraction of neurons. N_prg=256 is typical; smaller samples broaden the critical window and reduce sensitivity.

### Non-Gaussianity is not unique to criticality
Heavy-tailed distributions can arise from other mechanisms (e.g., mixture of Gaussians). PRG provides evidence for, not proof of, criticality. Combine with avalanche analysis for stronger claims.

## References

- **Original PRG proposal**: Meshulam et al. (2018) - "Coarse graining approach to neural network dynamics"
- **Critical brain hypothesis**: Beggs & Plenz (2003) - Neuronal avalanches in neocortical circuits
- **Excitable cellular automaton model**: (used for criticality validation)
- **E/I LIF model**: Girardi-Schappo et al. - stochastic leaky integrate-and-fire with excitation/inhibition
- Related skills: [[brain-criticality-assessment]], [[brain-criticality-hypothesis-assessment]], [[neural-critical-dynamics-theory]], [[renormalization-scaling-brain-activity]], [[griffiths-phase-brain-criticality]]
