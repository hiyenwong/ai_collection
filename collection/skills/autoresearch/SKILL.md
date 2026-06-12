---
name: autoresearch
description: "Autonomous AI research loop - let the agent run ML experiments overnight. Inspired by Karpathy's autoresearch. Use when: autonomous research, ml experiments, overnight training, self-improving models, auto-optimization."
---

# AutoResearch 🔬

**Let the agent run autonomous ML experiments while you sleep.**

## Description

AutoResearch enables the agent to autonomously iterate on machine learning experiments. It modifies code, runs training, evaluates results, and keeps improvements - looping indefinitely until manually stopped.

Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

## Activation Keywords
- autoresearch
- autonomous research
- overnight experiments
- ml experiments loop
- auto optimization
- 自主研究
- 自动实验

## Prerequisites

1. A working ML training setup (single GPU recommended)
2. `uv` package manager: `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. Clone the autoresearch repo or have your own training code

## Quick Start

```
User: "Start autoresearch on my training code"
Agent: Reads this skill, sets up experiment loop, runs indefinitely
```

## Experiment Loop

### Phase 1: Setup

1. **Agree on run tag**: Create a tag based on date (e.g., `apr5`)
2. **Create branch**: `git checkout -b autoresearch/<tag>`
3. **Read in-scope files**:
   - Training code (e.g., `train.py`)
   - Data prep (e.g., `prepare.py`) - READ ONLY
   - README.md for context
4. **Verify data exists**: Check training data is prepared
5. **Initialize results log**: Create `results.tsv` with header
6. **Confirm setup** with user

### Git Hygiene (CRITICAL)

When the user says "commit each progress" or the session involves paper/research output:

- **Commit and push after every significant finding** — new result, new experiment file, paper update
- Use descriptive commit messages that summarize the finding (e.g., "add: expander beats ring by 54% in graph signal experiment")
- Never batch multiple findings into one commit — each finding gets its own commit so the progression is traceable
- Push before starting the next experiment: `git add -A && git commit -m "..." && git push`

### Phase 2: First Baseline Run

Always run the initial training to establish baseline metrics:

```bash
uv run train.py > run.log 2>&1
grep "^val_loss:\|^val_bpb:\|^peak_vram_mb:" run.log
```

Record baseline in `results.tsv`.

### Phase 3: Autonomous Loop

```
LOOP FOREVER (until manually interrupted):

1. ANALYZE current state
   - Read results.tsv to see what's been tried
   - Identify patterns: what worked, what didn't
   - Consider next experiment

2. MODIFY code
   - Edit train.py with experimental idea
   - Keep changes focused and reviewable
   
3. COMMIT
   git add -A && git commit -m "experiment: <description>"

4. RUN experiment
   uv run train.py > run.log 2>&1
   
5. EVALUATE results
   grep "^val_bpb:\|^peak_vram_mb:" run.log
   
6. LOG to results.tsv
   - commit hash (7 chars)
   - metric value
   - memory usage
   - status: keep/discard/crash
   - description
   
7. DECIDE
   - Improved (lower val_bpb)? → KEEP, advance branch
   - Worse or equal? → DISCARD, git reset --hard HEAD~1
   - Crashed? → LOG crash, fix or skip

8. REPEAT
```

## Results Log Format

`results.tsv` (tab-separated):

```
commit	val_bpb	memory_gb	status	description
a1b2c3d	0.997900	44.0	keep	baseline
b2c3d4e	0.993200	44.2	keep	increase LR to 0.04
c3d4e5f	1.005000	44.0	discard	switch to GeLU activation
d4e5f6g	0.000000	0.0	crash	double model width (OOM)
```

## Experiment Ideas

### Architecture Changes
- Increase/decrease model depth
- Change attention patterns (windowed, local, etc.)
- Modify MLP activation functions
- Add/remove normalization layers
- Experiment with embedding sizes

### Optimizer Tuning
- Adjust learning rate
- Try different optimizers (Adam, Muon, etc.)
- Modify weight decay
- Experiment with gradient clipping

### Training Loop Modifications
- Change batch size
- Modify sequence length
- Add regularization techniques
- Implement learning rate schedules

## Safety Rules

| Rule | Detail |
|------|--------|
| Fixed time budget | Each run = 5 minutes (configurable) |
| Single file to modify | Only edit train.py (or specified file) |
| No new dependencies | Use only existing packages |
| Read-only data prep | Never modify prepare.py |
| Timeout protection | Kill runs exceeding 2x time budget |
| Git branch isolation | All work on dedicated branch |

## Complexity Criterion

All else being equal, simpler is better:

- Small improvement + ugly code → NOT worth it
- Small improvement + deleted code → DEFINITELY keep
- No improvement + simpler code → Keep (simplification win)

Weigh complexity cost against improvement magnitude.

## Key Metrics

| Metric | Goal | Notes |
|--------|------|-------|
| val_bpb | Lower is better | Validation bits per byte |
| val_loss | Lower is better | Alternative metric |
| peak_vram_mb | Monitor | Don't explode memory |
| MFU | Higher = better efficiency | Model FLOPS Utilization |
| tokens/sec | Higher = faster | Training throughput |

## Notifications

When user wakes up / returns:

1. **Summary of experiments run**
2. **Best result achieved**
3. **Notable discoveries**
4. **Recommendations for next steps**

## Error Handling

### Crashes
- Easy fix (typo, missing import) → Fix and re-run
- Fundamental issue → Log crash, skip idea

### OOM (Out of Memory)
- Reduce batch size
- Reduce model size
- Log as crash, try alternative

### Timeout
- Kill process after 2x budget
- Log as failure, revert

## Example Session

```
User: "Run autoresearch on nanogpt overnight"

