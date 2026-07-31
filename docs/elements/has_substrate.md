---
search:
  boost: 5.0
---

# Slot: has_substrate 


_Holds between a biochemical reaction or catalytic process and a chemical entity that is acted upon (consumed or transformed) by that reaction._



<div data-search-exclude markdown="1">



URI: [namo:has_substrate](https://w3id.org/monarch-initiative/namo/has_substrate)
Alias: has_substrate


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * **has_substrate**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |
| Domain | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |












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
| self | namo:has_substrate |
| native | namo:has_substrate |




## LinkML Source

<details>
```yaml
name: has substrate
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a biochemical reaction or catalytic process and a chemical
  entity that is acted upon (consumed or transformed) by that reaction.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has participant
domain: chemical entity or gene or gene product
inherited: true
alias: has_substrate
range: chemical entity or gene or gene product
multivalued: true

```
</details></div>