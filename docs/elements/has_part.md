---
search:
  boost: 5.0
---

# Slot: has_part 


_holds between wholes and their parts (material entities or processes)_



<div data-search-exclude markdown="1">



URI: [namo:has_part](https://w3id.org/monarch-initiative/namo/has_part)
Alias: has_part


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * **has_part**
                * [has_plasma_membrane_part](has_plasma_membrane_part.md)
                * [has_food_component](has_food_component.md)
                * [has_active_ingredient](has_active_ingredient.md)
                * [has_excipient](has_excipient.md)
                * [has_variant_part](has_variant_part.md)








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
| opposite_of | lacks part |




### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_part |
| native | namo:has_part |
| exact | BFO:0000051, BFO:0000055, WIKIDATA_PROPERTY:P527, RO:0001019, RXNORM:consists_of, RXNORM:has_part |
| narrow | BFO:0000117, FMA:has_constitutional_part, FMA:has_part, FMA:has_member, FOODON:00001563, FOODON:00002420, LOINC:has_component, LOINC:has_member, MEDDRA:has_member, MONDO:disease_has_major_feature, NCIT:complex_has_physical_part, NDDF:has_ingredient, PathWhiz:has_element_in_bound, NCIT:R50, PathWhiz:has_protein_in_complex, RO:0002104, RO:0002180, RO:0002351, RO:0002473, RO:0002524, RO:0002551, RXNORM:has_ingredient, SNOMED:has_component, UMLS:has_component |
| broad | RO:0001019, FMA:contains, RXNORM:contains |




## LinkML Source

<details>
```yaml
name: has part
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
  opposite_of:
    tag: opposite_of
    value: lacks part
description: holds between wholes and their parts (material entities or processes)
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- BFO:0000051
- BFO:0000055
- WIKIDATA_PROPERTY:P527
- RO:0001019
- RXNORM:consists_of
- RXNORM:has_part
narrow_mappings:
- BFO:0000117
- FMA:has_constitutional_part
- FMA:has_part
- FMA:has_member
- FOODON:00001563
- FOODON:00002420
- LOINC:has_component
- LOINC:has_member
- MEDDRA:has_member
- MONDO:disease_has_major_feature
- NCIT:complex_has_physical_part
- NDDF:has_ingredient
- PathWhiz:has_element_in_bound
- NCIT:R50
- PathWhiz:has_protein_in_complex
- RO:0002104
- RO:0002180
- RO:0002351
- RO:0002473
- RO:0002524
- RO:0002551
- RXNORM:has_ingredient
- SNOMED:has_component
- UMLS:has_component
broad_mappings:
- RO:0001019
- FMA:contains
- RXNORM:contains
rank: 1000
is_a: overlaps
domain: named thing
inherited: true
alias: has_part
range: named thing
multivalued: true

```
</details></div>