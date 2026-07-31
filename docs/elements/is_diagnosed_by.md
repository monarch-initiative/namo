---
search:
  boost: 5.0
---

# Slot: is_diagnosed_by 

<div data-search-exclude markdown="1">



URI: [namo:is_diagnosed_by](https://w3id.org/monarch-initiative/namo/is_diagnosed_by)
Alias: is_diagnosed_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **is_diagnosed_by**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiagnosticAid](DiagnosticAid.md) |
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
| Inverse | [diagnoses](diagnoses.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:is_diagnosed_by |
| native | namo:is_diagnosed_by |




## LinkML Source

<details>
```yaml
name: is diagnosed by
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: disease or phenotypic feature
inherited: true
alias: is_diagnosed_by
inverse: diagnoses
range: diagnostic aid
multivalued: true

```
</details></div>