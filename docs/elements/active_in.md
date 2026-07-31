---
search:
  boost: 5.0
---

# Slot: active_in 


_Holds between a gene or gene product and a cellular component in which it carries out its molecular function._



<div data-search-exclude markdown="1">



URI: [namo:active_in](https://w3id.org/monarch-initiative/namo/active_in)
Alias: active_in


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **active_in**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CellularComponent](CellularComponent.md) |
| Domain | [GeneOrGeneProduct](GeneOrGeneProduct.md) |

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
| self | namo:active_in |
| native | namo:active_in |
| exact | RO:0002432 |




## LinkML Source

<details>
```yaml
name: active in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a gene or gene product and a cellular component in which
  it carries out its molecular function.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002432
rank: 1000
is_a: related to at instance level
domain: gene or gene product
inherited: true
alias: active_in
range: cellular component
multivalued: true

```
</details></div>