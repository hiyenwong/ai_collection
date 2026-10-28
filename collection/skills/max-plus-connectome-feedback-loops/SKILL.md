---
name: max-plus-connectome-feedback-loops
description: Use for max-plus spectral routing analysis of connectomes.
category: ai_collection
trigger: max-plus algebra connectome, tropical spectral analysis neural networks, critical cycles feedback loops, routing vs diffusion brain communication, C. elegans multilayer connectome, maximum cycle mean eigenvalue
---

# Max-Plus (Tropical) Spectral Analysis of Connectomes: Dominant Feedback Loops

Source: Reyner-Fuentes, Rudolph, Peláez-Moreno, Valverde-Albacete, "Every route counts, but some count more: a max-plus view of the C. elegans brain", arXiv:2610.37587 (q-bio.NC, cs.NE, math.SP, Oct 2026). Code: github.com/emmareyner/Maxplus_eigenstructure_for_neuraldata (accepts user-provided connectivity matrices).

## When to use

- Extracting the DOMINANT weighted feedback circuits (critical cycles) from a weighted directed connectome, instead of diffusive summaries (linear spectra, centrality, community detection) that sum over all walks.
- Deciding whether a network question is routing-like (which routes dominate, thresholding, input competition, gating) rather than diffusion-like — then the right algebra is max-plus, and states live in LATTICES (order/inclusion), not Euclidean spaces.
- Composing multilayer functional connectomes (electrical / chemical-synaptic / monoaminergic / neuropeptidergic / hormonal) with time-varying engagement gates; analyzing how internal brain states reconfigure as gates switch.
- Any weighted neuronal network where you want: which closed routes dominate, what their max mean weight is, and which upstream/downstream domains they organize.

## Core method

1. **Max-plus semifield R_max,+**: a⊕b = max(a,b); a⊗b = a+b. Completed semifield: bottom ⊥=−∞ (⊕-neutral), unit e=0 (⊗-neutral), top ⊤=+∞. ⚠ Embedding rule: absent edge = ⊥; a numerical zero weight or negative response IS a finite edge (e=0 is not nothing). Min-plus dual (a⊕̇b=min) for inverse questions; the two are exchanged by sign flip (strongest-route on weights = shortest-route on costs).
2. **Routing state update**: x_i(t+1) = max_j [A_ij(t) + x_j(t)] — each neuron takes the largest gated incoming contribution; A_ij = weight of influence from neuron j to i (row = postsynaptic). Walks accumulate weight additively along connections while competing routes are MAXed: (A⊗̇^k)_ij = best accumulated weight among length-k walks j→i; Kleene star A⊛ collects best walks of any length.
3. **Layer composition (functional connectome model)**: A_ij(t) = max_ℓ [α_ℓ(t) + A_ij^(ℓ)] over layers ℓ ∈ {G gap junctions, S chemical synapses, M monoamines, N neuropeptides, H hormonal}. Gates α_ℓ(t) follow each mechanism's kinetics (electrical = stable scaffold α_G≡e; synaptic = fast; monoaminergic/neuropeptidergic/hormonal = seconds to minutes+). Three structural consequences: (a) engaging a layer can MERGE recurrent groups, never split them (graph = union of engaged layer graphs); (b) critical cycles depend ONLY on relative engagement α_ℓ−α_m (uniform shift moves all cycle means equally); (c) signaling kinetics set the time course of dominance reorganization → candidate mechanism for internal-state maintenance and roaming/dwelling-type transitions.
4. **Spectral machinery (reducible theory)**: (i) SCC decomposition → condensation DAG (where recurrence is structurally possible); (ii) per irreducible block, eigenvalue λ = maximum cycle mean max_c w(c)/ℓ(c) (Karp); cycles attaining it = critical cycles, their SCCs = critical classes; (iii) fundamental eigenvectors: columns of (λ^(−1)⊗̇A)⊛ indexed by one critical node per class; (iv) for reducible matrices solve each block and propagate through the condensation graph. Eigenvector semantics: RIGHT = downstream domain (reachable FROM the critical class), LEFT = upstream domain (can reach the critical class); ⊥ = structurally cut off; ⊤ = dominated by a recurrent component with LARGER eigenvalue (hierarchy between recurrent regimes, NOT unbounded activity).
5. **Reading λ**: max mean weight per step around the best closed route, in the units of the dataset (EM contact sections, supported ligand–receptor counts, mean calcium-response amplitude). Only differences between finite eigenvector coordinates are meaningful (one propagation step = common shift λ).

## C. elegans results (five layers, 302 neurons)

