---
search:
  boost: 5.0
---

# Slot: ameliorates_condition 


_Holds between an entity and an existing medical condition (disease or phenotypic feature) where the entity is able to ameliorate symptoms, stabilize progression, or cure the condition._



<div data-search-exclude markdown="1">



URI: [namo:ameliorates_condition](https://w3id.org/monarch-initiative/namo/ameliorates_condition)
Alias: ameliorates_condition


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **ameliorates_condition** [ [treats](treats.md)]








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


* ameliorates
* beneficial for condition
* therapeutic for condition


## Notes

* This predicate describes a narrower view of 'treats' - that covers interventions that are beneficial for existing disease, and excludes interventions that prevent/reduce risk of developing a condition in the future.



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | exacerbates condition |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:ameliorates_condition |
| native | namo:ameliorates_condition |
| exact | RO:0003307 |




## LinkML Source

<details>
```yaml
name: ameliorates condition
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: exacerbates condition
description: Holds between an entity and an existing medical condition (disease or
  phenotypic feature) where the entity is able to ameliorate symptoms, stabilize progression,
  or cure the condition.
notes:
- This predicate describes a narrower view of 'treats' - that covers interventions
  that are beneficial for existing disease, and excludes interventions that prevent/reduce
  risk of developing a condition in the future.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- ameliorates
- beneficial for condition
- therapeutic for condition
exact_mappings:
- RO:0003307
rank: 1000
is_a: affects
mixins:
- treats
domain: chemical or drug or treatment
inherited: true
alias: ameliorates_condition
range: disease or phenotypic feature
multivalued: true

```
</details></div>