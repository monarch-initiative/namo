---
search:
  boost: 5.0
---

# Slot: treats_or_applied_or_studied_to_treat 


_Holds between an substance, procedure, or activity and a medical condition (disease or phenotypic feature), and states that the substance, procedure, or activity is able to treat the condition, has been observed to be taken/prescribed in practice with the intent of treating the condition, or has been interrogated in a scientific study that hypothesized an ability to treat the condition (in humans or other biological systems/organisms)._



<div data-search-exclude markdown="1">



URI: [namo:treats_or_applied_or_studied_to_treat](https://w3id.org/monarch-initiative/namo/treats_or_applied_or_studied_to_treat)
Alias: treats_or_applied_or_studied_to_treat


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **treats_or_applied_or_studied_to_treat**
            * [treats](treats.md)







## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [studied_to_treat](studied_to_treat.md) | Holds between an  substance, procedure, or activity and a medical condition, ... | disease or phenotypic feature |  |
| [in_clinical_trials_for](in_clinical_trials_for.md) | Holds between an intervention and a medical condition, and reports that a cli... | disease or phenotypic feature |  |
| [in_preclinical_trials_for](in_preclinical_trials_for.md) | Holds between an  substance, procedure, or activity and a medical condition, ... | disease or phenotypic feature |  |
| [beneficial_in_models_for](beneficial_in_models_for.md) | Holds between an  substance, procedure, or activity and a medical condition, ... | disease or phenotypic feature |  |
| [applied_to_treat](applied_to_treat.md) | Holds between an  substance, procedure, or activity and a medical condition, ... | disease or phenotypic feature |  |



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
| Mixin | Yes |








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)




## Notes

* This predicate is helpful both as a grouping predicate to aid in searching for broader senses of treating a condition, and as a catch-all for representing sources that are not clear about the sense of treats that is being reported. For example, text-mined statements concerning treatments for disease are based on sentences that can report treatment in any of these different senses and thus require a broader predicate such as this to safely report statement semantics.



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
| self | namo:treats_or_applied_or_studied_to_treat |
| native | namo:treats_or_applied_or_studied_to_treat |
| exact | SEMMEDDB:TREATS |




## LinkML Source

<details>
```yaml
name: treats or applied or studied to treat
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between an substance, procedure, or activity and a medical condition
  (disease or phenotypic feature), and states that the substance, procedure, or activity
  is able to treat the condition, has been observed to be taken/prescribed in practice
  with the intent of treating the condition, or has been interrogated in a scientific
  study that hypothesized an ability to treat the condition (in humans or other biological
  systems/organisms).
notes:
- This predicate is helpful both as a grouping predicate to aid in searching for broader
  senses of treating a condition, and as a catch-all for representing sources that
  are not clear about the sense of treats that is being reported. For example, text-mined
  statements concerning treatments for disease are based on sentences that can report
  treatment in any of these different senses and thus require a broader predicate
  such as this to safely report statement semantics.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SEMMEDDB:TREATS
rank: 1000
is_a: related to at instance level
mixin: true
domain: chemical or drug or treatment
inherited: true
alias: treats_or_applied_or_studied_to_treat
range: disease or phenotypic feature
multivalued: true

```
</details></div>