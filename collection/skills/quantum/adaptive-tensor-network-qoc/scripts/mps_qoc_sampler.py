#!/usr/bin/env python3
"""
Adaptive Tensor Network Sampling for Quantum Optimal Control (MPS/TT).
Based on arXiv:2604.24467 - Adaptive Tensor Network Sampling for Quantum Optimal Control

Gradient-free matrix product state / tensor train sampling heuristic for
discrete quantum optimal control. The MPS defines a score function over the
space of discrete control parameters, inducing a sampling distribution that
is iteratively refined.
"""

import numpy as np
from typing import Callable, Tuple


class MPSSampler:
    """Matrix Product State / Tensor Train sampler for discrete control sequences."""

    def __init__(self, n_sites: int, local_dim: int, bond_dim: int):
        """
        Initialize MPS sampler.

        Args:
            n_sites: Number of control steps (time discretization)
            local_dim: Number of discrete control values per site
            bond_dim: MPS bond dimension (controls expressivity)
        """
        self.n_sites = n_sites
        self.local_dim = local_dim
        self.bond_dim = bond_dim

        # Initialize random tensors with appropriate shapes
        self.tensors = []
        for i in range(n_sites):
            d_left = 1 if i == 0 else bond_dim
            d_right = 1 if i == n_sites - 1 else bond_dim
            # Shape: (d_left, local_dim, d_right)
            tensor = np.random.randn(d_left, local_dim, d_right)
            self.tensors.append(tensor)

    def log_probability(self, sequence: np.ndarray) -> float:
        """Compute log P(sequence) under current MPS."""
        left_vec = np.array([1.0])  # shape (1,)

        for i, s in enumerate(sequence):
            # Contract left_vec with tensor at site i, index s
            tensor_slice = self.tensors[i][:, int(s), :]  # (d_left, d_right)
            left_vec = left_vec @ tensor_slice  # (d_right,)

        # Normalize
        norm = np.linalg.norm(left_vec)
        if norm > 0:
            return 2 * np.log(norm)
        return -np.inf

    def sample(self, n_samples: int = 1) -> np.ndarray:
        """Sample control sequences from MPS distribution."""
        sequences = []
        for _ in range(n_samples):
            seq = []
            left_vec = np.array([1.0])  # shape (d_left,) starts as (1,)

            for i in range(self.n_sites):
                tensor_i = self.tensors[i]
                d_left_i = tensor_i.shape[0]
                tensor_i.shape[2]

                # Ensure left_vec has correct shape
                if left_vec.shape[0] != d_left_i:
                    # Pad or truncate
                    new_vec = np.zeros(d_left_i)
                    new_vec[: min(len(left_vec), d_left_i)] = left_vec[
                        : min(len(left_vec), d_left_i)
                    ]
                    left_vec = new_vec

                # Contract: left_vec (d_left,) with tensor (d_left, local_dim, d_right)
                # Result: (local_dim, d_right)
                contracted = np.einsum("l,lmd->md", left_vec, tensor_i)

                # Probability over local_dim by summing squares over d_right
                probs = np.sum(contracted**2, axis=1)  # (local_dim,)
                probs = np.maximum(probs, 0)
                total = probs.sum()
                if total > 0:
                    probs /= total
                else:
                    probs = np.ones(self.local_dim) / self.local_dim

                s = np.random.choice(self.local_dim, p=probs)
                seq.append(s)

                left_vec = contracted[s, :]  # (d_right,) becomes next left_vec

            sequences.append(np.array(seq))

        return np.array(sequences)

    def update(
        self,
        sequences: np.ndarray,
        scores: np.ndarray,
        learning_rate: float = 0.01,
        top_fraction: float = 0.2,
    ):
        """
        Update MPS tensors by selecting top-performing sequences.

        Args:
            sequences: Array of sampled sequences, shape (n_samples, n_sites)
            scores: Array of objective scores, shape (n_samples,)
            learning_rate: Learning rate for tensor updates
            top_fraction: Fraction of top sequences to use for update
        """
        n_samples = len(scores)
        n_top = max(1, int(n_samples * top_fraction))

        # Select top sequences
        top_indices = np.argsort(scores)[-n_top:]
        top_seqs = sequences[top_indices]

        # Compute target distribution from top sequences (one-hot empirical)
        for i in range(self.n_sites):
            d_left = 1 if i == 0 else self.bond_dim
            d_right = 1 if i == self.n_sites - 1 else self.bond_dim

            # Build empirical target tensor from top sequences
            target = np.zeros((d_left, self.local_dim, d_right))
            for seq in top_seqs:
                # Simplified: assign unit weight to observed configurations
                # In practice, use SVD-based update from empirical distribution
                target[0, int(seq[i]), 0] += 1.0
            target /= target.sum()

            # Gradient step toward target
            self.tensors[i] += learning_rate * (target - self.tensors[i])

            # Normalize
            norm = np.linalg.norm(self.tensors[i])
            if norm > 0:
                self.tensors[i] /= norm


