---
search:
  boost: 5.0
---

# Slot: has_food_component 


_holds between food and one or more chemical entities composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)_



<div data-search-exclude markdown="1">



URI: [namo:has_food_component](https://w3id.org/monarch-initiative/namo/has_food_component)
Alias: has_food_component


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_food_component**
                    * [has_nutrient](has_nutrient.md)








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
| self | namo:has_food_component |
| native | namo:has_food_component |




## LinkML Source

<details>
```yaml
name: has food component
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between food and one or more chemical entities composing it, irrespective
  of nutritional value (i.e. could also be a contaminant or additive)
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has part
domain: chemical entity
inherited: true
alias: has_food_component
range: chemical entity
multivalued: true

```
</details></div>