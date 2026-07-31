---
search:
  boost: 5.0
---

# Slot: broad_match 


_a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree._



<div data-search-exclude markdown="1">



URI: [namo:broad_match](https://w3id.org/monarch-initiative/namo/broad_match)
Alias: broad_match


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **broad_match**






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








## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |
| opposite_of | narrow match |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:broad_match |
| native | namo:broad_match |
| exact | skos:broadMatch, WIKIDATA:Q39894595 |




## LinkML Source

<details>
```yaml
name: broad match
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: narrow match
description: a list of terms from different schemas or terminology systems that have
  a broader, more general meaning. Broader terms are typically shown as parents in
  a hierarchy or tree.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- skos:broadMatch
- WIKIDATA:Q39894595
rank: 1000
is_a: related to at concept level
domain: named thing
inherited: true
alias: broad_match
domain_of:
- predicate mapping
range: named thing
multivalued: true

```
</details></div>