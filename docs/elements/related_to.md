---
search:
  boost: 5.0
---

# Slot: related_to 


_A relationship that is asserted between two named things_



<div data-search-exclude markdown="1">



URI: [namo:related_to](https://w3id.org/monarch-initiative/namo/related_to)
Alias: related_to


## Inheritance

* **related_to**
    * [related_to_at_concept_level](related_to_at_concept_level.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
    * [disease_has_location](disease_has_location.md)
    * [location_of_disease](location_of_disease.md)
    * [composed_primarily_of](composed_primarily_of.md)
    * [primarily_composed_of](primarily_composed_of.md)








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
| self | namo:related_to |
| native | namo:related_to |
| exact | UMLS:related_to |
| narrow | SEMMEDDB:compared_with, SEMMEDDB:higher_than, SEMMEDDB:lower_than, SEMMEDDB:ADMINISTERED_TO, SEMMEDDB:ASSOCIATED_WITH, BFO:0000054, UBERON_CORE:protects, GOREL:0002005, GOREL:0012006, BTO:related_to, CHEBI:is_conjugate_acid_of, CHEBI:is_conjugate_base_of, CPT:has_add_on_code, CPT:mapped_to, EFO:0006351, FMA:connected_to, FMA:continuous_with, FMA:homonym_of, FMA:related_developmental_entity_of, RO:0002093, RO:0002092, RO:0002084, HCPCS:mapped_to, HMDB:disease, HMDB:has_protein_association, IAO:0000136, LOINC:has_answer, LOINC:has_challenge, LOINC:has_evaluation, LOINC:mapped_to, LOINC:mth_has_expanded_form, MESH:RO, MESH:has_mapping_qualifier, MESH:mapped_to, MONDO:disease_shares_features_of, NCIT:disease_may_have_associated_disease, NCIT:human_disease_maps_to_eo_disease, NCIT:is_abnormal_cell_of_disease, NCIT:is_related_to_endogenous_product, UBERON_NONAMESPACE:connected_to, UBERON_NONAMESPACE:innervated_by, NBO-PROPERTY:is_about, RO:0000053, PATO:reciprocal_of, RO:0000052, RO:0002001, RO:0002002, RO:0002003, RO:0002008, RO:0002134, RO:0002150, RO:0002159, RO:0002176, RO:0002177, RO:0002178, RO:0002179, RO:0002314, RO:0002322, RO:0002328, RO:0002332, RO:0002338, RO:0002339, RO:0002341, RO:0002342, RO:0002344, RO:0002348, RO:0002349, RO:0002356, RO:0002371, RO:0002372, RO:0002373, RO:0002374, RO:0002385, RO:0002387, RO:0002451, RO:0002494, RO:0002495, RO:0002568, RO:0002573, RO:0004026, RO:0004027, RO:0009001, RO:0009004, RXNORM:has_form, RXNORM:reformulated_to, SNOMED:has_associated_morphology, SNOMED:has_associated_procedure, SNOMED:has_direct_morphology, SNOMED:has_disposition, SNOMED:has_indirect_morphology, SNOMED:has_modification, SNOMED:has_procedure_morphology, SNOMED:has_specimen_source_morphology, SNOMED:inheres_in, SNOMED:is_interpreted_by, SNOMED:relative_to_part_of, UBERON:synapsed_by, UMLS:RO, UMLS:RQ, UMLS:class_code_classified_by, UMLS:exhibited_by, UMLS:has_context_binding, UMLS:has_form, UMLS:has_mapping_qualifier, UMLS:larger_than, UMLS:mapped_to, UMLS:owning_section_of |
| broad | owl:topObjectProperty |




## LinkML Source

<details>
```yaml
name: related to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: A relationship that is asserted between two named things
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- UMLS:related_to
narrow_mappings:
- SEMMEDDB:compared_with
- SEMMEDDB:higher_than
- SEMMEDDB:lower_than
- SEMMEDDB:ADMINISTERED_TO
- SEMMEDDB:ASSOCIATED_WITH
- BFO:0000054
- UBERON_CORE:protects
- GOREL:0002005
- GOREL:0012006
- BTO:related_to
- CHEBI:is_conjugate_acid_of
- CHEBI:is_conjugate_base_of
- CPT:has_add_on_code
- CPT:mapped_to
- EFO:0006351
- FMA:connected_to
- FMA:continuous_with
- FMA:homonym_of
- FMA:related_developmental_entity_of
- RO:0002093
- RO:0002092
- RO:0002084
- HCPCS:mapped_to
- HMDB:disease
- HMDB:has_protein_association
- IAO:0000136
- LOINC:has_answer
- LOINC:has_challenge
- LOINC:has_evaluation
- LOINC:mapped_to
- LOINC:mth_has_expanded_form
- MESH:RO
- MESH:has_mapping_qualifier
- MESH:mapped_to
- MONDO:disease_shares_features_of
- NCIT:disease_may_have_associated_disease
- NCIT:human_disease_maps_to_eo_disease
- NCIT:is_abnormal_cell_of_disease
- NCIT:is_related_to_endogenous_product
- UBERON_NONAMESPACE:connected_to
- UBERON_NONAMESPACE:innervated_by
- NBO-PROPERTY:is_about
- RO:0000053
- PATO:reciprocal_of
- RO:0000052
- RO:0002001
- RO:0002002
- RO:0002003
- RO:0002008
- RO:0002134
- RO:0002150
- RO:0002159
- RO:0002176
- RO:0002177
- RO:0002178
- RO:0002179
- RO:0002314
- RO:0002322
- RO:0002328
- RO:0002332
- RO:0002338
- RO:0002339
- RO:0002341
- RO:0002342
- RO:0002344
- RO:0002348
- RO:0002349
- RO:0002356
- RO:0002371
- RO:0002372
- RO:0002373
- RO:0002374
- RO:0002385
- RO:0002387
- RO:0002451
- RO:0002494
- RO:0002495
- RO:0002568
- RO:0002573
- RO:0004026
- RO:0004027
- RO:0009001
- RO:0009004
- RXNORM:has_form
- RXNORM:reformulated_to
- SNOMED:has_associated_morphology
- SNOMED:has_associated_procedure
- SNOMED:has_direct_morphology
- SNOMED:has_disposition
- SNOMED:has_indirect_morphology
- SNOMED:has_modification
- SNOMED:has_procedure_morphology
- SNOMED:has_specimen_source_morphology
- SNOMED:inheres_in
- SNOMED:is_interpreted_by
- SNOMED:relative_to_part_of
- UBERON:synapsed_by
- UMLS:RO
- UMLS:RQ
- UMLS:class_code_classified_by
- UMLS:exhibited_by
- UMLS:has_context_binding
- UMLS:has_form
- UMLS:has_mapping_qualifier
- UMLS:larger_than
- UMLS:mapped_to
- UMLS:owning_section_of
broad_mappings:
- owl:topObjectProperty
rank: 1000
domain: named thing
inherited: true
alias: related_to
symmetric: true
range: named thing
multivalued: true

```
</details></div>