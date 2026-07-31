---
search:
  boost: 5.0
---

# Slot: anatomical_structure_modeled 


_The anatomical structure being modeled — a tissue, organ, or other multicellular structure._



<div data-search-exclude markdown="1">



URI: [namo:anatomical_structure_modeled](https://w3id.org/monarch-initiative/namo/anatomical_structure_modeled)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TissueOnChip](TissueOnChip.md) | Tissue-level microphysiological systems that model specific tissue functions ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GrossAnatomicalStructure](GrossAnatomicalStructure.md) |
| Domain Of | [TissueOnChip](TissueOnChip.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [TissueOnChip](TissueOnChip.md) |


<details>
<summary>Advanced Properties</summary>
**Term Bindings:**
- EnumBinding({
  'range': 'AnatomicalStructureEnum',
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
| self | namo:anatomical_structure_modeled |
| native | namo:anatomical_structure_modeled |




## LinkML Source

<details>
```yaml
name: anatomical_structure_modeled
description: The anatomical structure being modeled — a tissue, organ, or other multicellular
  structure.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: TissueOnChip
domain_of:
- TissueOnChip
range: gross anatomical structure
bindings:
- range: AnatomicalStructureEnum
  obligation_level: REQUIRED
  binds_value_of: id
inlined: true

```
</details></div>