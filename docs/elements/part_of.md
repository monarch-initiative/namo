---
search:
  boost: 5.0
---

# Slot: part_of 


_holds between parts and wholes (material entities or processes)_



<div data-search-exclude markdown="1">



URI: [namo:part_of](https://w3id.org/monarch-initiative/namo/part_of)
Alias: part_of


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * **part_of**
                * [plasma_membrane_part_of](plasma_membrane_part_of.md)
                * [food_component_of](food_component_of.md)
                * [is_active_ingredient_of](is_active_ingredient_of.md)
                * [is_excipient_of](is_excipient_of.md)
                * [variant_part_of](variant_part_of.md)








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
| Inverse | [has_part](has_part.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:part_of |
| native | namo:part_of |
| exact | BFO:0000050, SEMMEDDB:PART_OF, WIKIDATA_PROPERTY:P361, FMA:part_of, RXNORM:constitutes, RXNORM:part_of |
| narrow | BSPO:0001106, BSPO:0001108, BSPO:0001113, BSPO:0001115, UBERON_CORE:layer_part_of, UBERON_CORE:subdivision_of, UBERON_CORE:trunk_part_of, CHEBI:is_substituent_group_from, CPT:panel_element_of, CPT:panel_element_of_possibly_included, DRUGBANK:component_of, FMA:constitutional_part_of, FMA:member_of, FMA:regional_part_of, FMA:related_developmental_entity_of, LOINC:component_of, LOINC:has_supersystem, LOINC:member_of, LOINC:multipart_of, MEDDRA:member_of, MONDO:part_of_progression_of_disease, NCIT:R82, NCIT:R27, NCIT:is_component_of_chemotherapy_regimen, NDDF:ingredient_of, RO:0002007, RO:0002350, RO:0002376, RO:0002380, RO:0002571, RO:0002572, RO:0002576, RXNORM:ingredient_of, RXNORM:ingredients_of, RXNORM:precise_ingredient_of, SNOMED:active_ingredient_of, SNOMED:basis_of_strength_substance_of, SNOMED:component_of, SNOMED:direct_substance_of, SNOMED:during, SNOMED:focus_of, SNOMED:has_dependent, SNOMED:part_anatomy_structure_of, SNOMED:precise_active_ingredient_of, UBERON:subdivision_of, UMLS:component_of, UMLS:has_owning_affiliate, UMLS:owning_subsection_of, VANDF:ingredient_of |
| broad | RO:0001018, FMA:contained_in, RXNORM:contained_in |




## LinkML Source

<details>
```yaml
name: part of
description: holds between parts and wholes (material entities or processes)
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- BFO:0000050
- SEMMEDDB:PART_OF
- WIKIDATA_PROPERTY:P361
- FMA:part_of
- RXNORM:constitutes
- RXNORM:part_of
narrow_mappings:
- BSPO:0001106
- BSPO:0001108
- BSPO:0001113
- BSPO:0001115
- UBERON_CORE:layer_part_of
- UBERON_CORE:subdivision_of
- UBERON_CORE:trunk_part_of
- CHEBI:is_substituent_group_from
- CPT:panel_element_of
- CPT:panel_element_of_possibly_included
- DRUGBANK:component_of
- FMA:constitutional_part_of
- FMA:member_of
- FMA:regional_part_of
- FMA:related_developmental_entity_of
- LOINC:component_of
- LOINC:has_supersystem
- LOINC:member_of
- LOINC:multipart_of
- MEDDRA:member_of
- MONDO:part_of_progression_of_disease
- NCIT:R82
- NCIT:R27
- NCIT:is_component_of_chemotherapy_regimen
- NDDF:ingredient_of
- RO:0002007
- RO:0002350
- RO:0002376
- RO:0002380
- RO:0002571
- RO:0002572
- RO:0002576
- RXNORM:ingredient_of
- RXNORM:ingredients_of
- RXNORM:precise_ingredient_of
- SNOMED:active_ingredient_of
- SNOMED:basis_of_strength_substance_of
- SNOMED:component_of
- SNOMED:direct_substance_of
- SNOMED:during
- SNOMED:focus_of
- SNOMED:has_dependent
- SNOMED:part_anatomy_structure_of
- SNOMED:precise_active_ingredient_of
- UBERON:subdivision_of
- UMLS:component_of
- UMLS:has_owning_affiliate
- UMLS:owning_subsection_of
- VANDF:ingredient_of
broad_mappings:
- RO:0001018
- FMA:contained_in
- RXNORM:contained_in
rank: 1000
is_a: overlaps
domain: named thing
inherited: true
alias: part_of
inverse: has part
range: named thing
multivalued: true

```
</details></div>