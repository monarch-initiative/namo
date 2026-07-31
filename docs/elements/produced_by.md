---
search:
  boost: 5.0
---

# Slot: produced_by 

<div data-search-exclude markdown="1">



URI: [namo:produced_by](https://w3id.org/monarch-initiative/namo/produced_by)
Alias: produced_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **produced_by**








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
| Inverse | [produces](produces.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:produced_by |
| native | namo:produced_by |
| exact | RO:0003001 |




## LinkML Source

<details>
```yaml
name: produced by
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0003001
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: produced_by
inverse: produces
range: named thing
multivalued: true

```
</details></div>