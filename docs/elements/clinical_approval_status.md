---
search:
  boost: 5.0
---

# Slot: clinical_approval_status 


_The clinical approval status of a chemical entity for treating a specific disease or condition, as captured in the context of the association between the chemical and the disease._



<div data-search-exclude markdown="1">



URI: [namo:clinical_approval_status](https://w3id.org/monarch-initiative/namo/clinical_approval_status)
Alias: clinical_approval_status


## Inheritance

* [association_slot](association_slot.md)
    * **clinical_approval_status**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where th... |  no  |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | An association between any entity and a disease, capturing clinical context s... |  no  |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | An association between any entity and a phenotypic feature, capturing clinica... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ClinicalApprovalStatusEnum](ClinicalApprovalStatusEnum.md) |
| Domain | [Association](Association.md) |
| Domain Of | [ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation](ChemicalEntityToDiseaseOrPhenotypicFeatureAssociation.md), [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md), [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:clinical_approval_status |
| native | namo:clinical_approval_status |




## LinkML Source

<details>
```yaml
name: clinical approval status
description: The clinical approval status of a chemical entity for treating a specific
  disease or condition, as captured in the context of the association between the
  chemical and the disease.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: clinical_approval_status
domain_of:
- chemical entity to disease or phenotypic feature association
- entity to disease association
- entity to phenotypic feature association
range: ClinicalApprovalStatusEnum

```
</details></div>