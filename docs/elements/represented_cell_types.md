---
search:
  boost: 5.0
---

# Slot: represented_cell_types 


_List of cell types present in both model and biological system._



<div data-search-exclude markdown="1">



URI: [namo:represented_cell_types](https://w3id.org/monarch-initiative/namo/represented_cell_types)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CellTypeCoverage](CellTypeCoverage.md) | Assessment of cell type representation and cellular diversity between systems |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Cell](Cell.md) |
| Domain Of | [CellTypeCoverage](CellTypeCoverage.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CellTypeCoverage](CellTypeCoverage.md) |


<details>
<summary>Advanced Properties</summary>
**Term Bindings:**
- EnumBinding({
  'range': 'CellTypeEnum',
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
| self | namo:represented_cell_types |
| native | namo:represented_cell_types |




## LinkML Source

<details>
```yaml
name: represented_cell_types
description: List of cell types present in both model and biological system.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: CellTypeCoverage
domain_of:
- CellTypeCoverage
range: Cell
bindings:
- range: CellTypeEnum
  obligation_level: REQUIRED
  binds_value_of: id
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>