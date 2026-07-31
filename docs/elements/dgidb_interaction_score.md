---
search:
  boost: 5.0
---

# Slot: dgidb_interaction_score 


_A score defined by DGIdb that is used to rank interaction record results in DGIdb, which  combines their evidence score  (based on total supporting sources and pubs), with their relative gene specificity score and relative drug specificity score. See https://dgidb.org/about/overview/interaction-score._



<div data-search-exclude markdown="1">



URI: [namo:dgidb_interaction_score](https://w3id.org/monarch-initiative/namo/dgidb_interaction_score)
Alias: dgidb_interaction_score

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes an interaction between a chemical entity and a gene or gene product |  no  |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md), [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:dgidb_interaction_score |
| native | namo:dgidb_interaction_score |




## LinkML Source

<details>
```yaml
name: dgidb interaction score
description: A score defined by DGIdb that is used to rank interaction record results
  in DGIdb, which  combines their evidence score  (based on total supporting sources
  and pubs), with their relative gene specificity score and relative drug specificity
  score. See https://dgidb.org/about/overview/interaction-score.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: dgidb_interaction_score
domain_of:
- chemical gene interaction association
- chemical affects gene association
range: float

```
</details></div>