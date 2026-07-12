# arXiv /abs/ ID Resolution Mismatch Pitfall (2026-06-10)

## Problem
arXiv listing page IDs do NOT correspond to the same papers on `/abs/{id}` pages.

## Symptom
- Listing page shows `2606.10777` as "Coset Ensemble Decoder for QEC" 
- But `/abs/2606.10777` returns "Can we trust our models? Epistemic calibration" (cs.LG)
- `2606.10849` listed as "quantum classifier" but `/abs/2606.10849` returns "Bethe-Salpeter excitation spectra"

## Root Cause
arXiv listing page ID ordering may differ from the actual arXiv database.

## Fix
1. NEVER trust `/abs/{id}` resolution for papers from listing pages
2. Extract titles directly from listing page snapshot
3. Use arXiv search results for verified details
4. Cross-verify by title search, not ID navigation
5. Use RSS feeds for reliable ID-to-title mapping
