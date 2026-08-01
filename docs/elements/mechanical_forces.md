---
search:
  boost: 5.0
---

# Slot: mechanical_forces 


_Mechanical forces applied to the model system_



<div data-search-exclude markdown="1">



URI: [namo:mechanical_forces](https://w3id.org/monarch-initiative/namo/mechanical_forces)
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
| Range | [MechanicalStimulation](MechanicalStimulation.md) |
| Domain Of | [MicrophysiologicalSystem](MicrophysiologicalSystem.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | namo:mechanical_forces |
| native | namo:mechanical_forces |




## LinkML Source

<details>
```yaml
name: mechanical_forces
description: Mechanical forces applied to the model system
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: MicrophysiologicalSystem
domain_of:
- MicrophysiologicalSystem
range: MechanicalStimulation
inlined: true

```
</details></div>