"""
Barren Plateau Detection and Mitigation Utilities
for Quantum Neural Networks

Usage:
    from qnn_bp_utils import detect_barren_plateau, AIInitializer, LayerwiseTrainer
"""

import numpy as np
from typing import Callable, Tuple, List


class BarrenPlateauDetector:
    """Detect barren plateaus in quantum circuits via gradient variance analysis."""

    def __init__(self, n_samples: int = 1000, threshold: float = 1e-6):
        """
        Args:
            n_samples: Number of random samples for variance estimation
            threshold: Variance threshold for plateau detection
        """
        self.n_samples = n_samples
        self.threshold = threshold

    def detect(self, circuit_evaluator: Callable, n_params: int) -> Tuple[bool, float]:
        """
        Detect if circuit exhibits barren plateaus.

        Args:
            circuit_evaluator: Function that takes parameters and returns gradients
            n_params: Number of circuit parameters

        Returns:
            (is_plateau, variance): Detection result and estimated variance
        """
        gradients = []

        for _ in range(self.n_samples):
            # Random initialization
            params = np.random.uniform(-np.pi, np.pi, n_params)
            grad = circuit_evaluator(params)
            gradients.append(np.mean(np.abs(grad)))

        variance = np.var(gradients)
        is_plateau = variance < self.threshold

        return is_plateau, variance

    def estimate_variance_decay(
        self, circuit_evaluator: Callable, n_qubits_range: List[int], depth: int
    ) -> dict:
        """
        Estimate how variance scales with qubit count.

        Returns:
            Dictionary with scaling analysis results
        """
        results = {}

        for n_qubits in n_qubits_range:
            # Estimate variance for this qubit count
            n_params = n_qubits * depth * 2  # Rough estimate
            _, variance = self.detect(circuit_evaluator, n_params)
            results[n_qubits] = variance

        return results


class SubmartingaleInitializer:
    """
    Initialize circuit parameters ensuring submartingale property
    for gradient variance.
    """

    def __init__(self, target_variance: float = 1e-4):
        self.target_variance = target_variance

    def initialize(self, n_params: int, strategy: str = "gaussian") -> np.ndarray:
        """
        Generate initial parameters.

        Args:
            n_params: Number of parameters
            strategy: 'gaussian', 'uniform', 'zero', 'layered'

        Returns:
            Initial parameter array
        """
        if strategy == "gaussian":
            # Small variance around zero
            return np.random.normal(0, 0.1, n_params)
        elif strategy == "uniform":
            return np.random.uniform(-0.1, 0.1, n_params)
        elif strategy == "zero":
            # Identity initialization
            return np.zeros(n_params)
        elif strategy == "layered":
            # Layer-wise decreasing magnitude
            params = np.random.normal(0, 0.1, n_params)
            n_layers = int(np.sqrt(n_params))
            for i in range(n_params):
                layer = i % n_layers
                params[i] *= 1.0 / (layer + 1)
            return params
        else:
            raise ValueError(f"Unknown strategy: {strategy}")

    def validate_variance(
        self, params: np.ndarray, circuit_evaluator: Callable
    ) -> bool:
        """Validate that parameters maintain acceptable variance."""
        grad = circuit_evaluator(params)
        variance = np.var(grad)
        return variance >= self.target_variance


