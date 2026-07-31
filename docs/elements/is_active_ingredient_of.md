---
search:
  boost: 5.0
---

# Slot: is_active_ingredient_of 


_holds between a molecular entity and a drug, in which the former is a part of the latter, and is a biologically active component_



<div data-search-exclude markdown="1">



URI: [namo:is_active_ingredient_of](https://w3id.org/monarch-initiative/namo/is_active_ingredient_of)
Alias: is_active_ingredient_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [part_of](part_of.md)
                * **is_active_ingredient_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Drug](Drug.md) |
| Domain | [MolecularEntity](MolecularEntity.md) |

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
| Inverse | [has_active_ingredient](has_active_ingredient.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_active_ingredient_of |
| native | namo:is_active_ingredient_of |
| undefined | RO:0002249 |




## LinkML Source

<details>
```yaml
name: is active ingredient of
description: holds between a molecular entity and a drug, in which the former is a
  part of the latter, and is a biologically active component
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
mappings:
- RO:0002249
rank: 1000
is_a: part of
domain: molecular entity
inherited: true
alias: is_active_ingredient_of
inverse: has active ingredient
range: drug
multivalued: true

```
</details></div>