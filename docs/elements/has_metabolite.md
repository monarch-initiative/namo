---
search:
  boost: 5.0
---

# Slot: has_metabolite 


_holds between two molecular entities in which the second one is derived from the first one as a product of metabolism_



<div data-search-exclude markdown="1">



URI: [namo:has_metabolite](https://w3id.org/monarch-initiative/namo/has_metabolite)
Alias: has_metabolite


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [derives_into](derives_into.md)
            * **has_metabolite**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MolecularEntity](MolecularEntity.md) |
| Domain | [MolecularEntity](MolecularEntity.md) |

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




## Comments

* The CHEBI ID represents a role rather than a predicate



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
| self | namo:has_metabolite |
| native | namo:has_metabolite |
| exact | CHEBI:25212 |




## LinkML Source

<details>
```yaml
name: has metabolite
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two molecular entities in which the second one is derived
  from the first one as a product of metabolism
comments:
- The CHEBI ID represents a role rather than a predicate
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- CHEBI:25212
rank: 1000
is_a: derives into
domain: molecular entity
inherited: true
alias: has_metabolite
range: molecular entity
multivalued: true

```
</details></div>