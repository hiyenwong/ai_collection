## 2026-05-16 - Neuroscience Research (Cron Job)

### Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation
- [[transport-mean-field-snn-dynamics]] - Transport-based mean field theory for SNN population dynamics (arXiv: 2605.14319)
  - Derives firing rate fluctuations from transport solutions to Fokker-Planck equation
  - Bridges microscopic integrate-and-fire to macroscopic population dynamics
  - **Activation**: transport equation, mean field, Fokker-Planck, firing rate fluctuations, SNN dynamics

### Multiple mechanisms of rhythm switching in recurrent neural networks with adaptive time constants
- [[rhythm-switching-adaptive-time-constants-rnn]] - Rhythm switching mechanisms in RNNs with learnable time constants (arXiv: 2605.14388)
  - Three coexisting mechanisms: subpopulation turnover, baseline shifts, phase reorganization
  - High-frequency rhythms dominated by short-time-constant neuron subpopulations
  - **Activation**: rhythm switching, adaptive time constants, RNN dynamics, frequency bands, functional differentiation


## 2026-05-15 - Number Theory, Statistics, Mathematics + Quantum (Cron Job)

### Universal quantum resource distillation via composite generalised quantum Stein's lemma
- [[quantum-resource-distillation]] - Universal framework for quantum resource distillation via composite quantum Stein's lemma, establishing fundamental limits on resource conversion rates (arXiv: 2605.15174)
  - Core: Quantum resource theories with free states F, free operations O; distillation rate bounded by Stein's bound R* = inf_σ∈F D(ρ||σ)
  - Composite settings: Rate = min_k inf_{σ∈F_k} D(ρ||σ) over union of convex free state families
  - Applications: Entanglement distillation, coherence theory, quantum thermodynamics
  - **Activation**: quantum resource distillation, quantum Stein's lemma, entanglement distillation rate, resource conversion, composite hypothesis testing

### QSeqSim: A Symbolic Simulator for Qiskit While Loops Using Sequential Quantum Circuits
- [[quantum-symbolic-simulation]] - Symbolic simulation methodology for quantum circuits with unbounded iteration (while loops) via sequential quantum circuits (arXiv: 2605.14881)
  - Core: Represents while-loop quantum programs symbolically as SQCs, enabling simulation of unbounded iteration
  - Convergence analysis: Truncation at K iterations with error ≤ (1-p)^K for exit probability p
  - Applications: Adaptive quantum algorithms, quantum error correction with repeated syndrome measurement
  - **Activation**: quantum while loop, symbolic quantum simulation, Qiskit sequential circuit, QSeqSim, quantum program verification

### Scalable self-testing of generic multipartite quantum states
- [[scalable-quantum-self-testing]] - Device-independent certification of multipartite quantum states from observed statistics alone (arXiv: 2605.15106)
  - Core: Self-testing identifies quantum state |ψ⟩ and measurements {M} from correlations P(a|x) up to local isometries
  - Bell functional construction: β(P) ≥ β_Q - ε implies ε-close to target state
  - Robustness bounds: Graph states O(√ε), GHZ states O(ε^{1/4}), cluster states O(√ε)
  - **Activation**: quantum self-testing, device-independent certification, multipartite entanglement verification, Bell inequality certification, scalable self-testing


## 2026-05-14 - Systems Engineering + Quantum (Cron Job)

### QBalance: A Reproducible Multi-Objective Workflow for Quantum Compilation, Noise Suppression, and Error-Mitigation Strategy Selection
- [[qbalance-workflow-optimization]] - Multi-objective quantum workflow optimization with Pareto strategy selection, survival-product error proxy, and Bayesian surrogate ordering (arXiv: 2605.02966)
  - Core: Weighted objective (fidelity/cost/time/reproducibility) for NISQ quantum compilation strategy selection
  - Pareto-optimal non-dominated selection across compilation, noise suppression, and error mitigation strategies
  - Bayesian linear surrogate + Thompson sampling for expensive strategy evaluation ordering
  - **Activation**: qbalance, quantum workflow optimization, quantum compilation strategy, noise suppression selection, error mitigation, multi-objective quantum


### Dynamic Quantum-Assisted Co-Design of Control Tuning and Lyapunov Stability Synthesis
- [[quantum-control-systems]] - Joint quantum-classical co-design framework for nonlinear system control with Lyapunov stability certificates (arXiv: 2605.04296)
  - Quantum search over controller-stability product space for simultaneous optimization
  - Bridges QAOA/VQE quantum optimization with classical Lyapunov synthesis
  - Exponential speedup for certain control design space exploration problems
  - **Activation**: quantum control, Lyapunov stability synthesis, quantum-assisted control, nonlinear system control, 量子控制合成


### Symplectic H2 Model Reduction for High-Dimensional Linear Quantum Systems
- [[quantum-control-systems]] - Structure-preserving model order reduction for quantum systems using symplectic balancing (arXiv: 2605.11817)
  - Preserves canonical commutation relations during reduction
  - H2 norm-optimal approximation with symplectic structure guarantees
  - **Activation**: quantum model reduction, symplectic H2, quantum system approximation


