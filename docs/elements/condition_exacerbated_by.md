---
search:
  boost: 5.0
---

# Slot: condition_exacerbated_by 

<div data-search-exclude markdown="1">



URI: [namo:condition_exacerbated_by](https://w3id.org/monarch-initiative/namo/condition_exacerbated_by)
Alias: condition_exacerbated_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affected_by](affected_by.md)
            * **condition_exacerbated_by**








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
| Inverse | [exacerbates_condition](exacerbates_condition.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:condition_exacerbated_by |
| native | namo:condition_exacerbated_by |




## LinkML Source

<details>
```yaml
name: condition exacerbated by
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: affected by
domain: disease or phenotypic feature
inherited: true
alias: condition_exacerbated_by
inverse: exacerbates condition
range: chemical or drug or treatment
multivalued: true

```
</details></div>