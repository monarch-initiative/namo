# NAM Database Integrations

This section documents how NAMO integrates with existing NAM databases, providing mappings, extraction pipelines, and usage examples for each source.

## Integrated Databases

### Comprehensive Resources

- **[OrganoidDB](organoiddb.md)** - Large-scale organoid transcriptomics database with 16,218 organoids
- **[CompTox Dashboard](comptox.md)** - EPA's comprehensive chemical toxicity database with 900,000+ chemicals

### Specialized Databases

- **[MPS-DB](mpsdb.md)** - Microphysiological systems with pharmacokinetic focus (150+ models)
- **[Cell Model Passports](cell-model-passports.md)** - Cancer model repository with genomic data (2,000+ models)
- **[KLOCD](klocd.md)** - Knowledge graph of organ-on-chip models from literature

## Integration Strategy

Each database integration follows a consistent approach:

1. **Schema Mapping** - Align database fields to NAMO classes
2. **Ontology Harmonization** - Map terms to standard ontologies
3. **Data Extraction** - ETL pipelines for data ingestion
4. **Quality Assessment** - Validation and completeness scoring
5. **Cross-Referencing** - Link related data across sources

## Data Access Patterns

### Federated Queries
Query across multiple databases simultaneously:
```python
from namo.client import NAMOClient

client = NAMOClient()
models = client.query_models(
    organ="liver",
    sources=["OrganoidDB", "MPS-DB", "CMP"]
)
```

### Source Attribution
All integrated data maintains provenance:
```yaml
model:
  id: NAMO:0001234
  source_database: OrganoidDB
  source_id: ORG_12345
  extraction_date: 2025-01-01
  extraction_method: API_v2
```

## Database Categories

### By Model Type
- **Organoid-Focused**: OrganoidDB
- **Chip-Focused**: MPS-DB, KLOCD
- **Cell Line-Focused**: Cell Model Passports
- **Chemical-Focused**: CompTox Dashboard

### By Data Type
- **Transcriptomics**: OrganoidDB
- **Pharmacokinetics**: MPS-DB
- **Genomics**: Cell Model Passports
- **Toxicology**: CompTox Dashboard
- **Literature**: KLOCD

## Quality Metrics

Each database integration includes:
- Coverage assessment
- Data completeness scoring
- Ontology mapping success rate
- Update frequency
- Validation status

## Contributing New Databases

To integrate a new database:
1. Create documentation following the template
2. Define schema mappings to NAMO classes
3. Implement ETL pipeline
4. Add quality metrics
5. Submit pull request

## See Also

- [Standards Documentation](../standards/index.md)
- [NAMO Schema](../elements/index.md)
- [Integration Examples](../examples.md)