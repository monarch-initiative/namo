---
search:
  boost: 5.0
---

# Slot: strain 


_The specific strain of the animal used in the model system. Deliberately unconstrained beyond the class: LinkML dynamic enums cannot filter by taxonomic rank, so any NCBITaxon-rooted enum would be indistinguishable from SpeciesEnum._



<div data-search-exclude markdown="1">



URI: [namo:strain](https://w3id.org/monarch-initiative/namo/strain)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnimalModel](AnimalModel.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OrganismTaxon](OrganismTaxon.md) |
| Domain Of | [AnimalModel](AnimalModel.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnimalModel](AnimalModel.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:strain |
| native | namo:strain |




## LinkML Source

<details>
```yaml
name: strain
description: 'The specific strain of the animal used in the model system. Deliberately
  unconstrained beyond the class: LinkML dynamic enums cannot filter by taxonomic
  rank, so any NCBITaxon-rooted enum would be indistinguishable from SpeciesEnum.'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: AnimalModel
domain_of:
- AnimalModel
range: OrganismTaxon
inlined: true

```
</details></div>