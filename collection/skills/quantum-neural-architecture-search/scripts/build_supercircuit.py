#!/usr/bin/env python3
"""
Build SuperCircuit for Quantum Neural Architecture Search.

SuperCircuit: Shared-parameter quantum circuit that encodes multiple
candidate architectures, enabling efficient evaluation without re-training.
"""

import pennylane as qml
import numpy as np
from typing import Dict, List, Optional

class SuperCircuit:
    """
    Shared-parameter SuperCircuit for QNAS.
    
    Attributes:
        max_qubits: Maximum qubits in search space
        max_depth: Maximum circuit depth
        embedding_types: Available embedding methods
        cnot_patterns: Available entangling patterns
        shared_weights: Shared parameters across architectures
    """
    
    def __init__(
        self,
        max_qubits: int = 8,
        max_depth: int = 5,
        embedding_types: List[str] = ['angle-y', 'angle', 'amplitude'],
        cnot_patterns: List[str] = ['sparse', 'full', 'linear']
    ):
        self.max_qubits = max_qubits
        self.max_depth = max_depth
        self.embedding_types = embedding_types
        self.cnot_patterns = cnot_patterns
        
        # Initialize shared weights
        # Total params: max_qubits * max_depth * 3 (Rx, Ry, Rz per qubit per layer)
        self.shared_weights = np.random.uniform(
            -np.pi, np.pi,
            size=(max_depth, max_qubits, 3)
        )
        
        # Quantum device
        self.device = qml.device('default.qubit', wires=max_qubits)
    
    def angle_y_embedding(self, features: np.ndarray, qubits: int):
        """
        Angle-Y embedding: Rotate each feature along Y-axis.
        
        Best for: Normalized image features (MNIST, Fashion-MNIST)
        """
        for i in range(min(len(features), qubits)):
            qml.RY(features[i], wires=i)
    
    def angle_embedding(self, features: np.ndarray, qubits: int):
        """
        Angle embedding: Rotate features along X, Y, Z axes.
        
        General-purpose embedding.
        """
        for i in range(min(len(features), qubits)):
            qml.RX(features[i], wires=i)
            qml.RY(features[i], wires=i)
    
    def amplitude_embedding(self, features: np.ndarray, qubits: int):
        """
        Amplitude embedding: Encode in amplitude basis.
        
        Best for: Dense vectors, tabular data (Iris)
        Requires: 2^n qubits for n features
        """
        # Normalize features
        norm = np.linalg.norm(features)
        normalized = features / norm
        
        # Pad to 2^qubits
        padded = np.pad(normalized, (0, 2**qubits - len(features)))
        
        qml.AmplitudeEmbedding(padded, wires=range(qubits), normalize=False)
    
    def sparse_cnot(self, qubits: int, layer: int):
        """
        Sparse CNOT pattern: Connect only adjacent qubits.
        
        Low overhead, maintains expressivity.
        """
        for i in range(qubits - 1):
            qml.CNOT(wires=[i, i+1])
    
    def full_cnot(self, qubits: int, layer: int):
        """
        Full CNOT pattern: All-to-all connectivity.
        
        Maximum entanglement, high overhead.
        """
        for i in range(qubits):
            for j in range(i+1, qubits):
                qml.CNOT(wires=[i, j])
    
    def linear_cnot(self, qubits: int, layer: int):
        """
        Linear CNOT pattern: Chain connectivity.
        
        Minimal overhead, suitable for shallow circuits.
        """
        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[qubits-2, qubits-1])
    
    def variational_layer(self, qubits: int, layer: int, weights: np.ndarray):
        """
        Variational layer: Rotation gates with shared weights.
        
        Args:
            qubits: Number of active qubits
            layer: Layer index
            weights: Weight slice from shared_weights
        """
        for i in range(qubits):
            qml.RX(weights[layer, i, 0], wires=i)
            qml.RY(weights[layer, i, 1], wires=i)
            qml.RZ(weights[layer, i, 2], wires=i)
    
    def build_circuit(
        self,
        architecture: Dict,
        features: np.ndarray
    ):
        """
        Build quantum circuit for given architecture.
        
        Args:
            architecture: {
                'embedding': str,
                'cnot_pattern': str,
                'depth': int,
                'qubits': int
            }
            features: Input data features
        
        Returns:
            Quantum function for Pennylane
        """
        @qml.qnode(self.device)
        def circuit(weights):
            # Embedding layer
            if architecture['embedding'] == 'angle-y':
                self.angle_y_embedding(features, architecture['qubits'])
            elif architecture['embedding'] == 'angle':
                self.angle_embedding(features, architecture['qubits'])
            elif architecture['embedding'] == 'amplitude':
                self.amplitude_embedding(features, architecture['qubits'])
            
            # Variational layers
            for layer in range(architecture['depth']):
                # Entangling layer
                if architecture['cnot_pattern'] == 'sparse':
                    self.sparse_cnot(architecture['qubits'], layer)
                elif architecture['cnot_pattern'] == 'full':
                    self.full_cnot(architecture['qubits'], layer)
                elif architecture['cnot_pattern'] == 'linear':
                    self.linear_cnot(architecture['qubits'], layer)
                
                # Variational layer
                self.variational_layer(
                    architecture['qubits'],
                    layer,
                    weights
                )
            
            # Measurement (expectation of Z on all qubits)
            return [qml.expval(qml.PauliZ(i)) for i in range(architecture['qubits'])]
        
        return circuit
    
    def sample_weights(self, architecture: Dict) -> np.ndarray:
        """
        Sample weights for given architecture from shared weights.
        
        Returns slice of shared_weights matching architecture dimensions.
        """
        return self.shared_weights[:architecture['depth'], :architecture['qubits'], :]
    
    def train(
        self,
        dataset: Dict,
        epochs: int = 50,
        learning_rate: float = 0.01
    ):
        """
        Train SuperCircuit on dataset.
        
        Args:
            dataset: {'features': np.ndarray, 'labels': np.ndarray}
            epochs: Training epochs
            learning_rate: Optimizer learning rate
        """
        optimizer = qml.AdamOptimizer(stepsize=learning_rate)
        
        for epoch in range(epochs):
            # Sample random architectures
            architectures = self._sample_architectures(n=10)
            
            for arch in architectures:
                # Build circuit
                circuit = self.build_circuit(arch, dataset['features'])
                
                # Get weights
                weights = self.sample_weights(arch)
                
                # Forward pass
                outputs = circuit(weights)
                
                # Compute loss (MSE for regression, cross-entropy for classification)
                loss = self._compute_loss(outputs, dataset['labels'])
                
                # Update shared weights
                self.shared_weights = optimizer.step(
                    lambda w: self._compute_loss(
                        self.build_circuit(arch, dataset['features'])(w),
                        dataset['labels']
                    ),
                    self.shared_weights
                )
            
            if epoch % 10 == 0:
                print(f"Epoch {epoch}: Loss = {loss:.4f}")
    
    def _sample_architectures(self, n: int) -> List[Dict]:
        """
        Sample n random architectures from search space.
        """
        architectures = []
        
        for _ in range(n):
            arch = {
                'embedding': np.random.choice(self.embedding_types),
                'cnot_pattern': np.random.choice(self.cnot_patterns),
                'depth': np.random.randint(1, self.max_depth + 1),
                'qubits': np.random.randint(4, self.max_qubits + 1)
            }
            architectures.append(arch)
        
        return architectures
    
    def _compute_loss(self, outputs, labels):
        """
        Compute loss (placeholder - implement based on task).
        """
        # MSE loss for demonstration
        return np.mean((outputs - labels)**2)


if __name__ == "__main__":
    # Example usage
    supercircuit = SuperCircuit(
        max_qubits=8,
        max_depth=5
    )
    
    # Sample architecture
    architecture = {
        'embedding': 'angle-y',
        'cnot_pattern': 'sparse',
        'depth': 2,
        'qubits': 8
    }
    
    # Build circuit
    features = np.random.uniform(-np.pi, np.pi, size=8)
    circuit = supercircuit.build_circuit(architecture, features)
    
    # Sample weights
    weights = supercircuit.sample_weights(architecture)
    
    # Execute
    outputs = circuit(weights)
    print(f"Circuit outputs: {outputs}")