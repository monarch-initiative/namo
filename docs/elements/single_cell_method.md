---
search:
  boost: 5.0
---

# Slot: single_cell_method 


_Method used for single-cell analysis (e.g., scRNA-seq, flow cytometry)._



<div data-search-exclude markdown="1">



URI: [namo:single_cell_method](https://w3id.org/monarch-initiative/namo/single_cell_method)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CellTypeCoverage](CellTypeCoverage.md) | Assessment of cell type representation and cellular diversity between systems |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CellTypeCoverage](CellTypeCoverage.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [CellTypeCoverage](CellTypeCoverage.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:single_cell_method |
| native | namo:single_cell_method |




## LinkML Source

<details>
```yaml
name: single_cell_method
description: Method used for single-cell analysis (e.g., scRNA-seq, flow cytometry).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: CellTypeCoverage
domain_of:
- CellTypeCoverage
range: string

```
</details></div>