# CogEEGAgent Implementation Details

## Key Concept: Participant-Disjoint Confirmation

The core innovation of CogEEGAgent is using **participant-disjoint confirmation** to prevent false positives from uncorrected adaptive search. This means:

- **Separation of Concerns**: The analysis selection process is separated from the confirmation process
- **Independent Validation**: Confirmation data comes from different participants than those used for analysis selection
- **Statistical Validity**: Prevents overfitting to specific participant patterns during adaptive search

## Scientific Authority vs Semantic Authority

CogEEGAgent implements a clear separation:
- **LLM Component**: Handles semantic interpretation and proposes registered analyses
- **Deterministic Components**: Handle scientific validation through typed contracts and evidence-bound release

## Practical Implementation Guidelines

### For EEG Analysis Automation:
1. Always maintain separate datasets for analysis selection and confirmation
2. Implement typed contracts that validate analysis choices against registered protocols
3. Use MNE-Python as the scientific foundation for reproducible results
4. Block capability hazards and lifecycle-reuse requests through policy enforcement

### For Knowledge Graph Integration:
- Link papers to skills using the `papers` and `skills` tables in kg.db
- Ensure foreign key relationships are maintained between paper_id and skill_name
- Include activation keywords that cover both methodology ("grounded execution", "selection-aware verification") and application domains ("autonomous eeg analysis", "mne-python agent")

### For Obsidian Notes:
- Document the participant-disjoint confirmation concept as a key methodological contribution
- Highlight the separation of semantic vs scientific authority as a general principle for scientific AI agents
- Include practical applications in cognitive neuroscience, clinical EEG, and research automation

## Related Concepts
- **Adaptive Search Control**: Preventing false positives through held-out confirmation
- **Bounded Autonomy**: Flexible language interface with constrained scientific execution  
- **Auditable Framework**: Complete traceability of analysis decisions and verifications
- **Hazard Prevention**: Blocking prespecified capability hazards and lifecycle-reuse requests