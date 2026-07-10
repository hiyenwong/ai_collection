---
name: snn-fpga-hardware-software-codesign
description: "Hardware-software co-design framework for event-driven SNN deployment on low-cost neuromorphic FPGAs. Unifies hardware and algorithm design with automated optimization. Keywords: SNN FPGA, hardware-software co-design, neuromorphic deployment, event-driven, low-cost FPGA."
---

# Hardware-Software Co-Design for Event-Driven SNN Deployment on Low-Cost Neuromorphic FPGAs

> A unified hardware-software co-design framework that bridges the gap between hardware-first and algorithm-first SNN approaches, enabling efficient deployment on low-cost FPGA platforms through automated hardware generation and event-driven processing optimization.

## Metadata
- **Source**: arXiv:2604.22179v1
- **Authors**: Jiwoon Lee, Souvik Chakraborty, Syed Bahauddin Alam, Kaushik Roy
- **Published**: 2026-04-24
- **Category**: Neuromorphic Engineering / Hardware-Software Codesign

## Core Methodology

### Key Innovation
Current SNN workflows are fragmented: hardware-first approaches are difficult to train, while algorithm-first approaches face deployment challenges. This work introduces a **unified co-design framework** that:
1. Automatically generates hardware from network specifications
2. Optimizes algorithms based on hardware constraints
3. Enables event-driven processing for maximum efficiency
4. Targets low-cost FPGAs (under $100) for accessibility

### Technical Framework

#### 1. Unified Representation
A common intermediate representation (IR) bridges software and hardware:
```
Software Layer (PyTorch/TensorFlow)
    ↓ (Compilation)
SNN Intermediate Representation (SNN-IR)
    ↓ (Optimization)
Hardware Layer (Verilog/VHDL)
```

#### 2. Hardware Generation Pipeline
- **Network Analysis**: Extracts connectivity and neuron parameters
- **Resource Estimation**: Predicts FPGA resource requirements
- **Automated RTL Generation**: Produces synthesizable Verilog
- **Timing Optimization**: Pipeline balancing and critical path reduction

#### 3. Event-Driven Architecture
```
Event Queue → Scheduler → Neuron Array → Synapse Array → Output
                ↑____________↓
              (Feedback loop for recurrent connections)
```

#### 4. Algorithm-Hardware Optimization
- **Sparsity Exploitation**: Skip zero-weight computations
- **Temporal Compression**: Batching events in time windows
- **Dynamic Precision**: Adjustable bit-width based on layer importance

## Implementation Guide

### Prerequisites
- Python 3.8+ with PyTorch
- FPGA synthesis tools (Xilinx Vivado or Intel Quartus)
- Low-cost FPGA board (Digilent Nexys A7, Terasic DE10-Lite)

### Step-by-Step Setup

#### Step 1: Install Framework
```bash
git clone https://github.com/neurohw/codesign-snn.git
cd codesign-snn
pip install -r requirements.txt
```

#### Step 2: Define SNN in Software
```python
import torch
import snn_ir

# Define SNN model
class EventSNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lif1 = snn_ir.LIFCell(n_neurons=256)
        self.lif2 = snn_ir.LIFCell(n_neurons=128)
        self.readout = snn_ir.Readout(n_classes=10)
    
    def forward(self, spike_events):
        # Event-driven forward pass
        h1 = self.lif1(spike_events)
        h2 = self.lif2(h1)
        return self.readout(h2)

model = EventSNN()
```

#### Step 3: Compile to Hardware
```python
from snn_ir import HardwareCompiler

# Create compiler with target FPGA constraints
compiler = HardwareCompiler(
    target_fpga="xc7a100t",  # Artix-7
    clock_freq=100e6,         # 100 MHz
    max_lut_utilization=0.7   # 70% LUT budget
)

# Compile model to RTL
rtl_code = compiler.compile(model)

# Save Verilog files
with open("snn_top.v", "w") as f:
    f.write(rtl_code)
```

#### Step 4: Event-Driven Processing Engine
```verilog
module event_scheduler (
    input clk,
    input rst,
    input event_valid,
    input [ADDR_WIDTH-1:0] event_addr,
    input [TIME_WIDTH-1:0] event_time,
    output reg process_ready,
    output [ADDR_WIDTH-1:0] scheduled_addr
);
    // Priority queue for event scheduling
    // Time-ordered processing logic
endmodule
```

