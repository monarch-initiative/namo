---
search:
  boost: 5.0
---

# Slot: nutrient_of 


_holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive)_



<div data-search-exclude markdown="1">



URI: [namo:nutrient_of](https://w3id.org/monarch-initiative/namo/nutrient_of)
Alias: nutrient_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [part_of](part_of.md)
                * [food_component_of](food_component_of.md)
                    * **nutrient_of**








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
| Inverse | [has_nutrient](has_nutrient.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:nutrient_of |
| native | namo:nutrient_of |




## LinkML Source

<details>
```yaml
name: nutrient of
description: holds between a one or more chemical entities present in food, irrespective
  of nutritional value (i.e. could also be a contaminant or additive)
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: food component of
domain: chemical entity
inherited: true
alias: nutrient_of
inverse: has nutrient
range: chemical entity
multivalued: true

```
</details></div>