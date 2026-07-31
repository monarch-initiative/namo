---
search:
  boost: 5.0
---

# Slot: precedes 


_holds between two processes, where one completes before the other begins_



<div data-search-exclude markdown="1">



URI: [namo:precedes](https://w3id.org/monarch-initiative/namo/precedes)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [temporally_related_to](temporally_related_to.md)
            * **precedes**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Occurrent](Occurrent.md) |
| Domain | [Occurrent](Occurrent.md) |

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
| self | namo:precedes |
| native | namo:precedes |
| exact | BFO:0000063, SEMMEDDB:PRECEDES, SNOMED:occurs_before |
| narrow | FMA:transforms_into, RO:0002090, RO:0002411, RO:0002412 |
| broad | WIKIDATA_PROPERTY:P156 |
| close | RO:0002263, RO:0002264 |




## LinkML Source

<details>
```yaml
name: precedes
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two processes, where one completes before the other begins
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- BFO:0000063
- SEMMEDDB:PRECEDES
- SNOMED:occurs_before
close_mappings:
- RO:0002263
- RO:0002264
narrow_mappings:
- FMA:transforms_into
- RO:0002090
- RO:0002411
- RO:0002412
broad_mappings:
- WIKIDATA_PROPERTY:P156
rank: 1000
is_a: temporally related to
domain: occurrent
inherited: true
range: occurrent
multivalued: true

```
</details></div>