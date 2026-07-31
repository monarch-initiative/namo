---
search:
  boost: 5.0
---

# Slot: acts_upstream_of_negative_effect 


_Holds between a gene or gene product and a biological process where the molecular function of the gene product is upstream of and has a negative (inhibiting or decreasing) effect on the execution of the process._



<div data-search-exclude markdown="1">



URI: [namo:acts_upstream_of_negative_effect](https://w3id.org/monarch-initiative/namo/acts_upstream_of_negative_effect)
Alias: acts_upstream_of_negative_effect


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [acts_upstream_of](acts_upstream_of.md)
            * **acts_upstream_of_negative_effect**








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
| self | namo:acts_upstream_of_negative_effect |
| native | namo:acts_upstream_of_negative_effect |
| exact | RO:0004035 |




## LinkML Source

<details>
```yaml
name: acts upstream of negative effect
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a gene or gene product and a biological process where the
  molecular function of the gene product is upstream of and has a negative (inhibiting
  or decreasing) effect on the execution of the process.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0004035
rank: 1000
is_a: acts upstream of
domain: gene or gene product
inherited: true
alias: acts_upstream_of_negative_effect
range: biological process
multivalued: true

```
</details></div>