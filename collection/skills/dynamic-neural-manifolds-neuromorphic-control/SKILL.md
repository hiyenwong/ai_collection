---
name: dynamic-neural-manifolds-neuromorphic-control
description: "Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware. Implements a ring attractor spiking network on the SpiNNaker 2 chip where sensory-modulated heterogeneous inhibition, multiplicative gain, and transient currents drive rapid subspace rotations and fine-grained trajectory control within low-dimensional neural manifolds. Validated with a robotic maze-navigation simulation. Provides an explainable, neuroscience-grounded framework for mapping world-model plans onto motor control via manifold geometry. Applicable to: neuromorphic control, neural manifolds, ring attractor networks, subspace rotation, closed-loop SNN, SpiNNaker 2, low-dimensional neural dynamics, explainable neuromorphic architectures, behavioral switching."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2607.07373"
  published: "2026-07-08"
  authors: "Oskar von Seeler, Christian Tetzlaff, Andrew Lehr"
  tags: [neuromorphic-computing, spiking-neural-networks, neural-manifolds, ring-attractor, subspace-rotation, closed-loop-control, spinnaker2, low-dimensional-dynamics, behavioral-switching, explainable-ai]
---

# Dynamic Neural Manifolds for Flexible Closed-Loop Control on Neuromorphic Hardware

**arXiv**: [2607.07373](https://arxiv.org/abs/2607.07373) | **Published**: 2026-07-08 | **Category**: cs.NE

## Core Contribution

Proposes an **explainable parameterization of neural activity as a low-dimensional manifold** whose geometry is directly controllable by simple circuit mechanisms, and demonstrates a **real-time closed-loop implementation on the SpiNNaker 2 neuromorphic chip**. By letting sensory input modulate heterogeneous inhibition, gain, and transient currents, the architecture drives **rapid subspace rotations** (behavior switching) and **fine-grained trajectory control** (within-behavior execution). Validated via a robotic maze simulation where an agent uses sensory feedback to reconfigure its manifold geometry.

## Why Neural Manifolds

A neural manifold is the geometric manifestation of a population's progression through a low-dimensional state space. Sequential activity in brain/spinal cord evolves along dynamic, low-dimensional manifolds. Specific circuit mechanisms map manifold geometry to behavior:
- **Heterogeneous inhibition** → subspace reorientation (rotate sequence into new hyperplanes to switch behavioral states)
- **Gain modulation + transient currents** → direct control of trajectory velocity and shape

## Architecture: Ring Attractor Spiking Network

Implemented as a **ring network with asymmetric recurrent connectivity**, forming a stable bump of activity that progresses along the ring → oscillatory sequences (Figure 2).

### Three Control Neurons

1. **Speed control** — multiplicative gain `S` scales how fast the bump travels
2. **Shape control** — additive current `I` changes bump width
3. **Selection control** — subspace inhibition `p_inh` silences subsets of neurons, steering the trajectory into a target subspace

### Control Mechanisms (verified on SpiNNaker 2)

| Mechanism | Effect on manifold |
|---|---|
| Multiplicative gain `S` ↑ | Faster bump traversal (trajectory speed) |
| Additive current `I` | Larger bump size during subspace (trajectory shape) |
| Subspace inhibition `p_inh` | Rotates activity into a different subspace (behavior switch), sequence dynamics preserved |
| Combined | Multiple subspaces at increasing rotation counts per unit time |

- Subspace rotation verified by **first principal angle** between subspaces (matches analytical solution)
- Selective inhibition: 80% subspace inhibition leaves sequential dynamics + behavioral state representation intact

## SpiNNaker 2 Implementation Details

- Original model is **rate-based**; SpiNNaker 2 is spike-optimized → added a **spike-based communication layer**: rate `r` treated as probability of spiking in current timestep (probabilistic rate→spike)
- Introduced **50% connection sparsity** (weights scaled 2× to compensate) to cut incoming spikes per neuron
- Used **circulant weight matrix** structure → store only one row + 1-bit sparsity mask (memory efficient)
- Host interface streams control parameters in, receives output spikes, computes motor commands
- Runtime scales with: number of neurons, connection sparsity, number of timesteps

## Closed-Loop Maze Validation

- Environment: maze from `labmaze` library; agent moves in real-valued steps, can jump hurdles
- Three subspaces encode three movements: forward, curved-forward, turn
- Agent has a **pre-learned world model / plan**; the framework **translates plan → manifold control parameters** (speed, shape, selection)
- Ring-network spikes → readout → motor speeds for two wheels
- Result: agent navigates maze successfully via closed-loop sensory feedback reconfiguring manifold geometry

## When to Use This Skill

- Building neuromorphic / SNN controllers for autonomous agents
- Needing **explainable** neural computation (manifold geometry ↔ behavior mapping)
- Closed-loop control where sensory feedback must reconfigure internal dynamics in real time
- Mapping a high-level plan/world-model onto low-level motor primitives
- Ring-attractor or bump-attractor based sequential generation on constrained hardware

## Implementation Checklist

1. Build ring network with asymmetric recurrent weights (circulant + sparse)
2. Implement 3 control inputs: gain (speed), current (shape), inhibition mask (selection)
3. Convert rate→spike probabilistically; keep spike-based inter-neuron communication
4. Assign neuron groups to subspaces via bitmask (1 = in subspace)
5. Decode bump position / spike counts → readout → motor commands
6. Close the loop: environment feedback → update control params → re-steering
7. Verify subspace rotations via principal-angle analysis against analytical solution

## Biological & Systems Significance

- Bridges neuroscience (neural manifolds in cortex/spinal cord) and neuromorphic engineering
- Simple circuit mechanisms (gain, inhibition, transient input) readily implement sequence control
- Offers a substrate for investigating biological neural dynamics and for humanoid/robotic control with many DOF
- Framework is general: any plan can be translated into manifold representation suitable for spiking hardware

## Pitfalls

- On-chip SRAM is limited: circulant+sparse storage needed; max execution time bounded by local memory
- Higher connectivity → higher runtime per timestep on SpiNNaker 2 (benchmark before scaling)
- Plan was manually created per maze in the paper — learning the plan from observations is future work
- Ring network is powerful but simplified; real networks use dendrites in 3D (extension noted)
- Rate→spike conversion introduces sampling noise; calibrate spike probability to match rate
