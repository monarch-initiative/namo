# GIVReST (Guidance for Good In Vitro Reporting Standards)

## Overview

GIVReST provides high-level guidance for reporting in vitro experimental design across six core axes. It offers top-down standards for reporting elements essential to reproducibility and interpretability of in vitro studies.

## Standard Information

- **Full Name**: Guidance for Good In Vitro Reporting Standards
- **Version**: 2025 draft
- **Axes**: 6 core reporting dimensions
- **Purpose**: Enhance in vitro study reproducibility
- **Scope**: All in vitro models including NAMs

## Six Core Reporting Axes

### 1. Cell Identity
```yaml
cell_identity:
  cell_type: CL ontology term
  source: primary/line/iPSC
  authentication: STR/karyotype
  passage_number: integer
  modifications: genetic/epigenetic
```

### 2. Cell Sourcing
```yaml
cell_sourcing:
  supplier: commercial/academic
  catalog_number: string
  lot_number: string
  donor_info: age/sex/disease
  ethical_approval: IRB number
```

### 3. Quality Control
```yaml
quality_control:
  mycoplasma_testing: method and result
  viability: percentage
  purity: percentage
  functionality: assay-specific
  batch_variability: CV
```

### 4. Materials & Methods
```yaml
materials:
  culture_vessels: type/coating
  media: composition/supplements
  reagents: catalog numbers
  equipment: specifications

methods:
  culture_conditions: detailed protocol
  experimental_timeline: step-by-step
  replicates: technical/biological
```

### 5. Experimental Design
```yaml
design:
  hypothesis: clear statement
  controls: positive/negative/vehicle
  randomization: method
  blinding: single/double
  sample_size: justification
  statistics: tests used
```

### 6. Data Availability
```yaml
data_sharing:
  raw_data: repository link
  processed_data: format
  code: GitHub/Zenodo
  protocols: protocols.io
  metadata: complete annotations
```

## NAMO Implementation

### GIVReST Compliance Tracking
```yaml
Study:
  givrest_compliance:
    cell_identity: boolean
    cell_sourcing: boolean
    quality_control: boolean
    materials_methods: boolean
    experimental_design: boolean
    data_availability: boolean
    overall_score: percentage
```

### Principle Mappings

| GIVReST Principle | NAMO Properties | Notes |
|-------------------|-----------------|-------|
| 2.1 Cell taxonomy | `cell_types` | Ontology-based |
| 2.2 Sourcing | `cell_source` | Detailed provenance |
| 2.3 Differentiation | `differentiation_method` | Efficiency metrics |
| 3.1 Culture conditions | `culture_conditions` | Complete protocol |
| 4.1 Experimental design | `Study.experimental_conditions` | Full context |
| 5.1 Analysis methods | `Study.endpoints` | Statistical approach |
| 6.1 Data sharing | `References`, external links | FAIR principles |

## Complex Model Recommendations

GIVReST adds specific guidance for complex NAMs:

### Co-Culture Systems
```yaml
coculture_reporting:
  cell_ratios: exact proportions
  spatial_arrangement: 2D/3D configuration
  interaction_type: direct/paracrine
  temporal_addition: simultaneous/sequential
  validation: cell-specific markers
```

### Microenvironment
```yaml
microenvironment:
  matrix: composition/stiffness
  mechanical_forces: type/magnitude
  oxygen_tension: percentage
  pH: monitored values
  metabolites: glucose/lactate levels
```

## Validation Examples

### GIVReST Checklist Validator
```python
from namo.standards import GIVReSTValidator

validator = GIVReSTValidator()
study_data = load_study("study_001.yaml")

# Generate compliance report
report = validator.assess_compliance(study_data)

# Check each axis
for axis in report.axes:
    print(f"{axis.name}: {axis.compliance}%")
    if axis.missing_elements:
        print(f"  Missing: {', '.join(axis.missing_elements)}")

# Overall assessment
if report.overall_score >= 80:
    print("Study meets GIVReST standards for publication")
else:
    print("Additional information needed for GIVReST compliance")
```

### Automated Report Generation
```python
from namo.reporting import GIVReSTReporter

reporter = GIVReSTReporter()
study = load_study("organoid_toxicity_study.yaml")

# Generate GIVReST-compliant report
report = reporter.generate(study)

# Output formatted document
report.to_markdown("givrest_report.md")
report.to_pdf("givrest_report.pdf")

# Extract for manuscript methods section
methods_text = report.get_methods_section()
```

## Benefits

1. **Transparency**: Complete experimental documentation
2. **Reproducibility**: Sufficient detail for replication
3. **Comparability**: Standardized reporting enables meta-analysis
4. **Regulatory Alignment**: Meets agency expectations
5. **Publication Support**: Journal requirement compliance

## Integration with NAM Reporting

GIVReST principles apply to all NAM types:

- **Organoids**: Formation method, maturation stage
- **Organ-on-Chip**: Device specifications, flow parameters
- **3D Cultures**: Architecture, size distribution
- **In Silico**: Training data, validation sets

## Future Enhancements

- Automated GIVReST compliance checking
- Integration with electronic lab notebooks
- Machine-readable reporting templates
- Version control for protocol updates

## References

- Mohapatra R, et al. Guidance for Good In Vitro Reporting Standards (GIVReSt). ALTEX. 2025;42:376–396.

## Related NAMO Classes

- [Study](../elements/Study.md)
- [NAMModel](../elements/NAMModel.md)
- [CellularSystem](../elements/CellularSystem.md)
- [ExperimentalConditions](../elements/ExperimentalConditions.md)