#!/usr/bin/env python3
"""
Architecture evaluation for Quantum Neural Architecture Search.

Three-objective evaluation:
1. Validation error (accuracy)
2. Runtime cost (efficiency)
3. Cutting overhead (deployability)
"""

import numpy as np
from typing import Dict, List, Tuple
from sklearn.metrics import accuracy_score


class ArchitectureEvaluator:
    """
    Evaluate quantum circuit architectures on three objectives.
    """

    def __init__(self, supercircuit, validation_data: Dict, target_qubits: int = 8):
        """
        Args:
            supercircuit: Trained SuperCircuit instance
            validation_data: {'features': np.ndarray, 'labels': np.ndarray}
            target_qubits: Hardware qubit budget
        """
        self.supercircuit = supercircuit
        self.validation_data = validation_data
        self.target_qubits = target_qubits

    def evaluate(self, architecture: Dict) -> Tuple[float, float, float]:
        """
        Three-objective evaluation.

        Returns:
            (validation_error, runtime_cost, cutting_overhead)
        """
        # Objective 1: Validation error
        val_error = self._evaluate_accuracy(architecture)

        # Objective 2: Runtime cost
        runtime_cost = self._estimate_runtime(architecture)

        # Objective 3: Cutting overhead
        cutting_overhead = self._estimate_cutting_overhead(architecture)

        return (val_error, runtime_cost, cutting_overhead)

    def _evaluate_accuracy(self, architecture: Dict) -> float:
        """
        Evaluate classification/regression accuracy.

        Strategy:
            1. Sample weights from SuperCircuit
            2. Build circuit
            3. Run cross-validation
        """
        features = self.validation_data["features"]
        labels = self.validation_data["labels"]

        # Sample weights from SuperCircuit
        weights = self.supercircuit.sample_weights(architecture)

        # Build circuit
        self.supercircuit.build_circuit(architecture, features)

        # Forward pass (batch processing)
        predictions = []
        for i in range(len(features)):
            # Preprocess feature for this sample
            sample_features = self._preprocess_feature(features[i], architecture)

            # Build circuit for this sample
            sample_circuit = self.supercircuit.build_circuit(
                architecture, sample_features
            )

            # Execute
            output = sample_circuit(weights)

            # Decode output to prediction
            prediction = self._decode_output(output, labels)
            predictions.append(prediction)

        # Compute validation error (1 - accuracy)
        accuracy = accuracy_score(labels, predictions)
        val_error = 1.0 - accuracy

        return val_error

    def _estimate_runtime(self, architecture: Dict) -> float:
        """
        Estimate runtime cost proxy.

        Formula: param_count × circuit_depth

        Higher values = slower execution.
        """
        # Parameter count: depth × qubits × 3 (Rx, Ry, Rz)
        param_count = architecture["depth"] * architecture["qubits"] * 3

        # Circuit depth estimate
        circuit_depth = self._estimate_circuit_depth(architecture)

        runtime_cost = param_count * circuit_depth

        return runtime_cost

    def _estimate_circuit_depth(self, architecture: Dict) -> int:
        """
        Estimate circuit depth based on components.

        Embedding depth + entangling depth + variational depth.
        """
        # Embedding depth
        if architecture["embedding"] == "angle-y":
            embedding_depth = 1
        elif architecture["embedding"] == "angle":
            embedding_depth = 2
        elif architecture["embedding"] == "amplitude":
            embedding_depth = 1
        else:
            embedding_depth = 1

        # Entangling depth (per layer)
        if architecture["cnot_pattern"] == "sparse":
            cnot_depth = architecture["qubits"] - 1
        elif architecture["cnot_pattern"] == "full":
            cnot_depth = architecture["qubits"] * (architecture["qubits"] - 1) / 2
        elif architecture["cnot_pattern"] == "linear":
            cnot_depth = 2
        else:
            cnot_depth = architecture["qubits"]

        # Variational depth (per layer)
        variational_depth = 3  # Rx, Ry, Rz

        # Total depth
        total_depth = embedding_depth + architecture["depth"] * (
            cnot_depth + variational_depth
        )

        return int(total_depth)

    def _estimate_cutting_overhead(self, architecture: Dict) -> float:
        """
        Estimate circuit cutting overhead.

        If circuit qubits > target_qubits:
            overhead = 4^k (wire cutting)

        where k = number of cuts needed
        """
        circuit_qubits = architecture["qubits"]

        if circuit_qubits <= self.target_qubits:
            return 1.0  # No cutting needed

        # Estimate number of cuts
        excess_qubits = circuit_qubits - self.target_qubits

        # Each cut can handle ~target_qubits/2 qubits
        cuts_per_wire = max(1, int(self.target_qubits / 2))
        k = int(np.ceil(excess_qubits / cuts_per_wire))

        # Wire cutting overhead: 4^k
        overhead = 4**k

        return float(overhead)

    def _preprocess_feature(
        self, feature: np.ndarray, architecture: Dict
    ) -> np.ndarray:
        """
        Preprocess feature for circuit input.

        Normalize, pad, or truncate based on embedding type.
        """
        if architecture["embedding"] == "amplitude":
            # Normalize and pad to 2^qubits
            norm = np.linalg.norm(feature)
            if norm > 0:
                feature = feature / norm

            # Pad
            target_size = 2 ** architecture["qubits"]
            if len(feature) < target_size:
                feature = np.pad(feature, (0, target_size - len(feature)))
            else:
                feature = feature[:target_size]
        else:
            # For angle embeddings, truncate/pad to qubits
            if len(feature) > architecture["qubits"]:
                feature = feature[: architecture["qubits"]]
            elif len(feature) < architecture["qubits"]:
                feature = np.pad(feature, (0, architecture["qubits"] - len(feature)))

            # Normalize to [0, π] range
            feature = feature * np.pi

        return feature

    def _decode_output(self, output: List[float], labels: np.ndarray) -> int:
        """
        Decode circuit output to class prediction.

        Strategy: Majority vote on qubit expectations.
        """
        # Threshold outputs at 0
        binary_outputs = [int(x > 0) for x in output]

        # Encode to class (simple sum for demo)
        prediction = sum(binary_outputs) % len(np.unique(labels))

        return prediction


if __name__ == "__main__":
    # Example usage
    from build_supercircuit import SuperCircuit

    # Initialize SuperCircuit
    supercircuit = SuperCircuit(max_qubits=8, max_depth=5)

    # Create validation data
    validation_data = {
        "features": np.random.uniform(-np.pi, np.pi, size=(100, 8)),
        "labels": np.random.randint(0, 10, size=100),
    }

    # Initialize evaluator
    evaluator = ArchitectureEvaluator(
        supercircuit=supercircuit, validation_data=validation_data, target_qubits=8
    )

    # Evaluate architecture
    architecture = {
        "embedding": "angle-y",
        "cnot_pattern": "sparse",
        "depth": 2,
        "qubits": 8,
    }

    fitness = evaluator.evaluate(architecture)

    print(f"Architecture: {architecture}")
    print(f"Fitness (val_error, runtime_cost, cutting_overhead): {fitness}")
