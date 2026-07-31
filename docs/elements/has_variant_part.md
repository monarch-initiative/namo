---
search:
  boost: 5.0
---

# Slot: has_variant_part 


_holds between a nucleic acid entity and a nucleic acid entity that is a sub-component of it_



<div data-search-exclude markdown="1">



URI: [namo:has_variant_part](https://w3id.org/monarch-initiative/namo/has_variant_part)
Alias: has_variant_part


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_variant_part**








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
| self | namo:has_variant_part |
| native | namo:has_variant_part |
| exact | GENO:0000382 |




## LinkML Source

<details>
```yaml
name: has variant part
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a nucleic acid entity and a nucleic acid entity that is
  a sub-component of it
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- GENO:0000382
rank: 1000
is_a: has part
domain: named thing
inherited: true
alias: has_variant_part
range: named thing
multivalued: true

```
</details></div>