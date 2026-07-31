---
search:
  boost: 5.0
---

# Slot: has_active_ingredient 


_holds between a drug and a molecular entity in which the latter is a part of the former, and is a biologically active component_



<div data-search-exclude markdown="1">



URI: [namo:has_active_ingredient](https://w3id.org/monarch-initiative/namo/has_active_ingredient)
Alias: has_active_ingredient


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_active_ingredient**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MolecularEntity](MolecularEntity.md) |
| Domain | [Drug](Drug.md) |

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
| opposite_of | is excipient of |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_active_ingredient |
| native | namo:has_active_ingredient |
| undefined | RO:0002248 |




## LinkML Source

<details>
```yaml
name: has active ingredient
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: is excipient of
description: holds between a drug and a molecular entity in which the latter is a
  part of the former, and is a biologically active component
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
mappings:
- RO:0002248
rank: 1000
is_a: has part
domain: drug
inherited: true
alias: has_active_ingredient
range: molecular entity
multivalued: true

```
</details></div>