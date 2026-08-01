---
search:
  boost: 5.0
---

# Slot: biological_specific_phenotypes 


_List of phenotypes present only in the biological system._



<div data-search-exclude markdown="1">



URI: [namo:biological_specific_phenotypes](https://w3id.org/monarch-initiative/namo/biological_specific_phenotypes)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhenotypeOverlap](PhenotypeOverlap.md) | Comparison of phenotypic manifestations between model and biological systems |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhenotypicFeature](PhenotypicFeature.md) |
| Domain Of | [PhenotypeOverlap](PhenotypeOverlap.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhenotypeOverlap](PhenotypeOverlap.md) |


<details>
<summary>Advanced Properties</summary>
**Term Bindings:**
- EnumBinding({
  'range': 'PhenotypeEnum',
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
| self | namo:biological_specific_phenotypes |
| native | namo:biological_specific_phenotypes |




## LinkML Source

<details>
```yaml
name: biological_specific_phenotypes
description: List of phenotypes present only in the biological system.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PhenotypeOverlap
domain_of:
- PhenotypeOverlap
range: PhenotypicFeature
bindings:
- range: PhenotypeEnum
  obligation_level: REQUIRED
  binds_value_of: id
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>