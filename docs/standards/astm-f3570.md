# ASTM F3570 Standard for Microphysiological Systems

## Overview

ASTM F3570 provides standardized terminology for microphysiological systems (organ-on-chip), facilitating communication between vendors, scientists, and stakeholders. It focuses on physical and engineering aspects of MPS devices.

## Standard Information

- **Full Name**: Standard Terminology Relating to Microphysiological Systems
- **Organization**: ASTM International
- **Committee**: F04 Medical and Surgical Materials and Devices
- **Focus**: MPS terminology standardization
- **Purpose**: Industry-wide consistency

## NAMO Implementation

### Device Terminology Mappings

```yaml
MicrophysiologicalSystem:
  see_also:
    - https://www.astm.org/f3570-24.html
  exact_mappings:
    - ASTM:F3570_microphysiological_system

OrganOnChip:
  exact_mappings:
    - ASTM:F3570_organ_on_chip

TissueOnChip:
  exact_mappings:
    - ASTM:F3570_tissue_chip
```

## Key Term Definitions

| ASTM F3570 Term | NAMO Property | Definition |
|-----------------|---------------|------------|
| Microphysiological system | `MicrophysiologicalSystem` | Engineered cellular system modeling tissue function |
| Microfluidic device | `microfluidic_design` | Device with microscale fluid channels |
| Perfusion | `perfusion_system` | Continuous flow through system |
| Barrier function | `barrier_functions` | Selective permeability property |
| Co-culture | `CoCulture` | Multiple cell types in same system |

## References

- ASTM F3570-24 Standard Terminology Relating to Microphysiological Systems

## Related NAMO Classes

- [MicrophysiologicalSystem](../elements/MicrophysiologicalSystem.md)
- [OrganOnChip](../elements/OrganOnChip.md)
- [TissueOnChip](../elements/TissueOnChip.md)