---
name: cross-tokenizer-on-policy-distillation
description: "Cross-Tokenizer On-Policy Distillation framework using byte-prefix marginalization to enable knowledge transfer between models with different tokenizers while preserving policy quality."
---

# Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization

## Overview
This framework enables on-policy distillation between teacher and student models that use different tokenizers by leveraging byte-prefix marginalization. The approach addresses the fundamental incompatibility between different tokenization schemes while preserving the quality of policy learning in reinforcement learning settings.

## Key Contributions
- **Byte-Prefix Marginalization**: Novel technique for aligning different tokenization spaces at the byte level
- **Cross-Tokenizer Compatibility**: Enables knowledge transfer between models with incompatible tokenizers
- **Policy Quality Preservation**: Maintains high-quality policy learning during distillation
- **On-Policy Learning**: Supports iterative policy improvement through on-policy distillation
- **General Framework**: Applicable to various RL and language modeling scenarios

## Methodology
1. **Byte-Level Alignment**: Map both teacher and student tokenizations to a common byte representation
2. **Prefix Marginalization**: Compute marginal probabilities over byte prefixes to handle token boundary mismatches
3. **Policy Transfer**: Transfer policy knowledge using aligned byte-level representations
4. **On-Policy Updates**: Iteratively improve student policy through interaction with environment
5. **Quality Assurance**: Validate policy performance throughout distillation process

## Applications
- **Reinforcement Learning**: Transfer policies between agents with different tokenization schemes
- **Language Model Distillation**: Distill large language models to smaller models with different tokenizers
- **Multi-Lingual Transfer**: Enable knowledge transfer across languages with different tokenization
- **Model Compression**: Compress models while changing tokenizer for efficiency
- **Cross-Architecture Learning**: Transfer knowledge between different model architectures with incompatible tokenizers

## Implementation Guidelines
- Implement efficient byte-prefix marginalization to handle computational complexity
- Use caching strategies for repeated byte sequence computations
- Validate alignment quality through token reconstruction accuracy
- Monitor policy degradation during distillation process
- Consider trade-offs between alignment fidelity and computational overhead

## Evaluation Metrics
- **Policy Performance**: Task-specific performance metrics after distillation
- **Alignment Quality**: Accuracy of byte-level token reconstruction
- **Computational Efficiency**: Time and memory overhead of cross-tokenizer alignment
- **Transfer Success Rate**: Proportion of successful knowledge transfers
- **Generalization**: Performance on held-out tasks or environments

## Activation Triggers
Use this framework when:
- Performing distillation between models with different tokenizers
- Working with on-policy reinforcement learning scenarios requiring knowledge transfer
- Need to preserve policy quality during cross-tokenizer model compression
- Building multi-lingual or cross-architecture transfer learning systems
- Encountering tokenization incompatibility in model distillation pipelines

## References
- arXiv:2607.22334 - Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization