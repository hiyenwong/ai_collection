---
name: code2lora-hypernetwork-adapter
description: "Code2LoRA: Hypernetwork-generated LoRA adapters for code language models under software evolution. Supports static and dynamic adaptation scenarios with zero inference overhead. Activation: code LLM adaptation, repository-specific LoRA, hypernetwork adapters, software evolution, code adaptation."
---

# Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models

## Paper Information

**Title**: Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution  
**arXiv ID**: 2606.06492  
**Published**: 2026-06-04  
**Authors**: Liliana Hotsko, Yinxi Li, Yuntian Deng, Pengyu Nie  
**Categories**: cs.SE, cs.AI, cs.CL  
**PDF**: https://arxiv.org/pdf/2606.06492v1  
**Code**: https://anonymous.4open.science/r/code2lora-6857  
**Models/Data**: https://huggingface.co/code2lora

## Core Contributions

### 1. Hypernetwork-Generated Repository-Specific Adapters

**Problem**: Existing methods for injecting repository knowledge:
- RAG or dependency analysis → long inference-time token overhead
- Per-repository fine-tuning/LoRA → costly at repository scale, brittle to evolving codebases

**Solution**: Hypernetwork generates repository-specific LoRA adapters with **zero inference-time token overhead**.

### 2. Two Usage Scenarios

#### Code2LoRA-Static
- Converts single repository snapshot into adapter
- Suitable for comprehension of stable codebases
- One-shot adapter generation

#### Code2LoRA-Evo
- Adapter backed by GRU hidden state
- Updated per code diff
- Suitable for active development of evolving codebases
- Continuous adaptation

### 3. RepoPeftBench Benchmark

**First benchmark for evaluating repository-level PEFT methods**:
- **Static track**: 40K training + 12K test assertion-completion tasks
- **Evolution track**: 215K commit-derived training + 87K commit-derived test tasks
- **Scale**: 604 Python repositories

## Key Technical Patterns

### Pattern 1: Hypernetwork Adapter Generation

```python
class Code2LoRAHypernetwork:
    """
    Hypernetwork that generates repository-specific LoRA adapters.
    
    Architecture:
        - Repository encoder (processes codebase)
        - Adapter generator (outputs LoRA weights)
        - Zero inference overhead (adapter merged into base model)
    """
    
    def __init__(self, base_model, adapter_dim=64):
        self.base_model = base_model
        self.adapter_dim = adapter_dim
        self.repo_encoder = RepositoryEncoder()
        self.adapter_generator = AdapterGenerator()
    
    def generate_adapter(self, repository_snapshot):
        """Generate LoRA adapter for repository."""
        # Encode repository structure
        repo_embedding = self.repo_encoder.encode(repository_snapshot)
        
        # Generate LoRA weights (A and B matrices)
        lora_A, lora_B = self.adapter_generator.generate(
            repo_embedding, 
            dim=self.adapter_dim
        )
        
        # Merge into base model (zero overhead)
        adapted_model = self.merge_adapter(lora_A, lora_B)
        
        return adapted_model
    
    def merge_adapter(self, lora_A, lora_B):
        """Merge LoRA adapter into base model weights."""
        # Standard LoRA merging: W_new = W_base + BA
        # No inference overhead after merging
        return merged_model
```

### Pattern 2: Evolution-Aware Adapter (Code2LoRA-Evo)

```python
class Code2LoRAEvo:
    """
    Evolution-aware adapter with GRU hidden state.
    
    Features:
        - GRU maintains repository state
        - Per-diff updates
        - Continuous adaptation for evolving codebases
    """
    
    def __init__(self):
        self.gru_state = None  # Hidden state tracking
        self.adapter_generator = AdapterGenerator()
    
    def update_adapter(self, code_diff):
        """Update adapter based on code diff."""
        # Process diff into embedding
        diff_embedding = self.encode_diff(code_diff)
        
        # Update GRU hidden state
        self.gru_state = self.gru_update(
            self.gru_state, 
            diff_embedding
        )
        
        # Generate updated adapter from GRU state
        lora_A, lora_B = self.adapter_generator.generate(
            self.gru_state,
            dim=self.adapter_dim
        )
        
        return lora_A, lora_B
    
    def gru_update(self, prev_state, diff_embedding):
        """GRU-based state update."""
        # GRU processes sequential diffs
        # Maintains accumulated repository knowledge
        return new_state
```

### Pattern 3: Variable-Speed Trajectory Augmentation (VSTA)

Although VSTA is mentioned in the paper context, the primary focus is on:

```python
class RepositoryKnowledgeInjection:
    """
    Repository knowledge injection without token overhead.
    
    Methods:
        - Static: Snapshot → Adapter (one-shot)
        - Evo: Diff stream → GRU state → Adapter (continuous)
    """
    
    def inject_static(self, repo_path):
        """One-shot knowledge injection."""
        snapshot = self.load_snapshot(repo_path)
        adapter = self.hypernetwork.generate_adapter(snapshot)
        return self.merge(adapter)
    
    def inject_evo(self, repo_path, commit_history):
        """Continuous knowledge injection."""
        self.gru_state = self.initialize_state()
        
        for commit in commit_history:
            diff = self.extract_diff(commit)
            adapter = self.update_adapter(diff)
            self.merge(adapter)
        
        return self.base_model
```

