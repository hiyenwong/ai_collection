---
name: heterarchy-brain-control-spectrum
description: Use when analyzing brain control hierarchy claims, cortico-subcortical direction, or designing context-resolved effective connectivity tests. Decouples hierarchy-as-configuration from heterarchy-as-architecture.
category: neuroscience
metadata:
  arxiv_id: "2610.04643"
  published: "2026-10-06"
  authors: "Luiz Pessoa, Andrea Gambarotto"
  source: "arXiv q-bio.NC"
  tags: [heterarchy, brain control, network neuroscience, dynamical decoupling, effective connectivity]
---

# Heterarchy in the Brain: Control as a Spectrum, Not a Chain of Command

Pessoa & Gambarotto (arXiv:2610.04643) argue that hierarchical control is a misread of time-bounded configurations as architecture. Local directional asymmetries are real, but control is relational and process-specific; relations form cycles that admit no consistent level assignment. Hierarchy is the special case, heterarchy the general condition.

## Core Argument (the composition failure)

The hierarchical picture rests on an unstated premise: local relations of influence compose into a consistent (transitive, loop-free) partial order that belongs to the system, not the occasion.

Three premises defeat it:
1. A structure is a controller **only relative to a process** unfolding over an interval (assembling a response, phase-locking, changing a synapse).
2. Each element participates in **multiple concurrent processes** — regulating some while regulated in others (PVT neurons collateralize to NAc, BNST, CeA before any activity is measured; 10k-neuron recordings find task-response repertoires crossing cytoarchitectural boundaries).
3. These relations form **loops**. One loop (A ⊳ B, B ⊳ A; or three-cycle A ⊳ B ⊳ C ⊳ A) defeats every possible level assignment.

**Critical distinction**: reciprocal wiring ≠ heterarchy. A thermostat has feedback. The premise requires **reciprocal constraint** — structures shaping what one another *learn, express, or transmit* (amygdala shapes what PFC works with while PFC shapes what the amygdala works on).

**Control vs dynamic stability**: a mechanism that only reacts to the present state of what it regulates is dynamic stability, not control. Control requires **dynamical decoupling** — the controller has its own dynamics, responding differently to the same current state depending on history, internal state, learned context (fear potentiates startle; idealized reflex has zero independence).

## The Spectrum of Control

Indexed by dynamical decoupling — how far behavior can depend on history, internal state, and anticipated consequences:

| End | Property |
|-----|----------|
| Reflex pole | Response fixed by the immediate stimulus |
| Decoupled pole | Commitment waits on memory, motivation, social rank, anticipated consequences |

**Selection without arbiter**: no separate comparator picks the configuration. Circuits differ in integration steps between sensing and acting; **the circuit that reaches commitment state within the available time governs**. Short deadline → short-path, weakly decoupled circuits; long deadline → long-path, strongly decoupled ones. Constrain response window to a few hundred ms and participants express a practiced response they know to be wrong. Path length is not the whole story: pre-primed circuits commit first; evidence-accumulation rate matters as much as distance.

**Urgency** is a relation between situation and self-maintaining organization (viability norms), not a stimulus property. Decoupling buys flexibility but costs time.

**CRR architecture**: combinatorial (many routes of different lengths) + reciprocal + reentrant. Combinatorial property affords the range — decoupling is purchased by *interposing circuitry*, not by adding a governor to an unchanged machine. Reciprocity leaves ordering open.

## Evidence Domains (control changing hands)

- **Practice shifts control** (reversible plus-maze): early place strategy ← hippocampus; late turn strategy ← caudate. Caudate inactivation after the shift *returns rats to the place strategy* — displaced solution remains available. Striatal ACh rises only at the shift; hippocampal ACh stays elevated → no handover-with-disengagement. DMS neurons track sequence init/exec/termination even after habitual overtraining; 5 human outcome-devaluation studies find NO increase in habitual control after overtraining.
- **Cortico-cerebellar loop**: ALM cortex initiates cerebellar (fastigial) preparatory state; perturbing fastigial during delay disrupts later licking and *weakens cortical preparation* via thalamus. Neither holds a fixed position.
- **Thalamocortical direction reverses with task phase**: MD→PFC needed for delay maintenance; PFC→MD needed for subsequent choice. MD doesn't encode attentional rules — it *amplifies local PFC interactions* so rule-specific activity persists. Pulvinar synchronizes visual areas per attentional focus.
- **Extinction is reciprocal**: amygdala "extinction neurons" may act upstream of infralimbic consolidation; NMDA blockade in amygdala dose-dependently impairs extinction. Nucleus reuniens: early extinction = 3–6 Hz tracking freezing → later 6–9 Hz coherence linking PFC-HPC; inactivation reduces coherence and revives fear; 8 Hz stimulation limits relapse. Which regime reuniens occupies depends on learning phase, not fixed nucleus role.
- **Urgency reassigns**: dorsal PAG applies synaptic threshold to SC threat input; PAG represents threat probability/prediction error and *teaches* amygdala (via thalamus); learned expectation suppresses the PAG response via CeA projection — amygdala regulates the signal that regulates its own plasticity.
- **Affordance-dependent routing**: dorsal premammillary hypothalamus drives escape vigor through PAG, but recruits an anteromedial thalamic route *only when terrain offers something to exploit* (rope, blocks).
- **Learning relocates control**: looming extinction leaves SC/PAG attenuated while vHPC ensembles carry the restored response. Reverse: V1 teaches looming suppression via vLGN, but lasting plasticity is stored in the thalamic target. Fear retrieval: prelimbic-amygdala shortly after learning → paraventricular thalamus a day later.

