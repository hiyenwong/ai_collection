---
name: skill-creator
description: Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.
license: Complete terms in LICENSE.txt
---

# Skill Creator

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing
specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific
domains or tasks—they transform Claude from a general-purpose agent into a specialized agent
equipped with procedural knowledge that no model can fully possess.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

## Core Principles

### Concise is Key

The context window is a public good. Skills share the context window with everything else Claude needs: system prompt, conversation history, other Skills' metadata, and the actual user request.

**Default assumption: Claude is already very smart.** Only add context Claude doesn't already have. Challenge each piece of information: "Does Claude really need this explanation?" and "Does this paragraph justify its token cost?"

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match the level of specificity to the task's fragility and variability:

**High freedom (text-based instructions)**: Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.

**Medium freedom (pseudocode or scripts with parameters)**: Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.

**Low freedom (specific scripts, few parameters)**: Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

Think of Claude as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

### Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

#### SKILL.md (required)

Every SKILL.md consists of:

- **Frontmatter** (YAML): Contains `name` and `description` fields. These are the only fields that Claude reads to determine when the skill gets used, thus it is very important to be clear and comprehensive in describing what the skill is, and when it should be used.
- **Body** (Markdown): Instructions and guidance for using the skill. Only loaded AFTER the skill triggers (if at all).

#### Bundled Resources (optional)

##### Scripts (`scripts/`)

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten.

- **When to include**: When the same code is being rewritten repeatedly or deterministic reliability is needed
- **Example**: `scripts/rotate_pdf.py` for PDF rotation tasks
- **Benefits**: Token efficient, deterministic, may be executed without loading into context
- **Note**: Scripts may still need to be read by Claude for patching or environment-specific adjustments

##### References (`references/`)

Documentation and reference material intended to be loaded as needed into context to inform Claude's process and thinking.

- **When to include**: For documentation that Claude should reference while working
- **Examples**: `references/finance.md` for financial schemas, `references/mnda.md` for company NDA template, `references/policies.md` for company policies, `references/api_docs.md` for API specifications
- **Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides
- **Benefits**: Keeps SKILL.md lean, loaded only when Claude determines it's needed
- **Best practice**: If files are large (>10k words), include grep search patterns in SKILL.md
- **Avoid duplication**: Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps SKILL.md lean while making information discoverable without hogging the context window. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files.

##### Assets (`assets/`)

Files not intended to be loaded into context, but rather used within the output Claude produces.

- **When to include**: When the skill needs files that will be used in the final output
- **Examples**: `assets/logo.png` for brand assets, `assets/slides.pptx` for PowerPoint templates, `assets/frontend-template/` for HTML/React boilerplate, `assets/font.ttf` for typography
- **Use cases**: Templates, images, icons, boilerplate code, fonts, sample documents that get copied or modified
- **Benefits**: Separates output resources from documentation, enables Claude to use files without loading them into context

#### What to Not Include in a Skill

A skill should only contain essential files that directly support its functionality. Do NOT create extraneous documentation or auxiliary files, including:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- etc.

The skill should only contain the information needed for an AI agent to do the job at hand. It should not contain auxilary context about the process that went into creating it, setup and testing procedures, user-facing documentation, etc. Creating additional documentation files just adds clutter and confusion.

### Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude (Unlimited because scripts can be executed without reading into context window)

#### Progressive Disclosure Patterns

Keep SKILL.md body to the essentials and under 500 lines to minimize context bloat. Split content into separate files when approaching this limit. When splitting out content into other files, it is very important to reference them from SKILL.md and describe clearly when to read them, to ensure the reader of the skill knows they exist and when to use them.

**Key principle:** When a skill supports multiple variations, frameworks, or options, keep only the core workflow and selection guidance in SKILL.md. Move variant-specific details (patterns, examples, configuration) into separate reference files.

**Pattern 1: High-level guide with references**

```markdown
# PDF Processing

## Quick start

Extract text with pdfplumber:
[code example]

## Advanced features

- **Form filling**: See [FORMS.md](FORMS.md) for complete guide
- **API reference**: See [REFERENCE.md](REFERENCE.md) for all methods
- **Examples**: See [EXAMPLES.md](EXAMPLES.md) for common patterns
```

Claude loads FORMS.md, REFERENCE.md, or EXAMPLES.md only when needed.

**Pattern 2: Domain-specific organization**

For Skills with multiple domains, organize content by domain to avoid loading irrelevant context:

