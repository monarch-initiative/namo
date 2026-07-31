---
search:
  boost: 5.0
---

# Slot: temporally_related_to 


_holds between two entities with a temporal relationship_



<div data-search-exclude markdown="1">



URI: [namo:temporally_related_to](https://w3id.org/monarch-initiative/namo/temporally_related_to)
Alias: temporally_related_to


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **temporally_related_to**
            * [precedes](precedes.md)
            * [preceded_by](preceded_by.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Occurrent](Occurrent.md) |
| Domain | [Occurrent](Occurrent.md) |

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
| self | namo:temporally_related_to |
| native | namo:temporally_related_to |
| exact | SNOMED:temporally_related_to |
| narrow | RO:0002082, RO:0002083, RO:0002092, RO:0002093, RO:0002223, RO:0002224, RO:0002229, RO:0002230, RO:0002488, RO:0002489, RO:0002492, RO:0002493, RO:0002496, RO:0002497 |




## LinkML Source

<details>
```yaml
name: temporally related to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two entities with a temporal relationship
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SNOMED:temporally_related_to
narrow_mappings:
- RO:0002082
- RO:0002083
- RO:0002092
- RO:0002093
- RO:0002223
- RO:0002224
- RO:0002229
- RO:0002230
- RO:0002488
- RO:0002489
- RO:0002492
- RO:0002493
- RO:0002496
- RO:0002497
rank: 1000
is_a: related to at instance level
domain: occurrent
inherited: true
alias: temporally_related_to
symmetric: true
range: occurrent
multivalued: true

```
</details></div>