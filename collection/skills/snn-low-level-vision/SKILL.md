---
name: snn-low-level-vision
description: Spiking Neural Network approaches for low-level vision tasks including edge detection, denoising, and optical flow using event-based processing.
version: 1.0.0
metadata:
  hermes:
    tags: [snn, vision, neuromorphic, low-level-vision]
---

# SNN Low-Level Vision Processing

## Overview
Event-based low-level vision using Spiking Neural Networks for energy-efficient image processing tasks.

## Key Tasks
- Edge detection via spatiotemporal spike patterns
- Denoising through lateral inhibition networks
- Optical flow using direction-selective neurons

## Implementation Pattern
```python
class SpikingEdgeDetector:
    '''Event-based edge detection using SNN.'''
    def __init__(self, threshold=1.0, tau=10.0):
        self.threshold = threshold
        self.tau = tau  # membrane time constant
        
    def process_event(self, event, spikes):
        '''Process a single event and produce edge spikes.'''
        # Lateral inhibition for edge enhancement
        local_activity = self.gather_local_spikes(event, spikes)
        net_input = event.polarity - local_activity
        return net_input > self.threshold
```

## Activation Keywords

- "snn-low-level-vision"
- "snn low level vision"
- "use snn low level vision"
- "snn low level vision help"
- "snn low level vision tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Snn Low Level Vision usage
```
User: "Help me with snn low level vision"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed snn low level vision assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
