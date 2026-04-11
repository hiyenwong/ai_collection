---
name: wattlytics-hpc-optimization
description: Wattlytics - Co-Optimizing Performance, Energy, and TCO in HPC Clusters. Interactive decision-support system for GPU-accelerated computing optimization.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [hpc, gpu, energy-optimization, tco, performance, decision-support]
    source_paper: "Wattlytics: A Web Platform for Co-Optimizing Performance, Energy, and TCO in HPC Clusters (arXiv:2604.08182)"
    citations: 0
    category: distributed computing
---

# Wattlytics: HPC Cluster Optimization

## Overview

This skill provides methodologies for co-optimizing performance, energy consumption, and total cost of ownership (TCO) in GPU-accelerated HPC clusters. Unlike procurement-oriented calculators, this approach integrates benchmark-driven GPU performance scaling analysis with operational energy efficiency metrics.

## Core Concepts

### Multi-Objective Optimization
- **Performance**: Computational throughput (FLOPS, samples/sec)
- **Energy**: Power consumption (Watts, kWh)
- **TCO**: Total cost over system lifetime (CAPEX + OPEX)

### Trade-off Analysis
- Performance vs Energy efficiency
- Capital expenditure vs operational costs
- Short-term vs long-term optimization

## Implementation Pattern

```python
from typing import List, Dict, Tuple
from dataclasses import dataclass
import numpy as np

@dataclass
class HardwareConfig:
    gpu_model: str
    num_gpus: int
    cpu_model: str
    memory_gb: int
    cost_usd: float
    power_watts: float

@dataclass
class BenchmarkResult:
    config: HardwareConfig
    performance_score: float  # Normalized performance
    energy_efficiency: float  # Performance per Watt
    tco_5year: float  # 5-year TCO

class HPCOptimizer:
    """
    Multi-objective optimizer for HPC cluster configurations
    """
    
    def __init__(self, electricity_cost_per_kwh: float = 0.12):
        self.electricity_cost = electricity_cost_per_kwh
        self.configs = []
        
    def add_configuration(self, config: HardwareConfig, 
                         benchmark_results: Dict):
        """
        Add a hardware configuration with benchmark results
        """
        # Calculate performance score
        perf_score = benchmark_results.get('throughput', 0)
        
        # Calculate energy efficiency
        energy_eff = perf_score / config.power_watts if config.power_watts > 0 else 0
        
        # Calculate 5-year TCO
        # TCO = CAPEX + (Power * Hours * Cost/kWh * Years)
        hours_per_year = 8760
        operational_cost = (config.power_watts / 1000) * hours_per_year *                           self.electricity_cost * 5
        tco = config.cost_usd + operational_cost
        
        result = BenchmarkResult(
            config=config,
            performance_score=perf_score,
            energy_efficiency=energy_eff,
            tco_5year=tco
        )
        self.configs.append(result)
    
    def find_pareto_frontier(self) -> List[BenchmarkResult]:
        """
        Find Pareto-optimal configurations
        A configuration is Pareto-optimal if no other configuration
        dominates it in all objectives
        """
        pareto = []
        for config in self.configs:
            is_dominated = False
            for other in self.configs:
                if other is config:
                    continue
                # Check if other dominates config
                if (other.performance_score >= config.performance_score and
                    other.energy_efficiency >= config.energy_efficiency and
                    other.tco_5year <= config.tco_5year and
                    (other.performance_score > config.performance_score or
                     other.energy_efficiency > config.energy_efficiency or
                     other.tco_5year < config.tco_5year)):
                    is_dominated = True
                    break
            if not is_dominated:
                pareto.append(config)
        
        return pareto
    
    def recommend_configuration(self, 
                                performance_weight: float = 0.4,
                                efficiency_weight: float = 0.3,
                                tco_weight: float = 0.3) -> BenchmarkResult:
        """
        Recommend configuration based on weighted objectives
        """
        assert abs(performance_weight + efficiency_weight + tco_weight - 1.0) < 1e-6
        
        # Normalize metrics
        max_perf = max(c.performance_score for c in self.configs)
        max_eff = max(c.energy_efficiency for c in self.configs)
        min_tco = min(c.tco_5year for c in self.configs)
        max_tco = max(c.tco_5year for c in self.configs)
        
        best_config = None
        best_score = float('-inf')
        
        for config in self.configs:
            norm_perf = config.performance_score / max_perf if max_perf > 0 else 0
            norm_eff = config.energy_efficiency / max_eff if max_eff > 0 else 0
            norm_tco = 1.0 - (config.tco_5year - min_tco) / (max_tco - min_tco)                       if max_tco > min_tco else 1.0
            
            score = (performance_weight * norm_perf + 
                    efficiency_weight * norm_eff + 
                    tco_weight * norm_tco)
            
            if score > best_score:
                best_score = score
                best_config = config
        
        return best_config
    
    def analyze_tradeoffs(self) -> Dict:
        """
        Analyze trade-offs between objectives
        """
        pareto = self.find_pareto_frontier()
        
        return {
            'pareto_size': len(pareto),
            'performance_range': {
                'min': min(c.performance_score for c in self.configs),
                'max': max(c.performance_score for c in self.configs)
            },
            'efficiency_range': {
                'min': min(c.energy_efficiency for c in self.configs),
                'max': max(c.energy_efficiency for c in self.configs)
            },
            'tco_range': {
                'min': min(c.tco_5year for c in self.configs),
                'max': max(c.tco_5year for c in self.configs)
            },
            'pareto_configs': [
                {
                    'gpu': c.config.gpu_model,
                    'num_gpus': c.config.num_gpus,
                    'performance': c.performance_score,
                    'efficiency': c.energy_efficiency,
                    'tco': c.tco_5year
                }
                for c in pareto
            ]
        }

# Usage Example
optimizer = HPCOptimizer(electricity_cost_per_kwh=0.12)

# Add configurations
config1 = HardwareConfig(
    gpu_model="A100",
    num_gpus=8,
    cpu_model="AMD EPYC",
    memory_gb=1024,
    cost_usd=150000,
    power_watts=3000
)
optimizer.add_configuration(config1, {'throughput': 1000})
```

## Key Insights

1. **Multi-Objective Trade-offs**: No single configuration optimizes all objectives
2. **Pareto Frontier**: Identifies configurations with optimal trade-offs
3. **Benchmark-Driven**: Real performance data drives optimization
4. **TCO Awareness**: Considers both capital and operational costs

## Best Practices

- Use real benchmark data for your specific workloads
- Consider workload characteristics (compute-bound vs memory-bound)
- Factor in electricity costs for your region
- Re-evaluate annually as hardware and energy costs change

## References

- Afzal, A., Hager, G., & Wellein, G. (2025). Wattlytics: A Web Platform for Co-Optimizing Performance, Energy, and TCO in HPC Clusters. arXiv:2604.08182.

## Trigger Words

- hpc optimization
- gpu cluster
- energy efficiency
- tco analysis
- performance tuning
- multi-objective optimization
