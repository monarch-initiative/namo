---
search:
  boost: 5.0
---

# Slot: object_activity_qualifier 

<div data-search-exclude markdown="1">



URI: [namo:object_activity_qualifier](https://w3id.org/monarch-initiative/namo/object_activity_qualifier)
Alias: object_activity_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [process_qualifier](process_qualifier.md)
            * **object_activity_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | parent class for different kinds of gene-gene or gene product to gene product... |  yes  |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes |  no  |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products |  no  |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |
| Domain Of | [GeneToGeneAssociation](GeneToGeneAssociation.md) |

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
| self | namo:object_activity_qualifier |
| native | namo:object_activity_qualifier |




## LinkML Source

<details>
```yaml
name: object activity qualifier
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: process qualifier
domain: association
alias: object_activity_qualifier
domain_of:
- gene to gene association
range: string

```
</details></div>