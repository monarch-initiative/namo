---
search:
  boost: 5.0
---

# Slot: diseases_confidence_score 


_A score defined by Jensen Lab Diseases that reports confidence level in an association on a scale of 1-5 stars.  It is based on different inputs for curated knowledge associations vs text-mined associations vs experimental/GWAS based associations, but adjusts/caps scores for these types of knowledge such that they are comparable on a single scale._



<div data-search-exclude markdown="1">



URI: [namo:diseases_confidence_score](https://w3id.org/monarch-initiative/namo/diseases_confidence_score)
Alias: diseases_confidence_score

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | An association between a gene or gene product and a disease, where variation ... |  no  |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease for which the g... |  no  |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | An association between a gene (or gene product) and a disease in which the ge... |  no  |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | An association in which a gene (e |  no  |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | A gene-to-disease association that is asserted on the grounds that the gene h... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md), [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:diseases_confidence_score |
| native | namo:diseases_confidence_score |




## LinkML Source

<details>
```yaml
name: diseases confidence score
description: A score defined by Jensen Lab Diseases that reports confidence level
  in an association on a scale of 1-5 stars.  It is based on different inputs for
  curated knowledge associations vs text-mined associations vs experimental/GWAS based
  associations, but adjusts/caps scores for these types of knowledge such that they
  are comparable on a single scale.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: diseases_confidence_score
domain_of:
- gene to disease association
- correlated gene to disease association
range: float

```
</details></div>