---
search:
  boost: 5.0
---

# Slot: species 


_The species of the animal used in the model system._



<div data-search-exclude markdown="1">



URI: [namo:species](https://w3id.org/monarch-initiative/namo/species)
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
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnimalModel](AnimalModel.md) |


<details>
<summary>Advanced Properties</summary>
**Term Bindings:**
- EnumBinding({
  'range': 'SpeciesEnum',
  'obligation_level': ObligationLevelEnum(text='REQUIRED', description='The metadata element is required to be present in the model'),
  'binds_value_of': 'id'
})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:species |
| native | namo:species |




## LinkML Source

<details>
```yaml
name: species
description: The species of the animal used in the model system.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: AnimalModel
domain_of:
- AnimalModel
range: OrganismTaxon
bindings:
- range: SpeciesEnum
  obligation_level: REQUIRED
  binds_value_of: id
required: true
inlined: true

```
</details></div>