---
search:
  boost: 5.0
---

# Slot: z_score 


_A measure of the divergence of an individual experimental result from the most probable result, the mean. Z is expressed in terms of the number of standard deviations from the mean value._



<div data-search-exclude markdown="1">



URI: [namo:z_score](https://w3id.org/monarch-initiative/namo/z_score)
Alias: z_score


## Inheritance

* [association_slot](association_slot.md)
    * **z_score**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease for which the g... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain | [Association](Association.md) |
| Domain Of | [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* z-score
* z-value
* standard score
* normal score




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:z_score |
| native | namo:z_score |
| exact | STATO:0000104, NCIT:C68741, EDAM-DATA:1668 |




## LinkML Source

<details>
```yaml
name: z score
description: A measure of the divergence of an individual experimental result from
  the most probable result, the mean. Z is expressed in terms of the number of standard
  deviations from the mean value.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- z-score
- z-value
- standard score
- normal score
exact_mappings:
- STATO:0000104
- NCIT:C68741
- EDAM-DATA:1668
rank: 1000
is_a: association slot
domain: association
alias: z_score
domain_of:
- correlated gene to disease association
range: float

```
</details></div>