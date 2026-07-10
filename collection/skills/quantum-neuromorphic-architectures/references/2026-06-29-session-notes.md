# Session Notes: 2026-06-29 Neuroscience + Quantum Mechanics

## Key Papers Discovered

### QHDC (2511.12664) - Quantum Hyperdimensional Computing
- First-ever implementation validated on 156-qubit IBM Heron r3
- HDC operations map "with remarkable elegance" to quantum-native ops
- Three-way comparison: classical simulation vs ideal quantum sim vs real hardware

### CQEC Three-Layer Quantum Brain (2604.08587)
- CRY: T2=52ms, gamma_veto=0.19, CQEC coherence=0.83 [0.76,0.79], vs 0.12 without (x6.9)
- MAO-A: T2=3.2ms, gamma_veto=3.08, CQEC coherence=0.012 (failed)
- Sensitivity: at T2=26ms (half CRY), CQEC coherence still 0.69
- Classical Markov baseline produces only monotonic relaxation (confirms quantum dynamics)
- Layer-protein tradeoff: CRY shorter T2e (0.53ns vs 1.1ns) worsens Layer 2 fidelity

### LMG Phase Transitions (2603.03345)
- Synaptic feedback expands paramagnetic phase at expense of ferromagnetic phases
- Enhanced with longitudinal field coupling
- Husimi distribution + Wehrl entropy for phase diagnosis

### LMG Homeostatic Control (2602.16003)
- Scalable computational primitives: stable set points, controllable oscillations, size-dependent robustness

### Photonic Quantum Memristors (2602.14736)
- Two coupled photonic quantum memristors with crossed feedback on silicon nitride PIC
- SiV- color center single-photon source (room temperature)
- NARMA task tested

## Knowledge Graph Operations
- DB: /Users/hiyenwong/.openclaw/workspace/kg.db
- kg_tool commands: import-paper, generate-embeddings, search, pagerank, communities, stats
- KG_DB_PATH env var overrides default /Users/hiyenwong/wiki/kg.db
