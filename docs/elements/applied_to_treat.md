---
search:
  boost: 5.0
---

# Slot: applied_to_treat 


_Holds between an  substance, procedure, or activity and a medical condition, and reports that the  substance, procedure, or activity was actually taken by one or more patients with the intent of treating the condition._



<div data-search-exclude markdown="1">



URI: [namo:applied_to_treat](https://w3id.org/monarch-initiative/namo/applied_to_treat)
Alias: applied_to_treat


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **applied_to_treat** [ [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md)]








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


* administered to treat
* used to treat
* given to treat


## Notes

* This predicate is used simply to report observations of use in the real world, and is agnostic to whether the treatment is approved for or might be effective in treating the condition. The treatment could be taken by a patient on their own accord or prescribed by a clinician, as an off-label or an approved intervention. In practice, it would be used to represent records/statements from patient self-reporting sources like FAERS / AEOLUS where patients directly report the condition for which they took a drug, or statements from a database cataloging instances of off-label prescription of drugs for specific conditions.



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
| self | namo:applied_to_treat |
| native | namo:applied_to_treat |




## LinkML Source

<details>
```yaml
name: applied to treat
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between an  substance, procedure, or activity and a medical condition,
  and reports that the  substance, procedure, or activity was actually taken by one
  or more patients with the intent of treating the condition.
notes:
- This predicate is used simply to report observations of use in the real world, and
  is agnostic to whether the treatment is approved for or might be effective in treating
  the condition. The treatment could be taken by a patient on their own accord or
  prescribed by a clinician, as an off-label or an approved intervention. In practice,
  it would be used to represent records/statements from patient self-reporting sources
  like FAERS / AEOLUS where patients directly report the condition for which they
  took a drug, or statements from a database cataloging instances of off-label prescription
  of drugs for specific conditions.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- administered to treat
- used to treat
- given to treat
rank: 1000
is_a: related to at instance level
mixins:
- treats or applied or studied to treat
domain: chemical or drug or treatment
inherited: true
alias: applied_to_treat
range: disease or phenotypic feature
multivalued: true

```
</details></div>