---
search:
  boost: 5.0
---

# Slot: is_frameshift_variant_of 


_holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three._



<div data-search-exclude markdown="1">



URI: [namo:is_frameshift_variant_of](https://w3id.org/monarch-initiative/namo/is_frameshift_variant_of)
Alias: is_frameshift_variant_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [is_sequence_variant_of](is_sequence_variant_of.md)
            * **is_frameshift_variant_of**








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


* frameshift variant
* start lost
* stop lost




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
| self | namo:is_frameshift_variant_of |
| native | namo:is_frameshift_variant_of |
| exact | SO:0001589 |




## LinkML Source

<details>
```yaml
name: is frameshift variant of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a sequence variant and a gene, such the sequence variant
  causes a disruption of the translational reading frame, because the number of nucleotides
  inserted or deleted is not a multiple of three.
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- frameshift variant
- start lost
- stop lost
exact_mappings:
- SO:0001589
rank: 1000
is_a: is sequence variant of
domain: sequence variant
inherited: true
alias: is_frameshift_variant_of
range: genomic entity
multivalued: true

```
</details></div>