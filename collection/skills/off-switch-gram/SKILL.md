---
name: off-switch-gram
description: GRAM (Gradient-Routed Auxiliary Modules) methodology for containing dual-use knowledge in removable, compartmentalized weight modules — enabling surgical knowledge removal without degrading general performance.
category: ai_collection
trigger_words: gram, gradient-routed, auxiliary modules, dual-use, knowledge containment, removable weights, surgical filtering, knowledge removal, model safety
date: 2026-07-13
source: "Anthropic Research - An off switch for dual-use knowledge in AI models (Jul 8, 2026)"
url: "https://www.anthropic.com/research/off-switch-dual-use"
---

# GRAM: Gradient-Routed Auxiliary Modules for Dual-Use Knowledge Containment

## Overview

GRAM is a methodology that gives a model dedicated, removable compartments for each category of dual-use knowledge. During training, knowledge from dual-use domains (e.g., virology, cybersecurity) accumulates in dedicated modules rather than diffusing across the whole network. After training, modules can be deleted to remove capabilities, or left in place for trusted deployments.

## How GRAM Works

### Architecture
1. Add extra neurons to every layer of a standard Transformer
2. Divide these neurons into groups ("modules"), one per dual-use category
3. During training:
   - General-purpose text → model learns normally (all weights update)
   - Dual-use text → general-purpose weights are **frozen**, only the relevant module updates
   - The model can use its general knowledge to make predictions, but only the specific module learns from dual-use data

### Key Innovation
Knowledge accumulates in the specific module rather than diffusing across the whole network. Deleting a module removes the corresponding capability as effectively as never having trained on that data at all — without degrading general performance.

## Training Protocol

1. **Define dual-use categories** (e.g., virology, cybersecurity, nuclear physics, specialized code)
2. **Add auxiliary modules** to every transformer layer, one per category
3. **Route gradients** during training:
   - When encountering dual-use text, freeze general weights, update only the relevant module
   - When encountering general text, update all weights normally
4. **Configure deployment**: After training, toggle modules on/off for different deployment scenarios

## Results

- One training run with GRAM yielded a model configurable 16 different ways (on/off for 4 categories)
- Deleting a module removed capability as effectively as data filtering (never training on that data)
- General performance was NOT degraded by module removal
- GRAM resisted knowledge recovery via malicious fine-tuning about as well as data filtering
- Results scaled from 50M to 5B parameters; gap between "module on" and "module off" grew wider at larger scales

## Advantages Over Data Filtering

| Aspect | Data Filtering | GRAM |
|--------|---------------|------|
| Training cost | Need separate model per filter combination | One model, multiple configurations |
| Frontier model cost | Prohibitive (train multiple frontier models) | Train once, configure many ways |
| Capability isolation | Blunt (entire filtered model) | Surgical (remove specific modules) |
| General performance | May degrade from filtered data | Preserved |

## Comparison with Unlearning

| Aspect | Post-training Unlearning | GRAM |
|--------|------------------------|------|
| Knowledge removal | Partial (easy to restore with fine-tuning) | Complete (as effective as filtering) |
| Attack resistance | Low | High (comparable to filtering) |

## Caveats

- Results are preliminary — GRAM has not been applied to any production Anthropic models
- Not clear if it will ever be applied to production models
- Requires defining dual-use categories upfront during training
