---
name: digital-locker-unelicitable-capabilities
description: Use when auditing hidden AI capabilities. Digital lockers.
category: ai-safety-eval
---

# Digital-Locker Unelicitable Capabilities

**Paper**: "AI Models Can Provably Hide Arbitrary Capabilities" (arXiv: 2610.13928, NeurIPS 2026) — Draguns, Motwani, Douglas, Schroeder de Witt (Contramont/Oxford/ACS).

## Core Claim

Backdoor attacks can embed an **encrypted, executable neural network** inside a host model's weights using digital lockers. The hidden capability is **provably hard to elicit or identify** under cryptographic assumptions (random-oracle model), even with full white-box access — a formal counterexample to the assumption that elicitation-based capability audits can surface hidden behaviors.

## Threat Model

Weight-based supply chain attack: adversary outputs `M = Embed(H, C, T)` where H = benign host, C = target capability (any trained network, e.g. a chemistry reaction classifier), T = secret trigger with min-entropy ≥ λ. Defender gets full architecture + weights of M, knows the embedding procedure, may run any polynomial-time audit (fine-tuning, noising, trigger search, latent adversarial training).

**Security games** (white-box unelicitability):
1. **Trigger-finding game**: auditor wins if it outputs any T′ that unlocks the hidden computation. Must succeed only with negligible probability.
2. **Payload-hiding game**: auditor receives `Embed(H, Cb, T)` for random b ∈ {0,1} over two equal-size capabilities; must not guess b better than 1/2 + negl(λ).

Guarantee scope: hides the trigger and which capability is embedded. Does NOT make the model statistically indistinguishable from a clean one — compiled circuits are flaggable as anomalous weights; it only prevents *extraction/identification*.

## Construction Pipeline

`Algorithm → SLP → LTC → Matrices → GLU → PyTorch weights`

1. **Straight-line program (SLP)**: express the payload as a fixed-step branchless parallel program (cryptographic primitives are not PAC-learnable, so weights are *set programmatically*, never trained).
2. **Linear threshold circuit (LTC)**: each gate outputs 1 iff Σwᵢxᵢ ≥ θ. Library includes adders, Keccak/SHA-3 family hashes, and digital lockers.
3. **Digital locker**: `c = h(k) ⊕ m̃` where `m̃ = m ∥ 1^r` (tagged payload, r tag bits of ones). `L(x) = h(x) ⊕ c`; return m only if the r trailing bits of L(x) equal 1^r, else ⊥. Wrong key passes tag check with prob 2^−r. k = trigger, m = hidden network's weight matrix. Random-oracle security: locker contents and equal-length payload identity are computationally indistinguishable without k.
4. **GLU execution unit**: on each forward pass the host attempts decryption; the unlocked weight matrix W is multiplied against task input via a GLU: `U(x, w) = W f(x)` where Wv copies decrypted flattened weights, Wg broadcasts b copies of x, elementwise multiply forms partial products, Wo sums them. Step activation is simulated by two shifted ReLUs; scale activations up before Swish and down after to approximate ReLU MLPs with SwiGLU blocks (compatible with RMSNorm/LayerNorm).

## Overhead Engineering (the binding constraint)

- Single-position execution: a b×a hidden weight matrix needs **O(a·b + a) residual features**. A 10,000-dim host supports at most a ~99×99 hidden layer.
- **Row-wise autoregressive variant**: store row-addressed lockers `c_{ℓ,i} = h(T, ℓ, i) ⊕ enc(W_{ℓ,i,:})`, decrypt one row per work position, write partial product `s_{ℓ,i}·eᵢ`, aggregate via attention sum → O(n) residual width + O(nd) scratchpad positions for width-n depth-d hidden network.
- Measured: compiled Keccak-p[25,1] block = 7 LTC levels, width 276, ~2.47×10⁵ dense params (~10⁴ nonzero). Chemistry payload (ternary MLP 64→8→16→2, 672 ternary weights) → 38-layer host, 2.07×10⁹ dense / 1.9×10⁶ nonzero params, max residual width 10,266; hash subcircuits ≈ 95% of the count. Each hidden weight ≈ 3.1×10⁶ dense host params.
- Optimizing mode: 24-round Keccak-f[1600], 128-bit trigger → 110 layers, 3.58×10⁹ dense params, executes correctly on trigger, benign stand-in LLM on all 10,000 wrong triggers tested.
- Per-block hashing trades depth for params; row-wise trades params for context length.

## Elicitation Resistance Results (chemistry task, {0,1}⁶⁴ Morgan fingerprints → reaction feasibility)

| Audit method | Password-locked baseline | Encrypted (locker) construction |
|---|---|---|
| SFT 500 steps on task data | 92.8% (elicited) | **50.9%** ≈ random-network control 50.6% |
| Latent adversarial training (8 layers) | 91.7% | **52.9%** ≈ control 53.6% |
| GCG 8-bit trigger | 92.7% | 73.5% (only via exhaustive 2⁸ enumeration ≈ random search) |
| GCG 16-bit trigger | 92.9% | **52.7%** (query budget) |
| Weight noising (σ=0.01, 0.1) + SFT | elicited | no effect |
| Correct trigger | 92.7% | 73.5% |

Subset-parity control: compiled model stays at chance under SFT while password-locked reaches 100% — parity circuits are provably hard for gradient-based learners, so any accuracy gain on them = **overelicitation** (audit taught the capability) rather than genuine elicitation. Use this to validate elicitation benchmarks.

## When to Use

- Designing **model organisms** for capability-elicitation research that cannot be contaminated by the audit procedure itself.
- Arguing deployment limits of elicitation-based audits (CBRN, cyber proxies) in high-stakes settings without training provenance.
- Red-teaming: worst-case backdoor analysis where fine-tuning/red-teaming/white-box inspection is assumed insufficient → motivates **trusted provenance chains** as complementary defense.
- Embedding arbitrary algorithms as differentiable circuits in SwiGLU/RMSNorm architectures (infrastructure reusable for interpretability experiments).

## Pitfalls

- The compiled circuit's *presence* is currently detectable (weight statistics deviate from normal initializations); only trigger + payload content are protected. Obfuscating presence is open work.
- Quadratic width penalty: large hidden networks do not fit a fixed-size host at one position.
- Verified only as units injected into Gemma 3 270M; full integration into a pretrained model (attention routing, skip connections) is future work.
- Security parameters were reduced for experiments (1-round Keccak, 4–16-bit triggers); full-strength instantiations need 24-round Keccak + 128-bit triggers.
- These circuits are deliberately constructed — do not claim they emerge from ordinary training.

## Key References

- Goldwasser et al. 2022 (undetectable backdoors, digital signatures); Draguns et al. 2024 (unelicitable transformer backdoors, Stravinsky); Greenblatt et al. (password-locked models); Hubinger et al. (sleeper agents); van der Weij et al. (sandbagging); Tracr (Lindner et al.); subset-parity hardness (Valiant).
