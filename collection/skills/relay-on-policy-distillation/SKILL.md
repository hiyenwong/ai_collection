---
name: relay-on-policy-distillation
description: Relay On-Policy Distillation (Relay-OPD) methodology for trajectory-relayed token-level supervision to overcome prefix failure in reasoning models.
paper_id: "2607.26057"
---

# Pass the Baton: Trajectory-Relayed On-Policy Distillation

## Overview
This methodology addresses prefix failure in standard On-Policy Distillation (OPD) where students commit to wrong reasoning directions and build subsequent generations on deviations. Relay-OPD uses teacher-student continuation asymmetry as a label-free handoff trigger.

## Key Contributions
- Identifies teacher-student continuation asymmetry on failed prefixes (teacher redirects, student continues original direction)
- Converts asymmetry into label-free handoff trigger for Relay On-Policy Distillation (Relay-OPD)
- Constructs relay trajectories by letting teacher briefly take over at trigger points to produce teacher leg
- Implements limited relay budget to concentrate intervention on critical early positions while limiting departure from student policy
- Achieves superior results over standard OPD (+5.73%) and FastOPD (+1.49%) on mathematical reasoning benchmarks
- Reduces training trajectory length by over 50%

## Implementation Guidelines
1. **Handoff Trigger Detection**: Monitor for teacher-student continuation asymmetry indicating prefix failure
2. **Relay Trajectory Construction**: 
   - Let teacher take over at detected trigger points
   - Teacher produces "teacher leg" of trajectory
   - Student resumes after teacher intervention
3. **Relay Budget Management**: Limit teacher interventions to concentrate on critical early positions
4. **Training Optimization**: Optimize student on resulting relay trajectories
5. **Model Configuration**: Tested with Qwen3-4B-Instruct-2507 teacher and Qwen3-0.6B/1.7B-Non-Thinking students

## Use Cases
- Mathematical reasoning model distillation
- Large language model compression for reasoning tasks
- Overcoming prefix failure in sequential generation tasks
- Efficient training of smaller reasoning models using larger teachers
- Token-level supervision scenarios with trajectory-based learning

## Activation Keywords
relay OPD, trajectory-relayed distillation, prefix failure, on-policy distillation, reasoning model distillation, handoff trigger

## References
- arXiv:2607.26057 [cs.CL]
- Project Page: https://zju-real.github.io/Relay-OPD
- Code: https://github.com/zju-real/Relay-OPD