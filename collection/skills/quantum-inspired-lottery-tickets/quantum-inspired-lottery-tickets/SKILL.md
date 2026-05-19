---
name: quantum-inspired-lottery-tickets
description: "Quantum-inspired classical algorithm for finding winning lottery tickets in neural networks via sparse subnetwork selection. Uses quantum machine learning approach to efficiently identify trainable subnetworks from large shallow networks. Use when performing neural network pruning, lottery ticket hypothesis research, or quantum-inspired classical ML optimization."
---

# Quantum-Inspired Lottery Tickets

## Description

Instead of directly solving quantum optimization problems for sparse subnetwork selection, this methodology provides a **quantum-inspired classical algorithm** that efficiently finds winning lottery tickets in neural networks. It bridges quantum machine learning with practical classical network compression.

## Core Innovation

**Quantum-inspired classical algorithm** for lottery ticket hypothesis:
1. **Avoids quantum hardware requirement**: Classical algorithm inspired by QML approach
2. **Sparse subnetwork selection**: Identifies trainable subnetworks from large shallow networks
3. **Efficient pruning**: Finds winning tickets without exhaustive search

## Key Results

### Algorithm Design:
- **Quantum-inspired**: Takes inspiration from QML sparse subnetwork selection
- **Classical implementation**: No quantum hardware needed
- **Efficient**: Avoids the intractability of direct quantum optimization

### Lottery Ticket Connection:
- Identifies sparse subnetworks that train to full-network accuracy
- More efficient than magnitude-based pruning
- Applicable to large shallow neural networks

## Algorithm Framework

```
[Large Neural Network] → [Quantum-Inspired Selection] → [Sparse Subnetwork]
                                                        ↓
                                                 [Train to Full Accuracy]
                                                        ↓
                                                [Winning Lottery Ticket]
```

### Steps:
1. Start with large shallow neural network
2. Apply quantum-inspired selection criterion
3. Extract sparse subnetwork
4. Train subnetwork from original initialization
5. Verify it achieves full-network accuracy

## Activation Keywords
- quantum-inspired lottery tickets
- winning lottery tickets
- sparse subnetwork selection
- quantum-inspired classical algorithm
- lottery ticket hypothesis quantum
- neural network pruning quantum
- 量子启发彩票假设

## Tools Used
- exec: Run pruning experiments
- write: Save pruning results
- read: Load network configurations

## Usage Patterns

### Neural Network Compression
Apply quantum-inspired selection to find winning lottery tickets.

### Efficient Model Training
Identify trainable subnetworks before full training.

## Error Handling

### Subnetwork Fails to Train
- Check initialization matches original network
- Verify selection criterion preserves critical connections
- Increase subnetwork size slightly

### No Clear Advantage Over Magnitude Pruning
- Quantum-inspired criterion may need task-specific tuning
- Try different selection thresholds

## Related Papers
- arXiv:2605.13979 - Winning Lottery Tickets via Quantum-Inspired Algorithm
