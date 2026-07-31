---
search:
  boost: 5.0
---

# Slot: object_context_qualifier 


_A qualifier describing the context in which the object of an association holds._



<div data-search-exclude markdown="1">



URI: [namo:object_context_qualifier](https://w3id.org/monarch-initiative/namo/object_context_qualifier)
Alias: object_context_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [context_qualifier](context_qualifier.md)
            * **object_context_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | parent class for different kinds of gene-gene or gene product to gene product... |  yes  |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | An association in which the subject entity is linked to the likelihood of the... |  yes  |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |  yes  |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | Describes the relationship between an enzyme (usually a macromolecular comple... |  no  |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | Describes an effect that a chemical has on a biological entity (e |  yes  |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | Describes an effect that a gene or gene product has on a chemical entity (e |  yes  |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes |  no  |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products |  no  |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |  no  |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |
| Domain Of | [PredicateMapping](PredicateMapping.md), [GeneToGeneAssociation](GeneToGeneAssociation.md), [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md), [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md), [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md), [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md), [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:object_context_qualifier |
| native | namo:object_context_qualifier |




## LinkML Source

<details>
```yaml
name: object context qualifier
description: A qualifier describing the context in which the object of an association
  holds.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: context qualifier
domain: association
alias: object_context_qualifier
domain_of:
- predicate mapping
- gene to gene association
- named thing associated with likelihood of named thing association
- chemical gene interaction association
- macromolecular machine has substrate association
- chemical affects biological entity association
- gene affects chemical association
range: string

```
</details></div>