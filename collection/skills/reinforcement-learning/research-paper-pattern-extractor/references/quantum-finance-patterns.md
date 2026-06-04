# Research Extraction Patterns — Economics/Finance + Quantum

## Papers from 2026-05-16 Cron Job (Saturday: Economics + Quantum Mechanics)

### Quantum Financial Time Series (arXiv:2605.02656)
**Pattern**: Hybrid classical-quantum architecture for temporal pattern learning.
- QLSTM replaces LSTM gates with variational quantum circuits; QRC uses quantum reservoir as fixed feature space
- Best results from hybrid pipeline: classical preprocessing → quantum core → classical readout
- Univariate (single lag) vs multivariate (cross-asset correlations) encoding strategies differ in qubit count

### Photonic QNN Algorithmic Advantage (arXiv:2605.10801)
**Pattern**: Room-temperature quantum computing via integrated photonics.
- Single-photon encoding with probabilistic gates emulates standard circuit model
- Key advantage: no cryogenic cooling, low decoherence, all-to-all connectivity via beamsplitters
- Trade-off: probabilistic gates require post-selection, reducing success rate

### Quantum IBP Certified Training (arXiv:2605.00747)
**Pattern**: Extending classical formal verification methods to quantum circuits.
- IBP propagates density matrix bounds through unitary evolution
- Certified loss = standard loss + λ × IBP robustness penalty
- Scales linearly with circuit depth vs exponential exact verification

### Tensor Network Option Pricing (arXiv:2603.26318)
**Pattern**: TN + GPR hybrid for high-dimensional financial surrogates.
- Tensor network compresses exponential state space to polynomial parameters
- GPR handles singularities (payoff kinks) that TN alone misses
- 100x speedup over full Monte Carlo for VaR/ES computation on 50+ asset portfolios
