---
search:
  boost: 5.0
---

# Slot: has_target 

<div data-search-exclude markdown="1">



URI: [namo:has_target](https://w3id.org/monarch-initiative/namo/has_target)
Alias: has_target


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_target**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Gene](Gene.md) |
| Domain | [Disease](Disease.md) |

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
| Inverse | [target_for](target_for.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_target |
| native | namo:has_target |




## LinkML Source

<details>
```yaml
name: has target
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: disease
inherited: true
alias: has_target
inverse: target for
range: gene
multivalued: true

```
</details></div>