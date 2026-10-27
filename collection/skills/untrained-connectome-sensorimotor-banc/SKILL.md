---
name: untrained-connectome-sensorimotor-banc
description: Use when simulating connectomes as untrained spiking nets.
category: ai_collection
version: 1.0
author: neuroscience-cron 2026-10-27
license: MIT
trigger_words:
  - connectome simulation
  - BANC
  - untrained spiking network
  - fly connectome embodied behaviour
  - NeuroMechFly
  - wiring null
  - input share rule
  - mushroom body valence
---

# Untrained Connectome Sensorimotor Simulation (BANC fly)

Source: Minnick et al., "Sensorimotor behaviour from an untrained brain-and-nerve-cord connectome", arXiv:2610.33881 (24 Oct 2026). They turned the complete BANC connectome of an adult female Drosophila (brain + ventral nerve cord: 172,433 neurons, 11.75M connections, 35.7M synapses) into a spiking network with ZERO fitted parameters, ran it inside a simulated body, and got emergent navigation plus dopamine-gated learned reversal. The method is a "fit-nothing" causal test of what wiring alone explains.

## When to Use

- Testing how much behaviour a connectome's wiring explains WITHOUT fitting or training any parameters.
- Building connectome-scale spiking simulations (fly, worm, other complete wiring diagrams) coupled to a body in a closed sensorimotor loop.
- Designing null models for connectome function claims (degree+sign-preserving rewiring, replay controls, lesion/rescue localization).
- Predicting which anatomical pathways can drive their targets from synapse-count shares alone.

## 1. Network construction recipe

Every neuron in the connection list is simulated as a leaky integrate-and-fire unit (Brian2, dt=0.1 ms):

```
tau_m dv/dt = v0 - v + g
tau_s dg/dt = -g
v0 = -52 mV, tau_m = 20 ms, tau_s = 5 ms
spike: v > -45 mV; reset v -> -52 mV, g -> 0; refractory 2.2 ms
synaptic delay 1.8 ms
```

Weight rule (the single free choice, from Shiu et al. brain model):
```
delta_g = s * n * 0.275 mV
```
- `n` = synapse count of the connection (synapse counts approximate contact area)
- `s` = +1 for acetylcholine/dopamine/serotonin/octopamine/tyramine, -1 for GABA/glutamate/histamine (glutamate signed INHIBITORY, as measured in fly antennal lobe)
- Transmitter taken from the connectome's own per-neuron prediction; unlisted neurons default +1
- Self-connections (156,311 of them, 4% of synapses) are LEFT IN — they are inert because their 1.8 ms arrival falls inside the 2.2 ms refractory period. This is a nice trick: refractoriness neutralizes autapses without editing data.
- Glia/trachea (6,404 units) left in as units; they hold 0.07% of output synapses and are functionally inert.

**Principle: do not add, remove, or reweight anything. The claim structure ("what does the wiring explain?") requires the connectome as read.**

## 2. Embodiment interface: two fixed rules only

Body: NeuroMechFly (MuJoCo), stepped at 0.1 ms; loop tick 50 ms. Nothing between network and body is trained.

Rule 1 (sensory): arena odour intensity at left/right sensors -> asymmetry a=(L-R)/mean clipped to +-1 -> ORN drive 120+80a / 120-80 Hz. Looming = 1 - mean brightness of upper 45% of ommatidia rows -> LC/LPLC drive 250x value, capped 150 Hz.

Rule 2 (motor): six leg motor pools (63-70 neurons each) -> smoothed spike counts -> per-leg gait amplitude `1 + 0.8(c-b)/s` (EMA weight 0.15, baseline b from 25 calibration steps, clipped [0.3, 1.45]). Steering: turn scaled by **valence v = (approach-MBON spikes - avoidance-MBON spikes)/norm** (clipped [-1.5, 1.5]); MBON approach/avoidance class assigned by transmitter (glutamatergic -> avoidance, GABA/cholinergic -> approach). Odour term e = tanh(-500(L-R)/mean); when v>0 slow the side with stronger odour by factor 1-0.8|e|v, when v<0 slow the opposite side (avoidance).

## 3. Validation battery (pre-registered pathway tests)

Test pathways whose behavioural role is KNOWN from experiments (15 total: sugar/bitter taste -> MN9, LPLC2/LC4 -> giant fibre escape, DNa02/PFL3 steering, DNg12 grooming, MDN backward, DNp09 forward...).

Conduction criteria (written down before each test):
- conducts: driven target rate exceeds control by >= 0.10 Hz AND by max(half control rate, 3 control SDs)
- wiring-specific: rewired twin's effect < half of intact effect
- sided rows must also carry the experimentally measured sign

**Rewired null (key control):** permute postsynaptic ends of ALL connections with a seeded RNG — every neuron keeps in-degree, out-degree, per-connection sign and synapse count; only partner identity is randomized. A result counts only if it conducts intact and dies under this shuffle. For pathway-scoped analysis, shuffle only the driven population's outgoing connections.

**The 2% input-share law:** every pathway that supplies >= ~2% of its target's input synapses conducts at some drive; pathways supplying <= 0.03% never do. Failures traced to missing physics: gap junctions (giant fibre -> TTMN needs ONE hand-added electrical connection to conduct) and absent ongoing activity.

## 4. Core empirical results

