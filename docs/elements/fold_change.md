---
search:
  boost: 5.0
---

# Slot: fold_change 


_Fold change in expression compared to control or reference._



<div data-search-exclude markdown="1">



URI: [namo:fold_change](https://w3id.org/monarch-initiative/namo/fold_change)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneExpressionResult](GeneExpressionResult.md) | A differential-expression measurement for a single gene in a model system |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [GeneExpressionResult](GeneExpressionResult.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GeneExpressionResult](GeneExpressionResult.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:fold_change |
| native | namo:fold_change |




## LinkML Source

<details>
```yaml
name: fold_change
description: Fold change in expression compared to control or reference.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: GeneExpressionResult
domain_of:
- GeneExpressionResult
range: float

```
</details></div>