---
name: coral-open-ended-discovery
description: Autonomous multi-agent open-ended discovery workflow inspired by the CORAL paper. Use when the task requires sustained search, iterative improvement, multi-agent exploration, shared knowledge accumulation, asynchronous parallel attempts, periodic reflection, or heartbeat-style redirection. Best for research discovery, algorithm design, systems optimization, skill discovery, long-running coding/search tasks, and open-ended problems where a single linear attempt is likely to plateau.
---

# CORAL-Style Open-Ended Discovery

## Overview

Use this skill when the user is not asking for a one-shot answer, but for **continued discovery under uncertainty**.

The core idea from CORAL is:
- run multiple long-horizon exploration threads
- accumulate reusable knowledge in shared memory/files
- periodically reflect and consolidate
- redirect when progress stalls

In OpenClaw, do **not** try to fully reproduce the CORAL infrastructure unless explicitly asked. Instead, map the paper's principles onto OpenClaw-native primitives:

- `sessions_spawn` → long-running parallel exploration
- `memory/` + workspace files → shared persistent memory
- `cron` or heartbeat-style reminders → periodic reflection / redirection
- isolated sessions / subagents → asynchronous multi-agent organization

## When To Use This Skill

Use this skill when the task has most of these properties:

1. **Open-ended objective**
   - “Keep improving this”
   - “Search for a better design”
   - “Explore multiple approaches”
   - “See what works best”

2. **Long-horizon progress matters more than one-shot accuracy**
   - code optimization
   - algorithm search
   - research discovery
   - system tuning
   - paper-to-skill distillation

3. **Knowledge accumulation is useful**
   - findings should be written down
   - later attempts should reuse earlier discoveries
   - failed attempts are informative, not just disposable

4. **Parallel exploration is beneficial**
   - different agents can try different strategies
   - direct messaging is not required; file-based knowledge sharing is enough

Do **not** use this skill for:
- simple Q&A
- deterministic short tasks
- tasks where one careful pass is enough
- tasks requiring immediate single-action completion with no iteration

## Core Mapping: CORAL → OpenClaw

| CORAL concept | OpenClaw equivalent |
|---|---|
| long-running autonomous agents | `sessions_spawn` persistent sessions or isolated runs |
| shared persistent memory | workspace files, `MEMORY.md`, `memory/*.md`, project notes |
| asynchronous multi-agent execution | multiple spawned sessions working in parallel |
| heartbeat-based interventions | `cron`, heartbeat prompts, explicit “reflect/checkpoint” messages |
| isolated workspaces | spawned sessions + separate task scopes + file discipline |
| evaluator separation | separate validation subtask / independent review pass |

## Workflow

### Step 1: Decide whether this is a CORAL-style problem

Ask:
- Does the task benefit from multiple attempts?
- Is there no obvious single best path?
- Will discoveries from one attempt help later attempts?
- Is progress likely to plateau without reflection?

If yes, use this workflow.

### Step 2: Define the search loop explicitly

Before spawning agents, define:

1. **Objective**
   - what is being improved?
   - what counts as progress?

2. **Artifacts to persist**
   - attempts
   - notes
   - reusable procedures
   - metrics / benchmark outputs

3. **Evaluation rule**
   - how will candidates be compared?
   - can evaluation be isolated from generation?

4. **Stopping / checkpoint rule**
   - fixed number of iterations?
   - time limit?
   - no-improvement trigger?

Write this down in a small file when the task is long or complex.

Recommended file pattern:

```text
memory/<topic>-discovery.md
```

Suggested sections:
- Objective
- Metrics
- Attempt log
- Promising strategies
- Dead ends
- Reusable patterns

### Step 3: Externalize memory early

CORAL works because knowledge is written down and reused.

For non-trivial discovery work, create or update a memory file immediately. Do not rely on chat history alone.

At minimum, persist:
- current objective
- constraints
- candidate strategies
- what has already been tried
- what seems promising

Use compact, high-signal notes. Prefer structured bullets over prose.

### Step 4: Spawn parallel explorers when useful

If the task is complex or benefits from diversity, spawn multiple sessions.

Typical decomposition:

- **Explorer A**: conservative / baseline improvement
- **Explorer B**: aggressive / unconventional strategy
- **Explorer C**: evaluation / benchmarking / review

Use `sessions_spawn` when:
- the work is long
- independence helps
- you want isolated exploration

Prefer different prompts rather than identical clones.

Good prompt pattern:
- assign a strategy
- require notes to be written back
- require a concise checkpoint summary
- make success criteria explicit

### Step 5: Separate generation from evaluation

A key CORAL insight is that generation and evaluation should not collapse into one untrusted loop.

