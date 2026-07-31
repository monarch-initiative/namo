---
search:
  boost: 5.0
---

# Slot: opposite_of 


_x is the opposite of y if there exists some distance metric M, and there exists no z such as M(x,z) <= M(x,y) or M(y,z) <= M(y,x). (This description is from RO. Needs to be rephrased)._



<div data-search-exclude markdown="1">



URI: [namo:opposite_of](https://w3id.org/monarch-initiative/namo/opposite_of)
Alias: opposite_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **opposite_of**








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









## See Also

* [https://doi.org/10.1101/108977](https://doi.org/10.1101/108977)
* [https://github.com/biolink/biolink-model/issues/657](https://github.com/biolink/biolink-model/issues/657)



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
| self | namo:opposite_of |
| native | namo:opposite_of |
| exact | RO:0002604 |




## LinkML Source

<details>
```yaml
name: opposite of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: x is the opposite of y if there exists some distance metric M, and there
  exists no z such as M(x,z) <= M(x,y) or M(y,z) <= M(y,x). (This description is from
  RO. Needs to be rephrased).
from_schema: https://w3id.org/monarch-initiative/namo
see_also:
- https://doi.org/10.1101/108977
- https://github.com/biolink/biolink-model/issues/657
exact_mappings:
- RO:0002604
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: opposite_of
symmetric: true
range: named thing
multivalued: true

```
</details></div>