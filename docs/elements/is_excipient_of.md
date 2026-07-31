---
search:
  boost: 5.0
---

# Slot: is_excipient_of 


_holds between a molecular entity and a drug in which the former is a part of the latter, and is a biologically inactive component_



<div data-search-exclude markdown="1">



URI: [namo:is_excipient_of](https://w3id.org/monarch-initiative/namo/is_excipient_of)
Alias: is_excipient_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [part_of](part_of.md)
                * **is_excipient_of**








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
| Inverse | [has_excipient](has_excipient.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_excipient_of |
| native | namo:is_excipient_of |
| undefined | WIKIDATA:Q902638 |




## LinkML Source

<details>
```yaml
name: is excipient of
description: holds between a molecular entity and a drug in which the former is a
  part of the latter, and is a biologically inactive component
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
mappings:
- WIKIDATA:Q902638
rank: 1000
is_a: part of
domain: molecular entity
inherited: true
alias: is_excipient_of
inverse: has excipient
range: drug
multivalued: true

```
</details></div>