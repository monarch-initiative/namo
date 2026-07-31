---
search:
  boost: 5.0
---

# Slot: same_as 


_holds between two entities that are considered equivalent to each other_



<div data-search-exclude markdown="1">



URI: [namo:same_as](https://w3id.org/monarch-initiative/namo/same_as)
Alias: same_as


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * [close_match](close_match.md)
            * [exact_match](exact_match.md)
                * **same_as**








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
| self | namo:same_as |
| native | namo:same_as |
| exact | owl:sameAs, skos:exactMatch, WIKIDATA_PROPERTY:P2888, CHEMBL.MECHANISM:equivalent_to, MONDO:equivalentTo |
| narrow | DRUGBANK:external-identifier |
| close | owl:equivalentClass |




## LinkML Source

<details>
```yaml
name: same as
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two entities that are considered equivalent to each other
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- owl:sameAs
- skos:exactMatch
- WIKIDATA_PROPERTY:P2888
- CHEMBL.MECHANISM:equivalent_to
- MONDO:equivalentTo
close_mappings:
- owl:equivalentClass
narrow_mappings:
- DRUGBANK:external-identifier
rank: 1000
is_a: exact match
domain: named thing
inherited: true
alias: same_as
symmetric: true
range: named thing
multivalued: true

```
</details></div>