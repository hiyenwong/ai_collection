#!/usr/bin/env python3
"""
Hybrid Transfer Learning Example - Quantum Neural Hybrid Skill

Demonstrates transfer learning from classical to quantum network.
Based on arXiv:1912.08278 - "Transfer learning in hybrid classical-quantum neural networks"
"""

import torch
import torch.nn as nn
import pennylane as qml

# Configuration
n_qubits = 4
n_layers = 2
input_dim = 16

# Classical Network (Pre-trained)
class ClassicalEncoder(nn.Module):
    """Pre-trained classical network for feature extraction"""
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, n_qubits),
            nn.Tanh()  # Normalize to [-1, 1] for quantum input
        )
    
    def forward(self, x):
        return self.features(x)

# Quantum Circuit
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def quantum_circuit(inputs, weights):
    """Variational quantum circuit"""
    # Angle encoding
    for i in range(n_qubits):
        qml.RY(inputs[i] * torch.pi, wires=i)
    
    # Variational layers with entanglement
    for layer in range(n_layers):
        # Single-qubit rotations
        for i in range(n_qubits):
            qml.Rot(weights[layer, i, 0],
                   weights[layer, i, 1],
                   weights[layer, i, 2], wires=i)
        
        # Entangling layer (CNOT ring)
        for i in range(n_qubits):
            qml.CNOT(wires=[i, (i+1) % n_qubits])
    
    # Measurements in Z basis
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

# Hybrid Model
class HybridModel(nn.Module):
    """Classical-Quantum hybrid architecture"""
    def __init__(self):
        super().__init__()
        self.classical = ClassicalEncoder()
        
        # Quantum weights ( trainable)
        weight_shapes = {"weights": (n_layers, n_qubits, 3)}
        self.q_layer = qml.qnn.TorchLayer(quantum_circuit, weight_shapes)
        
        # Output layer
        self.output = nn.Linear(n_qubits, 1)
    
    def forward(self, x):
        # Classical feature extraction
        features = self.classical(x)
        
        # Quantum processing
        quantum_out = self.q_layer(features)
        
        # Final prediction
        return self.output(quantum_out)

def train_hybrid_model():
    """Train hybrid model with transfer learning"""
    print("=== Hybrid Transfer Learning Example ===")
    
    # Initialize model
    model = HybridModel()
    
    # Freeze classical layers (transfer learning)
    print("\n1. Freezing classical layers...")
    for param in model.classical.parameters():
        param.requires_grad = False
    
    # Training configuration
    optimizer = torch.optim.Adam([
        {'params': model.q_layer.parameters(), 'lr': 0.01},
        {'params': model.output.parameters(), 'lr': 0.01}
    ])
    
    loss_fn = nn.MSELoss()
    
    # Dummy training data
    X_train = torch.randn(100, input_dim)
    y_train = torch.randn(100, 1)
    
    print("\n2. Training quantum layers...")
    epochs = 20
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        
        predictions = model(X_train)
        loss = loss_fn(predictions, y_train)
        
        loss.backward()
        optimizer.step()
        
        if (epoch + 1) % 5 == 0:
            print(f"   Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")
    
    print("\n3. Unfreezing classical layers for fine-tuning...")
    for param in model.classical.parameters():
        param.requires_grad = True
    
    # Fine-tune all layers
    optimizer_ft = torch.optim.Adam(model.parameters(), lr=0.001)
    
    print("\n4. Fine-tuning complete model...")
    for epoch in range(10):
        optimizer_ft.zero_grad()
        
        predictions = model(X_train)
        loss = loss_fn(predictions, y_train)
        
        loss.backward()
        optimizer_ft.step()
        
        if (epoch + 1) % 5 == 0:
            print(f"   Fine-tune Epoch {epoch+1}/10, Loss: {loss.item():.4f}")
    
    print("\n✓ Hybrid model training complete!")
    print(f"   Classical layers: {sum(p.numel() for p in model.classical.parameters())} params")
    print(f"   Quantum weights: {n_layers * n_qubits * 3} params")
    print(f"   Output layer: {sum(p.numel() for p in model.output.parameters())} params")
    
    return model

if __name__ == "__main__":
    model = train_hybrid_model()
    
    # Test inference
    print("\n=== Test Inference ===")
    test_input = torch.randn(1, input_dim)
    output = model(test_input)
    print(f"Input shape: {test_input.shape}")
    print(f"Output: {output.item():.4f}")