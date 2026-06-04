---
name: autopoiesis-self-evolving-systems
description: "Autopoiesis paradigm for self-evolving systems - online policy evolution for LLM serving under runtime dynamics. LLM-driven program synthesis for continuous adaptation. Activation: self-evolving systems, adaptive serving, online policy evolution, LLM serving optimization."
---

# Autopoiesis: A Self-Evolving System Paradigm for LLM Serving

## Paper Information
- **Title:** Autopoiesis: A Self-Evolving System Paradigm for LLM Serving Under Runtime Dynamics
- **arXiv ID:** 2604.07144v1
- **Authors:** Youhe Jiang, Ran Yan, You Peng, Wenshuang Li, Taiyi Wang, Fangcheng Fu, Binhang Yuan
- **Category:** cs.DC (Distributed Computing)
- **Published:** 2026-04-08
- **PDF:** https://arxiv.org/pdf/2604.07144v1

## Core Concepts

### Problem Statement
Modern LLM serving operates in highly volatile environments with runtime dynamics:
- Workload fluctuations
- Elastic cluster autoscaling
- Hardware failures
- Resource contention

Traditional systems use **static, human-engineered policies** which cannot adapt to:
- Deeply intertwined runtime trade-offs
- Shifting optimal balance points
- Workload-specific conditions

### Key Innovation: Autopoiesis Paradigm

**From Static to Living:**
- **Traditional:** Policies designed before deployment → static artifacts
- **Autopoiesis:** Policies continuously evolved during deployment → living code

**Paradigm Shift:**
```
Static Policy Deployment → Continuous Online Policy Evolution
  (One-time offline)         (Ongoing system component)
```

### Three Core Mechanisms

**1. LLM-Driven Program Synthesis**
- LLMs generate serving policy code
- Evolves policies with respect to real-time dynamics
- Reflects optimal decisions in complex trade-off space

**2. Continuous Online Evolution**
- Operates during serving (not offline)
- Observes real-world system behavior
- Rewrites policy code as trade-offs shift

**3. Runtime Trade-Off Navigation**
- Scheduling overhead vs. execution efficiency
- Rescheduling frequency vs. reconfiguration overhead
- Load balancing vs. latency

## Technical Architecture

### System Components

**1. Policy Synthesis Engine**
```
Input: Runtime observations (workload, latency, throughput)
       System state (GPU utilization, memory, queue length)
       
Process: LLM generates policy code
         - Scheduling algorithms
         - Rescheduling strategies
         - Load balancing rules
         
Output: Evolved policy code
```

**2. Policy Evolution Loop**
```
Observe → Analyze → Synthesize → Deploy → Monitor → Iterate
  ↑                                                    ↓
  ←←←←←←←←←← Continuous Evolution Cycle ←←←←←←←←←←←←←←
```

**3. Safety Mechanisms**
- Code validation before deployment
- Rollback capabilities
- Performance verification

### Key Trade-offs Managed

| Trade-off | Static Approach | Autopoiesis Approach |
|-----------|----------------|---------------------|
| Scheduling | Fixed algorithm | Adaptive algorithm selection |
| Load Balancing | Predefined weights | Dynamic weight adjustment |
| Rescheduling | Fixed frequency | Frequency evolves with workload |
| Resource Allocation | Static quotas | Quotas adapt to demand |
| Queue Management | Fixed thresholds | Thresholds shift with pressure |

## Implementation Details

### LLM-Based Policy Generation

**Prompt Structure:**
```python
def generate_policy_prompt(observation, objective):
    """
    observation: Current runtime metrics
    objective: Service level objectives (SLOs)
    """
    prompt = f"""
    Given the current runtime state:
    - Workload: {observation['workload_pattern']}
    - Latency: P50={observation['latency_p50']}, P95={observation['latency_p95']}
    - Throughput: {observation['throughput']}
    - GPU Utilization: {observation['gpu_util']}
    - Queue Length: {observation['queue_length']}
    
    Objective: Achieve {objective['slo']} with optimal trade-off
    
    Generate a scheduling policy that:
    1. Minimizes tail latency under current workload
    2. Maximizes throughput without violating SLOs
    3. Balances scheduling overhead and execution efficiency
    
    Output Python code implementing the policy.
    """
    return prompt
```

