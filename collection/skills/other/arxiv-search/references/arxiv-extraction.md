# Full-Text Extraction for arXiv Papers

## ⚠️ ar5iv Limitation
**ar5iv.labs.arxiv.org HTML pages only contain metadata** (title, abstract, authors, navigation chrome) — NOT the full paper body. Do not rely on ar5iv for full-text extraction.

## Reliable Methods (macOS/Homebrew)

### 1. pdftotext (Recommended — fastest, no deps)
`/opt/homebrew/bin/pdftotext paper.pdf output.txt`

### 2. pymupdf (Python)
`import pymupdf; doc = pymupdf.open("paper.pdf")`

### 3. pdf2txt.py (pdfminer)
`/opt/homebrew/Caskroom/miniconda/base/bin/pdf2txt.py paper.pdf > output.txt`
