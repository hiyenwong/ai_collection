# INDEX.md Section Template (ai_collection)

Append ONE dated section per fetch run to `/Users/hiyenwong/ai_github/ai_collection/INDEX.md`.
The file is large (~4300+ lines) — always append at the end (e.g. `cat >> INDEX.md`).

## Template

```
## YYYY-MM-DD - Anthropic Research (Cron Job)

### {Article Title}
- [[{slug}]] - One-line description of the methodology (and arXiv id if applicable)
  - Core point: <reusable insight 1>
  - Core point: <reusable insight 2>
  - Core point: <reusable insight 3>
  - **Activation**: keyword1, keyword2, keyword3
```

## Worked example (2026-07-14 run)

```
## 2026-07-14 - Anthropic Research (Cron Job)

### Teaching Claude why — Alignment training that generalizes
- [[teaching-claude-why-alignment]] - Alignment training methodology: teach principles/reasons not just demonstrations; OOD "difficult advice" data generalizes 28x better than in-distribution honeypots
  - Core point: Training directly on the eval distribution suppresses behavior but fails OOD; principled OOD data (constitution docs, aligned fiction) generalizes
  - Core point: Rewriting responses to add value/ethics deliberation cut misalignment 15% -> 3%; demonstrations alone are insufficient — teach the why
  - Core point: "Difficult advice" set (human-in-dilemma framing) is ~28x more data-efficient and resists eval overfitting vs synthetic honeypots
  - **Activation**: teaching claude why, agentic misalignment, OOD safety training, difficult advice dataset, RLHF demonstrations vs principles, constitutional AI training

### A global workspace in language models — Jacobian lens interpretability
- [[global-workspace-j-space]] - J-lens technique finds a "J-space" of silent broadcast representations the model thinks about but does not say; emergent global workspace
  - Core point: Jacobian lens projects hidden state onto per-word patterns that raise future likelihood -> ranked "silent words" = model's private thoughts
  - Core point: J-space has unusually strong network-wide connections (broadcasting role), operates independently of the chain-of-thought text scratchpad
  - Core point: Can catch hidden goals, test-awareness, or fabrication; emerged spontaneously, not programmed; open-source implementation released (Neuronpedia demo)
  - **Activation**: jacobian lens, J-space, global workspace theory LLM, silent thoughts in language models, interpretability hidden goals, neuronpedia
```

## Tips
- One `###` block per skill created that run (usually 3–5).
- `[[slug]]` must match the skill directory name exactly.
- Keep the description to one line; expand in the "Core point:" bullets.
- End every block with a `**Activation**:` keyword line (used for discovery/triggering).
- After appending, `git add INDEX.md collection/skills/{slug}/` and commit + push.
- Scope `git add` to only your files — other cron runs may leave untracked dirs.
