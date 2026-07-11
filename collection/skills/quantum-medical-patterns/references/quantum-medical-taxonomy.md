# Quantum Medical Sub-Class Taxonomy (2026-07-08)

The quantum medical domain has matured into 4+ distinct sub-classes. Use this taxonomy
to classify new papers and decide whether to extend an existing skill or create a new one.

## Sub-Class 1: Entanglement-Based PET Imaging
- **Skills**: `first-in-human-quantum-entanglement-imaging`, `quantum-entanglement-pet-imaging`
- **Core technique**: Exploiting polarization entanglement of annihilation photons
- **Hardware**: J-PET plastic scintillator scanner
- **Key papers**: 2606.29421 (first human), 2606.25804 (clinical activities)
- **Create new skill if**: Novel entanglement measurement approach, new tissue types, or different scanner architecture

## Sub-Class 2: CV Photonic QNNs for Edge Medical AI
- **Skills**: `cv-photonic-qnn-edge-medical`
- **Core technique**: Continuous-variable photonic quantum neural networks
- **Key innovations**: Parameter-efficient architectures (Phi-D-U1), barren plateau mitigation
- **Key papers**: 2606.28252 (oral cancer, 18 parameters)
- **Create new skill if**: Different CV encoding strategy, new medical domain, or novel optimization technique

## Sub-Class 3: Quantum Autoencoders for Anomaly Detection
- **Skills**: `quantum-autoencoder-mri-anomaly`
- **Core technique**: Compression-driven anomaly detection with trash qubits
- **Key innovations**: Incompressibility-based scoring, encoder-decoder asymmetry analysis
- **Key papers**: 2606.27411 (brain MRI)
- **Create new skill if**: Different anomaly detection paradigm (not QAE), or QAE applied to fundamentally different modality with novel methodology

## Sub-Class 4: Quantum Ophthalmology
- **Skills**: `quantum-ophthalmology`
- **Core technique**: Quantum-enhanced retinal/visual imaging
- **Key papers**: 2606.19238 (introductory survey)
- **Create new skill if**: Specific implementation paper with novel technique beyond the survey

## Decision Rule
- Paper matches existing sub-class → **Extend existing skill** or add to `quantum-medical-patterns` as new pattern
- Paper introduces new sub-class → **Create new dedicated skill** + update this taxonomy
- Paper spans multiple sub-classes → **Synthesis**: update umbrella + reference both sub-class skills