| Layer | Recurrent structure | λ (finite modes) | Critical class | Units / interpretation |
|---|---|---|---|---|
| Gap junctions (Cook et al.) | ONE 296/302 SCC (symmetric → left=right) | 401; 1 | {ALA, CANL, CANR} via reciprocal pairs ALA↔CANL, ALA↔CANR; isolated IL2DL↔URADL | EM serial sections — exceptionally extensive recurrent electrical contact |
| Chemical synapses | 11 SCCs, bow-tie: SCC7 somatic n=275, SCC9 pharyngeal n=18; M1→RIPL is the UNIQUE chemical bridge pharynx→soma | 37; 15 | {RIAR, SMDVL} reciprocal loop (43+31)/2 — known sensorimotor steering feedback; M4 self-loop (isthmus peristalsis motor neuron) | EM serial sections |
| Monoaminergic | 286 SCCs, divergent: 17-neuron core SCC268 broadcasts to 267 downstream SCCs (ADF/NSM/HSN serotonergic, CEP/PDE dopaminergic, RIM tyraminergic, RIC octopaminergic, +I5) | 2.5 | {NSML, NSMR, RIML, RIMR} | supported transmitter–receptor relations |
| Neuropeptidergic | 286/302 in ONE SCC | 14 | PQR self-loop = 14 distinct autocrine ligand–receptor routes (oxygen-sensing neuron, known high autocrine diversity) | supported peptide–receptor relations |
| Functional (Randi et al. atlas) | 147/188 in main SCC, 11 upstream + 19 downstream singletons | 0.921569 | {RIH, SIBVR}: 0.973749 + 0.869389 (mean) — serotonin-uptake regulator coupled to sublateral cholinergic motor neuron | mean post-stimulus calcium-response amplitude |

- Cross-layer motif: ALA–CAN pairing is the strongest recurrent electrical structure AND ALA's only chemical outputs — unresolved physiology, flagged for study.
- ⊤ semantics in action: for the λ=15 pharyngeal mode, the 280 somatic neurons take ⊤ because through M1→RIPL they reach a component whose loops grow 37/step > 15/step.

## Why not linear spectra

- Linear eigenproblem sums ALL walks (diffusion): leading mode = hub-dominated, 100+ eigenvalues exceed 10% of the spectral radius in the synaptic/functional networks (uninterpretable), spectral radius 1.5–26× the max-plus eigenvalues, remaining modes mix many neurons in signed/complex coordinates.
- Max-plus returns 1–2 finite modes per layer, each attached to NAMED neurons with biological meaning preserved, plus explicit upstream/downstream domains.
- Agrees with linear tools on coarse structure (top centrality ALA/CANL/CANR in gap junctions; RIAR top-6 in synaptic; pharynx/soma spectral-clustering split) — but adds which specific closed routes dominate.
- Community detection / rich-club analyses are usually undirected + unweighted + layer-merged: they see segregation, not ordered recurrence.

## Implementation notes

- Reducible max-plus spectral theory from Butkovič/theory in ref [24]: solve each irreducible diagonal block (Karp max-cycle-mean), propagate through condensation DAG, assemble fundamental eigenvectors with ⊥/⊤ completion.
- Weight comparability: only layers on a COMMON scale may be composed into A(t) (the empirical workaround is per-layer analysis; hormonal layer is model-only, no neuron-to-neuron map yet).
- The Randi signal-propagation atlas is NOT another layer — it is an experimental observation of the composite operator under specific conditions (includes polysynaptic/extrasynaptic effects).

## Pitfalls

- ⊤ coordinates are hierarchy markers between recurrent regimes (larger-λ component dominates under repeated propagation), not predictions of divergence.
- Uniform gate shifts are invisible to critical structure (only relative engagement matters) — when fitting α_ℓ(t), fix one gauge (e.g. α_G = 0).
- Directly maxing raw matrices across layers is only meaningful if weights share units; anatomical contact counts and calcium amplitudes do NOT.
- A terminal SCC in the condensation graph may reflect missing edges to non-neuronal targets (muscle, marginal cells: MCL/MCR, DD4/DD5) — not true network sinks in vivo.

## Related

- Routing-vs-diffusion taxonomy of network communication models (Fornito et al.); max-plus algebra of scheduling/discrete-event systems (Butkovič, Baccelli et al.).
- Patel preprint: max-plus threshold-timing simulation on a single C. elegans wiring diagram — this skill analyzes the SPECTRAL structure of each connectivity layer separately instead.
- Companion dynamics paper [26] (same group): max-plus/min-plus neural state-space modeling.
- Contrast skills: connectome-wiring-statistics-control, boundary-preserving-null-connectome (statistical controls), effective-connectivity causal-kernel (GP CaKe) — this skill is the routing-side alternative for directed weighted recurrence.
