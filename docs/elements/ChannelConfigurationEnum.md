# Enum: ChannelConfigurationEnum 




_Channel configurations for microfluidic devices aligned with ISO 22916:2022 interoperability requirements for dimensions and connections_



URI: [namo:ChannelConfigurationEnum](https://w3id.org/monarch-initiative/namo/ChannelConfigurationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PARALLEL | None | Parallel channel configuration |
| SERIAL | None | Serial/sequential channel configuration |
| BRANCHING | None | Branching channel configuration |
| CIRCULAR | None | Circular/loop channel configuration |
| SERPENTINE | None | Serpentine channel pattern |
| Y_SHAPED | None | Y-shaped channel junction |
| T_SHAPED | None | T-shaped channel junction |




## Slots

| Name | Description |
| ---  | --- |
| [channel_configuration](channel_configuration.md) | Configuration of channels (e |





## See Also

* [https://www.iso.org/standard/74157.html](https://www.iso.org/standard/74157.html)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo






## LinkML Source

<details>
```yaml
name: ChannelConfigurationEnum
description: Channel configurations for microfluidic devices aligned with ISO 22916:2022
  interoperability requirements for dimensions and connections
from_schema: https://w3id.org/monarch-initiative/namo
see_also:
- https://www.iso.org/standard/74157.html
rank: 1000
permissible_values:
  PARALLEL:
    text: PARALLEL
    description: Parallel channel configuration
    exact_mappings:
    - ISO22916:parallel_configuration
  SERIAL:
    text: SERIAL
    description: Serial/sequential channel configuration
    exact_mappings:
    - ISO22916:serial_configuration
  BRANCHING:
    text: BRANCHING
    description: Branching channel configuration
    exact_mappings:
    - ISO22916:branching_configuration
  CIRCULAR:
    text: CIRCULAR
    description: Circular/loop channel configuration
    exact_mappings:
    - ISO22916:circular_configuration
  SERPENTINE:
    text: SERPENTINE
    description: Serpentine channel pattern
    exact_mappings:
    - ISO22916:serpentine_configuration
  Y_SHAPED:
    text: Y_SHAPED
    description: Y-shaped channel junction
    exact_mappings:
    - ISO22916:y_junction
  T_SHAPED:
    text: T_SHAPED
    description: T-shaped channel junction
    exact_mappings:
    - ISO22916:t_junction

```
</details>