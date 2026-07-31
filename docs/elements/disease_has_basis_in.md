---
search:
  boost: 5.0
---

# Slot: disease_has_basis_in 


_A relation that holds between a disease and an entity where the state of the entity has contribution to the disease._



<div data-search-exclude markdown="1">



URI: [namo:disease_has_basis_in](https://w3id.org/monarch-initiative/namo/disease_has_basis_in)
Alias: disease_has_basis_in


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **disease_has_basis_in**








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




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:disease_has_basis_in |
| native | namo:disease_has_basis_in |
| narrow | MONDO:disease_has_basis_in_development_of, MONDO:disease_has_basis_in_accumulation_of |




## LinkML Source

<details>
```yaml
name: disease has basis in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A relation that holds between a disease and an entity where the state
  of the entity has contribution to the disease.
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- MONDO:disease_has_basis_in_development_of
- MONDO:disease_has_basis_in_accumulation_of
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: disease_has_basis_in
range: named thing
multivalued: true

```
</details></div>