```
bigquery-skill/
├── SKILL.md (overview and navigation)
└── reference/
    ├── finance.md (revenue, billing metrics)
    ├── sales.md (opportunities, pipeline)
    ├── product.md (API usage, features)
    └── marketing.md (campaigns, attribution)
```

When a user asks about sales metrics, Claude only reads sales.md.

Similarly, for skills supporting multiple frameworks or variants, organize by variant:

```
cloud-deploy/
├── SKILL.md (workflow + provider selection)
└── references/
    ├── aws.md (AWS deployment patterns)
    ├── gcp.md (GCP deployment patterns)
    └── azure.md (Azure deployment patterns)
```

When the user chooses AWS, Claude only reads aws.md.

**Pattern 3: Conditional details**

Show basic content, link to advanced content:

```markdown
# DOCX Processing

## Creating documents

Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).

## Editing documents

For simple edits, modify the XML directly.

**For tracked changes**: See [REDLINING.md](REDLINING.md)
**For OOXML details**: See [OOXML.md](OOXML.md)
```

Claude reads REDLINING.md or OOXML.md only when the user needs those features.

**Important guidelines:**

- **Avoid deeply nested references** - Keep references one level deep from SKILL.md. All reference files should link directly from SKILL.md.
- **Structure longer reference files** - For files longer than 100 lines, include a table of contents at the top so Claude can see the full scope when previewing.

## Skill Creation Process

Skill creation involves these steps:

1. Understand the skill with concrete examples
2. Plan reusable skill contents (scripts, references, assets)
3. Initialize the skill (run init_skill.py)
4. Edit the skill (implement resources and write SKILL.md)
5. Package the skill (run package_skill.py)
6. Iterate based on real usage

Follow these steps in order, skipping only if there is a clear reason why they are not applicable.

### Step 1: Understanding the Skill with Concrete Examples

Skip this step only when the skill's usage patterns are already clearly understood. It remains valuable even when working with an existing skill.

To create an effective skill, clearly understand concrete examples of how the skill will be used. This understanding can come from either direct user examples or generated examples that are validated with user feedback.

For example, when building an image-editor skill, relevant questions include:

- "What functionality should the image-editor skill support? Editing, rotating, anything else?"
- "Can you give some examples of how this skill would be used?"
- "I can imagine users asking for things like 'Remove the red-eye from this image' or 'Rotate this image'. Are there other ways you imagine this skill being used?"
- "What would a user say that should trigger this skill?"

To avoid overwhelming users, avoid asking too many questions in a single message. Start with the most important questions and follow up as needed for better effectiveness.

Conclude this step when there is a clear sense of the functionality the skill should support.

### Step 2: Planning the Reusable Skill Contents

To turn concrete examples into an effective skill, analyze each example by:

1. Considering how to execute on the example from scratch
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly

Example: When building a `pdf-editor` skill to handle queries like "Help me rotate this PDF," the analysis shows:

1. Rotating a PDF requires re-writing the same code each time
2. A `scripts/rotate_pdf.py` script would be helpful to store in the skill

Example: When designing a `frontend-webapp-builder` skill for queries like "Build me a todo app" or "Build me a dashboard to track my steps," the analysis shows:

1. Writing a frontend webapp requires the same boilerplate HTML/React each time
2. An `assets/hello-world/` template containing the boilerplate HTML/React project files would be helpful to store in the skill

Example: When building a `big-query` skill to handle queries like "How many users have logged in today?" the analysis shows:

1. Querying BigQuery requires re-discovering the table schemas and relationships each time
2. A `references/schema.md` file documenting the table schemas would be helpful to store in the skill

To establish the skill's contents, analyze each concrete example to create a list of the reusable resources to include: scripts, references, and assets.

### Step 3: Initializing the Skill

At this point, it is time to actually create the skill.

Skip this step only if the skill being developed already exists, and iteration or packaging is needed. In this case, continue to the next step.

When creating a new skill from scratch, always run the `init_skill.py` script. The script conveniently generates a new template skill directory that automatically includes everything a skill requires, making the skill creation process much more efficient and reliable.

Usage:

```bash
~/.hermes/skills/skill-creator/scripts/init_skill.py <skill-name> --path ~/.hermes/skills
```

The script:

- Creates the skill directory at the specified path
- Generates a SKILL.md template with proper frontmatter and TODO placeholders
- Creates example resource directories: `scripts/`, `references/`, and `assets/`
- Adds example files in each directory that can be customized or deleted

If the script reports "Skill directory already exists", either remove the existing directory or create it manually:

