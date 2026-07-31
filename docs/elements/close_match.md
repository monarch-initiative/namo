---
search:
  boost: 5.0
---

# Slot: close_match 


_a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives._



<div data-search-exclude markdown="1">



URI: [namo:close_match](https://w3id.org/monarch-initiative/namo/close_match)
Alias: close_match


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **close_match**
            * [exact_match](exact_match.md)








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
| self | namo:close_match |
| native | namo:close_match |
| exact | skos:closeMatch, SEMMEDDB:same_as |
| narrow | CHEBI:is_enantiomer_of, CHEBI:is_tautomer_of, MEDDRA:classified_as, oboInOwl:hasDbXref, RXNORM:has_quantified_form, UMLS:SY |




## LinkML Source

<details>
```yaml
name: close match
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: a list of terms from different schemas or terminology systems that have
  a semantically similar but not strictly equivalent, broader, or narrower meaning.
  Such terms often describe the same general concept from different ontological perspectives.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- skos:closeMatch
- SEMMEDDB:same_as
narrow_mappings:
- CHEBI:is_enantiomer_of
- CHEBI:is_tautomer_of
- MEDDRA:classified_as
- oboInOwl:hasDbXref
- RXNORM:has_quantified_form
- UMLS:SY
rank: 1000
is_a: related to at concept level
domain: named thing
inherited: true
alias: close_match
symmetric: true
range: named thing
multivalued: true

```
</details></div>