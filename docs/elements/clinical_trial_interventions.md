---
search:
  boost: 5.0
---

# Slot: clinical_trial_interventions 


_connects a clinical trial to one or more interventions being tested in the trial_



<div data-search-exclude markdown="1">



URI: [namo:clinical_trial_interventions](https://w3id.org/monarch-initiative/namo/clinical_trial_interventions)
Alias: clinical_trial_interventions


## Inheritance

* [node_property](node_property.md)
    * **clinical_trial_interventions**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ClinicalIntervention](ClinicalIntervention.md) |
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
| self | namo:clinical_trial_interventions |
| native | namo:clinical_trial_interventions |




## LinkML Source

<details>
```yaml
name: clinical trial interventions
description: connects a clinical trial to one or more interventions being tested in
  the trial
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: node property
domain: clinical trial
alias: clinical_trial_interventions
domain_of:
- clinical trial
range: clinical intervention
multivalued: true

```
</details></div>