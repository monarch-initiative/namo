---
search:
  boost: 5.0
---

# Slot: condition_promoted_by 

<div data-search-exclude markdown="1">



URI: [namo:condition_promoted_by](https://w3id.org/monarch-initiative/namo/condition_promoted_by)
Alias: condition_promoted_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [likelihood_affected_by](likelihood_affected_by.md)
            * **condition_promoted_by**







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
| Inverse | [promotes_condition](promotes_condition.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:condition_promoted_by |
| native | namo:condition_promoted_by |




## LinkML Source

<details>
```yaml
name: condition promoted by
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: likelihood affected by
mixin: true
domain: disease or phenotypic feature
inherited: true
alias: condition_promoted_by
inverse: promotes condition
range: chemical or drug or treatment
multivalued: true

```
</details></div>