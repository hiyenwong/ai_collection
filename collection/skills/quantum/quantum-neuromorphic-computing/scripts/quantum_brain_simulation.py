#!/usr/bin/env python3
"""Quantum Brain Model Simulation Script

Simulates quantum brain models with synaptic feedback,
based on Lipkin-Meshkov-Glick (LMG) framework.
"""

import numpy as np
import argparse
import json
from typing import Dict


class QuantumBrainModel:
    """LMG-based quantum brain model with synaptic feedback."""

    def __init__(self, n_spins: int = 10, feedback_strength: float = 0.5):
        self.n_spins = n_spins
        self.N = 2 * n_spins  # Collective spin dimension
        self.feedback = feedback_strength

        # Collective spin operators (simplified)
        self.Jx = np.zeros((self.N + 1, self.N + 1), dtype=complex)
        self.Jy = np.zeros((self.N + 1, self.N + 1), dtype=complex)
        self.Jz = np.zeros((self.N + 1, self.N + 1), dtype=float)

        self._init_operators()

    def _init_operators(self):
        """Initialize collective spin operators."""
        for m in range(-self.n_spins, self.n_spins + 1):
            idx = m + self.n_spins
            if idx < self.N:
                # Jx, Jy operators (simplified)
                self.Jx[idx, idx + 1] = 0.5 * np.sqrt(
                    self.n_spins * (self.n_spins + 1) - m * (m + 1)
                )
                self.Jx[idx + 1, idx] = self.Jx[idx, idx + 1]

                self.Jy[idx, idx + 1] = -0.5j * np.sqrt(
                    self.n_spins * (self.n_spins + 1) - m * (m + 1)
                )
                self.Jy[idx + 1, idx] = -self.Jy[idx, idx + 1]

            # Jz operator
            self.Jz[idx, idx] = m

    def hamiltonian(self, h: float, gamma: float, state: np.ndarray) -> np.ndarray:
        """Construct Hamiltonian with synaptic feedback.

        H = -h Jz - gamma (Jx^2 + Jy^2) + feedback * <Jz> * Jz

        Args:
            h: External field strength
            gamma: Interaction strength
            state: Current quantum state (for feedback calculation)

        Returns:
            Hamiltonian matrix
        """
        # Calculate expectation value for feedback
        exp_Jz = np.real(np.vdot(state, self.Jz @ state))

        # Base LMG Hamiltonian
        H = -h * self.Jz - gamma * (self.Jx @ self.Jx + self.Jy @ self.Jy)

        # Add synaptic feedback term
        H += self.feedback * exp_Jz * self.Jz

        return H

    def evolve(
        self,
        initial_state: np.ndarray,
        h: float,
        gamma: float,
        dt: float = 0.01,
        n_steps: int = 100,
    ) -> Dict:
        """Time evolution of quantum brain state.

        Args:
            initial_state: Initial quantum state vector
            h: External field
            gamma: Interaction strength
            dt: Time step
            n_steps: Number of evolution steps

        Returns:
            Dict with trajectory data
        """
        state = initial_state.copy()
        trajectory = {
            "expectation_Jx": [],
            "expectation_Jy": [],
            "expectation_Jz": [],
            "entropy": [],
            "time": [],
        }

        for step in range(n_steps):
            # Calculate Hamiltonian (feedback-dependent)
            H = self.hamiltonian(h, gamma, state)

            # Evolve state (simplified: small dt, use exp(-iHdt))
            U = np.eye(len(state)) - 1j * H * dt
            state = U @ state

            # Normalize
            state = state / np.linalg.norm(state)

            # Record observables
            trajectory["expectation_Jx"].append(
                float(np.real(np.vdot(state, self.Jx @ state)))
            )
            trajectory["expectation_Jy"].append(
                float(np.real(np.vdot(state, self.Jy @ state)))
            )
            trajectory["expectation_Jz"].append(
                float(np.real(np.vdot(state, self.Jz @ state)))
            )
            trajectory["entropy"].append(self._calculate_entropy(state))
            trajectory["time"].append(step * dt)

        return trajectory

    def _calculate_entropy(self, state: np.ndarray) -> float:
        """Calculate simplified Wehrl entropy."""
        # Husimi Q function (simplified: use |state|^2 as approximation)
        q = np.abs(state) ** 2

        # Avoid log(0)
        q = q + 1e-10

        # Wehrl entropy: -sum(q * log(q))
        entropy = -np.sum(q * np.log(q))

        return float(entropy)

    def phase_transition_analysis(
        self, h_range: np.ndarray, gamma: float = 1.0
    ) -> Dict:
        """Analyze phase transitions across field range.

        Args:
            h_range: Range of external field values
            gamma: Interaction strength

        Returns:
            Phase transition analysis data
        """
        results = {"h_values": [], "order_parameter": [], "entropy": [], "phase": []}

        for h in h_range:
            # Ground state approximation (highest weight state)
            state = np.zeros(self.N + 1)
            if h > 0:
                state[self.N] = 1.0  # Highest Jz
            else:
                state[0] = 1.0  # Lowest Jz

            # Evolve to equilibrium
            trajectory = self.evolve(state, h, gamma, dt=0.1, n_steps=50)

            # Order parameter: |<Jz>|
            order = abs(trajectory["expectation_Jz"][-1])

            # Final entropy
            entropy = trajectory["entropy"][-1]

            # Determine phase (simplified)
            if order > 0.5 * self.n_spins:
                phase = "ferromagnetic"
            elif entropy > 2.0:
                phase = "paramagnetic"
            else:
                phase = "mixed"

            results["h_values"].append(h)
            results["order_parameter"].append(order)
            results["entropy"].append(entropy)
            results["phase"].append(phase)

        return results


