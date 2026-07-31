---
search:
  boost: 5.0
---

# Slot: occurs_together_in_literature_with 


_holds between two entities where their co-occurrence is correlated by counts of publications in which both occur, using some threshold of occurrence as defined by the edge provider._



<div data-search-exclude markdown="1">



URI: [namo:occurs_together_in_literature_with](https://w3id.org/monarch-initiative/namo/occurs_together_in_literature_with)
Alias: occurs_together_in_literature_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **occurs_together_in_literature_with**








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




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:occurs_together_in_literature_with |
| native | namo:occurs_together_in_literature_with |




## LinkML Source

<details>
```yaml
name: occurs together in literature with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two entities where their co-occurrence is correlated by
  counts of publications in which both occur, using some threshold of occurrence as
  defined by the edge provider.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
is_a: correlated with
domain: named thing
inherited: true
alias: occurs_together_in_literature_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>