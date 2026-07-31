---
search:
  boost: 5.0
---

# Slot: ingest_date 


_The date on which a dataset version was ingested into the local knowledge graph or downstream data system; a specialization of dct:issued for the ingestion context._



<div data-search-exclude markdown="1">



URI: [namo:ingest_date](https://w3id.org/monarch-initiative/namo/ingest_date)
Alias: ingest_date


## Inheritance

* [node_property](node_property.md)
    * **ingest_date**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetVersion](DatasetVersion.md) | an item that holds version level information about a dataset |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [DatasetVersion](DatasetVersion.md) |
| Domain Of | [DatasetVersion](DatasetVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:ingest_date |
| native | namo:ingest_date |
| broad | dct:issued |




## LinkML Source

<details>
```yaml
name: ingest date
description: The date on which a dataset version was ingested into the local knowledge
  graph or downstream data system; a specialization of dct:issued for the ingestion
  context.
from_schema: https://w3id.org/monarch-initiative/namo
broad_mappings:
- dct:issued
rank: 1000
is_a: node property
domain: dataset version
alias: ingest_date
domain_of:
- dataset version
range: string

```
</details></div>