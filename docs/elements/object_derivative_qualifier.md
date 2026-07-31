---
search:
  boost: 5.0
---

# Slot: object_derivative_qualifier 


_A qualifier that composes with a core subject/object  concept to describe something that is derived from the core concept.  For example, the qualifier ‘metabolite’ combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite of Chemical X’.  This qualifier is for the object of an association (or statement)._



<div data-search-exclude markdown="1">



URI: [namo:object_derivative_qualifier](https://w3id.org/monarch-initiative/namo/object_derivative_qualifier)
Alias: object_derivative_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [derivative_qualifier](derivative_qualifier.md)
            * **object_derivative_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | Describes a relationship in which a chemical entity affects the sensitivity o... |  yes  |
| [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) | Describes an effect that a gene or gene product has on a chemical entity (e |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Association](Association.md) |
| Domain Of | [PredicateMapping](PredicateMapping.md), [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md), [GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |






## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)





## Examples

| Value |
| --- |
| metabolite |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:object_derivative_qualifier |
| native | namo:object_derivative_qualifier |




## LinkML Source

<details>
```yaml
name: object derivative qualifier
description: A qualifier that composes with a core subject/object  concept to describe
  something that is derived from the core concept.  For example, the qualifier ‘metabolite’
  combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite
  of Chemical X’.  This qualifier is for the object of an association (or statement).
examples:
- value: metabolite
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: derivative qualifier
domain: association
alias: object_derivative_qualifier
domain_of:
- predicate mapping
- chemical gene sensitivity association
- gene affects chemical association
range: string

```
</details></div>