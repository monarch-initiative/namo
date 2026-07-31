---
search:
  boost: 5.0
---

# Slot: promotes_condition 


_Holds between a substance, procedure, or activity and a medical condition (disease or phenotypic feature), and states that the  substance, procedure, or activity is able to promote it manifesting in the first place._



<div data-search-exclude markdown="1">



URI: [namo:promotes_condition](https://w3id.org/monarch-initiative/namo/promotes_condition)
Alias: promotes_condition


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects_likelihood_of](affects_likelihood_of.md)
            * **promotes_condition**







## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [predisposes_to_condition](predisposes_to_condition.md) | Holds between two entities where the presence or application of one increases... | disease or phenotypic feature |  |
| [exacerbates_condition](exacerbates_condition.md) | Holds between a substance, procedure, or activity and an existing medical con... | disease or phenotypic feature |  |



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






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | preventative for condition |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:promotes_condition |
| native | namo:promotes_condition |




## LinkML Source

<details>
```yaml
name: promotes condition
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: preventative for condition
description: Holds between a substance, procedure, or activity and a medical condition
  (disease or phenotypic feature), and states that the  substance, procedure, or activity
  is able to promote it manifesting in the first place.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: affects likelihood of
mixin: true
domain: chemical or drug or treatment
inherited: true
alias: promotes_condition
range: disease or phenotypic feature
multivalued: true

```
</details></div>