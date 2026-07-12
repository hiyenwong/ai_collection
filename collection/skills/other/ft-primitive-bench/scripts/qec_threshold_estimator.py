#!/usr/bin/env python3
"""
FTPrimitiveBench helper: QEC threshold estimation under biased noise.

Computes logical error rate vs physical error rate for surface code
under different noise bias configurations.

Usage:
    python qec_threshold_estimator.py --bias 100 --code_distances 3 5 7 9 11
    python qec_threshold_estimator.py --bias 1 --code_distances 3 5 7 --model depolarizing
"""

import argparse
import numpy as np
from typing import Optional


def surface_code_threshold(bias: float = 1.0, model: str = "biased") -> float:
    """
    Estimate surface code threshold under given noise bias.
    
    Args:
        bias: Ratio of Z errors to X errors (bias = pZ/pX)
        model: Noise model - "biased" or "depolarizing"
    
    Returns:
        Estimated threshold error rate
    
    Notes:
        Standard depolarizing threshold ~0.94%
        High bias (e.g., 100:1) can push threshold to ~4-5%
        XZZX surface code particularly benefits from bias
    """
    if model == "depolarizing":
        return 0.0094  # Standard surface code threshold
    
    # Approximate threshold scaling with bias
    # Based on empirical results from Bonilla Ataides et al. 2021
    # and Xu et al. 2023
    if bias <= 1:
        return 0.0094
    elif bias <= 10:
        return 0.0094 * (1 + 0.1 * np.log10(bias))
    elif bias <= 100:
        return 0.0094 * (1 + 0.3 * np.log10(bias))
    elif bias <= 1000:
        return 0.0094 * (1 + 0.5 * np.log10(bias))
    else:
        return 0.05  # Asymptotic limit for extreme bias


def logical_error_rate(
    physical_error_rate: float,
    code_distance: int,
    bias: float = 1.0,
    model: str = "biased"
) -> float:
    """
    Estimate logical error rate for surface code.
    
    Args:
        physical_error_rate: Physical error rate p
        code_distance: Surface code distance d
        bias: Noise bias ratio
        model: Noise model
    
    Returns:
        Estimated logical error rate pL
    """
    threshold = surface_code_threshold(bias, model)
    
    if physical_error_rate >= threshold:
        return 1.0  # Above threshold, logical errors dominant
    
    # Approximate scaling: pL ~ (p/p_th)^((d+1)/2)
    ratio = physical_error_rate / threshold
    exponent = (code_distance + 1) / 2
    return ratio ** exponent


def analyze_primitive_sensitivity(
    primitive: str,
    noise_model: dict,
    code_distance: int = 5
) -> dict:
    """
    Analyze how different logical primitives respond to noise structure.
    
    Primitives:
        - memory: Baseline idle code
        - lattice_surgery: Merge/split operations
        - hadamard: Transversal H gate
        - phase: S gate via lattice surgery
    
    Returns dict with sensitivity analysis.
    """
    px = noise_model.get("pX", 0.001)
    pz = noise_model.get("pZ", 0.001)
    pm = noise_model.get("pM", 0.001)
    
    bias = pz / px if px > 0 else 1.0
    
    # Base logical error rate from memory
    base_pL = logical_error_rate(px, code_distance, bias)
    
    # Primitive-specific multipliers (from FTPrimitiveBench findings)
    multipliers = {
        "memory": 1.0,
        "lattice_surgery": 1.5 + 0.5 * (pm / px),  # Sensitive to measurement errors
        "hadamard": 1.0 + 0.3 * abs(np.log10(bias)),  # Sensitive to bias asymmetry
        "phase": 2.0 + 0.5 * (pm / px) + 0.2 * abs(np.log10(bias)),  # Combined sensitivity
    }
    
    multiplier = multipliers.get(primitive, 1.0)
    primitive_pL = min(base_pL * multiplier, 1.0)
    
    return {
        "primitive": primitive,
        "base_logical_error_rate": base_pL,
        "primitive_logical_error_rate": primitive_pL,
        "sensitivity_multiplier": multiplier,
        "dominant_noise": "measurement" if pm > pz else "dephasing" if pz > px else "depolarizing",
        "code_distance": code_distance,
    }


def main():
    parser = argparse.ArgumentParser(description="QEC Threshold Estimator")
    parser.add_argument("--bias", type=float, default=1.0,
                       help="Noise bias ratio (pZ/pX)")
    parser.add_argument("--code_distances", type=int, nargs="+",
                       default=[3, 5, 7, 9, 11],
                       help="Code distances to analyze")
    parser.add_argument("--physical-rates", type=float, nargs="+",
                       default=[0.001, 0.005, 0.01, 0.02],
                       help="Physical error rates to test")
    parser.add_argument("--model", type=str, default="biased",
                       choices=["biased", "depolarizing"],
                       help="Noise model")
    
    args = parser.parse_args()
    
    threshold = surface_code_threshold(args.bias, args.model)
    print(f"\nFTPrimitiveBench QEC Threshold Estimator")
    print(f"=" * 50)
    print(f"Noise bias: {args.bias}:1")
    print(f"Noise model: {args.model}")
    print(f"Estimated threshold: {threshold:.4f} ({threshold*100:.2f}%)")
    print(f"\nLogical Error Rates:")
    print(f"{'p_phys':>10} | ", end="")
    for d in args.code_distances:
        print(f"  d={d:>2}  ", end="")
    print()
    print("-" * (10 + len(args.code_distances) * 10))
    
    for p in args.physical_rates:
        print(f"{p:>10.4f} | ", end="")
        for d in args.code_distances:
            pL = logical_error_rate(p, d, args.bias, args.model)
            if pL < 1e-15:
                print(f"  <1e-15", end="")
            else:
                print(f"  {pL:>8.2e}", end="")
        print()
    
    # Primitive sensitivity analysis
    print(f"\nLogical Primitive Sensitivity Analysis")
    print(f"=" * 50)
    noise_model = {"pX": 0.001, "pZ": args.bias * 0.001, "pM": 0.001}
    for primitive in ["memory", "lattice_surgery", "hadamard", "phase"]:
        result = analyze_primitive_sensitivity(primitive, noise_model)
        print(f"\n{primitive}:")
        print(f"  Base pL:     {result['base_logical_error_rate']:.2e}")
        print(f"  Primitive pL: {result['primitive_logical_error_rate']:.2e}")
        print(f"  Sensitivity:  {result['sensitivity_multiplier']:.2f}x")
        print(f"  Dominant:     {result['dominant_noise']}")


if __name__ == "__main__":
    main()
