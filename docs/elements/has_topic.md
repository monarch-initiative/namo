---
search:
  boost: 5.0
---

# Slot: has_topic 


_Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred. See https://github.com/biolink/biolink-model/issues/238_



<div data-search-exclude markdown="1">



URI: [namo:has_topic](https://w3id.org/monarch-initiative/namo/has_topic)
Alias: has_topic


## Inheritance

* [node_property](node_property.md)
    * **has_topic**








## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OntologyClass](OntologyClass.md) |
| Domain | [NamedThing](NamedThing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |







## Aliases


* topic
* descriptors




## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/monarch-initiative/namo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | namo:has_topic |
| native | namo:has_topic |
| exact | foaf:topic |




## LinkML Source

<details>
```yaml
name: has topic
description: Connects a node to a vocabulary term or ontology class that describes
  some aspect of the entity. In general specific characterization is preferred. See
  https://github.com/biolink/biolink-model/issues/238
from_schema: https://w3id.org/monarch-initiative/namo
aliases:
- topic
- descriptors
exact_mappings:
- foaf:topic
rank: 1000
is_a: node property
domain: named thing
alias: has_topic
range: ontology class

```
</details></div>