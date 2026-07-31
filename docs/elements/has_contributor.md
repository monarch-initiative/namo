---
search:
  boost: 5.0
---

# Slot: has_contributor 

<div data-search-exclude markdown="1">



URI: [namo:has_contributor](https://w3id.org/monarch-initiative/namo/has_contributor)
Alias: has_contributor


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_contributor**
            * [has_provider](has_provider.md)
            * [has_publisher](has_publisher.md)
            * [has_editor](has_editor.md)
            * [has_author](has_author.md)








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
| Inverse | [contributor](contributor.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_contributor |
| native | namo:has_contributor |




## LinkML Source

<details>
```yaml
name: has contributor
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: information content entity
inherited: true
alias: has_contributor
inverse: contributor
range: agent
multivalued: true

```
</details></div>