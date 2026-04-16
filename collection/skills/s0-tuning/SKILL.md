---
name: s0-tuning
description: Zero-overhead parameter-efficient fine-tuning for hybrid recurrent-attention models. Use when discussing efficient LLM adaptation, PEFT methods, LoRA alternatives, or fine-tuning hybrid models like Mamba/GatedDeltaNet. Triggers on "zero overhead PEFT", "S0 tuning", "recurrent state initialization", "hybrid model adaptation", or "efficient fine-tuning".
---

# S0 Tuning: Zero-Overhead Model Adaptation

Key findings from "S0 Tuning: Zero-Overhead Adaptation of Hybrid Recurrent-Attention Models" (arXiv:2604.01168) by Jack Young.

## Core Method

Tune only a **single initial state matrix** per recurrent layer while freezing all model weights.

- Zero inference overhead
- No weight merging required
- Task switching: just swap ~48 MB state file

## Performance Results

### HumanEval
- **+10.8 pp** over LoRA (p < 0.001)
- Using only ~48 execution-verified training solutions

### Qwen3.5-4B (GatedDeltaNet hybrid)
- Greedy pass@1: **+23.6 +/- 1.7 pp** (10 seeds)

### FalconH1-7B (Mamba-2 hybrid)
- S0: 71.8% +/- 1.3
- LoRA: 71.4% +/- 2.4 (statistically indistinguishable)

## Cross-Domain Transfer

Significant transfer:
- MATH-500: **+4.8 pp** (p = 0.00002)
- GSM8K: **+2.8 pp** (p = 0.0003)

No transfer on Spider (text-to-SQL) - consistent with trajectory-steering mechanism.

## When to Use

S0 tuning excels when:
- Verified supervision is scarce
- Need zero inference overhead
- Working with hybrid recurrent-attention models
- Fast task switching required

## Limitations

- Requires hybrid architecture (recurrent layers)
- Pure transformers show degradation (prefix-tuning control: -13.9 pp)
- Works best with execution-verified training data

## Code

GitHub: https://github.com/jackyoung27/s0-tuning

## Reference

arXiv:2604.01168 - "S0 Tuning: Zero-Overhead Adaptation of Hybrid Recurrent-Attention Models" by Jack Young.
Submitted: April 1, 2026