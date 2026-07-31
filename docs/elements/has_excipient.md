---
search:
  boost: 5.0
---

# Slot: has_excipient 


_holds between a drug and a molecular entities in which the latter is a part of the former, and is a biologically inactive component_



<div data-search-exclude markdown="1">



URI: [namo:has_excipient](https://w3id.org/monarch-initiative/namo/has_excipient)
Alias: has_excipient


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_excipient**








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




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_excipient |
| native | namo:has_excipient |
| undefined | WIKIDATA:Q902638 |




## LinkML Source

<details>
```yaml
name: has excipient
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a drug and a molecular entities in which the latter is
  a part of the former, and is a biologically inactive component
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
mappings:
- WIKIDATA:Q902638
rank: 1000
is_a: has part
domain: drug
inherited: true
alias: has_excipient
range: molecular entity
multivalued: true

```
</details></div>