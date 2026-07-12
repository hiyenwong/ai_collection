# Neuroscience Cron 2026-06-11 NeuroPINNs Session

## Session Summary

**Date**: Thursday, June 11, 2026 (concurrent with bilinear-gating/hyperbolic-geometry session)
**Paper**: arXiv:2511.06081 - "NeuroPINNs: Neuroscience Inspired Physics Informed Neural Networks"
**Authors**: Shailesh Garg, Souvik Chakraborty
**Skill Created**: `neuropinns-spiking-pinn`
**Branch**: `neuro-cron-2026-06-11` (shared with concurrent session)

## Cross-Domain Discovery Pattern

**Paper classification**: Neuroscience methodology (Variable Spiking Neurons) + Computational Physics application (PDE solving)
- **Neuroscience keywords**: spiking neuron, variable spiking, neural dynamics
- **Physics keywords**: physics-informed neural network, PDE, differential equation, computational physics
- **Cross-domain signal**: Variable Spiking Neurons (VSN) as stochastic projection mechanism for PDE solving — neuroscience-inspired computational physics

This paper exemplifies the cross-domain value pattern: neuroscience methodology applied to non-neuroscience domains (computational physics, engineering). Similar to how quantum+finance papers bridge two domains, this bridges neuroscience+physics.

## Methodology Summary

**Core innovation**: Variable Spiking Neurons (VSN) with learnable scaling factors
- Each VSN has: threshold θ, scaling factor α, membrane potential
- Spiking condition: V(t) ≥ θ → spike, reset V → V - αθ
- **Upscaled theory**: When α → ∞ (continuum limit), VSN ensemble converges to stochastic projection operator

**Key theoretical contribution**:
- Stochastic projection method from upscaled theory
- Convergence proof: VSN network → stochastic function space
- Energy efficiency: SNN-style computation with physics-informed loss

**Applications validated**:
1. Poisson equation (2D)
2. Helmholtz equation (2D)
3. Advection-diffusion equation (2D)
4. Burgers' equation (2D)
5. 3D linear elastic micromechanics (Prismatic RVE)

**Performance metrics**:
- Relative error < 1% on all test cases
- Energy-efficient: spike-based computation vs dense forward pass
- Adaptive: learnable α parameters adjust projection strength

## Skill Architecture Decision

Created as standalone skill `neuropinns-spiking-pinn` (paper-specific entry), following current workflow pattern.

**Architecture note**: This follows the current pattern of paper-specific skills, but as documented in `neuroscience-cron-2026-06-11-complete-workflow.md`, future architecture should favor class-level umbrellas with references. This skill is complete and valuable, but represents a structural pattern that should evolve toward hierarchical organization.

## Workflow Execution

**Discovery method**: 
1. arXiv API query via `execute_code` + `requests` with proxy
2. Query: neuroscience + brain network + neural dynamics + spiking neural network keywords
3. Scoring: neuroscience keyword count in title + abstract

**Paper selection criteria**:
- Cross-domain signal (neuroscience + physics/engineering)
- Mathematical framework present (upscaled theory, stochastic projection)
- Practical applications validated (4 PDE problems + 3D mechanics)

**Skill creation**:
- SKILL.md: 12,532 bytes (comprehensive methodology documentation)
- Core sections: Overview, Variable Spiking Neurons theory, Physics-Informed framework, Applications, Pitfalls, Activation keywords

**Git workflow**:
```bash
cd /Users/hiyenwong/ai_github/ai_collection
git checkout neuro-cron-2026-06-11
git add collection/skills/neuropinns-spiking-pinn/ INDEX.md
git commit -m "feat: add neuropinns-spiking-pinn from arXiv 2511.06081"
git push origin neuro-cron-2026-06-11
```

