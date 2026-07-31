---
search:
  boost: 5.0
---

# Slot: has_increased_amount 


_Holds between an entity and a component that is present at higher amount than in a reference state or sibling entity; used for comparative compositional statements._



<div data-search-exclude markdown="1">



URI: [namo:has_increased_amount](https://w3id.org/monarch-initiative/namo/has_increased_amount)
Alias: has_increased_amount


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_increased_amount**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [NamedThing](NamedThing.md) |

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
| opposite_of | has decreased amount |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_increased_amount |
| native | namo:has_increased_amount |
| narrow | CL:has_high_plasma_membrane_amount |




## LinkML Source

<details>
```yaml
name: has increased amount
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: has decreased amount
description: Holds between an entity and a component that is present at higher amount
  than in a reference state or sibling entity; used for comparative compositional
  statements.
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- CL:has_high_plasma_membrane_amount
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: has_increased_amount
range: named thing
multivalued: true

```
</details></div>