## System Engineering Principles

### 1. Zero-Inference Overhead Design

**Key Principle**: Knowledge injection should not increase inference cost.

**Implementation**:
- Generate adapters offline
- Merge into base model weights
- Standard inference with adapted model

### 2. Evolution-Aware Architecture

**GRU-Based State Maintenance**:
- Sequential state updates
- Accumulated repository knowledge
- Handles code drift over time

### 3. Scalability at Repository Scale

**Challenge**: Per-repository fine-tuning is costly at scale.

**Solution**:
- Single hypernetwork serves all repositories
- Efficient adapter generation
- No per-repo training overhead

## Implementation Guidelines

### Step 1: Prepare Repository Encoder

1. Design repository representation
2. Encode structure + semantics
3. Handle multiple file types
4. Test encoding quality

### Step 2: Train Hypernetwork

1. Collect repository samples
2. Train adapter generator
3. Validate generated adapters
4. Optimize generation speed

### Step 3: Static Adapter Generation

1. Load repository snapshot
2. Generate LoRA adapter
3. Merge into base model
4. Test on assertion completion

### Step 4: Evolution Adapter Setup

1. Initialize GRU hidden state
2. Process commit history
3. Update adapter per diff
4. Test on commit-derived tasks

### Step 5: Benchmark Evaluation

1. Prepare RepoPeftBench datasets
2. Evaluate static track (cross-repo/in-repo)
3. Evaluate evolution track (commit-derived)
4. Compare with PEFT baselines

## Performance Metrics

### Static Track Results
- **Cross-repo exact match**: 63.8%
- **In-repo exact match**: 66.2%
- **Matches**: Per-repository LoRA upper bound

### Evolution Track Results
- **Cross-repo exact match**: 60.3%
- **Improvement**: +5.2 pp over single shared LoRA

## Benchmark Construction

### RepoPeftBench Structure

**604 Python repositories** with two tracks:

1. **Static Track**:
   - 40K training assertion-completion tasks
   - 12K test assertion-completion tasks
   - Snapshot-based evaluation

2. **Evolution Track**:
   - 215K commit-derived training tasks
   - 87K commit-derived test tasks
   - Diff-based evaluation

### Task Types
- Assertion completion
- API usage prediction
- Import resolution
- Convention inference

## Advantages over Prior Methods

| Method | Inference Overhead | Evolution Support | Scalability |
|--------|-------------------|-------------------|-------------|
| RAG/Dependency Analysis | High (token cost) | Limited | Moderate |
| Per-repo LoRA | Zero | Brittle | Low |
| Shared LoRA | Zero | None | High |
| **Code2LoRA** | **Zero** | **Strong (Evo)** | **High** |

## Limitations

1. Hypernetwork training overhead
2. Adapter generation speed
3. Repository encoder complexity
4. GRU state maintenance for Evo mode

## Related Work Connections

- **LoRA**: Low-rank adaptation for LLMs
- **PEFT**: Parameter-efficient fine-tuning
- **Repository-Level Context**: Code understanding
- **Software Evolution**: Code drift handling

## Use Cases

### 1. Repository Comprehension
- Static analysis of stable codebases
- Convention inference
- API usage prediction

### 2. Active Development Support
- Continuous adaptation during development
- Code diff processing
- Real-time knowledge injection

### 3. Multi-Repository Management
- Scalable adapter generation
- Zero overhead inference
- Repository-specific customization

### 4. Assertion Completion
- Training and test tasks
- Cross-repo and in-repo evaluation
- Commit-derived task generation

## Activation Keywords

- code LLM adaptation
- repository-specific LoRA
- hypernetwork adapters
- software evolution
- code adaptation
- zero overhead knowledge injection
- GRU-based adapter
- RepoPeftBench
- assertion completion
- code drift handling

## References

- Paper: https://arxiv.org/abs/2606.06492
- PDF: https://arxiv.org/pdf/2606.06492v1
- Code: https://anonymous.4open.science/r/code2lora-6857
- Models: https://huggingface.co/code2lora
- Categories: cs.SE, cs.AI, cs.CL

## Notes

- First repository-level PEFT benchmark (RepoPeftBench)
- 604 Python repositories
- 40K + 12K static tasks, 215K + 87K evolution tasks
- Zero inference-time overhead
- Matches per-repo LoRA upper bound (static)
- +5.2 pp improvement over shared LoRA (evo)

## Citation

```bibtex
@article{hotsko2026code2lora,
  title={Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution},
  author={Hotsko, Liliana and Li, Yinxi and Deng, Yuntian and Nie, Pengyu},
  journal={arXiv preprint arXiv:2606.06492},
  year={2026}
}
```