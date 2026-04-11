# SKILL.md - Learned Transfer Membership Inference Attack (LT-MIA)

## Paper Reference
- **arXiv:** 2604.03199
- **Title:** Learning the Signature of Memorization in Autoregressive Language Models
- **Utility Score:** 0.88
- **Authors:** David Ilić et al. (JetBrains Research)
- **Date:** April 2026

## Core Insights

### Key Discovery
**Invariant signature of memorization** detectable across:
- Transformer architectures
- Mamba (state-space)
- RWKV-4 (linear attention)
- RecurrentGemma (gated recurrence)

### Novel Approach
- First **transferable learned attack** for membership inference
- Removes shadow model bottleneck
- Learning what matters rather than designing it
- Generalization through training diversity + scale

### Transfer Results (Zero-shot)
| Target Architecture | AUC |
|---------------------|-----|
| Mamba (state-space) | 0.963 |
| RWKV-4 (linear attention) | 0.972 |
| RecurrentGemma | 0.936 |
| Held-out transformers | 0.908 |

### Cross-Domain Transfer
- Trained only on natural language
- Transfers to code: 0.865 AUC

## Practical Applications

### Model Privacy Assessment
```markdown
1. Train classifier on known membership data
2. Apply to target model (any architecture)
3. Identify memorized training samples
4. Assess privacy risks
```

### Training Data Auditing
- Detect if specific data was in training set
- Cross-architecture detection
- Code detection from text-trained model

### Security Implications
- Gradient descent on cross-entropy creates memorization signature
- Architecture-independent vulnerability
- Requires mitigation strategies

## Key Takeaways
- Memorization is architecture-agnostic
- Membership inference now practical
- Training on synthetic data enables unlimited labeled data
- Privacy risks are cross-architecture

## Open Resources
- GitHub: https://github.com/JetBrains-Research/learned-mia
- Trained classifier available

## Related Work
- Loss thresholding attacks
- Min-K% heuristic
- Reference calibration methods

## Further Reading
- Full paper: https://arxiv.org/abs/2604.03199
- PDF: https://arxiv.org/pdf/2604.03199
## Description

SKILL.md - Learned Transfer Membership Inference Attack (LT-MIA)

## Activation Keywords

- membership-inference-transfer
- membership-inference-transfer 技能
- membership-inference-transfer skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply SKILL.md - Learned Transfer Membership Inference Attack (LT-MIA) to my analysis.

**Agent:** I'll help you apply membership-inference-transfer. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for membership-inference-transfer?

**Agent:** Let me search for the latest research and best practices...
