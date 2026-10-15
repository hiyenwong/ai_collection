---
name: neurogliovascular-unit-noradrenaline-model
description: Multicomponent NGVU model with NA-driven calcium/IP3 coupling.
category: ai_collection
---

# Neurogliovascular Unit Model with Noradrenaline Leading Force

**Paper**: Simple model of neurogliovascular unit activity with noradrenaline leading force
**arXiv**: 2610.15263 (Verisokin, Verveyko, Brazhe, Lagosha — Moscow State Univ. + Kursk State Univ., 11 Oct 2026; IEEE DCNA 2024 published version)
**Categories**: q-bio.NC

## When to Use

- Building multicomponent neurovascular-unit (NGVU) simulations coupling neurons, astrocytes, blood vessels, and extracellular space
- Modeling noradrenaline/norepinephrine neuromodulation of astrocyte calcium and vascular tone
- Studying how extracellular potassium / glutamate / GABA dynamics mediate neuron-glia-vessel feedback
- Designing hippocampal CA1 microcircuit models (pyramidal + PV interneuron + astrocyte + vessel)
- Computational studies of wake/sleep transitions or pathological dynamics driven by neuromodulator tone
- Basing work on Brian 2 simulator with HH-level biophysics

## Model Architecture (5 coupled blocks)

System scale: **50 excitatory pyramidal + 10 inhibitory PV neurons : 1 astrocyte : 1 blood vessel**, parameterized for hippocampal CA1 (parameters from Hippocampome.org + Aussel et al. 2022 biophysical models).

### 1. Neurons (modified Hodgkin-Huxley, ab initio ion-concentration form)

Membrane: C_m·dV/dt = -(I_M + I_leak + I_Na + I_K + I_Ca + I_tonic + I_syn) — pyramidal adds M-current and Ca current; PV interneurons drop I_M/I_Ca. Key coupling: **K_rev potential is dynamic**, V_revK = (RT/F)·log([K]_ext/[K]_i) — extracellular potassium concentration directly gates excitability.

- Gating variables follow dn/dt = α_n(1-n) - β_n·n
- Synapses: biexponential model, s0/s1 state variables with τ_s rise and β decay; AP-triggered reset s0 = s1
- Each pyramidal AP releases K⁺ into extracellular space AND glutamate
- GAT-3 astrocytic GABA transporter appears in the extracellular neurotransmitter loops

### 2. Astrocyte (extended calcium dynamics, adapted from Verisokin et al. 2023)

- Cytosolic Ca²⁺: d[Ca²⁺]_c/dt = (1-SVR)·J_ER + SVR·(J_in - J_out) (volume-ratio weighted ER/cytosol fluxes)
- ER Ca²⁺: d[Ca²⁺]_ER/dt = (1-SVR)·J_ER
- IP3: d[IP3]/dt = SVR·(J_δ + J_Glu + J_NA) - ([IP3]-[IP3]_∞)/τ_r — **three production sources: spontaneous δ, glutamate-driven, and NA-driven**
- Gating: dh/dt = (h_∞ - h)/τ_h
- Extracellular glutamate sensing: d[Glu]/dt = ([Glu]₀ - [Glu])/τ_Glu + v̄([K]_o) — K⁺-dependent glutamate release term

### 3. Arachidonic acid cascade (calcium-dependent vasomodulators)

AA and its derivatives (HETE family) synthesized via calcium-dependent pathway; these signaling molecules drive vasoconstriction/vasodilation — coupling astrocyte state to vessel radius.

### 4. Blood vessel (radius-dynamics hemodynamics)

- Vessel: dr/dt = (r₀ - r)/τ_r — relaxes toward reference radius r₀ modulated by vasomodulatory metabolites and extracellular K⁺
- Flow ∝ radius (Poiseuille simplification)
- Oxygen: dPO₂/dt = (PO₂₀ - PO₂)/τ_PO₂ + k_PO₂·r·r - CMRO₂·PO₂ — supply scales with radius², consumption with metabolic rate

