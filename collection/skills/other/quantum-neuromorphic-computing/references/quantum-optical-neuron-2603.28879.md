# Quantum Optical Neuron (arXiv: 2603.28879)

## Paper Details
- **Title**: Quantum Optical Neuron for Image Classification via Multiphoton Interference
- **Published**: 2026-03-30
- **Category**: quant-ph, cs.NE

## Key Methodology

### HOM Interference as Similarity Metric
- Two photons entering a 50:50 beam splitter: coincidence rate proportional to |input-template overlap| squared
- Input image encoded as spatial mode of photon A via SLM
- Template encoded as spatial mode of photon B
- Measurement: count two-photon coincidences gives direct similarity score
- No ADC, no pixel array, no digital processing pipeline

### Single-Perceptron Implementation
- SLM programs input spatial mode
- Programmable beam splitter sets template weights
- SPAD detectors count coincidences
- Threshold on coincidence rate gives binary classification

### Two-Neuron Shallow Network
- Two cascaded HOM interferometers
- Tunable beam splitters between neurons equal synaptic weights
- Multi-class via maximum coincidence across template bank

### Experimental Results
- High accuracy on benchmark datasets
- Performance insensitive to input resolution under fixed measurement budget
- Strong robustness to experimental noise
- Minimal hardware: no full quantum processor needed

## Why This Matters for Neuromorphic Quantum Computing
- First demonstration of quantum optical neuron at hardware level
- Proves quantum interference can replace classical dot-product computation
- Opens path to neuromorphic quantum photonic processors
- Photon-starved regimes (biological microscopy, remote sensing) are natural fit

## Implementation Notes
- Platform: Linear optics with SPDC or quantum dot sources
- Encoding: Spatial light modulator (SLM)
- Detection: Single-photon avalanche diodes (SPADs)
- Budget: Fixed number of coincidence measurements; optimize allocation
- Scalability: Cascading interferometers for network depth
