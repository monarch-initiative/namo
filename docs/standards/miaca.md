# MIACA (Minimal Information About a Cellular Assay) Standard

## Overview

MIACA is the first proposal for Minimal Information About a Cellular Assay for Regenerative Medicine. It provides a comprehensive framework for reporting cellular assays, ensuring reproducibility and comparability across studies.

## Standard Information

- **Full Name**: Minimal Information About a Cellular Assay
- **Version**: First proposal (2016)
- **Focus**: Cellular assays in regenerative medicine
- **Purpose**: Standardize reporting for reproducibility

## NAMO Implementation

### Core MIACA Elements in NAMO

Most MIACA elements are already incorporated in the NAMO schema:

```yaml
CellularSystem:
  attributes:
    cell_types:  # MIACA: Cell taxonomy
      range: Term
      bindings: CL (Cell Ontology)

    cell_source:  # MIACA: Cell sourcing
      description: Primary, iPSC-derived, immortalized

    culture_conditions:  # MIACA: Culture parameters
      description: Media, supplements, conditions

Study:
  attributes:
    experimental_conditions:  # MIACA: Assay conditions
    endpoints:  # MIACA: Measured outcomes
```

### Detailed Mappings

| MIACA Element | NAMO Property | Description |
|---------------|---------------|-------------|
| Cell Identity | `cell_types` | Ontology-based cell classification |
| Anatomical Location | `organ_modeled` | UBERON terms for tissue origin |
| Cell Source | `cell_source` | Donor, commercial, derived |
| Culture Method | `culture_conditions` | Growth requirements |
| Passage Number | `passage_protocol` | Subculturing information |
| Quality Control | `authentication_method` | STR, karyotype, markers |
| Assay Type | `technique` | Experimental method |
| Readout | `endpoints` | Measured parameters |

## Schema Extensions for MIACA

### Quality Control Attributes
```yaml
quality_control:
  mycoplasma_status:
    tested: boolean
    result: negative/positive
    method: PCR/biochemical

  authentication:
    str_profile: boolean
    karyotype: boolean
    marker_expression: boolean

  viability:
    method: string
    percentage: float
```

### Donor Information
```yaml
donor_characteristics:
  age: integer or range
  sex: male/female/unknown
  ethnicity: string
  disease_status: Mondo term
  consent: boolean
```

## Validation Rules

MIACA compliance checking in NAMO:

```yaml
validation:
  miaca_compliance:
    required_fields:
      - cell_types
      - cell_source
      - culture_conditions
      - passage_number

    recommended_fields:
      - authentication_method
      - mycoplasma_testing
      - viability_assessment
```

## Usage Examples

### MIACA-Compliant Data Entry
```yaml
organoid:
  type: Organoid
  id: ORG001

  # MIACA required elements
  cell_types:
    - id: CL:0000182
      name: hepatocyte

  cell_source: "iPSC-derived"

  culture_conditions: |
    Hepatocyte maturation medium with
    dexamethasone, oncostatin M, HGF

  # MIACA recommended elements
  authentication_method: "STR profiling"

  quality_control:
    mycoplasma_status:
      tested: true
      result: negative
      method: PCR
```

### Validation Check
```python
from namo.validation import MIACAValidator

validator = MIACAValidator()
model_data = load_model("organoid_001.yaml")

# Check MIACA compliance
result = validator.validate(model_data)
print(f"MIACA compliance: {result.compliance_level}%")
print(f"Missing required: {result.missing_required}")
print(f"Missing recommended: {result.missing_recommended}")
```

## Integration with Other Standards

MIACA complements:
- **MISpheroID**: For 3D culture specifics
- **GIVReST**: For general reporting
- **ARRIVE 2.0**: For in vivo comparisons

## Benefits of MIACA Compliance

1. **Reproducibility**: Complete method documentation
2. **Comparability**: Standardized terminology
3. **Quality Assurance**: Authentication requirements
4. **Regulatory Acceptance**: Meets agency expectations
5. **Data Integration**: Facilitates meta-analysis

## MIACA Checklist for NAMO Users

- [ ] Cell type identified with ontology term
- [ ] Cell source documented
- [ ] Culture conditions specified
- [ ] Passage number recorded
- [ ] Authentication method stated
- [ ] Mycoplasma testing performed
- [ ] Viability assessed
- [ ] Assay type defined
- [ ] Endpoints measured
- [ ] Quality metrics included

## Future Directions

- Automated MIACA compliance scoring
- Integration with electronic lab notebooks
- Machine-readable MIACA templates
- Version tracking for protocol changes

## References

- Sakurai K, et al. First proposal of Minimum Information About a Cellular Assay for Regenerative Medicine. Stem Cells Transl Med. 2016;5:1345–1361.

## Related NAMO Classes

- [CellularSystem](../elements/CellularSystem.md)
- [CellLineModel](../elements/CellLineModel.md)
- [Study](../elements/Study.md)
- [QualityMetrics](../elements/QualityMetrics.md)