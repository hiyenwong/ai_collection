# Systems Engineering + Quantum Cross-Domain Patterns

Session notes from 2026-07-09 hourly cron.

## Key Patterns

**Confidence-Gated Two-Stage Inference** (2607.05814): Cheap model routes majority, expensive model handles edge cases. 3.3-6.2% escalation at threshold 0.95. Bottleneck identification critical: beyond d=7, neural path saturates — optimize graph stage instead.

**Digital Twin + Multi-Agent LLM** (2607.05805): Physics-grounded simulator drives LLM agents for fault diagnosis. Few-shot + self-consistency: 0.685→0.990. Sim-to-real: 6.4% FA rate, 100% recall.

**Symbolic-Numerical Hybrid Loop** (2605.26021): LLM proposes analytic ansatz, optimizer refines parameters. Training-free across 16 tasks.

**Utility-Anonymity Trade-off** (2607.05281): Backend fingerprints in noisy quantum outputs. Routing anonymity decays exponentially at Chernoff rate. Intermediate-depth phenomenon.

## Cross-Domain Signal
"Neural" in quantum paper titles (neural decoders, neural quantum states) = valid cross-domain signal, not false positive.
