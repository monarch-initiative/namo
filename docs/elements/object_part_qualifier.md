---
search:
  boost: 5.0
---

# Slot: object_part_qualifier 


_defines a specific part/component of the core concept (used in cases there this specific part has no IRI we can use to directly represent it).  This qualifier is for the object of an association (or statement)._



<div data-search-exclude markdown="1">



URI: [namo:object_part_qualifier](https://w3id.org/monarch-initiative/namo/object_part_qualifier)
Alias: object_part_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [part_qualifier](part_qualifier.md)
            * **object_part_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |  yes  |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | Describes the relationship between an enzyme (usually a macromolecular comple... |  no  |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | Describes an effect that a chemical has on a biological entity (e |  yes  |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | Describes a relationship in which a chemical entity affects the sensitivity o... |  yes  |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | Describes an effect that a gene or gene product has on a chemical entity (e |  yes  |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |
| Domain Of | [PredicateMapping](PredicateMapping.md), [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md), [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md), [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md), [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md), [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)





## Examples

| Value |
| --- |
| polyA tail |
| upstream control region |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:object_part_qualifier |
| native | namo:object_part_qualifier |




## LinkML Source

<details>
```yaml
name: object part qualifier
description: defines a specific part/component of the core concept (used in cases
  there this specific part has no IRI we can use to directly represent it).  This
  qualifier is for the object of an association (or statement).
examples:
- value: polyA tail
- value: upstream control region
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: part qualifier
domain: association
alias: object_part_qualifier
domain_of:
- predicate mapping
- chemical gene interaction association
- macromolecular machine has substrate association
- chemical affects biological entity association
- chemical gene sensitivity association
- gene affects chemical association
range: string

```
</details></div>