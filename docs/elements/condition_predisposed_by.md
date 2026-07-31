---
search:
  boost: 5.0
---

# Slot: condition_predisposed_by 

<div data-search-exclude markdown="1">



URI: [namo:condition_predisposed_by](https://w3id.org/monarch-initiative/namo/condition_predisposed_by)
Alias: condition_predisposed_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [likelihood_affected_by](likelihood_affected_by.md)
            * **condition_predisposed_by**








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
| Inverse | [predisposes_to_condition](predisposes_to_condition.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:condition_predisposed_by |
| native | namo:condition_predisposed_by |




## LinkML Source

<details>
```yaml
name: condition predisposed by
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: likelihood affected by
domain: disease or phenotypic feature
inherited: true
alias: condition_predisposed_by
inverse: predisposes to condition
range: chemical or drug or treatment
multivalued: true

```
</details></div>