# Enum: MicrofluidicArchitectureEnum 




_Architecture types for microfluidic devices as defined in ISO 10991:2023_



URI: [namo:MicrofluidicArchitectureEnum](https://w3id.org/monarch-initiative/namo/MicrofluidicArchitectureEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SINGLE_CHANNEL | None | Single channel design |
| TWO_CHANNEL | None | Two-channel design with separated compartments |
| MULTI_CHANNEL | None | Multiple channels (>2) design |
| LAYERED | None | Layered/stacked channel architecture |
| RADIAL | None | Radial channel architecture |
| NETWORK | None | Network of interconnected channels |




## Slots

| Name | Description |
| ---  | --- |
| [architecture_type](architecture_type.md) | The overall architecture type of the microfluidic device |





## See Also

* [https://www.iso.org/standard/82146.html](https://www.iso.org/standard/82146.html)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: MicrofluidicArchitectureEnum
description: Architecture types for microfluidic devices as defined in ISO 10991:2023
from_schema: https://w3id.org/monarch-initiative/namo
see_also:
- https://www.iso.org/standard/82146.html
rank: 1000
permissible_values:
  SINGLE_CHANNEL:
    text: SINGLE_CHANNEL
    description: Single channel design
    exact_mappings:
    - ISO10991:single_channel_device
  TWO_CHANNEL:
    text: TWO_CHANNEL
    description: Two-channel design with separated compartments
    exact_mappings:
    - ISO10991:dual_channel_device
  MULTI_CHANNEL:
    text: MULTI_CHANNEL
    description: Multiple channels (>2) design
    exact_mappings:
    - ISO10991:multichannel_device
  LAYERED:
    text: LAYERED
    description: Layered/stacked channel architecture
    exact_mappings:
    - ISO10991:multilayer_device
  RADIAL:
    text: RADIAL
    description: Radial channel architecture
    exact_mappings:
    - ISO10991:radial_flow_device
  NETWORK:
    text: NETWORK
    description: Network of interconnected channels
    exact_mappings:
    - ISO10991:microfluidic_network

```
</details>