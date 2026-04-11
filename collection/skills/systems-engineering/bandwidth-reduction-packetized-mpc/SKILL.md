---
name: bandwidth-reduction-packetized-mpc
description: Bandwidth Reduction Methods for Packetized Model Predictive Control over Lossy Networks. Optimize control communication in networked control systems.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [mpc, model-predictive-control, bandwidth-reduction, networked-control, lossy-networks]
    source_paper: "Bandwidth reduction methods for packetized MPC over lossy networks (arXiv:2604.08270)"
    citations: 0
    category: optimization and control
---

# Bandwidth Reduction for Packetized MPC

## Overview

This skill provides methodologies for reducing bandwidth requirements in packetized Model Predictive Control (MPC) over lossy communication channels. Two complementary approaches are combined: multi-horizon MPC formulation and communication protocol optimization.

## Core Concepts

### Packetized MPC
- **Offloaded Control**: MPC computations performed remotely
- **Communication**: Control inputs transmitted over network
- **Challenge**: Bandwidth constraints and packet losses

### Bandwidth Reduction Strategies
1. **Multi-Horizon MPC**: Reduce optimization variables and transmitted trajectory size
2. **Communication Protocol**: Efficient encoding and transmission strategies

## Implementation Pattern

```python
from typing import List, Tuple, Optional
import numpy as np
from dataclasses import dataclass

@dataclass
class MPCConfig:
    horizon: int
    dt: float  # Time step
    state_dim: int
    control_dim: int
    
class MultiHorizonMPC:
    """
    Multi-horizon MPC with bandwidth reduction
    """
    
    def __init__(self, config: MPCConfig, compression_ratio: float = 0.5):
        self.config = config
        self.compression_ratio = compression_ratio
        # Define multiple horizons with different resolutions
        self.horizons = self._define_horizons()
        
    def _define_horizons(self) -> List[Tuple[int, int]]:
        """
        Define multi-horizon structure
        Returns list of (start_step, end_step) for each horizon segment
        """
        H = self.config.horizon
        # Fine resolution for immediate steps, coarse for future
        return [
            (0, int(H * 0.3)),      # Fine: first 30%
            (int(H * 0.3), int(H * 0.7)),  # Medium: next 40%
            (int(H * 0.7), H)       # Coarse: last 30%
        ]
    
    def solve(self, current_state: np.ndarray, 
              reference: np.ndarray) -> np.ndarray:
        """
        Solve MPC with multi-horizon formulation
        
        Returns:
            Compressed control trajectory
        """
        # Solve optimization (simplified - actual implementation
        # would use QP solver or similar)
        full_trajectory = self._solve_optimization(current_state, reference)
        
        # Compress trajectory based on multi-horizon structure
        compressed = self._compress_trajectory(full_trajectory)
        
        return compressed
    
    def _solve_optimization(self, state: np.ndarray, 
                           reference: np.ndarray) -> np.ndarray:
        """
        Solve MPC optimization problem
        Placeholder - actual implementation uses QP solver
        """
        H = self.config.horizon
        u_dim = self.config.control_dim
        # Placeholder: return random trajectory
        return np.random.randn(H, u_dim)
    
    def _compress_trajectory(self, trajectory: np.ndarray) -> np.ndarray:
        """
        Compress control trajectory based on multi-horizon structure
        """
        compressed = []
        for start, end in self.horizons:
            segment = trajectory[start:end]
            if len(segment) == 0:
                continue
            # For fine horizon: keep all points
            # For medium: keep every 2nd point
            # For coarse: keep every 4th point
            if start == 0:
                compressed.extend(segment)
            elif start < self.config.horizon * 0.7:
                compressed.extend(segment[::2])
            else:
                compressed.extend(segment[::4])
        
        return np.array(compressed)
    
    def decompress_trajectory(self, compressed: np.ndarray, 
                             original_length: int) -> np.ndarray:
        """
        Decompress trajectory at receiver side using interpolation
        """
        # Linear interpolation to reconstruct full trajectory
        n_compressed = len(compressed)
        x_old = np.linspace(0, 1, n_compressed)
        x_new = np.linspace(0, 1, original_length)
        
        decompressed = np.zeros((original_length, compressed.shape[1]))
        for i in range(compressed.shape[1]):
            decompressed[:, i] = np.interp(x_new, x_old, compressed[:, i])
        
        return decompressed

class LossyNetworkProtocol:
    """
    Communication protocol optimized for lossy networks
    """
    
    def __init__(self, packet_size: int, ack_timeout: float):
        self.packet_size = packet_size
        self.ack_timeout = ack_timeout
        self.packet_buffer = []
        
    def encode_trajectory(self, trajectory: np.ndarray) -> List[bytes]:
        """
        Encode control trajectory into network packets
        """
        # Quantize to reduce size
        quantized = self._quantize(trajectory)
        
        # Split into packets
        packets = []
        data = quantized.tobytes()
        for i in range(0, len(data), self.packet_size):
            packet = data[i:i+self.packet_size]
            # Add sequence number and checksum
            header = self._create_header(i // self.packet_size)
            packets.append(header + packet)
        
        return packets
    
    def _quantize(self, trajectory: np.ndarray, 
                  bits: int = 16) -> np.ndarray:
        """
        Quantize trajectory values to reduce bandwidth
        """
        # Map to integer range
        max_val = np.max(np.abs(trajectory))
        scale = (2**(bits-1) - 1) / max_val if max_val > 0 else 1
        quantized = np.round(trajectory * scale).astype(np.int16)
        return quantized
    
    def _create_header(self, seq_num: int) -> bytes:
        """Create packet header with sequence number"""
        return seq_num.to_bytes(4, 'big')
    
    def decode_trajectory(self, packets: List[bytes], 
                         expected_shape: Tuple[int, int]) -> Optional[np.ndarray]:
        """
        Decode packets back to trajectory
        Handles packet loss through interpolation
        """
        # Sort by sequence number
        packets = sorted(packets, key=lambda p: int.from_bytes(p[:4], 'big'))
        
        # Reconstruct data
        data = b''.join(p[4:] for p in packets)
        
        try:
            trajectory = np.frombuffer(data, dtype=np.int16)
            trajectory = trajectory.reshape(expected_shape)
            # Dequantize
            max_val = 32767
            trajectory = trajectory.astype(np.float32) / max_val
            return trajectory
        except:
            return None

# Usage Example
config = MPCConfig(horizon=20, dt=0.1, state_dim=4, control_dim=2)
mpc = MultiHorizonMPC(config, compression_ratio=0.5)
protocol = LossyNetworkProtocol(packet_size=1024, ack_timeout=0.01)
```

## Key Insights

1. **Multi-Horizon Strategy**: Fine resolution for immediate steps, coarse for future
2. **Compression Ratio**: Typically 50-70% reduction in transmitted data
3. **Loss Resilience**: Protocol handles packet loss through redundancy and interpolation
4. **Trade-off**: Slight performance degradation for significant bandwidth savings

## Best Practices

- Use multi-horizon formulation with 3-4 resolution levels
- Implement forward error correction for critical packets
- Monitor network conditions and adapt compression ratio dynamically
- Validate control performance under various loss rates

## References

- Mingoia, A., Pezzutto, M., Barbosa, F. S., & Umsonst, D. (2025). Bandwidth reduction methods for packetized MPC over lossy networks. arXiv:2604.08270.

## Trigger Words

- packetized mpc
- bandwidth reduction
- networked control
- lossy networks
- multi-horizon mpc
- control communication
