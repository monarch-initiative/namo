---
search:
  boost: 5.0
---

# Slot: clinical_trial_overall_status 


_The overall status of a clinical trial as determined by clinicaltrials.gov_



<div data-search-exclude markdown="1">



URI: [namo:clinical_trial_overall_status](https://w3id.org/monarch-initiative/namo/clinical_trial_overall_status)
Alias: clinical_trial_overall_status


## Inheritance

* [node_property](node_property.md)
    * **clinical_trial_overall_status**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ClinicalTrialStatusEnum](ClinicalTrialStatusEnum.md) |
| Domain | [ClinicalTrial](ClinicalTrial.md) |
| Domain Of | [ClinicalTrial](ClinicalTrial.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:clinical_trial_overall_status |
| native | namo:clinical_trial_overall_status |




## LinkML Source

<details>
```yaml
name: clinical trial overall status
description: The overall status of a clinical trial as determined by clinicaltrials.gov
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: clinical trial
alias: clinical_trial_overall_status
domain_of:
- clinical trial
range: ClinicalTrialStatusEnum

```
</details></div>