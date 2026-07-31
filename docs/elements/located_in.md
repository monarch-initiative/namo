---
search:
  boost: 5.0
---

# Slot: located_in 


_holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)_



<div data-search-exclude markdown="1">



URI: [namo:located_in](https://w3id.org/monarch-initiative/namo/located_in)
Alias: located_in


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **located_in**
            * [expressed_in](expressed_in.md)








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
| self | namo:located_in |
| native | namo:located_in |
| exact | RO:0001025, FMA:has_location |
| narrow | GOREL:0001004, BSPO:0000107, BSPO:0000108, BSPO:0000120, BSPO:0000121, BSPO:0000122, BSPO:0000123, BSPO:0000124, BSPO:0000125, BSPO:0000126, BSPO:0001100, BSPO:0001101, BSPO:0001107, BSPO:0015101, BSPO:0015102, BSPO:0015202, UBERON_CORE:in_central_side_of, UBERON_CORE:in_innermost_side_of, UBERON_CORE:in_outermost_side_of, NCIT:R100, EFO:0000784, FMA:has_location, HMDB:at_cellular_location, HMDB:at_tissue, HMDB:in_biospecimen, LOINC:has_imaging_focus, NCIT:R156, NCIT:R155, NCIT:R145, NCIT:R40, NCIT:R171, NCIT:R167, NCIT:R165, NCIT:R169, NCIT:R170, NCIT:R166, NCIT:R168, RO:0002303, SNOMED:has_finding_site, SNOMED:has_indirect_procedure_site, SNOMED:has_inherent_location |




## LinkML Source

<details>
```yaml
name: located in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a material entity and a material entity or site within
  which it is located (but of which it is not considered a part)
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- RO:0001025
- FMA:has_location
narrow_mappings:
- GOREL:0001004
- BSPO:0000107
- BSPO:0000108
- BSPO:0000120
- BSPO:0000121
- BSPO:0000122
- BSPO:0000123
- BSPO:0000124
- BSPO:0000125
- BSPO:0000126
- BSPO:0001100
- BSPO:0001101
- BSPO:0001107
- BSPO:0015101
- BSPO:0015102
- BSPO:0015202
- UBERON_CORE:in_central_side_of
- UBERON_CORE:in_innermost_side_of
- UBERON_CORE:in_outermost_side_of
- NCIT:R100
- EFO:0000784
- FMA:has_location
- HMDB:at_cellular_location
- HMDB:at_tissue
- HMDB:in_biospecimen
- LOINC:has_imaging_focus
- NCIT:R156
- NCIT:R155
- NCIT:R145
- NCIT:R40
- NCIT:R171
- NCIT:R167
- NCIT:R165
- NCIT:R169
- NCIT:R170
- NCIT:R166
- NCIT:R168
- RO:0002303
- SNOMED:has_finding_site
- SNOMED:has_indirect_procedure_site
- SNOMED:has_inherent_location
rank: 1000
is_a: related to at instance level
domain: named thing
inherited: true
alias: located_in
range: named thing
multivalued: true

```
</details></div>