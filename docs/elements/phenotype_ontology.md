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
deprecated: Redundant now that the phenotype slots are bound to PhenotypeEnum and
  ranged over PhenotypicFeature; the source ontology is carried by the CURIE prefix
  of each phenotype id.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PhenotypeOverlap
domain_of:
- PhenotypeOverlap
range: string

```
</details></div>