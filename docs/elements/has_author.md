---
search:
  boost: 5.0
---

# Slot: has_author 

<div data-search-exclude markdown="1">



URI: [namo:has_author](https://w3id.org/monarch-initiative/namo/has_author)
Alias: has_author


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_contributor](has_contributor.md)
            * **has_author**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Agent](Agent.md) |
| Domain | [Publication](Publication.md) |

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
| Inverse | [author](author.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_author |
| native | namo:has_author |




## LinkML Source

<details>
```yaml
name: has author
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has contributor
domain: publication
inherited: true
alias: has_author
inverse: author
range: agent
multivalued: true

```
</details></div>