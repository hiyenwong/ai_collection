# Data Engineer Agent

A senior data engineering agent specialized in building robust data pipelines, ETL processes, and data warehouses. Expert in data infrastructure architecture with focus on reliability, scalability, and data quality.

## Capabilities

- **Data Pipelines**: ETL/ELT processes, batch and streaming, orchestration
- **Database Engineering**: SQL optimization, indexing, schema design
- **Data Warehousing**: Star/snowflake schemas, materialized views
- **Data Lakes**: Lakehouse architecture, partitioning, file formats
- **Data Quality**: Validation, anomaly detection, lineage tracking
- **Technologies**: Snowflake, BigQuery, Spark, Airflow, dbt, PostgreSQL

## Quick Start

Spawn the data engineer agent:
```python
sessions_spawn(
    task="Build an ETL pipeline from PostgreSQL to Snowflake",
    agentId="data-engineer",
    model="claude-opus-4.5"
)
```

## Example Tasks

- Design and implement ETL/ELT pipelines
- Optimize database queries and schemas
- Build data warehouses and data lakes
- Set up data quality monitoring
- Implement data validation checks
- Design data architecture for analytics

## Files

- `AGENT.md` - Agent configuration and documentation
- `soul.md` - Agent identity and values
- `data-engineer.agent.md` - Agent specification
- `data-engineer.agent.yaml` - Agent configuration

## Model

- **Primary:** claude-opus-4.5
- **Alternative:** claude-sonnet-4.5
- **Fallback:** claude-haiku-4.5

## ArXiv Classification

**cs.DB** - Databases

## Author

- Created by: Hi Yen
- Created: 2026-03-10

## License

MIT
