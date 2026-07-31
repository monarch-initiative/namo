---
search:
  boost: 5.0
---

# Slot: anatomical_context_qualifier 


_A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location)._



<div data-search-exclude markdown="1">



URI: [namo:anatomical_context_qualifier](https://w3id.org/monarch-initiative/namo/anatomical_context_qualifier)
Alias: anatomical_context_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [statement_qualifier](statement_qualifier.md)
            * **anatomical_context_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
| [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md) | An association between a chemical entity and a biological process, where the ... |  no  |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |  yes  |
| [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md) | Describes the relationship between an enzyme (usually a macromolecular comple... |  no  |
| [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md) | Describes an effect that a chemical has on a biological entity (e |  yes  |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | Describes a relationship in which a chemical entity affects the sensitivity o... |  yes  |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | Describes an effect that a gene or gene product has on a chemical entity (e |  yes  |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) |  |  no  |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the c... |  no  |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where th... |  no  |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalOrDrugOrTreatmentAdverseEventAssociation](ChemicalOrDrugOrTreatmentAdverseEventAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalOrDrugOrTreatmentSideEffectAssociation](ChemicalOrDrugOrTreatmentSideEffectAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  no  |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype |  no  |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | An association in which a cell line - typically derived from an organismal en... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |
| Domain Of | [PredicateMapping](PredicateMapping.md), [ChemicalEntityToBiologicalProcessAssociation](ChemicalEntityToBiologicalProcessAssociation.md), [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md), [MacromolecularMachineHasSubstrateAssociation](MacromolecularMachineHasSubstrateAssociation.md), [ChemicalAffectsBiologicalEntityAssociation](ChemicalAffectsBiologicalEntityAssociation.md), [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md), [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md), [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)





## Examples

| Value |
| --- |
| UBERON:0000178 |
| UBERON:0000956 |
| GO:0005794 |

## Notes

* Anatomical context values can be any term from UBERON. For example, the context qualifier ‘cerebral cortext’ combines with a core concept of ‘neuron’ to express the composed concept ‘neuron in the cerebral cortext’. The species_context_qualifier applies taxonomic context.  Ontology CURIEs are expected as values here, the examples below are intended to help clarify the content of the CURIEs.



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:anatomical_context_qualifier |
| native | namo:anatomical_context_qualifier |




## LinkML Source

<details>
```yaml
name: anatomical context qualifier
description: A statement qualifier representing an anatomical location where an relationship
  expressed in an association took place (can be a tissue, cell type, or sub-cellular
  location).
notes:
- Anatomical context values can be any term from UBERON. For example, the context
  qualifier ‘cerebral cortext’ combines with a core concept of ‘neuron’ to express
  the composed concept ‘neuron in the cerebral cortext’. The species_context_qualifier
  applies taxonomic context.  Ontology CURIEs are expected as values here, the examples
  below are intended to help clarify the content of the CURIEs.
examples:
- value: UBERON:0000178
  description: blood
- value: UBERON:0000956
  description: cerebral cortex
- value: GO:0005794
  description: Golgi apparatus
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: statement qualifier
domain: association
alias: anatomical_context_qualifier
domain_of:
- predicate mapping
- chemical entity to biological process association
- chemical gene interaction association
- macromolecular machine has substrate association
- chemical affects biological entity association
- chemical gene sensitivity association
- gene affects chemical association
- entity to disease or phenotypic feature association mixin
range: string
multivalued: true

```
</details></div>