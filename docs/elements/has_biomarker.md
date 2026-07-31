---
search:
  boost: 5.0
---

# Slot: has_biomarker 


_holds between a disease or phenotypic feature and a measurable chemical entity that is used as an indicator of the presence or state of the disease or feature._

_ # metabolite_



<div data-search-exclude markdown="1">



URI: [namo:has_biomarker](https://w3id.org/monarch-initiative/namo/has_biomarker)
Alias: has_biomarker


## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **has_biomarker**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |
| Domain | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) |

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
| Inverse | [biomarker_for](biomarker_for.md) |

</details>







## In Subsets


* [TranslatorMinimal](TranslatorMinimal.md)






## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_biomarker |
| native | namo:has_biomarker |
| narrow | NCIT:disease_has_molecular_abnormality, NCIT:disease_is_marked_by_gene |




## LinkML Source

<details>
```yaml
name: has biomarker
description: "holds between a disease or phenotypic feature and a measurable chemical\
  \ entity that is used as an indicator of the presence or state of the disease or\
  \ feature.\n # metabolite"
in_subset:
- translator_minimal
from_schema: https://w3id.org/monarch-initiative/namo
narrow_mappings:
- NCIT:disease_has_molecular_abnormality
- NCIT:disease_is_marked_by_gene
rank: 1000
is_a: correlated with
domain: disease or phenotypic feature
inherited: true
alias: has_biomarker
inverse: biomarker for
range: chemical entity or gene or gene product
multivalued: true

```
</details></div>