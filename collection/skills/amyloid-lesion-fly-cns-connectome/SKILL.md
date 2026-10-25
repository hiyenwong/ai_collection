---
name: amyloid-lesion-fly-cns-connectome
description: Connectome lesion sims show synapses lost beat neuron counts as damage metric.
trigger: connectome disease model, lesion simulation, drosophila pathology, synapse loss vs neuron loss, hub vulnerability, within-fly restoration, discrete phenotype, early biomarker AUC
category: neuroscience
---

# Amyloid Lesion Simulation on the Fly CNS Connectome (arXiv 2610.19153)

**Paper**: "Simulating Alzheimer's amyloid-like pathology on a fly central nervous system connectome" — Taeho Jo (Indiana Univ. School of Medicine), submitted 13 Oct 2026, q-bio.NC.

**One-line**: 在完整雄性果蝇 CNS 连接组（MaleCNS v1.0，166,700 LIF 神经元 / 24.47M 连接 / 120.26M 突触接触）上按 Aβ 果蝇报告的三条病理规则做分级损伤仿真——核心发现：**丢失神经元数是糟糕的损伤度量，突触接触数才是**；单神经元丢失可产生离散表型；早期检测看"变化量/试次间变异"比看行为学分数更灵敏。

## Model & Validation

- **Base model**: published whole-brain LIF model (FlyWire), parameters: v_rest=−52mV, θ=−45mV, τ_m=20ms, τ_syn=5ms, refractory 2.2ms, delay 1.8ms, 0.275mV/contact, dt=0.1ms. Custom engine validated against Brian2 on FlyWire v630 sugar stimulation: per-neuron rate Pearson **r=0.9997** (438 active neurons).
- **Two MaleCNS extensions** (NOT covered by validation): (1) spike-frequency adaptation to stop persistent post-stimulus activity (lowers MN9 −42%, giant fibre −17%); (2) feedforward antennal lobe (remove recurrent AL synapses, drive PNs directly) because base model activated far too many Kenyon cells (healthy odour A → median 16.6% KCs, odour B → 8.5%).
- **Stimuli**: odours A/B (8/9 PNs), sugar (MN9 readout), looming left (LPLC2/LC4 → giant fibres), appetitive training (odour A + 100Hz PAM activation, 316 neurons), memory test. Sensory neurons exempt from pathology; stimulus-delivering neurons are NOT — so every odour/looming deficit partly includes input loss.
- 1,424 simulated flies total: severity series (64 healthy + 32×10 severities 0.05–1.0), rule ablation, map comparison, contact-matched comparison, within-fly analysis (48 flies), arena cohort (176 flies).

## The Three Pathology Rules (direction from Aβ42 flies, sizes ASSUMED)

| Rule | Implementation | Fly basis |
|------|----------------|-----------|
| Threshold shift | −2 mV × load (≤29% of 7mV rest-to-threshold gap) | Kv4 loss → hyperexcitability |
| Synapse loss | each outgoing contact lost w.p. 0.6 × load | fewer NMJ active zones/boutons |
| Neuron loss | neuron removed w.p. 0.5 × load | progressive neurodegeneration |

Load = severity s × vulnerability-map value. **Hub map** (default): load = connectivity-rank percentile (damages highly connected most); **shuffled**: random; **antihub**: reversed. Pathology does NOT propagate between neurons (rules act independently).

Severity anchored at ONE point: 17% KC loss at 40 days (mushroom-body-only Aβ42 expression, [11]) → reached between s=0.5 (14.7%) and s=0.6 (17.6%). No rule parameter was fitted.

## Core Results

