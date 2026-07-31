---
search:
  boost: 5.0
---

# Slot: tested_by_preclinical_trials_of 

<div data-search-exclude markdown="1">



URI: [namo:tested_by_preclinical_trials_of](https://w3id.org/monarch-initiative/namo/tested_by_preclinical_trials_of)
Alias: tested_by_preclinical_trials_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)
            * [treated_by](treated_by.md)
                * [treated_in_studies_by](treated_in_studies_by.md) [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]
                    * **tested_by_preclinical_trials_of** [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]
                        * [models_demonstrating_benefits_for](models_demonstrating_benefits_for.md) [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]








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
| Inverse | [in_preclinical_trials_for](in_preclinical_trials_for.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:tested_by_preclinical_trials_of |
| native | namo:tested_by_preclinical_trials_of |




## LinkML Source

<details>
```yaml
name: tested by preclinical trials of
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: treated in studies by
mixins:
- subject of treatment application or study for treatment by
domain: disease or phenotypic feature
inherited: true
alias: tested_by_preclinical_trials_of
inverse: in preclinical trials for
range: chemical or drug or treatment
multivalued: true

```
</details></div>