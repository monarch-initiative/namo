---
search:
  boost: 5.0
---

# Slot: species_modeled 


_Species for which the model is designed_



<div data-search-exclude markdown="1">



URI: [namo:species_modeled](https://w3id.org/monarch-initiative/namo/species_modeled)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PBPKModel](PBPKModel.md) | Physiologically Based Pharmacokinetic models that simulate drug absorption, d... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OrganismTaxon](OrganismTaxon.md) |
| Domain Of | [PBPKModel](PBPKModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | namo:species_modeled |
| native | namo:species_modeled |




## LinkML Source

<details>
```yaml
name: species_modeled
description: Species for which the model is designed
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PBPKModel
domain_of:
- PBPKModel
range: organism taxon
inlined: true

```
</details></div>