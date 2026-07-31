---
search:
  boost: 5.0
---

# Slot: predisposes_to_condition 


_Holds between two entities where the presence or application of one increases the chance that the other will come to be._



<div data-search-exclude markdown="1">



URI: [namo:predisposes_to_condition](https://w3id.org/monarch-initiative/namo/predisposes_to_condition)
Alias: predisposes_to_condition


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects_likelihood_of](affects_likelihood_of.md)
            * **predisposes_to_condition** [ [promotes_condition](promotes_condition.md)]








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


* risk factor for




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
| self | namo:predisposes_to_condition |
| native | namo:predisposes_to_condition |
| broad | SEMMEDDB:PREDISPOSES |




## LinkML Source

<details>
```yaml
name: predisposes to condition
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between two entities where the presence or application of one increases
  the chance that the other will come to be.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- risk factor for
broad_mappings:
- SEMMEDDB:PREDISPOSES
rank: 1000
is_a: affects likelihood of
mixins:
- promotes condition
domain: chemical or drug or treatment
inherited: true
alias: predisposes_to_condition
range: disease or phenotypic feature
multivalued: true

```
</details></div>