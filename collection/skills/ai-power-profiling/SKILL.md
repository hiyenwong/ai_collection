---
name: ai-power-profiling
description: Measuring and modeling power consumption profiles of generative AI workloads for data center infrastructure planning. Use when: GPU power profiling, data center energy modeling, AI workload characterization, infrastructure planning, power measurement methodology, HPC facility design, generative AI training/inference power analysis, or energy-aware computing.
---

# AI Power Profiling for Data Center Infrastructure

## Overview

This skill provides methodology for measuring generative AI workload power profiles at high resolution (0.1s) and scaling measurements to whole-facility energy demand for infrastructure planning. Addresses the challenge of proprietary and inconsistent power consumption data for AI workloads.

**Key Innovation**: Bridges the gap between high-resolution GPU power measurements and facility-level energy planning using standardized benchmarks and bottom-up modeling.

## Core Problem

### Current Challenges

1. **Proprietary Data**: Power consumption data is largely proprietary
2. **Varying Resolutions**: Data reported at inconsistent time granularities
3. **Missing Context**: Lack of workload characterization alongside power data
4. **Planning Gap**: Difficulty estimating whole-facility energy use
5. **Reproducibility**: No standardized benchmarking for power profiles

### Impact

- Grid connection planning uncertainty
- On-site energy generation sizing
- Microgrid design challenges
- Operational cost estimation errors

## Methodology

### Step 1: High-Resolution Power Measurement

**Equipment Requirements**:
- NVIDIA H100 GPUs (or equivalent high-performance GPUs)
- Power monitoring infrastructure (0.1-second resolution)
- HPC data center facility
- Power measurement software/hardware

**Measurement Resolution**: 0.1 seconds (10 Hz sampling)

**Key Metrics**:
- Instantaneous power consumption (W)
- Average power over workload duration
- Peak power consumption
- Power variance/fluctuations

### Step 2: Workload Characterization

Use standardized benchmarks for reproducibility:

**MLCommons Benchmarks**:
- Training benchmarks
- Fine-tuning benchmarks
- Standardized model architectures
- Reproducible dataset specifications

**vLLM Benchmarks**:
- Inference workload characterization
- Latency vs throughput analysis
- Different inference scenarios
- Batch size variations

**Workload Types**:
1. **AI Training**: Full model training cycles
2. **Fine-tuning**: Pre-trained model adaptation
3. **Inference**: Real-time or batch inference

### Step 3: Create Power Profile Dataset

**Dataset Components**:
- Time-series power measurements (0.1s resolution)
- Workload metadata (model type, size, batch size)
- GPU utilization metrics
- Memory usage profiles
- Duration information

**Data Format**:
```
timestamp    power_watts  gpu_util%  memory_gb  workload_type  model_info
0.0          450          95         40         training       LLM-7B
0.1          452          94         41         training       LLM-7B
0.2          455          96         42         training       LLM-7B
...
```

### Step 4: Whole-Facility Energy Modeling

**Bottom-Up Modeling Approach**:
1. Scale GPU power to server power (include CPU, memory, storage)
2. Scale server power to rack power (networking, cooling overhead)
3. Scale rack power to facility power (HVAC, lighting, infrastructure)

**Event-Driven Model**:
- User behavior patterns drive workload arrivals
- Temporal fluctuations from AI workload mix
- Realistic facility-level energy profiles
- Peak demand estimation

**Scaling Factors**:
```
Server Power = GPU Power × GPU_count + CPU_power + Memory_power + Storage_power + Overhead
Rack Power = Σ(Server Power) + Network_power + Cooling_overhead
Facility Power = Σ(Rack Power) + HVAC + Lighting + Infrastructure + PUE_factor
```

**PUE (Power Usage Effectiveness)**: Typical range 1.2-1.6 for modern data centers

### Step 5: Infrastructure Planning Applications

**Grid Connection Planning**:
- Peak demand estimation
- Average demand calculation
- Capacity requirements
- Connection sizing

**On-Site Energy Generation**:
- Solar/wind sizing
- Battery storage requirements
- Peak shaving strategies
- Renewable integration

**Distributed Microgrids**:
- Multiple facility coordination
- Load balancing strategies
- Backup power sizing
- Grid independence analysis

## Key Findings

### Power Consumption Characteristics

**Training Workloads**:
- High sustained power (450-700W per H100 GPU)
- Longer duration (hours to weeks)
- Higher total energy consumption
- More predictable power profiles

**Fine-tuning Workloads**:
- Medium sustained power (400-600W)
- Moderate duration (hours)
- Variable power based on fine-tuning approach
- Adaptive power profiles

**Inference Workloads**:
- Variable power (300-500W per request)
- Short duration (milliseconds to seconds)
- Bursty power profiles
- Request-rate dependent

### Temporal Fluctuations

**User Behavior Impact**:
- Workload arrivals follow user patterns
- Peak hours vs off-peak variations
- Geographic distribution effects
- Seasonal demand variations

**Realistic Facility Profiles**:
- Not constant power draw
- Significant temporal variation
- Peak-to-average ratio matters for planning
- Duration curves for capacity sizing

## Implementation Workflow

### Phase 1: Setup Measurement Infrastructure

