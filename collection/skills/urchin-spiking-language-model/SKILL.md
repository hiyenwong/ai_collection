---
name: urchin-spiking-language-model
description: "URCHIN: A Horizontal Spiking Language Model for Data-Constrained Pretraining. Single-layer Dale's-law E/I LIF connectome with multi-transmission loop, dual parallel-SSM/serial-RSNN deployment from one weight set. Use when building biologically-plausible spiking LMs, BabyLM-scale training, or event-driven edge language models."
---

# URCHIN: Horizontal Spiking Language Model

**Source**: arXiv:2609.13899 (Po-Han Chiang, NYCU, 2026-09-12) — q-bio.NC, cs.CL

## Core Thesis

A spiking language model can be trained at BabyLM scale (100M word budget) when the event-driven
spiking dynamics are recast as a parallel-scan SSM for training. One weight set runs in both
modes with identical benchmark scores — no ANN-to-SNN conversion, no conversion accuracy gap.

## Architecture (Deliberately Minimal)

- **Single horizontal layer**: 128 LIF neurons, one recurrent region, NO attention, NO depth
- **Total 4.23M parameters**; spiking core is only 34K params (0.8%) — rest is token embedding
  + untied linear LM head over 16,384 BPE vocab
- **Dale's law E/I structure**: 80/20 excitatory/inhibitory split; sign-clamped outgoing weights
  (|W| ⊙ M where sign mask M keeps each neuron purely E or I)
- **Full lateral connectivity** across four blocks: [E→E, I→E, E→I, I→I] = [1,1,1,1]
- Token embedding injected as input current; **membrane voltage of the SAME neurons**
  is read by the LM head (input and output share one population)

## Multi-Transmission Loop (Within-Token Recurrence)

Each token is resolved not in one forward pass but by a fixed-point loop over lateral
transmissions:

1. Neuron states reset at loop start (loop is within-token, separate from sequence axis)
2. Step k: embedding enters as input drive with learnable gain; previous spikes return
   through Dale-masked lateral weight with synaptic delay
3. Excitatory-membrane state V^E and refractory-reset state R with learnable leak factors;
   softplus nonlinearity; Heaviside spike at threshold
4. Membrane voltage = V^E − R; spikes of step k become lateral input of step k+1
5. Training: 13 transmission steps (target 12 + 1 buffer); Evaluation: 24 steps
   (more inference steps → closer to fixed point, free accuracy)
6. Sequence axis: log-domain **parallel prefix scan** over token positions

## Dual Implementation (The Key Trick)

| Mode | Form | Use |
|------|------|-----|
| Parallel URCHIN | SSM with parallel prefix scans (JAX/PyTorch) | GPU training, transformer-like throughput |
| Serial URCHIN | Event-driven RSNN, one timestep at a time | CPU / neuromorphic edge deployment, constant-cost inference |

- Both forms are **the same dynamics up to float summation order** — identical scores
  (agreement to floating-point floor)
- Train once, deploy either way. NOT ANN-to-SNN conversion (natively spiking, no emulation
  window of tens-hundreds of timesteps)

## Results

- Evaluated on all three BabyLM 2026 tracks: Strict-100M, Strict-Small, Multilingual
- Pretraining cost: **15–50× less compute** than GPT-2 / GPT-BERT baselines
- Biologically-plausible reference point: discrete spikes, Dale's law, lateral recurrence,
  tiny energy budget

## Implementation Checklist

1. Start from PHCSSM (Chiang 2026) core: LIF + Dale mask + lateral topology + prefix scan
2. Swap signal encoder → token embedding input current; swap classifier head → linear LM head
3. Use plain LIF (ALIF/STP/STDP available in PHCSSM but unused in URCHIN submission)
4. Clamp weight signs with |W| ⊙ M per neuron (Dale constraint during training)
5. Set transmission steps: train 13 / eval 24; verify eval steps ≥ train steps + 11
6. Untie LM head from embedding; causal next-token cross-entropy; backprop only
7. Verify parallel-serial agreement: run both modes on same checkpoint, diff logits

## When to Use

- BabyLM / data-constrained pretraining with biological constraints
- Neuromorphic or edge LM deployment (Loihi, SpiNNaker, TrueNorth-class hardware)
- Studying whether lateral-recurrent (non-attention) circuits can model language
- Baseline for "how much can a single tiny recurrent layer learn"

## Pitfalls

- Do NOT add attention or depth when replicating the minimal instance — the point is the
  single-horizontal-layer bound
- Reset neuron states per token (within-token loop ≠ sequence recurrence)
- The 24-step eval loop only helps because inference approaches the fixed point — do not
  truncate below training steps
- Surrogate gradients NOT needed: parallel-scan form makes plain backprop work

## Key References

- PHCSSM (Chiang 2026): the parent architecture — 5 biological priors (lateral, Dale, ALIF,
  STP, STDP), parallel/serial equivalence on UEA MTSCA
- SpikeGPT / SpikeLM / SpikeLLM / SpikingBERT: spiking LMs WITHOUT biological connectivity
  constraints (contrast class)
- BabyHGRN: recurrent non-transformer BabyLM precedent
- ANN-to-SNN conversion line (Cao 2015, Rueckauer 2017, Sengupta 2019, Bu 2022): the
  alternative that URCHIN avoids by being natively spiking
