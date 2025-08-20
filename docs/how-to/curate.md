# NAMO Paper Curation Guides

This directory contains comprehensive guides for curating different types of NAM (New Approach Methodology) research papers into the NAMO data model. Each guide provides step-by-step instructions tailored to the specific characteristics and requirements of different model types.

## Available Guides

### 📧 [How to Curate an Organoid Paper](curate-organoid-paper.md)

Learn to curate organoid research papers with focus on:
- **Biological complexity**: Self-organization, differentiation protocols
- **Culture systems**: Matrix composition, growth factors, cost optimization  
- **Validation strategies**: Morphological, functional, and molecular assessment
- **Example**: Takahashi et al. cost-reduced intestinal organoid drug screening

**Key Features**:
- Step-by-step walkthrough from abstract to final YAML
- Emphasis on biological differentiation and self-organization
- Culture optimization and cost-reduction strategies
- Organoid-specific validation metrics

---

### 🔬 [How to Curate an Organ-on-Chip Paper](curate-organ-on-chip-paper.md)

Learn to curate organ-on-chip and microphysiological system papers with focus on:
- **Technical engineering**: Microfluidic design, flow control, sensor integration
- **System architecture**: Multi-channel, layered, and complex geometries
- **Performance metrics**: Throughput, automation, reproducibility
- **Example**: Zhu et al. dynamic multi-organ drug screening platform

**Key Features**:
- Detailed microfluidic design parameter extraction
- Enum validation for technical specifications
- Multi-organ system integration approaches
- Engineering-focused validation strategies

---

## General Curation Principles

### Universal Best Practices

1. **Start with Paper Structure**
   - **Abstract**: Identifies model type and key innovation
   - **Methods**: Technical protocols and parameters  
   - **Results**: Performance data and validation
   - **Discussion**: Context and limitations

2. **Schema Mapping**
   - Use appropriate ontology IDs (UBERON for anatomy, CL for cell types)
   - Ensure controlled vocabulary compliance
   - Check enum values against schema definitions
   - Validate required fields for each model class

3. **Technical Accuracy**
   - Extract quantitative measurements and performance metrics
   - Capture innovation and unique features
   - Document validation approaches and results
   - Include comprehensive literature references

4. **Quality Assurance**
   - Run `just test` to ensure YAML validates
   - Verify all required fields are complete
   - Check enum values are correct
   - Test against the schema after curation

## Model Type Decision Tree

```
Is it a microfluidic device?
├─ Yes: Use OrganOnChip or TissueOnChip guide
│   ├─ Focus on organ physiology → OrganOnChip
│   └─ Focus on tissue function → TissueOnChip
└─ No: Is it self-organizing from stem cells?
    ├─ Yes: Use Organoid guide
    └─ No: Consider other NAM model types
        ├─ 3D cell culture without microfluidics → ThreeDCellCulture
        ├─ Computational model → MLModel, QSARModel, etc.
        └─ Animal model → AnimalModel
```

## Schema Classes Summary

| Model Class | Abstract? | Key Features | Required Fields |
|-------------|-----------|--------------|----------------|
| `Organoid` | No | Self-organizing, stem cell-derived | `organ_modeled`, `cell_source` |
| `OrganOnChip` | No | Microfluidic, organ physiology | `organ_modeled`, `microfluidic_design` |
| `TissueOnChip` | No | Microfluidic, tissue function | `tissue_modeled`, `microfluidic_design` |
| `MicrophysiologicalSystem` | **Yes** | Use concrete subclasses above | N/A |
| `ThreeDCellCulture` | No | 3D without microfluidics | `three_d_architecture` |

## Common Enum Values

### Complexity Levels
- `LOW`: Simple, single-parameter models
- `MODERATE`: Multi-parameter with some interactions  
- `HIGH`: Complex, multi-system interactions

### Architecture Types  
- **Microfluidic**: `SINGLE_CHANNEL`, `MULTI_CHANNEL`, `LAYERED`
- **3D Culture**: `SPHEROID`, `SCAFFOLD_BASED`, `HYDROGEL_EMBEDDED`

### Flow Control
- `SYRINGE_PUMP`, `PRESSURE_DRIVEN`, `GRAVITY_DRIVEN`, `PERISTALTIC_PUMP`

## Troubleshooting

### Common Validation Errors

1. **Unknown enum code**: Check schema for valid enum values
2. **Missing required field**: Add mandatory fields for model class
3. **Invalid class name**: Use concrete classes, not abstract ones
4. **Incorrect file naming**: Use `ClassName-example-ID.yaml` format

### Getting Help

- Check existing examples in `tests/data/valid/`
- Validate with `just test` after changes
- Review schema definitions in `src/namo/schema/namo.yaml`
- Consult class-specific guides for detailed instructions

---

*These guides ensure comprehensive, accurate curation while maintaining consistency with the NAMO data model across different types of NAM research.*