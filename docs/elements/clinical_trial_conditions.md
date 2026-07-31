---
search:
  boost: 5.0
---

# Slot: clinical_trial_conditions 


_connects a clinical trial to one or more conditions being studied in the trial_



<div data-search-exclude markdown="1">



URI: [namo:clinical_trial_conditions](https://w3id.org/monarch-initiative/namo/clinical_trial_conditions)
Alias: clinical_trial_conditions


## Inheritance

* [node_property](node_property.md)
    * **clinical_trial_conditions**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |
| Domain | [ClinicalTrial](ClinicalTrial.md) |
| Domain Of | [ClinicalTrial](ClinicalTrial.md) |

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
| self | namo:clinical_trial_conditions |
| native | namo:clinical_trial_conditions |




## LinkML Source

<details>
```yaml
name: clinical trial conditions
description: connects a clinical trial to one or more conditions being studied in
  the trial
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: clinical trial
alias: clinical_trial_conditions
domain_of:
- clinical trial
range: disease or phenotypic feature
multivalued: true

```
</details></div>