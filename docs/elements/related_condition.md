---
search:
  boost: 5.0
---

# Slot: related_condition 


_Links a genotype or genetic variant to a condition (disease or phenotypic feature) that is associated with it._



<div data-search-exclude markdown="1">



URI: [namo:related_condition](https://w3id.org/monarch-initiative/namo/related_condition)
Alias: related_condition


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **related_condition**








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
| self | namo:related_condition |
| native | namo:related_condition |
| exact | GENO:0000790 |




## LinkML Source

<details>
```yaml
name: related condition
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Links a genotype or genetic variant to a condition (disease or phenotypic
  feature) that is associated with it.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- GENO:0000790
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: related_condition
symmetric: true
range: named thing
multivalued: true

```
</details></div>