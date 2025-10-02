# NAM Standards and Guidelines

This section documents standards and guidelines integrated into NAMO, ensuring compliance with international reporting requirements and best practices.

## Reporting Standards

### Cell Culture Standards
- **[MIACA](miaca.md)** - Minimal Information About a Cellular Assay for standardized cell culture reporting
- **[MISpheroID](mispheroid.md)** - Comprehensive 89-parameter standard for spheroid characterization
- **[GIVReST](givrest.md)** - Six-axis framework for good in vitro reporting practices

### Technical Standards
- **[ISO 10991:2023](../schema/namo.yaml)** - Microfluidics vocabulary (integrated in schema)
- **[ISO 22916:2022](../schema/namo.yaml)** - Microfluidics interoperability requirements
- **[ASTM F3570](astm-f3570.md)** - Standardized terminology for microphysiological systems

### Regulatory Standards
- **[OECD OHT210](oecd-oht210.md)** - Harmonised template for chemical risk assessment with NAMs

## Standards by Application

### For Organoid Research
- MIACA (general cellular requirements)
- MISpheroID (3D culture specifics)
- GIVReST (overall reporting)

### For Organ-on-Chip
- ISO 10991:2023 (microfluidics terms)
- ISO 22916:2022 (interoperability)
- ASTM F3570 (MPS terminology)
- GIVReST (experimental design)

### For Toxicology
- OECD OHT210 (regulatory format)
- CompTox integration
- GIVReST (study design)

### For Publication
- MIACA (minimum requirements)
- GIVReST (comprehensive reporting)
- ARRIVE 2.0 (for animal comparisons)

## Compliance Checking

NAMO provides automated compliance checking:

```python
from namo.standards import ComplianceChecker

checker = ComplianceChecker()
model = load_model("my_organoid.yaml")

# Check all applicable standards
report = checker.check_all(model)

# Check specific standard
miaca_report = checker.check_miaca(model)
print(f"MIACA compliance: {miaca_report.score}%")
```

## Standards Hierarchy

```
General Reporting (GIVReST)
  └── Cell Culture (MIACA)
      ├── 3D Culture (MISpheroID)
      └── Microfluidics (ISO 10991, ISO 22916)
          └── MPS (ASTM F3570)
```

## Key Benefits

1. **Reproducibility** - Complete method documentation
2. **Interoperability** - Standardized terminology
3. **Regulatory Acceptance** - Agency-compliant reporting
4. **Data Integration** - Harmonized across sources
5. **Quality Assurance** - Defined acceptance criteria

## Implementation in NAMO

Standards are implemented through:
- **Schema Mappings** - Direct property alignments
- **Validation Rules** - Automated compliance checking
- **Ontology Terms** - Standardized vocabularies
- **Documentation** - Integrated guidance

## Future Standards

Planned integrations:
- FDA guidance documents
- EMA qualification opinions
- ICH guidelines
- ICCVAM recommendations

## Contributing

To add a new standard:
1. Document the standard requirements
2. Map to NAMO schema properties
3. Implement validation rules
4. Add compliance checker
5. Submit documentation

## See Also

- [Database Integrations](../databases/index.md)
- [NAMO Schema](../elements/index.md)
- [Validation Guide](../how-to/validation.md)