---
name: openai-privacy-filter
description: Methodology for building PII detection and redaction models using bidirectional token-classification with span decoding and constrained Viterbi. Based on OpenAI Privacy Filter (1.5B params, 50M active, 128K context). Use when implementing privacy-preserving NLP pipelines, PII detection systems, or data redaction workflows.
---

# OpenAI Privacy Filter

Methodology for building privacy-preserving PII detection models inspired by OpenAI's Privacy Filter. Uses a bidirectional token-classification approach with span decoding.

## Architecture Overview

The Privacy Filter architecture consists of:

1. **Base**: Start from an autoregressive pretrained checkpoint
2. **Adaptation**: Convert into a bidirectional token classifier over a fixed taxonomy of privacy labels
3. **Span Decoding**: Use constrained Viterbi procedure for coherent span boundaries
4. **Output**: BIOES span tags for clean masking boundaries

Key properties:
- **Fast**: All tokens labeled in a single forward pass
- **Context-aware**: Language prior enables detection based on surrounding context
- **Long-context**: Supports up to 128,000 tokens
- **Configurable**: Tunable operating points for precision vs. recall tradeoff
- **Local execution**: Can run on-device without data leaving the machine

## Model Specs

- Total parameters: 1.5B
- Active parameters: 50M
- Context window: 128K tokens
- Architecture: Bidirectional token-classification with span decoding

## PII Categories (8 types)

The model predicts spans across eight categories:
- PERSON (names)
- EMAIL (email addresses)
- PHONE (phone numbers)
- ADDRESS (physical addresses)
- ACCOUNT_NUMBER (credit cards, bank accounts, etc.)
- CREDENTIAL (passwords, API keys, etc.)
- DATE (dates, times)
- URL (web addresses)

Labels decoded with BIOES span tags.

## Training Approach

1. Fine-tune from autoregressive pretrained checkpoint
2. Adapt into token classifier over privacy label taxonomy
3. Use constrained Viterbi procedure for coherent span decoding
4. Achieves SOTA on PII-Masking-300k benchmark

## Usage Patterns

### Deployment Options
- Run locally for privacy: PII can be masked without leaving the machine
- High-throughput: Single pass processing
- Production-grade: Configurable precision/recall tradeoff

### Integration
- Training pipelines (data sanitization)
- Indexing pipelines (content filtering)
- Logging pipelines (log redaction)
- Review pipelines (content moderation)

## Related Resources

- [OpenAI Privacy Filter Announcement](https://openai.com/index/introducing-openai-privacy-filter/)
- PII-Masking-300k benchmark

## Activation

- Keywords: PII detection, privacy filter, data redaction, token classification, span decoding, Viterbi decoding, personal information, data sanitization
