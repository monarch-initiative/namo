---
search:
  boost: 5.0
---

# Slot: in_preclinical_trials_for 


_Holds between an  substance, procedure, or activity and a medical condition, and reports that a pre-clinical study has been performed specifically to test the potential of the  substance, procedure, or activity to treat the medical condition  (i.e. to ameliorate, stabilize, or cure the condition, or to delay, prevent, or reduce the risk of it manifesting in the first place)._



<div data-search-exclude markdown="1">



URI: [namo:in_preclinical_trials_for](https://w3id.org/monarch-initiative/namo/in_preclinical_trials_for)
Alias: in_preclinical_trials_for


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [studied_to_treat](studied_to_treat.md) [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]
            * **in_preclinical_trials_for** [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]
                * [beneficial_in_models_for](beneficial_in_models_for.md) [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]








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








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






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
| self | namo:in_preclinical_trials_for |
| native | namo:in_preclinical_trials_for |




## LinkML Source

<details>
```yaml
name: in preclinical trials for
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between an  substance, procedure, or activity and a medical condition,
  and reports that a pre-clinical study has been performed specifically to test the
  potential of the  substance, procedure, or activity to treat the medical condition  (i.e.
  to ameliorate, stabilize, or cure the condition, or to delay, prevent, or reduce
  the risk of it manifesting in the first place).
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: studied to treat
mixins:
- treats or applied or studied to treat
domain: chemical or drug or treatment
inherited: true
alias: in_preclinical_trials_for
range: disease or phenotypic feature
multivalued: true

```
</details></div>