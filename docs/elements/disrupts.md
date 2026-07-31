---
search:
  boost: 5.0
---

# Slot: disrupts 


_describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another._



<div data-search-exclude markdown="1">



URI: [namo:disrupts](https://w3id.org/monarch-initiative/namo/disrupts)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **disrupts**








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








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* disease causes disruption of




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | enables |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:disrupts |
| native | namo:disrupts |
| exact | SEMMEDDB:DISRUPTS, CHEMBL.MECHANISM:disrupting_agent |
| narrow | RO:0004024, RO:0004025 |




## LinkML Source

<details>
```yaml
name: disrupts
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: enables
description: describes a relationship where one entity degrades or interferes with
  the structure, function, or occurrence of another.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- disease causes disruption of
exact_mappings:
- SEMMEDDB:DISRUPTS
- CHEMBL.MECHANISM:disrupting_agent
narrow_mappings:
- RO:0004024
- RO:0004025
rank: 1000
is_a: affects
domain: named thing
inherited: true
range: named thing
multivalued: true

```
</details></div>