---
search:
  boost: 5.0
---

# Slot: indirectly_physically_interacts_with 


_Holds between two entities that physically interact by way of one or more intermediary entities, rather than through direct physical contact._



<div data-search-exclude markdown="1">



URI: [namo:indirectly_physically_interacts_with](https://w3id.org/monarch-initiative/namo/indirectly_physically_interacts_with)
Alias: indirectly_physically_interacts_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [physically_interacts_with](physically_interacts_with.md) [ [interacts_with](interacts_with.md)]
                * **indirectly_physically_interacts_with**








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
| Symmetric | Yes |

</details>











## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:indirectly_physically_interacts_with |
| native | namo:indirectly_physically_interacts_with |




## LinkML Source

<details>
```yaml
name: indirectly physically interacts with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between two entities that physically interact by way of one or
  more intermediary entities, rather than through direct physical contact.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: physically interacts with
domain: named thing
inherited: true
alias: indirectly_physically_interacts_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>