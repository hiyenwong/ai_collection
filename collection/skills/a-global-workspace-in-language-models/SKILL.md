---
name: a-global-workspace-in-language-models
description: "A global workspace in language models"
metadata:
  title: "A global workspace in language models"
  url: "https://www.anthropic.com/research/global-workspace"
  date: "Jul 6, 2026"
  section: "hero"
  category: "Interpretability"
license: Complete terms in LICENSE.txt
---

# Jacobian Lens (J-lens) Interpretability Methodology

## Overview
The Jacobian lens (J-lens) is a technique for identifying and analyzing the "J-space" - a collection of internal neural patterns in language models that function as a global workspace for consciously accessible thoughts. Unlike standard chain-of-thought reasoning, the J-space operates silently in the model's internal activations, allowing the model to think about concepts without writing them down.

## Key Properties
- **Consciously accessible**: The J-space contains thoughts the model can report on, deliberately bring to mind, and reason with
- **Broadcasting hub**: J-space patterns have especially strong connections to the rest of the neural network, allowing information to be shared across different systems  
- **Limited capacity**: Holds only a few dozen concepts at a time, accounting for less than 10% of overall activity
- **Emergent structure**: Not designed or programmed, but emerges during training as a useful way to organize computation

## How It Works
1. **Finding the J-space**: For every word in the model's vocabulary, the J-lens finds the internal activity pattern that makes the model more likely to say that word at some point in the future
2. **Reading contents**: Apply the lens to internal activity to get a list of words representing the current J-space contents  
3. **Layer evolution**: Apply the technique across different layers to watch how silent thoughts evolve during processing

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

This skill includes example resource directories that demonstrate how to organize different types of bundled resources:

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