```bash
mkdir -p ~/.hermes/skills/<skill-name>/{scripts,references,assets}
# Then write SKILL.md directly
```

After initialization, customize or remove the generated SKILL.md and example files as needed.

After initialization, customize or remove the generated SKILL.md and example files as needed.

**Pitfall (2026-06-01 confirmed)**: `init_skill.py` fails with "Error: Skill directory already exists" if another agent already created it (e.g., parallel sessions or previous cron runs). If this happens, read the existing SKILL.md first — it may contain content from the other agent. Overwrite with your own content if needed, but check for sibling work before writing.

**Pitfall: Ambiguous skill name loading**: Skills with the same name may exist across multiple categories (e.g., `knowledge-graph-ops` exists at both `~/.hermes/skills/knowledge-graph-ops/` and `~/.hermes/skills/ai_collection/knowledge-graph-ops/`). Calling `skill_view(name)` or `skill_manage()` with the bare name triggers an ambiguous-match error.

**Resolution strategy**:
- **For skill_view**: Use the categorized path (e.g., `skill_view(name='research/arxiv-to-skill-research-workflow')`)
- **For skill_manage**: The tool picks one version automatically — check the `path` field in the response to verify which was modified
- **Which version to use**: Prefer the version in the category that matches your workflow (e.g., `ai_collection/` for research workflows, `neuroscience/` for domain-specific skills). The `ai_collection/` category is the primary repository for arXiv-derived research skills. Local skills (`~/.hermes/skills/<name>/`) are user-specific customizations.

**Prevention**: Name skills with unique, specific identifiers from the start. If creating a skill for a research paper, include the arxiv ID or a distinctive method name (e.g., `mcts-encoding-discovery-qml` instead of generic `quantum-encoding`).

### Step 4: Edit the Skill

When editing the (newly-generated or existing) skill, remember that the skill is being created for another instance of Claude to use. Include information that would be beneficial and non-obvious to Claude. Consider what procedural knowledge, domain-specific details, or reusable assets would help another Claude instance execute these tasks more effectively.

#### Learn Proven Design Patterns

Consult these helpful guides based on your skill's needs:

- **Multi-step processes**: See references/workflows.md for sequential workflows and conditional logic
- **Specific output formats or quality standards**: See references/output-patterns.md for template and example patterns
- **Network/API failures**: See references/network-api-failures.md for arXiv API, web search, and browser tool failure patterns and fallback strategies

These files contain established best practices for effective skill design.

#### Start with Reusable Skill Contents

To begin implementation, start with the reusable resources identified above: `scripts/`, `references/`, and `assets/` files. Note that this step may require user input. For example, when implementing a `brand-guidelines` skill, the user may need to provide brand assets or templates to store in `assets/`, or documentation to store in `references/`.

Added scripts must be tested by actually running them to ensure there are no bugs and that the output matches what is expected. If there are many similar scripts, only a representative sample needs to be tested to ensure confidence that they all work while balancing time to completion.

Any example files and directories not needed for the skill should be deleted. The initialization script creates example files in `scripts/`, `references/`, and `assets/` to demonstrate structure, but most skills won't need all of them.

#### Update SKILL.md

**Writing Guidelines:** Always use imperative/infinitive form.

##### Frontmatter

Write the YAML frontmatter with `name` and `description`:

- `name`: The skill name
- `description`: This is the primary triggering mechanism for your skill, and helps Claude understand when to use the skill.
  - Include both what the Skill does and specific triggers/contexts for when to use it.
  - Include all "when to use" information here - Not in the body. The body is only loaded after triggering, so "When to Use This Skill" sections in the body are not helpful to Claude.
  - Example description for a `docx` skill: "Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction. Use when Claude needs to work with professional documents (.docx files) for: (1) Creating new documents, (2) Modifying or editing content, (3) Working with tracked changes, (4) Adding comments, or any other document tasks"

Do not include any other fields in YAML frontmatter.

