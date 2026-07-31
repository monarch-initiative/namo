---
search:
  boost: 5.0
---

# Slot: positively_correlated_with 


_A relationship that holds between two concepts represented by variables for which a statistical correlation is demonstrated, wherein variable values move together in the same direction (i.e. increased in one or presence of one correlates with an increase or presence of the other)._



<div data-search-exclude markdown="1">



URI: [namo:positively_correlated_with](https://w3id.org/monarch-initiative/namo/positively_correlated_with)
Alias: positively_correlated_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **positively_correlated_with**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [NamedThing](NamedThing.md) |

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
| opposite_of | negatively correlated with |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:positively_correlated_with |
| native | namo:positively_correlated_with |
| exact | CTD:positive_correlation |




## LinkML Source

<details>
```yaml
name: positively correlated with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: negatively correlated with
description: A relationship that holds between two concepts represented by variables
  for which a statistical correlation is demonstrated, wherein variable values move
  together in the same direction (i.e. increased in one or presence of one correlates
  with an increase or presence of the other).
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- CTD:positive_correlation
rank: 1000
is_a: correlated with
domain: named thing
inherited: true
alias: positively_correlated_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>