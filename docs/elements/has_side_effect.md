---
search:
  boost: 5.0
---

# Slot: has_side_effect 


_An unintended, but predictable, secondary effect shown to be correlated with a therapeutic agent, drug or treatment. Side effects happen at normal, recommended doses or treatments, and are unrelated to the intended purpose of the medication._



<div data-search-exclude markdown="1">



URI: [namo:has_side_effect](https://w3id.org/monarch-initiative/namo/has_side_effect)
Alias: has_side_effect


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **has_side_effect**








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


* adverse drug reaction


## Notes

* Side effects are listed on drug labels. There can be positive side effects, while adverse events are always negative. Aeolus, Sider are both resources that provide side effects.



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
| self | namo:has_side_effect |
| native | namo:has_side_effect |
| exact | NCIT:C2861 |




## LinkML Source

<details>
```yaml
name: has side effect
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: An unintended, but predictable, secondary effect shown to be correlated
  with a therapeutic agent, drug or treatment. Side effects happen at normal, recommended
  doses or treatments, and are unrelated to the intended purpose of the medication.
notes:
- Side effects are listed on drug labels. There can be positive side effects, while
  adverse events are always negative. Aeolus, Sider are both resources that provide
  side effects.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- adverse drug reaction
exact_mappings:
- NCIT:C2861
rank: 1000
is_a: affects
domain: chemical or drug or treatment
inherited: true
alias: has_side_effect
range: disease or phenotypic feature
multivalued: true

```
</details></div>