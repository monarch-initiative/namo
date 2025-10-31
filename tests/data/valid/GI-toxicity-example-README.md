# GI Organoid Toxicity Screening Example

This example demonstrates how to model an intestinal organoid-derived monolayer system for Phase IV drug metabolite toxicity screening in NAMO.

## File Location
`tests/data/valid/Dataset-GI-toxicity-example.yaml`

## Overview

The example models the workflow shown in your diagram:

1. **Donor → Mixed cell types → Organoids → Monolayers** 
2. **Accessible apical and basal compartments**
3. **Multi-throughput readouts of epithelial damage**

## Key Features

### Model System (OrganOnChip)
- **Organ modeled**: Intestine (UBERON:0000160)
- **Cell types**: Epithelial cells, enterocytes, goblet cells, Paneth cells, enteroendocrine cells
- **Device**: Dual-chamber microfluidic system with:
  - Porous polymer membrane (0.4 μm pores)
  - Apical and basal channels
  - TEER electrodes for barrier function monitoring
  - Transparent for imaging

### Multi-Throughput Functional Assays

The example organizes 17 different functional assays into three categories:

#### High-Throughput Readouts (96/384-well)
- Cell viability (MTT, ATP content)
- Cytotoxicity (LDH release)
- Calcium signaling (Fluo-4)
- ROS generation (DCF)
- ER stress markers (BiP/GRP78, CHOP)
- Mitochondrial membrane potential (TMRE)

#### Medium-Throughput Readouts (24-well)
- TEER measurements (barrier function)
- Paracellular permeability (FITC-dextran, Lucifer Yellow)

#### Low-Throughput Readouts (Microscopy)
- Junction integrity (ZO-1, occludin, E-cadherin immunostaining)
- Cell morphology and swelling
- Calcium signaling dynamics (time-lapse)
- ER stress visualization (confocal imaging)
- XBP1 splicing (RT-PCR/Western)
- Redox state (GSH/GSSG ratio)
- Apoptosis markers (cleaved caspase-3)

### Study Design

The `Study` object captures:
- **Context of use**: Regulatory toxicology and post-market drug safety
- **Biological context**: Polarized epithelial monolayers with mixed cell types
- **Perturbations**: Phase IV metabolites at 0.1-100 μM, acute and chronic exposure
- **Endpoints**: Complete description of multi-throughput readouts
- **Comparators**: Validation against known GI toxicants and clinical data

## How to Use This Example

### 1. View the Complete Example
```bash
cat tests/data/valid/Dataset-GI-toxicity-example.yaml
```

### 2. Validate the Example
```bash
uv run python -m pytest tests/test_data.py -k "Dataset-GI" -v
```

### 3. Load Programmatically
```python
from linkml_runtime.loaders import yaml_loader
import namo.datamodel.namo as namo

# Load the dataset
dataset = yaml_loader.load(
    "tests/data/valid/Dataset-GI-toxicity-example.yaml",
    target_class=namo.Dataset
)

# Access the model system
intestinal_chip = dataset.model_systems[0]
print(f"Model: {intestinal_chip.name}")
print(f"Organ: {intestinal_chip.organ_modeled.name}")

# Access functional assays
functional_parity = intestinal_chip.models[0].structured_concordance.functional_parity
print(f"Number of assays: {len(functional_parity.functional_assays)}")

for assay in functional_parity.functional_assays:
    print(f"- {assay.name} ({assay.assay_type})")
```

## Key Design Patterns Demonstrated

### 1. Structured Concordance
Uses the full `structured_concordance` framework with:
- `molecular_similarity` - Gene expression analysis
- `functional_parity` - **17 functional assays organized by throughput**
- `cell_type_coverage` - Cell type representation analysis
- `reproducibility` - Quality control metrics

### 2. Comprehensive Functional Assays
Each assay captures:
- `id`, `name`, `assay_type`
- `assay_result` and `reference_value`
- `units` for quantification
- `methodology` with detailed protocol description

### 3. Multi-Scale Organization
The example shows how to organize readouts by:
- **Throughput level** (high/medium/low)
- **Mechanism** (viability, stress pathways, barrier function)
- **Technical approach** (plate reader, microscopy, molecular)

### 4. Study Context
Comprehensive study design including:
- Regulatory context and intended use
- Detailed biological context with limitations
- Perturbation conditions (dose, duration, route)
- Complete endpoint descriptions
- Validation strategy

## Customization Tips

To adapt this example for your specific study:

1. **Change the organ/tissue**: Update `organ_modeled` and `cell_types`
2. **Modify device specifications**: Edit `microfluidic_design` details
3. **Add/remove assays**: Adjust the `functional_assays` list
4. **Update perturbations**: Modify the `Study.perturbations` field
5. **Change validation strategy**: Update `Study.plan_comparators`

## Validation

The example has been validated against the NAMO schema and successfully loads with all metadata intact.

```bash
# Run all tests including this example
uv run python -m pytest tests/test_data.py -v
```

## Related Examples

- `OrganOnChip-example-001.yaml` - CF Airway-on-Chip with structured concordance
- `Organoid-example-002.yaml` - Hepatic organoid with functional assays
- `TissueOnChip-example-002.yaml` - Intestinal absorption model

## Questions?

For more information about NAMO schema design:
- Schema documentation: https://monarch-initiative.github.io/namo/
- Curation guides: Check `docs/how-to/` directory
- CLAUDE.md: Project-specific guidance at `/Users/cjm/repos/namo/CLAUDE.md`
