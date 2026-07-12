# Adaptive Shot Budget Pattern — Quantum Circuit Execution

## Discovered: 2026-06-24 (arXiv: 2606.22170 — StableShots)

## Pattern

Instead of fixed shot budgets for quantum circuit execution, use **adaptive stopping** based on distribution convergence:

1. Execute in small batches (100-500 shots)
2. Monitor total-variation distance (TVD) between cumulative empirical distributions
3. Stop after k consecutive batches below threshold δ

## Key Numbers

- TVD ≤ 0.05 on all held-out test evaluations
- Median 7,650 shots (vs wasteful fixed-shot baselines)
- Validated on 180 QSimBench traces, 6 circuit families, 5 noisy IBM backends
- Black-box: requires no knowledge of circuit structure or backend noise model

## Skill Extraction Trigger

When encountering papers with: `adaptive shot`, `shot stopping`, `shot budget`, `online sampling`, `TVD convergence` in quant-ph — this pattern produces cross-domain value bridging quantum computing and software engineering.

## Pitfall

TVD measures distribution stability, NOT accuracy to the true distribution. A biased backend can converge to the WRONG distribution. Combine with error mitigation for accuracy-critical applications.
