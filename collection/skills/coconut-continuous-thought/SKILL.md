# Coconut: Chain of Continuous Thought

## Description

Coconut (Chain of Continuous Thought) is a novel paradigm that enables LLMs to reason in continuous latent space rather than language space. Instead of decoding hidden states into words, Coconut feeds them back directly as input embeddings, enabling breadth-first search (BFS) for better reasoning on complex planning tasks.

**Key Innovation:**
- Reasoning in continuous latent space vs language space
- Avoids premature commitment to single reasoning path
- Enables breadth-first search capability
- Better accuracy-efficiency trade-off

## Tools Used

- read: Load model states
- write: Save reasoning traces
- exec: Run Coconut inference
- browser: Access model weights
- memory_search: Retrieve reasoning patterns

## Instructions for Agents

### Core Concept

**Traditional CoT:** Token → Token → Token → Answer
**Coconut:** Hidden State → Hidden State → Hidden State → Answer

### When to Use

- Complex planning tasks
- Multi-step logical reasoning
- Problems requiring search
- Avoiding premature commitments

## Overview

**Source:** arXiv:2412.06769v3 (COLM 2025)
**Utility:** 0.93
**Paradigm:** Latent reasoning

## Activation Keywords

- coconut reasoning
- continuous thought
- latent reasoning LLM
- chain of continuous thought
- BFS reasoning

---

## Paradigm Comparison

### Language Space vs Latent Space

| Aspect | CoT (Language) | Coconut (Latent) |
|--------|----------------|------------------|
| Representation | Word tokens | Hidden states |
| Search | Greedy (single path) | BFS (multiple paths) |
| Efficiency | Lower (token decoding) | Higher (no decoding) |
| Flexibility | Limited | High |

### Reasoning Pattern

```python
# Traditional CoT
def chain_of_thought(model, question):
    tokens = tokenize(question)
    reasoning = []
    
    while not done:
        token = model.generate_token(tokens + reasoning)
        reasoning.append(token)
    
    return reasoning

# Coconut
def chain_of_continuous_thought(model, question):
    tokens = tokenize(question)
    hidden = model.encode(tokens)
    
    thoughts = []
    for step in range(max_steps):
        # No decoding - use hidden state directly
        hidden = model.forward_hidden(hidden)
        thoughts.append(hidden)
        
        # Can explore multiple paths
        if needs_branching:
            branches = model.branch(hidden, k=3)
            # BFS exploration
    
    return decode(final_hidden)
```

---

## Architecture

### Continuous Thought Mechanism

```python
class ContinuousThought(nn.Module):
    def __init__(self, llm):
        self.llm = llm
        self.hidden_dim = llm.config.hidden_size
    
    def forward(self, input_hidden):
        """
        Instead of: hidden → decode → token → encode → hidden
        We do: hidden → LLM → hidden
        """
        # Use LLM's transformer layers
        output_hidden = self.llm.forward_hidden(input_hidden)
        
        return output_hidden
    
    def reason(self, question, max_steps=5):
        # Encode question
        h = self.llm.encode(question)
        
        # Continuous reasoning loop
        for step in range(max_steps):
            h = self.forward(h)
        
        # Decode only at the end
        answer = self.llm.decode(h)
        return answer
```

---

## Breadth-First Search

### Multi-Path Exploration

```python
class CoconutBFS:
    def __init__(self, model, beam_width=3):
        self.model = model
        self.beam_width = beam_width
    
    def search(self, question, max_depth=5):
        # Initialize with question hidden state
        initial_h = self.model.encode(question)
        
        # BFS frontier
        frontier = [(initial_h, 0.0)]  # (hidden, score)
        solutions = []
        
        for depth in range(max_depth):
            new_frontier = []
            
            for h, score in frontier:
                # Generate multiple continuations
                branches = self.model.branch(h, k=self.beam_width)
                
                for branch_h, branch_score in branches:
                    new_score = score + branch_score
                    new_frontier.append((branch_h, new_score))
            
            # Keep top-k
            frontier = sorted(new_frontier, key=lambda x: -x[1])[:self.beam_width]
            
            # Check for solutions
            for h, s in frontier:
                if self.model.is_complete(h):
                    solutions.append((self.model.decode(h), s))
        
        return solutions
```

