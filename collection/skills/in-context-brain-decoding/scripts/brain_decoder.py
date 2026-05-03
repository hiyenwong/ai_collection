#!/usr/bin/env python3
"""
In-Context Brain Decoding Implementation

Reference implementation for meta-learning based brain decoding.
This script demonstrates the core concepts from the paper:
"Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding"

Note: This is a conceptual implementation. For production use,
refer to the official implementation at https://github.com/ezacngm/brainCodec
"""

import numpy as np
import torch
import torch.nn as nn
from typing import List, Tuple, Dict


class BrainEncoder(nn.Module):
    """
    Subject-specific brain encoding model.
    Maps visual stimuli to predicted fMRI responses.
    """

    def __init__(self, visual_dim: int, brain_dim: int, hidden_dim: int = 512):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(visual_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, brain_dim),
        )

    def forward(self, visual_features: torch.Tensor) -> torch.Tensor:
        """
        Encode visual features to predicted brain responses.

        Args:
            visual_features: Visual feature vectors [batch, visual_dim]

        Returns:
            predicted_responses: Predicted fMRI responses [batch, brain_dim]
        """
        return self.encoder(visual_features)


class MetaBrainDecoder(nn.Module):
    """
    Meta-learning model for in-context brain decoding.
    Learns to estimate subject-specific encoding models from few examples.
    """

    def __init__(
        self,
        visual_dim: int,
        brain_dim: int,
        context_size: int = 10,
        hidden_dim: int = 512,
    ):
        super().__init__()
        self.visual_dim = visual_dim
        self.brain_dim = brain_dim
        self.context_size = context_size

        # Context encoder for estimating encoding parameters
        self.context_encoder = nn.Sequential(
            nn.Linear(visual_dim + brain_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
        )

        # Encoding parameter predictor
        self.param_predictor = nn.Linear(hidden_dim, visual_dim * brain_dim + brain_dim)

        # Functional inversion network
        self.inversion_network = nn.Sequential(
            nn.Linear(brain_dim + visual_dim * brain_dim + brain_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, visual_dim),
        )

    def estimate_encoder_params(
        self, context_stimuli: torch.Tensor, context_responses: torch.Tensor
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Estimate subject-specific encoding model parameters from context.

        Args:
            context_stimuli: Context visual stimuli [context_size, visual_dim]
            context_responses: Context brain responses [context_size, brain_dim]

        Returns:
            weight_matrix: Estimated encoding weights [brain_dim, visual_dim]
            bias_vector: Estimated encoding bias [brain_dim]
        """
        # Concatenate stimuli and responses
        context_pairs = torch.cat([context_stimuli, context_responses], dim=-1)

        # Encode context
        context_encoded = self.context_encoder(context_pairs)

        # Aggregate across context examples
        context_summary = context_encoded.mean(dim=0)

        # Predict encoding parameters
        params = self.param_predictor(context_summary)

        # Split into weight matrix and bias
        weight_flat = params[: self.visual_dim * self.brain_dim]
        weight_matrix = weight_flat.view(self.brain_dim, self.visual_dim)
        bias_vector = params[self.visual_dim * self.brain_dim :]

        return weight_matrix, bias_vector

    def invert_encoder(
        self,
        brain_responses: torch.Tensor,
        encoder_weight: torch.Tensor,
        encoder_bias: torch.Tensor,
    ) -> torch.Tensor:
        """
        Perform functional inversion to decode visual features.

        Args:
            brain_responses: Observed brain responses [batch, brain_dim]
            encoder_weight: Estimated encoding weights [brain_dim, visual_dim]
            encoder_bias: Estimated encoding bias [brain_dim]

        Returns:
            decoded_visual: Decoded visual features [batch, visual_dim]
        """
        batch_size = brain_responses.shape[0]

        # Flatten encoder parameters for each batch element
        encoder_weight_flat = (
            encoder_weight.flatten().unsqueeze(0).expand(batch_size, -1)
        )
        encoder_bias_expanded = encoder_bias.unsqueeze(0).expand(batch_size, -1)

        # Concatenate brain responses with encoding parameters
        inversion_input = torch.cat(
            [brain_responses, encoder_weight_flat, encoder_bias_expanded], dim=-1
        )

        # Decode visual features
        decoded_visual = self.inversion_network(inversion_input)

        return decoded_visual

    def forward(
        self,
        context_stimuli: torch.Tensor,
        context_responses: torch.Tensor,
        target_responses: torch.Tensor,
    ) -> torch.Tensor:
        """
        Forward pass for in-context brain decoding.

        Args:
            context_stimuli: Context visual stimuli [context_size, visual_dim]
            context_responses: Context brain responses [context_size, brain_dim]
            target_responses: Target brain responses to decode [batch, brain_dim]

        Returns:
            decoded_visual: Decoded visual features [batch, visual_dim]
        """
        # Step 1: Estimate subject-specific encoding parameters
        encoder_weight, encoder_bias = self.estimate_encoder_params(
            context_stimuli, context_responses
        )

        # Step 2: Decode target responses
        decoded_visual = self.invert_encoder(
            target_responses, encoder_weight, encoder_bias
        )

        return decoded_visual


class BrainDecodingPipeline:
    """
    Complete pipeline for in-context brain decoding.
    """

    def __init__(self, meta_model: MetaBrainDecoder, visual_extractor=None):
        self.meta_model = meta_model
        self.visual_extractor = visual_extractor

    def collect_context(
        self, subject_data: Dict, n_examples: int = 10
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Collect context examples for a new subject.

        Args:
            subject_data: Dictionary containing 'images' and 'fmri' data
            n_examples: Number of context examples to collect

        Returns:
            context_stimuli: Visual features [n_examples, visual_dim]
            context_responses: fMRI responses [n_examples, brain_dim]
        """
        indices = np.random.choice(
            len(subject_data["images"]), size=n_examples, replace=False
        )

        context_images = subject_data["images"][indices]
        context_responses = subject_data["fmri"][indices]

        # Extract visual features if extractor is provided
        if self.visual_extractor is not None:
            context_stimuli = self.visual_extractor(context_images)
        else:
            context_stimuli = torch.from_numpy(context_images).float()

        context_responses = torch.from_numpy(context_responses).float()

        return context_stimuli, context_responses

    def decode_subject(
        self,
        context_data: Tuple[torch.Tensor, torch.Tensor],
        target_responses: torch.Tensor,
    ) -> torch.Tensor:
        """
        Decode brain responses for a new subject using in-context learning.

        Args:
            context_data: (context_stimuli, context_responses) tuple
            target_responses: Brain responses to decode [batch, brain_dim]

        Returns:
            decoded_visual: Decoded visual features [batch, visual_dim]
        """
        context_stimuli, context_responses = context_data

        with torch.no_grad():
            decoded_visual = self.meta_model(
                context_stimuli, context_responses, target_responses
            )

        return decoded_visual


def meta_training_step(
    meta_model: MetaBrainDecoder,
    optimizer: torch.optim.Optimizer,
    subject_batch: List[Dict],
    loss_fn: nn.Module,
) -> float:
    """
    Single meta-training step across multiple subjects.

    Args:
        meta_model: The meta-learning model
        optimizer: Optimizer for meta-model
        subject_batch: List of subject data dictionaries
        loss_fn: Loss function

    Returns:
        loss: Training loss value
    """
    meta_model.train()
    optimizer.zero_grad()

    total_loss = 0.0

    for subject_data in subject_batch:
        # Split into context and target
        n_total = len(subject_data["fmri"])
        n_context = min(10, n_total // 2)

        indices = np.random.permutation(n_total)
        context_idx = indices[:n_context]
        target_idx = indices[n_context:]

        context_stimuli = torch.from_numpy(subject_data["stimuli"][context_idx]).float()
        context_responses = torch.from_numpy(subject_data["fmri"][context_idx]).float()
        target_stimuli = torch.from_numpy(subject_data["stimuli"][target_idx]).float()
        target_responses = torch.from_numpy(subject_data["fmri"][target_idx]).float()

        # Forward pass
        decoded = meta_model(context_stimuli, context_responses, target_responses)

        # Compute loss
        loss = loss_fn(decoded, target_stimuli)
        total_loss += loss

    # Backward pass
    total_loss.backward()
    optimizer.step()

    return total_loss.item() / len(subject_batch)


# Example usage
if __name__ == "__main__":
    print("In-Context Brain Decoding Implementation")
    print("=" * 50)
    print("\nThis script demonstrates the core concepts from:")
    print("'Meta-learning In-Context Enables Training-Free")
    print("Cross Subject Brain Decoding' (CVPR 2026)")
    print("\nFor production use, see: https://github.com/ezacngm/brainCodec")

    # Model dimensions
    visual_dim = 512  # e.g., CLIP visual features
    brain_dim = 1000  # Number of voxels

    # Initialize model
    model = MetaBrainDecoder(visual_dim, brain_dim)
    print("\nModel initialized:")
    print(f"  Visual dimension: {visual_dim}")
    print(f"  Brain dimension: {brain_dim}")
    print(f"  Total parameters: {sum(p.numel() for p in model.parameters()):,}")
