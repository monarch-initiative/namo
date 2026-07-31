---
search:
  boost: 5.0
---

# Slot: has_manifestation 

<div data-search-exclude markdown="1">



URI: [namo:has_manifestation](https://w3id.org/monarch-initiative/namo/has_manifestation)
Alias: has_manifestation


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_manifestation**
            * [has_mode_of_inheritance](has_mode_of_inheritance.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
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
| Inverse | [manifestation_of](manifestation_of.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_manifestation |
| native | namo:has_manifestation |




## LinkML Source

<details>
```yaml
name: has manifestation
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: disease
inherited: true
alias: has_manifestation
inverse: manifestation of
range: named thing
multivalued: true

```
</details></div>