---
name: repeater-swapping-scheduling-decoherence
description: Use when designing quantum repeater chains. Models memory exposure under heralding delays to find optimal repeater count and swapping schedule.
category: ai_collection
trigger_words: quantum repeater, entanglement swapping, swapping scheduling, memory decoherence, heralding delay, entanglement distribution, quantum internet, repeater count optimization
---

# Entanglement Swapping Scheduling under Decoherence (arXiv:2610.07991)

**Paper**: Díaz, Agustí, Faba, Ortiz, Robledo, Martín (UPM/UAM, quant-ph, Oct 2026)
**Task**: Analytically model first-generation quantum repeater chains where entangled memories decohere while waiting for classical heralding signals.

## Core Method: Memory Exposure Θ

The central quantity is **memory exposure** — the cumulative sum of storage times experienced by all entangled states contributing to the final end-to-end pair:

```
Θ = Θ_gen + Θ_swap
w_final = w0^(N+1) · exp(-Θ/τ)
```

- `Θ_gen`: exposure during the generation phase — pairs generated early wait while the slowest elementary link finishes; plus a global readiness delay (last EG success at one chain end must propagate across the whole chain).
- `Θ_swap`: strategy-dependent exposure during composition — per stage, (communication span time) × (number of stored pairs).
- Werner parameters multiply under swapping; decoherence acts exponentially per stored state — so **exposure, not elapsed time, is the right temporal aggregate**.

## Repeater-Count Competition (key finding)

Two opposing effects as N grows for fixed L_tot:
1. **Shorter elementary links** → higher EG probability per round → faster generation.
2. **More stored pairs + more ES ops** → additive memory decoherence + success probability drops as q^N.

Result: **an interior optimal N exists**. Repeater density is an architectural design variable, NOT something to maximize.
- Metropolitan (60 km): optimum N=1–2; rate collapses beyond.
- Intermetropolitan (500 km): optimum N≈10–11 for τ=100–150 ms; longer memories (500 ms) shift optimum to smaller N.

## Three Scheduling Strategies

| Strategy | Composition | Best regime |
|----------|-------------|-------------|
| **Binary-tree** | Hierarchical stages of 1-ES ops | Competitive as τ→large; long-memory regime |
| **Parallel** | All N repeaters swap simultaneously (single N-ES, success q^N) | Metropolitan / short chains / high-rate region |
| **Hybrid** | B blocks compose internally, then one final n-ES | Long distance (500 km), most of relevant range |

- No single strategy is optimal across all regimes — architectures should support multiple schedules.
- Policy class: reactive in EG (cheap to react), non-reactive in ES (signaling cost during late ES rounds is hard to compute and often outweighs awareness).

## Performance Metric: Entanglement Rate R

Use **logarithmic negativity** (additive over pairs) to jointly score rate and quality:
```
R = E[E2E log-negativity | success] · q^N / E[execution time]
```
- Expected execution time includes **early-abort policy**: on ES failure at stage k, only time up to failure counts; subsequent stages skipped.
- Restart requires a classical broadcast delay (max transmission time to all nodes) — include it.

## Implementation Notes

- EG rounds per link ~ geometric(p(L)); generation phase duration = max over links (slowest realization).
- Exponential fiber loss modulates baseline p0: p(L) = p0·e^(-L/L_att).
- Conservative readiness modeling: last success at chain end, information traverses full chain.
- Hybrid block parameter B must be optimized per parameter point; B=1 and B=N+1 collapse to parallel.

## Reusable Patterns

1. **Cumulative exposure aggregation** — when multiple subsystems wait on a shared signaling process, aggregate their waiting times weighted by count, not wall-clock time.
2. **Interior optimum from competing scaling** — explicit "density is a design variable" analysis for any chain-pipeline system with per-stage success probability q^stage and per-element decay.
3. **Additive entanglement metrics** — logarithmic negativity enables rate-quality tradeoff comparisons across protocols with different pair counts.
4. **Early-abort time accounting** — failed multi-stage protocols consume only time up to failure; weight stage durations by cumulative success probability.
5. **Classical-plane/quantum-plane coupling** — heralding latency directly determines memory decoherence; the classical control plane is a first-order design constraint, not overhead.

## Verification Notes

Parameters used: p0=0.5, q=0.8, w0=1 (isolates decoherence from scheduling). τ ∈ {3,6,12} ms (metro), {100,150,500} ms (intermetro). Hybrid B optimized per point. Direct-link N=0 baseline included for τ=6 ms only.

## Related

- Briegel-Dür-Cirac-Zoller repeater protocol (PRL 81, 5932, 1998) — original binary-tree ES
- Azuma et al., RMP 95, 045006 (2023) — repeater taxonomy
- Shchukin et al., PRA 100, 032322 — waiting-time computations with probabilistic ES
- kg concepts: quantum repeaters, entanglement swapping, memory exposure, swapping scheduling
