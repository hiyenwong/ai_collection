---
name: bci-rehabilitation-protocols
description: Optimized BCI rehabilitation protocols for stroke recovery. Addresses task design, training duration, and neuroplasticity-driven adaptation for maximizing post-stroke motor recovery through brain-computer interfaces.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, bci, rehabilitation, stroke, neuroplasticity, motor-recovery, clinical]
    source_paper: "Optimizing BCI Rehabilitation Protocols for Stroke: Exploring Task Design and Training Duration (arXiv:2510.08082v1)"
---

# BCI Rehabilitation Protocols for Stroke Recovery

## Overview

This research optimizes brain-computer interface (BCI) rehabilitation protocols for stroke patients by systematically investigating **task design** and **training duration** effects on motor recovery outcomes. The study provides evidence-based guidelines for structuring BCI therapy sessions, selecting appropriate motor imagery tasks, and determining optimal training schedules to maximize neuroplasticity-driven functional recovery.

## Key Insights

1. **Task-Specific Plasticity**: Motor imagery tasks that closely match target recovery functions produce stronger and more specific neuroplastic changes
2. **Training Duration Sweet Spot**: There exists an optimal training duration beyond which additional sessions yield diminishing returns (identified as ~20-30 sessions)
3. **Adaptive Difficulty**: Progressively increasing task difficulty maintains engagement and promotes continued neuroplasticity
4. **Multi-Modal Feedback**: Combining visual, proprioceptive, and auditory feedback enhances motor learning and cortical reorganization

## Protocol Framework

```
┌─────────────────────────────────────────────────────────┐
│          BCI Stroke Rehabilitation Protocol              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Phase 1: Assessment                                    │
│  ┌──────────────────────────────────────────────────┐   │
│  │ • Baseline motor function evaluation             │   │
│  │ • EEG/BCI calibration session                    │   │
│  │ • Individual motor imagery capability screening  │   │
│  └────────────────────┬─────────────────────────────┘   │
│                       │                                 │
│  Phase 2: Training (Adaptive)                           │
│  ┌────────────────────▼─────────────────────────────┐   │
│  │ • Session 1-10: Basic motor imagery              │   │
│  │   (single joint, simple feedback)                 │   │
│  │ • Session 11-20: Complex motor imagery            │   │
│  │   (multi-joint, multi-modal feedback)             │   │
│  │ • Session 21-30: Functional task training         │   │
│  │   (goal-directed, real-world tasks)               │   │
│  └────────────────────┬─────────────────────────────┘   │
│                       │                                 │
│  Phase 3: Consolidation                                 │
│  ┌────────────────────▼─────────────────────────────┐   │
│  │ • Transfer to unassisted movement                │   │
│  │ • Home-based maintenance program                 │   │
│  │ • Long-term outcome assessment                   │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Implementation Pattern

```python
import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum

class RehabPhase(Enum):
    ASSESSMENT = "assessment"
    BASIC_TRAINING = "basic_training"
    COMPLEX_TRAINING = "complex_training"
    FUNCTIONAL_TRAINING = "functional_training"
    CONSOLIDATION = "consolidation"

@dataclass
class PatientState:
    """Tracks patient progress through rehabilitation."""
    session_number: int
    motor_score: float        # Fugl-Meyer or similar score
    bci_accuracy: float       # Motor imagery classification accuracy
    engagement_level: float   # 0-1 engagement metric
    neuroplasticity_index: float  # EEG-based plasticity marker

