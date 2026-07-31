---
search:
  boost: 5.0
---

# Slot: has_nearby_variant 

<div data-search-exclude markdown="1">



URI: [namo:has_nearby_variant](https://w3id.org/monarch-initiative/namo/has_nearby_variant)
Alias: has_nearby_variant


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_sequence_variant](has_sequence_variant.md)
            * **has_nearby_variant**








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
| Inverse | [is_nearby_variant_of](is_nearby_variant_of.md) |

</details>








## Aliases


* intron variant
* 3 prime UTR variant
* 5 prime UTR variant
* 5 prime UTR premature start codon gain variant
* non coding transcript exon variant




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_nearby_variant |
| native | namo:has_nearby_variant |




## LinkML Source

<details>
```yaml
name: has nearby variant
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- intron variant
- 3 prime UTR variant
- 5 prime UTR variant
- 5 prime UTR premature start codon gain variant
- non coding transcript exon variant
rank: 1000
is_a: has sequence variant
domain: genomic entity
inherited: true
alias: has_nearby_variant
inverse: is nearby variant of
range: sequence variant
multivalued: true

```
</details></div>