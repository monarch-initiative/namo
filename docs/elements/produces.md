---
search:
  boost: 5.0
---

# Slot: produces 


_holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity_



<div data-search-exclude markdown="1">



URI: [namo:produces](https://w3id.org/monarch-initiative/namo/produces)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **produces**








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
| self | namo:produces |
| native | namo:produces |
| exact | RO:0003000, WIKIDATA_PROPERTY:P1056, SEMMEDDB:PRODUCES |
| narrow | NCIT:R29, SNOMED:has_process_output, SNOMED:specimen_procedure_of |
| related | GOREL:0001010 |




## LinkML Source

<details>
```yaml
name: produces
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a material entity and a product that is generated through
  the intentional actions or functioning of the material entity
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0003000
- WIKIDATA_PROPERTY:P1056
- SEMMEDDB:PRODUCES
related_mappings:
- GOREL:0001010
narrow_mappings:
- NCIT:R29
- SNOMED:has_process_output
- SNOMED:specimen_procedure_of
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
range: named thing
multivalued: true

```
</details></div>