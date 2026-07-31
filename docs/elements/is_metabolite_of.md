---
search:
  boost: 5.0
---

# Slot: is_metabolite_of 


_holds between two molecular entities in which the first one is derived from the second one as a product of metabolism_



<div data-search-exclude markdown="1">



URI: [namo:is_metabolite_of](https://w3id.org/monarch-initiative/namo/is_metabolite_of)
Alias: is_metabolite_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [derives_from](derives_from.md)
            * **is_metabolite_of**








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


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [has_metabolite](has_metabolite.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)




## Comments

* The CHEBI ID represents a role rather than a predicate



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_metabolite_of |
| native | namo:is_metabolite_of |
| exact | CHEBI:25212 |




## LinkML Source

<details>
```yaml
name: is metabolite of
description: holds between two molecular entities in which the first one is derived
  from the second one as a product of metabolism
comments:
- The CHEBI ID represents a role rather than a predicate
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- CHEBI:25212
rank: 1000
is_a: derives from
domain: molecular entity
inherited: true
alias: is_metabolite_of
inverse: has metabolite
range: molecular entity
multivalued: true

```
</details></div>