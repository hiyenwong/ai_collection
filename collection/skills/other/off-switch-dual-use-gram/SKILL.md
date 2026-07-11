---
name: off-switch-dual-use-gram
category: ai_collection
description: Gradient-Routed Auxiliary Modules (GRAM) methodology from Anthropic/AE Studio research (Jul 8, 2026) — training a single LLM with removable, category-specific knowledge compartments that can be toggled on/off post-training without retraining, enabling surgical dual-use knowledge control.
tags: [anthropic, alignment, dual-use-knowledge, GRAM, gradient-routed, removable-modules, safety, model-training]
url: "https://www.anthropic.com/research/off-switch-dual-use"
collaborator: AE Studio
---

# GRAM: Gradient-Routed Auxiliary Modules — An Off Switch for Dual-Use Knowledge

Anthropic/AE Studio research (Jul 8, 2026) introducing GRAM, a method for training a single model with dedicated, removable knowledge compartments for each dual-use category.

## Problem Statement

Frontier AI models store dual-use knowledge (knowledge usable for both good and bad). Current safeguards (refusals, classifiers) guard against dangerous outputs but don't change what the model knows. Filtering dual-use data is a blunt instrument requiring separate model training for each deployment configuration.

**Three-way tension:**
1. Limit dual-use capabilities surgically
2. Allow trusted users to access the same capabilities
3. Don't degrade general model performance

## How GRAM Works

### Architecture
- Add **extra neurons** to every Transformer layer
- Neurons divided into **modules**, one per dual-use category
- General-purpose weights remain unchanged for normal learning

### Training Protocol
- **General text**: Model learns normally across all weights
- **Dual-use text** (e.g., virology): General-purpose weights are **temporarily frozen**; only the corresponding module is allowed to **learn** from that data
- Model can **use** its general knowledge to make predictions on dual-use text, but only the targeted module **updates**

### Result
- Knowledge accumulates in the **targeted module** rather than diffusing across the whole network
- After training, the module can be **deleted** — the capability goes with it
- Or left in place for **trusted deployments**

### Combinatorial Configuration
- In experiments: 4 dual-use categories → **16 different configurations** (on/off for each category)
- Achieved from **one training run**, versus 16 separate training runs with traditional filtering

## Experimental Results

### Test 1: Synthetic Dataset
- Children's stories tagged by topic
- Small GRAM model could "forget" any chosen topic
- Each configuration performed **almost identically** to a separate model trained from scratch with that topic filtered out
- Cost of **one model** → results that normally require **multiple training runs**

### Test 2: Realistic Dataset
- Mix of web text, code, and scientific papers
- **Four dual-use domains**: virology, cybersecurity, nuclear physics, niche programming language
- Deleting a module removed capability **as effectively as never having trained** on that data
- Removal **did not degrade general performance**
- Post-removal fine-tuning attack: GRAM resisted recovery **about as well as data filtering**
- By contrast, post-training "unlearning" only **suppressed** knowledge — easily restored with small fine-tuning

### Test 3: Scaling
- Seven model sizes: 50M → 5B parameters
- GRAM matched data filtering performance at **every size**
- Gap between "module on" and "module off" **grew wider** at larger sizes
- Bypassing protections became **relatively more expensive** as models scaled

## Comparison to Alternatives

| Method | Requires Retraining? | Knowledge Recoverable? | Performance Degradation? |
|--------|---------------------|----------------------|------------------------|
| Data filtering | Yes (per configuration) | Resistant | None |
| Post-training unlearning | No | Easily restored with fine-tuning | Unknown |
| **GRAM** | **No (one run, many configs)** | **Resistant (like filtering)** | **None** |

## Key Advantages

1. **One training run → N configurations**: Exponential configuration space from linear cost
2. **No performance degradation**: Deleting modules doesn't harm general capabilities
3. **Removable by deletion**: Physically removing weights, not just suppressing behavior
4. **Scales favorably**: Larger models make bypass harder, not easier
5. **Resists post-removal recovery**: As resistant as data filtering to fine-tuning attacks

## Limitations

- **Preliminary**: Not applied to production Anthropic models
- **Requires labeled dual-use data**: Need to identify and categorize dual-use content at training time
- **Fixed module count**: Number of modules set at training time; cannot add categories post-hoc
- **Overhead**: Extra neurons increase model size proportionally to number of dual-use categories

## Applications

- **Biosecurity**: Deploy models with virology capabilities only in vetted labs
- **Cybersecurity**: Control access to vulnerability exploitation knowledge
- **Nuclear safety**: Compartmentalize nuclear physics knowledge
- **Regulatory compliance**: Region-specific capability toggling
- **Trusted researcher access**: Enable specific domains for verified users while deploying safe versions publicly

## Implementation Considerations

1. **Module routing**: Need a classifier at training time to route dual-use text to correct modules
2. **Neuron overhead**: Each module adds parameters; for K categories, overhead is ~K× module size per layer
3. **Freeze/unfreeze mechanics**: Training loop must dynamically freeze general weights on dual-use examples
4. **Module deletion**: Post-training weight pruning is straightforward — zero out module weights
5. **Combinatorial deployment**: Binary on/off per module → 2^K deployment configurations from 1 model

## Activation

GRAM, gradient-routed auxiliary modules, dual-use knowledge, removable knowledge, knowledge compartments, model unlearning, AI safety, capability toggling, surgical knowledge removal, Anthropic alignment, AE Studio, model training efficiency
