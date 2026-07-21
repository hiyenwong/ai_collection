---
name: physics-guided-quantum-learning
description: "Physics-guided and physics-informed quantum machine learning methodologies — embedding physical priors (symmetries, conservation laws, Hamiltonians) into VQCs, QNNs, and quantum classifiers for improved accuracy, trainability, and physical consistency"
---

# Physics-Guided Quantum Learning

## Overview

Methodologies for embedding physical knowledge (symmetries, conservation laws, Hamiltonians, order parameters) into quantum machine learning pipelines including Variational Quantum Circuits (VQCs), Quantum Neural Networks (QNNs), and quantum classifiers. Physical priors improve classification accuracy, mitigate barren plateaus, ensure physical consistency of predictions, and reduce required circuit depth compared to generic quantum ML approaches.

## Physics-Informed VQC Architecture (arXiv: 2606.14489)

### Symmetry-Preserving Ansatz Design
1. Identify the symmetry group of the target Hamiltonian (e.g., Z2, U(1), SU(2))
2. Construct parameterized gates that commute with symmetry operators
3. Remove gates that violate known conservation laws
4. Include physics-motivated entanglement patterns matching system correlation structure

### Physics-Regularized Loss Function
- Composite loss: L = L_classification + λ × L_physics
- Physics loss terms:
  - **Symmetry violation penalty**: ||[U(θ), S]||² where S is the symmetry operator
  - **Order parameter alignment**: ⟨O⟩_predicted vs ⟨O⟩_known
  - **Energy constraints**: ⟨H⟩ within expected range for the target phase
- Tune λ via validation on held-out states

### Application: Phase Detection in Strongly Correlated Matter
- System examples: Ising model, Heisenberg model, Hubbard model
- Phases: ferromagnetic vs paramagnetic, trivial vs topological
- Key advantage: VQC learns to detect phase order without explicit analytical order parameter calculation
- Near critical points: physics-informed VQC outperforms generic VQC due to symmetry-aware encoding

## Structuring This Skill

[TODO: Choose the structure that best fits this skill's purpose. Common patterns:

**1. Workflow-Based** (best for sequential processes)
- Works well when there are clear step-by-step procedures
- Example: DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
- Structure: ## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
- Structure: ## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 2...

**3. Reference/Guidelines** (best for standards or specifications)
- Works well for brand guidelines, coding standards, or requirements
- Example: Brand styling with "Brand Guidelines" → "Colors" → "Typography" → "Features"
- Structure: ## Overview → ## Guidelines → ## Specifications → ## Usage...

**4. Capabilities-Based** (best for integrated systems)
- Works well when the skill provides multiple interrelated features
- Example: Product Management with "Core Capabilities" → numbered capability list
- Structure: ## Overview → ## Core Capabilities → ### 1. Feature → ### 2. Feature...

Patterns can be mixed and matched as needed. Most skills combine patterns (e.g., start with task-based, add workflow for complex operations).

Delete this entire "Structuring This Skill" section when done - it's just guidance.]

## [TODO: Replace with the first main section based on chosen structure]

[TODO: Add content here. See examples in existing skills:
- Code samples for technical skills
- Decision trees for complex workflows
- Concrete examples with realistic user requests
- References to scripts/templates/references as needed]

## Resources
- [references/physics-informed-vqc-phase-detection-2606-14489.md](references/physics-informed-vqc-phase-detection-2606-14489.md) — Session notes from arXiv: 2606.14489 with detailed methodology, symmetry groups, and application examples
- Related skills: `physics-informed-vqc-phase-detection` (class-level umbrella for VQC phase detection), `fourier-vqc-nonlinear-embedding-barren-plateau`, `quantum-ml-patterns` that demonstrate how to organize different types of bundled resources:

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Examples from other skills:**
- PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
- DOCX skill: `document.py`, `utilities.py` - Python modules for document processing

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read by Claude for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Claude should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Claude produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.

---

**Any unneeded directories can be deleted.** Not every skill requires all three types of resources.
