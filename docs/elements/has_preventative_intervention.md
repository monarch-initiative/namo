---
search:
  boost: 5.0
---

# Slot: has_preventative_intervention 

<div data-search-exclude markdown="1">



URI: [namo:has_preventative_intervention](https://w3id.org/monarch-initiative/namo/has_preventative_intervention)
Alias: has_preventative_intervention


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [likelihood_affected_by](likelihood_affected_by.md)
            * **has_preventative_intervention**








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
| Inverse | [preventative_for_condition](preventative_for_condition.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_preventative_intervention |
| native | namo:has_preventative_intervention |




## LinkML Source

<details>
```yaml
name: has preventative intervention
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: likelihood affected by
domain: disease or phenotypic feature
inherited: true
alias: has_preventative_intervention
inverse: preventative for condition
range: chemical or drug or treatment
multivalued: true

```
</details></div>