## Testable Signature (rejection criteria)

If heterarchy holds, among structures supporting a shared capacity:
- (a) dominant influence within a pair should **reverse** across contexts differing in urgency, history, or affordances;
- (b) each structure should shape what the other **learns or expresses** (beyond bidirectional signaling);
- (c) relations mapped across contexts should form a **loop** — no ranking survives.

If relations instead fall into a consistent ranking with context changing only strength → hierarchical account vindicated, heterarchy false. **One reliable reversal rejects stable pairwise ordering; one cycle rejects composition.**

Deadline test: hold evidence, contingencies, alternatives fixed; vary only decision deadline → the circuit whose activity predicts (and whose perturbation changes) the response should shift.

## Methodological Traps (toolkit encodes the disputed hypothesis)

1. **Modularity maximization presupposes near-decomposability** — it *defines* good decomposition as max within/between, so using it to ask whether the brain is near-decomposable begs the question. Methods without assortativity recover core–periphery / disassortative structure modularity cannot represent.
2. **Monosynaptic reasoning underestimates influence**: amygdala directly links ~40% of PFC but reaches ~90% with one additional connection; functional connectivity predicted better by **communicability** (all-paths) than direct paths.
3. **Cortico-centric analysis** cannot evaluate a claim about the failure of a cortical apex on cortex-only data.
4. **Session-averaged FC may estimate a quantity corresponding to no configuration the system ever occupied**; same anatomy can express several distinct effective-connectivity patterns by dynamical state alone.
5. **DCM does not forbid cycles** but only compares the model space the investigator specifies — cyclic alternatives are examined only when someone includes them.

## McCulloch's Diadrome (historical root)

Circular preference (A>B, B>C, C>A) under constant conditions → no single value scale → any network producing it must contain a **diadrome**: a loop running *between* competing circuits. Topological, sign-independent: merely summative connections (singly insufficient, jointly sufficient) produce the same circularity. What defeats ranking is the loop, not coupling sign.

## Implementation Guidance

**Analyzing control claims in data:**
1. Do not average away context — estimate directed influence *separately per urgency condition, learning phase, task phase*.
2. Test explicitly for dominance reversal (pairwise) and cycles (3+ relations) rather than fitting acyclic model spaces.
3. Prefer communicability over direct-path metrics for influence prediction.
4. Treat probe-then-inactivate logic as the gold standard for revealing latent controllers (plus-maze: caudate inactivation post-shift reveals dormant hippocampal strategy).
5. Operationalize decoupling: how much does the response depend on variables not present in the immediate stimulus (history, state, expectation)? This is a measurable quantity candidate.

**Modeling:**
- Use models whose nodes/edges can change with context, not fixed graphs. Trajectory-level control without a posited controller (competition among carrier circuits).
- For HPA axis, circadian system, feeding circuits, motor hierarchy: apply the same composition test — do named hierarchies fail to compose when tested by these criteria?

## Relation to Adjacent Frameworks

- **Shallow brain hypothesis** (Suzuki/Pennartz/Aru 2023): compatible — both reject deep chains; heterarchy adds the composition criterion and the decoupling spectrum.
- **Predictive coding / hierarchical active inference**: open question — does the composition argument apply to their hierarchies (levels constraining levels), or do they escape it?
- **Network model of emotion** (Pessoa 2017/2022): extends "function is distributed" to "control is relational".

## Pitfalls

- Heterarchy ≠ equipotentiality ≠ holism. Regions differ; projections are asymmetric; some structures are necessary. Anatomy **underdetermines** which relation operates in the moment.
- A momentary configuration can correctly be described hierarchically (diffuse unreciprocated projection → local controller/controlled description valid; tens-of-ms configurations exhibit real asymmetries). The claim concerns scope of description, not the brain's standing organization.
- "Fast/slow dual systems" is the hierarchical picture in disguise; the spectrum replaces it with one architecture at continuum positions.

## Key Experimental Anchors

| Result | Citation in paper |
|--------|------------------|
| Reversible maze + double inactivation | [36][37] |
| ALM–fastigial reciprocal preparation | [40] |
| MD↔PFC phase-dependent direction | [41] |
| Reuniens 3–6→6–9 Hz regime shift | [50] |
| PAG teaching-signal to amygdala; CeA suppression of PAG | [52–59] |
| Affordance-dependent escape routing | [20][60] |
| Looming extinction relocating to vHPC | [62] |
| V1→vLGN plasticity storage | [63] |
| PVT retrieval timing shift | [64] |
| Constrained deadline → wrong practiced response | [75] |

## Cross-References

- Related skills: `brain-network-controllability`, `directional-coordination-hierarchy-brain`, `quiet-edge-centric-brain-synchronization`
- For phase/oscillation formalism of coupled units: `izhikevich-weak-coupling-phase-model`
