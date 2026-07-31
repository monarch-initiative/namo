---
search:
  boost: 5.0
---

# Slot: is_side_effect_of 

<div data-search-exclude markdown="1">



URI: [namo:is_side_effect_of](https://w3id.org/monarch-initiative/namo/is_side_effect_of)
Alias: is_side_effect_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affected_by](affected_by.md)
            * **is_side_effect_of**








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
| Inverse | [has_side_effect](has_side_effect.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_side_effect_of |
| native | namo:is_side_effect_of |




## LinkML Source

<details>
```yaml
name: is side effect of
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: affected by
domain: disease or phenotypic feature
inherited: true
alias: is_side_effect_of
inverse: has side effect
range: chemical or drug or treatment
multivalued: true

```
</details></div>