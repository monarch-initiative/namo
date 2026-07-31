---
search:
  boost: 5.0
---

# Slot: expresses 


_holds between an anatomical entity and gene or gene product that is expressed there_



<div data-search-exclude markdown="1">



URI: [namo:expresses](https://w3id.org/monarch-initiative/namo/expresses)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [location_of](location_of.md)
            * **expresses**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneOrGeneProduct](GeneOrGeneProduct.md) |
| Domain | [AnatomicalEntity](AnatomicalEntity.md) |

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
| Inverse | [expressed_in](expressed_in.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)



## Aliases


* anatomy expresses gene




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:expresses |
| native | namo:expresses |
| exact | RO:0002292 |




## LinkML Source

<details>
```yaml
name: expresses
description: holds between an anatomical entity and gene or gene product that is expressed
  there
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- anatomy expresses gene
exact_mappings:
- RO:0002292
rank: 1000
is_a: location of
domain: anatomical entity
inherited: true
inverse: expressed in
range: gene or gene product
multivalued: true

```
</details></div>