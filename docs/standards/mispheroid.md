# MISpheroID (Minimum Information for Spheroid Identity) Standard

## Overview

MISpheroID provides a comprehensive knowledgebase and transparency tool for minimum information in spheroid identity. It defines 89 parameters for complete spheroid characterization, ensuring reproducibility and standardization in 3D culture research.

## Standard Information

- **Full Name**: Minimum Information for Spheroid Identity
- **Parameters**: 89 defined attributes
- **Focus**: Spheroid and 3D culture characterization
- **Purpose**: Standardize spheroid reporting
- **Year**: 2021

## NAMO Implementation

### Core MISpheroID Elements

MISpheroID parameters map to NAMO's 3D culture classes:

```yaml
ThreeDCellCulture:
  attributes:
    three_d_architecture: SPHEROID  # MISpheroID focus

    # Spheroid characteristics
    spheroid_properties:
      diameter:
        value: float
        unit: micrometers
      volume:
        value: float
        unit: cubic_micrometers
      compactness:
        value: float  # 0-1 scale
      circularity:
        value: float  # 0-1 scale
```

### Formation Method Categories

MISpheroID defines different formation approaches:

| Formation Method | NAMO Mapping | Sub-parameters |
|-----------------|--------------|----------------|
| Scaffold-based | `matrix_composition` | Material, pore size, stiffness |
| Liquid overlay | `culture_system` | Coating, surface treatment |
| Hanging drop | `culture_system` | Volume, media exchange |
| Magnetic levitation | `culture_system` | Nanoparticle type |
| Microfluidics | `microfluidic_design` | Flow rate, channel design |

## Detailed Parameter Mappings

### Morphological Parameters
```yaml
spheroid_morphology:
  diameter_mean: float
  diameter_std: float
  volume: float
  surface_area: float
  compactness_index: float
  circularity: float
  eccentricity: float

  growth_kinetics:
    formation_time: days
    growth_rate: micrometers_per_day
    maximum_size: micrometers
    plateau_time: days
```

### Cellular Composition
```yaml
cellular_composition:
  total_cell_number: integer

  cell_populations:
    - cell_type: CL term
      percentage: float
      viability: float
      location: core/periphery/mixed

  dead_cell_percentage: float
  proliferation_index: float
  differentiation_markers: []
```

### Culture Conditions
```yaml
formation_conditions:
  seeding_density: cells_per_well

  medium:
    base_medium: string
    supplements: []
    serum_concentration: percentage
    growth_factors: []

  incubation:
    temperature: 37°C
    co2_concentration: 5%
    humidity: 95%
    oxygen_level: normoxic/hypoxic

  culture_vessel:
    type: plate/bioreactor/chip
    surface_treatment: coating_type
    volume: milliliters
```

### Quality Metrics
```yaml
quality_assessment:
  uniformity:
    size_cv: float  # coefficient of variation
    shape_consistency: float
    batch_reproducibility: float

  viability:
    live_dead_staining: boolean
    atp_content: float
    metabolic_activity: float

  functionality:
    albumin_secretion: float  # for hepatic spheroids
    insulin_response: float   # for pancreatic
    barrier_function: float    # for BBB models
```

## MISpheroID Compliance Checklist

Essential parameters (minimum required):
- [ ] Cell type(s) with ontology terms
- [ ] Seeding density
- [ ] Formation method
- [ ] Culture medium composition
- [ ] Time point of analysis
- [ ] Diameter measurement
- [ ] Viability assessment

Recommended parameters:
- [ ] Complete morphological characterization
- [ ] Growth kinetics
- [ ] Cell number quantification
- [ ] Metabolic assessment
- [ ] Batch-to-batch variability
- [ ] Functional readouts

## Schema Extensions for MISpheroID

```yaml
ThreeDCellCulture:
  attributes:
    mispheroid_compliance:
      compliant: boolean
      completeness_score: float  # 0-100%
      missing_essential: []
      missing_recommended: []

    spheroid_specific:
      formation_method: MISpheroIDFormationEnum
      characterization_methods: []
      imaging_modality: confocal/light_sheet/brightfield
      analysis_software: string
```

## Usage Examples

### MISpheroID-Compliant Entry
```yaml
spheroid_model:
  type: ThreeDCellCulture
  three_d_architecture: SPHEROID

  # Essential MISpheroID parameters
  cell_types:
    - id: CL:0000182
      name: hepatocyte
    - id: CL:0000632
      name: Kupffer cell

  spheroid_properties:
    diameter:
      value: 350
      unit: micrometers
    compactness: 0.85

  formation_conditions:
    seeding_density: 1000
    formation_method: hanging_drop

  culture_conditions: |
    William's E medium, 10% FBS,
    dexamethasone, insulin, transferrin

  quality_assessment:
    viability: 92%
    uniformity:
      size_cv: 0.12
```

### Validation Tool
```python
from namo.standards import MISpheroIDValidator

validator = MISpheroIDValidator()
spheroid_data = load_spheroid("spheroid_001.yaml")

# Check MISpheroID compliance
report = validator.validate(spheroid_data)
print(f"MISpheroID score: {report.compliance_score}/100")
print(f"Essential parameters: {report.essential_complete}/{report.essential_total}")
print(f"Recommended parameters: {report.recommended_complete}/{report.recommended_total}")

# Generate missing parameter report
for param in report.missing_essential:
    print(f"Missing essential: {param}")
```

## Benefits of MISpheroID Compliance

1. **Reproducibility**: Complete documentation of formation methods
2. **Comparability**: Standardized morphological measurements
3. **Quality Control**: Defined acceptance criteria
4. **Method Selection**: Informed choice of formation technique
5. **Regulatory Support**: Meets reporting requirements

## Integration with Other Standards

- **MIACA**: General cellular assay requirements
- **GIVReST**: Overall experimental design
- **OECD GD 298**: Spheroid use in toxicity testing

## Future Directions

- Automated image analysis for MISpheroID parameters
- Machine learning for quality prediction
- Integration with high-content screening
- Standardized data exchange formats

## References

- Peirsman A, et al. MISpheroID: a knowledgebase and transparency tool for minimum information in spheroid identity. Nat Methods. 2021;18:1294–1303.

## Related NAMO Classes

- [ThreeDCellCulture](../elements/ThreeDCellCulture.md)
- [Organoid](../elements/Organoid.md)
- [CellularSystem](../elements/CellularSystem.md)
- [QualityMetrics](../elements/QualityMetrics.md)