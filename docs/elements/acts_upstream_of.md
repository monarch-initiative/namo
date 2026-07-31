---
search:
  boost: 5.0
---

# Slot: acts_upstream_of 


_Holds between a gene or gene product and a biological process such that the molecular function of the gene product, by way of a chain of causally linked events, is upstream of and contributes to the execution of the process._



<div data-search-exclude markdown="1">



URI: [namo:acts_upstream_of](https://w3id.org/monarch-initiative/namo/acts_upstream_of)
Alias: acts_upstream_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **acts_upstream_of**
            * [acts_upstream_of_positive_effect](acts_upstream_of_positive_effect.md)
            * [acts_upstream_of_negative_effect](acts_upstream_of_negative_effect.md)
            * [acts_upstream_of_or_within](acts_upstream_of_or_within.md)








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
| self | namo:acts_upstream_of |
| native | namo:acts_upstream_of |
| exact | RO:0002263 |




## LinkML Source

<details>
```yaml
name: acts upstream of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a gene or gene product and a biological process such that
  the molecular function of the gene product, by way of a chain of causally linked
  events, is upstream of and contributes to the execution of the process.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002263
rank: 1000
is_a: related to at instance level
domain: gene or gene product
inherited: true
alias: acts_upstream_of
range: biological process
multivalued: true

```
</details></div>