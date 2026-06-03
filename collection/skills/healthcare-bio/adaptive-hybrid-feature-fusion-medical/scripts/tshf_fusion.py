"""Temperature-Scaled Hybrid Fusion (TSHF) for Quantum-Classical Medical Classification.

Implementation of the TSHF methodology from arXiv:2604.22903.

Three fusion strategies:
  - SHF: Static Hybrid Fusion (offline extraction + concat)
  - DHF: Dynamic Hybrid Fusion (end-to-end joint training)
  - TSHF: Temperature-Scaled Hybrid Fusion (learnable temperature scalars)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class TSHFFusion(nn.Module):
    """Temperature-Scaled Hybrid Fusion module.

    Applies learnable temperature scaling to each branch's features
    before concatenation, enabling dynamic gradient balancing.
    """

    def __init__(
        self,
        dim_classical: int,
        dim_quantum: int,
        init_temp_c: float = 1.0,
        init_temp_q: float = 1.0,
    ):
        super().__init__()
        self.log_tau_c = nn.Parameter(torch.tensor(init_temp_c).log())
        self.log_tau_q = nn.Parameter(torch.tensor(init_temp_q).log())
        self.dim_out = dim_classical + dim_quantum

    @property
    def tau_c(self):
        return torch.exp(self.log_tau_c)

    @property
    def tau_q(self):
        return torch.exp(self.log_tau_q)

    def forward(self, f_c: torch.Tensor, f_q: torch.Tensor) -> torch.Tensor:
        """Scale features by inverse temperature and concatenate."""
        f_c_scaled = f_c / self.tau_c
        f_q_scaled = f_q / self.tau_q
        return torch.cat([f_c_scaled, f_q_scaled], dim=-1)


class DHFFusion(nn.Module):
    """Dynamic Hybrid Fusion — simple concat, end-to-end training."""

    def __init__(self, dim_classical: int, dim_quantum: int):
        super().__init__()
        self.dim_out = dim_classical + dim_quantum

    def forward(self, f_c: torch.Tensor, f_q: torch.Tensor) -> torch.Tensor:
        return torch.cat([f_c, f_q], dim=-1)


class SHFFusion(nn.Module):
    """Static Hybrid Fusion — offline extraction simulation."""

    def __init__(self, dim_classical: int, dim_quantum: int):
        super().__init__()
        self.dim_out = dim_classical + dim_quantum

    def forward(self, f_c: torch.Tensor, f_q: torch.Tensor) -> torch.Tensor:
        return torch.cat([f_c.detach(), f_q.detach()], dim=-1)


class HybridQuantumClassicalClassifier(nn.Module):
    """Full dual-branch hybrid classifier with configurable fusion strategy.

    Args:
        strategy: 'shf', 'dhf', or 'tshf'
        dim_classical: feature dimension of classical branch
        dim_quantum: feature dimension of quantum branch
        num_classes: number of output classes
    """

    def __init__(
        self,
        dim_classical: int = 512,
        dim_quantum: int = 16,
        num_classes: int = 2,
        strategy: str = "tshf",
    ):
        super().__init__()

        # Placeholder classical backbone (flattened 28x28=784 input)
        self.classical_backbone = nn.Sequential(
            nn.Linear(28 * 28, 512),
            nn.ReLU(),
            nn.Linear(512, dim_classical),
        )

        # Placeholder quantum circuit encoder
        self.quantum_encoder = nn.Sequential(
            nn.Linear(28 * 28, 64),
            nn.ReLU(),
            nn.Linear(64, dim_quantum),
        )

        if strategy == "tshf":
            self.fusion = TSHFFusion(dim_classical, dim_quantum)
        elif strategy == "dhf":
            self.fusion = DHFFusion(dim_classical, dim_quantum)
        elif strategy == "shf":
            self.fusion = SHFFusion(dim_classical, dim_quantum)
        else:
            raise ValueError(f"Unknown strategy: {strategy}")

        self.classifier = nn.Sequential(
            nn.Linear(self.fusion.dim_out, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        f_c = self.classical_backbone(x.view(x.size(0), -1).float())
        f_q = self.quantum_encoder(x.view(x.size(0), -1).float())
        fused = self.fusion(f_c, f_q)
        return self.classifier(fused)


def train_epoch(model: nn.Module, loader, optimizer, device="cpu"):
    """Single training epoch."""
    model.train()
    total_loss, correct, total = 0.0, 0, 0
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        logits = model(x)
        loss = F.cross_entropy(logits, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * x.size(0)
        correct += (logits.argmax(1) == y).sum().item()
        total += x.size(0)
    return total_loss / total, correct / total


def print_fusion_comparison(model_tshf, model_dhf, model_shf):
    """Print temperature values from TSHF model for analysis."""
    if isinstance(model_tshf.fusion, TSHFFusion):
        print(
            f"TSHF temperatures: tau_c={model_tshf.fusion.tau_c.item():.4f}, "
            f"tau_q={model_tshf.fusion.tau_q.item():.4f}"
        )


if __name__ == "__main__":
    # Quick test with synthetic data
    print("Testing TSHF fusion strategies...")

    torch.manual_seed(42)
    batch_size = 8
    x = torch.randn(batch_size, 1, 28, 28)  # Mini grayscale images
    y = torch.randint(0, 2, (batch_size,))

    for strategy in ["shf", "dhf", "tshf"]:
        model = HybridQuantumClassicalClassifier(strategy=strategy)
        optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

        for epoch in range(10):
            loss, acc = train_epoch(model, [(x, y)], optimizer)

        print(f"\n{strategy.upper()}: loss={loss:.4f}, acc={acc:.4f}")
        if strategy == "tshf":
            print_fusion_comparison(model, None, None)

    print("\nAll strategies tested successfully.")
