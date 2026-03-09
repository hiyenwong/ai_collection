# Dependency Checker Script

Cross-platform dependency checker and installer for the ai_collection project.

## Features

- **System Detection**: Automatically detects macOS, Linux (Debian/RedHat/Arch), and Windows
- **Package Manager Support**: 
  - macOS: Homebrew (`brew`)
  - Debian-based Linux: `apt`
  - RedHat-based Linux: `dnf`/`yum`
  - Arch-based Linux: `pacman`
  - Windows: `winget`/`chocolatey`/`scoop`
- **Dependency Types**: Supports system tools, Python packages, and npm packages
- **Colored Output**: Clear, color-coded status indicators
- **JSON Reports**: Machine-readable reports for CI/CD integration
- **Auto-Install**: Optional automatic installation of missing dependencies

## Usage

```bash
# Check all dependencies
python scripts/check-dependencies.py

# Auto-install missing dependencies
python scripts/check-dependencies.py --install

# Preview installations without running them
python scripts/check-dependencies.py --install --dry-run

# Check a specific skill
python scripts/check-dependencies.py --skill stock-analysis

# Generate JSON report
python scripts/check-dependencies.py --report

# Disable colors (for CI/CD)
python scripts/check-dependencies.py --no-color
```

## Output Example

```
============================================================
  System Information
============================================================

  OS:        macOS
  Version:   26.3.1
  Architecture: arm64
  Package Manager: brew

============================================================
  Checking Dependencies
============================================================


  stock-analysis:
    Comprehensive stock technical analysis
    ✅ python3 (3.14.3) [required: >=3.8]
    ✅ pip3 (26.0)
    ✅ akshare (1.18.30)
    ✅ pandas (3.0.1)
    ✅ numpy (2.4.2)
    ✅ matplotlib (3.10.8)
    ❌ plotly
    ⚠️  TA-Lib (optional)
    ⚠️  mplfinance (optional)

============================================================
  Summary
============================================================

  Total Dependencies: 10
  Satisfied: 6
  Missing (Required): 1
    • plotly
      Install: pip3 install plotly
```

## Status Indicators

| Icon | Meaning |
|------|---------|
| ✅ | Installed and satisfied |
| ❌ | Missing (required) |
| ⚠️ | Missing (optional) |

## Supported Skills

| Skill | Description | Dependencies |
|-------|-------------|--------------|
| `chat-history-lancedb` | LanceDB chat history with vector search | Node.js, npm |
| `skill-rag-indexer` | RAG indexer for skills | Node.js, npm |
| `akshare` | Chinese financial market data | Python 3.8+, pip, akshare |
| `stock-analysis` | Stock technical analysis | Python 3.8+, pip, akshare, pandas, numpy, matplotlib, plotly |
| `teach-cofounder` | Socratic technical mentorship | None |

## Notes

### macOS with Homebrew Python

If you're using Homebrew's Python on macOS, you may encounter an "externally-managed-environment" error when installing Python packages. The script will automatically try using the `--break-system-packages` flag.

For better isolation, consider using:
- **Virtual environments**: `python3 -m venv .venv && source .venv/bin/activate`
- **pipx**: For installing Python CLI tools globally

### Linux Distributions

The script automatically detects your Linux distribution and uses the appropriate package manager:
- Debian/Ubuntu/Mint: `apt`
- Fedora/RHEL/CentOS: `dnf` or `yum`
- Arch/Manjaro: `pacman`

### Windows

On Windows, the script checks for:
1. Windows Package Manager (`winget`)
2. Chocolatey (`choco`)
3. Scoop (`scoop`)

## Extending

To add new skills or dependencies, edit the `SKILLS` dictionary in `check-dependencies.py`:

```python
SKILLS: dict[str, Skill] = {
    "your-skill": Skill(
        name="your-skill",
        description="Your skill description",
        dependencies=[
            Dependency(name="python3", version_required=">=3.8", category="system"),
            Dependency(name="your-package", category="python"),
        ]
    ),
}
```

## Integration with CI/CD

Use the `--report` flag to generate a JSON report for CI/CD pipelines:

```yaml
# GitHub Actions example
- name: Check dependencies
  run: python scripts/check-dependencies.py --report
  
- name: Upload report
  uses: actions/upload-artifact@v3
  with:
    name: dependency-report
    path: dependency-report.json
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All required dependencies satisfied |
| 1 | Missing required dependencies |

This allows using the script in shell scripts:

```bash
python scripts/check-dependencies.py || python scripts/check-dependencies.py --install
```