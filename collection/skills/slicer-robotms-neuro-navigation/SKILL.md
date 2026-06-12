---
name: slicer-robotms-neuro-navigation
description: "Open-source 3D Slicer extension for robot-assisted transcranial magnetic stimulation (Robo-TMS). Enables accurate, reproducible non-invasive brain stimulation with image-guided robotic intervention. Activation: robot TMS, Robo-TMS, Slicer extension, TMS navigation, transcranial magnetic stimulation robot, neurostimulation robotic."
---

# SlicerRoboTMS: Robot-Assisted TMS Navigation

> An open-source 3D Slicer extension that enables robot-assisted transcranial magnetic stimulation, combining image guidance with robotic precision for accurate and reproducible non-invasive brain stimulation.

## Metadata
- **Source**: arXiv:2604.25661v1  
- **Published**: 2026-04-28
- **Category**: Neurostimulation / Robotic Intervention

## Core Methodology

### Key Innovation
**SlicerRoboTMS** bridges the gap between conventional manual TMS and fully automated robotic systems by providing an **open-source, extensible platform** built on the widely-used 3D Slicer medical imaging software. This enables clinical researchers to implement robot-assisted TMS without proprietary vendor lock-in.

### Technical Framework

#### Robot-Assisted TMS (Robo-TMS)
- **Image-guided intervention**: Uses MRI/CT data for precise coil positioning
- **Robotic accuracy**: Sub-millimeter precision for coil placement
- **Reproducibility**: Eliminates inter-operator variability
- **Real-time tracking**: Continuous position verification during stimulation

#### 3D Slicer Integration
- **Modular architecture**: Leverages 3D Slicer's plugin ecosystem
- **Multi-modal imaging**: Supports MRI, CT, fMRI navigation
- **Visualization**: Real-time 3D visualization of coil-brain relationship
- **Open-source**: Extensible and customizable for research needs

### Clinical Applications

#### Standard TMS Targets
- **Dorsolateral prefrontal cortex (DLPFC)**: Depression treatment
- **Motor cortex**: Motor evoked potential (MEP) studies
- **Visual cortex**: Phosphene threshold mapping
- **Language areas**: Pre-surgical language mapping

#### Research Applications
- **Connectivity mapping**: TMS-fMRI integration
- **Plasticity studies**: Paired associative stimulation
- **Cognitive modulation**: Working memory, attention studies
- **Rehabilitation**: Post-stroke motor recovery

## Implementation Guide

### Prerequisites
- **Hardware**: 
  - Compatible robotic arm (e.g., Kinova, Franka, Universal Robots)
  - TMS coil with tracking markers
  - Optical tracking system (e.g., NDI Polaris, OptiTrack)
- **Software**:
  - 3D Slicer (latest stable version)
  - SlicerRoboTMS extension
  - Robot control interface

### Setup Workflow

#### 1. Imaging and Planning
```
1. Acquire high-resolution T1-weighted MRI
2. Import into 3D Slicer
3. Perform brain segmentation and surface reconstruction
4. Identify stimulation targets using atlases or fMRI
5. Plan coil trajectory and orientation
```

#### 2. Registration and Calibration
```
1. Register patient space to image space
2. Calibrate robot coordinate system
3. Verify tracking system alignment
4. Test coil positioning accuracy
```

#### 3. Intervention Execution
```
1. Load stimulation protocol
2. Execute robot-assisted positioning
3. Verify coil-target relationship
4. Deliver stimulation with real-time monitoring
5. Log position data for reproducibility
```

### Key Features

#### Precision Control
- **Position accuracy**: < 1mm positioning error
- **Orientation control**: Tilt, rotation, and yaw adjustment
- **Force compliance**: Safe contact with scalp
- **Emergency stops**: Multiple safety interlocks

#### Data Integration
- **Neuronavigation**: Real-time coil-brain distance monitoring
- **Stimulation logging**: Automated session recording
- **Outcome tracking**: Integration with EMG/fMRI data
- **Reproducibility**: Exact session replication capability

## Safety Considerations

### Hardware Safety
- **Collision detection**: Automatic stop on unexpected contact
- **Force limits**: Maximum contact force thresholds
- **Workspace boundaries**: Software-defined safety zones
- **Manual override**: Immediate human operator control

### Clinical Safety
- **Motor threshold**: Individualized intensity calibration
- **Seizure risk**: Contraindication screening
- **Concurrent medications**: Drug interaction awareness
- **Adverse event monitoring**: Standardized reporting

## Advantages Over Manual TMS

| Aspect | Manual TMS | Robo-TMS |
|--------|------------|----------|
| Positioning accuracy | Operator-dependent (~5-10mm) | Sub-millimeter |
| Session reproducibility | Low | High |
| Multi-session targeting | Variable | Consistent |
| Operator fatigue | Significant | None |
| Integration with imaging | Limited | Seamless |
| Complex trajectories | Difficult | Automated |

## Limitations

1. **Setup time**: Initial calibration requires additional time
2. **Cost**: Robotic hardware investment
3. **Training**: Operators need robotics training
4. **Emergency protocols**: Requires defined failure modes
5. **Movement compensation**: Patient motion during stimulation

## Related Skills
- `brain-stimulation-dynamics-state`: Brain stimulation network effects
- `tms-eeg-biomarkers`: TMS-EEG biomarker assessment
- `neural-digital-twins-bci`: Neural modeling for BCI
- `neurocybernetic-large-scale-neuroscience`: Neurocybernetic modeling

## References
- SlicerRoboTMS: An Open-Source 3D Slicer Extension for Robot-Assisted Transcranial Magnetic Stimulation. arXiv:2604.25661v1
- 3D Slicer: https://www.slicer.org/
