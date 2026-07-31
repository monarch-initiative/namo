---
search:
  boost: 5.0
---

# Slot: max_research_phase 


_The maximum research phase reached for a specific chemical-disease pair, indicating the highest clinical trial phase achieved for the chemical entity's investigation as a treatment for the associated disease or condition._



<div data-search-exclude markdown="1">



URI: [namo:max_research_phase](https://w3id.org/monarch-initiative/namo/max_research_phase)
Alias: max_research_phase


## Inheritance

* [association_slot](association_slot.md)
    * **max_research_phase**






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
| Range | [ResearchPhaseEnum](ResearchPhaseEnum.md) |
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
| self | namo:max_research_phase |
| native | namo:max_research_phase |




## LinkML Source

<details>
```yaml
name: max research phase
description: The maximum research phase reached for a specific chemical-disease pair,
  indicating the highest clinical trial phase achieved for the chemical entity's investigation
  as a treatment for the associated disease or condition.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: association
alias: max_research_phase
domain_of:
- chemical entity to disease or phenotypic feature association
- entity to disease association
- entity to phenotypic feature association
range: ResearchPhaseEnum

```
</details></div>