# Autonomous ML Research Loop with Claude Code + tmux

A pattern for running autonomous ML experiments where Claude Code iterates on experiments, fixes bugs, scales up, and updates a paper — all without manual intervention.

## When to Use

You have an ML experiment that requires:
- Multiple iterations (run → analyze → fix → re-run)
- Bug-finding and fixing during iteration
- Scale-up (increase N, seeds, parameters)
- Paper/documentation updates tied to results
- Git commits after each meaningful finding

## Setup

### 1. Write the Experiment Script

Create a standalone Python script that:
- Accepts a config dict (seed, N, G, topology, etc.)
- Runs training on MPS/GPU
- Saves results to a JSON file
- Prints progress during training

**Script structure:**
```python
if __name__ == "__main__":
    experiments = [
        {"name": "flat_N64_s42", "type": "flat", ...},
        {"name": "hier_ring_N64_G16_s42", "type": "hier", ...},
        {"name": "hier_expander_N64_G16_s42", "type": "hier", ...},
    ]
    results = [run_exp(c) for c in experiments]
    with open("results.json", 'w') as f:
        json.dump(results, f, indent=2)
```

### 2. Write a CLAUDE.md

Put a `CLAUDE.md` in the experiment directory that tells Claude Code:

```markdown
# Project Autoresearch

## Mission
[Clear one-sentence goal]

## Architecture
[Brief description]

## Iteration Plan
1. **Run 1** (seed=42, default params): Verify baseline
2. **Analyze**: Compare configurations
3. **Run 2-3** (seed=123, 456): Statistical replication
4. **If effect detected**: Scale up
5. **If no effect**: Fix bugs, tune hyperparameters

## Paper Update
After each significant finding, update `../paper.md`.

## Rules
- Always use MPS device
- Commit and push after every finding
- Save results to JSON
- Never delete existing results
```

### 3. Start Claude Code in tmux

```bash
tmux new-session -d -s my_experiment
tmux send-keys -t my_experiment \
  "cd /path/to/experiments && claude --dangerously-skip-permissions" Enter
```

### 4. Send the Initial Prompt

Use load-buffer + paste-buffer for multi-line prompts:

```bash
cat << 'PROMPT' > /tmp/prompt.txt
[Your instructions here]
PROMPT

tmux load-buffer -b mybuf /tmp/prompt.txt
sleep 0.5
tmux paste-buffer -b mybuf -t my_experiment
tmux send-keys -t my_experiment Enter
```

Note: `tmux send-keys` with heredoc or `while read line` loops often fail on special characters. Always use `load-buffer` + `paste-buffer` for complex multi-line prompts.

## Monitoring

### Check Progress
```bash
tmux capture-pane -t my_experiment -p -S -20
```

### Read Status Indicators
- `❯` at bottom = waiting for your input
- `●` / `✻` / `✽` = actively working
- `(ctrl+b ctrl+b to run in background)` = long shell command running

### Check Results Independently
```bash
cat experiments/results.json
```

## The Iteration Cycle

### Phase 1: First Run
Claude Code runs the experiment script and monitors output:
```bash
until [ $(wc -l < /path/to/output) -ge 50 ]; do sleep 2; done
```

### Phase 2: Analysis
Reads results JSON, compares configurations, identifies patterns.

### Phase 3: Bug Fix
**Common ML experiment bugs:**
1. **Dead gradient path**: States computed but never used in loss
2. **Weak conditioning**: State → gate projection 500x weaker than input → gate (use dot-product instead of scalar)
3. **Dead activations**: ReLU on near-zero values kills gradients in topology weights (use GELU + LayerNorm)
4. **Training/test inversion**: Train loss favors dense, test favors sparse (oversmoothing / regularization)

### Phase 4: Scale Up
Once effect detected, increase N and G:
- N=64, G=8: ring diam=4, expander diam=3 (gap too small)
- N=64, G=16: ring diam=8, expander diam=4 (detectable)
- N=256, G=32: ring diam=16, expander diam=5 (substantial)

### Phase 5: Multi-Seed Validation
Seeds 42, 123, 456. Calculate mean ± std per config.

### Phase 6: Paper Update
```bash
git add paper.md && git commit -m "add: Section X results"
git push origin main
```

## Key Pitfalls

1. **Don't use nohup/disown/&** — use `background=true` or let Claude manage shells
2. **JSON race condition** — don't read while experiment writes
3. **Clean up tmux** — `tmux kill-session -t <name>` when done
4. **Claude context degradation** — long sessions need `/compact`
5. **Seed both torch AND numpy** — `torch.manual_seed()` + `np.random.seed()`
6. **MPS check** — always `torch.backends.mps.is_available()`

## Template: Fix Prompt Structure

```
## CRITICAL FINDING: [result]

## ROOT CAUSE
[what went wrong]

## FIX REQUIRED
[step-by-step fix]

## IMPLEMENTATION
1. Edit script
2. Re-run
3. Analyze
4. Scale
5. Update paper

## Expected outcome
[what should happen with the fix]
```
