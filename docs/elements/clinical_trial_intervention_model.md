---
search:
  boost: 5.0
---

# Slot: clinical_trial_intervention_model 


_The intervention model of a clinical trial as determined by clinicaltrials.gov.  The most common values are SINGLE_GROUP, PARALLEL, CROSSOVER, FACTORIAL, and (null)._



<div data-search-exclude markdown="1">



URI: [namo:clinical_trial_intervention_model](https://w3id.org/monarch-initiative/namo/clinical_trial_intervention_model)
Alias: clinical_trial_intervention_model


## Inheritance

* [node_property](node_property.md)
    * **clinical_trial_intervention_model**






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










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:clinical_trial_intervention_model |
| native | namo:clinical_trial_intervention_model |




## LinkML Source

<details>
```yaml
name: clinical trial intervention model
description: The intervention model of a clinical trial as determined by clinicaltrials.gov.  The
  most common values are SINGLE_GROUP, PARALLEL, CROSSOVER, FACTORIAL, and (null).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: clinical trial
alias: clinical_trial_intervention_model
domain_of:
- clinical trial
range: string

```
</details></div>