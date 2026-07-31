---
search:
  boost: 5.0
---

# Slot: treatment_applications_from 

<div data-search-exclude markdown="1">



URI: [namo:treatment_applications_from](https://w3id.org/monarch-initiative/namo/treatment_applications_from)
Alias: treatment_applications_from


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **treatment_applications_from** [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) |
| Domain | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [applied_to_treat](applied_to_treat.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:treatment_applications_from |
| native | namo:treatment_applications_from |




## LinkML Source

<details>
```yaml
name: treatment applications from
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
mixins:
- subject of treatment application or study for treatment by
domain: disease or phenotypic feature
inherited: true
alias: treatment_applications_from
inverse: applied to treat
range: chemical or drug or treatment
multivalued: true

```
</details></div>