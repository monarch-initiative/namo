# Enum: MicrofluidicArchitectureEnum 



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





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: MicrofluidicArchitectureEnum
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
permissible_values:
  SINGLE_CHANNEL:
    text: SINGLE_CHANNEL
    description: Single channel design
  TWO_CHANNEL:
    text: TWO_CHANNEL
    description: Two-channel design with separated compartments
  MULTI_CHANNEL:
    text: MULTI_CHANNEL
    description: Multiple channels (>2) design
  LAYERED:
    text: LAYERED
    description: Layered/stacked channel architecture
  RADIAL:
    text: RADIAL
    description: Radial channel architecture
  NETWORK:
    text: NETWORK
    description: Network of interconnected channels

```
</details>