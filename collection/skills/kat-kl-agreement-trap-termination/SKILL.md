---
name: kat-kl-agreement-trap-termination
description: KL Agreement Trap Termination (KAT) for on-policy distillation. Detects persistent low-KL agreement traps and terminates early to improve training efficiency.
version: 1.0
created: 2026-06-10
source: arXiv 2606.09471v1
tags: [distillation, OPD, KL-divergence, termination, LLM, reasoning]
---

# KAT: KL Agreement Trap Termination

Online termination rule for On-Policy Distillation (OPD) that detects when student enters unrecoverable "KL agreement trap" states.

## Problem Statement

In on-policy distillation, when the student drifts into an unrecoverable prefix:
- Teacher may locally agree with degraded state
- Produces low reverse KL but little corrective training signal
- Tokens during and after traps produce less useful supervision

## KAT Detection Algorithm

### Dynamic Threshold Detection
```python
class KLAgreementTrapDetector:
    def __init__(self, threshold_alpha=0.05, window_size=10):
        self.threshold_alpha = threshold_alpha
        self.window_size = window_size
        self.kl_history = []
    
    def detect_trap(self, kl_divergence, training_step):
        # Dynamic threshold adapts to training progress
        dynamic_threshold = self.compute_adaptive_threshold(training_step)
        
        # Track persistent low-KL
        self.kl_history.append(kl_divergence)
        if len(self.kl_history) > self.window_size:
            self.kl_history.pop(0)
        
        # Check for persistent agreement
        avg_kl = np.mean(self.kl_history)
        if avg_kl < dynamic_threshold:
            return True  # Trap detected
        return False
    
    def compute_adaptive_threshold(self, step):
        # Threshold increases as model improves
        base_threshold = 0.1
        return base_threshold * (1 + self.threshold_alpha * step)
```

### Termination Rule
```python
def kat_termination_rule(rollout, teacher_logits, detector):
    kl_values = []
    for position, (student_token, teacher_dist) in enumerate(rollout):
        kl = compute_reverse_kl(student_token, teacher_dist)
        kl_values.append(kl)
        
        # Check for trap at each position
        if detector.detect_trap(kl, position):
            # Terminate early, discard weak supervision
            return rollout[:position], kl_values[:position]
    
    return rollout, kl_values  # Full rollout if no trap
```

## Results on Math Benchmarks

- Avg@k accuracy: +2.66%
- Pass@k: +3.43%
- Average rollout length: -59.73% (significant efficiency gain)

## Integration with OPD

```python
def opd_with_kat(student, teacher, problems, detector):
    for problem in problems:
        # Generate student rollout
        rollout = student.generate(problem)
        
        # Get teacher logits
        teacher_logits = teacher.score(rollout)
        
        # Apply KAT termination
        filtered_rollout, filtered_kl = kat_termination_rule(
            rollout, teacher_logits, detector
        )
        
        # Train only on non-trapped portions
        student.update(filtered_rollout, filtered_kl)
```

## When to Use

- On-policy distillation for reasoning models
- Mathematical reasoning benchmarks
- When student trajectories can drift into unrecoverable states
- To reduce rollout length while improving accuracy

## Activation Triggers

- `KL agreement trap`, `OPD termination`, `on-policy distillation quality`, `KAT`, `distillation trap detection`

## References

- arXiv:2606.09471v1 - Xin et al., "Escaping the KL Agreement Trap in On-Policy Distillation"
- Reverse KL divergence for distillation
- On-policy vs off-policy distillation trade-offs