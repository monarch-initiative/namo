---
search:
  boost: 5.0
---

# Slot: regulated_by 

<div data-search-exclude markdown="1">



URI: [namo:regulated_by](https://w3id.org/monarch-initiative/namo/regulated_by)
Alias: regulated_by


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affected_by](affected_by.md)
            * **regulated_by**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) |
| Domain | [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) |

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
| Inverse | [regulates](regulates.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:regulated_by |
| native | namo:regulated_by |




## LinkML Source

<details>
```yaml
name: regulated by
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: affected by
domain: physical essence or occurrent
inherited: true
alias: regulated_by
inverse: regulates
range: physical essence or occurrent
multivalued: true

```
</details></div>