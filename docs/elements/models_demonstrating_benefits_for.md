---
search:
  boost: 5.0
---

# Slot: models_demonstrating_benefits_for 

<div data-search-exclude markdown="1">



URI: [namo:models_demonstrating_benefits_for](https://w3id.org/monarch-initiative/namo/models_demonstrating_benefits_for)
Alias: models_demonstrating_benefits_for


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)
            * [treated_by](treated_by.md)
                * [treated_in_studies_by](treated_in_studies_by.md) [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]
                    * [tested_by_preclinical_trials_of](tested_by_preclinical_trials_of.md) [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]
                        * **models_demonstrating_benefits_for** [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]








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
| Inverse | [beneficial_in_models_for](beneficial_in_models_for.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:models_demonstrating_benefits_for |
| native | namo:models_demonstrating_benefits_for |




## LinkML Source

<details>
```yaml
name: models demonstrating benefits for
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: tested by preclinical trials of
mixins:
- subject of treatment application or study for treatment by
domain: disease or phenotypic feature
inherited: true
alias: models_demonstrating_benefits_for
inverse: beneficial in models for
range: chemical or drug or treatment
multivalued: true

```
</details></div>