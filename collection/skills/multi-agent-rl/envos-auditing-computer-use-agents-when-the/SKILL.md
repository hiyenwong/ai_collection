---
name: envos-auditing-computer-use-agents-when-the
description: "EnvOS: Auditing Computer-Use Agents When the World..."
tags: [cs.AI, cs.HC]
source: arxiv
arxiv_id: 2610.40246v1
utility: 0.92
published: 2026-10-29
---

# EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation

**Authors:** Ankush Kadu, Athira Gopal, Niharika Singh, Arpit Jain, Aswanth Krishnan
**Published:** 2026-10-29
**arXiv:** [2610.40246v1](https://arxiv.org/abs/2610.40246v1)
**Categories:** cs.AI, cs.HC
**Utility Score:** 0.92

## Abstract

Computer-use agents built on large language models (LLMs) work in software that can change while they act: an appointment moves, a policy is revised, a record is updated. Testing agents under such changes is harder than it looks. When an agent fails, the cause may be the agent, but it may also be a change that did not fire as intended, an update the agent never received, or a grader that scored the episode wrongly. We introduce EnvOS, a framework for building and certifying environments that change mid-task. Before any agent runs, EnvOS checks that each change fires correctly, that the task remains solvable, and that the grader separates correct from incorrect behavior; after each run, separate code re-checks the verdict from archived evidence. We apply it to stale information, where a value the agent has already seen changes before the agent acts on it. In clinic booking, Claude Opus 5 succeeds on 0/16 tasks when nothing extra is shown, 2/16 when reminded to re-check the source, and 15/16 when the updated value is shown; the gain over the reminder holds after correcting for all tests (p = 0.00293). In insurance-claim approval, Opus 5 re-checks on its own and succeeds on 10/10, whereas Claude Sonnet 5 rises from 1/10 to 9/10 when the current policy is shown again, a gain significant in its pre-registered test but not after correcting for all tests. Whether an agent caught a change thus varied with the model and the interface. We also stress-test the grading itself: on corrupt

## Key Contributions

- Novel research in cs.AI, cs.HC
- Published 2026-10-29

## Activation

envos, auditing, computeruse, agents, when, world, moves, phenomenonbased, task, construction
