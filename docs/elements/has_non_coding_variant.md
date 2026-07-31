---
search:
  boost: 5.0
---

# Slot: has_non_coding_variant 

<div data-search-exclude markdown="1">



URI: [namo:has_non_coding_variant](https://w3id.org/monarch-initiative/namo/has_non_coding_variant)
Alias: has_non_coding_variant


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_sequence_variant](has_sequence_variant.md)
            * **has_non_coding_variant**








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
| Inverse | [is_non_coding_variant_of](is_non_coding_variant_of.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_non_coding_variant |
| native | namo:has_non_coding_variant |




## LinkML Source

<details>
```yaml
name: has non coding variant
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has sequence variant
domain: genomic entity
inherited: true
alias: has_non_coding_variant
inverse: is non coding variant of
range: sequence variant
multivalued: true

```
</details></div>