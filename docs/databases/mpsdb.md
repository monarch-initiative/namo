# MPS-DB Integration

## Overview

MPS-DB (Microphysiology Systems Database) is a database of 150 microphysiological models with emphasis on pharmacokinetic models. Originally containing 32 MPS models, it has grown to include comprehensive pharmacokinetic and pharmacodynamic data for organ-on-chip and tissue-on-chip systems.

## Database Information

- **URL**: Requires paid subscription
- **Focus**: Microphysiological systems with pharmacokinetic emphasis
- **Size**: 150+ models (expanded from original 32)
- **Data Type**: Pharmacokinetic parameters, experimental protocols, model specifications
- **Access**: Subscription-based

## NAMO Integration Strategy

### Data Mapping

MPS-DB entries map primarily to NAMO's microphysiological system classes:

```yaml
OrganOnChip:
  is_a: MicrophysiologicalSystem

TissueOnChip:
  is_a: MicrophysiologicalSystem

MicrophysiologicalSystem:
  attributes:
    microfluidic_design:  # Maps to device specifications
    mechanical_forces:  # Maps to physical parameters
    perfusion_system:  # Maps to flow conditions
    sensor_integration:  # Maps to monitoring capabilities
```

### Key Mappings

| MPS-DB Field | NAMO Property | Ontology/Standard |
|--------------|---------------|-------------------|
| Device Architecture | `microfluidic_design.architecture_type` | ISO10991 |
| Flow Rate | `perfusion_system` | - |
| Cell Types | `cell_types` | CL |
| Drug/Compound | `perturbations` | ChEBI |
| PK Parameters | `pharmacokinetic_properties` | - |
| Organ System | `organ_modeled` | UBERON |
| Channel Configuration | `microfluidic_design.channel_configuration` | ISO22916 |

### Pharmacokinetic Data Integration

Special emphasis on PK/PD parameters:

```yaml
pharmacokinetic_properties:
  clearance:
    value: float
    unit: L/h
  volume_of_distribution:
    value: float
    unit: L
  half_life:
    value: float
    unit: hours
  bioavailability:
    value: float
    unit: percentage
```

## Standards Alignment

### ISO Standards
- **ISO 10991:2023**: Microfluidics vocabulary for device components
- **ISO 22916:2022**: Interoperability requirements for dimensions and connections
- **ASTM F3570**: Standardized terminology for microphysiological systems

### Pharmacokinetic Standards
- PBPK modeling standards from FDA and EMA
- ADMET endpoint standardization
- ICH M15 guideline alignment for extrapolation

## Data Extraction Pipeline

1. **Access Management**: Handle subscription-based access requirements
2. **Structured Extraction**: Parse device specifications and experimental data
3. **PK Parameter Normalization**: Standardize units and calculations
4. **Ontology Mapping**: Link compounds to ChEBI, organs to UBERON
5. **Validation**: Ensure compliance with ISO standards

## Integration Challenges

### Current Limitations
- Subscription paywall limits broad accessibility
- Focus on PK may lack other biological endpoints
- Limited to 150 models compared to other databases
- May lack detailed cellular characterization

### Mitigation Strategies
- Establish institutional access agreements
- Augment PK data with complementary biological endpoints from literature
- Cross-reference with open-access alternatives when possible
- Use metadata for discovery even when full data requires subscription

## Quality Metrics

For MPS-DB entries:
- **Device Specification Completeness**: Coverage of ISO-required parameters
- **PK Data Quality**: Presence of key ADMET parameters
- **Reproducibility Score**: Based on protocol detail level
- **Interoperability Rating**: ISO 22916 compliance level

## Usage Examples

### Query Example
Find liver-on-chip models with drug clearance data:
```sparql
SELECT ?model ?drug ?clearance
WHERE {
  ?model a namo:OrganOnChip ;
         namo:organ_modeled uberon:0002107 ;  # liver
         namo:pharmacokinetic_data ?pk_data .
  ?pk_data namo:compound ?drug ;
           namo:clearance ?clearance .
  FILTER(?clearance > 0)
}
```

### Python API Example
```python
from namo.client import NAMOClient

client = NAMOClient()
mps_models = client.query_mps(
    organ="liver",
    has_pk_data=True,
    source="MPS-DB"
)

# Extract PK parameters
for model in mps_models:
    pk_params = model.get_pharmacokinetic_parameters()
    print(f"Model: {model.id}")
    print(f"Clearance: {pk_params.clearance}")
    print(f"Half-life: {pk_params.half_life}")
```

## Regulatory Relevance

MPS-DB models are particularly valuable for:
- FDA IND applications requiring ADMET data
- EMA qualification opinions for organ-on-chip models
- OECD test guideline development
- ICH S6(R1) nonclinical safety studies

## References

- Gough A, et al. The microphysiology systems database for analyzing and modeling compound interactions with human and animal organ models. Appl In Vitro Toxicol. 2016;2:103–117.

## Related NAMO Classes

- [OrganOnChip](../elements/OrganOnChip.md)
- [TissueOnChip](../elements/TissueOnChip.md)
- [MicrophysiologicalSystem](../elements/MicrophysiologicalSystem.md)
- [MicrofluidicDesign](../elements/MicrofluidicDesign.md)