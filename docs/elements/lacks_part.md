---
search:
  boost: 5.0
---

# Slot: lacks_part 


_Holds between an entity and a component that is absent from it relative to a reference type; for example a cell type lacking a particular organelle or a protein lacking a particular domain. Corresponds to CL:lacks_part / PR:lacks_part._



<div data-search-exclude markdown="1">



URI: [namo:lacks_part](https://w3id.org/monarch-initiative/namo/lacks_part)
Alias: lacks_part


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **lacks_part**








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
| opposite_of | has part |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:lacks_part |
| native | namo:lacks_part |
| exact | CL:lacks_part, PR:lacks_part |
| narrow | CL:lacks_plasma_membrane_part |




## LinkML Source

<details>
```yaml
name: lacks part
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: has part
description: Holds between an entity and a component that is absent from it relative
  to a reference type; for example a cell type lacking a particular organelle or a
  protein lacking a particular domain. Corresponds to CL:lacks_part / PR:lacks_part.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- CL:lacks_part
- PR:lacks_part
narrow_mappings:
- CL:lacks_plasma_membrane_part
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: lacks_part
range: named thing
multivalued: true

```
</details></div>