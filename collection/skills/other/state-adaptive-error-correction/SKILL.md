---
name: state-adaptive-error-correction
description: >
  State-adaptive error correction and fault tolerance methodology. Use when designing
  resilient systems that need to adapt error handling based on current system state,
  optimize recovery strategies dynamically, or build fault-tolerant architectures.
  Applicable to distributed systems, quantum computing, network protocols, ML pipelines,
  and control systems. Trigger words: state-adaptive, adaptive error correction,
  fault-tolerant design, resilient architecture, dynamic error handling, system state awareness.
---

# State-Adaptive Error Correction

## Overview

A methodology for building error correction and fault tolerance that adapts to the
current state of the system. Instead of static error handling rules, the approach
incorporates real-time state knowledge to optimize recovery strategies, achieving
better resilience without additional measurement or monitoring overhead.

## Core Principle

**State-adaptivity**: Error correction effectiveness increases when the correction
strategy incorporates knowledge of the current system state. The optimal error
handling strategy depends on what the system is currently doing, not just what
error occurred.

## Key Patterns

### 1. State-Aware Error Classification

Classify errors not just by type, but by the system state when they occur:

```
error_context = (error_type, system_state, recent_history)
correction_strategy = lookup_optimal(error_context)
```

- **Nominal state errors**: Standard recovery procedures
- **High-load state errors**: Graceful degradation, queue backpressure
- **Transition state errors**: Wait-and-retry with state synchronization
- **Degraded state errors**: Aggressive correction with fallback paths

### 2. Adaptive Recovery Hierarchy

Build layered recovery that adapts based on state assessment:

| Layer | Trigger | Strategy |
|-------|---------|----------|
| L0: Local | Transient error in stable state | Retry with exponential backoff |
| L1: Contextual | Persistent error, known state | Apply state-specific correction |
| L2: Structural | Unknown state, cascading errors | Full state reconstruction |
| L3: Fallback | All else fails | Safe mode with minimal functionality |

### 3. State-Guided Resource Allocation

Allocate correction resources based on state criticality:

- **Critical path components**: Real-time monitoring + proactive correction
- **Non-critical paths**: Periodic checks + reactive correction
- **Shared resources**: Contention-aware scheduling

## Implementation Workflow

### Step 1: Define System States

Identify distinguishable operational states:

```python
class SystemState:
    NOMINAL = "nominal"           # Normal operation
    HIGH_LOAD = "high_load"       # Under heavy load
    TRANSITION = "transition"     # Between configurations
    DEGRADED = "degraded"         # Some components failing
    RECOVERING = "recovering"     # In recovery process
    SAFE_MODE = "safe_mode"       # Minimal operation
```

### Step 2: Build State Detector

Implement lightweight state detection that doesn't add significant overhead:

```python
def detect_state(metrics, recent_errors):
    """Detect current system state from observable metrics."""
    score = compute_health_score(metrics)
    if score > 0.9:
        return SystemState.NOMINAL
    elif score > 0.7:
        return SystemState.HIGH_LOAD
    elif is_transitioning(metrics):
        return SystemState.TRANSITION
    elif recent_errors.count > threshold:
        return SystemState.DEGRADED
    # ... etc
```

### Step 3: Map Error-State to Correction Strategy

```python
CORRECTION_MATRIX = {
    (ErrorType.TIMEOUT, SystemState.NOMINAL): {
        "action": "retry", "max_retries": 3, "backoff": "exponential"
    },
    (ErrorType.TIMEOUT, SystemState.HIGH_LOAD): {
        "action": "queue", "priority": "low", "timeout": "extended"
    },
    (ErrorType.CORRUPTION, SystemState.DEGRADED): {
        "action": "rebuild_from_checkpoint", "verify": True
    },
    # ... more mappings
}
```

### Step 4: Implement Adaptive Handler

```python
def handle_error(error, system_state):
    strategy = CORRECTION_MATRIX.get((type(error), system_state), DEFAULT_STRATEGY)
    result = execute_strategy(strategy, error)
    if result.success:
        log_correction(error, system_state, strategy)
    else:
        escalate_error(error, system_state, result)
    return result
```

## Application Domains

### Distributed Systems
- Network partition handling adapts to cluster state
- Consensus protocol recovery based on node health
- Load balancer failover with state awareness

### ML/Training Pipelines
- Gradient anomaly detection adapts to training phase
- Checkpoint selection based on convergence state
- Data pipeline error recovery with buffer state

### Quantum Computing
- Error correction adapts to qubit coherence state
- Decoding strategies informed by circuit context
- Fault-tolerant gate selection based on noise profile

### Control Systems
- Controller parameter adjustment based on operating point
- Safety filter activation based on proximity to boundaries
- Observer switching based on model validity

## Pitfalls

1. **State detection overhead**: The state detector must be lightweight. If detecting
   state costs more than the error itself, the approach fails.
2. **State explosion**: Too many states makes the correction matrix unmaintainable.
   Start with 4-6 states and expand only when needed.
3. **Stale state**: Ensure state information is current. Using outdated state for
   correction can make errors worse.
4. **Circular dependency**: State detection shouldn't depend on components that
   might be in error.

## Verification

- Test each (error, state) combination independently
- Measure correction success rate per state
- Compare against static error handling baseline
- Verify state detector accuracy under fault conditions

## References

- State-adaptive quantum error correction framework (Wang, 2025/2026)
  - Key insight: incorporating state knowledge into error correction
    improves capacity regime from coherent to mutual information bounds
- Surface code error correction with ML decoding
- Fault-tolerant neutral atom architectures (Bluvstein et al., Nature 2025)
