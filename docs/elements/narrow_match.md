---
search:
  boost: 5.0
---

# Slot: narrow_match 


_a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree._



<div data-search-exclude markdown="1">



URI: [namo:narrow_match](https://w3id.org/monarch-initiative/namo/narrow_match)
Alias: narrow_match


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **narrow_match**






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
| Inverse | [broad_match](broad_match.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| opposite_of | broad match |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:narrow_match |
| native | namo:narrow_match |
| exact | skos:narrowMatch, WIKIDATA:Q39893967 |




## LinkML Source

<details>
```yaml
name: narrow match
annotations:
  opposite_of:
    tag: opposite_of
    value: broad match
description: a list of terms from different schemas or terminology systems that have
  a narrower, more specific meaning. Narrower terms are typically shown as children
  in a hierarchy or tree.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- skos:narrowMatch
- WIKIDATA:Q39893967
rank: 1000
is_a: related to at concept level
domain: named thing
inherited: true
alias: narrow_match
domain_of:
- predicate mapping
inverse: broad match
range: named thing
multivalued: true

```
</details></div>