---
search:
  boost: 5.0
---

# Slot: has_adverse_event 


_An untoward medical occurrence in a patient or clinical investigation subject that happens during treatment with a therapeutic agent. Adverse events may be caused by something other than the drug or therapy being given and may include abnormal laboratory finding, symptoms, or diseases temporally associated with the treatment, whether or not considered related to the treatment. Adverse events are unintended effects that occur when a medication is administered correctly._



<div data-search-exclude markdown="1">



URI: [namo:has_adverse_event](https://w3id.org/monarch-initiative/namo/has_adverse_event)
Alias: has_adverse_event


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **has_adverse_event**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |
| Domain | [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |









## Aliases


* adverse effect




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_adverse_event |
| native | namo:has_adverse_event |




## LinkML Source

<details>
```yaml
name: has adverse event
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: An untoward medical occurrence in a patient or clinical investigation
  subject that happens during treatment with a therapeutic agent. Adverse events may
  be caused by something other than the drug or therapy being given and may include
  abnormal laboratory finding, symptoms, or diseases temporally associated with the
  treatment, whether or not considered related to the treatment. Adverse events are
  unintended effects that occur when a medication is administered correctly.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- adverse effect
rank: 1000
is_a: affects
domain: chemical or drug or treatment
inherited: true
alias: has_adverse_event
range: disease or phenotypic feature
multivalued: true

```
</details></div>