# CompTox Chemicals Dashboard Integration

## Overview

The CompTox Chemicals Dashboard is a comprehensive resource from the US EPA that compiles chemistry, toxicity, and exposure data for over 900,000 chemicals. While primarily focused on chemical information, it includes extensive in vitro screening data relevant to NAM validation and chemical testing.

## Database Information

- **URL**: [comptox.epa.gov/dashboard](https://comptox.epa.gov/dashboard)
- **Institution**: US Environmental Protection Agency
- **Focus**: Chemical toxicity and exposure data
- **Size**: 900,000+ chemicals
- **NAM Relevance**: High-throughput in vitro screening results
- **Data Type**: Chemical properties, toxicity endpoints, assay results

## NAMO Integration Strategy

### Chemical-NAM Linkage

CompTox provides the chemical exposure side of NAM studies:

```yaml
Study:
  perturbations:  # Links to CompTox chemicals
    - chemical: ChEBI or CompTox ID
      concentration: value with units
      duration: time period

NAMModel:
  validated_compounds:  # Chemicals tested in the model
    - compound: CompTox ID
      endpoint: toxicity measure
      response: quantitative result
```

### Key Mappings

| CompTox Field | NAMO Property | Standard |
|---------------|---------------|----------|
| DSSTox ID | `chemical.id` | CompTox namespace |
| Chemical Name | `chemical.name` | IUPAC/common |
| InChIKey | `chemical.inchikey` | InChI |
| ToxCast Assays | `assay_results` | - |
| AC50 Values | `dose_response.ec50` | - |
| Toxicity Endpoints | `endpoints` | - |
| Exposure Predictions | `exposure_context` | - |

### ToxCast/Tox21 Integration

High-throughput screening data maps to NAM validation:

```yaml
validation_data:
  toxcast_assays:
    - assay_id: ToxCast identifier
      activity: active/inactive
      ac50: concentration value
      efficacy: max response
  comparison_to_nam:
    correlation: statistical measure
    concordance: agreement percentage
```

## Standards Alignment

### EPA Standards
- **ToxCast**: High-throughput screening program
- **Tox21**: Federal collaboration screening initiative
- **EDSP21**: Endocrine Disruptor Screening Program

### Chemical Standards
- **DSSTox**: EPA's chemical database
- **InChI**: International Chemical Identifier
- **SMILES**: Chemical structure notation
- **CAS Registry Numbers**: Chemical Abstracts Service

## Data Extraction Pipeline

1. **API Access**: Use CompTox REST API for chemical queries
2. **Chemical Mapping**: Link compounds to ChEBI and PubChem
3. **Assay Result Extraction**: Parse ToxCast/Tox21 screening data
4. **NAM Correlation**: Match chemicals tested in both CompTox and NAMs
5. **Endpoint Harmonization**: Standardize toxicity measures

## Integration Use Cases

### NAM Validation
- Compare NAM results with ToxCast screening data
- Validate organ-on-chip responses against known toxicants
- Benchmark organoid sensitivity to reference compounds

### Chemical Prioritization
- Identify untested chemicals for NAM screening
- Select positive/negative controls from validated compounds
- Design dose ranges based on ToxCast AC50 values

### Regulatory Applications
- Support read-across for chemical categories
- Provide weight-of-evidence for NAM reliability
- Document precedent for regulatory acceptance

## Quality Metrics

For CompTox-NAM integration:
- **Chemical Coverage**: Percentage of NAM compounds in CompTox
- **Assay Overlap**: Common endpoints between ToxCast and NAM
- **Concordance Score**: Agreement between in vitro predictions
- **Data Completeness**: Available metadata for each chemical

## Usage Examples

### Query Example
Find NAM models tested with EPA priority chemicals:
```sparql
SELECT ?model ?chemical ?response
WHERE {
  ?model a namo:NAMModel ;
         namo:tested_compound ?test .
  ?test namo:chemical ?chemical ;
        namo:response ?response .
  ?chemical namo:in_list comptox:EPAPriorityList .
}
```

### Python API Example
```python
from namo.client import NAMOClient
from comptox import CompToxClient

namo = NAMOClient()
comptox = CompToxClient()

# Find organoids tested with validated hepatotoxicants
hepatotoxicants = comptox.get_chemicals(
    endpoint="hepatotoxicity",
    min_studies=5
)

for chemical in hepatotoxicants:
    # Find NAM models tested with this chemical
    models = namo.query_models(
        tested_chemical=chemical.dsstox_id,
        model_type="Organoid",
        organ="liver"
    )

    # Compare responses
    comptox_ac50 = chemical.get_toxcast_ac50()
    for model in models:
        nam_ec50 = model.get_ec50(chemical.dsstox_id)
        correlation = compare_potencies(comptox_ac50, nam_ec50)
```

## Regulatory Relevance

CompTox integration supports:
- TSCA alternative testing requirements
- FDA Modernization Act 2.0 implementation
- REACH compliance for EU chemicals
- OECD test guideline development
- EPA New Approach Methodology workplan

## Data Access

- **Public API**: RESTful web services
- **Batch Download**: FTP site for bulk data
- **Dashboard Search**: Web interface queries
- **R Package**: tcpl for ToxCast analysis

## References

- Williams AJ, et al. The CompTox Chemistry Dashboard: a community data resource for environmental chemistry. J Cheminform. 2017;9:61.

## Related NAMO Classes

- [Study](../elements/Study.md)
- [NAMModel](../elements/NAMModel.md)
- [BiologicalSystem](../elements/BiologicalSystem.md)