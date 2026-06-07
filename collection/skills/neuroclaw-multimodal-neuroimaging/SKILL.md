---
name: neuroclaw-multimodal-neuroimaging
description: "NeuroClaw - Domain-specialized multi-agent research assistant for executable and reproducible neuroimaging research. Supports heterogeneous modalities (sMRI, fMRI, dMRI, EEG), BIDS metadata integration, environment management, and three-tier skill/agent hierarchy. Use for automated neuroimaging pipelines, reproducible research workflows, and multi-modal brain data analysis. Keywords: neuroimaging, BIDS, multi-agent, reproducible research, fMRI, sMRI, dMRI, EEG."
---

# NeuroClaw: Multi-Agent Neuroimaging Research Assistant

NeuroClaw is a domain-specialized multi-agent research assistant designed for executable and reproducible neuroimaging research. It operates directly on raw neuroimaging data across formats and modalities.

## Core Features

### Multi-Modal Support
- **sMRI**: Structural MRI (T1w, T2w)
- **fMRI**: Functional MRI (resting-state, task-based)
- **dMRI**: Diffusion MRI (DTI, HARDI)
- **EEG**: Electroencephalography
- **PET**: Positron Emission Tomography (optional)

### BIDS Integration

NeuroClaw grounds decisions in **BIDS (Brain Imaging Data Structure)** metadata:

```python
# Example BIDS dataset query
from bids import BIDSLayout

layout = BIDSLayout('/data/my_study')
subjects = layout.get_subjects()
sessions = layout.get_sessions()

# Get all T1-weighted images
t1w_files = layout.get(suffix='T1w', extension='nii.gz')

# Get fMRI runs for task
task_fmri = layout.get(
    suffix='bold', 
    task='rest', 
    extension='nii.gz'
)
```

## Architecture

### Three-Tier Skill/Agent Hierarchy

```
┌─────────────────────────────────────────────────────────┐
│  Tier 1: User-Facing Interaction                        │
│  - Natural language interface                           │
│  - Intent parsing                                       │
│  - Response formatting                                  │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  Tier 2: High-Level Orchestration                       │
│  - Pipeline planning                                    │
│  - Resource allocation                                  │
│  - Quality control                                      │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│  Tier 3: Low-Level Tool Skills                          │
│  - FSL, ANTs, FreeSurfer, Nilearn                       │
│  - Preprocessing, analysis, visualization               │
│  - Checkpointing, verification                          │
└─────────────────────────────────────────────────────────┘
```

## Environment Management

### Pinned Python Environments

```yaml
# environment.yml
name: neuroclaw
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy=1.24.0
  - scipy=1.11.0
  - nibabel=5.1.0
  - nilearn=0.10.0
  - ants=2.5.0
  - pip
  - pip:
    - pybids==0.16.0
    - neuroclaw==0.1.0
```

### Docker Support

```dockerfile
# Dockerfile
FROM neurodebian:bullseye

# Install NeuroClaw
RUN pip install neuroclaw

# Install neuroimaging tools
RUN apt-get update && apt-get install -y \
    fsl-core \
    ants \
    afni \
    && rm -rf /var/lib/apt/lists/*

# Set up BIDS validator
RUN npm install -g bids-validator

ENTRYPOINT ["neuroclaw"]
```

### GPU Configuration

```python
# GPU resource management
from neuroclaw.resources import GPUManager

gpu_mgr = GPUManager()

# Request GPU for deep learning pipeline
with gpu_mgr.allocate(gpu_ids=[0], memory_fraction=0.8) as gpu:
    results = run_dl_pipeline(data, device=gpu.device)
```

## Reproducibility Features

### Checkpointing

```python
from neuroclaw.checkpoint import CheckpointManager

checkpoint_mgr = CheckpointManager(
    checkpoint_dir='./checkpoints',
    save_interval=300  # Save every 5 minutes
)

# Enable checkpointing for pipeline
@checkpoint_mgr.checkpoint
def preprocessing_pipeline(raw_data):
    # Step 1: Brain extraction
    brain = extract_brain(raw_data)
    checkpoint_mgr.save(step='brain_extraction', data=brain)
    
    # Step 2: Registration
    registered = register_to_mni(brain)
    checkpoint_mgr.save(step='registration', data=registered)
    
    return registered
```

### Post-Execution Verification

```python
from neuroclaw.verification import verify_outputs

# Verify pipeline outputs
verification_results = verify_outputs(
    expected_outputs=['brain_mask.nii.gz', 'registered.nii.gz'],
    actual_outputs=output_dir,
    checksums=True,
    metadata_check=True
)

if not verification_results.valid:
    print(f"Verification failed: {verification_results.errors}")
```

### Structured Audit Traces

```python
from neuroclaw.audit import AuditLogger

audit = AuditLogger()

# Log pipeline execution
with audit.session() as session:
    session.log_start(pipeline_name='fmri_preprocess')
    session.log_tool('fsl', version='6.0.5')
    session.log_parameters({'smoothing_fwhm': 6, 'high_pass': 0.01})
    session.log_end(status='success', duration=3600)

# Generate audit report
report = audit.generate_report(format='html')
```

## Workflow Examples

### Example 1: fMRI Preprocessing Pipeline

