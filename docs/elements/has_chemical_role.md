---
search:
  boost: 5.0
---

# Slot: has_chemical_role 


_A role is particular behaviour which a chemical entity may exhibit._



<div data-search-exclude markdown="1">



URI: [namo:has_chemical_role](https://w3id.org/monarch-initiative/namo/has_chemical_role)
Alias: has_chemical_role


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **has_chemical_role**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |  no  |
| [MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently ... |  no  |
| [SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |  no  |
| [ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |  no  |
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |  no  |
| [MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |  no  |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |  no  |
| [ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional... |  no  |
| [Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, o... |  no  |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | Any unwanted chemical in food |  no  |
| [FoodAdditive](FoodAdditive.md) | Any substance which is added to food to preserve or enhance its flavour and/o... |  no  |
| [Food](Food.md) | A substance of plant, animal, or artificial origin consumed by a living organ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalRole](ChemicalRole.md) |
| Domain | [ChemicalEntity](ChemicalEntity.md) |
| Domain Of | [ChemicalEntity](ChemicalEntity.md) |

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
| Inverse | [is_chemical_role_of](is_chemical_role_of.md) |

</details>









## Comments

* We expect primarily to use CHEBI chemical roles here; however, we are looking for a mapping between CHEBI And ATC codes to support this slot.



## Identifier and Mapping Information

### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEBI







### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_chemical_role |
| native | namo:has_chemical_role |




## LinkML Source

<details>
```yaml
name: has chemical role
id_prefixes:
- CHEBI
description: A role is particular behaviour which a chemical entity may exhibit.
comments:
- We expect primarily to use CHEBI chemical roles here; however, we are looking for
  a mapping between CHEBI And ATC codes to support this slot.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at concept level
domain: chemical entity
inherited: true
alias: has_chemical_role
domain_of:
- chemical entity
inverse: is chemical role of
range: chemical role
multivalued: true

```
</details></div>