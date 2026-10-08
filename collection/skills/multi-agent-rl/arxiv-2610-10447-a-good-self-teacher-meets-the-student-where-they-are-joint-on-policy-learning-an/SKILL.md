---
name: arxiv-2610-10447-a-good-self-teacher-meets-the-student-where-they-are-joint-on-policy-learning-an
description: 'A Good Self-Teacher Meets the Student Where They Are: Joint On-Policy Learning and Teaching (arXiv: 2610.10447)'
metadata:
  {
    "arxiv_id": "2610.10447",
    "utility": 0.86,
    "title": "A Good Self-Teacher Meets the Student Where They Are: Joint On-Policy Learning and Teaching",
    "authors": "Randy Ardywibowo, Arnav Dalal, Jiantao Jiao",
    "url": "https://arxiv.org/abs/2610.10447v1",
    "categories": ["cs.LG", "cs.AI"],
    "published": "2026-10-07"
  }
---

# A Good Self-Teacher Meets the Student Where They Are: Joint On-Policy Learning and Teaching

**arXiv ID:** 2610.10447
**Authors:** Randy Ardywibowo, Arnav Dalal, Jiantao Jiao
**URL:** https://arxiv.org/abs/2610.10447v1
**Utility Score:** 0.86
**Published:** 2026-10-07
**Categories:** cs.LG, cs.AI

## Summary

Reinforcement Learning (RL) from outcome rewards suffers from sparse supervision, particularly on difficult, long-horizon tasks where successful trajectories are rare and costly to generate. On-Policy Distillation (OPD) offers an attractive alternative by providing dense token-level supervision from a stronger teacher along the student's own generations. Self-distillation methods further remove the need for a separate teacher model by conditioning the same policy on privileged information to serve as its own teacher. However, privileged conditioning alone does not guarantee that the resulting distillation update improves the student. Indeed, privileged information can lead the teacher to solve tasks through shortcuts unavailable to the student, producing supervision poorly matched to the student's current behavior. Consequently, even a higher-performing teacher can provide guidance that degrades student performance. To address this, we analyze how the choice of privileged teacher affects the student's update. We derive a necessary and sufficient condition for the teacher's local distillation update to be a positive multiple of the student's reward gradient. Our analysis suggests that the teacher should not only perform well on the task, but also provide guidance suited to the student's current capabilities. This characterization motivates a practical teacher-training surrogate that combines outcome rewards with token-level Kullback-Leibler (KL) regularization toward the student. Based on this result, we propose Joint On-Policy Learning and Teaching (JOLT), which jointly trains a single policy in two roles: a privileged teacher using a KL-regularized objective, and an unprivileged student using dense on-policy distillation. Across mathematical reasoning, coding, tool use, and terminal use, JOLT improves training efficiency and performance, with further gains from student rewards.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10447v1