def main():
    parser = argparse.ArgumentParser(description="Quantum Brain Model Simulation")
    parser.add_argument(
        "--model",
        type=str,
        default="lmg",
        choices=["lmg", "feedback"],
        help="Model type",
    )
    parser.add_argument(
        "--feedback",
        type=str,
        default="synaptic",
        choices=["none", "synaptic", "retroactive"],
        help="Feedback type",
    )
    parser.add_argument("--spins", type=int, default=10, help="Number of spins")
    parser.add_argument("--h", type=float, default=1.0, help="External field strength")
    parser.add_argument("--gamma", type=float, default=0.5, help="Interaction strength")
    parser.add_argument("--steps", type=int, default=100, help="Evolution steps")
    parser.add_argument("--output", type=str, help="Output JSON file")
    args = parser.parse_args()

    print("\n# Quantum Brain Model Simulation")
    print(f"Model: {args.model}")
    print(f"Feedback: {args.feedback}")
    print(f"Spins: {args.spins}")
    print(f"h = {args.h}, gamma = {args.gamma}")

    # Set feedback strength based on type
    feedback_strength = 0.0 if args.feedback == "none" else 0.5

    # Create model
    model = QuantumBrainModel(n_spins=args.spins, feedback_strength=feedback_strength)

    # Initial state (balanced)
    initial_state = np.ones(model.N + 1)
    initial_state = initial_state / np.linalg.norm(initial_state)

    # Run evolution
    trajectory = model.evolve(
        initial_state, h=args.h, gamma=args.gamma, dt=0.01, n_steps=args.steps
    )

    # Print results
    print("\n## Evolution Results")
    print(f"Final <Jz>: {trajectory['expectation_Jz'][-1]:.3f}")
    print(f"Final entropy: {trajectory['entropy'][-1]:.3f}")

    # Phase transition analysis
    if args.feedback == "synaptic":
        print("\n## Phase Transition Analysis")
        h_range = np.linspace(-2, 2, 10)
        phase_data = model.phase_transition_analysis(h_range, args.gamma)

        for i, (h, phase) in enumerate(zip(h_range, phase_data["phase"])):
            print(f"h={h:.1f}: {phase} (order={phase_data['order_parameter'][i]:.2f})")

    # Save output
    if args.output:
        output_data = {
            "model": args.model,
            "feedback": args.feedback,
            "parameters": {
                "spins": args.spins,
                "h": args.h,
                "gamma": args.gamma,
                "steps": args.steps,
            },
            "trajectory": trajectory,
        }
        with open(args.output, "w") as f:
            json.dump(output_data, f, indent=2)
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
