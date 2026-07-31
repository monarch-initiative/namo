---
search:
  boost: 5.0
---

# Slot: target_for 


_A gene is a target of a disease when its products are druggable and when a drug interaction with the gene product could have a therapeutic effect_



<div data-search-exclude markdown="1">



URI: [namo:target_for](https://w3id.org/monarch-initiative/namo/target_for)
Alias: target_for


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **target_for**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Disease](Disease.md) |
| Domain | [Gene](Gene.md) |

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
| self | namo:target_for |
| native | namo:target_for |




## LinkML Source

<details>
```yaml
name: target for
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A gene is a target of a disease when its products are druggable and when
  a drug interaction with the gene product could have a therapeutic effect
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: gene
inherited: true
alias: target_for
range: disease
multivalued: true

```
</details></div>