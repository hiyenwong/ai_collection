# Spatiotemporal TDANN — Paper Detail (arXiv:2605.11718)

**Authors**: Zhaotian Gu, Molan Li, Jie Su, Chang Liu, Tianyi Qian, Dahui Wang
**Published**: 2026-05-12 | **Categories**: q-bio.NC, cs.AI, cs.NE

## Spatial Loss Formula

$$L_{spatial,k} = \frac{1 - \text{corr}(r_k, D_k)}{2}$$

- `r_k` = pairwise unit activation correlations
- `D_k` = inverse physical distance vector on simulated 2D cortical sheet
- `D_i = 1 / (d_i + 1)` where `d_i` is pairwise distance

Total: `L_total = L_contrast + α * Σ_k L_spatial,k`

## MoCo Contrastive Loss

$$L_{contrast} = -\log \frac{\exp(q \cdot k^+ / \tau)}{\exp(q \cdot k^+ / \tau) + \sum_{i=1}^{K} \exp(q \cdot k_i^- / \tau)}$$

- `q` = query embedding, `k⁺` = positive key (temporally-augmented clips from same video)
- `kᵢ⁻` = negative samples from momentum queue
- `τ` = temperature parameter

## Why 3D ResNet for Biological Mapping

3D CNNs have activations with both spatial and temporal dimensions. When mapping to cortical sheet, **average over time** to simulate neural firing rates — only spatial information is used for topography analysis.

## Key Mechanistic Insight

The competition between task-driven discriminative pressure and biophysical spatial constraints serves as a **universal mechanism** shaping both individual neural tuning and global map topography. This unifies ventral and dorsal stream computational origins.

## Limitations (from paper)

- Lacks temporal recurrence and top-down feedback prevalent in biological brains
- Future: incorporate ConvRNNs, SNNs, or predictive coding
- Needs validation with electrophysiological data during active behavioral tasks
