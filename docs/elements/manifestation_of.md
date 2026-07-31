---
search:
  boost: 5.0
---

# Slot: manifestation_of 


_that part of a phenomenon which is directly observable or visibly expressed, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome_



<div data-search-exclude markdown="1">



URI: [namo:manifestation_of](https://w3id.org/monarch-initiative/namo/manifestation_of)
Alias: manifestation_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **manifestation_of**
            * [mode_of_inheritance_of](mode_of_inheritance_of.md)








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Disease](Disease.md) |
| Domain | [NamedThing](NamedThing.md) |

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




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:manifestation_of |
| native | namo:manifestation_of |
| exact | SEMMEDDB:MANIFESTATION_OF, OMIM:manifestation_of |
| narrow | SNOMED:has_definitional_manifestation |
| broad | WIKIDATA_PROPERTY:P1557 |




## LinkML Source

<details>
```yaml
name: manifestation of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: that part of a phenomenon which is directly observable or visibly expressed,
  or which gives evidence to the underlying process; used in SemMedDB for linking
  things like dysfunctions and processes to some disease or syndrome
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SEMMEDDB:MANIFESTATION_OF
- OMIM:manifestation_of
narrow_mappings:
- SNOMED:has_definitional_manifestation
broad_mappings:
- WIKIDATA_PROPERTY:P1557
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: manifestation_of
range: disease
multivalued: true

```
</details></div>