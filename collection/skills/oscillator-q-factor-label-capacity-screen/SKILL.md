---
name: oscillator-q-factor-label-capacity-screen
description: "Substrate-independent quality-factor screen for proposed biological information carriers. Spectral distinguishability alone bounds label capacity: M ≤ Q = 2πντ (linewidth-coherence time relation). Evaluates any proposed oscillator-based information carrier (collective vibrational modes, endogenous EM fields, microtubule excitations, phase codes) from two published numbers — independent of mechanism or quantum-biology stance. Includes six further criteria incl. two-sided persistence window (readable AND rewritable). Use when evaluating quantum-cognition/neuroscience carrier proposals, screening biological oscillators, or benchmarking EM-field brain theories."
---

# Oscillator Q-Factor Label-Capacity Screen (M ≤ Q = 2πντ)

## Paper
- **Title**: How many labels can a biological oscillator carry? A quality-factor screen for proposed information carriers (arXiv:2608.10560v2, 2026-08-11)
- **Author**: Eran Kopel
- **Categories**: q-bio.NC, physics.bio-ph, quant-ph
- **KG position (2026-10-05 import)**: Top similarity neighbor of quantum-cognition cluster (cosine 0.65–0.72 with path-integral cognition, ABS liar paradox, supraliminal information processing)

## Core Methodology

### The Central Bound
For ANY oscillator-based information carrier, spectral distinguishability alone limits the number of distinguishable labels:

```
M ≤ Q = 2π ν τ
```

where:
- `ν` = carrier frequency
- `τ` = coherence time (from linewidth: Δν = 1/(2πτ))
- `Q` = quality factor

**Why substrate-independent**: it follows purely from the **linewidth–coherence-time relation** — no assumptions about mechanism, biology, or quantum effects. Two published numbers suffice to evaluate any proposal.

### Case Study: 30 GHz Intracolumnar Microwave Field in Cortex
- Proposed carrier: endogenous 30 GHz microwave field
- Computed: **Q = 0.19** — the linewidth exceeds the carrier frequency **five-fold**
- Meaning: fewer than ONE distinguishable label — the channel cannot carry information at all
- **Rescue attempt fails**: a driven emitter can be spectrally narrower than its gain medium ONLY inside a resonant cavity — and the model's own cortical geometry forbids one
- **Independent metabolic bound exceeded by 5–9 orders of magnitude**

### The Six Further Screening Criteria (same standpoint)
1. **Two-sided persistence window** — a label must be BOTH readable (persists long enough to be read out) AND rewritable (decays fast enough to be updated)
2. Spectral distinguishability (the Q bound itself)
3. Metabolic power budget
4. Coupling to readout mechanism (can downstream machinery actually measure the label?)
5. Noise floor vs. label separation
6. Cross-talk between simultaneous labels

## Reusable Screening Protocol

```python
def q_factor_screen(nu_hz, tau_s, metabolic_power_W=None, readout_coupling=None):
    """Screen a proposed biological oscillator information carrier.
    Returns dict with capacity bound and verdict."""
    Q = 2 * math.pi * nu_hz * tau_s          # linewidth-derived capacity bound
    linewidth = 1 / (2 * math.pi * tau_s)     # Δν
    verdict = {
        'Q': Q,
        'max_labels_M': math.floor(Q),
        'linewidth_hz': linewidth,
        'linewidth_exceeds_carrier': linewidth > nu_hz,
        'carrier_resolvable': Q >= 2,          # need ≥2 labels for binary info
    }
    # Two-sided persistence window: readable AND rewritable
    # readable:  τ ≥ k / readout_rate ;  rewritable: τ ≤ T_max_update_interval
    if metabolic_power_W is not None:
        # compare against cortical metabolic budget (~20 W whole brain)
        verdict['metabolic_plausible'] = metabolic_power_W < 20.0
    return verdict

# Example: the 30 GHz cortex proposal
# nu = 30e9 Hz, tau = 1e-12 s  →  Q = 2π * 30e9 * 1e-12 ≈ 0.19  → FAIL
```

### Decision Rule
- **Q < 2**: carrier cannot hold even one bit (binary requires 2 labels) → reject proposal on spectral grounds alone
- **2 ≤ Q < M_needed**: insufficient capacity for the claimed coding scheme
- **Q ≥ M_needed**: pass to secondary criteria (metabolic, coupling, persistence window, noise, cross-talk)

## Reusable Patterns

### Pattern A: Two-number kill test
Evaluate contested proposals with a **bound derivable from two published quantities**, before engaging mechanism-specific debates. This sidesteps entire literature wars (here: quantum effects in biology) with one inequality.

### Pattern B: Geometric self-refutation check
Test whether a proposal's rescue mechanisms are **forbidden by its own geometry** (the cortical model needed a resonant cavity its geometry cannot form). Proposals that die by their own assumptions need no external counter-evidence.

### Pattern C: Two-sided persistence window
Information labels are not just about writing — they must be **simultaneously readable and rewritable**. This dual constraint (persistence vs. update speed) applies to any state-carrying substrate: neural activity-silent memory, synaptic weights, protein states, EM field configurations.

## When to Use
- Evaluating any "X is the neural information carrier" proposal (EM fields, microtubules, vibrational modes, phase codes)
- Reviewing quantum-cognition papers making channel-capacity claims
- Designing synthetic biological information carriers (optogenetics frequencies, synthetic oscillators)
- Teaching/audit of neuroscience claims: quick mechanism-independent sanity check
- Analogous screens in other domains: any oscillator-based classical or quantum channel capacity claim

## Related Skills
- `path-integral-cognition-projector-hamiltonian` (companion: models cognition quantum-mechanically — this skill bounds which carriers could physically support such models)
- `meg-quantum-information-capacity`-style capacity analyses (same family: information-theoretic bounds on neural carriers)
- `three-layer-quantum-brain` (3-layer quantum brain hypothesis evaluation)
- `nvc-mdd-eeg-fnirs` (neurovascular coupling measurement — readout coupling criterion)

## Source
- arXiv:2608.10560 — Kopel, E. (2026). "How many labels can a biological oscillator carry? A quality-factor screen for proposed information carriers."
