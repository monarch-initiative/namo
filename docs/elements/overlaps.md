---
search:
  boost: 5.0
---

# Slot: overlaps 


_holds between entities that overlap in their extents (materials or processes)_



<div data-search-exclude markdown="1">



URI: [namo:overlaps](https://w3id.org/monarch-initiative/namo/overlaps)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **overlaps**
            * [has_part](has_part.md)
            * [part_of](part_of.md)








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


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Symmetric | Yes |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






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
| self | namo:overlaps |
| native | namo:overlaps |
| exact | RO:0002131 |
| narrow | BSPO:0005001, CHEMBL.MECHANISM:overlaps_with, RO:0002100, RO:0002102, RO:0002433 |




## LinkML Source

<details>
```yaml
name: overlaps
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between entities that overlap in their extents (materials or processes)
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002131
narrow_mappings:
- BSPO:0005001
- CHEMBL.MECHANISM:overlaps_with
- RO:0002100
- RO:0002102
- RO:0002433
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
symmetric: true
range: named thing
multivalued: true

```
</details></div>