---
name: ultrasound-neuromodulation-prediction-framework
description: "Open-source computational framework for predicting ultrasound neuromodulation effects by bridging tissue elastomechanics and neuron firing dynamics. Maps transcranial acoustic fields to per-voxel neural firing maps using coupled physics models. Activation: ultrasound neuromodulation, transcranial focused ultrasound, neural firing prediction, tissue elastomechanics, Hodgkin-Huxley neuron"
metadata:
  arxiv_id: "2608.06321"
  published: "2026-08-06"
  authors: "Gianmarco Pinton"
  tags: [ultrasound, neuromodulation, computational neuroscience, biophysics, neural dynamics]
license: Complete terms in LICENSE.txt
---

# Ultrasound Neuromodulation Prediction Framework

## Overview

This skill provides access to an open-source computational framework for predicting the effects of transcranial focused ultrasound (tFUS) neuromodulation. The framework bridges tissue elastomechanics and neuron firing dynamics by mapping transcranial acoustic fields to per-voxel neural firing maps registered to anatomy.

## Key Components

The pipeline couples multiple physical and biological processes:

1. **Heterogeneous nonlinear full-wave acoustic propagation** - Models ultrasound wave propagation through skull and brain tissue
2. **Viscoelastic shear-wave propagation** - Captures mechanical wave transmission in brain tissue  
3. **Pennes bioheat diffusion** - Models thermal effects from ultrasound energy absorption
4. **Bilayer-mechanics conversion** - Transforms tissue strain to membrane tension
5. **Multi-compartment Hodgkin-Huxley neuron model** - Simulates neural firing with multiple mechanosensitive pathways

## Six Candidate Mechanisms

The framework implements six interchangeable candidate mechanisms on a shared neuron model:

- Mechanosensitive pathways
- Cavitation-coupled pathways  
- Calcium-coupled pathways
- Thermosensitive pathways
- Astrocytic-gliotransmitter pathways
- Mechanosensitive-synaptic pathways

This allows direct comparison of firing predictions for the same acoustic field across different biophysical hypotheses.

## Primary Output

The principal output is a **per-voxel firing-volume map** resolved jointly with the acoustic, elastic, and thermal field histories that drive it. This provides:

- Spatially resolved, falsifiable predictions
- Testable against high-density extracellular recordings
- Support for parameter estimation
- Cell-type-resolved mechanism identification
- Quantitative safety assessment

## Use Cases

- **Therapeutic planning**: Predict focal firing zones for targeted neuromodulation
- **Safety assessment**: Evaluate thermal rise within ITRUSST consensus safety envelopes
- **Mechanism identification**: Compare different biophysical hypotheses
- **Experimental design**: Generate testable predictions for validation studies

## Implementation Details

- Every numerical parameter is classified by source and bracketed by sensitivity analysis
- Demonstrated on theta-burst sonication through micro-CT human-skull specimen
- Targets left dorsal anterior cingulate cortex
- Predicts focal firing zone of approximately 8,500 mm³
- Thermal rise well within safety envelopes

## When to Use This Skill

Use this skill when working with:
- Transcranial focused ultrasound neuromodulation research
- Computational modeling of ultrasound-brain interactions  
- Safety assessment for ultrasound neuromodulation protocols
- Biophysical mechanism investigation for neuromodulation
- Integration of multi-physics models with neural dynamics

## Activation Keywords

- ultrasound neuromodulation
- transcranial focused ultrasound  
- neural firing prediction
- tissue elastomechanics
- Hodgkin-Huxley neuron
- acoustic field mapping
- per-voxel firing maps
- mechanosensitive pathways
- theta-burst sonication
- ITRUSST safety envelopes