---

## Training

### Multi-Stage Training

```python
class CoconutTrainer:
    def train(self, model, dataset):
        # Stage 1: Language-based CoT training
        for batch in dataset:
            loss = model.cot_loss(batch)
            loss.backward()
        
        # Stage 2: Gradually replace tokens with continuous thoughts
        for stage in range(num_stages):
            for batch in dataset:
                # Mix language tokens and continuous thoughts
                mixed_loss = model.mixed_loss(
                    batch,
                    cot_ratio=1.0 - stage / num_stages
                )
                mixed_loss.backward()
        
        # Stage 3: Pure continuous thought
        for batch in dataset:
            loss = model.coconut_loss(batch)
            loss.backward()
```

---

## Advantages

### 1. Efficiency

```python
# CoT requires decoding at each step
for step in range(10):
    token = decode(hidden)  # Expensive
    hidden = encode(token)  # Expensive

# Coconut skips decoding
for step in range(10):
    hidden = model(hidden)  # Efficient
```

### 2. Better Search

```python
# CoT: Commit to first plausible step
def cot_reasoning():
    step1 = generate_next()  # Greedy
    step2 = generate_next()  # Greedy
    # No backtracking

# Coconut: Explore multiple paths
def coconut_reasoning():
    branches = generate_branches(k=5)  # BFS
    best = evaluate_and_select(branches)
    # Can backtrack if needed
```

---

## Performance

| Task | CoT | Coconut | Improvement |
|------|-----|---------|-------------|
| Logical Reasoning | Baseline | +5-10% | Better |
| Planning Tasks | Baseline | +15% | Significant |
| Math Problems | Baseline | +3% | Moderate |
| Efficiency | Baseline | 2x faster | Better |

---

## Implementation

### Complete Coconut Model

```python
class CoconutModel(nn.Module):
    def __init__(self, base_llm, num_thought_tokens=1):
        super().__init__()
        self.llm = base_llm
        self.num_thought_tokens = num_thought_tokens
        
        # Special token for continuous thought
        self.thought_token = nn.Parameter(
            torch.randn(num_thought_tokens, base_llm.config.hidden_size)
        )
    
    def forward(self, input_ids, use_latent=True):
        # Encode input
        hidden = self.llm.get_hidden_states(input_ids)
        
        if use_latent:
            # Append thought tokens
            thought_embeds = self.thought_token.expand(
                hidden.size(0), -1, -1
            )
            hidden = torch.cat([hidden, thought_embeds], dim=1)
        
        # Forward through LLM
        output = self.llm.forward_from_hidden(hidden)
        
        return output
    
    def generate(self, question, max_thoughts=5):
        h = self.encode(question)
        
        # Continuous reasoning
        for _ in range(max_thoughts):
            h = self.thought_step(h)
        
        # Decode answer
        return self.decode(h)
```

---

## Best Practices

1. **Start with CoT training** - Warm up with language reasoning
2. **Gradual transition** - Don't jump straight to latent
3. **Multi-path exploration** - Use BFS for complex tasks
4. **Hybrid approach** - Mix CoT and Coconut as needed
5. **Decode only when needed** - Save computation

---

## Applications

| Domain | Use Case |
|--------|----------|
| Logic Puzzles | Multi-path exploration |
| Planning | BFS search |
| Math Reasoning | Step-by-step without token cost |
| Decision Making | Explore alternatives |

---

## Examples

### Example 1: Basic Usage

**User:** How can I apply coconut-continuous-thought?

**Agent:** I'll help you understand and apply coconut-continuous-thought...

### Example 2: Advanced Application

**User:** What are the key considerations for coconut-continuous-thought?

**Agent:** Let me search for the latest research and best practices...

## References

- Paper: https://arxiv.org/abs/2412.06769
- DOI: https://doi.org/10.48550/arXiv.2412.06769
- Conference: COLM 2025

---

**Created:** 2026-03-28
**Source:** arXiv:2412.06769v3 - "Training LLMs to Reason in a Continuous Latent Space"