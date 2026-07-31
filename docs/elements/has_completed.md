---
search:
  boost: 5.0
---

# Slot: has_completed 


_holds between an entity and a process that the entity is capable of and has completed_



<div data-search-exclude markdown="1">



URI: [namo:has_completed](https://w3id.org/monarch-initiative/namo/has_completed)
Alias: has_completed


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_completed**








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
| opposite_of | has not completed |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_completed |
| native | namo:has_completed |
| exact | CL:has_completed |




## LinkML Source

<details>
```yaml
name: has completed
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: has not completed
description: holds between an entity and a process that the entity is capable of and
  has completed
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- CL:has_completed
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: has_completed
range: named thing
multivalued: true

```
</details></div>