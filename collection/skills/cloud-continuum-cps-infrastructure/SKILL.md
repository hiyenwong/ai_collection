---
name: cloud-continuum-cps-infrastructure
title: Cloud Continuum Research Infrastructure for Distributed CPS
version: 1.0.0
description: Two-level reference architecture for Cloud Continuum experimentation separating research-infrastructure layer from application layer with Edge-Fog-Cloud patterns.
trigger: When designing or implementing distributed Cyber-Physical Systems across Edge, Fog, and Cloud resources.
---

# Cloud Continuum Research Infrastructure for Distributed CPS

## Overview
This skill implements the methodology from arXiv:2607.28193 "A Cloud Continuum Research Infrastructure for Distributed CPS Experimentation" by Mirto et al. The approach provides a two-level reference architecture built on the SLICES Cloud Continuum Blueprint that separates:

1. **Research-Infrastructure Layer**: Exposes and manages distributed Edge, Fog, Cloud, and HPC resources
2. **Application Layer**: Organizes Cyber-Physical workflows using Edge-Fog-Cloud patterns with first-class treatment of placement, timing, and data provenance

## Key Architecture Principles

### Two-Level Separation
- **Infrastructure Independence**: Applications can be deployed across different programmable substrates without modification
- **Resource Abstraction**: Heterogeneous resources (physical/virtualized edge, fog nodes, cloud instances) are uniformly exposed
- **Experimental Control**: Placement, timing, and data flow are explicit experimental variables

### Edge-Fog-Cloud Pattern
- **Edge Layer**: Low-latency sensing, safety actions, physical device interaction
- **Fog Layer**: Near-source coordination, mediation, stream processing, local decision making  
- **Cloud Layer**: Global knowledge consolidation, analytics, optimization, visualization

### First-Class Experimental Concerns
- **Placement**: Explicit control over where components execute (edge vs fog vs cloud)
- **Timing**: Precise timing constraints and synchronization across distributed components
- **Data Provenance**: Complete tracking of data lineage from edge sensors to cloud analytics

## Implementation Steps

### 1. Infrastructure Setup
```yaml
# Example infrastructure configuration
infrastructure:
  edge_nodes:
    - type: physical
      location: site_a
      capabilities: [sensing, actuation, real-time]
    - type: virtualized  
      location: site_b
      capabilities: [container_runtime, low_latency]
  fog_nodes:
    - type: server
      location: regional_center
      capabilities: [stream_processing, coordination]
  cloud_resources:
    - type: cloud_instance
      provider: aws_gcp_azure
      capabilities: [analytics, storage, visualization]
```

### 2. Application Layer Design
- Define CPS workflow as directed acyclic graph (DAG) of tasks
- Annotate each task with resource requirements and constraints
- Specify data dependencies and communication patterns
- Define timing requirements (latency bounds, synchronization points)

### 3. Deployment Strategy
- Map application tasks to infrastructure resources based on constraints
- Implement data routing between Edge-Fog-Cloud layers
- Configure monitoring and observability across all layers
- Set up experiment orchestration for systematic evaluation

### 4. Evaluation Framework
- **Reproducibility**: Ensure identical deployments across experiment runs
- **Observability**: Monitor performance metrics at all layers (latency, throughput, resource usage)
- **Control Variables**: Systematically vary placement, timing, and resource types
- **Workload Patterns**: Test with representative use cases (Renewable Energy Community, AirWatch)

## Use Cases

### Renewable Energy Community Management
- **Edge**: Local energy generation/consumption monitoring, safety controls
- **Fog**: Time-window-based energy coordination, local optimization
- **Cloud**: Global energy trading, long-term forecasting, visualization

### AirWatch Monitoring Pipeline  
- **Edge**: Sensor data collection, anomaly detection, low-latency alerts
- **Fog**: Stream aggregation, local correlation analysis, alert filtering
- **Cloud**: Historical analysis, pattern recognition, dashboard visualization

## Validation Methodology
The original paper validates the approach through:
- **40 experimental runs** comparing virtualized vs physical edge deployments
- **Geographically distributed infrastructure** across multiple sites
- **Systematic comparison** of alternative control and monitoring strategies
- **Performance metrics**: Latency, throughput, resource utilization, reliability

## Benefits
- **Multi-application support**: Single infrastructure supports diverse CPS workloads
- **Comparative research**: Enables fair comparison of alternative approaches
- **Reproducibility**: Standardized experimental environment
- **Scalability**: Supports geographically distributed deployments
- **Flexibility**: Accommodates both physical and virtualized resources

## References
- **Primary Paper**: Mirto, F. O., Tricomi, G., D'Agati, L., Sabbioni, A., Silvestri, S., Longo, F., Merlino, G., Bujari, A., Bellavista, P., & Puliafito, A. (2026). A Cloud Continuum Research Infrastructure for Distributed CPS Experimentation. arXiv:2607.28193 [cs.DC]
- **Foundation**: SLICES Cloud Continuum Blueprint
- **Target Journal**: Elsevier Future Generation Computer Systems

## Activation Keywords
cloud continuum, distributed CPS, edge-fog-cloud, research infrastructure, SLICES, cyber-physical systems, distributed experimentation, placement optimization, timing constraints, data provenance, renewable energy community, AirWatch, heterogeneous resources