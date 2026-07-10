---
name: topological-grid-cell-decoding-codes
description: "Topological decoding of grid cell activity via path lifting to covering spaces. Uses TDA to extract toroidal coordinates from grid cell populations and reconstructs spatial trajectories from a single module without training data or external position info. Activation: grid cells, topological data analysis, toroidal manifold, path lifting, spatial navigation, neural manifolds, continuous attractor network, entorhinal cortex, path integration, covering space"
metadata:
  arxiv_id: "2510.16216"
  published: "2025-10-17"
  updated: "2026-07-08"
  authors: "Yuxing Jared Yao, Iris H. R. Yoon"
  tags: [grid cells, topological data analysis, toroidal manifold, path lifting, spatial navigation, neural manifolds, entorhinal cortex, covering spaces]
---

# Topological Decoding of Grid Cell Activity via Path Lifting to Covering Spaces

## Core Concept

Grid cells in the medial entorhinal cortex encode spatial position on a **toroidal manifold** due to their periodic firing patterns. This paper introduces a purely topological framework to decode spatial trajectories from grid cell population activity **without training data, external position labels, or supervised learning** — using only the intrinsic topological structure of the neural manifold.

## Key Innovations

### 1. Toroidal Coordinate Extraction via TDA
- Use **topological data analysis** (persistent homology) to identify the toroidal structure in high-dimensional grid cell population activity
- Extract **toroidal coordinates** (angular parameters on the torus) from the neural manifold
- Works on both simulated continuous attractor networks (CANs) and experimental recordings

### 2. Path Lifting to Covering Spaces
- The toroidal manifold is periodic — a single point on the torus corresponds to infinitely many physical positions
- **Path lifting** to the covering space (Euclidean plane ℝ²) resolves this ambiguity
- Reconstructed trajectories differ from ground truth only by an **affine transformation** (rotation, scaling, translation)
- Demonstrates that a **single grid cell module** contains sufficient information for path integration

### 3. Training-Free Decoding
- No neural network training, no calibration, no external position reference
- Entirely based on the **topological structure** of the population code
- Validated on both CAN simulations and real experimental grid cell recordings

## Methodology

### Step 1: Extract Neural Manifold
1. Collect grid cell population activity vectors (firing rates across cells at each time point)
2. Apply dimensionality reduction (e.g., PCA, UMAP) to identify low-dimensional embedding
3. Verify toroidal topology via persistent homology (two independent 1-cycles = torus)

### Step 2: Extract Toroidal Coordinates
1. Map neural activity to angular coordinates (θ₁, θ₂) on the torus
2. Use circular statistics to track the position on each cycle of the torus
3. Handle wrapping/discontinuities at torus boundaries

### Step 3: Path Lifting
1. Starting from an initial position, integrate angular changes over time
2. Lift the path from the torus T² to the covering space ℝ²
3. Track unwrapping events when the path crosses torus boundaries
4. Result: reconstructed trajectory in physical space (up to affine transform)

### Step 4: Validation
- Compare reconstructed trajectory to ground truth via Procrustes analysis
- Measure correlation, angular error, and path similarity
- Validated on: (a) CAN simulations with known ground truth, (b) experimental recordings

## Key Findings

- **Single-module sufficiency**: One grid cell module contains enough information for reliable path reconstruction
- **Affine equivalence**: Reconstructed paths match ground truth up to rotation + scaling + translation
- **No training needed**: Purely topological, no supervised learning or calibration
- **Robust to noise**: Works on experimental data with biological variability
- **Path integration mechanism**: Suggests how the brain performs path integration from grid cell activity alone

## Applications

- **Spatial navigation research**: Decoding animal trajectories from neural recordings
- **BCI for navigation**: Brain-computer interfaces for spatial state estimation
- **Neuroscience theory**: Understanding how grid cell population codes represent space
- **Robotics**: Bio-inspired navigation systems using topological representations

## Implementation Considerations

### Data Requirements
- Grid cell population recordings (≥ ~50 cells recommended for reliable TDA)
- Sufficient spatial coverage (animal should explore environment thoroughly)
- Single module identification (cells with similar grid spacing/orientation)

### TDA Parameters
- Persistence threshold: filter out topological noise
- Window size for sliding window analysis
- Choice of distance metric for point cloud construction

### Pitfalls
- **Multiple modules**: If multiple grid modules are mixed, the manifold structure becomes more complex (higher-dimensional torus)
- **Boundary effects**: At environment boundaries, grid cell firing patterns may distort
- **Temporal resolution**: Path lifting requires sufficient temporal sampling to resolve wrapping events
- **Ambiguity**: Path lifting recovers trajectory up to affine transform — absolute position and orientation cannot be determined without additional information

## Related Concepts

- Continuous attractor networks (CANs) for grid cells
- Persistent homology / topological data analysis
- Covering spaces and path lifting in algebraic topology
- Path integration in the entorhinal-hippocampal system
- Neural manifold analysis

## References

- Paper: arXiv:2510.16216 (October 2025, updated July 2026)
- Authors: Yuxing Jared Yao, Iris H. R. Yoon
- Categories: q-bio.NC, math.AT
