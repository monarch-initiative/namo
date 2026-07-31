---
search:
  boost: 0.5
---

# Slot: phenotype_ontology  <span style="color: red;"><strong> (DEPRECATED) </strong></span> 


_Ontology used for phenotype classification (e.g., HPO, MP)._



<div data-search-exclude markdown="1">



URI: [namo:phenotype_ontology](https://w3id.org/monarch-initiative/namo/phenotype_ontology)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhenotypeOverlap](PhenotypeOverlap.md) | Comparison of phenotypic manifestations between model and biological systems |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PhenotypeOverlap](PhenotypeOverlap.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PhenotypeOverlap](PhenotypeOverlap.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:phenotype_ontology |
| native | namo:phenotype_ontology |




## LinkML Source

<details>
```yaml
name: phenotype_ontology
description: Ontology used for phenotype classification (e.g., HPO, MP).
deprecated: 'Redundant since the three phenotype slots above became `phenotypic feature`
  bound to PhenotypeEnum: the source ontology is now carried by each term''s own CURIE
  prefix (HP:, MP:, ...) rather than declared once as free text. Retained for one
  release so existing data keeps loading; remove in a later cleanup.'
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PhenotypeOverlap
domain_of:
- PhenotypeOverlap
range: string

```
</details></div>