def run_qoc_optimization(
    objective_fn: Callable[[np.ndarray], float],
    n_sites: int = 10,
    local_dim: int = 4,
    bond_dim: int = 8,
    n_iterations: int = 50,
    n_samples: int = 100,
    learning_rate: float = 0.05,
    verbose: bool = True,
) -> Tuple[np.ndarray, float]:
    """
    Run quantum optimal control optimization using MPS/TT sampling.

    Args:
        objective_fn: Function that takes a control sequence and returns a score (higher=better)
        n_sites: Number of control steps
        local_dim: Number of discrete control values
        bond_dim: MPS bond dimension
        n_iterations: Number of optimization iterations
        n_samples: Number of sequences to sample per iteration
        learning_rate: Learning rate for MPS updates
        verbose: Print progress

    Returns:
        best_sequence: Best control sequence found
        best_score: Best score achieved
    """
    sampler = MPSSampler(n_sites, local_dim, bond_dim)

    best_sequence = None
    best_score = -np.inf
    history = []

    for iteration in range(n_iterations):
        # Sample candidate sequences
        sequences = sampler.sample(n_samples)

        # Evaluate objective
        scores = np.array([objective_fn(seq) for seq in sequences])

        # Track best
        idx = np.argmax(scores)
        if scores[idx] > best_score:
            best_score = scores[idx]
            best_sequence = sequences[idx].copy()

        history.append(best_score)

        # Update MPS toward better sequences
        sampler.update(sequences, scores, learning_rate=learning_rate)

        if verbose and (iteration % 10 == 0 or iteration == n_iterations - 1):
            print(
                f"Iteration {iteration:3d} | Best score: {best_score:.4f} | "
                f"Mean score: {scores.mean():.4f}"
            )

    return best_sequence, best_score


if __name__ == "__main__":
    # Example: Optimize a simple quantum state transfer objective
    # Target: maximize overlap with |1> state starting from |0>
    # Simplified 2D Bloch sphere objective

    def simple_state_transfer_objective(seq: np.ndarray) -> float:
        """Simulated objective: maximize population transfer."""
        # Simulated dynamics: each control step rotates the state
        theta = 0.0
        for s in seq:
            # Control values map to rotation angles
            angle = (s / 3.0) * np.pi
            theta += angle

        # Overlap with target state
        return np.sin(theta / 2) ** 2

    print("MPS/TT Sampling for Quantum Optimal Control")
    print("=" * 50)

    best_seq, best_score = run_qoc_optimization(
        objective_fn=simple_state_transfer_objective,
        n_sites=8,
        local_dim=4,
        bond_dim=4,
        n_iterations=30,
        n_samples=50,
        learning_rate=0.1,
    )

    print(f"\nBest sequence: {best_seq}")
    print(f"Best score: {best_score:.4f}")
