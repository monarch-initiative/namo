---
search:
  boost: 5.0
---

# Slot: FDA_regulatory_approvals 


_Numbers that identify specific drug applications. Each drug can have multiple approval numbers (for example, as seen with ranitidine having both ANADA200536 and ANDA200536)._



<div data-search-exclude markdown="1">



URI: [namo:FDA_regulatory_approvals](https://w3id.org/monarch-initiative/namo/FDA_regulatory_approvals)
Alias: FDA_regulatory_approvals

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | An association between any entity and a disease, capturing clinical context s... |  no  |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | An association between any entity and a phenotypic feature, capturing clinica... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md), [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:FDA_regulatory_approvals |
| native | namo:FDA_regulatory_approvals |




## LinkML Source

<details>
```yaml
name: FDA regulatory approvals
description: Numbers that identify specific drug applications. Each drug can have
  multiple approval numbers (for example, as seen with ranitidine having both ANADA200536
  and ANDA200536).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: FDA_regulatory_approvals
domain_of:
- entity to disease association
- entity to phenotypic feature association
range: string
multivalued: true

```
</details></div>