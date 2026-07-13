---
name: dart-q-realtime-qldpc-decoding
description: "DART-Q methodology for real-time quantum error correction decoding. Deadline-driven QLDPC decoder framework with queueing theory, EDF scheduling, and admission control for fault-tolerant quantum computing. Activation: real-time decoding, quantum decoder scheduling, QLDPC decoding, deadline-driven quantum, DART-Q."
category: quantum
---

# DART-Q: Real-Time QLDPC Decoding Framework

## Description

DART-Q is a deadline-driven framework for real-time quantum low-density parity-check (QLDPC) decoding. It treats windowed decode workloads as discrete arrival, queueing, service, and completion events within the fault-tolerant control loop. The framework models each decode request as a deadline-driven online service job with Earliest Deadline First (EDF) scheduling, configurable admission control, and bounded rescue policies.

**arXiv**: 2605.09142v1
**Authors**: Ameya S. Bhave, Navnil Choudhury, Kanad Basu

## Activation Keywords

- real-time decoding
- quantum decoder scheduling
- QLDPC decoding
- deadline-driven quantum
- DART-Q
- quantum error correction timing
- 实时量子解码
- 量子解码调度

## Core Concepts

### 1. Deadline-Driven Online Service Model

Decode requests arrive as discrete events with strict deadlines determined by the quantum error correction cycle time. Each request is characterized by:

- **Arrival time**: When syndrome measurement completes
- **Deadline**: Maximum allowable latency before logical error accumulates
- **Service time**: Decoder computation time for the syndrome
- **Priority**: Determined by remaining time to deadline

### 2. Earliest Deadline First (EDF) Scheduling

Non-preemptive EDF scheduling prioritizes decode requests with the closest deadlines:

```
while decode_queue not empty:
    request = select_earliest_deadline(decode_queue)
    if can_complete_before_deadline(request):
        execute_decode(request)
    else:
        apply_rescue_policy(request)
```

### 3. Admission Control

Not all decode requests should be processed. Admission control filters requests based on:

- **Current queue depth**: Reject if backlog exceeds threshold
- **Estimated service time**: Reject if decoder is overloaded
- **Priority threshold**: Only accept high-priority (near-deadline) requests under load

### 4. Cached-Summary State Organization

Key finding: A cached-summary state organization lowers the SRAM-fit boundary by 4x relative to an edge-centric baseline. This reduces memory pressure on the decoder hardware.

### 5. Capacity Scaling

Doubling decoder capacity reduces MissRate from 97.64% to 0.98% and improves p99 latency from 3.861ms to 10μs. This demonstrates that service capacity is the dominant factor in real-time decoder viability.

## Implementation Guidelines

### Phase 1: Model the Decode Pipeline

```python
class DecodeRequest:
    def __init__(self, syndrome, arrival_time, deadline, priority):
        self.syndrome = syndrome
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.priority = priority
        self.estimated_service_time = estimate_decode_time(syndrome)
        self.status = "pending"  # pending, queued, processing, completed, missed
```

### Phase 2: Implement EDF Scheduler

```python
class EDFScheduler:
    def __init__(self, decoder_capacity=1):
        self.queue = []
        self.capacity = decoder_capacity
    
    def add_request(self, request):
        if self.admission_check(request):
            self.queue.append(request)
            self.queue.sort(key=lambda r: r.deadline)
    
    def admission_check(self, request):
        # Check if processing this request would cause deadline misses
        total_service = sum(r.estimated_service_time for r in self.queue)
        remaining_time = request.deadline - current_time()
        return total_service + request.estimated_service_time < remaining_time
    
    def select_next(self):
        if not self.queue:
            return None
        return self.queue[0]  # Earliest deadline first
```

### Phase 3: Rescue Policies

When a deadline cannot be met, apply bounded rescue:

1. **Skip**: Ignore the syndrome (rely on previous correction)
2. **Approximate**: Run a faster, lower-accuracy decoder
3. **Defer**: Process in next cycle with adjusted priority

## Key Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **MissRate** | Fraction of decode requests missing deadlines | < 1% |
| **p99 Latency** | 99th percentile decode latency | < 100μs |
| **Throughput** | Decodes per second | Matches syndrome rate |
| **SRAM-fit** | Decoder state fitting on-chip memory | Minimize off-chip access |

## Design Tradeoffs

### Queue Depth vs. Latency
- Relaxing backlog cap increases queued work by ~20.1x and worsens p99 latency by ~17.6x
- Little gain in useful throughput from excessive queuing

### Capacity vs. Cost
- Doubling capacity dramatically reduces miss rate (97.64% → 0.98%)
- This is the most effective optimization lever

### State Organization vs. Memory
- Cached-summary reduces SRAM-fit boundary by 4x
- Edge-centric baseline requires significantly more on-chip memory

## Error Handling

### Decoder Overload
When decoder capacity is insufficient:
1. Apply admission control to filter low-priority requests
2. Use approximate decoder for non-critical syndromes
3. Scale capacity (most effective solution)

### Deadline Misses
When a decode request misses its deadline:
1. Log the miss for analysis
2. Apply rescue policy based on error severity
3. Adjust future admission control thresholds

### Memory Pressure
When on-chip memory is insufficient:
1. Switch to cached-summary state organization
2. Reduce syndrome window size
3. Increase SRAM or use hierarchical memory

## Related Papers

- Price and Payoff (2605.07983): Stochastic resource planning for FTQC
- Lower overhead fault-tolerant building blocks (2605.12385): FTQC building block optimization

## Tools Used

- exec: Run simulation and benchmark scripts
- read: Load syndrome data, benchmark results
- write: Save decoder configurations, performance reports

## References

- Paper: "DART-Q: A Deadline-Driven Framework for Real-Time QLDPC Decoding" (arXiv:2605.09142v1)
- QLDPC codes: Quantum Low-Density Parity-Check codes
- EDF: Earliest Deadline First scheduling algorithm
