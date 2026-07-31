---
search:
  boost: 5.0
---

# Slot: has_missense_variant 

<div data-search-exclude markdown="1">



URI: [namo:has_missense_variant](https://w3id.org/monarch-initiative/namo/has_missense_variant)
Alias: has_missense_variant


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_sequence_variant](has_sequence_variant.md)
            * **has_missense_variant**








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
| Inverse | [is_missense_variant_of](is_missense_variant_of.md) |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_missense_variant |
| native | namo:has_missense_variant |




## LinkML Source

<details>
```yaml
name: has missense variant
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: has sequence variant
domain: genomic entity
inherited: true
alias: has_missense_variant
inverse: is missense variant of
range: sequence variant
multivalued: true

```
</details></div>