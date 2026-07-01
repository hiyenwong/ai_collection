---
name: demonstration-unpartible-entanglement
description: "Methodology for generating and certifying mode-independent (unpartible) entanglement that persists under basis transformation — a resilient quantum correlation for real-world applications."
arxiv_id: "2606.30468"
---

# Demonstration of Unpartible Entanglement

## Description
First experimental verification of mode-independent entanglement — a type of quantum entanglement that persists even when the party/mode definition is transformed. This safeguards entanglement performance in real-world quantum communication settings involving noise and untrusted parties. Uses a fully reconfigurable temporally multiplexed interferometer with measurement-induced nonlinearities to generate heralded two-photon states entangled across all orthonormal mode bases.

## Activation Keywords
- unpartible entanglement
- mode-independent entanglement
- basis-independent entanglement
- resilient quantum correlation
- temporally multiplexed interferometer
- heralded two-photon entanglement
- party-independent entanglement
- quantum communication resilience

## Core Concepts

### Mode-Independent Entanglement
Traditional entanglement is party-dependent: a state may be entangled under one party/mode definition but separable under another. Unpartible entanglement is a stronger form that remains entangled for ALL orthonormal mode basis choices, providing operational resilience.

### State Generation Scheme
- Fully reconfigurable temporally multiplexed interferometer
- Measurement-induced nonlinearities
- Heralded two-photon state generation in two modes
- Entangled for all orthonormal mode basis choices

### Certification Protocol
- Tailored quantum-state tomography
- Fidelity validation above classical bounds
- Mode-independent entanglement certified as resilient correlation

## Usage Patterns

### Pattern 1: Quantum Communication Under Noise
When designing quantum communication protocols that must operate in noisy environments or with untrusted intermediate nodes, use mode-independent entanglement as the resource instead of standard entanglement.

### Pattern 2: Entanglement Verification Under Basis Uncertainty
When the receiver's measurement basis is unknown or may vary, mode-independent entanglement guarantees that the quantum correlation survives regardless of basis choice.

### Pattern 3: Temporally Multiplexed State Generation
For generating multi-photon entangled states with high heralding rates, the temporally multiplexed interferometer architecture with measurement-induced nonlinearities provides a scalable approach.

## Instructions for Agents

### Step 1: Assess Entanglement Requirements
- Determine whether the application requires basis-dependent or basis-independent entanglement
- If the system involves unknown/untrusted measurement bases → use unpartible entanglement
- If the system has fixed, well-controlled bases → standard entanglement suffices

### Step 2: State Generation Design
- Use a fully reconfigurable temporally multiplexed interferometer
- Implement measurement-induced nonlinearities for heralded state generation
- Verify heralded two-photon states are produced in two modes

### Step 3: Certification via Tomography
- Apply tailored quantum-state tomography adapted for mode-independent certification
- Compute fidelities across multiple basis choices
- Validate that fidelities exceed classical bounds for ALL tested bases

### Step 4: Operational Validation
- Test entanglement under simulated noise conditions
- Verify performance with untrusted intermediate parties
- Measure resilience compared to standard entanglement

## Error Handling

### Certification Failure
- If fidelity drops below classical bound for some bases → the state is NOT mode-independent
- Remedy: Check interferometer calibration, verify temporal multiplexing alignment

### Heralding Rate Too Low
- Increase multiplexing depth or improve photon detection efficiency
- Consider alternative heralding schemes

## Key Results from Paper
- First experimental verification of mode-independent entanglement
- Temporally multiplexed interferometer with measurement-induced nonlinearities
- Tailored quantum-state tomography validates presence of mode-independent entanglement
- Entanglement persists as resilient, operationally advantageous quantum correlation

## Resources
- arXiv: https://arxiv.org/abs/2606.30468
- PDF: https://arxiv.org/pdf/2606.30468v1

## Related Skills
- `quantum-entanglement-detection` — general entanglement detection and characterization
- `demonstration-unpartible-entanglement` — this skill (mode-independent entanglement)
- `quantum-communication-distributed-privacy` — quantum communication primitives
