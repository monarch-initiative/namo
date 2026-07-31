---
search:
  boost: 5.0
---

# Slot: in_complex_with 


_holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex_



<div data-search-exclude markdown="1">



URI: [namo:in_complex_with](https://w3id.org/monarch-initiative/namo/in_complex_with)
Alias: in_complex_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [coexists_with](coexists_with.md)
            * **in_complex_with**








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







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






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
| self | namo:in_complex_with |
| native | namo:in_complex_with |
| broad | SIO:010285 |
| related | SIO:010497 |




## LinkML Source

<details>
```yaml
name: in complex with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two genes or gene products that are part of (or code for
  products that are part of) in the same macromolecular complex
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
related_mappings:
- SIO:010497
broad_mappings:
- SIO:010285
rank: 1000
is_a: coexists with
domain: gene or gene product
inherited: true
alias: in_complex_with
symmetric: true
range: gene or gene product
multivalued: true

```
</details></div>