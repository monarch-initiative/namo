---
search:
  boost: 5.0
---

# Slot: adverse_event_of 

<div data-search-exclude markdown="1">



URI: [namo:adverse_event_of](https://w3id.org/monarch-initiative/namo/adverse_event_of)
Alias: adverse_event_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affected_by](affected_by.md)
            * **adverse_event_of**








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
| Inverse | [has_adverse_event](has_adverse_event.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:adverse_event_of |
| native | namo:adverse_event_of |




## LinkML Source

<details>
```yaml
name: adverse event of
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: affected by
domain: disease or phenotypic feature
inherited: true
alias: adverse_event_of
inverse: has adverse event
range: chemical or drug or treatment
multivalued: true

```
</details></div>