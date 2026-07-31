---
search:
  boost: 5.0
---

# Slot: is_toxic 


_A boolean flag indicating whether a chemical entity is toxic under ordinary conditions of exposure._



<div data-search-exclude markdown="1">



URI: [namo:is_toxic](https://w3id.org/monarch-initiative/namo/is_toxic)
Alias: is_toxic


## Inheritance

* [node_property](node_property.md)
    * **is_toxic**






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
| Range | [Boolean](Boolean.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [ChemicalEntity](ChemicalEntity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_toxic |
| native | namo:is_toxic |




## LinkML Source

<details>
```yaml
name: is toxic
description: A boolean flag indicating whether a chemical entity is toxic under ordinary
  conditions of exposure.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: named thing
alias: is_toxic
domain_of:
- chemical entity
range: boolean
multivalued: false

```
</details></div>