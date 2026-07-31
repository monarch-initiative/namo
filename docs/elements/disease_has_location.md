---
search:
  boost: 5.0
---

# Slot: disease_has_location 


_A relationship between a disease and an anatomical entity where the disease has one or more features that are located in that entity._



<div data-search-exclude markdown="1">



URI: [namo:disease_has_location](https://w3id.org/monarch-initiative/namo/disease_has_location)
Alias: disease_has_location


## Inheritance

* [related_to](related_to.md)
    * **disease_has_location**








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





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:disease_has_location |
| native | namo:disease_has_location |
| exact | RO:0004026, MONDO:disease_has_location |




## LinkML Source

<details>
```yaml
name: disease has location
description: A relationship between a disease and an anatomical entity where the disease
  has one or more features that are located in that entity.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0004026
- MONDO:disease_has_location
rank: 1000
is_a: related to
domain: named thing
inherited: true
alias: disease_has_location
range: named thing
multivalued: true

```
</details></div>