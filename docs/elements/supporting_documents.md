---
search:
  boost: 0.5
---

# Slot: supporting_documents  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 


_One or more referenceable documents that report the statement expressed in an Association, or provide information used as evidence supporting this statement._



<div data-search-exclude markdown="1">



URI: [namo:supporting_documents](https://w3id.org/monarch-initiative/namo/supporting_documents)
Alias: supporting_documents


## Inheritance

* [association_slot](association_slot.md)
    * **supporting_documents**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  no  |
| [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) | Describes a relationship in which a chemical entity affects the sensitivity o... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain | [Association](Association.md) |
| Domain Of | [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md), [ChemicalGeneSensitivityAssociation](ChemicalGeneSensitivityAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |









## Examples

| Value |
| --- |
| PMID:12345678 |



## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:supporting_documents |
| native | namo:supporting_documents |




## LinkML Source

<details>
```yaml
name: supporting documents
description: One or more referenceable documents that report the statement expressed
  in an Association, or provide information used as evidence supporting this statement.
deprecated: 'true'
examples:
- value: PMID:12345678
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: supporting_documents
domain_of:
- chemical affects gene association
- chemical gene sensitivity association
range: uriorcurie
multivalued: true

```
</details></div>