> **Exception for ai_collection/category skills**: Skills created under named categories (like `ai_collection`, `neuroscience`, `quantum`) that represent research papers benefit from structured metadata — but `quick_validate.py` only allows `name`, `description`, `license`, `metadata`, and `allowed-tools` as top-level keys. **Put paper-specific fields inside a `metadata:` block**, not as top-level keys:
>
> **CRITICAL (2026-06-04 Verified)**: 
> - `arxiv_id` MUST be under `metadata:` key — NOT top-level
> - Previous skills with top-level `arxiv_id` failed validation via `quick_validate.py`
> - Correct: `metadata: arxiv_id: "2606.03310"`
> - Wrong: `arxiv_id: "2606.03310"` (at top level causes validation failure)
> - Use `skill_manage(action='patch')` to fix invalid frontmatter in existing skills
>
> ```yaml
> name: mcts-encoding-discovery-qml
> description: "..."
> metadata:
>   arxiv_id: "2606.03310"
>   conference: "ICML 2026"
>   authors: ["Jaeyoon Sim", "Sung Woo Park"]
> license: Complete terms in LICENSE.txt
> metadata:
>   arxiv_id: "2605.18540"
>   published: "2026-05-18"
>   authors: "Author One, Author Two"
>   tags: [quantum, machine-learning, encoding, mcts]
> ```
>
> **Pitfall (2026-05-31 confirmed)**: Putting `arxiv_id`, `date`, `authors`, or `tags` as top-level keys causes `quick_validate.py` to fail with "Unexpected key(s) in SKILL.md frontmatter". The validator does NOT recognize them at top level — nest them under `metadata:` instead. If a skill's SKILL.md has invalid frontmatter keys, rewrite the entire file with corrected structure before syncing to ai_collection.

- **Creating Unified Framework Skills (Synthesis from Multiple Papers)** → See below
- **Skill Validation**: Use `quick_validate.py` from the skill-creator scripts dir. ⚠️ The validator rejects angle brackets (`<` or `>`) in the description field (2026-06-04 confirmed). Use parentheses or plain text instead (e.g., "Fock states 4 and 7" not "Fock states |4> and |7>").

When blocked on new discovery (e.g., arXiv API rate-limited) or when multiple existing skills cover related concepts, synthesize them into a unified framework skill. This produces class-level skills with richer theoretical depth than single-paper narrow skills.

**Synthesis workflow**:

1. **Discovery**: Scan existing skills via `skills_list(category='ai_collection')` → grep descriptions for shared concepts (e.g., "oscillation", "synchronization", "phase", "delay")

2. **Selection**: Choose 2-4 skills covering complementary aspects of a unified theory:
   - Example: Kuramoto phase dynamics (arXiv:2105.08288) + delay plasticity (2605.23520) + cortical information flux (2605.14680) → unified "brain oscillation synchronization framework"

3. **Read**: Load each source SKILL.md → extract key theoretical contributions, methodologies, activation keywords

4. **Synthesize**: Create unified framework skill:
   - **Name**: Class-level (e.g., `brain-oscillation-synchronization-framework`) NOT paper-specific
   - **Metadata**: Combined `arxiv_id: "2605.23520,2605.14680,2105.08288"` (comma-separated)
   - **Description**: "Unified framework for [domain] combining [concept1], [concept2], [concept3]. Activation: [keywords from all sources]"
   - **Structure**:
     - **Introduction**: Conceptual synthesis (why these theories combine)
     - **Core Components**: Section per source theory (Kuramoto, delay plasticity, information flux)
     - **Unified Theory**: Integration section showing how components interact
     - **Methodology**: Combined workflow steps from all sources
     - **Pitfalls**: Consolidated from all sources + integration-specific issues
     - **References**: Link to all source papers, existing skills

5. **Sync**: Copy to ai_collection, update INDEX.md with combined arxiv_id, git commit with multi-paper message, add to kg.db

**Benefits**:
- Class-level skill (reusable across many papers) vs narrow single-paper skill
- Richer theoretical framework from integration
- Cross-links multiple existing skills → improves discoverability
- Better activation coverage (union of keywords)

**Pitfall**: Do NOT create framework skill for unrelated papers. Only synthesize when genuine theoretical connections exist (shared mathematical foundation, complementary mechanisms, same domain with different approaches).

**Pitfall: All papers already have skills** (2026-06-01 confirmed): When every paper from a cron discovery batch already has one or more skills (sometimes 3+ duplicates), do NOT create another narrow skill. Instead:
1. Check all papers against existing skills: `grep -rl "{arxiv_id}" ~/.hermes/skills/*/SKILL.md`
2. If ALL papers have existing skills → create a **synthesis umbrella skill** that unifies them into a higher-level framework
3. If SOME papers lack skills → create individual skills for new ones + synthesis umbrella for the set

**Pattern: Multi-Scale Synthesis** (2026-06-01 confirmed): When papers cover complementary abstraction levels, synthesize them hierarchically:
- **Systems level** → brain-wide dynamics, network states
- **Algorithmic level** → inference mechanisms, predictive coding
- **Learning level** → plasticity rules, training dynamics
- **Measurement level** → experimental tools, simulation

