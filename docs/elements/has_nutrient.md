---
search:
  boost: 5.0
---

# Slot: has_nutrient 


_one or more nutrients which are growth factors for a living organism_



<div data-search-exclude markdown="1">



URI: [namo:has_nutrient](https://w3id.org/monarch-initiative/namo/has_nutrient)
Alias: has_nutrient


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * [has_food_component](has_food_component.md)
                    * **has_nutrient**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalEntity](ChemicalEntity.md) |
| Domain | [ChemicalEntity](ChemicalEntity.md) |

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
| self | namo:has_nutrient |
| native | namo:has_nutrient |
| exact | WIKIDATA:Q181394 |




## LinkML Source

<details>
```yaml
name: has nutrient
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: one or more nutrients which are growth factors for a living organism
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA:Q181394
rank: 1000
is_a: has food component
domain: chemical entity
inherited: true
alias: has_nutrient
range: chemical entity
multivalued: true

```
</details></div>