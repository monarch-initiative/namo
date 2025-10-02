# Cell Model Passports (CMP) Integration

## Overview

Cell Model Passports is a database providing an index of 2,000+ cancer models including organoids, cell lines, and patient-derived xenografts (PDXs). It focuses on cancer research with comprehensive genomic characterization data.

## Database Information

- **URL**: [cellmodelpassports.sanger.ac.uk](https://cellmodelpassports.sanger.ac.uk)
- **Institution**: Wellcome Sanger Institute
- **Focus**: Cancer models with genomic data
- **Size**: 2,000+ models
- **Model Types**: Organoids, cell lines, PDXs
- **Data Type**: Genomic, transcriptomic, drug sensitivity

## NAMO Integration Strategy

### Data Mapping

CMP entries map to multiple NAMO classes:

```yaml
Organoid:
  is_a: ThreeDCellCulture
  # For cancer organoids

CellLineModel:
  is_a: TwoDCellCulture
  # For immortalized cancer cell lines

# Note: PDX models would require AnimalModel class extension
```

### Key Mappings

| CMP Field | NAMO Property | Ontology |
|-----------|---------------|----------|
| Cancer Type | `models.disease` | Mondo |
| Tissue Origin | `organ_modeled` | UBERON |
| Cell Line ID | `id` | Cellosaurus |
| Mutations | `molecular_signatures` | - |
| Drug Response | `pharmacological_response` | ChEBI |
| Patient Demographics | `donor_characteristics` | - |
| Growth Properties | `culture_conditions` | - |

### Cancer-Specific Extensions

CMP requires special handling for cancer-specific properties:

```yaml
cancer_model_properties:
  tumor_type:
    primary_site: UBERON term
    histology: NCIT term
  molecular_features:
    driver_mutations: []
    copy_number_alterations: []
    fusion_genes: []
  drug_sensitivity:
    ic50_values: []
    auc_scores: []
```

## Standards Alignment

### Cell Line Standards
- **Cellosaurus**: Cell line nomenclature and identification
- **COSMIC**: Cancer mutation cataloging
- **CCLE**: Cancer Cell Line Encyclopedia integration

### Authentication Standards
- STR profiling requirements
- Mycoplasma testing protocols
- Species verification standards

## Data Extraction Pipeline

1. **API Access**: Connect to CMP REST API
2. **Model Classification**: Categorize as organoid, cell line, or PDX
3. **Genomic Data Integration**: Link to mutation databases
4. **Drug Response Mapping**: Normalize IC50/AUC values
5. **Donor Metadata**: Extract patient characteristics where available

## Integration Challenges

### Current Limitations
- Limited to cancer models only
- May lack detailed culture protocols
- PDX models don't fit current NAMO NAM focus
- Patient data privacy considerations

### Mitigation Strategies
- Extend NAMO with cancer-specific properties
- Link to external protocol databases
- Create separate PDX tracking with linkage to derived organoids
- Implement appropriate data de-identification

## Quality Metrics

For CMP entries:
- **Authentication Status**: STR profiling completion
- **Genomic Coverage**: WGS/WES/targeted panel specification
- **Drug Panel Size**: Number of compounds tested
- **Clinical Annotation**: Presence of patient treatment history
- **Publication Count**: Number of associated papers

## Usage Examples

### Query Example
Find lung cancer organoids with EGFR mutations:
```sparql
SELECT ?organoid ?mutation
WHERE {
  ?organoid a namo:Organoid ;
           namo:organ_modeled uberon:0002048 ;  # lung
           namo:models ?disease .
  ?disease a mondo:0008903 .  # lung cancer
  ?organoid namo:molecular_features ?features .
  ?features namo:has_mutation "EGFR" .
}
```

### Python API Example
```python
from namo.client import NAMOClient

client = NAMOClient()

# Find breast cancer models with HER2 amplification
models = client.query_cancer_models(
    cancer_type="MONDO:0007254",  # breast cancer
    molecular_feature="ERBB2_amplification",
    source="CMP"
)

# Get drug sensitivity data
for model in models:
    sensitivity = model.get_drug_response("lapatinib")
    print(f"{model.id}: IC50 = {sensitivity.ic50}")
```

## Clinical Relevance

CMP models are valuable for:
- Precision oncology drug selection
- Biomarker discovery
- Resistance mechanism studies
- Co-clinical trial design
- Avatar model development

## Privacy and Ethics

- Patient consent tracking for PDX-derived models
- De-identification protocols for donor metadata
- Data sharing agreements for clinical information
- Ethical review board approvals

## References

- van der Meer D, et al. Cell Model Passports-a hub for clinical, genetic and functional datasets of preclinical cancer models. Nucleic Acids Res. 2019;47:D923–D929.

## Related NAMO Classes

- [Organoid](../elements/Organoid.md)
- [CellLineModel](../elements/CellLineModel.md)
- [ThreeDCellCulture](../elements/ThreeDCellCulture.md)
- [TwoDCellCulture](../elements/TwoDCellCulture.md)