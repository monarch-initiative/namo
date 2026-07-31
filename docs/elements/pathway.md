---
search:
  boost: 5.0
---

# Slot: pathway 


_The pathway this measurement is about. Identifier prefixes follow Biolink's `pathway` (REACT, KEGG, GO, ...), which replaces the former pathway_database / pathway_id attributes._



<div data-search-exclude markdown="1">



URI: [namo:pathway](https://w3id.org/monarch-initiative/namo/pathway)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PathwayActivityResult](PathwayActivityResult.md) | An activity and enrichment measurement for a single biological pathway |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Pathway](Pathway.md) |
| Domain Of | [PathwayActivityResult](PathwayActivityResult.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PathwayActivityResult](PathwayActivityResult.md) |




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PathwayActivityResult](PathwayActivityResult.md) | [Pathway](Pathway.md) | range | [Pathway](Pathway.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object](object.md) | range | [Pathway](Pathway.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object](object.md) | range | [Pathway](Pathway.md) |
| [ChemicalEntityToPathwayAssociation](ChemicalEntityToPathwayAssociation.md) | [object](object.md) | range | [Pathway](Pathway.md) |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:Pathway |
| native | namo:Pathway |
| exact | PW:0000001, WIKIDATA:Q4915012 |
| narrow | SIO:010526, GO:0007165 |




## LinkML Source

<details>
```yaml
name: pathway
description: The pathway this measurement is about. Identifier prefixes follow Biolink's
  `pathway` (REACT, KEGG, GO, ...), which replaces the former pathway_database / pathway_id
  attributes.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: PathwayActivityResult
domain_of:
- PathwayActivityResult
range: pathway
inlined: true

```
</details></div>