```python
from neuroclaw import NeuroClawAgent

# Initialize agent
agent = NeuroClawAgent(
    dataset_path='/data/my_fmri_study',
    output_dir='/output/preprocessed'
)

# Define preprocessing workflow
workflow = agent.create_workflow()

# Add preprocessing steps
workflow.add_step(
    name='motion_correction',
    tool='mcflirt',
    inputs={'in_file': 'bold.nii.gz'}
)

workflow.add_step(
    name='brain_extraction',
    tool='bet',
    inputs={'in_file': '{motion_correction.out}'}
)

workflow.add_step(
    name='registration',
    tool='flirt',
    inputs={
        'in_file': '{brain_extraction.out}',
        'ref': 'MNI152_T1_2mm_brain.nii.gz'
    }
)

workflow.add_step(
    name='smoothing',
    tool='fslmaths',
    inputs={
        'in_file': '{registration.out}',
        'fwhm': 6
    }
)

# Execute workflow
results = workflow.execute()
```

### Example 2: Multi-Modal Analysis

```python
# Multi-modal integration
from neuroclaw.multimodal import MultiModalAnalysis

mma = MultiModalAnalysis()

# Add different modalities
mma.add_modality(
    name='structural',
    data='t1w.nii.gz',
    type='sMRI'
)

mma.add_modality(
    name='functional',
    data='bold.nii.gz',
    type='fMRI',
    task='rest'
)

mma.add_modality(
    name='diffusion',
    data='dwi.nii.gz',
    type='dMRI',
    bvals='bvals.txt',
    bvecs='bvecs.txt'
)

# Run cross-modal analysis
connectivity = mma.analyze_connectivity(
    method='structural_functional_coupling'
)
```

### Example 3: Quality Control Automation

```python
from neuroclaw.qc import QualityControl

qc = QualityControl()

# Define QC criteria
criteria = {
    'motion': {'threshold': 0.5, 'metric': 'mean_fd'},
    'tSNR': {'threshold': 50, 'metric': 'temporal_snr'},
    'coregistration': {'threshold': 0.9, 'metric': 'dice_overlap'}
}

# Run QC on dataset
qc_results = qc.evaluate_dataset(
    dataset_path='/data/processed',
    criteria=criteria
)

# Generate QC report
qc_report = qc.generate_report(
    results=qc_results,
    format='html',
    include_visualizations=True
)
```

## NeuroBench: System-Level Benchmark

### Benchmark Categories

1. **Executability**: Can the pipeline run successfully?
2. **Artifact Validity**: Are outputs scientifically valid?
3. **Reproducibility Readiness**: Can results be reproduced?

### Benchmark Execution

```python
from neuroclaw.benchmark import NeuroBench

bench = NeuroBench()

# Run benchmark on task
results = bench.evaluate(
    task='fmri_preprocessing',
    dataset='ds000117',  # OpenNeuro dataset
    models=['gpt-4', 'claude-3', 'neuroclaw']
)

# Compare results
comparison = bench.compare(results)
print(comparison.summary())
```

### Expected Improvements

Compared with direct agent invocation:
- **Consistent score improvements** across multiple multimodal LLMs
- **Higher executability** due to environment management
- **Better artifact validity** via post-execution verification
- **Improved reproducibility** through structured audit traces

## Tool Integration

### Supported Tools

| Tool | Purpose | Integration |
|------|---------|-------------|
| FSL | fMRI analysis | Full API |
| ANTs | Registration | Full API |
| FreeSurfer | Cortical analysis | Surface support |
| Nilearn | Python neuroimaging | Native |
| DIPY | Diffusion analysis | Pipeline integration |
| MNE | EEG/MEG analysis | Multi-modal |

### Custom Tool Integration

```python
from neuroclaw.tools import ToolRegistry

registry = ToolRegistry()

# Register custom tool
@registry.register(
    name='my_custom_tool',
    version='1.0.0',
    inputs=['nifti_file'],
    outputs=['processed_file']
)
def my_custom_tool(input_file, output_dir):
    # Custom processing logic
    result = process(input_file)
    return save(result, output_dir)
```

## Best Practices

### 1. Dataset Organization

```
my_study/
├── dataset_description.json
├── participants.tsv
├── sub-01/
│   ├── anat/
│   │   └── sub-01_T1w.nii.gz
│   └── func/
│       ├── sub-01_task-rest_bold.nii.gz
│       └── sub-01_task-rest_events.tsv
└── sub-02/
    └── ...
```

### 2. Pipeline Documentation

```python
# Document pipeline with metadata
workflow = agent.create_workflow(
    name='resting_state_preprocessing',
    description='Standard preprocessing for resting-state fMRI',
    citation='Power et al., 2017'
)
```

### 3. Error Handling

```python
from neuroclaw.error import PipelineError

try:
    results = workflow.execute()
except PipelineError as e:
    # Auto-recovery or graceful degradation
    recovery = agent.handle_error(e, strategy='retry_with_fallback')
```

## References

- Paper: arXiv:2604.24696v1 [cs.CV]
- Title: "NeuroClaw Technical Report"
- Authors: Cheng Wang, Zhibin He, Zhihao Peng, et al.
- Homepage: https://cuhk-aim-group.github.io/NeuroClaw/

## Related Skills

- `homology-morphometry-brain-atrophy`: Topological brain analysis
- `bandrouternet-eeg-artifact`: EEG artifact removal
- `brain-network-controllability`: Network control theory

## Activation Keywords

- neuroimaging pipeline
- BIDS neuroimaging
- fMRI preprocessing
- multi-modal brain data
- neuroimaging reproducibility
- 神经影像处理
- 多模态脑成像
- 神经影像可重复性