### 5. Norepinephrine (the "leading force")

```
d[NA]/dt = J_NA + ([NA]_amb - [NA])/τ_NA + NA_diff
J_NA = r_NA + r_NG·([Glu] - [Glu]_amb)        # tonic + glutamate-coupled release
I_NA = v_NA·[NA]⁰·³/([NA]⁰·³ + k_NA)          # saturating Hill-type influx → IP3
```

NA enters the astrocyte IP3 production block (J_NA term), so neuromodulator tone directly shifts astrocyte calcium dynamics, which propagates through the AA cascade to vessel radius, oxygen supply, and back to neuronal excitability. NA controls pathways between wakefulness and sleep modes of local tissue.

## Observed Dynamics

1. **Periodic oscillatory mode** (vessel-only + astrocyte, no NA block): vessel radius, extracellular K⁺ and glutamate, astrocyte calcium all show stable periodicity; notably **doubled calcium and radius responses** to each glutamate/potassium peak (two-timescale filtering)
2. **Pseudostochastic regime** (full system with 60-neuron ensemble + NA): superimposed activity types across time scales — network spiking drives K⁺/Glu fluctuations which drive astrocyte Ca²⁺ and NA, whose characteristic times clearly differ (glutamate fast, norepinephrine slow)
3. The full coupled model exhibits multiple behavior types depending on parameters — direct connection visible between pyramidal population activity and glutamate/potassium/noradrenaline trajectories

## Method Notes

- Simulator: **Brian 2** with reduced sampling time enabled by HH dynamics — comparable with high-time-resolution experimental NGVU recordings
- Extracellular space treated as active medium: neurotransmitter leakage from synaptic clefts, gliotransmitter release, ion concentration dynamics affecting molecular machine thermodynamics
- Deliberate scope cuts: rare cell types, weak ion transporters, long-term metabolic expression changes omitted; all principal NGVU relationships retained

## Practical Guidance

1. Keep the **4.6:1 pyramidal:PV ratio per astrocyte** for CA1-like balance; reparameterize from Hippocampome.org for other regions
2. Extracellular K⁺ is the cheapest single observable to validate against — it couples to V_revK (excitability), astrocyte glutamate release v̄([K]_o), and vessel radius
3. NA acts on astrocytes primarily via IP3 production — model neuromodulator drug effects as shifts in J_NA parameters (r_NA tonic tone, r_NG glutamate-coupling gain), not as direct neuronal current
4. Use the doubled Ca²⁺/radius response to glutamate peaks as a sanity signature of the ER-cytosol two-compartment structure
5. The radius² oxygen scaling + CMRO₂ term makes the model usable for hypoxia/ischemia perturbation studies
6. Target pathology applications: sleep/wake transitions, pathological activity control via the described signaling relationships

## Related Skills

- `atp-hysteresis-tripartite-synapse` — astrocyte adenosine-mediated hysteresis (complementary gliotransmission pathway)
- `ai-collection/atp-hysteresis-tripartite-synapse` — same, aliased path
- `neurodyn-eeg-neural-dynamics-pretrained` — neural-mass inversion (macroscopic counterpart)
- `seizure-suppression-hub-stimulation` — network-level intervention targeting

## Key Equations

```
C_m dV/dt = -(I_M + I_leak + I_Na + I_K + I_Ca + I_tonic + I_syn)   # pyramidal
V_revK(t) = (RT/F)·log([K]_ext/[K]_i)                              # dynamic K reversal
d[Ca²⁺]_c/dt = (1-SVR)J_ER + SVR(J_in - J_out)
d[IP3]/dt  = SVR(J_δ + J_Glu + J_NA) - ([IP3]-[IP3]_∞)/τ_r
dr/dt = (r₀ - r)/τ_r;   dPO₂/dt = (PO₂₀-PO₂)/τ_PO₂ + k·r² - CMRO₂·PO₂
d[NA]/dt = J_NA + ([NA]_amb-[NA])/τ_NA;  J_NA = r_NA + r_NG([Glu]-[Glu]_amb)
```
