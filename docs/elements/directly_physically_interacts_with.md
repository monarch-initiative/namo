---
search:
  boost: 5.0
---

# Slot: directly_physically_interacts_with 


_A causal mechanism mediated by a direct contact between the effector and target entities (this contact may be weak or strong, transient or stable)._



<div data-search-exclude markdown="1">



URI: [namo:directly_physically_interacts_with](https://w3id.org/monarch-initiative/namo/directly_physically_interacts_with)
Alias: directly_physically_interacts_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [physically_interacts_with](physically_interacts_with.md) [ [interacts_with](interacts_with.md)]
                * **directly_physically_interacts_with**
                    * [binds](binds.md)








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
| self | namo:directly_physically_interacts_with |
| native | namo:directly_physically_interacts_with |
| exact | RO:0002436 |
| narrow | PHAROS:drug_targets, DRUGBANK:chelator, CTD:affects_binding, DGIdb:cofactor |
| broad | SIO:000203, RO:0002578 |




## LinkML Source

<details>
```yaml
name: directly physically interacts with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A causal mechanism mediated by a direct contact between the effector
  and target entities (this contact may be weak or strong, transient or stable).
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002436
narrow_mappings:
- PHAROS:drug_targets
- DRUGBANK:chelator
- CTD:affects_binding
- DGIdb:cofactor
broad_mappings:
- SIO:000203
- RO:0002578
rank: 1000
is_a: physically interacts with
domain: named thing
inherited: true
alias: directly_physically_interacts_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>