---
search:
  boost: 5.0
---

# Slot: is_chemical_role_of 


_Holds between a chemical role and a chemical entity that exhibits that role._



<div data-search-exclude markdown="1">



URI: [namo:is_chemical_role_of](https://w3id.org/monarch-initiative/namo/is_chemical_role_of)
Alias: is_chemical_role_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **is_chemical_role_of**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalEntity](ChemicalEntity.md) |
| Domain | [ChemicalRole](ChemicalRole.md) |

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
| Inverse | [has_chemical_role](has_chemical_role.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_chemical_role_of |
| native | namo:is_chemical_role_of |




## LinkML Source

<details>
```yaml
name: is chemical role of
description: Holds between a chemical role and a chemical entity that exhibits that
  role.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at concept level
domain: chemical role
inherited: true
alias: is_chemical_role_of
inverse: has chemical role
range: chemical entity
multivalued: true

```
</details></div>