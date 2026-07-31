---
search:
  boost: 5.0
---

# Slot: correlated_with 


_A relationship that holds between two concepts represented by variables for which a statistical correlation is believed to exist, as demonstrated using a correlation analysis method._



<div data-search-exclude markdown="1">



URI: [namo:correlated_with](https://w3id.org/monarch-initiative/namo/correlated_with)
Alias: correlated_with


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * **correlated_with**
                * [positively_correlated_with](positively_correlated_with.md)
                * [negatively_correlated_with](negatively_correlated_with.md)
                * [occurs_together_in_literature_with](occurs_together_in_literature_with.md)
                * [coexpressed_with](coexpressed_with.md)
                * [has_biomarker](has_biomarker.md)
                * [biomarker_for](biomarker_for.md)








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




## Notes

* These concepts may map exactly to the statistical variables, or represent related entities for which the variables serve as proxies in an Association (e.g. diseases, chemical entities or processes). Note also that this predicate can be used in the absence of a direct statistical analysis, if there is other evidence suggesting that a correlation is likely to exist.



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
| self | namo:correlated_with |
| native | namo:correlated_with |
| exact | RO:0002610, PATO:correlates_with |




## LinkML Source

<details>
```yaml
name: correlated with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A relationship that holds between two concepts represented by variables
  for which a statistical correlation is believed to exist, as demonstrated using
  a correlation analysis method.
notes:
- These concepts may map exactly to the statistical variables, or represent related
  entities for which the variables serve as proxies in an Association (e.g. diseases,
  chemical entities or processes). Note also that this predicate can be used in the
  absence of a direct statistical analysis, if there is other evidence suggesting
  that a correlation is likely to exist.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0002610
- PATO:correlates_with
rank: 1000
is_a: associated with
domain: named thing
inherited: true
alias: correlated_with
symmetric: true
range: named thing
multivalued: true

```
</details></div>