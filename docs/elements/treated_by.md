---
search:
  boost: 5.0
---

# Slot: treated_by 

<div data-search-exclude markdown="1">



URI: [namo:treated_by](https://w3id.org/monarch-initiative/namo/treated_by)
Alias: treated_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)
            * **treated_by**
                * [treated_in_studies_by](treated_in_studies_by.md) [ [subject_of_treatment_application_or_study_for_treatment_by](subject_of_treatment_application_or_study_for_treatment_by.md)]







## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |



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
| Inverse | [treats](treats.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:treated_by |
| native | namo:treated_by |
| exact | WIKIDATA_PROPERTY:P2176, MONDO:disease_responds_to |
| narrow | RO:0002302 |




## LinkML Source

<details>
```yaml
name: treated by
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- WIKIDATA_PROPERTY:P2176
- MONDO:disease_responds_to
narrow_mappings:
- RO:0002302
rank: 1000
is_a: subject of treatment application or study for treatment by
mixin: true
domain: disease or phenotypic feature
inherited: true
alias: treated_by
inverse: treats
range: chemical or drug or treatment
multivalued: true

```
</details></div>