class BCIRehabProtocol:
    """
    Adaptive BCI rehabilitation protocol for stroke recovery.
    
    Manages:
    - Phase progression based on patient performance
    - Task difficulty adaptation
    - Training session optimization
    - Neuroplasticity monitoring
    """
    
    # Protocol parameters
    SESSIONS_PER_PHASE = 10
    MAX_SESSIONS = 30
    ACCURACY_THRESHOLD = 0.75  # Minimum BCI accuracy to advance phase
    
    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.current_phase = RehabPhase.ASSESSMENT
        self.session_number = 0
        self.history = []
        
        # Task parameters per phase
        self.task_configs = {
            RehabPhase.BASIC_TRAINING: {
                'n_classes': 2,           # 2 motor imagery classes
                'feedback_modality': 'visual',
                'trial_duration': 8.0,    # seconds
                'n_trials': 40,
                'difficulty': 0.3
            },
            RehabPhase.COMPLEX_TRAINING: {
                'n_classes': 4,           # 4 motor imagery classes
                'feedback_modality': 'visual+proprioceptive',
                'trial_duration': 6.0,
                'n_trials': 60,
                'difficulty': 0.5
            },
            RehabPhase.FUNCTIONAL_TRAINING: {
                'n_classes': 4,
                'feedback_modality': 'visual+proprioceptive+auditory',
                'trial_duration': 5.0,
                'n_trials': 80,
                'difficulty': 0.7
            }
        }
    
    def get_session_config(self, patient: PatientState) -> dict:
        """Get optimized session configuration for current patient state."""
        phase = self._determine_phase(patient)
        config = self.task_configs[phase].copy()
        
        # Adapt difficulty based on recent performance
        if patient.bci_accuracy > 0.85:
            config['difficulty'] = min(config['difficulty'] + 0.1, 1.0)
        elif patient.bci_accuracy < 0.55:
            config['difficulty'] = max(config['difficulty'] - 0.1, 0.1)
        
        return config
    
    def _determine_phase(self, patient: PatientState) -> RehabPhase:
        """Determine appropriate rehabilitation phase."""
        if self.session_number == 0:
            return RehabPhase.ASSESSMENT
        
        sessions_in_current = self.session_number % self.SESSIONS_PER_PHASE
        
        # Phase advancement criteria
        if patient.bci_accuracy >= self.ACCURACY_THRESHOLD and sessions_in_current >= 5:
            if self.current_phase == RehabPhase.BASIC_TRAINING:
                self.current_phase = RehabPhase.COMPLEX_TRAINING
            elif self.current_phase == RehabPhase.COMPLEX_TRAINING:
                self.current_phase = RehabPhase.FUNCTIONAL_TRAINING
        
        # Check for consolidation phase
        if self.session_number >= self.MAX_SESSIONS:
            self.current_phase = RehabPhase.CONSOLIDATION
        
        return self.current_phase
    
    def compute_neuroplasticity_index(
        self,
        baseline_eeg: np.ndarray,
        current_eeg: np.ndarray
    ) -> float:
        """
        Compute EEG-based neuroplasticity index.
        
        Measures spectral power changes in motor-related bands
        (mu and beta rhythms) indicating cortical reorganization.
        """
        # Power in mu band (8-13 Hz) and beta band (13-30 Hz)
        def band_power(signal, low, high):
            # Simplified: assume signal is already band-filtered
            return np.mean(signal ** 2)
        
        mu_change = (band_power(current_eeg, 8, 13) / 
                     (band_power(baseline_eeg, 8, 13) + 1e-10))
        beta_change = (band_power(current_eeg, 13, 30) / 
                       (band_power(baseline_eeg, 13, 30) + 1e-10))
        
        # Plasticity index: normalized change
        return np.clip((mu_change + beta_change - 2.0) / 2.0, -1, 1)
    
    def evaluate_recovery_trajectory(
        self, history: List[PatientState]
    ) -> dict:
        """Evaluate patient recovery trajectory and predict outcome."""
        if len(history) < 3:
            return {'status': 'insufficient_data', 'prediction': None}
        
        scores = [p.motor_score for p in history]
        # Simple linear trend
        x = np.arange(len(scores))
        slope = np.polyfit(x, scores, 1)[0]
        
        if slope > 0.5:
            status = 'excellent_progress'
        elif slope > 0.2:
            status = 'good_progress'
        elif slope > 0:
            status = 'slow_progress'
        else:
            status = 'plateau'
        
        # Predict final score
        remaining = self.MAX_SESSIONS - len(history)
        predicted_final = scores[-1] + slope * remaining
        
        return {
            'status': status,
            'slope': slope,
            'predicted_final_score': predicted_final,
            'sessions_completed': len(history),
            'sessions_remaining': remaining
        }
```

## Evidence-Based Guidelines

| Parameter | Recommendation | Evidence Level |
|-----------|----------------|----------------|
| Session frequency | 3-5 sessions/week | Strong |
| Session duration | 45-60 minutes | Moderate |
| Total sessions | 20-30 for optimal gains | Strong |
| Task progression | 2→4 class motor imagery | Moderate |
| Feedback modality | Multi-modal (visual+proprioceptive+auditory) | Strong |
| Rest intervals | 2-3 minutes between blocks | Moderate |

## Applications

1. **Stroke Rehabilitation**: Evidence-based BCI therapy protocols
2. **Spinal Cord Injury**: Motor function recovery programs
3. **Neurorehabilitation Clinics**: Standardized BCI therapy workflows
4. **Home-Based Therapy**: Remote rehabilitation monitoring
5. **Clinical Trials**: Standardized outcome measures for BCI studies

## Key Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| `sessions_per_phase` | Sessions before phase advancement | 8-12 |
| `accuracy_threshold` | BCI accuracy for phase advancement | 0.7-0.8 |
| `max_sessions` | Total protocol sessions | 20-40 |
| `trial_duration` | Motor imagery trial length (seconds) | 4-8 |

## Activation Keywords

- BCI rehabilitation
- stroke recovery protocol
- motor imagery training
- neurorehabilitation BCI
- post-stroke BCI
- adaptive rehabilitation
- 脑机接口康复
- 卒中康复协议
- 运动想象训练

## References

- **Original Paper**: Optimizing BCI Rehabilitation Protocols for Stroke: Exploring Task Design and Training Duration. arXiv:2510.08082v1 (2025)
- **Related Skills**: [[neural-digital-twins-bci]], [[eeg-foundation-model-adapters]], [[neural-brain-framework]]

## Limitations

- Protocol efficacy depends on individual BCI literacy
- Stroke severity and lesion location affect outcomes
- Requires trained personnel for setup and monitoring
- Long-term maintenance effects need further study
