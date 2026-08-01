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
| [Gene](Gene.md) | A gene entity with identifiers and expression information |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Gene](Gene.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Gene](Gene.md) |












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
owner: Gene
domain_of:
- Gene
range: float

```
</details></div>