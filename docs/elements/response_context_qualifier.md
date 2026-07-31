---
search:
  boost: 5.0
---

# Slot: response_context_qualifier 


_a biological response (general, study, cohort, etc.) with a specific set of characteristics to constrain an association._



<div data-search-exclude markdown="1">



URI: [namo:response_context_qualifier](https://w3id.org/monarch-initiative/namo/response_context_qualifier)
Alias: response_context_qualifier


## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [context_qualifier](context_qualifier.md)
            * **response_context_qualifier**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) | A statistical association between a disease and a chemical entity where the c... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ResponseEnum](ResponseEnum.md) |
| Domain | [Association](Association.md) |
| Domain Of | [DiseaseAssociatedWithResponseToChemicalEntityAssociation](DiseaseAssociatedWithResponseToChemicalEntityAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:response_context_qualifier |
| native | namo:response_context_qualifier |




## LinkML Source

<details>
```yaml
name: response context qualifier
description: a biological response (general, study, cohort, etc.) with a specific
  set of characteristics to constrain an association.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: context qualifier
domain: association
alias: response_context_qualifier
domain_of:
- disease associated with response to chemical entity association
range: ResponseEnum

```
</details></div>