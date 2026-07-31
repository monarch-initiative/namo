---
search:
  boost: 5.0
---

# Slot: object_form_or_variant_qualifier 


_A qualifier that composes with a core subject/object concept to define a specific type, variant, alternative version of this concept. The composed concept remains a subtype or instance of the core concept. For example, the qualifier ‘mutation’ combines with the core concept ‘Gene X’ to express the compose concept ‘a mutation of Gene X’.  This qualifier specifies a change in the object of an association (aka: statement)._



<div data-search-exclude markdown="1">



URI: [namo:object_form_or_variant_qualifier](https://w3id.org/monarch-initiative/namo/object_form_or_variant_qualifier)
Alias: object_form_or_variant_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [form_or_variant_qualifier](form_or_variant_qualifier.md)
            * **object_form_or_variant_qualifier**






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
| mutation |
| late stage |
| severe |
| transplant |
| chemical analog |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:object_form_or_variant_qualifier |
| native | namo:object_form_or_variant_qualifier |




## LinkML Source

<details>
```yaml
name: object form or variant qualifier
description: 'A qualifier that composes with a core subject/object concept to define
  a specific type, variant, alternative version of this concept. The composed concept
  remains a subtype or instance of the core concept. For example, the qualifier ‘mutation’
  combines with the core concept ‘Gene X’ to express the compose concept ‘a mutation
  of Gene X’.  This qualifier specifies a change in the object of an association (aka:
  statement).'
examples:
- value: mutation
- value: late stage
- value: severe
- value: transplant
- value: chemical analog
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: form or variant qualifier
domain: association
alias: object_form_or_variant_qualifier
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