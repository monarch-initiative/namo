---
search:
  boost: 5.0
---

# Slot: has_synonymous_variant 

<div data-search-exclude markdown="1">



URI: [namo:has_synonymous_variant](https://w3id.org/monarch-initiative/namo/has_synonymous_variant)
Alias: has_synonymous_variant


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_sequence_variant](has_sequence_variant.md)
            * **has_synonymous_variant**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SequenceVariant](SequenceVariant.md) |
| Domain | [GenomicEntity](GenomicEntity.md) |

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
| Inverse | [is_synonymous_variant_of](is_synonymous_variant_of.md) |

</details>








## Aliases


* stop gained




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_synonymous_variant |
| native | namo:has_synonymous_variant |




## LinkML Source

<details>
```yaml
name: has synonymous variant
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- stop gained
rank: 1000
is_a: has sequence variant
domain: genomic entity
inherited: true
alias: has_synonymous_variant
inverse: is synonymous variant of
range: sequence variant
multivalued: true

```
</details></div>