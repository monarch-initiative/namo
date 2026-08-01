---
search:
  boost: 5.0
---

# Slot: pathway_database 


_Source database (e.g., KEGG, Reactome, GO)._



<div data-search-exclude markdown="1">



URI: [namo:pathway_database](https://w3id.org/monarch-initiative/namo/pathway_database)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Pathway](Pathway.md) | A biological pathway with activity and enrichment information |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Pathway](Pathway.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Pathway](Pathway.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:pathway_database |
| native | namo:pathway_database |




## LinkML Source

<details>
```yaml
name: pathway_database
description: Source database (e.g., KEGG, Reactome, GO).
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: Pathway
domain_of:
- Pathway
range: string

```
</details></div>