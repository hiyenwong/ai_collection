"""Quantum cognition: detect contextuality in cognitive measurement data."""

import numpy as np
from typing import Tuple


def chsh_test(
    E_ab: float, E_ab_p: float, E_ap_b: float, E_ap_bp: float
) -> Tuple[float, bool]:
    """CHSH inequality test for contextuality.
    Returns (S_value, is_contextual) where S > 2 indicates contextuality.
    Quantum bound: S <= 2*sqrt(2) (Tsirelson bound)."""
    S = abs(E_ab - E_ab_p + E_ap_b + E_ap_bp)
    return S, S > 2.0


def quantum_interference(p_a: float, p_b: float, theta: float) -> float:
    """Compute quantum probability with interference.
    Classical: p = p_A + p_B
    Quantum: p = p_A + p_B + 2*sqrt(p_A*p_B)*cos(theta)"""
    return p_a + p_b + 2 * np.sqrt(p_a * p_b) * np.cos(theta)


def order_effect_noncommutativity(
    P_A: np.ndarray, P_B: np.ndarray, psi: np.ndarray
) -> Tuple[float, float]:
    """Test non-commutativity of cognitive measurements.
    Returns (P_AB, P_BA) — different values indicate order effects."""
    P_AB = np.linalg.norm(P_B @ P_A @ psi) ** 2
    P_BA = np.linalg.norm(P_A @ P_B @ psi) ** 2
    return P_AB, P_BA


def mental_state_evolution(H: np.ndarray, psi_0: np.ndarray, t: float) -> np.ndarray:
    """Unitary evolution of mental state: |psi(t)> = exp(-iHt)|psi(0)>"""
    from scipy.linalg import expm

    U = expm(-1j * H * t)
    return U @ psi_0


def coherence_time_analysis(T1: float, T2: float, window_ms: float = 200.0) -> dict:
    """Analyze coherence times for biological quantum systems.
    Returns coherence metrics relative to behavioral window."""
    return {
        "T1_ns": T1 * 1e9,
        "T2_ms": T2 * 1000,
        "window_ms": window_ms,
        "covers_window": T2 * 1000 >= window_ms,
        "T2_ratio": T2 / T1 if T1 > 0 else float("inf"),
    }