**INDEX.md entry** (prepended at top):
```markdown
## 2026-06-11 - Neuroscience Research (Cron Job)

### NeuroPINNs: Neuroscience Inspired Physics Informed Neural Networks
- [[neuropinns-spiking-pinn]] - 变量脉冲神经元(VSN)结合物理信息神经网络高效求解PDE (arXiv: 2511.06081)
  - 变量脉冲神经元通过放缩理论实现随机投影
  - 验证于4个PDE问题+3D线性弹性微力学
  - **Activation**: variable spiking, physics-informed, PDE solving, stochastic projection, energy-efficient computation
```

## Obsidian Integration

**Note location**: `~/.hermes/obsidian_notes/2026-06-11-neuropinns-spiking-pinn.md`
**Size**: 3,415 bytes
**Format**: Research note with paper metadata, methodology summary, key findings, activation keywords

## Knowledge Graph Update

**kg.db path**: `/Users/hiyenwong/Library/Application Support/knowledge-graph/kg.db`

**Schema (2026-06-11 verified)**:
```sql
papers: (id INTEGER PK AUTOINCREMENT, arxiv_id TEXT UNIQUE, title TEXT, 
         authors TEXT, categories TEXT, submitted_date TEXT, doi TEXT,
         skill_name TEXT, skill_path TEXT, created_at TEXT, abstract TEXT)
```

**Insert executed**:
```sql
INSERT INTO papers 
(arxiv_id, title, authors, categories, submitted_date, skill_name, 
 skill_path, created_at, abstract)
VALUES 
('2511.06081', 'NeuroPINNs: Neuroscience Inspired Physics Informed Neural Networks',
 'Shailesh Garg, Souvik Chakraborty', 'cs.LG; cs.NE; physics.comp-ph',
 '2025-11-12', 'neuropinns-spiking-pinn',
 '/Users/hiyenwong/.hermes/skills/ai_collection/neuropinns-spiking-pinn/',
 datetime('now'), '{abstract text}');
```

**Verification query**:
```bash
sqlite3 kg.db "SELECT arxiv_id, title, skill_name FROM papers WHERE arxiv_id='2511.06081'"
# Output: 2511.06081|NeuroPINNs: Neuroscience Inspired Physics Informed Neural Networks|neuropinns-spiking-pinn
```

## Concurrent Session Pattern

This session ran concurrently with the bilinear-gating/hyperbolic-geometry session documented in `neuroscience-cron-2026-06-11-complete-workflow.md`.

**Pattern verified**:
- Multiple neuroscience cron jobs on same day → independent skills
- Shared git branch: `neuro-cron-2026-06-11`
- Sequential commits appended to branch
- Paper IDs differ → skills differ → no collision
- Targeted `git add collection/skills/neuropinns-spiking-pinn/` (not `-A`) avoids capturing sibling session files

## Lessons Learned

1. **Cross-domain discovery**: Neuroscience methodology applied to computational physics yields valuable skills — expand keyword scoring to include physics/engineering keywords when searching neuroscience papers
2. **Upscaled theory pattern**: Mathematical frameworks with continuum limits (α → ∞) and convergence proofs encode reusable theoretical patterns
3. **Energy-efficient computation**: Spike-based methods for physics problems — generalizes beyond neuroscience to computational physics
4. **Concurrent session safety**: Multiple cron jobs sharing branch with targeted git add — pattern stable across multiple sessions on 2026-06-11
5. **kg.db schema verification**: PRAGMA before INSERT — schema drifted multiple times, 2026-06-11 schema confirmed

## Related References

- [neuroscience-cron-2026-06-11-complete-workflow.md](neuroscience-cron-2026-06-11-complete-workflow.md) — concurrent session (bilinear-gating + hyperbolic-geometry)
- [kg-db-actual-schemas-2026-06-11.md](kg-db-actual-schemas-2026-06-11.md) — PRAGMA verification
- [neuroscience-cron-2026-06-10-bilinear-hyperbolic.md](neuroscience-cron-2026-06-10-bilinear-hyperbolic.md) — theoretical framework prioritization pattern