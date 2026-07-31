---
search:
  boost: 5.0
---

# Slot: is_missense_variant_of 


_holds between a gene  and a sequence variant, such the sequence variant results in a different amino acid sequence but where the length is preserved._



<div data-search-exclude markdown="1">



URI: [namo:is_missense_variant_of](https://w3id.org/monarch-initiative/namo/is_missense_variant_of)
Alias: is_missense_variant_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [is_sequence_variant_of](is_sequence_variant_of.md)
            * **is_missense_variant_of**








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
| self | namo:is_missense_variant_of |
| native | namo:is_missense_variant_of |
| exact | SO:0001583 |




## LinkML Source

<details>
```yaml
name: is missense variant of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a gene  and a sequence variant, such the sequence variant
  results in a different amino acid sequence but where the length is preserved.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SO:0001583
rank: 1000
is_a: is sequence variant of
domain: sequence variant
inherited: true
alias: is_missense_variant_of
range: genomic entity
multivalued: true

```
</details></div>