When possible:
- one agent proposes
- another agent validates
- objective tooling checks the result

Examples:
- code optimization → benchmark separately
- skill creation → validate skill structure separately
- paper distillation → separate note-writing from quality review

If there is no separate agent, at least run an explicit review pass after generation.

### Step 6: Add periodic reflection / consolidation

CORAL's heartbeat mechanism is one of the most reusable ideas.

In OpenClaw, simulate this with:
- `cron` reminders
- heartbeat prompts
- explicit follow-up messages to spawned sessions

Use three reflection modes:

#### A. Per-iteration reflection
After each meaningful attempt, record:
- what changed
- whether it helped
- what to try next

#### B. Periodic consolidation
After several attempts, consolidate into:
- stable insights
- reusable procedure
- skill candidate
- shortlist of best strategies

#### C. Stagnation-triggered redirection
If no progress after several rounds:
- stop micro-optimizing
- pivot strategy
- try a different search region
- reduce / expand constraints

## Recommended Reflection Prompts

### Prompt: attempt reflection

```text
Summarize the last attempt in 5 bullets:
1. What was tried
2. What changed
3. Evidence of improvement or failure
4. What should be reused
5. Best next move
```

### Prompt: consolidation

```text
Review all recent attempts and produce:
- 3 stable insights
- 3 failed patterns to avoid
- 1 reusable workflow
- current best candidate
```

### Prompt: stagnation redirect

```text
You appear to be plateauing. Do not continue local tweaking by default.
Reassess the search space and propose 3 qualitatively different next directions.
Choose one and justify why it escapes the current local minimum.
```

## Persistence Conventions

For CORAL-style work, use these artifact types:

### Attempts
Store candidate outputs and measured results.

### Notes
Store observations, hypotheses, and failure analysis.

### Skills
If a repeated procedure emerges, convert it into a skill candidate.

Useful workspace pattern:

```text
memory/
  <topic>-discovery.md
  <topic>-attempts.md
  <topic>-skill-candidate.md
```

## OpenClaw-Native Patterns

### Pattern 1: paper → skill
Use when a paper describes a reusable framework or systems pattern.

Loop:
1. extract core abstraction
2. list reusable workflow elements
3. identify OpenClaw-native equivalents
4. draft skill
5. validate / refine

### Pattern 2: code optimization search
Use when the user wants a better implementation, not just a working one.

Loop:
1. baseline implementation
2. multiple optimization branches
3. benchmark each branch
4. consolidate best ideas
5. rerun with redirected search if plateaued

### Pattern 3: research discovery
Use when exploring a topic with multiple candidate hypotheses.

Loop:
1. collect candidate directions
2. assign separate exploration threads
3. write shared notes
4. periodically synthesize
5. spin out new sub-questions

## Safety and Guardrails

CORAL includes explicit safeguards. Keep those principles here too:

1. **Isolate risky actions**
   - destructive commands require confirmation
   - do not let exploration overwrite important files casually

2. **Protect the evaluator**
   - do not let the proposing agent define the benchmark unchecked
   - preserve an independent validation path

3. **Manage resources**
   - do not spawn agents endlessly
   - prefer a small number of differentiated explorers

4. **Avoid runaway loops**
   - every discovery loop needs stop criteria or a checkpoint cadence

5. **Write before you forget**
   - memory not written is memory lost

## Deliverables

A CORAL-style task should usually produce some combination of:
- a best current candidate
- a log of explored directions
- reusable notes
- a distilled workflow
- optionally a new skill draft

## Minimal Template For Real Use

When starting a CORAL-style task, create a file like this:

```markdown
# <topic> discovery log

## Objective
- 

## Success metric
- 

## Constraints
- 

## Candidate directions
- 
- 
- 

## Attempts
### Attempt 1
- Hypothesis:
- Action:
- Result:
- Reuse:

## Stable insights
- 

## Dead ends
- 

## Next move
- 
```

## Examples

### Example 1: create a skill from a paper

User request:
- “基于这篇论文创建一个 skill”

Apply this skill by:
- extracting the paper’s reusable operational pattern
- mapping it to OpenClaw tools and workflows
- drafting a skill instead of summarizing only the paper

### Example 2: improve an optimization task over time

User request:
- “继续优化这个算法，看看还能不能更好”

Apply this skill by:
- creating a discovery log
- spawning 2–3 distinct exploration threads
- separating candidate generation from benchmarking
- adding a reflection checkpoint after each batch

## Notes

The most important takeaway from CORAL is not “always use many agents.”

It is:
- **externalize knowledge**
- **explore asynchronously when diversity helps**
- **reflect periodically**
- **redirect when stalled**
- **turn repeated success patterns into reusable skills**
