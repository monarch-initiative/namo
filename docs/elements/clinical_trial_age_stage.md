---
search:
  boost: 5.0
---

# Slot: clinical_trial_age_stage 


_The age stage of a clinical trial as determined by clinicaltrials.gov (adult, child, older adult)_



<div data-search-exclude markdown="1">



URI: [namo:clinical_trial_age_stage](https://w3id.org/monarch-initiative/namo/clinical_trial_age_stage)
Alias: clinical_trial_age_stage


## Inheritance

* [node_property](node_property.md)
    * **clinical_trial_age_stage**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ClinicalTrialAgeStageEnum](ClinicalTrialAgeStageEnum.md) |
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
| self | namo:clinical_trial_age_stage |
| native | namo:clinical_trial_age_stage |




## LinkML Source

<details>
```yaml
name: clinical trial age stage
description: The age stage of a clinical trial as determined by clinicaltrials.gov
  (adult, child, older adult)
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: clinical trial
alias: clinical_trial_age_stage
domain_of:
- clinical trial
range: ClinicalTrialAgeStageEnum
multivalued: true

```
</details></div>