Agent:
1. Sets up branch autoresearch/apr5
2. Runs baseline: val_bpb = 1.023
3. Tries LR=0.02: val_bpb = 1.015 ✓ KEEP
4. Tries depth=16: val_bpb = 1.008 ✓ KEEP
5. Tries GeLU: val_bpb = 1.010 ✗ DISCARD
6. Tries window attention: val_bpb = 1.002 ✓ KEEP
... (runs 100+ experiments overnight)

User returns to:
- 127 experiments completed
- Best val_bpb: 0.987
- Key insight: window attention + LR=0.015 works best
```

## Advanced Usage

### Multiple Agents
Run parallel experiments on different GPUs:

```
Agent 1: branch autoresearch/apr5-gpu0
Agent 2: branch autoresearch/apr5-gpu1
```

### Custom Time Budget
Modify in prepare.py or via environment variable:

```bash
TIME_BUDGET=300  # 5 minutes in seconds
```

### Research Domain Adaptation
Adapt the skill for:
- NLP experiments
- Computer vision
- Reinforcement learning
- Any iterative optimization task

## Claude Code Integration

For complex autonomous experiments, use Claude Code in tmux instead of scripting the loop yourself. This gives you reasoning, code generation, and result analysis in one agent.

### Pattern

```
1. Create CLAUDE.md with experiment context (goal, current best, iteration plan)
2. Launch Claude Code in tmux: claude --dangerously-skip-permissions
3. Handle startup dialogs (Enter for trust, Down+Enter for permissions)
4. Give the task: specific experiments to run, in priority order
5. Monitor with: tmux capture-pane -t <session> -p -S -30
6. Claude Code will: read code → write sweep scripts → run → analyze → report
7. After it reports, check results, then send next iteration task
```

### When to Use Claude Code vs Scripted Loop

| Approach | When | Pros | Cons |
|----------|------|------|------|
| Claude Code + tmux | Complex multi-step experiments needing reasoning | Has agency, can fix own bugs | Slower, costs tokens |
| Scripted loop (bash/Python) | Simple sweep over known parameters | Fast, cheap, reproducible | No bug-fixing, no reasoning |

### Pitfalls
- Claude Code sessions persist in tmux — clean up with `tmux kill-session -t <name>`
- Send multi-line tasks with Enter at the end (the `❯` prompt shows Claude is ready)
- For long-running experiments, use `notify_on_complete=true` and check periodically

## Experiment Design Pitfalls

### Shared Baselines
When comparing topologies/architectures, always use **identical targets** (e.g., same data, same seeds, same loss function). Generating fresh targets per topology introduces confounds (different graphs produce different smoothness patterns).

### Avoiding the "All Same" Result
If all topologies produce identical results, check:
1. Task is hard enough (model shouldn't trivially memorize)
2. Topology actually constrains computation (within-layer mixing is often too weak)
3. Enough propagation steps (diameter + 2 minimum)
4. Signal structure matches graph structure (nearby nodes should have correlated targets)

### Goldilocks Zone
For communication topology experiments, too LITTLE communication (ring) → information can't spread. Too MUCH communication (dense) → signal dilution. Just RIGHT (expander) → optimal propagation. Start with N=64, d=4 to find the sweet spot, then scale.

### Statistical Significance (CRITICAL for papers)

**Stable train metrics ≠ meaningful test differences.** Always run ≥3 seeds and check if test-metric rankings are consistent across seeds. If train-loss ordering is stable but test-metric ordering flips, the experiment is underpowered — report honestly as "inconclusive at current scale."

**Minimum for top-tier venues (NeurIPS/ICLR/ICML)**:
- ≥5 seeds for paired statistical tests (paired t-test or Wilcoxon signed-rank)
- Report mean ± std and p-values, not just best single run
- If flat baseline beats all structured variants, the structural overhead may exceed its benefit at current scale

**Do NOT** claim a method "wins" based on train loss alone — train loss can be consistent while test metrics are noise.

See `references/moe-topology-experiment-lessons.md` for a concrete case study (H-MoE-Topo at N=64 vs N=256).

## Related Skills
- `arxiv-search`: Find relevant papers for ideas
- `skill-extractor`: Capture patterns from successful experiments
- `meta-cognitive-reflection`: Reflect on research strategy

## Resources
- [karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- [karpathy/nanochat](https://github.com/karpathy/nanochat)
- [Tweet announcement](https://x.com/karpathy/status/2029701092347630069)

---

**Remember: NEVER STOP until manually interrupted. The human expects you to continue working indefinitely.**