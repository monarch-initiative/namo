---
search:
  boost: 5.0
---

# Slot: treated_in_studies_by 

<div data-search-exclude markdown="1">



URI: [namo:treated_in_studies_by](https://w3id.org/monarch-initiative/namo/treated_in_studies_by)
Alias: treated_in_studies_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)
            * [treated_by](treated_by.md)
                * **treated_in_studies_by** [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]
                    * [tested_by_clinical_trials_of](tested_by_clinical_trials_of.md) [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]
                    * [tested_by_preclinical_trials_of](tested_by_preclinical_trials_of.md) [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]








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
| Inverse | [studied_to_treat](studied_to_treat.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:treated_in_studies_by |
| native | namo:treated_in_studies_by |




## LinkML Source

<details>
```yaml
name: treated in studies by
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: treated by
mixins:
- subject of treatment application or study for treatment by
domain: disease or phenotypic feature
inherited: true
alias: treated_in_studies_by
inverse: studied to treat
range: chemical or drug or treatment
multivalued: true

```
</details></div>