---
search:
  boost: 5.0
---

# Slot: coexpressed_with 


_holds between any two genes or gene products, in which both are generally expressed within a single defined experimental context._



<div data-search-exclude markdown="1">



URI: [namo:coexpressed_with](https://w3id.org/monarch-initiative/namo/coexpressed_with)
Alias: coexpressed_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **coexpressed_with**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GeneOrGeneProduct](GeneOrGeneProduct.md) |
| Domain | [GeneOrGeneProduct](GeneOrGeneProduct.md) |

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
| Symmetric | Yes |

</details>











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
| self | namo:coexpressed_with |
| native | namo:coexpressed_with |




## LinkML Source

<details>
```yaml
name: coexpressed with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between any two genes or gene products, in which both are generally
  expressed within a single defined experimental context.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: correlated with
domain: gene or gene product
inherited: true
alias: coexpressed_with
symmetric: true
range: gene or gene product
multivalued: true

```
</details></div>