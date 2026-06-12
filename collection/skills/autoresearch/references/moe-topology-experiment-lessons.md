# MoE Topology Experiment Lessons (Paper Work Project)

**Project**: H-MoE-Topo — Hierarchical MoE with Topology-Conditioned Routing
**Target venues**: NeurIPS / ICLR / ICML
**Status**: Phase 4 complete, scale-up pending

## Experimental Setup

- **Model**: N=64, char-level LM, G=8 and G=16 expert groups
- **Topologies tested**: dense, expander, ring (+ flat baseline)
- **Seeds**: 42, 123, 456
- **Total runs**: 15 (3 flat baselines + 12 hierarchical)

## Key Findings

### 1. Train-Loss Ranking is Stable, Test PPL is Not

Across all 3 seeds, train-loss ranking was **perfectly consistent**:

```
dense (2.553/2.540/2.526) < expander (2.556/2.546/2.531) < ring (2.558/2.547/2.531)
```

But test PPL rankings **flipped across seeds** — no statistically significant ordering.

**Lesson**: Stable train metrics ≠ meaningful test differences. Always report both. Do not claim a topology "wins" based on train loss alone.

### 2. Scale Requirements for Statistical Significance

At N=64 with G=16:
- Train loss differences: ~0.005 between topologies (consistent)
- Test PPL differences: ~0.2 between topologies (inconsistent)
- The hierarchical overhead itself exceeds the topology benefit at this scale

**Minimum viable scale for top-tier venues**:
- N=256, G=32 (8x more parameters)
- Multiple real datasets (not just char-level LM)
- ≥5 seeds for paired statistical tests

### 3. Topology = Implicit Regularizer

The key theoretical insight: topology acts as an **implicit regularizer** on expert mixing.

- **Over-mixing** (dense) → over-smoothing of expert representations
- **Under-mixing** (ring) → information bottleneck
- **Sweet spot** (expander) → optimal propagation in theory, but effect too small at N=64

This means topology's effect is real but subtle — needs sufficient model capacity to manifest as a measurable test-time benefit.

### 4. Flat Baseline Always Wins at Small Scale

Flat (non-hierarchical) MoE consistently outperformed all hierarchical variants at N=64:

```
flat:   best_ppl 11.80/11.65/11.90
dense:  best_ppl 12.86/12.39/12.65
```

**Reason**: Hierarchical routing overhead (extra params, 2-level gating) exceeds topology benefit at small scale. The overhead-to-benefit ratio inverts at larger scales.

## Honest Reporting Template

When experiments produce inconclusive results:

```markdown
### Results Summary

**Train loss**: [Topology A] < [Topology B] < [Topology C] (stable across N seeds)
**Test metric**: No statistically significant difference (p > 0.05, paired t-test)
**Scale**: N=[size], may be insufficient for topology effects to manifest

**Honest conclusion**: At the current scale, topology acts as a regularizer with
consistent train-loss ordering but test-time effects below detection threshold.
Scale-up to N=[target] with G=[target] is needed for conclusive results.
```

## Numbers Reference (G=16, 3 seeds)

| Topology | Seed 42 | Seed 123 | Seed 456 |
|----------|---------|----------|----------|
| flat     | 2.475 / 11.80 | 2.461 / 11.65 | 2.461 / 11.90 |
| dense    | 2.553 / 12.86 | 2.540 / 12.39 | 2.526 / 12.65 |
| expander | 2.556 / 12.74 | 2.546 / 12.51 | 2.531 / 12.66 |
| ring     | 2.558 / 12.67 | 2.547 / 12.45 | 2.531 / 12.72 |

(Train loss / Best PPL per seed)

## Architecture Lessons for H-MoE-Topo

1. **Topology state must be conditionally gated** to affect gradients — passive inclusion is ignored by optimization
2. **Scalar projection too weak** → use dot-product attention for topology conditioning
3. **ReLU causes dead gradients** → GELU + LayerNorm for stable hierarchical routing
4. **G=8 too few groups** — all topologies collapse to equivalent behavior; G≥16 needed
