---
search:
  boost: 5.0
---

# Slot: entrez_id 


_NCBI Entrez gene identifier._



<div data-search-exclude markdown="1">



URI: [namo:entrez_id](https://w3id.org/monarch-initiative/namo/entrez_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Gene](Gene.md) | A gene entity with identifiers and expression information |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Gene](Gene.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Gene](Gene.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:entrez_id |
| native | namo:entrez_id |




## LinkML Source

<details>
```yaml
name: entrez_id
description: NCBI Entrez gene identifier.
from_schema: https://w3id.org/monarch-initiative/namo
rank: 1000
owner: Gene
domain_of:
- Gene
range: integer

```
</details></div>