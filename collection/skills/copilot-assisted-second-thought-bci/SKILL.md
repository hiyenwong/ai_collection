---
name: copilot-assisted-second-thought-bci
description: >
  Copilot-Assisted Second-Thought Framework for EEG-to-robot motion decoding.
  Uses LLMs as copilot to refine motor kinematics predictions from EEG signals.
  Improves BCI decoding accuracy through iterative refinement.
  Activation: BCI, brain-computer interface, EEG decoding, motor kinematics,
  robot control, EEG-to-robot, second-thought framework, EEG prediction,
  脑机接口, 脑电解码, 运动学预测
version: 1.0.0
metadata:
  hermes:
    source_paper: "Copilot-Assisted Second-Thought Framework for Brain-to-Robot Hand Motion Decoding"
    arxiv_id: "2603.27492"
    citations: 0
    tags: [bci, eeg, motor-decoding, llm-copilot, kinematics]
---

# Copilot-Assisted Second-Thought Framework for BCI

## Overview

Framework that improves EEG-to-robot hand motion decoding using an LLM as a "copilot" for second-thought refinement. Motor kinematics prediction from EEG is noisy; this approach uses the LLM to iteratively refine predictions, leveraging its understanding of plausible human motion patterns.

## Core Architecture

```
EEG Signal → Initial Decoder (MLP/Transformer) → LLM Copilot → Refined Motion Output
```

### Phase 1: Initial Decoding
- Encode EEG signals using standard architecture (e.g., DeepConvNet, EEGNet)
- Predict raw motor kinematics (joint angles, velocities, positions)
- Output: initial kinematic trajectory with noise/artifacts

### Phase 2: LLM Copilot Refinement
- Convert kinematic predictions to text representation
- Prompt LLM with:
  - Current prediction
  - Physical constraints (joint limits, smoothness priors)
  - Task context (what movement is expected)
- LLM applies biomechanical reasoning to refine output

## Key Components

1. **EEG Feature Extractor**: Standard EEG decoding network
2. **Kinematic Predictor**: Maps neural features to motor parameters
3. **LLM Copilot**: Refines predictions using biomechanical knowledge
4. **Constraint Layer**: Ensures physical plausibility

## Implementation Pattern

```python
class CopilotBCIDecoder:
    def __init__(self, eeg_model, llm_client, constraints):
        self.eeg_model = eeg_model
        self.llm = llm_client
        self.constraints = constraints
    
    def decode(self, eeg_signal, task_context=""):
        # Phase 1: Initial prediction
        kinematics = self.eeg_model(eeg_signal)
        
        # Phase 2: LLM refinement
        prompt = self._build_prompt(kinematics, task_context)
        refined = self.llm.generate(prompt)
        
        # Apply physical constraints
        return self._apply_constraints(refined)
    
    def _build_prompt(self, kinematics, context):
        return (
            f"Refine this predicted hand trajectory for physical plausibility.\n"
            f"Joint limits: {self.constraints['joint_limits']}\n"
            f"Context: {context}\n"
            f"Current prediction: {kinematics}\n"
            f"Return refined trajectory respecting biomechanical constraints."
        )
```

## Applications

- Brain-controlled robotic arm manipulation
- EEG-based prosthetic control
- Rehabilitation BCI systems
- Hands-free device control

## References

- arXiv:2603.27492
- Related skills: eeg-foundation-models, eeg-ieeg-bridge
