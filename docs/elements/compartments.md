---
search:
  boost: 5.0
---

# Slot: compartments 


_Physiological compartments included in the model_



<div data-search-exclude markdown="1">



URI: [namo:compartments](https://w3id.org/monarch-initiative/namo/compartments)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug absorption, d... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PBPKCompartment](PBPKCompartment.md) |
| Domain Of | [PBPKModel](PBPKModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PBPKModel](PBPKModel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:compartments |
| native | namo:compartments |




## LinkML Source

<details>
```yaml
name: compartments
description: Physiological compartments included in the model
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PBPKModel
domain_of:
- PBPKModel
range: PBPKCompartment
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>