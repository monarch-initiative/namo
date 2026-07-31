---
search:
  boost: 5.0
---

# Slot: causes 


_holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other_



<div data-search-exclude markdown="1">



URI: [namo:causes](https://w3id.org/monarch-initiative/namo/causes)

## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contributes_to](contributes_to.md)
            * **causes**








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
| self | namo:causes |
| native | namo:causes |
| exact | SEMMEDDB:CAUSES, WIKIDATA_PROPERTY:P1542, SNOMED:cause_of, RO:0003303 |
| narrow | MONDO:disease_triggers, GOREL:0000040, MONDO:disease_causes_feature, NCIT:allele_has_abnormality, NCIT:biological_process_has_result_biological_process, NCIT:chemical_or_drug_has_physiologic_effect, NCIT:chemical_or_drug_initiates_biological_process, NCIT:process_initiates_biological_process, NCIT:chromosome_mapped_to_disease, NCIT:disease_has_normal_tissue_origin, NBO-PROPERTY:in_response_to, orphanet:317343, orphanet:317344, orphanet:317346, orphanet:410295, orphanet:410296, RO:0002256, RO:0002315, RO:0002507, RO:0002509, RO:0004001, SNOMED:causative_agent_of, SNOMED:has_realization, UMLS:has_physiologic_effect |
| broad | RO:0002410, RO:0002506 |




## LinkML Source

<details>
```yaml
name: causes
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between two entities where the occurrence, existence, or activity
  of one causes the occurrence or generation of the other
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- SEMMEDDB:CAUSES
- WIKIDATA_PROPERTY:P1542
- SNOMED:cause_of
- RO:0003303
narrow_mappings:
- MONDO:disease_triggers
- GOREL:0000040
- MONDO:disease_causes_feature
- NCIT:allele_has_abnormality
- NCIT:biological_process_has_result_biological_process
- NCIT:chemical_or_drug_has_physiologic_effect
- NCIT:chemical_or_drug_initiates_biological_process
- NCIT:process_initiates_biological_process
- NCIT:chromosome_mapped_to_disease
- NCIT:disease_has_normal_tissue_origin
- NBO-PROPERTY:in_response_to
- orphanet:317343
- orphanet:317344
- orphanet:317346
- orphanet:410295
- orphanet:410296
- RO:0002256
- RO:0002315
- RO:0002507
- RO:0002509
- RO:0004001
- SNOMED:causative_agent_of
- SNOMED:has_realization
- UMLS:has_physiologic_effect
broad_mappings:
- RO:0002410
- RO:0002506
rank: 1000
is_a: contributes to
domain: named thing
inherited: true
range: named thing
multivalued: true

```
</details></div>