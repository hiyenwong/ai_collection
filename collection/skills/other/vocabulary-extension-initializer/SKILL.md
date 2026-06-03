---
name: vocabulary-extension-initializer
description: "Initialize and extend the vocabulary of language models by adding new tokens, domain-specific terminology, or language-specific characters. Handles embedding initialization strategies (random, average, subword-based) for new tokens. Use when: (1) Adding new language tokens to an existing model, (2) Extending tokenizer with domain-specific vocabulary, (3) Initializing embeddings for new tokens before fine-tuning, (4) Supporting multilingual vocabulary extension."
---

# Vocabulary Extension Initializer

Initialize and extend language model vocabulary with new tokens and embeddings.

## Activation Keywords

- vocabulary extension
- extend tokenizer
- add new tokens
- embedding initialization
- token embedding
- vocabulary initializer
- 词表扩展
- tokenizer extension
- new token embedding
- 词汇表初始化

## Tools Used

- `exec`: Run Python scripts for tokenizer/model modification
- `read`: Load model configuration, tokenizer files, and domain vocabulary
- `write`: Save updated tokenizer and embedding weights

## Core Workflow

### Step 1: Define New Vocabulary

Collect domain-specific tokens, special characters, or language-specific terms:

```python
new_tokens = ["[DOMAIN]", "量子", "纠缠", "[SPECIAL]"]
# Or load from file
with open("domain_vocab.txt") as f:
    new_tokens = [line.strip() for line in f]
```

### Step 2: Extend Tokenizer

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("model_name")
num_added = tokenizer.add_tokens(new_tokens)
print(f"Added {num_added} new tokens")
tokenizer.save_pretrained("./extended_tokenizer")
```

### Step 3: Initialize New Embeddings

Choose initialization strategy:

```python
import torch
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("model_name")
model.resize_token_embeddings(len(tokenizer))

# Strategy 1: Average of subword embeddings
def init_by_subword_average(model, tokenizer, new_token):
    subwords = tokenizer.tokenize(new_token, add_special_tokens=False)
    subword_ids = tokenizer.convert_tokens_to_ids(subwords)
    avg_embedding = model.get_input_embeddings().weight[subword_ids].mean(0)
    return avg_embedding

# Strategy 2: Random initialization (default)
# Model already initialized randomly after resize_token_embeddings
```

### Step 4: Fine-tune on Domain Data

Fine-tune only the new embeddings initially, then jointly:

```python
# Freeze all except new embeddings
for name, param in model.named_parameters():
    if "embed" not in name:
        param.requires_grad = False

# Train on domain data
trainer.train()
```

## Instructions for Agents

### Step 1: Inventory New Vocabulary
Collect tokens to add: domain terms, special tokens, language characters, or symbols.

### Step 2: Check for Conflicts
Verify new tokens don't overlap with existing vocabulary; check for subword coverage.

### Step 3: Extend Tokenizer and Model
Add tokens to tokenizer; resize model embedding matrix accordingly.

### Step 4: Initialize Embeddings
Choose strategy: average of subword embeddings (recommended) or random initialization.

### Step 5: Validate and Fine-tune
Verify tokenization of new tokens; run domain fine-tuning; report vocabulary coverage improvement.

## Examples

### Example 1: Add Chinese Domain Terms

```
User: "Add quantum physics Chinese vocabulary to this language model"

Agent:
1. Collect Chinese quantum terms: 量子, 纠缠, 叠加态, 波函数
2. Check tokenizer: verify these are not already single tokens
3. Add tokens to tokenizer; resize model embeddings
4. Initialize via subword average for Chinese characters
5. Fine-tune on quantum physics Chinese corpus
6. Report tokenization coverage improvement
```

### Example 2: Add Special Domain Tokens

```
User: "Add [PROTEIN], [GENE], [DRUG] special tokens to biomedical model"

Agent:
1. Define special tokens: [PROTEIN], [GENE], [DRUG], [DISEASE]
2. Add to tokenizer as special_tokens
3. Resize embedding matrix (4 new rows)
4. Initialize randomly; these tokens have no subword basis
5. Fine-tune on biomedical NER dataset
6. Validate token recognition in downstream task
```

## Resources

- `references/`: Vocabulary extension techniques and embedding initialization guides
- Related: `declarative-self-improvement`, `espl-evolutionary-system-prompt`
