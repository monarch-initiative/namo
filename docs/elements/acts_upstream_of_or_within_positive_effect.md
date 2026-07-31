---
search:
  boost: 5.0
---

# Slot: acts_upstream_of_or_within_positive_effect 


_Holds between a gene or gene product and a biological process when the gene product acts upstream of or within the process with a positive (activating or increasing) effect on its execution. Corresponds to RO:0004032._



<div data-search-exclude markdown="1">



URI: [namo:acts_upstream_of_or_within_positive_effect](https://w3id.org/monarch-initiative/namo/acts_upstream_of_or_within_positive_effect)
Alias: acts_upstream_of_or_within_positive_effect


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [acts_upstream_of](acts_upstream_of.md)
            * [acts_upstream_of_or_within](acts_upstream_of_or_within.md)
                * **acts_upstream_of_or_within_positive_effect**








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
| self | namo:acts_upstream_of_or_within_positive_effect |
| native | namo:acts_upstream_of_or_within_positive_effect |
| exact | RO:0004032 |




## LinkML Source

<details>
```yaml
name: acts upstream of or within positive effect
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: Holds between a gene or gene product and a biological process when the
  gene product acts upstream of or within the process with a positive (activating
  or increasing) effect on its execution. Corresponds to RO:0004032.
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0004032
rank: 1000
is_a: acts upstream of or within
domain: gene or gene product
inherited: true
alias: acts_upstream_of_or_within_positive_effect
range: biological process
multivalued: true

```
</details></div>