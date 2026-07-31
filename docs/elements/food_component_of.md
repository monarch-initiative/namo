---
search:
  boost: 5.0
---

# Slot: food_component_of 


_holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive)_



<div data-search-exclude markdown="1">



URI: [namo:food_component_of](https://w3id.org/monarch-initiative/namo/food_component_of)
Alias: food_component_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [part_of](part_of.md)
                * **food_component_of**
                    * [nutrient_of](nutrient_of.md)








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


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [has_food_component](has_food_component.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:food_component_of |
| native | namo:food_component_of |




## LinkML Source

<details>
```yaml
name: food component of
description: holds between a one or more chemical entities present in food, irrespective
  of nutritional value (i.e. could also be a contaminant or additive)
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: part of
domain: chemical entity
inherited: true
alias: food_component_of
inverse: has food component
range: chemical entity
multivalued: true

```
</details></div>