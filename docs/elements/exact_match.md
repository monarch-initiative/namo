---
search:
  boost: 5.0
---

# Slot: exact_match 


_holds between two entities that have strictly equivalent meanings, with a high degree of confidence_



<div data-search-exclude markdown="1">



URI: [namo:exact_match](https://w3id.org/monarch-initiative/namo/exact_match)
Alias: exact_match


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * [close_match](close_match.md)
            * **exact_match**
                * [same_as](same_as.md)






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NamedThing](NamedThing.md) |
| Domain | [NamedThing](NamedThing.md) |
| Domain Of | [PredicateMapping](PredicateMapping.md) |

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
| self | namo:exact_match |
| native | namo:exact_match |
| exact | skos:exactMatch, WIKIDATA:Q39893449, WIKIDATA:P2888 |




## LinkML Source

<details>
```yaml
name: exact match
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two entities that have strictly equivalent meanings, with
  a high degree of confidence
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- skos:exactMatch
- WIKIDATA:Q39893449
- WIKIDATA:P2888
rank: 1000
is_a: close match
domain: named thing
inherited: true
alias: exact_match
domain_of:
- predicate mapping
symmetric: true
range: named thing
multivalued: true

```
</details></div>