# Enum: FlowControlMethodEnum 




_Flow control methods for microfluidic devices as defined in ISO 10991:2023_



URI: [namo:FlowControlMethodEnum](https://w3id.org/monarch-initiative/namo/FlowControlMethodEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SYRINGE_PUMP | None | Syringe pump-driven flow |
| PERISTALTIC_PUMP | None | Peristaltic pump-driven flow |
| GRAVITY_DRIVEN | None | Gravity-driven flow |
| PRESSURE_DRIVEN | None | Pressure-driven flow |
| ELECTROOSMOTIC | None | Electroosmotic flow |
| CAPILLARY_ACTION | None | Capillary action-driven flow |
| PNEUMATIC_VALVES | None | Pneumatic valve control |
| MICROVALVES | None | Integrated microvalves |




## Slots

| Name | Description |
| ---  | --- |
| [flow_control_method](flow_control_method.md) | Methods used to control fluid flow in the device |





## See Also

* [https://www.iso.org/standard/82146.html](https://www.iso.org/standard/82146.html)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: FlowControlMethodEnum
description: Flow control methods for microfluidic devices as defined in ISO 10991:2023
from_schema: https://w3id.org/monarch-initiative/namo
see_also:
- https://www.iso.org/standard/82146.html
rank: 1000
permissible_values:
  SYRINGE_PUMP:
    text: SYRINGE_PUMP
    description: Syringe pump-driven flow
    exact_mappings:
    - ISO10991:syringe_pump
  PERISTALTIC_PUMP:
    text: PERISTALTIC_PUMP
    description: Peristaltic pump-driven flow
    exact_mappings:
    - ISO10991:peristaltic_pump
  GRAVITY_DRIVEN:
    text: GRAVITY_DRIVEN
    description: Gravity-driven flow
    exact_mappings:
    - ISO10991:gravity_flow
  PRESSURE_DRIVEN:
    text: PRESSURE_DRIVEN
    description: Pressure-driven flow
    exact_mappings:
    - ISO10991:pressure_driven_flow
  ELECTROOSMOTIC:
    text: ELECTROOSMOTIC
    description: Electroosmotic flow
    exact_mappings:
    - ISO10991:electroosmotic_flow
  CAPILLARY_ACTION:
    text: CAPILLARY_ACTION
    description: Capillary action-driven flow
    exact_mappings:
    - ISO10991:capillary_flow
  PNEUMATIC_VALVES:
    text: PNEUMATIC_VALVES
    description: Pneumatic valve control
    exact_mappings:
    - ISO10991:pneumatic_valve
  MICROVALVES:
    text: MICROVALVES
    description: Integrated microvalves
    exact_mappings:
    - ISO10991:microvalve

```
</details>