| Test | Intact | Rewired (deg+sign null) | Meaning |
|---|---|---|---|
| 9-arena navigation (32 sources) | 95% | 18% | wiring carries navigation |
| MB-lesioned | ~0% approach, walking spared | - | deficit localizes at MB output |
| Motor replay, senses off (30-deg rotated start) | 2% | - | closed sensorimotor loop required |
| Random walk, same speed | ~7% | - | baseline |
| Valence pinned at 1.44 | rescues lesion+rewired approach | - | valence is the readout that MB supplies |

Random lesion of 4,608 neurons (MB size) spares approach (2.55/3) but costs walking; removing top-1%-by-synapse-count neurons kills everything abruptly (premotor traffic). Navigation degrades gradually under random removal vs abruptly under traffic-ranked removal.

## 5. Dopamine-gated learning rule (only plasticity)

Aversive compartments: KC -> MBON synapses depress under reinforcement while the fly forages:
- 6 pairing episodes take mean plastic weight 0.513 -> 0.138 mV; approach-MBONs fall 103 -> 37 spikes/step, avoidance-MBONs stay ~50; valence 1.41 -> -0.33; every trained fly then avoids the source (Cliff's delta +1.00).
- Learning-rate threshold: eta = 1e-5 no behavioural flip (valence 0.44), eta >= 3e-5 flips.
- **Associativity condition (the key insight): depression is associative iff Kenyon-cell activity depends on the odour.** In the network as read, KCs fire 67% without any odour (antennal-lobe bistability), so reinforcement WITHOUT the odour devalues equally (non-associative). In the matched variant (KCs odour-dependent), pairing flips valence (-0.53) while reinforcement alone does nothing (1.38). Sparse code NOT required — associativity follows from odour-dependence of the code, not sparsity.
- Readout matters: valence-balance readout flips behaviour; summed-MBON-count readout floors at 0.24 (held by non-KC MBONs) and never flips. Confined (compartment-specific) reinforcement is also required.

## 6. Failure catalogue: what a wiring diagram leaves out

1. **Gap junctions**: chemical-synapse-only connectome misses the GF->TTMN electrical coupling; one hand-added connection restores conduction. Predicted this class broadly: pathways failing at ~0.01x the 2% threshold likely depend on electrical synapses.
2. **No background activity**: a silent network cannot show suppression-only actions. DNa01/DNa02 steering acts by LOWERING one side's rate; with 2-10 Hz background the sign matches the animal, in silence it does not. Steering sign depends on baseline.
3. **Transmitter prediction errors**: APL neuron predicted cholinergic (excitatory) but is GABAergic (verified column). 2,732/60,448 neurons have verified sign disagreeing with prediction (82% in optic lobe). Fixing APL alone gives 42% KC activity (still dense) — the dense code is the antennal-lobe excitatory local-neuron loop, not APL.
4. **Antennal-lobe bistability**: PN<->cholinergic-LN loop is self-sustaining once started (68% KC active with NO receptor input; hysteresis: stays on after input removed). Scaling the 105 cholinergic LN output synapses by gain g=0.15 (the "matched variant") brings KC code into the fly's 3-15% window and overlap under 0.5.
5. **Generalization follows code overlap**: depression transfer between odours tracks KC-code overlap (complete by 3 shared glomeruli), as in the fly.

## 7. Reuse checklist for other connectomes

1. Take connection list + per-neuron transmitter prediction as-is; LIF with literature parameters, nothing retuned.
2. Define minimal sensory-in / motor-out rules with FIXED constants; calibrate baselines on separate runs.
3. Pre-register pathway tests with known behavioural roles + conduction criteria BEFORE running.
4. Always run the degree+sign-preserving rewired twin at matched seeds; require conduct-and-die for any claim.
5. Measure input-share (%) of each tested pathway onto its target; use the ~2% law to predict conduction before simulating.
6. Test both silent AND background (2-20 Hz independent Poisson) regimes; suppression-mediated actions only appear with background.
7. For learning, implement dopamine-gated depression at KC->MBON (or analogue) with confined compartments; check odour-dependence of the pre-learning code before claiming associativity.
8. Replay control: hold motor commands fixed, remove sensory feedback (rotate start 30 deg) — required to prove closed-loop necessity.

## Reference numbers

- 172,433 neurons / 11,752,828 connections / 35,733,096 synapses; 24 regions; 6,775/3,884 neurons spike after odour/looming pulse; first-spike order vs wiring-traversal order Spearman rho = 0.59/0.58.
- Region-pair influence map: 139/552 responding pairs vs 358 connected; follows excitatory-signed synapse counts at rho=0.65.
- Odour pulse reaches lateral horn + descending in 12 ms, MB in 18 ms, leg pools in 24 ms.
- DNa02 600 Hz drive = 259 spikes/s due to refractory period (r/(1+0.0022r)).
- Navigation measures: intact speed 8.9 mm/s, straightness 0.61; rewired 0.31; MBON output 154 vs 7.5 spikes/step (intact vs rewired); valence 1.41 vs 0.11.

## Related skills
- [[connectome-reconstruction-robustness-audit]] — robustness audit of connectome-constrained circuits
- [[fly-walking-wiring-specificity]] / [[connectome-wiring-specificity-null-models]] — wiring-specificity nulls
- [[connectome-only-message-passing-fly-vision]] — connectome-constrained vision models
