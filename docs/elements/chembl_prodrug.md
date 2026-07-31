---
search:
  boost: 5.0
---

# Slot: chembl_prodrug 


_Flag indicating if a drug is a prodrug that is active only after being metabolized by the body._



<div data-search-exclude markdown="1">



URI: [namo:chembl_prodrug](https://w3id.org/monarch-initiative/namo/chembl_prodrug)
Alias: chembl_prodrug

<!-- no inheritance hierarchy -->





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
| self | namo:chembl_prodrug |
| native | namo:chembl_prodrug |




## LinkML Source

<details>
```yaml
name: chembl prodrug
description: Flag indicating if a drug is a prodrug that is active only after being
  metabolized by the body.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: chembl_prodrug
domain_of:
- chemical entity
range: boolean

```
</details></div>