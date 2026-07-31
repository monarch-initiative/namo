---
search:
  boost: 5.0
---

# Slot: dgidb_evidence_score 


_A score defined by DGIdb that is used to report the amount of evidence supporting a given interaction statement, which is simply the sum of all supporting sources and publications. See https://dgidb.org/about/overview/interaction-score._



<div data-search-exclude markdown="1">



URI: [namo:dgidb_evidence_score](https://w3id.org/monarch-initiative/namo/dgidb_evidence_score)
Alias: dgidb_evidence_score

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
| Range | [Integer](Integer.md) |
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
| self | namo:dgidb_evidence_score |
| native | namo:dgidb_evidence_score |




## LinkML Source

<details>
```yaml
name: dgidb evidence score
description: A score defined by DGIdb that is used to report the amount of evidence
  supporting a given interaction statement, which is simply the sum of all supporting
  sources and publications. See https://dgidb.org/about/overview/interaction-score.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
alias: dgidb_evidence_score
domain_of:
- chemical gene interaction association
- chemical affects gene association
range: integer

```
</details></div>