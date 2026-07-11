# Category Relevance Guide for Neuroscience Cron Jobs

## High-Priority Categories (check these first)
- **q-bio.NC** — Primary category. 3-5 new submissions/day. Saturation is common for hourly cron.
- **cs.LG** (cross-listed) — Many neuroscience + ML papers cross-list here.
- **q-bio.QM** — Quantitative methods, sometimes relevant for computational neuroscience.

## Medium-Priority (useful for cross-domain work)
- **cs.AI** — Agentic AI papers that might overlap with brain-inspired architectures.
- **stat.ME** — Statistical methodology papers sometimes have neuroscience applications.
- **physics.bio-ph** — Biophysics papers with neural computation angles.

## Low-Priority (mostly unrelated, skip unless cross-listed)
- **cs.NE** — Predominantly evolutionary computation (DE, GA, ES), swarm intelligence, molecular optimization. NOT spiking neural networks or brain networks. Only relevant when cross-listed with q-bio.NC.
- **cs.RO** — Robotics; occasionally SNN control papers but rare.

## Discovery Strategy
1. Start with `browser_navigate` to `https://arxiv.org/list/q-bio.NC/new`
2. Check cross-lists on cs.NE page: `https://arxiv.org/list/cs.NE/new` → "Cross-lists" tab
3. If all q-bio.NC papers have existing skills → domain saturation → validate sync → `[SILENT]`
4. Use `search_files(pattern='ARXIV_ID', path='~/.hermes/skills', target='content')` to check saturation before creating new skills

## Submission Volume Estimates (2026-06-29)
| Category | New/day | Relevance to neuro | Saturation risk |
|----------|---------|--------------------|--------------------|
| q-bio.NC | 3-5 | High | Very high for hourly cron |
| cs.NE | 8-12 | Low (< 10%) | Low (few to process) |
| cs.LG | 50+ | Medium (cross-lists) | Low |
| q-bio.QM | 2-4 | Medium | High |
