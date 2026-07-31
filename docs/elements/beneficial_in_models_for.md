---
search:
  boost: 5.0
---

# Slot: beneficial_in_models_for 


_Holds between an  substance, procedure, or activity and a medical condition, and reports that the substance, procedure, or activity has been shown to be effective in alleviating, preventing, or delaying symptoms/ phenotypes associated with a disease, in a model system for that disease (e.g. a mouse, fly, cell line, etc)._



<div data-search-exclude markdown="1">



URI: [namo:beneficial_in_models_for](https://w3id.org/monarch-initiative/namo/beneficial_in_models_for)
Alias: beneficial_in_models_for


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [studied_to_treat](studied_to_treat.md) [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]
            * [in_preclinical_trials_for](in_preclinical_trials_for.md) [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]
                * **beneficial_in_models_for** [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]








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




## Notes

* This predicate would be used to represent Model Organism Database (MOD) records reporting that an intervention alleviated phenotypes associated with a human disease in a model organism designated as a model of that disease. (e.g. a ZFIN record reporting that treatment with Braf Inhibitors reduced the abnormal brain cell proliferation phenotype of zebrafish used to model the human disease Kabuki Syndrome) .



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
| self | namo:beneficial_in_models_for |
| native | namo:beneficial_in_models_for |




## LinkML Source

<details>
```yaml
name: beneficial in models for
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between an  substance, procedure, or activity and a medical condition,
  and reports that the substance, procedure, or activity has been shown to be effective
  in alleviating, preventing, or delaying symptoms/ phenotypes associated with a disease,
  in a model system for that disease (e.g. a mouse, fly, cell line, etc).
notes:
- This predicate would be used to represent Model Organism Database (MOD) records
  reporting that an intervention alleviated phenotypes associated with a human disease
  in a model organism designated as a model of that disease. (e.g. a ZFIN record reporting
  that treatment with Braf Inhibitors reduced the abnormal brain cell proliferation
  phenotype of zebrafish used to model the human disease Kabuki Syndrome) .
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: in preclinical trials for
mixins:
- treats or applied or studied to treat
domain: chemical or drug or treatment
inherited: true
alias: beneficial_in_models_for
range: disease or phenotypic feature
multivalued: true

```
</details></div>