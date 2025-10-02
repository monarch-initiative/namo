# OrganoidDB Integration

## Overview

OrganoidDB is a comprehensive database from China that provides an overlay on existing transcriptomics datasets for organoid models. It contains 16,218 organoids with associated transcriptomic data, making it one of the largest collections of organoid-related omics data.

## Database Information

- **URL**: Not specified in available documentation
- **Origin**: China
- **Focus**: Organoid models with transcriptomic data
- **Size**: 16,218 organoids
- **Data Type**: Primarily transcriptomics overlays

## NAMO Integration Strategy

### Data Mapping

OrganoidDB entries map to NAMO's `Organoid` class, which is a subtype of `ThreeDCellCulture`:

```yaml
Organoid:
  is_a: ThreeDCellCulture
  attributes:
    organ_modeled:  # Maps to OrganoidDB tissue/organ annotations
    differentiation_method:  # Maps to protocol information
    culture_system:  # Maps to culture conditions
```

### Key Mappings

| OrganoidDB Field | NAMO Property | Ontology |
|-----------------|---------------|----------|
| Tissue Type | `organ_modeled` | UBERON |
| Cell Types | `cell_types` | CL (Cell Ontology) |
| Species | `species` (inherited) | NCBITaxon |
| Transcriptomic Data | Links to external datasets | - |
| Culture Protocol | `differentiation_method` | OBI |

### Ontology Alignments

- **Anatomical structures**: Map tissue/organ annotations to UBERON terms
- **Cell types**: Map cell type annotations to Cell Ontology (CL) terms
- **Experimental protocols**: Map to OBI (Ontology for Biomedical Investigations)

## Data Extraction Pipeline

1. **ETL Process**: Use Koza framework to extract OrganoidDB data
2. **Harmonization**: Map free-text annotations to ontology terms using OntoGPT
3. **Validation**: Ensure all organoid entries conform to NAMO schema
4. **Linkage**: Connect to external transcriptomic repositories (GEO, ArrayExpress)

## Integration Challenges

### Current Limitations
- Database is primarily focused on transcriptomics rather than comprehensive organoid metadata
- Limited information about culture conditions and protocols
- May lack standardized cell type annotations
- Geographic/language barriers may affect data accessibility

### Mitigation Strategies
- Use AI-based harmonization to standardize tissue and cell type annotations
- Augment with literature mining to capture missing metadata
- Cross-reference with other organoid resources for validation
- Implement multilingual support for data extraction if needed

## Quality Metrics

For OrganoidDB entries integrated into NAMO:
- Completeness score: Percentage of required NAMO fields populated
- Ontology coverage: Percentage of annotations mapped to standard ontologies
- Data linkage: Number of external dataset connections maintained
- Validation status: Pass/fail for NAMO schema compliance

## Usage Examples

### Query Example
Find all liver organoids with transcriptomic data:
```sparql
SELECT ?organoid ?transcriptome
WHERE {
  ?organoid a namo:Organoid ;
           namo:organ_modeled uberon:0002107 ;  # liver
           namo:has_dataset ?transcriptome .
  ?transcriptome a namo:TranscriptomicDataset .
}
```

### Python API Example
```python
from namo.client import NAMOClient

client = NAMOClient()
organoids = client.query_organoids(
    organ="UBERON:0002107",  # liver
    source_database="OrganoidDB"
)
```

## References

- Ma Q, et al. OrganoidDB: a comprehensive organoid database for the multi-perspective exploration of bulk and single-cell transcriptomic profiles of organoids. Nucleic Acids Res. 2023;51:D1086–D1093.

## Related NAMO Classes

- [Organoid](../elements/Organoid.md)
- [ThreeDCellCulture](../elements/ThreeDCellCulture.md)
- [CellularSystem](../elements/CellularSystem.md)