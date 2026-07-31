---
search:
  boost: 5.0
---

# Slot: has_positive_upstream_or_within_actor 

<div data-search-exclude markdown="1">



URI: [namo:has_positive_upstream_or_within_actor](https://w3id.org/monarch-initiative/namo/has_positive_upstream_or_within_actor)
Alias: has_positive_upstream_or_within_actor


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_upstream_actor](has_upstream_actor.md)
            * [has_upstream_or_within_actor](has_upstream_or_within_actor.md)
                * **has_positive_upstream_or_within_actor**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneOrGeneProduct](GeneOrGeneProduct.md) |
| Domain | [BiologicalProcess](BiologicalProcess.md) |

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
| Inverse | [acts_upstream_of_or_within_positive_effect](acts_upstream_of_or_within_positive_effect.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_positive_upstream_or_within_actor |
| native | namo:has_positive_upstream_or_within_actor |




## LinkML Source

<details>
```yaml
name: has positive upstream or within actor
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has upstream or within actor
domain: biological process
inherited: true
alias: has_positive_upstream_or_within_actor
inverse: acts upstream of or within positive effect
range: gene or gene product
multivalued: true

```
</details></div>