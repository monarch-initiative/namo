---
search:
  boost: 5.0
---

# Slot: exacerbates_condition 


_Holds between a substance, procedure, or activity and an existing medical condition (disease or phenotypic_

_ feature) where the substance, procedure, or activity worsens some or all aspects of the condition._



<div data-search-exclude markdown="1">



URI: [namo:exacerbates_condition](https://w3id.org/monarch-initiative/namo/exacerbates_condition)
Alias: exacerbates_condition


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **exacerbates_condition** [ [promotes_condition](promotes_condition.md)]








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


* exacerbates
* detrimental for condition




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | ameliorates condition |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:exacerbates_condition |
| native | namo:exacerbates_condition |
| exact | RO:0003309 |
| broad | SEMMEDDB:COMPLICATES |




## LinkML Source

<details>
```yaml
name: exacerbates condition
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: ameliorates condition
description: "Holds between a substance, procedure, or activity and an existing medical\
  \ condition (disease or phenotypic\n feature) where the substance, procedure, or\
  \ activity worsens some or all aspects of the condition."
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- exacerbates
- detrimental for condition
exact_mappings:
- RO:0003309
broad_mappings:
- SEMMEDDB:COMPLICATES
rank: 1000
is_a: affects
mixins:
- promotes condition
domain: chemical or drug or treatment
inherited: true
alias: exacerbates_condition
range: disease or phenotypic feature
multivalued: true

```
</details></div>