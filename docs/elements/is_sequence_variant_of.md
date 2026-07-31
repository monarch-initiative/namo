---
search:
  boost: 5.0
---

# Slot: is_sequence_variant_of 


_holds between a sequence variant and a nucleic acid entity_



<div data-search-exclude markdown="1">



URI: [namo:is_sequence_variant_of](https://w3id.org/monarch-initiative/namo/is_sequence_variant_of)
Alias: is_sequence_variant_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **is_sequence_variant_of**
            * [is_missense_variant_of](is_missense_variant_of.md)
            * [is_synonymous_variant_of](is_synonymous_variant_of.md)
            * [is_nonsense_variant_of](is_nonsense_variant_of.md)
            * [is_frameshift_variant_of](is_frameshift_variant_of.md)
            * [is_splice_site_variant_of](is_splice_site_variant_of.md)
            * [is_nearby_variant_of](is_nearby_variant_of.md)
            * [is_non_coding_variant_of](is_non_coding_variant_of.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GenomicEntity](GenomicEntity.md) |
| Domain | [SequenceVariant](SequenceVariant.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Inherited | Yes |









## Aliases


* gene product sequence variation encoded by gene mutant
* allelic variant of
* gene product variant of gene product




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
| self | namo:is_sequence_variant_of |
| native | namo:is_sequence_variant_of |
| narrow | WIKIDATA:P3433 |




## LinkML Source

<details>
```yaml
name: is sequence variant of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a sequence variant and a nucleic acid entity
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- gene product sequence variation encoded by gene mutant
- allelic variant of
- gene product variant of gene product
narrow_mappings:
- WIKIDATA:P3433
rank: 1000
is_a: related to at instance level
domain: sequence variant
inherited: true
alias: is_sequence_variant_of
range: genomic entity
multivalued: true

```
</details></div>