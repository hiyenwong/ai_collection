# Full-Text Extraction for arXiv Papers

## ⚠️ ar5iv Limitation
**ar5iv.labs.arxiv.org HTML pages only contain metadata** (title, abstract, authors, navigation chrome) — NOT the full paper body. Do not rely on ar5iv for full-text extraction.

## Reliable Methods (macOS/Homebrew)

### 1. pdftotext (Recommended — fastest, no deps)

Available at `/opt/homebrew/bin/pdftotext` (Homebrew poppler).

```bash
# Download PDF
curl -sL "https://arxiv.org/pdf/{id}" -o /tmp/paper.pdf

# Extract text
/opt/homebrew/bin/pdftotext /tmp/paper.pdf /tmp/paper.txt

# Read
cat /tmp/paper.txt
```

### 2. pymupdf (Python)

```bash
pip install pymupdf
```

```python
import pymupdf
doc = pymupdf.open("paper.pdf")
text = "\n".join(page.get_text() for page in doc)
```

Note: May not be available in all venvs. Install in system Python or target venv.

### 3. pdf2txt.py (pdfminer)

Available at `/opt/homebrew/Caskroom/miniconda/base/bin/pdf2txt.py`

```bash
/opt/homebrew/Caskroom/miniconda/base/bin/pdf2txt.py paper.pdf > paper.txt
```

## Workflow

1. Download PDF via `curl -sL "https://arxiv.org/pdf/{id}" -o paper.pdf`
2. Extract text via `pdftotext` (preferred) or pymupdf
3. Read and analyze the extracted text
4. Clean up temp files when done
