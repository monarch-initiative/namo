---
search:
  boost: 0.5
---

# Slot: binds  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 


_A causal mechanism mediated by the direct contact between effector and target chemical or biomolecular entity, which form a stable physical interaction._



<div data-search-exclude markdown="1">



URI: [namo:binds](https://w3id.org/monarch-initiative/namo/binds)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [physically_interacts_with](physically_interacts_with.md) [ [interacts_with](interacts_with.md)]
                * [directly_physically_interacts_with](directly_physically_interacts_with.md)
                    * **binds**








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
| self | namo:binds |
| native | namo:binds |
| close | DGIdb:binder |




## LinkML Source

<details>
```yaml
name: binds
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A causal mechanism mediated by the direct contact between effector and
  target chemical or biomolecular entity, which form a stable physical interaction.
deprecated: 'true'
from_schema: https://w3id.org/monarch-initiative/namo
close_mappings:
- DGIdb:binder
rank: 1000
is_a: directly physically interacts with
domain: named thing
inherited: true
symmetric: true
range: named thing
multivalued: true

```
</details></div>