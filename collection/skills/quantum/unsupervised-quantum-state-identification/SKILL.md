---
name: "unsupervised-quantum-state-identification"
description: "Unsupervised learning methodology for automated identification of nondispersive wave packets in driven quantum systems using Floquet-based probability representations."
---

# Unsupervised Quantum State Identification

## Description
Unsupervised learning approach for automated identification of physically relevant nondispersive wave packets in driven quantum systems. Uses Floquet-based quantum state representations as probability distributions for unsupervised clustering, automating what traditionally requires detailed phase-space analysis.

**Source**: arXiv:2605.25324 — "Unsupervised learning for the systematic identification of nondispersive wave packets in driven helium"

## Activation Keywords
- unsupervised quantum state identification
- nondispersive wave packets
- driven helium quantum
- floquet quantum state learning
- automated quantum state clustering
- quantum probability distribution learning
- wave packet identification

## Core Concepts

### Nondispersive Wave Packets
- Long-lived quantum states following classical resonant orbits without spreading
- Critical for quantum control and state preparation
- Traditionally identified through manual phase-space analysis

### Floquet-Based Representation
- Quantum states computed via Floquet theory for driven systems
- Represented as probability distributions over state space
- Enables statistical/ML approaches to quantum state analysis

### Unsupervised Learning Pipeline
1. Compute Floquet quantum states for the driven system
2. Represent states as probability distributions
3. Apply unsupervised clustering to identify physically relevant states
4. Automate parameter regime exploration

## Usage Patterns

### Pattern 1: Automated Wave Packet Discovery
When searching for stable quantum states in driven systems:
1. Set up Floquet framework for the driven Hamiltonian
2. Compute eigenstates across parameter regimes
3. Convert states to probability distributions
4. Apply unsupervised clustering (e.g., DBSCAN, GMM)
5. Identify clusters corresponding to nondispersive packets

### Pattern 2: Parameter Space Exploration
When exploring parameter regimes for quantum state properties:
1. Define parameter grid for system parameters
2. Compute Floquet states at each point
3. Track state evolution across parameter space
4. Use clustering to identify robust states

### Pattern 3: Quantum State Classification
When classifying quantum states by their dynamical properties:
1. Extract probability distribution features
2. Compute similarity metrics between states
3. Cluster states by dynamical similarity
4. Identify long-lived vs. dispersive states

## Instructions for Agents

### Step 1: Floquet State Computation
1. Define the driven Hamiltonian H(t) with periodicity T
2. Compute the Floquet operator U(T)
3. Diagonalize to get Floquet states and quasienergies
4. Represent each state as probability distribution |ψ⟩⟨ψ|

### Step 2: Feature Extraction
1. Compute spatial probability density |ψ(x)|²
2. Extract phase-space representations (Wigner, Husimi)
3. Calculate statistical moments and entropic measures
4. Build feature vectors for clustering

### Step 3: Unsupervised Clustering
1. Choose appropriate clustering algorithm
2. Apply to feature vectors across parameter space
3. Identify clusters with low dispersion characteristics
4. Validate against classical resonance conditions

## Error Handling
### Floquet Convergence Issues
If Floquet states fail to converge:
- Reduce time step in propagator
- Increase basis set size
- Check for numerical instabilities in driven Hamiltonian

### Clustering Ambiguity
If clusters are not well-separated:
- Try different feature representations
- Adjust clustering hyperparameters
- Use dimensionality reduction (t-SNE, UMAP) before clustering

## Resources
- arXiv:2605.25324 — "Unsupervised learning for the systematic identification of nondispersive wave packets in driven helium" (quant-ph, May 2026)
