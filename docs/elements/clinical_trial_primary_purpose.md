---
search:
  boost: 5.0
---

# Slot: clinical_trial_primary_purpose 


_The primary purpose of a clinical trial as determined by clinicaltrials.gov.  The most common values are TREATMENT and PREVENTION. Other possible values include BASIC_SCIENCE, SUPPORTIVE_CARE, DIAGNOSTIC, HEALTH_SERVICES_RESEARCH, SCREENING, DEVICE_FEASIBILITY, OTHER, and (null)._



<div data-search-exclude markdown="1">



URI: [namo:clinical_trial_primary_purpose](https://w3id.org/monarch-initiative/namo/clinical_trial_primary_purpose)
Alias: clinical_trial_primary_purpose


## Inheritance

* [node_property](node_property.md)
    * **clinical_trial_primary_purpose**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [ClinicalTrial](ClinicalTrial.md) |
| Domain Of | [ClinicalTrial](ClinicalTrial.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* primary purpose




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:clinical_trial_primary_purpose |
| native | namo:clinical_trial_primary_purpose |




## LinkML Source

<details>
```yaml
name: clinical trial primary purpose
description: The primary purpose of a clinical trial as determined by clinicaltrials.gov.  The
  most common values are TREATMENT and PREVENTION. Other possible values include BASIC_SCIENCE,
  SUPPORTIVE_CARE, DIAGNOSTIC, HEALTH_SERVICES_RESEARCH, SCREENING, DEVICE_FEASIBILITY,
  OTHER, and (null).
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- primary purpose
rank: 1000
is_a: node property
domain: clinical trial
alias: clinical_trial_primary_purpose
domain_of:
- clinical trial
range: string

```
</details></div>