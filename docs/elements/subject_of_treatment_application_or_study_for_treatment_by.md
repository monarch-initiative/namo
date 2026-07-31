---
search:
  boost: 5.0
---

# Slot: subject_of_treatment_application_or_study_for_treatment_by 

<div data-search-exclude markdown="1">



URI: [namo:subject_of_treatment_application_or_study_for_treatment_by](https://w3id.org/monarch-initiative/namo/subject_of_treatment_application_or_study_for_treatment_by)
Alias: subject_of_treatment_application_or_study_for_treatment_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **subject_of_treatment_application_or_study_for_treatment_by**
            * [treated_by](treated_by.md)







## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [tested_by_clinical_trials_of](tested_by_clinical_trials_of.md) |  | chemical or drug or treatment |  |
| [treated_in_studies_by](treated_in_studies_by.md) |  | chemical or drug or treatment |  |
| [tested_by_preclinical_trials_of](tested_by_preclinical_trials_of.md) |  | chemical or drug or treatment |  |
| [models_demonstrating_benefits_for](models_demonstrating_benefits_for.md) |  | chemical or drug or treatment |  |
| [treatment_applications_from](treatment_applications_from.md) |  | chemical or drug or treatment |  |



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
| Mixin | Yes |


<details>
<summary>Relationship Properties</summary>

| Property | Value |
| --- | --- |
| Inverse | [treats_or_applied_or_studied_to_treat](treats_or_applied_or_studied_to_treat.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:subject_of_treatment_application_or_study_for_treatment_by |
| native | namo:subject_of_treatment_application_or_study_for_treatment_by |




## LinkML Source

<details>
```yaml
name: subject of treatment application or study for treatment by
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
mixin: true
domain: disease or phenotypic feature
inherited: true
alias: subject_of_treatment_application_or_study_for_treatment_by
inverse: treats or applied or studied to treat
range: chemical or drug or treatment
multivalued: true

```
</details></div>