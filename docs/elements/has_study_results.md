---
search:
  boost: 5.0
---

# Slot: has_study_results 


_Connects an study to instances of its study result_



<div data-search-exclude markdown="1">



URI: [namo:has_study_results](https://w3id.org/monarch-initiative/namo/has_study_results)
Alias: has_study_results


## Inheritance

* [association_slot](association_slot.md)
    * **has_study_results**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | a detailed investigation and/or analysis |  no  |
| [NAMStudy](NAMStudy.md) | A study is a structured investigation or analysis, often involving the collec... |  no  |
| [ClinicalTrial](ClinicalTrial.md) | A clinical trial is a research study that prospectively assigns human partici... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyResult](StudyResult.md) |
| Domain | [Study](Study.md) |
| Domain Of | [Study](Study.md) |

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
| self | namo:has_study_results |
| native | namo:has_study_results |




## LinkML Source

<details>
```yaml
name: has study results
description: Connects an study to instances of its study result
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: association slot
domain: study
alias: has_study_results
domain_of:
- study
range: study result
multivalued: true
inlined: true
inlined_as_list: true

```
</details></div>