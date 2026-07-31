---
search:
  boost: 5.0
---

# Slot: has_provider 

<div data-search-exclude markdown="1">



URI: [namo:has_provider](https://w3id.org/monarch-initiative/namo/has_provider)
Alias: has_provider


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_contributor](has_contributor.md)
            * **has_provider**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain | [InformationContentEntity](InformationContentEntity.md) |

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
| Inverse | [provider](provider.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_provider |
| native | namo:has_provider |




## LinkML Source

<details>
```yaml
name: has provider
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has contributor
domain: information content entity
inherited: true
alias: has_provider
inverse: provider
range: agent
multivalued: true

```
</details></div>