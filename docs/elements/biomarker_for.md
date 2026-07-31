---
search:
  boost: 5.0
---

# Slot: biomarker_for 


_holds between a measurable chemical entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._



<div data-search-exclude markdown="1">



URI: [namo:biomarker_for](https://w3id.org/monarch-initiative/namo/biomarker_for)
Alias: biomarker_for


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **biomarker_for**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |
| Domain | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |

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
| self | namo:biomarker_for |
| native | namo:biomarker_for |
| exact | NCIT:R39 |
| narrow | NCIT:R47, NCIT:genetic_biomarker_related_to, NCIT:is_molecular_abnormality_of_disease, orphanet:465410 |
| broad | RO:0002607 |




## LinkML Source

<details>
```yaml
name: biomarker for
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: true
description: holds between a measurable chemical entity and a disease or phenotypic
  feature, where the entity is used as an indicator of the presence or state of the
  disease or feature.
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
exact_mappings:
- NCIT:R39
narrow_mappings:
- NCIT:R47
- NCIT:genetic_biomarker_related_to
- NCIT:is_molecular_abnormality_of_disease
- orphanet:465410
broad_mappings:
- RO:0002607
rank: 1000
is_a: correlated with
domain: chemical entity or gene or gene product
inherited: true
alias: biomarker_for
range: disease or phenotypic feature
multivalued: true

```
</details></div>