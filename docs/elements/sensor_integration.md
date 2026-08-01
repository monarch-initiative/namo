---
search:
  boost: 5.0
---

# Slot: sensor_integration 


_Sensors integrated for real-time monitoring_



<div data-search-exclude markdown="1">



URI: [namo:sensor_integration](https://w3id.org/monarch-initiative/namo/sensor_integration)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MicrophysiologicalSystem](MicrophysiologicalSystem.md) | Organ-/tissue-on-chip systems that integrate microfluidics, biomaterials, and... |  no  |
| [OrganOnChip](OrganOnChip.md) | A model system that simulates the physiological functions of an organ using a... |  no  |
| [TissueOnChip](TissueOnChip.md) | Tissue-level microphysiological systems that model specific tissue functions ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IntegratedSensorEnum](IntegratedSensorEnum.md) |
| Domain Of | [MicrophysiologicalSystem](MicrophysiologicalSystem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MicrophysiologicalSystem](MicrophysiologicalSystem.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:sensor_integration |
| native | namo:sensor_integration |




## LinkML Source

<details>
```yaml
name: sensor_integration
description: Sensors integrated for real-time monitoring
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: MicrophysiologicalSystem
domain_of:
- MicrophysiologicalSystem
range: IntegratedSensorEnum
multivalued: true

```
</details></div>