---
name: unified-vv-activity-schema-jpl
description: Use when standardizing verification/validation workflows or building requirements-to-evidence traceability schemas. JPL relationship-based V&V schema.
category: ai_collection
---

# Unified V&V Activity Schema (JPL)

## Paper Source
- **arXiv**: 2609.28600 (2026-09-23)
- **Title**: Developing a Unified Verification and Validation Activity Standard at JPL
- **Authors**: Vierlboeck, Van Wyk, Sanchez, Oaida, Eberhart, Piette Gomez, Delp, Jorritsma, Desharnais (JPL/Caltech)
- **Domain**: Systems engineering practice / cs.SE + eess.SY

## Core Thesis
V&V practice fragmentation across projects/missions is solved by a **relationship-based schema**: separate V&V method item types (Test, Analysis, Inspection, Demonstration, Review of Design) sharing a **common core attribute set**, connected through **explicit bidirectional relationships** to requirements, venues, and evidence. Formalized as a **platform-agnostic SysML model** — implementable in any requirements management tool (JPL uses Jama).

## Schema Building Blocks

### 1. Item Types (inheritance-based MVP structure)
```
Base MVP block (universal attributes)
  ├─ identifier, ownership, status tracking, scheduling, evidence documentation
  ├─ Test          → + venue info
  ├─ Analysis      → + analytical metadata
  ├─ Inspection    → + method-specific fields
  ├─ Demonstration → + venue info
  └─ Review of Design → + review metadata
```
Key decision: earlier single generic "V&V Activity" type failed because "the structures/hierarchies are different between tests and analysis" — separate item types with shared core attributes won.

### 2. Relationship Types (bidirectional, explicit directionality)
| Relationship | Connects | Purpose |
|---|---|---|
| **Verified By** / Verifies | requirement ↔ V&V Activity | foundational traceability (one-to-many AND many-to-one) |
| **Executed In** | test/demonstration VA ↔ Venue | where performed, facility usage tracking |
| upstream/downstream | change propagation | requirement change flags affected VAs; VA issues flag requirements |

Bidirectional philosophy captures **flow down** (requirements → activities) and **flow up** (results → completion status). Enables rollup status indicators at requirement level.

### 3. Venue (critical addition)
Explicit item type for physical/virtual environments (test facilities, labs, simulation environments, field sites). Enables resource planning, schedule deconfliction, environmental-condition documentation across campaigns.

### 4. Supporting mechanisms
- **Outbound references**: traceability across platform/repository boundaries (simulation data, test equipment control, external evidence storage)
- **Templates** (free/rich text): controlled content structure without rigid mandates — balances standardization vs project-specific customization
- **Pick lists (two-tier)**: core standard lists (e.g. status: Not Started/In Work/Complete/Waived) + extensible project-specific lists (e.g. facility names)

## Human-Centered Design Process (HCDP)
Schema developed through workshops with **29 practitioners** across mission types using the **Double Diamond** scaffold with voting, grouping, time-boxing:
- 85% agreed "final MVP can be used by all of JPL's missions"
- 100% agreed "MVP emerged from the group's shared understanding" and "workshop format allowed me to share opinions"
- Lesson learned: starting from scratch can overwhelm — consider pre-gathering use cases from representative practitioners, then using workshop time for group review

## SysML Information Model
- Block Definition Diagrams (BDD) for item structure + inheritance trace table
- Relationship schema modeled as a **separate BDD** with association blocks carrying semantic naming + directionality
- Internal Block Diagram (IBD) for information flows between requirements, VAs, evidence
- Platform-independence: the SysML model IS the standard; Jama is one implementation → tool-agnostic, evolvable

## Measured Benefits (institutional)
1. **Cross-discipline collaboration**: common language for VAs across engineering domains
2. **Traceability + impact assessment**: requirement changes auto-flag affected VAs; bidirectional coverage reduces gaps/overlaps
3. **Targeted planning**: similar approaches identifiable across system elements → resource optimization, test consolidation, facility utilization
4. **Documentation time savings** + improved reviewer readability
5. **Inner-source automation flywheel**: all projects share the same information architecture → automations built for one project deploy to all without modification; especially helps small projects lacking capacity
6. **Knowledge transfer**: common framework makes previous missions' V&V approaches adaptable, accelerating planning

## Reusable Implementation Patterns

### Pattern 1: Relationship-first schema design
When standardizing fragmented practice across teams: model explicit typed relationships between artifacts (requirement↔activity↔venue↔evidence) BEFORE defining artifact field structure. The relationship network is the durable asset; fields evolve.

### Pattern 2: Common-core + method-specific inheritance
Shared base attribute set guarantees cross-project consistency while subclasses absorb method-specific divergence — resolves "one generic type fits nobody" vs "fully custom types fragment" tension.

### Pattern 3: Two-tier controlled vocabulary
Core pick lists standardize semantics institution-wide; extensible lists absorb legitimate project variation (partner orgs that can't align). Never force full standardization where exchange partners differ.

### Pattern 4: HCDP workshop scaffolding
Double Diamond + voting + grouping + time-boxing to converge diverse practitioner practice into one MVP schema. Preregister use cases from representative users before the workshop to avoid input overload.

### Pattern 5: Platform-agnostic formalization
Formalize the standard in a modeling language (SysML BDD/IBD) independent of the implementation tool. Tool churns; the model standard persists. Implementations become interchangeable.

## When to Apply
- Multi-project/multi-team V&V or test-management standardization
- Building requirements-to-evidence digital threads / traceability matrices
- Requirements management platform selection or migration (Jama, DOORS, Polarion, etc.)
- Designing test-facility/resource management schemas
- Any fragmented engineering documentation practice needing convergence without losing project flexibility
- Graph-analytics plans over engineering artifacts (relationship mining → coverage patterns, resource utilization insights)

## Limitations
- Single-institution case study (JPL); mission-domain specificity may not transfer directly to other industries
- Benefits partially qualitative/expected (time savings "expected as" adoption grows); no quantitative baseline measurements reported yet
- Adoption-dependent network effects: automation flywheel and knowledge transfer scale only as adoption expands

## Related Skills
- [[requirement-bound-verified-commissioning]] — complementary: deterministic acceptance at requirement boundaries; this schema provides the organizing structure such boundaries live in
- [[kg-operations]] — relationship-based schemas map naturally to knowledge graphs
- [[sheaf-consistency-mbse]] — multi-view consistency in MBSE

## Key References
- [16] Prior JPL relationship-based requirements schema (extended by this work)
- Boehm 1984 — verification vs validation distinction
- VDI/VDE 2206 — mechatronic V-model (referenced in companion paper)
