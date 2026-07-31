---
search:
  boost: 5.0
---

# Slot: studied_to_treat 


_Holds between an  substance, procedure, or activity and a medical condition, and reports that one or more scientific study has been performed to specifically test the potential of the  substance, procedure, or activity to treat the medical condition  (i.e. to ameliorate, stabilize, or cure the condition, or to delay, prevent, or reduce the risk of it manifesting in the first place)._



<div data-search-exclude markdown="1">



URI: [namo:studied_to_treat](https://w3id.org/monarch-initiative/namo/studied_to_treat)
Alias: studied_to_treat


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **studied_to_treat** [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]
            * [in_clinical_trials_for](in_clinical_trials_for.md) [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]
            * [in_preclinical_trials_for](in_preclinical_trials_for.md) [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]








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










## Notes

* Predicates in this hierarchy are used in practice when a source reports performance of a study, but there is not sufficient evidence or demonstrated efficacy against the condition to warrant creating a ‘treats’ assertion edge. Note however that a 'studied to treat' edge may be used as evidence to support creation of a separate 'treats' prediction edge.



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
| self | namo:studied_to_treat |
| native | namo:studied_to_treat |




## LinkML Source

<details>
```yaml
name: studied to treat
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between an  substance, procedure, or activity and a medical condition,
  and reports that one or more scientific study has been performed to specifically
  test the potential of the  substance, procedure, or activity to treat the medical
  condition  (i.e. to ameliorate, stabilize, or cure the condition, or to delay, prevent,
  or reduce the risk of it manifesting in the first place).
notes:
- Predicates in this hierarchy are used in practice when a source reports performance
  of a study, but there is not sufficient evidence or demonstrated efficacy against
  the condition to warrant creating a ‘treats’ assertion edge. Note however that a
  'studied to treat' edge may be used as evidence to support creation of a separate
  'treats' prediction edge.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
mixins:
- treats or applied or studied to treat
domain: chemical or drug or treatment
inherited: true
alias: studied_to_treat
range: disease or phenotypic feature
multivalued: true

```
</details></div>