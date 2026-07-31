---
search:
  boost: 5.0
---

# Slot: has_frameshift_variant 

<div data-search-exclude markdown="1">



URI: [namo:has_frameshift_variant](https://w3id.org/monarch-initiative/namo/has_frameshift_variant)
Alias: has_frameshift_variant


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_sequence_variant](has_sequence_variant.md)
            * **has_frameshift_variant**








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
| Inverse | [is_frameshift_variant_of](is_frameshift_variant_of.md) |

</details>








## Aliases


* splice region variant
* splice acceptor variant
* splice donor variant




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_frameshift_variant |
| native | namo:has_frameshift_variant |




## LinkML Source

<details>
```yaml
name: has frameshift variant
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- splice region variant
- splice acceptor variant
- splice donor variant
rank: 1000
is_a: has sequence variant
domain: genomic entity
inherited: true
alias: has_frameshift_variant
inverse: is frameshift variant of
range: sequence variant
multivalued: true

```
</details></div>