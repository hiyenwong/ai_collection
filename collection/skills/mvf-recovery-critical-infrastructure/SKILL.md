---
name: mvf-recovery-critical-infrastructure
description: "Minimum Viable Factory (MVF) Recovery methodology for ransomware recovery in critical manufacturing infrastructure. Reframes recovery as capability-centric continuity and interdependency problem across IT/OT/physical/supply-chain domains. Identifies nine evidence-backed recovery failure modes and derives recovery lifecycle. Use when: designing ransomware recovery plans, assessing manufacturing system resilience, evaluating critical infrastructure continuity, analyzing IT-OT interdependencies, building recovery benchmarks, or studying cross-domain system recovery."
---

# MVF Recovery — Minimum Viable Factory Recovery Methodology

## Core Concept

Reframe ransomware recovery in critical manufacturing as an **interdependency and continuity problem**, not just a backup-restoration task. Production capability depends on coupled IT, OT, physical-process, quality, logistics, identity, and supplier systems.

**MVF Recovery**: The smallest safe, trusted, and operationally meaningful production capability that can be resumed under current dependency, evidence, identity, data, network, OT, and supplier constraints. It is an analytical objective — not a claim of full recovery or safety certification.

## Nine Recovery Failure Modes

| # | Failure Mode | Description |
|---|---|---|
| 1 | **Dependency Blindness** | Failing to map cross-domain dependencies before recovery |
| 2 | **Untrusted Restore Point / Backup Over-Trust** | Restoring from compromised backups without verification |
| 3 | **Identity Trust Collapse** | Inability to authenticate operators after AD/PKI compromise |
| 4 | **Lack of Proof-of-Recovery** | No evidence that restored systems are clean and functional |
| 5 | **Unsafe OT Reconnection** | Reconnecting OT assets before security validation |
| 6 | **Segmentation Assumption Failure** | Assuming network segmentation was effective when it was not |
| 7 | **Capability Mismatch** | Restored systems cannot meet production requirements |
| 8 | **Unmanaged Degraded Operation** | Running in degraded mode without explicit management |
| 9 | **Supplier Dependency Failure** | External suppliers cannot support recovery |

## Recovery Lifecycle

1. **Assess**: Map all IT/OT/physical/supplier dependencies
2. **Contain**: Isolate affected systems, preserve evidence
3. **Verify**: Validate backup integrity and restore points
4. **Restore MVF**: Resume smallest safe, trusted production capability
5. **Expand**: Gradually restore full production capability
6. **Validate**: Verify all systems are clean and functional

## Implementation Pattern

```python
def assess_dependencies(system):
    """Map cross-domain dependencies (IT, OT, physical, supplier)."""
    return {
        "it_systems": identify_it_dependencies(system),
        "ot_systems": identify_ot_dependencies(system),
        "physical_processes": map_physical_processes(system),
        "supplier_chain": map_supplier_dependencies(system),
        "identity_systems": map_identity_infrastructure(system),
    }

def calculate_mvf(dependencies, constraints):
    """Determine minimum viable factory capability."""
    safe_capability = set()
    for dep in dependencies:
        if is_safe_to_restore(dep, constraints):
            safe_capability.add(dep)
    return safe_capability

def validate_recovery(restored_system):
    """Verify restored system is clean and functional."""
    checks = [
        check_backup_integrity(restored_system),
        verify_identity_trust(restored_system),
        validate_segmentation(restored_system),
        confirm_capability_match(restored_system),
    ]
    return all(checks)
```

## Key Principles

1. **Capability-centric**: Focus on resuming production capability, not just restoring servers
2. **Evidence-calibrated**: Base recovery decisions on verified evidence, not assumptions
3. **Constraint-aware**: Account for dependency, identity, data, network, OT, and supplier constraints
4. **Gradual expansion**: Start with MVF, then incrementally expand to full production
5. **Cross-domain**: Consider IT, OT, physical process, quality, logistics, and supplier systems together

## Activation Keywords

- mvf recovery, minimum viable factory, ransomware recovery, manufacturing recovery
- critical infrastructure recovery, IT-OT recovery, cross-domain recovery
- recovery failure modes, dependency blindness, identity trust collapse
- production capability recovery, systems resilience, backup restoration

## References

- arXiv: 2605.16167
- Paper: "From Backup Restoration to Minimum Viable Factory Recovery"
