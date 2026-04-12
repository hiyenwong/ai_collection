#!/usr/bin/env python3
"""
SIGN: Sparse Identification Graph Neural Network

Core implementation for inferring governing equations of complex networked systems.
"""

import numpy as np
import torch
import torch.nn as nn
from typing import Dict, List, Optional


class SIGN(nn.Module):
    """
    Sparse Identification Graph Neural Network for equation discovery.
    
    Attributes:
        num_nodes: Number of nodes in the network
        node_dim: Dimension of node state
        hidden_dim: Hidden dimension for GNN
        library: Function library type
        sparsity_threshold: Threshold for sparse coefficient selection
    """
    
    def __init__(
        self,
        num_nodes: int,
        node_dim: int = 1,
        hidden_dim: int = 64,
        library: str = 'polynomial',
        sparsity_threshold: float = 0.01,
        ridge_alpha: float = 1e-5,
        max_iterations: int = 10
    ):
        super().__init__()
        self.num_nodes = num_nodes
        self.node_dim = node_dim
        self.hidden_dim = hidden_dim
        self.library_type = library
        self.sparsity_threshold = sparsity_threshold
        self.ridge_alpha = ridge_alpha
        self.max_iterations = max_iterations
        
        # GNN layers
        self.node_encoder = nn.Linear(node_dim, hidden_dim)
        self.edge_encoder = nn.Linear(2 * node_dim, hidden_dim)
        self.message_fn = nn.Linear(2 * hidden_dim, hidden_dim)
        self.update_fn = nn.Linear(2 * hidden_dim, hidden_dim)
        
        # Library function
        self.library = self._build_library(library)
        
        # Discovered equations (to be filled)
        self.equations: Dict[int, Dict] = {}
        self.coefficients: Optional[np.ndarray] = None
        
    def _build_library(self, library_type: str) -> List[str]:
        """Build candidate function library."""
        if library_type == 'polynomial':
            return ['1', 'x', 'y', 'x^2', 'y^2', 'xy', 'x^3', 'y^3', 'x^2y', 'xy^2']
        elif library_type == 'polynomial_trigonometric':
            return ['1', 'x', 'y', 'x^2', 'y^2', 'xy', 
                    'sin(x)', 'cos(x)', 'sin(y)', 'cos(y)',
                    'sin(xy)', 'cos(xy)']
        elif library_type == 'interaction':
            return ['1', 'dx', 'dy', 'dx^2', 'dy^2', 'dx*dy',
                    'x*y', 'sin(dx)', 'cos(dx)']
        else:
            raise ValueError(f"Unknown library type: {library_type}")
    
    def encode_network(
        self, 
        node_states: torch.Tensor,
        adjacency: torch.Tensor
    ) -> torch.Tensor:
        """
        Encode network structure using GNN.
        
        Args:
            node_states: Node state tensor [N, D]
            adjacency: Adjacency matrix [N, N]
            
        Returns:
            Edge representations [E, hidden_dim]
        """
        # Encode nodes
        h = self.node_encoder(node_states)  # [N, hidden_dim]
        
        # Find edges
        edge_indices = torch.nonzero(adjacency, as_tuple=True)
        src, dst = edge_indices
        
        # Encode edges
        edge_features = torch.cat([node_states[src], node_states[dst]], dim=-1)
        e = self.edge_encoder(edge_features)
        
        # Compute messages
        h_src = h[src]
        messages = self.message_fn(torch.cat([h_src, e], dim=-1))
        
        # Aggregate messages to nodes
        aggregated = torch.zeros(self.num_nodes, self.hidden_dim)
        aggregated.index_add_(0, dst, messages)
        
        # Update nodes
        h_new = self.update_fn(torch.cat([h, aggregated], dim=-1))
        
        return h_new, e
    
    def build_theta(
        self,
        edge_repr: np.ndarray,
        derivatives: np.ndarray
    ) -> np.ndarray:
        """
        Build candidate library matrix.
        
        Args:
            edge_repr: Edge representations [E, hidden_dim]
            derivatives: Target derivatives [E, D]
            
        Returns:
            Library matrix Theta [E, L]
        """
        # Use first few dimensions as state variables
        x = edge_repr[:, 0]
        y = edge_repr[:, 1] if edge_repr.shape[1] > 1 else np.zeros_like(x)
        
        theta_list = []
        for term in self.library:
            if term == '1':
                theta_list.append(np.ones_like(x))
            elif term == 'x':
                theta_list.append(x)
            elif term == 'y':
                theta_list.append(y)
            elif term == 'x^2':
                theta_list.append(x**2)
            elif term == 'y^2':
                theta_list.append(y**2)
            elif term == 'xy':
                theta_list.append(x * y)
            elif term == 'sin(x)':
                theta_list.append(np.sin(x))
            elif term == 'cos(x)':
                theta_list.append(np.cos(x))
            elif term == 'dx':
                theta_list.append(derivatives[:, 0])
            # ... add more terms as needed
        
        return np.column_stack(theta_list)
    
    def stridge(
        self,
        theta: np.ndarray,
        target: np.ndarray
    ) -> np.ndarray:
        """
        Sequential Threshold Ridge Regression.
        
        Args:
            theta: Library matrix [E, L]
            target: Target derivatives [E, D]
            
        Returns:
            Sparse coefficients [L, D]
        """
        # Initial pseudoinverse
        xi = np.linalg.pinv(theta) @ target
        
        for _ in range(self.max_iterations):
            # Threshold
            small_inds = np.abs(xi) < self.sparsity_threshold
            xi[small_inds] = 0
            
            # Ridge regression on active terms
            active_inds = ~small_inds
            if not np.any(active_inds):
                break
            
            theta_active = theta[:, active_inds]
            xi_active = np.linalg.solve(
                theta_active.T @ theta_active + self.ridge_alpha * np.eye(theta_active.shape[1]),
                theta_active.T @ target
            )
            
            xi[active_inds] = xi_active
        
        return xi
    
    def fit(
        self,
        time_series: np.ndarray,
        adjacency: np.ndarray,
        dt: float = 0.1
    ) -> None:
        """
        Fit SIGN to network time series data.
        
        Args:
            time_series: Node states over time [T, N, D]
            adjacency: Adjacency matrix [N, N]
            dt: Time step
        """
        T, N, D = time_series.shape
        
        # Compute derivatives
        derivatives = np.gradient(time_series, dt, axis=0)  # [T, N, D]
        
        # Use mean across time for robust estimation
        mean_states = time_series.mean(axis=0)  # [N, D]
        mean_derivs = derivatives.mean(axis=0)  # [N, D]
        
        # Encode network
        with torch.no_grad():
            node_states = torch.FloatTensor(mean_states)
            adj_tensor = torch.FloatTensor(adjacency)
            h, e = self.encode_network(node_states, adj_tensor)
        
        edge_repr = e.numpy()
        
        # Build library
        theta = self.build_theta(edge_repr, mean_derivs)
        
        # Sparse regression
        self.coefficients = self.stridge(theta, mean_derivs)
        
        # Extract equations
        self._extract_equations()
    
    def _extract_equations(self) -> None:
        """Extract discovered equations from coefficients."""
        if self.coefficients is None:
            return
        
        for i, term in enumerate(self.library):
            coef = self.coefficients[i]
            if np.abs(coef).max() > self.sparsity_threshold:
                self.equations[i] = {
                    'term': term,
                    'coefficient': coef,
                    'active': True
                }
    
    def get_equations(self) -> str:
        """Return discovered equations as human-readable string."""
        if not self.equations:
            return "No equations discovered yet. Run fit() first."
        
        lines = []
        for idx, eq in self.equations.items():
            coef_str = ', '.join([f'{c:.4f}' for c in eq['coefficient']])
            lines.append(f"{eq['term']}: [{coef_str}]")
        
        return '\n'.join(lines)
    
    def predict(
        self,
        initial_state: np.ndarray,
        horizon: int,
        dt: float = 0.1
    ) -> np.ndarray:
        """
        Predict future network dynamics using discovered equations.
        
        Args:
            initial_state: Initial node states [N, D]
            horizon: Number of time steps to predict
            dt: Time step
            
        Returns:
            Predicted states [horizon, N, D]
        """
        if self.coefficients is None:
            raise ValueError("No equations discovered. Run fit() first.")
        
        predictions = np.zeros((horizon, self.num_nodes, self.node_dim))
        predictions[0] = initial_state
        
        for t in range(1, horizon):
            state = predictions[t-1]
            
            # Compute derivative using discovered equation
            # Simplified: use mean coefficients
            deriv = self._compute_derivative(state)
            
            # Euler integration
            predictions[t] = state + deriv * dt
        
        return predictions
    
    def _compute_derivative(self, state: np.ndarray) -> np.ndarray:
        """Compute derivative using discovered equation."""
        # Placeholder: implement based on discovered terms
        return np.zeros_like(state)


def main():
    """Example usage of SIGN."""
    # Create synthetic network dynamics
    N = 1000  # nodes
    D = 2     # dimensions (e.g., x, y)
    T = 500   # time steps
    
    # Random adjacency (sparse)
    adjacency = np.random.rand(N, N) < 0.01
    adjacency = adjacency.astype(float)
    
    # Random initial states
    initial_state = np.random.randn(N, D)
    
    # Generate synthetic dynamics
    time_series = np.zeros((T, N, D))
    time_series[0] = initial_state
    for t in range(1, T):
        # Simple dynamics: coupling + noise
        coupling = adjacency @ time_series[t-1] * 0.1
        noise = np.random.randn(N, D) * 0.01
        time_series[t] = time_series[t-1] + coupling + noise
    
    # Initialize SIGN
    model = SIGN(
        num_nodes=N,
        node_dim=D,
        library='polynomial',
        sparsity_threshold=0.05
    )
    
    # Fit to data
    model.fit(time_series, adjacency)
    
    # Print discovered equations
    print("Discovered Equations:")
    print(model.get_equations())
    
    # Predict
    predictions = model.predict(time_series[-1], horizon=100)
    print(f"\nPredictions shape: {predictions.shape}")


if __name__ == '__main__':
    main()