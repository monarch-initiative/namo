---
search:
  boost: 5.0
---

# Slot: causal_mechanism_qualifier 


_A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated_



<div data-search-exclude markdown="1">



URI: [namo:causal_mechanism_qualifier](https://w3id.org/monarch-initiative/namo/causal_mechanism_qualifier)
Alias: causal_mechanism_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [statement_qualifier](statement_qualifier.md)
            * **causal_mechanism_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | parent class for different kinds of gene-gene or gene product to gene product... |  no  |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |  yes  |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | Describes the relationship between an enzyme (usually a macromolecular comple... |  no  |
| [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md) | Describes a regulatory relationship between two genes or gene products |  no  |
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
| Range | [CausalMechanismQualifierEnum](CausalMechanismQualifierEnum.md) |
| Domain | [Association](Association.md) |
| Domain Of | [PredicateMapping](PredicateMapping.md), [GeneToGeneAssociation](GeneToGeneAssociation.md), [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md), [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md), [GeneRegulatesGeneAssociation](GeneRegulatesGeneAssociation.md), [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md), [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)





## Examples

| Value |
| --- |
| agonism |
| inhibition |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:causal_mechanism_qualifier |
| native | namo:causal_mechanism_qualifier |




## LinkML Source

<details>
```yaml
name: causal mechanism qualifier
description: A statement qualifier representing a type of molecular control mechanism
  through which an effect of a chemical on a gene or gene product is mediated
examples:
- value: agonism
- value: inhibition
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: statement qualifier
domain: association
alias: causal_mechanism_qualifier
domain_of:
- predicate mapping
- gene to gene association
- chemical gene interaction association
- macromolecular machine has substrate association
- gene regulates gene association
- chemical affects biological entity association
- gene affects chemical association
range: CausalMechanismQualifierEnum

```
</details></div>