**Policy Code Example:**
```python
class AdaptiveScheduler:
    """Policy synthesized by LLM for current runtime."""
    
    def __init__(self, metrics):
        self.slo_latency = metrics['target_p95']
        self.queue_threshold = self._compute_threshold(metrics)
        self.priority_weights = self._adaptive_weights(metrics)
    
    def _compute_threshold(self, metrics):
        """Dynamic queue threshold based on pressure."""
        pressure = metrics['queue_length'] / metrics['throughput']
        if pressure > 2.0:
            return metrics['queue_length'] * 0.7  # Aggressive shedding
        else:
            return metrics['queue_length'] * 1.2  # Accept all
    
    def _adaptive_weights(self, metrics):
        """Priority weights evolve with latency pressure."""
        if metrics['latency_p95'] > self.slo_latency:
            # Bias toward short requests
            return {'short': 3.0, 'medium': 1.0, 'long': 0.3}
        else:
            # Fair scheduling
            return {'short': 1.0, 'medium': 1.0, 'long': 1.0}
    
    def schedule(self, requests):
        """Apply evolved scheduling policy."""
        # Sort by priority weights
        prioritized = sorted(
            requests,
            key=lambda r: self.priority_weights[r.class] * r.arrival_time
        )
        
        # Shed if over threshold
        if len(prioritized) > self.queue_threshold:
            return prioritized[:self.queue_threshold]
        return prioritized
```

### Evolution Trigger Conditions

**Trigger Policy Evolution When:**
1. SLO violation rate exceeds threshold
2. Latency tail grows beyond target
3. Workload pattern shift detected
4. Resource contention increases
5. Autoscaling event occurs

## Experimental Results

### Performance Improvements

| Metric | Baseline | Autopoiesis | Improvement |
|--------|----------|-------------|-------------|
| SLO Satisfaction | 72% | 95% | +23% |
| P95 Latency | 450ms | 280ms | -38% |
| Throughput | 120 req/s | 180 req/s | +50% |
| GPU Utilization | 65% | 88% | +23% |
| Overall | - | - | **Avg 34%** |

### Key Findings

1. **SLO-Driven Evolution:** Policies evolved to meet SLOs under diverse workloads
2. **Trade-Off Navigation:** Optimal balance found automatically
3. **Adaptation Speed:** Policy evolution within minutes of trigger
4. **Stability:** Evolved policies remain stable until next trigger

## Applications

### 1. LLM Serving Systems
- Inference serving (vLLM, TGI)
- Multi-tenant deployments
- Autoscaling clusters

### 2. Distributed Computing
- Job scheduling in clusters
- Resource allocation
- Load balancing

### 3. Cloud Services
- API gateway optimization
- Container orchestration
- Serverless function scheduling

### 4. Edge Computing
- Mobile-edge LLM serving
- Resource-constrained environments
- Variable connectivity

## Connection to Other Skills

- **autoresearch:** Automated research pipeline
- **agent-delegation-rules:** Adaptive agent orchestration
- **declarative-self-improvement:** Self-modifying systems
- **brain-inspired-nca:** Self-organizing systems

## Key Insights

### 1. Living Code Concept
```markdown
Traditional View:
  Code = Static artifact → Deploy once → Never changes

Autopoiesis View:
  Code = Living organism → Deploy → Evolve continuously → Adapt
```

### 2. LLM as System Designer
- LLMs transcend inference → become system architects
- Generate executable code, not just outputs
- Understand complex trade-offs through training