### 1. Same neuron count, 3× different deficit (hub/shuffled/antihub)
At s=0.5, same 11.9% of all neurons removed (Kruskal-Wallis p=0.11 across maps), whole-brain activity = **31% / 47% / 93%** of healthy median (hub/shuffled/antihub, p=3×10⁻¹⁶; antihub/hub ratio 3.04). Contacts lost: **48% / 35% / 20%** — hub map takes more synapses along because load targets contact-rich neurons.
- **Contact-matched comparison** (raise other maps' severity to equal contacts lost at 11.5/27.1/48.3%): differences shrink. Pre-specified criterion (R = most-active-map/least-active-map median ratio vs replicate variation 1.27): within replicate variation at 11.5% (R=1.20), **beyond it only at 27.1% (R=1.52)**, unresolved at 48.3% (R=1.45). Antihub deficit goes from 1/10 of hub's (equal neurons) to 36–41% (equal contacts) while losing 2.8–2.9× more neurons.
- **Confound chain**: contact-matching raises the OTHER maps' severity → larger threshold shifts (0.24/0.35/0.68 mV at 27.1%) which RAISE activity, and hub-map flies got least odour input (PN rate lowest under hub at every level, p=0.049; ρ=0.42–0.75 with whole-brain activity). **So "where the damage falls" beyond contacts lost is NOT established** — the paper is explicit about this.

### 2. Rule ablation (s=0.5, 32 flies/condition)
- Synapse loss alone → whole-brain 36%; neuron loss alone → 47% (both much of deficit).
- MBON deficit mainly from synapse loss alone (36%); neuron loss alone did NOT detectably lower MBON rate (84%, p=0.27).
- **Threshold shift ALONE raises whole-brain to 148% and MBON to 139% (protective!)**. With loss rules present, removing the shift made MBON WORSE (19% vs 31%, p=0.006) — the shift partially offsets losses, strongest in mushroom body. NOTE: disagrees with flies (Kv4 loss alone impairs larval learning) — offset reflects model construction (no hyperexcitability→neuron-loss coupling), not biology.

### 3. Within-fly counterfactual restoration (48 flies, s=0.3/0.5, identical input spikes)
- Restoring all thinned synapses (survivors' lost contacts) recovered **62%** of whole-brain deficit; restoring all removed neurons **39%**; per-fly they sum to ≈ whole deficit. Synapse-loss share LARGER at both severities; only neuron-loss share fell with severity (p=0.001). Yet removed neurons took MORE contacts than the synapse-loss rule did (26.3% vs 22.2%) — contacts-lost is not a complete measure either.
- **Neuron-loss deficit comes from input & command neurons**: antennal lobe PN class = 0.65% of removed neurons (median 99.5 neurons/fly) yet restoration recovered 11/33/30% of whole-brain/lateral-horn/KC deficits; effect grows as PN rate falls (ρ=−0.85) and is ABSENT in the 12 flies with undiminished odour input. Descending-neuron class recovered 37% of giant-fibre deficit.
- **Screen of 450/4,982 cell types**: 91–98% of single-type restorations changed NOTHING; best type recovered median 4.2% of whole-brain deficit; top-10 together 4.6%. Ranking NOT robust (holds in only 15/36 readout×variant combos). Connectivity measures did not predict which types matter (R² −0.02 to 0.05).

### 4. Discrete phenotypes from single-neuron loss
- All **66/66** flies that lost the left giant fibre had GF rate <100 Hz; only 1/254 that kept it did. A single command neuron splits a severity group in two. Below-100Hz ≠ escape failure: 13/15 such arena flies still took off (right GF can fire the burst).
- Silent MN9 followed MN9-neuron loss less closely. Opposite phenotype: 1–6 of 32 flies per severity (s=0.05–0.4) had KC AND MBON rates ABOVE the healthy maxima — candidate cause: loss of the two inhibitory APL neurons (shown in the one fly where tested).

### 5. Same KC loss, different deficit
Kenyon-cell-only pathology (mimics MB-restricted Aβ42 expression) vs pan-neuronal at same 14.7% KC loss: learning index 66% vs 28% (p=2×10⁻⁵), MBON rate 76% vs 33% (p=2×10⁻⁶); readouts outside MB indistinguishable from healthy. **A neuron count predicts nothing without knowing what else is damaged.**

### 6. Early-detection principle: change / trial-to-trial spread
- Readouts ranked by first severity reaching AUC 0.80 vs healthy: whole-brain activity & lateral horn rate at **s=0.10**; others 0.2–0.4; learning index & PN rate last; learning-index/MBON-rate never.
- AUC at s=0.10 follows |change| ÷ robust CV (ρ=0.74, exact permutation p=0.046, n=8), NOT change alone (ρ=0.38) or inverse spread alone (ρ=−0.07). Whole-brain: big change (16.6%) + moderate spread (9.6%); lateral horn: tiny change (5.6%) + tiny spread (4.0%); learning index: big change (25%) but spread 32.8% → AUC 0.66.
- Healthy flies are ONE network (spread = input-noise only) — real animals add wiring/excitability/state variation, so the RANKING may not transfer, only the principle.

## Honest Limitations (from the paper)
- Damage exceeds base-model validation range: contact loss passes the ±30% synaptic-weight robustness bound between s=0.25–0.3 → **results above s≈0.3 describe this model under large perturbation**. Lowest detected severity (s=0.10, 11.5% contacts) lies below it.
- All rule SIZES assumed (only directions from flies); hub-weighting borrowed from human imaging, **untested in flies** — single-cell data points to cell-identity vulnerability (better assumption: cell-type vulnerability from expression data + activity term).
- No homeostatic compensation, glia, sleep, failing inhibition, hyperactive-neuron elimination, pathology propagation; glutamate treated as uniformly inhibitory (base-model convention); connectome from a single male.
- Replicate groups of 32 flies differ ~27% (whole-brain), 39–44% (MBON/learning) — smaller group differences uninterpretable.
- Within-fly analysis restored neurons WITH their threshold shift and their own lost synapses; learning index measured in only 12 flies; no reverse-pairing control; arena odour readouts failed as memory measure.

## Reusable Methodological Patterns

1. **Within-fly counterfactual restoration**: re-simulate a damaged network with identical input noise but one damage component undone → causal fraction of deficit per component, immune to between-fly variance. Generalizes to any network-lesion attribution question.
2. **Contact-matched comparison with pre-registered replicate criterion**: define R = best/worst group median BEFORE running; judge "beyond replicate variation" against the max replicate ratio (1.27). Prevents over-reading group differences.
3. **Vulnerability-map trio (hub/shuffled/antihub)**: separates "how much tissue" from "which tissue" while holding neuron-count constant; then match on the deeper metric (contacts) to see how much remains.
4. **Discrete-phenotype census**: count flies by WHICH specific neuron they lost (all-66-vs-1-of-254 style) — single command/inhibitory neurons create bimodal readouts that group medians hide.
5. **AUC-vs-severity for biomarker ranking**: an early marker needs large change ÷ small trial-to-trial spread, not large change alone. Compute the ratio before collecting the biomarker.
6. **Severity anchoring**: tie an abstract damage parameter to ONE published measurement (17% KC loss at 40 days) rather than fitting anything.

## Cross-links
- Related skills: [[connectome-wiring-statistics-control]], [[connectome-wiring-specificity-null-models]], [[fly-walking-wiring-specificity]], [[functional-whole-brain-models]], [[mutation-specific-amyloid-connectome-diffusion]] (Aβ aggregation-fragmentation + connectome diffusion), [[topological-sensitivity-connectome-constraints]]
- Predictions testable in flies: (a) pan-neuronal Aβ42 → summed PN odour response falls; (b) mild stage shows minority of flies with KC/MBON above healthy range (APL loss candidate — test by APL-restricted expression); (c) population-averaged activity (e.g. lateral horn calcium) detects damage earlier than learning scores/behaviour.

**Activation**: connectome disease model, drosophila lesion simulation, amyloid pathology rules, hub vulnerability map, synapse loss vs neuron loss, within-fly restoration analysis, discrete circuit phenotype, giant fibre, early biomarker AUC, MaleCNS, 果蝇连接组损伤仿真, 突触丢失
