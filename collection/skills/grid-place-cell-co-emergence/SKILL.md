---
name: grid-place-cell-co-emergence
description: "First unified recurrent network model implementing Dale's Law that achieves co-emergence of grid cells and place fields from a single sensory-prediction objective without supervision of either cell type. Based on arXiv:2605.21356."
---

# A Simple Model of Co-Emergence of Grid and Place Fields

**arXiv**: 2605.21356 | **Authors**: Zhaoze Wang, Genela Morris, Dori Derdikman, Pratik Chaudhari, Vijay Balasubramanian

First single-objective recurrent network model in which grid cells (medial entorhinal cortex) and place cells (hippocampus) co-emerge without supervision of either type, addressing the chicken-and-egg problem of spatial representation development.

## Key Contributions

1. **First co-emergence model**: Unified recurrent network with Dale's Law trained on sensory-prediction objective produces both grid and place fields simultaneously
2. **1,000+ config robustness**: Both spatial codes coexist across all tested training configurations; balance controlled by sensory noise/masking
3. **Two complementary pressures**: (1) Sensory reconstruction/pattern completion → place fields, (2) Motion prediction/path integration → grid fields
4. **Qualitative experimental reproduction**: Grid fragmentation, wall-removal merging, lattice alignment, 3D bat fields, developmental ordering (place cells precede grid cells)

## Method

### Network Architecture
- Recurrent neural network with Dale's Law (each neuron is either excitatory or inhibitory)
- Trained via sensory prediction: predict next sensory observation from masked previous observations and egocentric motion
- No spatial labels, no place/grid cell supervision

### Training Objective
- **Reconstruction pressure**: Correct errors and reconstruct masked components of sensory observations
- **Prediction pressure**: Predict next sensory state during navigation
- The balance between these two pressures determines the grid vs. place field distribution

### Validation
- Tested across 1,000 different training configurations (varying noise, masking, network size)
- Compared against experimental data: hairpin maze grids, wall removal, connected rooms, 3D bat flight
- Developmental trajectory analysis: place cells emerge before grid cells

## Key Findings

### Grid Cells for Path Integration
- Grid-like firing patterns emerge from the motion prediction (path integration) objective
- Hexagonal grid tessellation of spatial environment
- Phase relationships and scale organization match experimental observations

### Place Cells for Pattern Completion
- Place-like fields emerge from the sensory reconstruction objective
- Sparse, localized firing in specific spatial locations
- Remapping properties consistent with hippocampal place cells

### Emergent Properties
- Grid fragmentation in hairpin mazes reproduces experimental findings
- Grid field merging after wall removal matches observations
- Lattice alignment across connected rooms
- 3D volumetric grid fields in simulated bat flight
- Developmental order: place cells before grid cells

## When to Use

- Modeling spatial navigation and hippocampal-entorhinal circuits
- Understanding neural code development without supervision
- Studying grid/place cell interactions and co-emergence
- Exploring sensory-prediction as a unified learning objective
- Developing biologically-plausible spatial representations in AI

## Related Skills

- [[platonic-representations-brain]] - Cross-subject neural geometry alignment
- [[hippocampal-entorhinal-world-model]] - HPC-MEC inspired hierarchical world models
- [[grid-cell-normative-theory-review]] - Normative theory review of grid cell representations

## Activation Keywords

grid cells, place cells, co-emergence, sensory prediction, path integration, entorhinal cortex, hippocampus, Dale's Law, spatial navigation, recurrent neural network, self-supervised spatial learning, grid field development, hippocampal place fields, 3D grid fields, neural development ordering
