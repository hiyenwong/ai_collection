# Neuro Research Paper Selection Heuristics

## How to Select High-Value Papers from arXiv Batch

### Priority Signals (score 1 point each)
1. **Novel mechanism** — proposes a new computational mechanism, not incremental
2. **Empirical breakthrough** — achieves something prior methods failed at
3. **Hardware implementation** — validated on real neuromorphic hardware (SpiNNaker, Loihi, etc.)
4. **Cross-domain impact** — connects neuroscience to ML theory or vice versa
5. **Biological grounding** — testable hypothesis about real neural circuits
6. **Theoretical depth** — provides formal analysis (convergence proofs, complexity bounds)
7. **Efficiency gains** — significant energy/compute advantage over baselines

### Deprioritize
- Incremental accuracy improvements on standard benchmarks
- Survey/review papers (already covered in existing skills)
- Purely theoretical without empirical validation
- Papers that duplicate existing skill content

### Typical Selection Pattern
From ~25 papers per search batch, select 1-2 that score ≥4 points.
Usually: 1 theory-heavy paper + 1 implementation/hardware paper.
