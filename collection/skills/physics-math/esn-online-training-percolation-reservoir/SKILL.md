---
name: esn-online-training-percolation-reservoir
description: Set ESN reservoir density near the percolation threshold.
category: ai_collection
---

# Online-Trained Echo State Networks: Reservoir Topology at the Percolation Threshold

**Source**: A. Provata, M. Syroukis, J. Hizanidis (INN Demokritos / FORTH), arXiv:2610.20147, submitted 14 Oct 2026, nlin.CD + cond-mat.dis-nn + cond-mat.stat-mech + nlin.AO.

## Core Insight

**The best-performing reservoir sits at, or immediately above, the mean-field bond percolation threshold** — not at some arbitrary "1% connectivity" empirical value. Percolation theory, not folklore, sets the reservoir's operating point.

- ER reservoir: optimal p is the region just above pc = 1/(N−1) (mean-field bond percolation: each node connects to exactly one other on average). Below pc, information localizes in disconnected clusters; above pc, redundant exchange dominates.
- WS reservoir: best at low coupling range 2 ≤ R ≤ 5 on the k-ring; rewiring probability pWS has only minor influence. R=1 fails (one cut link disconnects the ring); R≥2 tolerates rewiring.
- Test systems: Lorenz (chaotic, df=2.06), Rössler (chaotic, harder — needs 3× lower learning rate), FitzHugh-Nagumo (limit cycle, df=1).

## Methodology: OLT ESN (Echo State Network with OnLine Training)

Reservoir state update and per-step readout adaptation (Widrow-Hoff LMS): only output weights W^out are trained; reservoir W and input W^in stay fixed.

```python
# OLT ESN step (Jaeger 2002 formulation)
# state: x(n) = tanh(W @ x(n-1) + W_in * I(n) + b)   # tanh activation, bias node
# prediction: y_pred(n) = W_out(n-1) @ z(n), z = augmented state [x; 1]
# LMS update:  W_out(n) = W_out(n-1) + r_learning * e(n) * z(n)
#              e(n) = I(n+1) - y_pred(n)
```

Hyperparameters used in the paper: αleaky = 0.9, learning rate r_learning ~ 1/N (chaotic Lorenz/FHN), 1/(3N) (Rössler multiscale dynamics), Ktraining = 30,000, Ktransient = 8,000 discarded, Ktest = 400.

### Reservoir construction rules

1. **ER reservoir**: choose p just above pc = 1/(N−1). For N=1000 → p ≈ 0.001–0.01; empirical "0.01 connectivity" from the literature coincides with this for typical N.
2. **WS reservoir**: N=600, coupling range R = k/2 with 2 ≤ R ≤ 5, any pWS; connectivity p = 2R/(N−1).
3. **Excitatory/inhibitory mix**: 50/50 positive/negative weights beat pure-inhibitory, which beats pure-excitatory. (Brain context: cortex ~80:20 E:I, local inhibitory up to 30%.)
4. **Symmetric reservoirs (w_ij = w_ji) perform much worse** — directional randomness matters.

## Key Results (NRMSE, lower = better)

| Reservoir | Lorenz | Rössler | FHN |
|---|---|---|---|
| ER optimal band | 0.04–0.13 | just above pc | pc-or-below acceptable (2D phase space needs fewer nodes) |
| WS best (2≤R≤5) | 0.04–0.075 | 0.04–0.26 | 0.01–0.12 |

- Averaging over 20 network realizations sharpens the optimal band without moving it (deviation map ∆NRMSE small in the optimal region).
- FHN (2D limit cycle) tolerates sub-percolation connectivity — low-dimensional attractors need fewer coupled nodes; percolation constraint binds hardest for high-dimensional chaotic attractors.

## Reusable Design Rules

1. **Set reservoir density from percolation theory, not habit**: p ≳ 1/(N−1) for ER-type; for structured reservoirs derive the specific pc of the topology (1D k-ring: pc = 1).
2. **For multiscale dynamics (Rössler-type: fast/slow alternation), divide the LMS learning rate by 3** relative to uniform-chaos (Lorenz-type) data.
3. **Online (LMS) vs offline (ridge/inversion)**: online avoids repeated state-matrix inversions and adapts to non-stationary streams; cost is per-step updates.
4. **Check percolation of the realized network**, not the nominal p — a single realization below pc has isolated modules and degraded performance.
5. **Mixed E/I signs and asymmetric weights** are structural requirements, echoing Dale's-law-like constraints in biological circuits.

## Relations

- Reservoir computing lineage: Jaeger 2001/2002 ESN, Maass 2002 LSM; Ott/Pathak next-generation RC.
- Percolation threshold as a criticality proxy aligns with edge-of-chaos reservoir theory.
- Open questions from the paper: scale-free (Barabási-Albert) reservoirs, optimal E:I ratio vs biological 80:20, structured spatial correlations, physical/neuron-model reservoirs (LIF/FHN/Hindmarsh-Rose nodes).

**Activation**: echo state network, reservoir computing, percolation threshold, online training, LMS, Lorenz, Rössler, FitzHugh-Nagumo, Watts Strogatz, Erdős-Rényi, small-world reservoir, chaotic time series prediction, NRMSE, edge of chaos
