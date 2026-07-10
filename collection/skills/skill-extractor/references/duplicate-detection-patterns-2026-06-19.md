# Efficient Duplicate Detection Patterns (2026-06-19)

## search_files vs grep -rl for Skill Duplicate Checks

When checking whether an arXiv paper's concepts already have a skill, two methods are available:

### Method 1: `search_files` (Preferred — Fast, Tool-Native)
```
search_files(path="/Users/hiyenwong/.hermes/skills", pattern="keyword1|keyword2|arxiv_id")
```
- **Pros**: Fast, no timeout issues, built-in pagination, searches all skill directories automatically
- **Cons**: Regex only (no glob), may need multiple calls for different keyword combinations
- **Use when**: Quick existence check, large skill directories (>500 skills)

### Method 2: `grep -rl` (Fallback — More Precise but Slower)
```
cd /Users/hiyenwong/.hermes/skills && grep -rl "keyword.*pattern" . 2>/dev/null
```
- **Pros**: More flexible regex, can combine with other grep flags
- **Cons**: Can hit 15s timeout on large directories, macOS grep limitations (no -P)
- **Use when**: Complex pattern matching needed, search_files returns too many false positives

### Recommended Strategy
1. First try `search_files` with arXiv ID (most precise)
2. If no hit, try `search_files` with 2-3 key concept terms (pipe-separated regex)
3. Only use `grep -rl` if search_files misses something obvious

### Example: Checking 4 Papers
```python
# search_files approach (used successfully 2026-06-19)
search_files(path="~/.hermes/skills", pattern="blind.*symmetry.*matching|2606.19196")
search_files(path="~/.hermes/skills", pattern="TopSFF|topological.*spectral.*form|2606.19331")
search_files(path="~/.hermes/skills", pattern="exclusion.*statistics.*thermodynamic|2606.19310")
search_files(path="~/.hermes/skills", pattern="quantum.soliton|2606.19339|transmon.*soliton")
```
Result: Found 1 existing (blind-symmetry-matching), 3 genuinely new — in under 5 seconds total.

## Number Theory + Quantum Domain Saturation (Updated 2026-06-19)

**Saturation Level**: ~40-50% (lower than most domains)

**Pattern**: Genuine Number Theory + Quantum cross-domain papers are rare. Most search hits are from adjacent areas:
- Quantum algebra / topology (knot invariants, quantum groups, Verma modules)
- Statistical mechanics (spectral form factors, exclusion statistics)
- Quantum simulation platforms (transmon arrays, superconducting qubits)

**True intersections** (quantum algorithms for number-theoretic problems, Shor's algorithm improvements, post-quantum cryptography number theory) appear infrequently in recent arXiv submissions.

**Strategy**: When searching Number Theory + Quantum:
1. Broaden to "quantum algebra", "quantum topology", "quantum statistics" for better yield
2. Accept adjacent-area papers — they still produce valuable skills
3. Don't expect Shor's-algorithm-type papers every session

**Updated saturation data (2026-06-19)**: Physics+Quantum statistics domain shows good yield — papers on quantum statistics in colliders, Pauli blocking in plasmas, and anyonic thermodynamics are all valid cross-domain signals. The "quantum statistics" keyword bridges statistical mechanics and quantum information, making it a productive search axis for Number Theory + Quantum sessions.

## arXiv API Rate Limit Fallback (2026-06-19)

When arXiv API returns HTTP 429 and web_search (Firecrawl) returns NoneType errors:

**Working fallback**: Use `browser_navigate` to arXiv search URL:
```
browser_navigate("https://arxiv.org/search/?searchtype=all&query=quantum+AND+number+theory&start=0&order=-announced_date_first")
```

Extract arXiv IDs from page snapshot → `search_files` against skills for dedup.

**Alternative**: Crossref API works as independent fallback:
```
curl "https://api.crossref.org/works?query=quantum+number+theory&select=title,author,published&rows=5"
```
