---
search:
  boost: 5.0
---

# Slot: consumed_by 

<div data-search-exclude markdown="1">



URI: [namo:consumed_by](https://w3id.org/monarch-initiative/namo/consumed_by)
Alias: consumed_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * [is_input_of](is_input_of.md)
                * **consumed_by**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [NamedThing](NamedThing.md) |

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
| Inverse | [consumes](consumes.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:consumed_by |
| native | namo:consumed_by |




## LinkML Source

<details>
```yaml
name: consumed by
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: is input of
domain: named thing
inherited: true
alias: consumed_by
inverse: consumes
range: named thing
multivalued: true

```
</details></div>