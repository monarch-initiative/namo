---
search:
  boost: 5.0
---

# Slot: gene2phenotype_confidence_category 


_A term used by EBI Gene2Phenotype to describe the confidence that the association is real. GenCC confidence terms are used for different levels of confidence (enum).  See https://www.ebi.ac.uk/gene2phenotype/about/terminology#g2p-confidence-section._



<div data-search-exclude markdown="1">



URI: [namo:gene2phenotype_confidence_category](https://w3id.org/monarch-initiative/namo/gene2phenotype_confidence_category)
Alias: gene2phenotype_confidence_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | An association between a gene or gene product and a disease, where variation ... |  no  |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease in which the ge... |  no  |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | An association in which a gene (e |  no  |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | A gene-to-disease association that is asserted on the grounds that the gene h... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:gene2phenotype_confidence_category |
| native | namo:gene2phenotype_confidence_category |




## LinkML Source

<details>
```yaml
name: gene2phenotype confidence category
description: A term used by EBI Gene2Phenotype to describe the confidence that the
  association is real. GenCC confidence terms are used for different levels of confidence
  (enum).  See https://www.ebi.ac.uk/gene2phenotype/about/terminology#g2p-confidence-section.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: gene2phenotype_confidence_category
domain_of:
- gene to disease association
range: string

```
</details></div>