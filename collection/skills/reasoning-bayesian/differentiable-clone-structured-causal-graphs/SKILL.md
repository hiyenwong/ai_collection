---
name: differentiable-clone-structured-causal-graphs
description: "Skill for implementing the differentiable Clone-Structured Causal Graph (gradCSCG) algorithm for end-to-end cognitive map learning from raw image sequences, as described in arXiv:2607.12382."
tags: ["neuroscience", "machine learning", "cognitive mapping", "differentiable models", "VQ-VAE"]
related_skills: []
---
## Context
The Clone-Structured Causal Graph (CSCG) algorithm is a normative hippocampus model that learns interpretable cognitive maps from aliased observations. However, CSCG requires a predefined discrete alphabet and its expectation-maximization formulation is not easily combined with neural networks, preventing end-to-end learning from raw sensory input. This skill implements gradCSCG, a fully differentiable reformulation of CSCG coupled with a learned vector-quantized variational autoencoder (VQ-VAE) perceptual front-end, enabling gradient-based training directly from image sequences to learn structured maps.

## Core Methodology
1. **Perceptual Front‑end**: Train a VQ‑VAE to encode raw image sequences into discrete latent representations that serve as the “alphabet” for CSCG.
2. **Differentiable CSCG (gradCSCG)**: Reformulate the CSCG dynamics as a differentiable module that operates on the VQ‑VAE latent sequences, computing soft state transitions and emissions.
3. **Soft Emission Forward Pass**: Allow the map‑learning objective (graph reconstruction) to back‑propagate into the perceptual front‑end via a soft emission distribution over observations.
4. **Loss‑Balancing Mechanisms**: Add auxiliary losses (e.g., commitment loss, codebook diversity loss) to prevent posterior collapse and module collapse during joint training.
5. **Joint Optimization**: Train the VQ‑VAE and gradCSCG end‑to‑end by maximizing the evidence lower bound (ELBO) of the VQ‑VAE plus the graph reconstruction loss, weighted appropriately.
6. **Inference**: After training, use the learned graph adjacency matrix as the cognitive map; decode latent trajectories to retrieve visited locations.

## Implementation Steps
1. **Environment Setup**
   - Install PyTorch, torchvision, and any required libraries.
   - Prepare a dataset of image sequences with known ground‑truth topology (e.g., synthetic grid worlds, MNIST‑based sequences).
2. **VQ‑VAE Architecture**
   - Encoder: convolutional network mapping images to latent vectors.
   - Vector Quantizer: codebook of learnable embeddings; straight‑through estimator for gradients.
   - Decoder: transposed convolutional network reconstructing images from quantized latents.
   - Loss: reconstruction loss + commitment loss + codebook loss.
3. **gradCSCG Module**
   - Represent the cognitive map as a directed graph with nodes corresponding to latent discrete states.
   - Implement differentiable state transitions using a learned transition matrix (softmax over logits).
   - Implement soft emission probabilities: p(x_t | z_t) derived from the VQ‑VAE decoder likelihood.
   - Define the map‑learning objective as the expected log‑likelihood of the observed sequence under the graph model.
4. **Loss Balancing**
   - Add a commitment loss term to encourage the encoder to commit to codebook entries.
   - Add a diversity loss (e.g., orthogonal regularization) to prevent codebook collapse.
   - Optionally add entropy regularization on the transition matrix to avoid degenerate solutions.
5. **Training Loop**
   - For each batch of image sequences:
     a. Encode frames to latent indices via the VQ‑VAE.
     b. Compute reconstruction and commitment losses.
     c. Feed the latent sequence into gradCSCG to compute transition and emission probabilities.
     d. Compute the graph reconstruction loss (negative log likelihood of the sequence under the learned graph).
     e. Combine losses with weighting hyperparameters (λ_recon, λ_commit, λ_diversity, λ_graph).
     f. Backpropagate and update parameters of both VQ‑VAE and gradCSCG.
6. **Evaluation**
   - After training, extract the learned adjacency matrix from gradCSCG.
   - Compare to the ground‑truth graph using edge precision/recall or structural similarity metrics.
   - Optionally, visualize learned trajectories embedded in the graph.

## Pitfalls
- **Posterior Collapse**: The VQ‑VAE may learn to ignore the latent bottleneck, outputting uniform assignments. Mitigate with a sufficiently high commitment loss weight and/or exponential moving average codebook updates.
- **Module Collapse**: gradCSCG may degenerate to a trivial graph (e.g., all‑to‑zero transitions). Use loss‑balancing and monitor the entropy of the transition matrix.
- **Discrete Bottleneck Mismatch**: The number of codebook entries should exceed the expected number of distinct states; too few leads to under‑fitting, too many makes learning unstable.
- **Gradient Signal Weakness**: Early in training, the graph loss may provide weak gradients to the perceptual front‑end; consider curriculum learning or pretraining the VQ‑VAE in isolation.
- **Hardware Limitations**: Training voxel‑wise VQ‑VAE on high‑resolution video can be memory‑intensive; use gradient accumulation or mixed‑precision training.

## Verification
- **Synthetic Grid World**: Train on sequences generated from a known 4‑room grid with aliased observations (e.g., same visual cue for multiple locations). Verify that the recovered adjacency matrix matches the true grid connections with >80% precision and recall.
- **MNIST Image Sequences**: Generate sequences where each location is associated with a randomly sampled MNIST digit (changing per visit). Confirm that the model still recovers the underlying topology despite the changing appearance.
- **Ablation Study**: Remove the VQ‑VAE and feed random one‑hot vectors; performance should drop sharply, demonstrating the necessity of the perceptual front‑end.
- **Loss Visualization**: Track reconstruction, commitment, and graph losses during training; ensure none diverge to zero or explode.

## Activation Keywords
differentiable clone structured causal graphs, gradCSCG, cognitive map learning, VQ-VAE, end‑to‑end map learning from image sequences, hippocampal model, differentiable CSCG, neural cognitive mapping