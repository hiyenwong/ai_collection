#!/usr/bin/env python3
"""
Quantum ML Data Loading Utilities

Utilities for encoding classical data into quantum circuits.
Compatible with Qiskit and PennyLane.
"""

import numpy as np

try:
    from qiskit import QuantumCircuit
    from qiskit.circuit.library import StatePreparation
    QISKIT_AVAILABLE = True
except ImportError:
    QISKIT_AVAILABLE = False
    QuantumCircuit = None

try:
    import pennylane as qml
    PENNYLANE_AVAILABLE = True
except ImportError:
    PENNYLANE_AVAILABLE = False


def validate_normalization(vector: np.ndarray, tolerance: float = 1e-10) -> bool:
    """Check if vector is normalized."""
    norm = np.linalg.norm(vector)
    return abs(norm - 1.0) < tolerance


def normalize_vector(vector: np.ndarray) -> np.ndarray:
    """Normalize a vector to unit length."""
    norm = np.linalg.norm(vector)
    if norm < 1e-15:
        raise ValueError("Cannot normalize zero vector")
    return vector / norm


def pad_to_power_of_two(vector: np.ndarray) -> np.ndarray:
    """Pad vector to nearest power of 2."""
    n = len(vector)
    n_qubits = int(np.ceil(np.log2(n)))
    padded_size = 2 ** n_qubits
    
    if n == padded_size:
        return vector
    
    padded = np.zeros(padded_size, dtype=vector.dtype)
    padded[:n] = vector
    return padded


def basis_encoding_qiskit(data: list[int]) -> "QuantumCircuit":
    """
    Encode binary data as computational basis state using Qiskit.
    
    Args:
        data: List of binary values (0 or 1)
    
    Returns:
        QuantumCircuit with X gates for each |1⟩
    """
    if not QISKIT_AVAILABLE:
        raise ImportError("Qiskit not installed. Install with: pip install qiskit")
    
    n_qubits = len(data)
    qc = QuantumCircuit(n_qubits)
    
    for i, bit in enumerate(data):
        if bit == 1:
            qc.x(i)
    
    return qc


def amplitude_encoding_qiskit(
    vector: np.ndarray,
    validate: bool = True
) -> "QuantumCircuit":
    """
    Encode normalized vector into quantum amplitudes using Qiskit.
    
    Args:
        vector: Normalized classical vector
        validate: Check normalization
    
    Returns:
        QuantumCircuit preparing the state
    """
    if not QISKIT_AVAILABLE:
        raise ImportError("Qiskit not installed. Install with: pip install qiskit")
    
    if validate and not validate_normalization(vector):
        vector = normalize_vector(vector)
    
    # Pad to power of 2
    padded = pad_to_power_of_two(vector)
    
    n_qubits = int(np.log2(len(padded)))
    qc = QuantumCircuit(n_qubits)
    
    # Use StatePreparation
    qc.append(StatePreparation(padded), range(n_qubits))
    
    return qc


def angle_encoding_qiskit(
    data: np.ndarray,
    rotation: str = 'RY'
) -> "QuantumCircuit":
    """
    Encode data as rotation angles using Qiskit.
    
    Args:
        data: Array of values in [0, 1]
        rotation: 'RX', 'RY', or 'RZ'
    
    Returns:
        QuantumCircuit with rotation gates
    """
    if not QISKIT_AVAILABLE:
        raise ImportError("Qiskit not installed. Install with: pip install qiskit")
    
    n_qubits = len(data)
    qc = QuantumCircuit(n_qubits)
    
    for i, val in enumerate(data):
        angle = np.pi * val
        
        if rotation == 'RX':
            qc.rx(angle, i)
        elif rotation == 'RY':
            qc.ry(angle, i)
        elif rotation == 'RZ':
            qc.rz(angle, i)
        else:
            raise ValueError(f"Unknown rotation: {rotation}")
    
    return qc


def calculate_encoding_metrics(
    target: np.ndarray,
    circuit: "QuantumCircuit"
) -> dict:
    """
    Calculate metrics for encoding quality.
    
    Args:
        target: Target state vector
        circuit: Actual encoding circuit
    
    Returns:
        Dictionary of metrics
    """
    if not QISKIT_AVAILABLE:
        raise ImportError("Qiskit not installed")
    
    from qiskit.quantum_info import Statevector, state_fidelity
    
    actual = Statevector.from_instruction(circuit)
    target_sv = Statevector(target)
    
    return {
        'fidelity': state_fidelity(target_sv, actual),
        'depth': circuit.depth(),
        'num_qubits': circuit.num_qubits,
        'num_gates': sum(circuit.size())
    }


# PennyLane versions
def amplitude_encoding_pennylane(vector: np.ndarray, wires: list):
    """
    Amplitude encoding using PennyLane.
    
    Args:
        vector: Normalized vector
        wires: List of wire indices
    """
    if not PENNYLANE_AVAILABLE:
        raise ImportError("PennyLane not installed")
    
    padded = pad_to_power_of_two(vector)
    qml.AmplitudeEmbedding(padded, wires=wires)


def angle_encoding_pennylane(data: np.ndarray, wires: list, rotation: str = 'RY'):
    """
    Angle encoding using PennyLane.
    
    Args:
        data: Data values in [0, 1]
        wires: List of wire indices
        rotation: Rotation type
    """
    if not PENNYLANE_AVAILABLE:
        raise ImportError("PennyLane not installed")
    
    qml.AngleEmbedding(data, wires=wires, rotation=rotation)


if __name__ == "__main__":
    # Example usage
    print("Quantum ML Data Loading Utilities")
    print("=" * 50)
    
    # Test normalization
    vec = np.array([1, 2, 3, 4])
    norm_vec = normalize_vector(vec)
    print(f"Original: {vec}")
    print(f"Normalized: {norm_vec}")
    print(f"Norm: {np.linalg.norm(norm_vec):.6f}")
    
    # Test padding
    vec2 = np.array([1, 2, 3])
    padded = pad_to_power_of_two(vec2)
    print(f"\nOriginal: {vec2} (length {len(vec2)})")
    print(f"Padded: {padded} (length {len(padded)})")