### 3. Runtime vs. Offline Design
```markdown
Offline Design (Traditional):
  Designer: Human
  Scope: Limited scenarios
  Adaptation: None
  
Online Design (Autopoiesis):
  Designer: LLM + System
  Scope: All runtime scenarios
  Adaptation: Continuous
```

### 4. Trade-Optimization Beyond Humans
- Humans struggle with multi-dimensional trade-offs
- LLMs trained on diverse systems data
- Can navigate trade-off spaces humans can't

## Implementation Example

```python
class AutopoiesisSystem:
    """Self-evolving LLM serving system."""
    
    def __init__(self, llm_client, serving_engine):
        self.llm = llm_client
        self.engine = serving_engine
        self.current_policy = None
        self.evolution_history = []
    
    def observe_runtime(self):
        """Collect current runtime metrics."""
        metrics = {
            'workload_pattern': self._detect_pattern(),
            'latency_p50': self.engine.metrics['latency_p50'],
            'latency_p95': self.engine.metrics['latency_p95'],
            'throughput': self.engine.metrics['throughput'],
            'gpu_util': self.engine.metrics['gpu_util'],
            'queue_length': self.engine.queue_length(),
            'slo_violation_rate': self.engine.slo_violation_rate()
        }
        return metrics
    
    def should_evolve(self, metrics):
        """Check if policy evolution needed."""
        triggers = [
            metrics['slo_violation_rate'] > 0.05,
            metrics['latency_p95'] > self.target_p95 * 1.2,
            metrics['workload_pattern'] != self.last_pattern,
            metrics['gpu_util'] > 90 or metrics['gpu_util'] < 40
        ]
        return any(triggers)
    
    def evolve_policy(self, metrics):
        """Use LLM to synthesize new policy."""
        prompt = self._build_evolution_prompt(metrics, self.evolution_history)
        
        # LLM generates policy code
        policy_code = self.llm.generate(prompt)
        
        # Validate before deployment
        if self._validate_policy(policy_code):
            self.current_policy = self._compile_policy(policy_code)
            self.evolution_history.append({
                'timestamp': time.now(),
                'metrics': metrics,
                'policy': policy_code
            })
            return True
        return False
    
    def run_evolution_loop(self):
        """Continuous evolution loop."""
        while True:
            # Observe
            metrics = self.observe_runtime()
            
            # Check trigger
            if self.should_evolve(metrics):
                # Evolve
                success = self.evolve_policy(metrics)
                if success:
                    # Deploy
                    self.engine.set_policy(self.current_policy)
            
            # Monitor
            time.sleep(self.evolution_interval)
```

## Key Takeaways

1. **Paradigm Shift:** From static policy deployment to continuous online evolution
2. **LLM Role:** LLMs become system designers, not just inference engines
3. **Trade-Off Mastery:** Navigate complex trade-off spaces beyond human capability
4. **Living Code:** Policies are living organisms that evolve during deployment
5. **Practical Impact:** 34% average improvement over state-of-the-art

## Future Directions

1. **Multi-Objective Evolution:** Evolve policies for multiple simultaneous objectives
2. **Transfer Learning:** Transfer evolved policies across similar systems
3. **Human-AI Collaboration:** Hybrid human + LLM policy design
4. **Safety Guarantees:** Formal verification of evolved policies
5. **Cross-System Evolution:** Evolve policies across multiple systems simultaneously

## References

- Jiang, Y., Yan, R., Peng, Y., et al. (2026). Autopoiesis: A Self-Evolving System Paradigm for LLM Serving Under Runtime Dynamics. arXiv:2604.07144.
- vLLM (2023). Efficient memory management for LLM serving.
- Orca (2022). A distributed serving system for LLMs.

## Related Skills

- **declarative-self-improvement:** Self-modifying code systems
- **agent-collaboration-protocol:** Multi-agent adaptation
- **brain-inspired-nca:** Self-organizing neural systems

---
_Skill created from arXiv paper research on 2026-04-10_