```python
# Example: GPU power monitoring setup
import pynvml

pynvml.nvmlInit()
gpu_count = pynvml.nvmlDeviceGetCount()

def get_power_sample(gpu_index):
    handle = pynvml.nvmlDeviceGetHandleByIndex(gpu_index)
    power = pynvml.nvmlDeviceGetPowerUsage(handle)  # milliwatts
    return power / 1000.0  # convert to watts

# Sample at 0.1s resolution
import time
power_data = []
for _ in range(1000):  # 100 seconds
    sample = {
        'timestamp': time.time(),
        'power': [get_power_sample(i) for i in range(gpu_count)]
    }
    power_data.append(sample)
    time.sleep(0.1)
```

### Phase 2: Run Benchmarks

```bash
# MLCommons training benchmark
mlperf_training --model bert_large --batch_size 32

# vLLM inference benchmark
vllm_benchmark --model llama-7b --requests 1000 --batch_size 16
```

### Phase 3: Collect Power Data

While benchmark runs, collect power samples:
- Record at 0.1s intervals
- Tag with workload metadata
- Store in structured format
- Include GPU utilization metrics

### Phase 4: Create Power Profile Dataset

```python
import pandas as pd

# Organize power data
df = pd.DataFrame(power_data)
df['workload_type'] = 'training'
df['model'] = 'bert_large'
df['batch_size'] = 32

# Save to dataset
df.to_csv('power_profile_training_bert.csv', index=False)
```

### Phase 5: Scale to Facility Level

```python
def estimate_facility_power(gpu_profiles, facility_config):
    """
    Scale GPU power to facility power
    
    Args:
        gpu_profiles: DataFrame with GPU power measurements
        facility_config: Dict with facility parameters
    
    Returns:
        DataFrame with facility power estimates
    """
    # Server-level scaling
    server_power = (
        gpu_profiles['gpu_power'] * facility_config['gpu_per_server'] +
        facility_config['cpu_power'] +
        facility_config['memory_power'] +
        facility_config['storage_power'] +
        facility_config['server_overhead']
    )
    
    # Rack-level scaling
    rack_power = (
        server_power * facility_config['servers_per_rack'] +
        facility_config['network_power'] +
        facility_config['rack_cooling']
    )
    
    # Facility-level scaling
    facility_power = (
        rack_power * facility_config['racks'] +
        facility_config['hvac'] +
        facility_config['lighting'] +
        facility_config['infrastructure']
    ) * facility_config['pue']
    
    return facility_power

# Example facility configuration
facility_config = {
    'gpu_per_server': 8,
    'servers_per_rack': 10,
    'racks': 50,
    'cpu_power': 200,  # W
    'memory_power': 50,  # W per server
    'storage_power': 30,  # W per server
    'server_overhead': 20,  # W
    'network_power': 500,  # W per rack
    'rack_cooling': 1000,  # W per rack
    'hvac': 50000,  # W
    'lighting': 10000,  # W
    'infrastructure': 20000,  # W
    'pue': 1.4
}
```

## Research Applications

### Capacity Planning

**Questions Answered**:
- What peak demand should grid connection support?
- How much on-site generation needed?
- What battery storage capacity required?
- How many GPUs can facility support?

### Energy Optimization

**Use Cases**:
- Workload scheduling to minimize peak demand
- Renewable energy integration timing
- Cooling system optimization
- Power-aware job scheduling

### Cost Estimation

**Benefits**:
- Accurate energy cost predictions
- Operational cost modeling
- Infrastructure investment sizing
- ROI calculations for efficiency measures

## Dataset Availability

**Public Dataset**: Power profile measurements made publicly available

**Dataset Contents**:
- Training workload power profiles
- Fine-tuning power profiles
- Inference power profiles
- Timestamps and metadata
- GPU utilization data

**Reproducibility**: Benchmarks and methods fully documented

## GPU Hardware Reference

**NVIDIA H100 GPU**:
- Peak power: ~700W
- Typical training power: 450-600W
- Typical inference power: 300-500W
- Memory: 80GB HBM3
- Architecture: Hopper

**Power Measurement Tools**:
- nvidia-smi (utility)
- pynvml (Python library)
- dcgm (Data Center GPU Manager)
- Power meters (hardware)

## Facility Infrastructure Components

### Power Infrastructure

- **UPS Systems**: Uninterruptible power supply
- **PDU**: Power distribution units
- **Transformers**: Voltage conversion
- **Switchgear**: Power switching

### Cooling Infrastructure

- **HVAC**: Heating, ventilation, air conditioning
- **Chillers**: Liquid cooling systems
- **CRAC**: Computer room air conditioning
- **Liquid cooling**: Direct-to-chip cooling

### Networking Infrastructure

- **Switches**: Network switches
- **Routers**: Network routers
- **Cabling**: Fiber and copper cables
- **Load balancers**: Traffic distribution

## Research Paper Reference

**Paper**: "Measurement of Generative AI Workload Power Profiles for Whole-Facility Data Center Infrastructure Planning"
- **Authors**: Roberto Vercellino, Jared Willard, Gustavo Campos, et al.
- **arXiv ID**: 2604.07345
- **Published**: April 8, 2026
- **Categories**: eess.SY, cs.DC, cs.LG
- **Link**: https://arxiv.org/abs/2604.07345

## Related Skills

- **data-center-operations**: Facility management
- **energy-aware-computing**: Power optimization
- **gpu-optimization**: GPU performance tuning
- **benchmarking**: Workload characterization

## See Also

- MLCommons benchmark documentation
- vLLM inference benchmark tools
- Data center design guidelines
- Power measurement best practices