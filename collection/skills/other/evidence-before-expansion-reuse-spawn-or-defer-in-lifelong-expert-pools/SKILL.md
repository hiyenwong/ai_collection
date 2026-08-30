# Evidence Before Expansion: Reuse, Spawn, or Defer in Lifelong Expert Pools

**arXiv ID:** 2608.19888
**Authors:** Kentaro Oda
**Published:** 2026-08-20T10:54:17Z
**Abstract:**
Streaming systems that maintain a pool of expert models must repeatedly decide whether to reuse an existing expert for arriving data, spawn a new one, or defer. We present a decision layer that makes all three outcomes statistically meaningful. Reuse and spawn are posed as one-sided sequential hypotheses on a conditional (mechanism-level) discrepancy, separated by an indifference zone; defer is exactly the state in which neither betting e-process has accumulated sufficient evidence. We prove finite-time anytime validity for the observable surrogate discrepancy of a predictable discriminator sequence, and an unconditional one-sided transfer to the population quantity in which each side's slack is the excess risk of a single discriminator; an empirically observed downward-bias regularity makes the spawn side exactly conservative. Recency without sacrificing the guarantee is obtained by a restarted e-detector: a bank of unwindowed betting supermartingales at geometrically spaced restart times (O(log t) memory), with the error budget spent over restart instances, which preserves lifetime anytime validity; spending over expert-creation order likewise controls multiplicity for unboundedly many experts. On synthetic multi-concept streams, Electricity, Covertype, and the recurrence-heavy INSECTS benchmark, the instance-accounted restarted bank achieves zero false spawns and zero false reuses after switches and matches or exceeds the retired windowed heuristic (INSECTS-reoccurring accuracy 0.675), making the deployed algorithm and the guaranteed algorithm one and the same.

## Skill Description

This skill is generated from the arXiv paper: Evidence Before Expansion: Reuse, Spawn, or Defer in Lifelong Expert Pools (2608.19888).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2608.19888](http://arxiv.org/abs/2608.19888v1)
