---
search:
  boost: 5.0
---

# Slot: channel_configuration 


_Configuration of channels (e.g., parallel, serial, branching)_



<div data-search-exclude markdown="1">



URI: [namo:channel_configuration](https://w3id.org/monarch-initiative/namo/channel_configuration)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MicrofluidicDesign](MicrofluidicDesign.md) | Detailed specification of a microfluidic device design including its architec... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChannelConfigurationEnum](ChannelConfigurationEnum.md) |
| Domain Of | [MicrofluidicDesign](MicrofluidicDesign.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MicrofluidicDesign](MicrofluidicDesign.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:channel_configuration |
| native | namo:channel_configuration |




## LinkML Source

<details>
```yaml
name: channel_configuration
description: Configuration of channels (e.g., parallel, serial, branching)
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: MicrofluidicDesign
domain_of:
- MicrofluidicDesign
range: ChannelConfigurationEnum
multivalued: true

```
</details></div>