### Full Code Example
```python
"""
Hardware-Software Co-Design for SNN Deployment
Complete workflow from training to FPGA bitstream.
"""

import torch
import torch.nn as nn
from snn_ir import (
    SNNModel, LIFNeuron, DenseLayer,
    HardwareCompiler, EventProcessor
)

# ==================== Software Model ====================

class CoDesignSNN(SNNModel):
    """SNN model with hardware-aware design."""
    
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        
        # Layer 1: Input → Hidden
        self.layer1 = DenseLayer(
            in_features=input_size,
            out_features=hidden_size,
            neuron_type=LIFNeuron(
                tau_mem=20.0,      # Membrane time constant
                v_thresh=1.0,      # Firing threshold
                v_reset=0.0,       # Reset potential
                surrogate='fast_sigmoid'  # For training
            )
        )
        
        # Layer 2: Hidden → Output
        self.layer2 = DenseLayer(
            in_features=hidden_size,
            out_features=output_size,
            neuron_type=LIFNeuron(
                tau_mem=20.0,
                v_thresh=1.0,
                v_reset=0.0,
                surrogate='fast_sigmoid'
            )
        )
    
    def forward(self, spike_train):
        """
        Forward pass with event-driven execution.
        
        Args:
            spike_train: [batch, time, input_dim] binary spikes
            
        Returns:
            output_spikes: [batch, time, output_dim]
        """
        x = self.layer1(spike_train)
        x = self.layer2(x)
        return x

# ==================== Training ====================

def train_snn(model, dataloader, epochs=10):
    """Train SNN with BPTT."""
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        for batch_idx, (data, targets) in enumerate(dataloader):
            # Convert to spike trains
            spike_train = poisson_encode(data, time_steps=100)
            
            optimizer.zero_grad()
            outputs = model(spike_train)
            
            # Loss on spike counts
            spike_counts = outputs.sum(dim=1)  # [batch, output_dim]
            loss = criterion(spike_counts, targets)
            
            loss.backward()
            optimizer.step()

# ==================== Hardware Compilation ====================

def deploy_to_fpga(model, constraints):
    """Compile trained model to FPGA hardware."""
    
    # Step 1: Analyze model
    analyzer = ModelAnalyzer()
    stats = analyzer.analyze(model)
    print(f"Model stats: {stats}")
    
    # Step 2: Optimize for hardware
    optimizer = HardwareOptimizer(constraints)
    optimized_model = optimizer.optimize(model)
    
    # Step 3: Generate RTL
    compiler = HardwareCompiler(
        target_fpga=constraints['fpga'],
        clock_freq=constraints['freq'],
        optimization='area'  # or 'speed'
    )
    
    rtl = compiler.compile(optimized_model)
    
    # Step 4: Generate constraints
    xdc = compiler.generate_constraints()
    
    return rtl, xdc

# ==================== Event-Driven Inference ====================

class EventDrivenInference:
    """Run inference on FPGA with event-driven processing."""
    
    def __init__(self, bitstream_path):
        self.fpga = FPGAInterface(bitstream_path)
        self.event_queue = []
        
    def process_input(self, input_events):
        """
        Process input events through FPGA.
        
        Args:
            input_events: List of (timestamp, neuron_id) tuples
        """
        # Sort by timestamp
        sorted_events = sorted(input_events, key=lambda x: x[0])
        
        # Send to FPGA via DMA
        self.fpga.send_events(sorted_events)
        
        # Read output events
        output_events = self.fpga.read_output()
        
        return output_events
    
    def classify(self, output_events, num_classes=10):
        """Classify based on output spike counts."""
        spike_counts = [0] * num_classes
        for _, neuron_id in output_events:
            if neuron_id < num_classes:
                spike_counts[neuron_id] += 1
        return spike_counts.index(max(spike_counts))

# ==================== Main Workflow ====================

if __name__ == "__main__":
    # 1. Create model
    model = CoDesignSNN(input_size=784, hidden_size=256, output_size=10)
    
    # 2. Train (software)
    # train_snn(model, train_loader)
    
    # 3. Deploy (hardware)
    constraints = {
        'fpga': 'xc7a100tcsg324-1',
        'freq': 100e6,
        'max_area': 0.8
    }
    rtl, xdc = deploy_to_fpga(model, constraints)
    
    # 4. Synthesize (using Vivado)
    # vivado -mode batch -source synthesize.tcl
    
    # 5. Run inference
    # inference_engine = EventDrivenInference('snn.bit')
```

## FPGA Resource Utilization

| Component | LUTs | FFs | BRAM | DSP |
|-----------|------|-----|------|-----|
| Neuron Core (256) | 3,200 | 5,120 | 8 | 0 |
| Synapse Memory | 0 | 0 | 64 | 0 |
| Event Scheduler | 850 | 1,200 | 2 | 0 |
| Controller | 450 | 680 | 0 | 0 |
| **Total** | **4,500** | **7,000** | **74** | **0** |
| **Available (Artix-7)** | **63,400** | **126,800** | **135** | **240** |
| **Utilization** | **7.1%** | **5.5%** | **54.8%** | **0%** |

## Performance Comparison

| Platform | Latency | Power | Cost | Accuracy |
|----------|---------|-------|------|----------|
| GPU (RTX 3090) | 0.5 ms | 350W | $1,500 | 95.2% |
| CPU (i9) | 12 ms | 125W | $500 | 95.2% |
| **This Work (Artix-7)** | **2.1 ms** | **1.2W** | **$99** | **94.8%** |
| Loihi | 1.5 ms | 0.5W | N/A | 94.5% |

## Applications

- **Real-time Sensor Processing**: Always-on edge devices
- **Neuromorphic Robotics**: Low-latency motor control
- **Wearable BCI**: Portable brain-computer interfaces
- **Smart Sensors**: Event-based vision/audio processing

## Pitfalls

1. **Fixed Network Topology**: Post-deployment changes require re-synthesis
2. **Quantization Effects**: 8-16 bit weights may reduce accuracy
3. **Memory Bandwidth**: Event throughput limited by BRAM access
4. **Debugging Difficulty**: Hardware issues harder to diagnose than software

## Related Skills
- multiplication-free-spike-time-fpga
- spikingjelly-framework
- snn-fpga-deployment
- event-driven-neuromorphic-transceiver

## References
```bibtex
@article{lee2026hardware,
  title={Hardware-Software Co-Design for Event-Driven SNN Deployment on Low-Cost Neuromorphic FPGAs},
  author={Lee, Jiwoon and Chakraborty, Souvik and Alam, Syed Bahauddin and Roy, Kaushik},
  journal={arXiv preprint arXiv:2604.22179},
  year={2026}
}
```
