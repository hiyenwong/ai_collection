# Systems Engineering + Quantum RSS Discovery (2026-06-04 Thursday)

## Feed Yields (Verified)

| Feed | Items | Cross-Domain Matches |
|------|-------|---------------------|
| quant-ph+cs.SE+cs.DC+cs.SY+eess.SY+cs.CR | 271 | included below |
| quant-ph+cs.SY+eess.SY | 158 | included below |
| quant-ph+cs.DC+cs.NI | 164 | included below |
| cs.SY+eess.SY+cs.DC | 57 | included below |
| **Combined (deduped)** | **650+** | **102** |

## Dual-Keyword Scoring Methodology (Verified)

Score papers by counting keyword matches in title + abstract:
- **Systems keywords**: system, control, engineer, reliability, optimization, architecture, protocol, network, distributed, fault, error, compilation, routing, scheduling, resource, verification, design, compiler, hardware, software, cyber-physical, CPS, digital twin, safety, resilience, robust, stability
- **Quantum keywords**: quantum, qubit, qaoa, vqe, entanglement, superposition, quantum neural, quantum machine, quantum computing, quantum algorithm, quantum chemistry, quantum simulation, quantum error correction, QEC, decoherence, hamiltonian
- **Filter**: require BOTH systems_score > 0 AND quantum_score > 0
- **Sort**: by total_score (systems + quantum) descending

## Top Papers Without Skills (2026-06-04)

| arXiv | Score | Title |
|-------|-------|-------|
| 2604.13643 | 10 (6+4) | Quantum secret sharing in tripartite superconducting network |
| 2511.23462 | 10 (8+2) | Arbitrary control of temporal waveform of photons during spontaneous emission |
| 2511.11404 | 9 (5+4) | Hamiltonian simulation with explicit formulas for Digital-Analog Quantum Computing |
| 2606.04079 | 7 (3+4) | Quantum error correction with the toric code |
| 2606.04186 | 7 (3+4) | Quantum Information Harvesting with the Parallel Quantum Flow Algorithm |

## Skill Created
- `arbitrary-photon-waveform-control` from arXiv:2511.23462 (Score 10, best systems+quantum match)

## Sync Gap Found
- `photon-heralded-quantum-error-characterization` existed in `ai_collection/collection/skills/` but NOT in `~/.hermes/skills/`
- Required manual `cp` to make available to agent
- Lesson: when `grep -rl` finds a skill in ai_collection but not .hermes/skills, copy it back
