---
search:
  boost: 5.0
---

# Slot: is_supplement 


_A boolean or categorical flag indicating that a chemical mixture is marketed, formulated, or used as a dietary or nutritional supplement rather than as a conventional drug or food._



<div data-search-exclude markdown="1">



URI: [namo:is_supplement](https://w3id.org/monarch-initiative/namo/is_supplement)
Alias: is_supplement


## Inheritance

* [node_property](node_property.md)
    * **is_supplement**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |  no  |
| [MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |  no  |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |  no  |
| [ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional... |  no  |
| [Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, o... |  no  |
| [Food](Food.md) | A substance of plant, animal, or artificial origin consumed by a living organ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [ChemicalMixture](ChemicalMixture.md) |
| Domain Of | [ChemicalMixture](ChemicalMixture.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_supplement |
| native | namo:is_supplement |




## LinkML Source

<details>
```yaml
name: is supplement
description: A boolean or categorical flag indicating that a chemical mixture is marketed,
  formulated, or used as a dietary or nutritional supplement rather than as a conventional
  drug or food.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: chemical mixture
alias: is_supplement
domain_of:
- chemical mixture
range: string

```
</details></div>