# Enum: MechanicalStimulationTypeEnum 



URI: [namo:MechanicalStimulationTypeEnum](https://w3id.org/monarch-initiative/namo/MechanicalStimulationTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CYCLIC_STRETCH | None | Cyclic stretching |
| SHEAR_STRESS | EFO:0022075 | Fluid shear stress |
| COMPRESSION | None | Compression forces |
| TENSION | None | Tensile forces |
| HYDROSTATIC_PRESSURE | EFO:0000534 | Hydrostatic pressure |
| PULSATILE_FLOW | None | Pulsatile flow |
| BREATHING_MOTION | None | Breathing-like cyclic motion |
| PERISTALTIC_MOTION | None | Peristaltic-like motion |




## Slots

| Name | Description |
| ---  | --- |
| [stimulation_type](stimulation_type.md) | Type of mechanical stimulation applied |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: MechanicalStimulationTypeEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  CYCLIC_STRETCH:
    text: CYCLIC_STRETCH
    description: Cyclic stretching
  SHEAR_STRESS:
    text: SHEAR_STRESS
    description: Fluid shear stress
    meaning: EFO:0022075
  COMPRESSION:
    text: COMPRESSION
    description: Compression forces
  TENSION:
    text: TENSION
    description: Tensile forces
  HYDROSTATIC_PRESSURE:
    text: HYDROSTATIC_PRESSURE
    description: Hydrostatic pressure
    meaning: EFO:0000534
  PULSATILE_FLOW:
    text: PULSATILE_FLOW
    description: Pulsatile flow
  BREATHING_MOTION:
    text: BREATHING_MOTION
    description: Breathing-like cyclic motion
  PERISTALTIC_MOTION:
    text: PERISTALTIC_MOTION
    description: Peristaltic-like motion

```
</details>