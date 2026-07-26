# Quantum Drug Discovery: New Methodologies (2026)

## CovAngelo: QM/QM/MM Multiscale Embedding (arXiv:2604.10487)

Three-tier multiscale approach: inner QM (reaction center, quantum hardware), outer QM (DMET with entanglement-consistent orbitals), MM (full protein + solvent). Uses quantum information metrics (von Neumann entropy) to guide active space partitioning. Supports IQM, IonQ, IBM via CUDA-Q. Demonstrated on zanubrutinib covalent docking to BTK. Up to 20x speedup over classical methods for strongly correlated systems.

**Implementation**: See `covangelo-hybrid-quantum-drug-discovery` skill for full code.

## Quantum Wasserstein GAN for Drug Design (arXiv:2603.22399)

Style-based QGAN with VAE latent encoding. Each rotational gate receives independent noise injection for style control. WGAN-GP gradient penalty prevents mode collapse. Validated on 156-qubit IBM Heron. Benchmark: MOSES suite.

**Implementation**: See `quantum-wasserstein-gan-drug-design` skill for full code.
