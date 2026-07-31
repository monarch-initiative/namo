---
search:
  boost: 5.0
---

# Slot: has_sequence_variant 

<div data-search-exclude markdown="1">



URI: [namo:has_sequence_variant](https://w3id.org/monarch-initiative/namo/has_sequence_variant)
Alias: has_sequence_variant


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_sequence_variant**
            * [has_missense_variant](has_missense_variant.md)
            * [has_synonymous_variant](has_synonymous_variant.md)
            * [has_nonsense_variant](has_nonsense_variant.md)
            * [has_frameshift_variant](has_frameshift_variant.md)
            * [has_splice_site_variant](has_splice_site_variant.md)
            * [has_nearby_variant](has_nearby_variant.md)
            * [has_non_coding_variant](has_non_coding_variant.md)








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
| Inverse | [is_sequence_variant_of](is_sequence_variant_of.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_sequence_variant |
| native | namo:has_sequence_variant |




## LinkML Source

<details>
```yaml
name: has sequence variant
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: related to at instance level
domain: genomic entity
inherited: true
alias: has_sequence_variant
inverse: is sequence variant of
range: sequence variant
multivalued: true

```
</details></div>