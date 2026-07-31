---
search:
  boost: 5.0
---

# Slot: expressed_in 


_holds between a gene or gene product and an anatomical entity in which it is expressed_



<div data-search-exclude markdown="1">



URI: [namo:expressed_in](https://w3id.org/monarch-initiative/namo/expressed_in)
Alias: expressed_in


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [located_in](located_in.md)
            * **expressed_in**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AnatomicalEntity](AnatomicalEntity.md) |
| Domain | [GeneOrGeneProduct](GeneOrGeneProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:expressed_in |
| native | namo:expressed_in |
| exact | RO:0002206 |
| narrow | NCIT:R49, NCIT:R46 |




## LinkML Source

<details>
```yaml
name: expressed in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a gene or gene product and an anatomical entity in which
  it is expressed
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002206
narrow_mappings:
- NCIT:R49
- NCIT:R46
rank: 1000
is_a: located in
domain: gene or gene product
inherited: true
alias: expressed_in
range: anatomical entity
multivalued: true

```
</details></div>