## 2026-05-13 - Neuroscience Research (Cron Job)

### Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets
- [[spiking-bandpass-wavelet-encoding]] - Recasts spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds; achieves NRMSE comparable to continuous wavelet transforms on ECG and audio (arXiv: 2605.09770)
  - Spike-based encoding reformulated as wavelet frame decomposition
  - Quantitative bandwidth analysis and reconstruction error bounds for spiking representations
  - Direct mapping to neuromorphic hardware (Loihi, SpiNNaker)
  - **Activation**: spiking bandpass wavelet, spike-based signal encoding, neuromorphic signal processing, temporal signal encoding, wavelet spike encoding, time-causal wavelet frames

### Cortico-cerebellar modularity as architectural inductive bias for efficient temporal learning
- [[cortico-cerebellar-modularity-rnn]] - Augments RNN with cerebellar-inspired feedforward module (CB-RNN), enabling faster convergence on temporal tasks via bidirectional cortico-cerebellar coupling (arXiv: 2605.10356)
  - Cortical module (RNN) for rich temporal dynamics + cerebellar module (feedforward) for fast predictive correction
  - Bidirectional coupling between slow recurrent and fast feedforward pathways
  - Improved learning efficiency and temporal precision across tasks
  - **Activation**: cortico-cerebellar RNN, cerebellar neural architecture, temporal sequence learning, brain-inspired RNN, modular neural architecture

     1|## 2026-05-13 - Quantum Metrology Research (Cron Job)
     2|
     3|### Optimal FALQON for Quantum Approximate Optimization via Layer-wise Parameter Tuning
     4|- [[optimal-falqon-qaoa]] - Treats per-layer time step (δ_k) and scaling factor (M_k) as classical optimization variables, reducing circuit depth vs standard FALQON, outperforms QAOA on all 94 3-regular graphs (12 vertices) (arXiv: 2605.08332)
     5|  - Single circuit evaluation per layer maintained, NISQ-compatible
     6|