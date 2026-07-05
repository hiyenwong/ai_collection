#!/usr/bin/env python3
"""
QAOA Portfolio Optimization Example

Basic implementation using Qiskit for portfolio selection.
"""

import numpy as np
from typing import List, Dict


# Mock implementation (requires qiskit-optimization for real use)
def portfolio_qaoa(
    expected_returns: List[float],
    covariance: np.ndarray,
    risk_penalty: float = 0.5,
    max_assets: int = None,
) -> Dict:
    """
    Solve portfolio optimization using QAOA (mock implementation).

    Args:
        expected_returns: Expected return for each asset
        covariance: Covariance matrix of asset returns
        risk_penalty: Risk aversion parameter (λ)
        max_assets: Cardinality constraint (optional)

    Returns:
        Dictionary with selected assets and metrics
    """
    n_assets = len(expected_returns)

    # Build QUBO matrix
    # Q_ij = -μ_i + λ Σ_ij
    # For diagonal: Q_ii = -μ_i + λ Σ_ii
    Q = np.zeros((n_assets, n_assets))

    for i in range(n_assets):
        Q[i, i] = -expected_returns[i] + risk_penalty * covariance[i, i]
        for j in range(i + 1, n_assets):
            Q[i, j] = risk_penalty * covariance[i, j]
            Q[j, i] = Q[i, j]  # Symmetric

    # Mock solution: select assets with highest expected return
    # In real implementation, this would use QAOA
    sorted_indices = np.argsort(expected_returns)[::-1]

    if max_assets:
        selected = sorted_indices[:max_assets]
    else:
        selected = sorted_indices[: int(n_assets * 0.3)]  # Default: 30%

    # Calculate metrics
    portfolio_return = sum(expected_returns[i] for i in selected)
    portfolio_risk = np.sqrt(sum(covariance[i, j] for i in selected for j in selected))

    return {
        "selected_assets": list(selected),
        "expected_return": portfolio_return,
        "portfolio_risk": portfolio_risk,
        "sharpe_ratio": portfolio_return / portfolio_risk if portfolio_risk > 0 else 0,
        "qubo_matrix": Q,
    }


def main():
    """Example usage."""
    # Sample data: 5 assets
    returns = [0.12, 0.10, 0.08, 0.15, 0.09]  # Expected annual returns
    cov = np.array(
        [
            [0.04, 0.02, 0.01, 0.03, 0.02],
            [0.02, 0.03, 0.01, 0.02, 0.01],
            [0.01, 0.01, 0.02, 0.01, 0.01],
            [0.03, 0.02, 0.01, 0.05, 0.02],
            [0.02, 0.01, 0.01, 0.02, 0.03],
        ]
    )

    result = portfolio_qaoa(returns, cov, risk_penalty=0.5, max_assets=3)

    print("=== QAOA Portfolio Optimization ===")
    print(f"Selected assets: {result['selected_assets']}")
    print(f"Expected return: {result['expected_return']:.2%}")
    print(f"Portfolio risk: {result['portfolio_risk']:.2%}")
    print(f"Sharpe ratio: {result['sharpe_ratio']:.2f}")

    print("\nQUBO Matrix:")
    print(result["qubo_matrix"])


if __name__ == "__main__":
    main()
