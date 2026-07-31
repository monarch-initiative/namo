---
search:
  boost: 5.0
---

# Slot: acts_upstream_of_or_within 


_Holds between a gene or gene product and a biological process when the gene product either acts upstream of the process or participates in it; used when the more specific causal relationship is not known. Corresponds to RO:0002264._



<div data-search-exclude markdown="1">



URI: [namo:acts_upstream_of_or_within](https://w3id.org/monarch-initiative/namo/acts_upstream_of_or_within)
Alias: acts_upstream_of_or_within


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [acts_upstream_of](acts_upstream_of.md)
            * **acts_upstream_of_or_within**
                * [acts_upstream_of_or_within_positive_effect](acts_upstream_of_or_within_positive_effect.md)
                * [acts_upstream_of_or_within_negative_effect](acts_upstream_of_or_within_negative_effect.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiologicalProcess](BiologicalProcess.md) |
| Domain | [GeneOrGeneProduct](GeneOrGeneProduct.md) |

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
| self | namo:acts_upstream_of_or_within |
| native | namo:acts_upstream_of_or_within |
| exact | RO:0002264 |




## LinkML Source

<details>
```yaml
name: acts upstream of or within
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a gene or gene product and a biological process when the
  gene product either acts upstream of the process or participates in it; used when
  the more specific causal relationship is not known. Corresponds to RO:0002264.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002264
rank: 1000
is_a: acts upstream of
domain: gene or gene product
inherited: true
alias: acts_upstream_of_or_within
range: biological process
multivalued: true

```
</details></div>