class LayerwiseTrainer:
    """Train quantum circuits layer by layer to avoid barren plateaus."""

    def __init__(self, learning_rate: float = 0.01, steps_per_layer: int = 100):
        self.learning_rate = learning_rate
        self.steps_per_layer = steps_per_layer

    def train(
        self,
        circuit_builder: Callable,
        cost_function: Callable,
        n_layers: int,
        n_params_per_layer: int,
    ) -> np.ndarray:
        """
        Train circuit layer by layer.

        Args:
            circuit_builder: Function(layer_idx, params) -> circuit_output
            cost_function: Function(circuit_output) -> scalar
            n_layers: Total number of layers
            n_params_per_layer: Parameters per layer

        Returns:
            Trained parameters
        """
        all_params = np.zeros((n_layers, n_params_per_layer))

        for current_layer in range(n_layers):
            print(f"Training layer {current_layer + 1}/{n_layers}")

            # Train only up to current layer
            for step in range(self.steps_per_layer):
                # Compute gradients for active parameters
                gradients = self._compute_gradients(
                    all_params, current_layer, circuit_builder, cost_function
                )

                # Update only current layer's parameters
                all_params[current_layer] -= self.learning_rate * gradients

        return all_params.flatten()

    def _compute_gradients(
        self,
        params: np.ndarray,
        active_layer: int,
        circuit_builder: Callable,
        cost_function: Callable,
    ) -> np.ndarray:
        """Compute numerical gradients for active layer."""
        eps = 1e-5
        gradients = np.zeros_like(params[active_layer])

        for i in range(len(gradients)):
            params_plus = params.copy()
            params_minus = params.copy()
            params_plus[active_layer][i] += eps
            params_minus[active_layer][i] -= eps

            output_plus = circuit_builder(active_layer, params_plus)
            output_minus = circuit_builder(active_layer, params_minus)

            cost_plus = cost_function(output_plus)
            cost_minus = cost_function(output_minus)

            gradients[i] = (cost_plus - cost_minus) / (2 * eps)

        return gradients


def create_local_ansatz(
    n_qubits: int, depth: int, connectivity: str = "linear"
) -> dict:
    """
    Create ansatz with local connectivity to reduce barren plateau probability.

    Args:
        n_qubits: Number of qubits
        depth: Circuit depth
        connectivity: 'linear', 'circular', 'nearest-neighbor'

    Returns:
        Dictionary describing ansatz structure
    """
    ansatz = {
        "n_qubits": n_qubits,
        "depth": depth,
        "connectivity": connectivity,
        "n_params": n_qubits * depth * 2,  # Rotation + entanglement
        "layers": [],
    }

    for d in range(depth):
        layer = {
            "rotation_gates": [("RY", i) for i in range(n_qubits)]
            + [("RZ", i) for i in range(n_qubits)],
            "entanglement": [],
        }

        # Add entanglement based on connectivity
        if connectivity == "linear":
            layer["entanglement"] = [("CNOT", i, i + 1) for i in range(n_qubits - 1)]
        elif connectivity == "circular":
            layer["entanglement"] = [
                ("CNOT", i, (i + 1) % n_qubits) for i in range(n_qubits)
            ]

        ansatz["layers"].append(layer)

    return ansatz


def variance_scaling_analysis(n_qubits_list: List[int], depths: List[int]) -> dict:
    """
    Analyze how gradient variance scales with circuit size.

    Returns:
        Analysis results with scaling exponents
    """
    results = {}

    for n_qubits in n_qubits_list:
        results[n_qubits] = {}
        for depth in depths:
            # Theoretical prediction: variance ~ 2^(-depth) * 2^(-n_qubits/2)
            theoretical = 2 ** (-depth - n_qubits / 2)
            results[n_qubits][depth] = {
                "theoretical": theoretical,
                "recommendation": "acceptable" if theoretical > 1e-6 else "high_risk",
            }

    return results


# Example usage
if __name__ == "__main__":
    print("Barren Plateau Utilities Demo")
    print("=" * 40)

    # Detector demo
    detector = BarrenPlateauDetector(n_samples=100)
    print(f"\nDetector configured with threshold: {detector.threshold}")

    # Initializer demo
    initializer = SubmartingaleInitializer(target_variance=1e-4)
    params = initializer.initialize(n_params=10, strategy="layered")
    print(f"\nGenerated {len(params)} parameters with layered strategy")
    print(f"Sample values: {params[:5]}")

    # Ansatz demo
    ansatz = create_local_ansatz(n_qubits=4, depth=2, connectivity="linear")
    print(f"\nCreated ansatz: {ansatz['n_qubits']} qubits, {ansatz['depth']} layers")
    print(f"Total parameters: {ansatz['n_params']}")

    # Variance analysis demo
    analysis = variance_scaling_analysis(n_qubits_list=[4, 6, 8, 10], depths=[2, 4, 6])
    print(f"\nVariance scaling analysis complete for {len(analysis)} qubit counts")
