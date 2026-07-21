# Knowledge Base Pattern: Repository + Spec Enforcement

This pattern ensures the Knowledge Base is both **pluggable** (supports multiple DBs) and **self-validating** (ensures data quality).

## Directory Structure

```text
knowledge/
├── schema.py          # SQL Schema (includes entity_specs table)
├── models.py          # Pydantic/Dataclass models (Entity, Source, Relation)
├── repository/
│   ├── base.py        # Abstract KnowledgeRepository Interface
│   └── sqlite.py      # Concrete SQLite Implementation
├── validator.py       # EntityValidator (Checks rules against specs)
└── service.py         # High-level API (CRUD + Promotion)
```

## 1. The Repository Pattern

Define an abstract interface in `repository/base.py`:

```python
class KnowledgeRepository(ABC):
    @abstractmethod
    def initialize(self) -> None: ...
    @abstractmethod
    def insert_entity(self, entity: Entity) -> str: ...
    @abstractmethod
    def get_entity_spec(self, entity_type: str) -> Optional[dict]: ...
```

## 2. Spec Enforcement

The Knowledge Base stores validation rules in an `entity_specs` table.
When `KnowledgeService.add_entity()` is called:

1.  **Fetch Spec**: `repo.get_entity_spec(entity.type)`
2.  **Validate**: `EntityValidator.validate(entity, rules)`
3.  **Check Rules**:
    -   `required_tags`: Ensure entity has specific tags (e.g., `['approved']`).
    -   `min_confidence`: Reject low-confidence entries (e.g., `< 0.8`).
    -   `min_sources`: Require citations.
4.  **Insert**: Only if validation passes.

## Benefits

-   **Data Quality**: Agents cannot pollute the KB with garbage data.
-   **Flexibility**: Rules can be updated dynamically without code changes.
-   **Portability**: SQLite logic is isolated; switching to Postgres only requires a new Repository implementation.