This produces class-level framework skills that are richer than any single paper.

##### Body

Write instructions for using the skill and its bundled resources.

### Step 5: Packaging a Skill

Once development of the skill is complete, it must be packaged into a distributable .skill file that gets shared with the user. The packaging process automatically validates the skill first to ensure it meets all requirements:

```bash
scripts/package_skill.py <path/to/skill-folder>
```

Optional output directory specification:

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

The packaging script will:

1. **Validate** the skill automatically, checking:

   - YAML frontmatter format and required fields
   - Skill naming conventions and directory structure
   - Description completeness and quality
   - File organization and resource references

2. **Package** the skill if validation passes, creating a .skill file named after the skill (e.g., `my-skill.skill`) that includes all files and maintains the proper directory structure for distribution. The .skill file is a zip file with a .skill extension.

If validation fails, the script will report the errors and exit without creating a package. Fix any validation errors and run the packaging command again.

### Step 6: Iterate

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

**Iteration workflow:**

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how SKILL.md or bundled resources should be updated
4. Implement changes and test again

## Activation Keywords

- `skill-creator`
- `skill-creator`
- `skill creator`

## Tools Used

- `exec`
- `read`
- `write`
- `edit`

### YAML Frontmatter Gotcha

**Colons in ANY free-text field break YAML parsing.** If a field (description, source, tags, or any value containing free text) contains a colon (e.g., `source: Anthropic Research - Project Glasswing: An Initial Update`), wrap the entire value in double quotes:

```yaml
description: "Methodology for X: handles case Y with parameter Z"
source: "Anthropic Research - Project Glasswing: An Initial Update (May 22, 2026)"
```

Without quotes, YAML interprets the colon as a key-value separator and fails with `mapping values are not allowed here`. The `quick_validate.py` script catches this, but it is faster to quote from the start when any field contains punctuation that YAML might misinterpret (colons, commas in strings, leading special chars).

**Multi-line lists also sometimes need quotes.** For tags with internal colons or commas that should be literal rather than parsed as YAML list syntax, prefer the inline array form `tags: [tag1, tag2]` over multiline multi-line form to avoid ambiguity.

## Common Pitfalls

- **Nested directory on copy**: `init_skill.py` creates `{skill-name}/{skill-name}/SKILL.md`. When copying to another location (e.g., `cp -r ~/.hermes/skills/{name}/ /dest/{name}/`), this creates `/dest/{name}/{name}/SKILL.md`. Fix after copy: `mv /dest/{name}/{name}/SKILL.md /dest/{name}/ && rm -rf /dest/{name}/{name}`. Or copy the inner directory directly: `cp -r ~/.hermes/skills/{name}/{name}/ /dest/{name}/`.

- **Empty directory from cross-reference**: When an umbrella skill references a specific skill by name (e.g., "See `hybrid-quantum-financial-security` skill"), verify the directory actually contains a SKILL.md — it may have been created as an empty placeholder. Always check with `ls ~/.hermes/skills/{category}/{skill-name}/` before assuming the skill exists.

- **Git push timeout in ai_collection**: `git push` from the ai_collection repo can time out (30s+) due to network connectivity issues. The commit succeeds locally. If push times out, retry once, then note the issue in the daily report for manual follow-up. Do NOT retry indefinitely.

- **Template description parsed as YAML list**: `init_skill.py` generates top-level SKILL.md with `description: [TODO: ...]`. YAML parses the bracket syntax as a list, not a string, so `quick_validate.py` fails with "Description must be a string, got list". **Fix**: Always write your actual SKILL.md to the top-level path (not the nested subdirectory) before running `quick_validate.py`. After copying content from the nested `SKILL-NAME/SKILL-NAME/SKILL.md` to `SKILL-NAME/SKILL.md`, remove the nested directory, then validate.

- **Validate the right file**: `quick_validate.py` takes a **directory path** (`<skill-folder>/`), NOT a file path (`<skill-folder>/SKILL.md`). It searches for SKILL.md inside the given directory. `ls SKILL-NAME/` should show `SKILL.md` directly, not another directory with that name.

## Instructions for Agents

1. Read the task description carefully
2. Follow the step-by-step process
3. Use the appropriate tools
4. Verify the results

## Examples

### Example 1: Basic Usage

**User:** <example user request>

**Agent:** <example agent response>

### Example 2: Advanced Usage

**User:** <example user request>

**Agent:** <example agent response>
