#!/usr/bin/env python3
"""
QBalance-inspired workflow optimizer helper.
Evaluates quantum compilation strategies using survival-product error proxy
and Pareto-optimal selection.
"""

import argparse
import json
import math


def survival_product_error_proxy(gate_error_rates):
    """Compute survival-product error proxy: product of (1 - error_rate) for all gates."""
    proxy = 1.0
    for rate in gate_error_rates:
        proxy *= (1.0 - rate)
    return proxy


def weighted_objective(fidelity, cost, time_sec, reproducibility, weights=None):
    """Compute weighted objective score."""
    w = weights or {"fidelity": 0.4, "cost": 0.2, "time": 0.2, "reproducibility": 0.2}
    return w["fidelity"] * fidelity - w["cost"] * cost - w["time"] * time_sec + w["reproducibility"] * reproducibility


def pareto_select(strategies):
    """Return non-dominated strategies from evaluation results."""
    pareto = []
    for i, s1 in enumerate(strategies):
        dominated = False
        for j, s2 in enumerate(strategies):
            if i == j:
                continue
            all_geq = all(s2.get(k, 0) >= s1.get(k, 0) for k in ["fidelity", "reproducibility"])
            all_geq = all_geq and all(s2.get(k, 0) <= s1.get(k, 0) for k in ["cost", "time_sec"])
            any_better = (
                any(s2.get(k, 0) > s1.get(k, 0) for k in ["fidelity", "reproducibility"]) or
                any(s2.get(k, 0) < s1.get(k, 0) for k in ["cost", "time_sec"])
            )
            if all_geq and any_better:
                dominated = True
                break
        if not dominated:
            pareto.append(s1)
    return pareto


def evaluate_strategies(gate_error_rates, n_gates, strategies=None):
    """Evaluate compilation strategies given circuit characteristics."""
    strategies = strategies or ["baseline", "sabre", "dd_protected", "zne", "full"]

    strategy_params = {
        "baseline": {"fidelity_mod": 1.0, "cost_mod": 1.0, "time_mod": 1.0, "repro_mod": 1.0},
        "sabre": {"fidelity_mod": 1.1, "cost_mod": 1.2, "time_mod": 1.5, "repro_mod": 1.1},
        "dd_protected": {"fidelity_mod": 1.3, "cost_mod": 1.5, "time_mod": 2.0, "repro_mod": 1.2},
        "zne": {"fidelity_mod": 1.5, "cost_mod": 3.0, "time_mod": 3.0, "repro_mod": 1.3},
        "full": {"fidelity_mod": 1.8, "cost_mod": 5.0, "time_mod": 5.0, "repro_mod": 1.5},
    }

    base_fidelity = survival_product_error_proxy(gate_error_rates)
    base_cost = n_gates * 0.01
    base_time = n_gates * 0.1

    results = []
    for strategy in strategies:
        params = strategy_params.get(strategy, strategy_params["baseline"])
        results.append({
            "strategy": strategy,
            "fidelity": base_fidelity * params["fidelity_mod"],
            "cost": base_cost * params["cost_mod"],
            "time_sec": base_time * params["time_mod"],
            "reproducibility": params["repro_mod"],
        })

    for r in results:
        r["score"] = weighted_objective(
            r["fidelity"], r["cost"], r["time_sec"], r["reproducibility"]
        )

    return results


def main():
    parser = argparse.ArgumentParser(description="QBalance-inspired workflow optimizer")
    parser.add_argument("--gate-error-rates", type=str, default="0.001,0.002,0.001")
    parser.add_argument("--n-gates", type=int, default=100)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    gate_errors = [float(x) for x in args.gate_error_rates.split(",")]
    results = evaluate_strategies(gate_errors, args.n_gates)
    pareto = pareto_select(results)

    print(f"Strategy Evaluations (n_gates={args.n_gates})")
    print(f"Base fidelity: {survival_product_error_proxy(gate_errors):.6f}")
    print(f"All strategies:")
    for r in results:
        marker = " [PARETO]" if r in pareto else ""
        print(f"  {r['strategy']:15s} score={r['score']:.4f} "
              f"fidelity={r['fidelity']:.4f} cost={r['cost']:.4f} "
              f"time={r['time_sec']:.2f}s repro={r['reproducibility']:.2f}{marker}")

    print(f"Pareto-optimal: {len(pareto)}")
    for p in pareto:
        print(f"  - {p['strategy']}: score={p['score']:.4f}")

    if args.output:
        with open(args.output, "w") as f:
            json.dump({"all": results, "pareto": pareto}, f, indent=2)
        print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
