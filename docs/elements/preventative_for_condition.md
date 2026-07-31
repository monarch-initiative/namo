---
search:
  boost: 5.0
---

# Slot: preventative_for_condition 


_Holds between a substance, procedure, or activity and a medical condition (disease or phenotypic feature), and states that the  substance, procedure, or activity is able to prevent it manifesting in the first place._



<div data-search-exclude markdown="1">



URI: [namo:preventative_for_condition](https://w3id.org/monarch-initiative/namo/preventative_for_condition)
Alias: preventative_for_condition


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects_likelihood_of](affects_likelihood_of.md)
            * **preventative_for_condition** [ [treats](treats.md)]








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



## Aliases


* prophylactic for
* prevents




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | promotes condition |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:preventative_for_condition |
| native | namo:preventative_for_condition |
| broad | SEMMEDDB:PREVENTS |




## LinkML Source

<details>
```yaml
name: preventative for condition
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: promotes condition
description: Holds between a substance, procedure, or activity and a medical condition
  (disease or phenotypic feature), and states that the  substance, procedure, or activity
  is able to prevent it manifesting in the first place.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- prophylactic for
- prevents
broad_mappings:
- SEMMEDDB:PREVENTS
rank: 1000
is_a: affects likelihood of
mixins:
- treats
domain: chemical or drug or treatment
inherited: true
alias: preventative_for_condition
range: disease or phenotypic feature
multivalued: true

```
</details></div>