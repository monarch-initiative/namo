---
search:
  boost: 5.0
---

# Slot: occurs_in 


_holds between a process and a material entity or site within which the process occurs_



<div data-search-exclude markdown="1">



URI: [namo:occurs_in](https://w3id.org/monarch-initiative/namo/occurs_in)
Alias: occurs_in


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **occurs_in**








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
| self | namo:occurs_in |
| native | namo:occurs_in |
| exact | BFO:0000066, PathWhiz:has_location, SNOMED:occurs_in |
| narrow | SEMMEDDB:OCCURS_IN, SEMMEDDB:PROCESS_OF, UBERON_CORE:site_of, LOINC:has_imaged_location, PathWhiz:in_species, RO:0002231, RO:0002232, SNOMED:has_direct_procedure_site, SNOMED:has_direct_site, SNOMED:has_procedure_site |
| close | BFO:0000067, SNOMED:has_occurrence, UBERON:site_of |




## LinkML Source

<details>
```yaml
name: occurs in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a process and a material entity or site within which the
  process occurs
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- BFO:0000066
- PathWhiz:has_location
- SNOMED:occurs_in
close_mappings:
- BFO:0000067
- SNOMED:has_occurrence
- UBERON:site_of
narrow_mappings:
- SEMMEDDB:OCCURS_IN
- SEMMEDDB:PROCESS_OF
- UBERON_CORE:site_of
- LOINC:has_imaged_location
- PathWhiz:in_species
- RO:0002231
- RO:0002232
- SNOMED:has_direct_procedure_site
- SNOMED:has_direct_site
- SNOMED:has_procedure_site
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: occurs_in
range: named thing
multivalued: true

```
</details></div>